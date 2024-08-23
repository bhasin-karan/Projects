// Authored by: Alok Agrawal
// Team: AxKRA Studios

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

[RequireComponent(typeof(NavMeshAgent))]
[RequireComponent(typeof(AudioSource))]
public class SentryChase : MonoBehaviour
{
    private NavMeshAgent sentrypathfinder;
    private GameObject player;
    AudioSource audioData;
    // Start is called before the first frame update
    void Start()
    {
        sentrypathfinder = GetComponent<NavMeshAgent>();
        // player = GameObject.FindGameObjectWithTag("Player");
        player = GameObject.Find("Droid");
        audioData = GetComponent<AudioSource>();
        
    }

    // Update is called once per frame
    void Update()
    {
        sentrypathfinder.SetDestination(player.transform.position);
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.GetComponent<ThirdPersonControl>() != null)
        {
            player.GetComponent<HealthRespawnManager>().CauseDamage();

            audioData.Play(0);

        }
    }
}
