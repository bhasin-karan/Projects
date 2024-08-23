//Karan Bhasin

using UnityEngine;
using System.Collections;

public class KeyLockedDoor : MonoBehaviour
{
    private Animator anim;
    public GameObject[] lights;
    public Material unlockcolor;
    public AudioClip keyUnlockClip;
    public AudioClip getKeyClip;
    public AudioClip doorOpenClip;
    private AudioSource doorSound;
    public bool doorOpen;

    void Awake()
    {
        anim = GetComponent<Animator>();
        doorSound = GetComponent<AudioSource>();
        doorOpen = false;

        if (anim == null)
        {
            Debug.LogError("Animator could not be found for Key Locked Doors");
        }
        if (doorOpenClip == null)
        {
            Debug.LogError("No Door Open Audio Clip assigned for Key Locked Doors");
        }
        if (keyUnlockClip == null)
        {
            Debug.LogError("No Key Unlock Audio Clip assigned for Key Locked Doors");
        }
        if (getKeyClip == null)
        {
            Debug.LogError("No Get Key Audio Clip assigned for Key Locked Doors");
        }
        if (doorSound == null)
        {
            Debug.LogError("Missing AudioSource for Key Locked Doors");
        }
        if (unlockcolor == null)
        {
            Debug.LogError("No Unlock Color Material assigned for Key Locked Doors");
        }
        if (lights.Length == 0)
        {
            Debug.LogError("No lights array assigned for Key Locked Doors");
        }
    }

    private void Start()
    {
        if (anim.GetBool("character_nearby"))
        {
            doorOpen = true;
            foreach (GameObject light in lights)
            {
                if (light != null)
                {
                    Renderer renderer = light.GetComponent<Renderer>();
                    Material[] materials = renderer.materials;
                    materials[1] = unlockcolor;
                    renderer.materials = materials;
                }
                else
                {
                    Debug.LogError("Light not assigned for Key Locked Doors");
                }
            }
        }
    }

    private void OnTriggerEnter(Collider c)
    {
        if (c.CompareTag("Player") && doorOpen == false)
        {
            PlayerCollector pc = c.gameObject.GetComponent<PlayerCollector>();
            if (pc != null && pc.hasKey)
            {
                StartCoroutine(UnlockDoor());
                doorOpen = true;
                pc.hasKey = false;
            }
            else
            {
                Debug.Log("Find the key!");
                doorSound.clip = getKeyClip;
                doorSound.Play();
            }
        }
    }

    IEnumerator UnlockDoor()
    {
        doorSound.clip = keyUnlockClip;
        doorSound.Play();

        foreach (GameObject light in lights)
        {
            if (light != null)
            {
                Renderer renderer = light.GetComponent<Renderer>();
                Material[] materials = renderer.materials;
                materials[1] = unlockcolor;
                renderer.materials = materials;
            }
            else
            {
                Debug.LogError("Light not assigned for Key Locked Doors");
            }
        }

        yield return new WaitForSeconds(0.2f);

        anim.SetBool("character_nearby", true);
        doorSound.clip = doorOpenClip;
        doorSound.Play();
    }

}

