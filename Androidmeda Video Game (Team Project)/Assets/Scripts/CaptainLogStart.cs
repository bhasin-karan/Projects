//Karan Bhasin

using System.Collections;
using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class CaptainLogStart : MonoBehaviour
{

    private TMP_Text logText;
    private string captainLogStartText = "CAPTAIN'S LOG - STARDATE 4213.4\nOur spaceship has been attacked and overrun by hostile forces. Emergency signals were sent, but to no avail. We are now imprisoned on the bridge, with dwindling supplies and fading hope. The new droid technician has managed to access the AxKRA5 droids in the storage bay. The technician believes they can navigate the droids to us and free us. The journey is fraught with danger, making success unlikely, but it remains our last hope.";
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
        foreach (char letter in captainLogStartText)
        {
            logText.text += letter;
            yield return waitTime;
        }
        yield return new WaitForSeconds(3f);
        SceneManager.LoadScene("_FinalGame");
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
        logText.text = captainLogStartText;
        yield return new WaitForSeconds(3f);
        SceneManager.LoadScene("_FinalGame");
    }

}
