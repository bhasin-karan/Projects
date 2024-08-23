// Authored by: Alok Agrawal
// Team: AxKRA Studios

using UnityEngine;

public class FootSteps : MonoBehaviour
{
    // [SerializeField]
    // private AudioClip[] walkstepClips;

    [SerializeField]
    private AudioClip[] runstepClips;

    private AudioSource audioSource;

    private void Awake()
    {
        audioSource = GetComponent<AudioSource>();
        
    }

    private void runstep()
    {
        AudioClip clip = GetRandomRunClip();
        audioSource.PlayOneShot(clip);
    }


    private AudioClip GetRandomRunClip()
    {
        return runstepClips[UnityEngine.Random.Range(0, runstepClips.Length)];
    }

}