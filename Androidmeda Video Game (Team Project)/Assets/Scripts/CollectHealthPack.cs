//Karan Bhasin

using UnityEngine;

public class CollectHealthPack : MonoBehaviour
{
    void OnTriggerEnter(Collider c)
    {
        if (c.CompareTag("Player"))
        {
            PlayerCollector pc = c.gameObject.GetComponent<PlayerCollector>();
            HealthRespawnManager hrm = c.gameObject.GetComponent<HealthRespawnManager>();
            if (pc != null)
            {
                hrm.HealthPackIncrease();
                Destroy(this.gameObject);
                pc.ReceiveHealthPack();
            }
            else
            {
                Debug.LogError("PlayerCollector script not found for Droid");
            }
        }
    }
}