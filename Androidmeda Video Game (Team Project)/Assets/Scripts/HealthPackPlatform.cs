//Karan Bhasin

using UnityEngine;

public class HealthPackPlatform : MonoBehaviour
{
    private void OnTriggerExit(Collider c)
    {
        if (c.gameObject.tag == "Box")
        {
            Rigidbody box = c.GetComponent<Rigidbody>();
            if (box!= null)
            {
                box.constraints = RigidbodyConstraints.FreezePositionX | RigidbodyConstraints.FreezeRotation;
            }
        }
    }
}
