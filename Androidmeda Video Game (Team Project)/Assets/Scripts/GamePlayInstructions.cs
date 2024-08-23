//Author: Roshaun Brady
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using TMPro;

public class GamePlayInstructions : MonoBehaviour
{
    public TextMeshProUGUI textComponent;
    public Canvas canvas;
    private string[] instructions = {
            "Press SPACEBAR to JUMP. \nUse arrow keys or WASD to move directionally. \nPress 'm' to open/close this box.",
            "Explore the corridors and make your way through the rooms.",
            "This door with lights needs a key to open.",
            "This is a gravity switch. When activated, objects can levitate for 10 seconds.",
            "Explore this room - there are multiple keys and maybe some extra health!"
        };
    private float textSpeed = 0.02f;
    public int index;
    private bool trig = true;
    private string backupInstructions;

    void Start()
    {
        textComponent.text = string.Empty;
        canvas.enabled = false;
    }
    void Update()
    {
        if (Input.GetKeyUp(KeyCode.M))
        {
            /*              if (textComponent.text == instructions[index])
                        {
                            canvas.enabled = false;
                            isTyping = false;
                        }
                        else{
                            //textComponent.text = string.Empty;
                            isTyping = false;
                            StopCoroutine(typeText());
                            textComponent.text = backupInstructions;
                        }  */
            if (canvas.enabled)
                canvas.enabled = false;
            else
                canvas.enabled = true;
        }

    }
    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player") && trig == true)
        {
            canvas.enabled = true;
            playInstructions();
        }
    }
    void playInstructions()
    {
        textComponent.text = string.Empty;
        if (trig)
        {
            StartCoroutine(typeText());
        }
        trig = false;
    }
    IEnumerator typeText()
    {
        foreach (char c in instructions[index].ToCharArray())
        {
            textComponent.text += c;
            yield return new WaitForSeconds(textSpeed);
        }
        // Wait for a short duration between instructions until fully displayed
        yield return new WaitForSeconds(0.5f);
        yield return new WaitUntil(() => textComponent.text.Length == instructions[index].Length);
        yield return new WaitForSeconds(1.5f); // play after fully displayed
        canvas.enabled = false;
    }
}