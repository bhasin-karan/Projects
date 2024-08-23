// Author: Roshaun Brady

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GravitySwitch : MonoBehaviour
{
    //Set up variables
    public float buttonSinkDepth = 0.5f;
    public float animationDuration = 15f;
    public AnimationCurve animationCurve;

    //Sound variables
    private AudioSource switchAudio;
    private AudioSource objectAudio;
    public AudioClip switchPressSound;
    public AudioClip objectAnimationSound;

    private Vector3 originalPosition;
    private bool isAnimating = false;
    private bool isAnimationFinished = true;
    private float animationStartTime;
    private float elapsedTime = 0f;
    public GameObject[] objectsToAnimate; //animated objects (could be more than one)

    private void Awake()
    {
        switchAudio = GetComponent<AudioSource>();
        objectAudio = objectsToAnimate[0].GetComponent<AudioSource>();

        if (switchAudio == null)
        {
            Debug.LogError("Audio Source missing for Gravity Switch");
        }
        if (objectAudio == null)
        {
            Debug.LogError("Audio Source missing for Gravity Switch object");
        }
        if (switchPressSound == null)
        {
            Debug.LogError("No Audio Clip assigned for Gravity Switch");
        }
        if (objectAnimationSound == null)
        {
            Debug.LogError("No Audio Clip assigned for Gravity Switch object");
        }
    }
    void Start()
    {
        originalPosition = transform.position;
        // Debug.Log("TESTING THAT SCRIPT EVEN STARTS");
        
    }
    void Update()
    {
        if (isAnimating)
        {
            // Debug.Log("Animation process started");
            elapsedTime = 0f;
            while (elapsedTime < animationDuration)
                {
                    transform.position = Vector3.Lerp(originalPosition, originalPosition - Vector3.up * buttonSinkDepth, elapsedTime / animationDuration);
                    elapsedTime += Time.deltaTime;
                    // Debug.Log("Button is moving down");
                }
            isAnimating = false;
            TriggerObjectAnimation();
            
        }
    }

    void OnTriggerEnter(Collider other)
    {
        if (!isAnimating && other.CompareTag("Player"))
        {
            isAnimating = true;
            animationStartTime = Time.time;
            switchAudio.clip = switchPressSound;
            switchAudio.Play();

        }
    }

    void TriggerObjectAnimation()
    {
        foreach (GameObject obj in objectsToAnimate)
        {
            Animator anim = obj.GetComponent<Animator>();
            if (anim != null)
            {
                anim.SetTrigger("activated");
            }
        }
        objectAudio.clip = objectAnimationSound;
        objectAudio.Play();
        ResetButton();
    }

    IEnumerator WaitForAnimationToEnd(Animator anim)
    {
        while (!isAnimationFinished)
        {
            if (anim.GetCurrentAnimatorStateInfo(0).normalizedTime >= 1f)
            {
                isAnimationFinished = true;
            }
            yield return null;
        }

        // Animation has finished, execute code here
        // Debug.Log("Animation finished!");
    }

    void ResetButton()
    {
        transform.position = originalPosition;
    }
}
//GOALS
// Top of switch goes to the floor when player is standing on it
// Activates animation for xx objects
// Top of Switch returns to original state once animation is finished running