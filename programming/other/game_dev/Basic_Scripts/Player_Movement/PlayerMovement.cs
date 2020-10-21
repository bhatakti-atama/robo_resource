using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public CharacterController controller;
    public float speed = 12f;
    public float gravity = -9.81f;
    public float jumphight = 1.8f;
    public Transform GroundCheck;
    public float groundDistance = 0.4f;
    public LayerMask groundMask;
    bool isgrounded;
    public float PlayerHealth=500f;
    public health healthbar;
    public GameManager gamemanager;
   

    public void PlayerShot(float amount)
    {
        PlayerHealth =PlayerHealth-amount;
        healthbar.SetHealth(PlayerHealth);
        if(PlayerHealth<=0)
        {
            gamemanager.EndGame();
        }

    }

   

    Vector3 velocity;
    // Update is called once per frame
    void Update()
    {
        isgrounded = Physics.CheckSphere(GroundCheck.position, groundDistance, groundMask);
        if (isgrounded)
        {
            velocity.y = -2f;
        }
        float x = Input.GetAxis("Horizontal");
        float z = Input.GetAxis("Vertical");

        Vector3 move = transform.right * x + transform.forward * z;

        controller.Move(move*speed*Time.deltaTime);
        if(Input.GetButtonDown("Jump")&&isgrounded)
        {
            velocity.y =Mathf.Sqrt(jumphight * 2f * gravity);
        }
        velocity.y -= gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);

    }
}
