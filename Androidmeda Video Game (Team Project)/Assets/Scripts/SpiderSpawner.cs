// Authored by: Alok Agrawal
// Team: AxKRA Studios

using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.AI;

public class SpiderSpawner : MonoBehaviour
{
    public SentryChase spider;
    private List<SentryChase> sentries = new List<SentryChase>();

    [Range(0, 10)]
    public int spiderCount = 5;
    private float _range = 10.0f;
    // Start is called before the first frame update
    void Start()
    {
        for(int index = 0; index < spiderCount; index++)
        {
            if (RandomLocationPoint(transform.position, _range, out Vector3 randomPoint))
                sentries.Add(Instantiate(spider, randomPoint, Quaternion.identity));
        }
        
    }

    bool RandomLocationPoint(Vector3 spawnCenter, float range, out Vector3 result)
    {
        for (int i = 0; i < 100; i++)
        {
            Vector3 randomDir = spawnCenter + Random.insideUnitSphere * _range;
            if (NavMesh.SamplePosition(randomDir, out NavMeshHit hit, 2.0f, NavMesh.GetAreaFromName("cafetaria")))
            {
                result = hit.position;
                return true;
            }
        }
        result = Vector3.zero;
        return false;
    }

}
