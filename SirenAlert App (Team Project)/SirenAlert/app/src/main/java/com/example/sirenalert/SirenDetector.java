package com.example.sirenalert;

import android.content.pm.PackageManager;
import android.media.AudioFormat;
import android.media.AudioRecord;
import android.media.MediaRecorder;
import android.util.Log;
import android.widget.Toast;

import androidx.core.app.ActivityCompat;
import androidx.core.util.Pair;

import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;

import org.jtransforms.fft.DoubleFFT_1D;

import java.util.Stack;

import java.util.Arrays;

public class SirenDetector {
    // https://developer.android.com/ndk/guides/audio/sampling-audio
    private static final int SAMPLE_RATE = 44100;
    private static final int BUFFER_SIZE = 1024;

    // https://stackoverflow.com/questions/11862662
    private AudioRecord recorder;
    private boolean isRecording = false;
    private final MainActivity mainActivity;

    Stack<Boolean> targets;
    int lowFreq = 600;
    int highFreq = 1400;
    double error = .1;
    int cyclesForDetect = 2;


    // Configuration for recording settings
    // https://developer.android.com/reference/android/media/AudioFormat#CHANNEL_IN_MONO
    private final int CHANNEL_TYPE = AudioFormat.CHANNEL_IN_MONO;
    private final int AUDIO_SOURCE = MediaRecorder.AudioSource.MIC;
    private final int ENCODING = AudioFormat.ENCODING_PCM_16BIT;

    //To help visualize sound
    //LineGraphSeries<DataPoint> soundSeriesFreq;
    //LineGraphSeries<DataPoint> soundSeriesAmp;
    //int xCount;

    // Constructor
    public SirenDetector(MainActivity mainActivity) {
        this.mainActivity = mainActivity;
        targets = new Stack<>();
    }

    // Start recording
    public void startRecording() {
        // https://developer.android.com/reference/android/media/AudioRecord#getMinBufferSize(int,%20int,%20int)
        // https://developer.android.com/reference/android/media/AudioFormat#ENCODING_PCM_16BIT
        int bufferSize = AudioRecord.getMinBufferSize(SAMPLE_RATE, CHANNEL_TYPE, ENCODING);

        // Check if the necessary permissions (microphone) are granted
        if (ActivityCompat.checkSelfPermission(mainActivity, android.Manifest.permission.RECORD_AUDIO) != PackageManager.PERMISSION_GRANTED) {
            // TODO: Consider calling
            //    ActivityCompat#requestPermissions
            // here to request the missing permissions, and then overriding
            //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
            //                                          int[] grantResults)
            // to handle the case where the user grants the permission. See the documentation
            // for ActivityCompat#requestPermissions for more details.
            return;
        }
        else
        {
            // https://developer.android.com/reference/android/media/MediaRecorder.AudioSource#MIC
            recorder = new AudioRecord(AUDIO_SOURCE, SAMPLE_RATE, CHANNEL_TYPE, ENCODING, bufferSize);
        }

        //To help visualize sound
        //soundSeriesFreq = new LineGraphSeries<>();
        //soundSeriesAmp = new LineGraphSeries<>();
        //xCount = 0;

        // Start recording
        recorder.startRecording();
        isRecording = true;

        // Start a new thread to continuously process the audio buffer
        new Thread(this::processAudioBuffer).start();
    }

    // Stop recording
    public void stopRecording()
    {
        // Stop the recorder if it exists
        if (recorder != null)
        {
            // https://developer.android.com/reference/android/media/MediaRecorder
            recorder.stop();
            recorder.release();
            recorder = null;
            isRecording = false;
        }
    }

    // Get frequency and amplitude
    private Pair<Double, Double> getFrequencyFromAmplitudeFFT(short[] buffer, int read)
    {
        // Return if no data
        if (read == 0)
        {
            return new Pair<>(0.0, 0.0);
        }

        // Create double buffer
        double[] doubleBuffer = new double[read];
        // Normalize values to between -1 and 1 and apply Hann window
        for (int i = 0; i < read; i++)
        {
            // https://mathworks.com/help/signal/ref/hann.html
            double hann = 0.5 * (1 - Math.cos(2 * Math.PI * i / (read - 1)));
            doubleBuffer[i] = (double) buffer[i] / Short.MAX_VALUE * hann;
        }
        // FFT to frequency domain
        DoubleFFT_1D fft = new DoubleFFT_1D(read);
        fft.realForward(doubleBuffer);

        // Get the amplitude
        double[] amplitude = new double[read / 2];
        for (int i = 0; i < amplitude.length; i++) {
            double real = doubleBuffer[2 * i];
            double imaginary = doubleBuffer[2 * i + 1];
            amplitude[i] = Math.sqrt(real * real + imaginary * imaginary);
        }

        // Determine frequency resolution from the sample rate
        double resolution = (double) SAMPLE_RATE / read;

        // Find max frequency and amplitude
        double maxAmplitude = -1;
        double maxFrequency = 0;
        for (int i = 0; i < amplitude.length; i++) {
            if (amplitude[i] > maxAmplitude) {
                maxAmplitude = amplitude[i];
                maxFrequency = i * resolution;
            }
        }
        // Return frequency and amplitude
        return new Pair<>(maxFrequency, maxAmplitude);
    }

    // TODO: Add siren detection logic, return true/false depending on siren presence
    private boolean detectSiren(short[] buffer, int read)
    {
        // Get frequency and amplitude
        Pair<Double, Double> frequencyAmplitude = getFrequencyFromAmplitudeFFT(buffer, read);

        // Debug log the values
        Log.d(Double.toString(frequencyAmplitude.first), "frequency");
        Log.d(Double.toString(frequencyAmplitude.second), "amplitude");
        Log.d(Double.toString(targets.size()), "targets size");

        //Right now a percentage for the buffer
        double lowBuffer = lowFreq * error;
        double highBuffer = highFreq * error;
        double freq = frequencyAmplitude.first;
        //Nothing in stack
        if (targets.isEmpty()) {
            if (freq >= highFreq - highBuffer && freq <= highFreq + highBuffer) {
                //High value
                targets.add(true);
            } else if (freq >= lowFreq - lowBuffer && freq <= lowFreq + lowBuffer) {
                //Low value
                targets.add(false);
            }
        } else {
            if (freq >= highFreq - highBuffer && freq <= highFreq + highBuffer && !targets.peek()) {
                //High value
                targets.add(true);
            } else if (freq >= lowFreq - lowBuffer && freq <= lowFreq + lowBuffer && targets.peek()) {
                //Low value
                targets.add(false);
            }

            return targets.size() == cyclesForDetect * 2;
        }

        //soundSeriesFreq.appendData(new DataPoint(xCount, frequencyAmplitude.first), true, BUFFER_SIZE);
        //soundSeriesAmp.appendData(new DataPoint(xCount, frequencyAmplitude.second), true, BUFFER_SIZE);
        return false;
    }

    // Detect the siren
    private void processAudioBuffer()
    {
        short[] soundBuffer = new short[BUFFER_SIZE];

        while(isRecording)
        {
            int read = recorder.read(soundBuffer, 0, soundBuffer.length);
            if (read > 0)
            {
                // Determine if a siren has been detected
                boolean sirenDetected = detectSiren(soundBuffer, read);

                // If a siren has been detected, alert the main thread at mainActivity
                if (sirenDetected)
                {
                    mainActivity.onSirenDetected();
                    targets.clear();
                }
            }

        }
    }
}

