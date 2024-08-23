package com.example.sirenalert;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;

import androidx.activity.EdgeToEdge;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.jjoe64.graphview.GraphView;
public class Graph extends AppCompatActivity {
    private GraphView soundGraph;

    private Button backToMainButtonID;

    private final SirenDetector sirenDetector;

    public Graph(SirenDetector sirenDetector) {
        this.sirenDetector = sirenDetector;
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.visualize_page);

        soundGraph = (GraphView) findViewById(R.id.graph);
        backToMainButtonID = findViewById(R.id.toMainPage);

        backToMainButtonID.setOnClickListener(view -> {

            Intent intent = new Intent(Graph.this, MainActivity.class);
            startActivity(intent);
        });
    }

    //protected void visualizeGraph() {
        //soundGraph.addSeries(sirenDetector.soundSeriesFreq);}
}
