# La bêta du starhack [1/2]

When we explore the page we note that the current score is stored in the cookie. 

![[Pasted image 20240906164537.png]]

Let's try to improve our score : 

![[Pasted image 20240906164631.png]]

Flag : `Star{l3s_c0ok13s_c3st_b0n_QD_m3m3}`

# La bêta du starhack [2/2]

For this part of the chall we create a dummy session and then explore the page. It seems that we are logged in thanks to a JWT token stored as a cookie.

![[Pasted image 20240906212349.png]]

Here's the JWT token : `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcyNTY1MDYwNSwiZXhwIjoxNzI1NzM3MDA1fQ.9_KfDAyws76j0R_iJKT4h5ylelrxgTdN5IhhSUwT7VI`

JWT decryption : 

![[Pasted image 20240906212544.png]]

The payload contains a field `admin` set to `false`. In order to set it to true we should find the signature of this token and then modify the payload and resign it again. We thus try a brute force attack against this token signature as so : `hashcat -m 16500 jwt.txt rockyou.txt`

![[Pasted image 20240906212444.png]]


The password found by hashcat is `lovelove`. We we try to check the passphrase it matches so this is the correct one.

![[Pasted image 20240906212617.png]]

We can then corrupt the payload by changing the value of `admin` to `true` and sing with the password `lovelove`.

![[Pasted image 20240906212632.png]]

The new token is : 
`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNzI1NjQ5OTg3LCJleHAiOjE3MjU3MzYzODd9.InV4N4T_O7GZ7ApEH7wxmVsQiFlB2GHOf1OUpPssZVY`

When we insert the new token into the cookie and refresh the page we obtain the admin flag.

![[Pasted image 20240906212728.png]]
Flag : `Star{jaimelesmotsdepassedecurisesouiouicesttresbienlesmdp}`