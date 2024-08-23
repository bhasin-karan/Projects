// Xun Liu

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameQuitter : MonoBehaviour
{
    // Start is called before the first frame update
    bool isCompleted = false;
    public GameObject statusObj;
    private GameObject player;

    void Awake()
    {
        player = GameObject.Find("Droid");
    }

    void Start()
    {
        if (statusObj)
        {
            statusObj.SetActive(false);
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyUp(KeyCode.X) && GameObject.FindWithTag("PopUpWindow").activeSelf)
            QuitGame();        
    }
    //Roshaun
    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            isCompleted = true;
            if (isCompleted){
                GameObject[] gameObjects = GameObject.FindGameObjectsWithTag("PreservedObject");
                foreach (GameObject gameObject in gameObjects)
                {
                    Destroy(gameObject);
                }
                StartCoroutine(GameCompleted());
                //Display message. Tell player to press X to quit the game.
                //if (statusObj)
                //{
                //   statusObj.SetActive(true);
                //}
            }
        }
    }


    IEnumerator GameCompleted()
    {
        yield return new WaitForSeconds(8f);
        SceneManager.LoadScene("CaptainLogEnd");
        player.GetComponent<HealthRespawnManager>().ResetLives();

    }

    public void QuitGame()
    {
        #if UNITY_EDITOR
                UnityEditor.EditorApplication.isPlaying = false;
        #else
                Application.Quit();
        #endif
    }
}
