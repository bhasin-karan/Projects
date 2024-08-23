//if Button is actvate, key is released onto the floor
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
//ROSHAUN
public class KeyRelease : MonoBehaviour 
{
    public GameObject key; // Reference to the object to drop
    public Rigidbody rb;
    public float dropHeight = 5f;  // Height from which the object will drop
    public float dropSpeed = 3f;    // Speed at which the object will drop

    private bool isPressed = false; // Track if the button is pressed
    private AudioSource audioSrc;

    void Start(){
        audioSrc = GetComponent<AudioSource>();
        rb = key.GetComponent<Rigidbody>();
    }

    // OnTriggerEnter is called when the Collider other enters the trigger
    void OnTriggerEnter(Collider other)
    {
        // Check if the colliding object has the "Player" tag
        if (other.CompareTag("Player"))
        {
            isPressed = true;
            DropObject();
            gameObject.SetActive(false);
        }
    }

    // Update is called once per frame
    void Update()
    {

    }

    void DropObject()
    {
        // Activate gravity
        rb.useGravity = true;
        audioSrc.Play();
    } 
}