//Karan Bhasin

using UnityEngine;
using System.Collections;

public class SecurityGate : MonoBehaviour
{
    private Animator anim;
    public GameObject[] gateLights;
    public Material gateUnlockColor;
    public AudioClip passUnlockClip;
    public AudioClip getPassClip;
    public AudioClip gateOpenClip;
    private AudioSource gateSound;
    private bool gateOpen;

    void Awake()
    {
        anim = GetComponent<Animator>();
        gateSound = GetComponent<AudioSource>();
        gateOpen = false;

        if (anim == null)
        {
            Debug.LogError("Animator could not be found for Security Gate");
        }
        if (gateOpenClip == null)
        {
            Debug.LogError("No Door Open Audio Clip assigned for Security Gate");
        }
        if (passUnlockClip == null)
        {
            Debug.LogError("No Key Unlock Audio Clip assigned for Security Gate");
        }
        if (getPassClip == null)
        {
            Debug.LogError("No Get Key Audio Clip assigned for Security Gate");
        }
        if (gateSound == null)
        {
            Debug.LogError("Missing AudioSource for Security Gate");
        }
        if (gateUnlockColor == null)
        {
            Debug.LogError("No Unlock Color Material assigned for Security Gate");
        }
        if (gateLights.Length == 0)
        {
            Debug.LogError("No lights array assigned for Security Gate");
        }
    }

    private void OnTriggerEnter(Collider c)
    {
        if (c.CompareTag("Player") && gateOpen == false)
        {
            PlayerCollector pc = c.gameObject.GetComponent<PlayerCollector>();
            if (pc != null && pc.hasPass)
            {
                StartCoroutine(UnlockDoor());
                gateOpen = true;
                pc.hasPass = false;
            }
            else
            {
                Debug.Log("Find the pass for the security gate!");
                gateSound.clip = getPassClip;
                gateSound.Play();
            }
        }
    }

    IEnumerator UnlockDoor()
    {
        gateSound.clip = passUnlockClip;
        gateSound.Play();

        foreach (GameObject light in gateLights)
        {
            if (light != null)
            {
                Renderer renderer = light.GetComponent<Renderer>();
                Material[] materials = renderer.materials;
                materials[1] = gateUnlockColor;
                renderer.materials = materials;
            }
            else
            {
                Debug.LogError("Light not assigned for Security Gate");
            }
        }

        yield return new WaitForSeconds(1f);

        anim.SetBool("character_nearby", true);
        gateSound.clip = gateOpenClip;
        gateSound.Play();
    }

}

