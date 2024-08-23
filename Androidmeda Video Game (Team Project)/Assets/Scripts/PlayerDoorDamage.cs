// Authored by: Alok Agrawal
// Team: AxKRA Studios

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerDoorDamage : MonoBehaviour
{

    private int collisionTimer = 0;
    private GameObject player;
    
    void Awake()
    {
        player = GameObject.Find("Droid");
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnTriggerStay(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            collisionTimer++;
            if (collisionTimer > 30)
            {
                player.GetComponent<HealthRespawnManager>().CauseDamage();
                Debug.Log("collisionTimer: " + collisionTimer);
            }
        }
    }

    void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {            
            collisionTimer = 0;
        }
    }
}
