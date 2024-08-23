using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.AI;

public class SentrySpawner : MonoBehaviour
{
    public SentryChase sentry;
    private List<SentryChase> sentries = new List<SentryChase>();

    [Range(0, 10)]
    public int sentryCount = 5;
    private float _range = 20.0f;
    // Start is called before the first frame update
    void Start()
    {
        for(int index = 0; index < sentryCount; index++)
        {
            if (RandomLocationPoint(transform.position, _range, out Vector3 randomPoint))
                sentries.Add(Instantiate(sentry, randomPoint, Quaternion.identity));
        }
        
    }

    bool RandomLocationPoint(Vector3 spawnCenter, float range, out Vector3 result)
    {
        for (int i = 0; i < 30; i++)
        {
            Vector3 randomDir = spawnCenter + Random.insideUnitSphere * _range;
            if (NavMesh.SamplePosition(randomDir, out NavMeshHit hit, 3.0f, NavMesh.GetAreaFromName("storage")))
            {
                result = hit.position;
                return true;
            }
        }
        result = Vector3.zero;
        return false;
    }

}
