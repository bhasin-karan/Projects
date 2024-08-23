//Karan Bhasin

using System.Collections;
using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class CaptainLogGameOver : MonoBehaviour
{

    private TMP_Text logText;
    private string captainLogGOText = "CAPTAIN'S LOG - STARDATE 4218.7\nAlas! All our efforts have failed. There is no more hope. We are prisoners of our fates, adrift in the void. \n\n\n\n GAME OVER";
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
        foreach (char letter in captainLogGOText)
        {
            logText.text += letter;
            yield return waitTime;
        }
        yield return new WaitForSeconds(3f);
        SceneManager.LoadScene("OpenScene");
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
        logText.text = captainLogGOText;
        yield return new WaitForSeconds(3f);
        SceneManager.LoadScene("OpenScene");
    }

}
