// Authored by: Alok Agrawal
// Team: AxKRA Studios

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CharacterStateController : MonoBehaviour
{
    Animator animator;
    Renderer[] characterMaterials;
    HealthRespawnManager playerControls;

    public Texture2D[] albedoList;
    [ColorUsage(true,true)]
    public Color[] eyeColors;

    // Start is called before the first frame update
    void Start()
    {
        animator = GetComponent<Animator>();
        characterMaterials = GetComponentsInChildren<Renderer>();
        playerControls = GetComponent<HealthRespawnManager>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            ChangeMaterialSettings(0);

        }
        if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            ChangeMaterialSettings(1);
        }

        if (Input.GetKeyDown(KeyCode.Alpha3))
        {
            ChangeMaterialSettings(2);
        }
        // if (Input.GetKeyDown(KeyCode.Alpha4)) {
        //     playerControls.CauseDamage();
        //     Debug.Assert(playerControls.health > 0, "Player Dead, game over!");
        // }

        if (playerControls.health == 10) 
        {
            ChangeMaterialSettings(3);
            
        }
    }


    void ChangeMaterialSettings(int index)
    {
        for (int i = 0; i < characterMaterials.Length; i++)
        {
            if (characterMaterials[i].transform.CompareTag("PlayerEyes"))
                characterMaterials[i].material.SetColor("_EmissionColor", eyeColors[index]);
            else
                characterMaterials[i].material.SetTexture("_MainTex",albedoList[index]);
        }
    }

}
