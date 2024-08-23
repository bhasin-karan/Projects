// Authored by: Alok Agrawal
// Team: AxKRA Studios

using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using Cinemachine;
using UnityEngine.SceneManagement;

public class ThirdPersonControl : MonoBehaviour
{
    // Start is called before the first frame update
    // public CharacterController controller;
    public Camera maincam;
    public Transform cam;

    float speed = 7f;
    public float gravity = -9.81f;
    public float jumpHeight = 0.3f;
    public float turnSmoothTime = 0.1f;
    float turnSmoothVelocity;

    public Transform groundCheck;
    
    public float groundDistance = 0.3f;
    public LayerMask[] groundMask;
    int raycastMask;
    int gravityDisplayValue;

    bool touchingBox;
    
    Animator anim;
    CharacterController controller;

    Vector3 velocity;
    bool isGrounded;

    float speedXZ;
    float allowPlayerRotation = 0.1f;
    float StartAnimTime = 0.3f;
    float StopAnimTime = 0.15f;

    bool isJumping;
    bool isLanding;

    [SerializeField] private CinemachineVirtualCamera vcam;

    void Awake()
    {
        Cursor.lockState = CursorLockMode.Locked;

        Cursor.visible = false;

        raycastMask = (1 << LayerMask.NameToLayer("Ground") | 1 << LayerMask.NameToLayer("LowGravity") | 1 << LayerMask.NameToLayer("HighGravity") | 1 << LayerMask.NameToLayer("Default"));
    }
    

    void Start () {
        
		anim = this.GetComponent<Animator> ();

		maincam = Camera.main;

		controller = this.GetComponent<CharacterController> ();

        touchingBox = false;

        // transform.position = new Vector3(-43.41f, 5f, 101.4f);
        
	}

    // Update is called once per frame
    void Update()
    {
        isJumping = anim.GetBool("isJumping");
        isLanding = anim.GetBool("isLanding");
        // isGrounded = Physics.CheckSphere(groundCheck.position, groundDistance, raycastMask);

        handleJumpGravity();

        isGrounded = Physics.Raycast(transform.position, Vector3.down, 0.3f, raycastMask);

        if (isGrounded && velocity.y < 0) velocity.y = -2f;

        float horizontalMove = Input.GetAxisRaw("Horizontal");

        float verticalMove = Input.GetAxisRaw("Vertical");

        //Calculate the Input Magnitude
		speedXZ = new Vector2(horizontalMove, verticalMove).sqrMagnitude;

        if (speedXZ > allowPlayerRotation) 
        {
			anim.SetFloat ("Blend", speedXZ, StartAnimTime, Time.deltaTime);
		} 
        else if (speedXZ < allowPlayerRotation) 
        {
			anim.SetFloat ("Blend", speedXZ, StopAnimTime, Time.deltaTime);
		}

        Vector3 direction = new Vector3(horizontalMove, 0f, verticalMove).normalized;

        if (direction.magnitude >= 0.1f)
        {
            float targetAngle = Mathf.Atan2(direction.x, direction.z) * Mathf.Rad2Deg + cam.eulerAngles.y;
            
            float angle = Mathf.SmoothDampAngle(transform.eulerAngles.y, targetAngle, ref turnSmoothVelocity, turnSmoothTime);
            
            transform.rotation = Quaternion.Euler(0f, angle, 0f);

            Vector3 moveDir = Quaternion.Euler(0f, targetAngle, 0f) * Vector3.forward;

            controller.Move(moveDir.normalized * speed * Time.deltaTime);
        }

        if(Input.GetButtonDown("Jump") && isGrounded)
        {
            velocity.y = Mathf.Sqrt(jumpHeight * -2f * gravity);

            if (!isJumping) anim.SetBool("isJumping", true);
        }
        else if (isJumping && velocity.y < 0) 
        {
            anim.SetBool("isJumping", false);
        }

        velocity.y += gravity * Time.deltaTime;

        controller.Move(velocity * Time.deltaTime);

    }

    void handleJumpGravity()
    {
        if (Physics.CheckSphere(groundCheck.position, groundDistance, groundMask[1]))
        {
            jumpHeight = 4f;
            gravity = -5f;
            gravityDisplayValue = 2;
            
        }
        else if (Physics.CheckSphere(groundCheck.position, groundDistance, groundMask[2]))
        {
            jumpHeight = 9f;
            gravity = -2.5f;
            gravityDisplayValue = 1;
        }
        else
        {
            jumpHeight = 1.5f;
            gravity = -9.81f;
            gravityDisplayValue = 3;
        }
    }

    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "Finish")
        {
            anim.SetBool("happy", true);

            float angle = Mathf.SmoothDampAngle(transform.eulerAngles.y, -vcam.transform.eulerAngles.y, ref turnSmoothVelocity, turnSmoothTime);
            
            transform.rotation = Quaternion.Euler(0f, angle, 0f);

            // switch to second cinemachine virtual camera
            vcam.Priority = 20;

            this.speed = 0;
        }     
        
    }

    public int GetGravity()
    {
        return gravityDisplayValue;
    }


}
