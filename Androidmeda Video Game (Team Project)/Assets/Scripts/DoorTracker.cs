/*
 * Author: Archit Amal Sahay
 * DoorTracker contains the logic to
 * preserve progress on reload/respawn.
 */

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DoorTracker : MonoBehaviour
{
    private static DoorTracker instance;
    public static DoorTracker Instance
    {
        get { return instance; }
    }    

    public GameObject[] doors;
    public GameObject[] keys;

    public bool[] state = new bool[] { false, false };

    void Awake()
    {
        if (instance == null)
        {
            instance = this;
        }
        else if (instance != this)
        {
            state = instance.state;
            Destroy(instance.gameObject);
            instance = this;
        }
        DontDestroyOnLoad(gameObject);

        for (int i = 0; i < doors.Length; i++)
        {
            if (state[i])
            {
                doors[i].GetComponent<Animator>().SetBool("character_nearby", true);
                Destroy(keys[i]);
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        for (int i = 0; i < doors.Length; i++)
        {
            if (doors[i].GetComponent<KeyLockedDoor>().doorOpen)
            {
                state[i] = true;
            }
        }
    }
}
