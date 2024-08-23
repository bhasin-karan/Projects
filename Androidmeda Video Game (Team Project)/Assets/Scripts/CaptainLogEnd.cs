//Karan Bhasin

using System.Collections;
using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class CaptainLogEnd : MonoBehaviour
{

    private TMP_Text logText;
    private string captainLogEndText = "CAPTAIN'S LOG - STARDATE 4217.2\nSuccess! Our plan to escape has triumphed. The droid, under the guidance of our adept new technician, has freed us from the confines of the bridge. We've made it to the escape pods and have now set a course for the nearest Alliance planet. Against all odds, our final hope has prevailed.";
    public float typeSpeed;
    private bool skiptoEnd;


    private void Awake()
    {
        logText = GetComponent<TMP_Text>();
        if (logText == null)
        {
            Debug.LogError("No TMP_Text Component found");
        }
        skiptoEnd = false;
    }


    void Start()
    {
        StartCoroutine(LogType());
    }

    IEnumerator LogType()
    {
        var waitTime = new WaitForSeconds(typeSpeed);
        foreach (char letter in captainLogEndText)
        {
            logText.text += letter;
            yield return waitTime;
        }
        yield return new WaitForSeconds(3f);
        SceneManager.LoadScene("Credits");
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space) && !skiptoEnd)
        {
            skiptoEnd = true;
            StopAllCoroutines();
            StartCoroutine(SkipEndLog());
            
        }
    }

    IEnumerator SkipEndLog()
    {
        logText.text = captainLogEndText;
        yield return new WaitForSeconds(3f);
        SceneManager.LoadScene("Credits");
    }

}
