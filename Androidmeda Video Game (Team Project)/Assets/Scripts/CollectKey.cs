//Karan Bhasin

using UnityEngine;

public class CollectKey : MonoBehaviour
{
    void OnTriggerEnter(Collider c)
    {
        if (c.CompareTag("Player"))
        {
            PlayerCollector pc = c.gameObject.GetComponent<PlayerCollector>();
            if (pc != null)
            {
                Destroy(this.gameObject);
                pc.ReceiveKey();
            }
            else
            {
                Debug.LogError("PlayerCollector script not found for Droid");
            }
        }
    }
}
