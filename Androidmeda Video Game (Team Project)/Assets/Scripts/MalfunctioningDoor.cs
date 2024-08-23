//Karan Bhasin

using UnityEngine;

public class MalfunctioningDoor : MonoBehaviour
{
    public ParticleSystem malfunctioningSpark1;
    public ParticleSystem malfunctioningSpark2;
    public ParticleSystem malfunctioningSpark3;
    public ParticleSystem malfunctioningSpark4;
    private AudioSource malSound;

    void Awake()
    {
        malSound = GetComponent<AudioSource>();

        if (malSound == null)
        {
            Debug.LogError("Missing AudioSource for Malfunctioning Door");
        }
        if (malfunctioningSpark1 == null)
        {
            Debug.LogError("No Malfunctioning Spark 1 assigned for Malfunctioning Door");
        }
        if (malfunctioningSpark2 == null)
        {
            Debug.LogError("No Malfunctioning Spark 2 assigned for Malfunctioning Door");
        }
        if (malfunctioningSpark3 == null)
        {
            Debug.LogError("No Malfunctioning Spark 1 assigned for Malfunctioning Door");
        }
        if (malfunctioningSpark4 == null)
        {
            Debug.LogError("No Malfunctioning Spark 2 assigned for Malfunctioning Door");
        }
    }

    public void TriggerSparks()
    {
            malfunctioningSpark1.Play();
            malfunctioningSpark2.Play();
            malfunctioningSpark3.Play();
            malfunctioningSpark4.Play();
            malSound.Play();
    }
}