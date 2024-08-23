using System.Collections;
using System.Collections.Generic;
using UnityEngine;
//ROSHAUN
public class DroneRoomActivator : MonoBehaviour 
{
   public GameObject glassDoor;
   bool isPlayerInteracting = false;

   //establish game object
   void Start(){
        glassDoor = gameObject;
   }
   //If spacebar is pressed remove door. When pressed again return the door.
   //Note: add additional checks so that the spacebar can be used for other applications, if needed.
   void Update(){
        if (Input.GetKeyDown(KeyCode.Space) && isPlayerInteracting)
        {
            if (glassDoor.activeSelf){
                glassDoor.SetActive(false);
                float timer = 0f;
                while (timer < 3f)
                {
                    timer += Time.deltaTime;
                }
            }
            else{
                glassDoor.SetActive(true);
            }
        }
    }
    //See if player is in the triggerzone of the door
    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            isPlayerInteracting = true;
        }
    }

    void OnTriggerExit(Collider other)
    {
        // Check if the player exited the trigger zone of this door
        if (other.CompareTag("Player"))
        {
            isPlayerInteracting = false;
        }
    }
}