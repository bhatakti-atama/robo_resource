using UnityEngine;
using System.Collections;
public class gun : MonoBehaviour
{
    public float damage = 10f;
    public float range = 100f;
    public float impactForce = 30f;
    public float fireRate = 15f;
    public int maxAmmo = 10;
    private int currentAmmo;
    public float reloadTime = 1f;

    public Camera fpscam;

    public ParticleSystem muzzleflash;

    public GameObject impactEffect;

    private float nextTimeToFire = 0f;

    private bool IsReloading = false;

    public Animator animator;

     void Start()
    {
        currentAmmo = maxAmmo; 
    }

    void OnEnable()
    {
        IsReloading = false;
        animator.SetBool("Reloading", false);
    }
    // Update is called once per frame
    void Update()
    {
        if (IsReloading)
            return;
        if(currentAmmo<=0)
        {
            StartCoroutine(Reload());
            return;
        }

        if(Input.GetButton("Fire1")&&Time.time>=nextTimeToFire)
        {
            nextTimeToFire = Time.time + 1f / fireRate;
            shoot();
        }
        

        IEnumerator Reload()
        {
            IsReloading = true;
            animator.SetBool("Reloading", true);
            yield return new WaitForSeconds(reloadTime-0.25f);

            animator.SetBool("Reloading", false);

            yield return new WaitForSeconds(0.25f);
            currentAmmo = maxAmmo;
            IsReloading = false;
        }

        void shoot()
        {
            currentAmmo--;

            muzzleflash.Play();
            RaycastHit hit;
            if(Physics.Raycast(fpscam.transform.position,fpscam.transform.forward,out hit,range))
            {
                Debug.Log(hit.transform.name);
                Torget tar = hit.transform.GetComponent<Torget>();
                if(tar!=null)
                {
                    tar.TakeDamage(damage); 
                }

                if(hit.rigidbody!=null)
                {
                    hit.rigidbody.AddForce(-hit.normal * impactForce);
                }
               GameObject IM=Instantiate(impactEffect, hit.point, Quaternion.LookRotation(hit.normal));
                Destroy(IM, 2f);
            }
        }
    }
}
