using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HeightControl : MonoBehaviour
{
    public CharacterController controller;

    public float gravity = -9.81f;
    public Transform GroundCheck;
    public float groundDistance = 0.4f;
    public LayerMask groundMask;
    bool isgrounded;

    Vector3 velocity;
    // Update is called once per frame
    void Update()
    {
        isgrounded = Physics.CheckSphere(GroundCheck.position, groundDistance, groundMask);
        if (isgrounded)
        {
            velocity.y = -2f;
        }

        velocity.y -= gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);
    }
}
