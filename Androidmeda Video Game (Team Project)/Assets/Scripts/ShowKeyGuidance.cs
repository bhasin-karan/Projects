using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShowKeyGuidance : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        GameObject droid = GameObject.FindGameObjectWithTag("Player");
        if (!droid.GetComponent<PlayerCollector>().hasPass)
        {
            EventManager.TriggerEvent<KeyGuidanceAppearanceEvent>();
        }
    }
}