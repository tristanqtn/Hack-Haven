It's Apple's latest innovation, the "iDoor!" ... well, it is basically the Ring Doorbell camera, but the iDoor offers a web-based browser to monitor your camera, and super secure using ultimate cryptography with even SHA256 hashing algorithms to protect customers! Don't even _think_ about snooping on other people's cameras!!

The URL given by the chall is:

```
http://challenge.nahamcon.com:31646/4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8
```

They are talking about SH256 in the guide lines and when we arrive on the chall page we can see a customer ID. Does the hash in the URL is the SHA256 encoding of the cutomer ID ? 
![[Pasted image 20240524102322.png]]

Yes it is ! 

![[Pasted image 20240524102209.png]]

Then we are computing the hash of number below 11 in a decreasing order and when we hit 0 (5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9), we obtain the flag.