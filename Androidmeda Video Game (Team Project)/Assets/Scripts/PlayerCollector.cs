//Karan Bhasin

using UnityEngine;

public class PlayerCollector : MonoBehaviour
{
    private AudioSource playerCollectorSource;

    public bool hasKey = false;
    public AudioClip keyCollectSound;

    public AudioClip healthPackCollectSound;

    public bool hasPass = false;
    public AudioClip passCollectSound;

    private void Awake()
    {
        playerCollectorSource = GetComponent<AudioSource>();
        
        if (playerCollectorSource == null)
        {
            Debug.LogError("Missing AudioSource for Key");
        }
        if (keyCollectSound == null)
        {
            Debug.LogError("Missing Audio clip for Key");
        }
        
        if (healthPackCollectSound == null)
        {
            Debug.LogError("Missing Audio clip for Health Pack");
        }
        

        if (passCollectSound == null)
        {
            Debug.LogError("Missing Audio clip for Security Pass");
        }

    }

    public void ReceiveKey()
    {
        playerCollectorSource.clip = keyCollectSound;
        playerCollectorSource.Play();
        hasKey = true;
    }

    public void ReceiveHealthPack()
    {
        playerCollectorSource.clip = healthPackCollectSound;
        playerCollectorSource.Play();
    }

    public void ReceivePass()
    {
        playerCollectorSource.clip = passCollectSound;
        playerCollectorSource.Play();
        hasPass = true;
    }
}

