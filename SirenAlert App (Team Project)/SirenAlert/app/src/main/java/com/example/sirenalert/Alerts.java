package com.example.sirenalert;

import android.content.Intent;
import android.os.Bundle;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import android.widget.Button;
import android.os.Vibrator;
import android.os.VibratorManager;
import android.os.VibrationEffect;
import android.media.MediaPlayer;
import android.util.Log;

public class Alerts extends AppCompatActivity {


    private Button alertThanksButtonID;
    private Button alertWrongDetectionButtonID;
    private Button alertPermissionsButtonID;
    private Vibrator hapticAlert;
    private MediaPlayer audioAlert;
    private VibrationEffect hapticEffect;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.alert_page);

        //Referenced https://developer.android.com/reference/android/media/MediaPlayer
        //https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects

        long[] timings = new long[] { 50, 50, 100, 50, 50 };
        int[] amplitudes = new int[] { 64, 128, 255, 128, 64 };
        int repeat = 1;
        hapticAlert = this.getSystemService(Vibrator.class);
        hapticEffect = VibrationEffect.createWaveform(timings, amplitudes, repeat);
        hapticAlert.vibrate(hapticEffect);

        audioAlert = MediaPlayer.create(this, R.raw.app_alert_tone_011);
        audioAlert.start();
        audioAlert.setLooping(true);

        alertThanksButtonID = findViewById(R.id.alertThanksButtonID);
        alertWrongDetectionButtonID = findViewById(R.id.alertWrongDetectionButtonID);
        alertPermissionsButtonID = findViewById(R.id.alertPermissionsButtonID);


        alertThanksButtonID.setOnClickListener(view -> {
            hapticAlert.cancel();
            audioAlert.stop();
            Intent intent = new Intent(Alerts.this, MainActivity.class);
            startActivity(intent);
        });

        alertWrongDetectionButtonID.setOnClickListener(view -> {
            hapticAlert.cancel();
            audioAlert.stop();
            Intent intent = new Intent(Alerts.this, MainActivity.class);
            startActivity(intent);
        });

        alertPermissionsButtonID.setOnClickListener(view -> {
            hapticAlert.cancel();
            audioAlert.stop();
            Intent intent = new Intent(Alerts.this, Permissions.class);
            startActivity(intent);
        });
        //Referenced https://developer.android.com/reference/android/media/MediaPlayer
        //https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects
    }

}