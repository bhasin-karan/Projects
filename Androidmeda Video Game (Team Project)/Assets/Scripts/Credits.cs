//Karan Bhasin

using System.Collections;
using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class Credits : MonoBehaviour
{

    private TMP_Text logText;
    private string creditText = "An AxKRA Studios Game\n\n\nAlok Agrawal\nXun Liu\nKaran Bhasin\nRoshaun Toni-Marie Brady\nArchit Amal Sahay";
    public float typeSpeed;
    private bool skiptoEnd;

    private void Awake()
    {
        logText = GetComponent<TMP_Text>();
        if (logText == null)
        {
            Debug.LogError("No TMP_Text Component found");
        }
    }

    void Start()
    {
        StartCoroutine(LogType());
    }

    IEnumerator LogType()
    {
        var waitTime = new WaitForSeconds(typeSpeed);
        foreach (char letter in creditText)
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
        logText.text = creditText;
        yield return new WaitForSeconds(3f);
        SceneManager.LoadScene("OpenScene");
    }
}
