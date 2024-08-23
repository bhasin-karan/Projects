// Xun Liu

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GravityIndicator : MonoBehaviour
{
    public GameObject[] globes;
    // Start is called before the first frame update
    public ThirdPersonControl thirdPersonControl;
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        switch (thirdPersonControl.GetGravity())
        {
            case 1:
                setToLowG();
                break;
            case 2:
                setToNorm();
                break;
            case 3:
                setToHighG();
                break;
            default:
                setToNorm();
                break;
        }
    }

    public void setToLowG()
    {
        globes[0].SetActive(true);
        globes[1].SetActive(false);
        globes[2].SetActive(false);
    }

    public void setToNorm()
    {
        globes[0].SetActive(true);
        globes[1].SetActive(true);
        globes[2].SetActive(false);
    }

    public void setToHighG()
    {
        globes[0].SetActive(true);
        globes[1].SetActive(true);
        globes[2].SetActive(true);
    }
}
