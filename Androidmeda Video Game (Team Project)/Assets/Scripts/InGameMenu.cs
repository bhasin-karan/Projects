// Xun Liu

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(CanvasGroup))]
public class InGameMenu : MonoBehaviour
{
    // Start is called before the first frame update
    private CanvasGroup canvasGroup;
    private GameObject menu;
    public ThirdPersonControl thirdPersonControl;

    void Start()
    {
    }

    private void Awake()
    {
        CanvasGroup canvasGroup = GetComponent<CanvasGroup>();

        if (canvasGroup == null)
        {
            Debug.LogError("no canvas group component found");
        }

        menu = canvasGroup.transform.Find("PopUpMenu")?.gameObject;
        menu.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {

        if (Input.GetKeyUp(KeyCode.Escape))
        {
            if (menu.activeSelf)
            {
                menu.SetActive(false);
                Cursor.lockState = CursorLockMode.Locked;
                Cursor.visible = false;
                Time.timeScale = 1f;
            }
            else
            {
                menu.SetActive(true);
                Cursor.lockState = CursorLockMode.None;
                Cursor.visible = true;
                Time.timeScale = 0f;

            }
        }

    }
}
