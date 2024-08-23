// Authored by: Alok Agrawal
// Team: AxKRA Studios

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class HealthRespawnManager : MonoBehaviour
{

    public int health;
    public GameObject DamageSplash;
    [SerializeField] private int maxLives = 3; // Maximum number of lives the player can have
    static int currentLives = 0; // Current number of lives

    private float invincibleTimer;
    [SerializeField] private float invincibilityTime = 1f;

    bool lifeLost;

    Animator anim;
    // Start is called before the first frame update
    void Start()
    {
        health = 100;
        anim = this.GetComponent<Animator> ();
        lifeLost = false;
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void CauseDamage(){

        if(Time.time >= invincibleTimer)
        {
            invincibleTimer = Time.time + invincibilityTime;

            health -= 10;
            
            GameObject effectDamage = Instantiate(DamageSplash, transform.position, Quaternion.identity) as GameObject;
            
            var main = effectDamage.gameObject.GetComponent<ParticleSystem>().main;
            
            main.startColor = this.GetComponentsInChildren<Renderer>()[12].material.color;
        }

        if (health <= 0)
        {
            ReduceLife();
            health = 0;
        }
    }

    public void ReduceLife()
    {
        if (lifeLost) return;
        
        currentLives++;
        
        Debug.Log(currentLives);
        if (currentLives < 0) currentLives = 0;

        if (currentLives >= maxLives)
        {
            anim.SetBool("gameOver", true);
            StartCoroutine(WaitForKeyPressAndReload(true));
        }
        else
        {
            anim.SetBool("hasLost", true);
            StartCoroutine(WaitForKeyPressAndReload(false));
            
        }

        lifeLost = true;
    }

    public int GetHealth()
    {
        return health;
    }
    public int GetCurrentLives()
    {
        return maxLives - currentLives;
    }
    //HealthPackIncrease - Karan Bhasin
    public void HealthPackIncrease()
    {
        health += 20;

        if (health > 100)
        {
            health = 100;
        }

    }

    public void ResetLives()
    {
        currentLives = 0;
    }

    private IEnumerator WaitForKeyPressAndReload(bool loadOpenScene)
    {
        // Wait for 5 seconds and then continue
        yield return new WaitForSeconds(5f);
        // Wait until the player presses 'R'
        

        if (loadOpenScene)
        {
            // Load the OpenScene
            GameObject[] gameObjects = GameObject.FindGameObjectsWithTag("PreservedObject");
            foreach (GameObject gameObject in gameObjects)
            {
                Destroy(gameObject);
            }
            ResetLives();
            SceneManager.LoadScene("CaptainLogGameOver");
        }
        else
        {
            // Reload the current scene
            SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        }
    }
}
