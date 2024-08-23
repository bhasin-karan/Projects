//Karan Bhasin

using UnityEngine;

public class CollectSecurityGatePass : MonoBehaviour
{
    void OnTriggerEnter(Collider c)
    {
        if (c.CompareTag("Player"))
        {
            PlayerCollector pc = c.gameObject.GetComponent<PlayerCollector>();
            if (pc != null)
            {
                Destroy(this.gameObject);
                pc.ReceivePass();
            }
            else
            {
                Debug.LogError("PlayerCollector script not found for Droid");
            }
        }

        EventManager.TriggerEvent<TurnOffGuidanceEvent, int>(100);
    }
}
