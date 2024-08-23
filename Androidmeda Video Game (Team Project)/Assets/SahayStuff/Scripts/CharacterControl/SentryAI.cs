/*
 * Author: Archit Amal Sahay
 * SentryAI contains the logic for the Sentry as well as
 * its interactions with the player
 */


using System.Collections;
using System.Collections.Generic;
using System.Diagnostics.Tracing;
// using UnityEditor.UI;
using UnityEngine;
using UnityEngine.AI;
using UnityEngine.UI;

public class SentryAI : MonoBehaviour
{
    private NavMeshAgent nma;
    private Animator animator;
    private LineRenderer lr;
    private AudioSource alarm;
    private AudioSource attack;

    private GameObject gun;
    private GameObject mount;
    private GameObject detectionRadius;
    private GameObject laserSight;
    private Color lro;
    private Color laserFlash = Color.yellow;

    public GameObject player;
    public GameObject[] waypoints;

    private int index = -1;

    public float threshold = 1.50f;

    public float attackRadius = 5.0f;
    public float frontDetect = 15.0f;
    public float backDetect = 7.5f;
    public float expandRatio = 1.5f;
    public float waitTime = 3f;
    public float swingTimer = 1f;

    private float planeScale = 1.4f;
    private float currWait = 0f;
    private float backswing;

    public enum AIState
    {
        Patrol,
        Wait,
        Detect,
        Chase
    }

    public AIState state;

    // Start is called before the first frame update
    void Start()
    {
        nma = GetComponent<NavMeshAgent>();
        animator = GetComponent<Animator>();
        laserSight = transform.GetChild(2).gameObject;
        // lr = GetComponent<LineRenderer>();
        lr = laserSight.GetComponent<LineRenderer>();
        lro = lr.material.color;
        gun = transform.GetChild(0).GetChild(0).GetChild(0).gameObject;
        mount = transform.GetChild(0).GetChild(0).GetChild(1).gameObject;
        detectionRadius = transform.GetChild(1).gameObject;
        AudioSource[] sources = GetComponents<AudioSource>();
        alarm = sources[0];
        attack = sources[1];

        nma.stoppingDistance = threshold;
        backswing = swingTimer + float.Epsilon;

        state = AIState.Patrol;
        SetNextWaypoint();
    }

    // Update is called once per frame
    void Update()
    {
        // Debug.Log(state.ToString());
        backswing += Time.deltaTime;
        if (backswing >= (swingTimer / 2))
        {
            lr.material.color = lro;
        }
        switch (state)
        {
            case AIState.Patrol:
                if (playerDetected() && !playerBehindCover())
                {
                    // raycast to see if player is behind cover?
                    transitionToDetect();
                }

                else if (nma.remainingDistance < threshold && !nma.pathPending)
                {
                    // Debug.Log(nma.remainingDistance);
                    transitionToWait();
                }
                break;

            case AIState.Wait:
                if (playerDetected() && !playerBehindCover())
                {
                    transitionToDetect();
                }

                else if (currWait >= waitTime)
                {
                    transitionToPatrol();
                }

                else
                {
                    currWait += Time.deltaTime;
                }
                break;

            case AIState.Detect:
                if (!playerDetected() || playerBehindCover())
                {
                    // player has escaped us
                    transitionToPatrol();
                }

                // player still in range
                else if (animator.GetCurrentAnimatorStateInfo(0).IsName("Sentry Detect"))
                {
                    Quaternion dest = Quaternion.LookRotation(player.transform.position - transform.position, Vector3.up);
                    transform.rotation = Quaternion.RotateTowards(transform.rotation, dest, 180.0f * Time.deltaTime);
                }

                // maybe this doesn't need the if?
                else if (animator.GetCurrentAnimatorStateInfo(0).IsName("Sentry Chase"))
                {
                    transitionToChase();
                }

                break;

            case AIState.Chase:
                if (!playerDetected() || playerBehindCover())
                {
                    transitionToPatrol();
                }
                else
                {
                    drawTarget();
                    if (playerInAttackRange() && backswing >= swingTimer)
                    {
                        // Change this to match the corresponding name in the player script
                        player.GetComponent<HealthRespawnManager>().CauseDamage();
                        playAttack();
                        backswing = 0;
                        lr.material.color = laserFlash;
                    }
                    else
                    {
                        nma.SetDestination(player.transform.position);
                    }
                }
                break;
        }
    }

    private bool playerDetected()
    {
        float dist = Vector3.Distance(transform.position, player.transform.position);
        if (dist > frontDetect)
        {
            return false;
        }

        else if (dist <= backDetect)
        {
            return true;
        }

        else
        {
            // backDetect < dist <= frontDetect
            // is the player in front?
            Vector3 towards = (player.transform.position - transform.position).normalized;
            return Vector3.Dot(transform.forward, towards) >= 0; // offensive tiebreak
        }

    }

    private bool playerBehindCover()
    {
        // player can avoid sentry by hugging the walls - may need to do both navmesh and physics against walls
        NavMeshHit hit;
        return nma.Raycast(player.transform.position, out hit);
        // return NavMesh.Raycast(transform.position, player.transform.position, out hit, NavMesh.AllAreas);
        // return Physics.Raycast(transform.position, player.transform.position - transform.position, Vector3.Distance(player.transform.position, transform.position), ~(1 << 3));
    }

    private bool playerInAttackRange()
    {
        return Vector3.Distance(transform.position, player.transform.position) <= attackRadius;
    }

    private void transitionToPatrol()
    {
        // Debug.Log("Transitioning to Patrol");
        if (state == AIState.Detect || state == AIState.Chase)
        {
            // shrink radii, reset detection, clean up laser sight, and navigate to previous waypoint
            frontDetect /= expandRatio;
            backDetect /= expandRatio;
            detectionRadius.transform.localScale = new Vector3(detectionRadius.transform.localScale.x / planeScale, detectionRadius.transform.localScale.y, detectionRadius.transform.localScale.z / planeScale);
            animator.SetBool("Detect", false);
            destroyTarget();
            index = (index - 1) % waypoints.Length;
        }
        animator.SetBool("Reached", false);
        nma.isStopped = false;
        state = AIState.Patrol;
        SetNextWaypoint();
    }

    private void transitionToWait()
    {
        if (state == AIState.Patrol)
        {
            animator.SetBool("Reached", true);
        }
        nma.isStopped = true;
        currWait = 0;
        state = AIState.Wait;
    }

    private void transitionToDetect()
    {
        // Debug.Log("Transitioning to Detect");
        frontDetect *= expandRatio;
        backDetect *= expandRatio;
        detectionRadius.transform.localScale = new Vector3(detectionRadius.transform.localScale.x * planeScale, detectionRadius.transform.localScale.y, detectionRadius.transform.localScale.z * planeScale);
        nma.isStopped = true;
        state = AIState.Detect;
        animator.SetBool("Detect", true);
    }

    private void transitionToChase()
    {
        // Debug.Log("Transitioning to Chase");
        nma.isStopped = false;
        state = AIState.Chase;
        animator.SetBool("Detect", true);
        nma.SetDestination(player.transform.position);
    }

    void SetNextWaypoint()
    {
        index = (index + 1) % waypoints.Length;
        nma.SetDestination(waypoints[index].transform.position);
    }

    void playAlarm()
    {
        alarm.Play();
    }

    void playAttack()
    {
        attack.Play();
    }

    private void drawTarget()
    {
        Vector3[] positions = new Vector3[2];
        positions[0] = laserSight.transform.position;
        positions[1] = player.transform.position;
        lr.positionCount = 2;
        lr.SetPositions(positions);
    }

    private void destroyTarget()
    {
        lr.positionCount = 0;
    }
}
