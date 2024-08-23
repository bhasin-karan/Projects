//Karan Bhasin

using System.Collections;
using UnityEngine;

public class HealthPackGlassBox : MonoBehaviour
{
    public GameObject brokenGlass;
    public Transform healthPackObject;
    private AudioSource glassBoxBreak;
    

    void Awake()
    {
       glassBoxBreak = GetComponent<AudioSource>();
        if (glassBoxBreak == null)
        {
            Debug.LogError("Missing AudioSource for Glass Box");
        }
        if (brokenGlass == null)
        {
            Debug.LogError("Missing Broken Glass for Glass Box");
        }
        if (healthPackObject == null)
        {
            Debug.LogError("Missing Health Pack for Glass Box");
        }
    }

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.tag == "Ground")
        {
            StartCoroutine(DestroyAfterSound());
            
        }
    }

    IEnumerator DestroyAfterSound()
    {
        glassBoxBreak.Play();

        if (healthPackObject != null)
        {
            healthPackObject.SetParent(null);
        }

        if (brokenGlass != null)
        {
            Instantiate(brokenGlass, transform.position, Quaternion.identity);
        }

        GetComponent<MeshRenderer>().enabled = false;

        yield return new WaitForSeconds(0.4f);
        
        Destroy(gameObject);

    }
}
