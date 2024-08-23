package com.example.sirenalert;
import android.content.Intent;
import android.os.Bundle;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.Manifest;
import android.content.pm.PackageManager;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
//Referenced code from https://www.geeksforgeeks.org/android-how-to-request-permissions-in-android-application/

public class Permissions extends AppCompatActivity {

    private Button permissionsBackHomeButtonID;

    private RadioButton microphoneButtonID;
    private RadioButton notificationsButtonID;

    private static final int MIC_CODE = 100;
    private static final int NOTIFICATIONS_CODE = 101;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.permissions_page);


        permissionsBackHomeButtonID = findViewById(R.id.permissionsBackHomeButtonID);
        microphoneButtonID = findViewById(R.id.microphoneButtonID);
        notificationsButtonID = findViewById(R.id.notificationsButtonID);



        microphoneButtonID.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                checkPermission(Manifest.permission.RECORD_AUDIO, MIC_CODE);
            }
        });

        notificationsButtonID.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                checkPermission(Manifest.permission.POST_NOTIFICATIONS, NOTIFICATIONS_CODE);
            }
        });

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO) == PackageManager.PERMISSION_GRANTED) {
            microphoneButtonID.setChecked(true);
        } else {
            microphoneButtonID.setChecked(false);
        }

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED) {
            notificationsButtonID.setChecked(true);
        } else {
            notificationsButtonID.setChecked(false);
        }

        permissionsBackHomeButtonID.setOnClickListener(view -> {

            Intent intent = new Intent(Permissions.this, MainActivity.class);
            startActivity(intent);
        });
        }



    public void checkPermission(String permission, int requestCode){
        if (ContextCompat.checkSelfPermission(Permissions.this, permission) == PackageManager.PERMISSION_DENIED) {
            ActivityCompat.requestPermissions(Permissions.this, new String[]{permission}, requestCode);
        } else {
            Toast.makeText(Permissions.this, "Permission already granted", Toast.LENGTH_SHORT).show();
        }
    }


    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults)
    {
        super.onRequestPermissionsResult(requestCode,
                permissions,
                grantResults);

        if (requestCode == MIC_CODE) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                Toast.makeText(Permissions.this, "Microphone Permission Granted", Toast.LENGTH_SHORT) .show();
            }
            else {
                Toast.makeText(Permissions.this, "Microphone Permission Denied", Toast.LENGTH_SHORT) .show();
            }
        }
        else if (requestCode == NOTIFICATIONS_CODE) {
            if (grantResults.length > 0
                    && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                Toast.makeText(Permissions.this, "Notifications Permission Granted", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(Permissions.this, "Notifications Permission Denied", Toast.LENGTH_SHORT).show();
            }
        }
    }
}
//Referenced code from https://www.geeksforgeeks.org/android-how-to-request-permissions-in-android-application/