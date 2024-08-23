//Karan Bhasin

using UnityEngine;

public class ProximityDoor : MonoBehaviour
{
    private Animator anim;
    public AudioClip doorOpenClip;
    public AudioClip doorCloseClip;
    private AudioSource doorSound;

    void Awake()
    {
        anim = GetComponent<Animator>();
        doorSound = GetComponent<AudioSource>();

        if (anim == null)
        {
            Debug.LogError("Animator could not be found for Proximity Doors");
        }
        if (doorOpenClip == null)
        {
            Debug.LogError("No Door Open Audio Clip assigned for Proximity Doors");
        }
        if (doorCloseClip == null)
        {
            Debug.LogError("No Door Close Audio Clip assigned for Proximity Doors");
        }
        if (doorSound == null)
        {
            Debug.LogError("Missing AudioSource for Proximity Doors");
        }
    }

    private void OnTriggerEnter(Collider c)
    {
        if (c.CompareTag("Player"))
        {
            anim.SetBool("character_nearby", true);
            doorSound.clip = doorOpenClip;
            doorSound.Play();
        }
    }

    private void OnTriggerExit(Collider c)
    {
        if (c.CompareTag("Player"))
        {
            anim.SetBool("character_nearby", false);
            doorSound.clip = doorCloseClip;
            doorSound.Play();
        }
    }
}

