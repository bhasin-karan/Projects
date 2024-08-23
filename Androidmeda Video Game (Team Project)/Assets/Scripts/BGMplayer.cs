// Authored by: Alok Agrawal
// Team: AxKRA Studios

using UnityEngine;

public class BGMplayer : MonoBehaviour
{

    [SerializeField]
    private AudioClip[] bgmClips;

    private AudioSource audioSource;

    private void Awake()
    {
        audioSource = GetComponent<AudioSource>();
        
    }

    private void Start()
    {
        audioSource.clip = GetRandomBgmClip();
        audioSource.loop = true;
        audioSource.Play();
    }

    private void Update()
    {
        if (!audioSource.isPlaying)
        {
            audioSource.clip = GetRandomBgmClip();
            audioSource.loop = true;
            audioSource.Play();
        }
    }
    private AudioClip GetRandomBgmClip()
    {
        return bgmClips[UnityEngine.Random.Range(0, bgmClips.Length)];
    }

}