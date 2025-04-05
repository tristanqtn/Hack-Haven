# Let me out [1/3]

As usual it's complicated to get out of Vim. This first jail is still easy to escape with the basic Vim quit instruction : 

```
:q
```

Then : 

```
letmeout@linux-hackademy-6b4545cb6f-s7q28:~$ ls
flag.txt  message.txt
letmeout@linux-hackademy-6b4545cb6f-s7q28:~$ cat flag.txt
Star{Wo0aa@4_y0u_Go7_0u7_aNd_v1m_iz_ur_n3_fR1eNd}
```

# Let me out [2/3]

For this one we have to enable the command line mode of Vim with the following command : 

```
:!bash
```

Then : 

```
cantgetout@linux-hackademy-6b4545cb6f-2fg6z:~$ ls
flag.txt  message.txt
cantgetout@linux-hackademy-6b4545cb6f-2fg6z:~$ cat flag.txt
Star{Ok_s0_yOu_zt1ll_g0t_ou7_w3l1_d0n3_m@ate}
```
# Let me out [3/3]

This one is different because we don't exit Vim we just try to print the flag inside the editor by opening in Vim the file containing the flag :

```
:e flag.txt
```

Then the flag appears in our Vim editor: 

```
Star{Y0u_@r3_tHe_V1m_m@s73r_n0w!}
```