//Karan Bhasin

using UnityEngine;

public class JammoPushBox : MonoBehaviour
{

    public float pushForce;

    public void OnControllerColliderHit(ControllerColliderHit hit)
    {
        Rigidbody box = hit.collider.attachedRigidbody;
        Vector3 pushDir = new Vector3(hit.moveDirection.x, 0, hit.moveDirection.z);

        if (hit.moveDirection.y < -0.3f)
        {
            return;
        }

        if (box != null && !box.isKinematic)
        {
            box.velocity = pushDir * pushForce;
        }
    }
}