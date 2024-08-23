// Xun Liu

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LivesCount : MonoBehaviour
{
    public GameObject[] lives;
    private int currentBot;
    public HealthRespawnManager healthRespawnManager;

    // Start is called before the first frame update
    void Start()
    {
        currentBot = lives.Length - 1;
    }


    // Update is called once per frame
    void Update()
    {
        if (currentBot >= healthRespawnManager.GetCurrentLives())
        {
            LoseOneLife();
        }
    }

    public void LoseOneLife()
    {
        if (currentBot >= 0)
        {
            lives[currentBot].SetActive(false);
            currentBot -= 1;
        }
    }
}
