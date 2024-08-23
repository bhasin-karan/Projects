// Xun Liu

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameStarter : MonoBehaviour
{
    public void StartGame()
    {
        GameObject[] gameObjects = GameObject.FindGameObjectsWithTag("PreservedObject");
        foreach (GameObject gameObject in gameObjects)
        {
            Destroy(gameObject);
        }
        SceneManager.LoadScene("CaptainLogStart");
        Time.timeScale = 1f;
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyUp(KeyCode.S) && GameObject.FindWithTag("PopUpWindow").activeSelf)
        {
            StartGame();
        }
            
    }
}
