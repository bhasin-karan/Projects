using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class KeyGuidanceManager : MonoBehaviour
{
    private UnityAction keyGuidanceAppearanceEventListener;
    private UnityAction<int> keyGuidanceTurnOffEventListener;
    public int order;

    void Awake()
    {
        keyGuidanceAppearanceEventListener = new UnityAction(keyGuidanceAppearanceEventHandler);
        keyGuidanceTurnOffEventListener = new UnityAction<int>(keyGuidanceTurnOffEventHandler);
    }

    void OnEnable()
    {
        EventManager.StartListening<KeyGuidanceAppearanceEvent>(keyGuidanceAppearanceEventListener);
        EventManager.StartListening<TurnOffGuidanceEvent, int>(keyGuidanceTurnOffEventListener);
    }

    void OnDisable()
    {
        EventManager.StopListening<KeyGuidanceAppearanceEvent>(keyGuidanceAppearanceEventListener);
        EventManager.StopListening<TurnOffGuidanceEvent, int>(keyGuidanceTurnOffEventListener);
    }

    void Start()
    {
        gameObject.transform.GetComponent<Light>().enabled = false;
    }

    void keyGuidanceAppearanceEventHandler()
    {
        gameObject.transform.GetComponent<Light>().enabled = true;
    }

    void keyGuidanceTurnOffEventHandler(int orderOther)
    {
        if (order <= orderOther)
        {
            gameObject.transform.GetComponent<Light>().enabled = false;
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        EventManager.TriggerEvent<TurnOffGuidanceEvent, int>(order);
    }
}