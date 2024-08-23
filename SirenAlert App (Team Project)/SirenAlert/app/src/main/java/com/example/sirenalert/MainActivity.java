package com.example.sirenalert;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import android.widget.Button;
import android.widget.Toast;
import android.widget.TextView;

import com.jjoe64.graphview.GraphView;

public class MainActivity extends AppCompatActivity {


    private Button mainPermissionsButtonID;
    private Button mainHearSirenButtonID;
    private SirenDetector sirenDetector;
    private TextView permWarningTextID;

    //private Graph graph;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        mainPermissionsButtonID = findViewById(R.id.mainPermissionsButtonID);
        mainHearSirenButtonID = findViewById(R.id.mainHearSirenButtonID);
        permWarningTextID = findViewById(R.id.permWarningTextID);

        mainPermissionsButtonID.setOnClickListener(view -> {

            Intent intent = new Intent(MainActivity.this, Permissions.class);
            startActivity(intent);
        });

        mainHearSirenButtonID.setOnClickListener(view -> {

            Intent intent = new Intent(MainActivity.this, Alerts.class);
            startActivity(intent);
        });

        //Referenced https://www.educative.io/answers/what-is-android-visibility
        boolean micPerm = ContextCompat.checkSelfPermission(this, android.Manifest.permission.RECORD_AUDIO) == PackageManager.PERMISSION_GRANTED;
        boolean notifPerm = ContextCompat.checkSelfPermission(this, Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED;
        if (micPerm && notifPerm){
            permWarningTextID.setVisibility(TextView.INVISIBLE);
        } else {
            permWarningTextID.setVisibility(TextView.VISIBLE);
        }
        //Referenced https://www.educative.io/answers/what-is-android-visibility

        // Get a siren detector
        sirenDetector = new SirenDetector(this);
        //graph = new Graph(sirenDetector);
    }

    // https://developer.android.com/guide/components/activities/activity-lifecycle#onresume
    protected void onResume() {
        // Start recording and siren processing
        super.onResume();
        // Start recording if we have permission
        if (checkRequiredPermissions())
        {
            sirenDetector.startRecording();
        }
        // Otherwise request permission or error
        {
            // TODO: Request permission or throw an error?
        }
    }

    // https://developer.android.com/guide/components/activities/activity-lifecycle#onpause
    protected void onPause() {
        // Stop recording and siren processing
        super.onPause();
        sirenDetector.stopRecording();
        //Intent intent = new Intent(MainActivity.this, Graph.class);
        //startActivity(intent);
    }

    // Function is called when a siren is detected
    // TODO: Plug into alerting system
    public void onSirenDetected() {
        runOnUiThread(() -> {
            Toast.makeText(this, "*** SIREN DETECTED ***", Toast.LENGTH_SHORT).show();
        });

        startActivity(new Intent(MainActivity.this, Alerts.class));
    }

    // Check if we have the required permissions
    private boolean checkRequiredPermissions() {
        int result = ContextCompat.checkSelfPermission(this, android.Manifest.permission.RECORD_AUDIO);
        // Return true if permission granted
        return result == android.content.pm.PackageManager.PERMISSION_GRANTED;
    }
}