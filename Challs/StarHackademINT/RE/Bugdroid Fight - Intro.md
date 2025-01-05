In order to reverse some APK apps I usually go jadx, a well known Java decompiler very efficient when it comes to APKs.

```bash
jadx -d ./output/ bugdroid_fight_intro.apk
```

```bash
ls -la
total 7564
drwxrwxrwx 1 root root     512 Sep  6 11:45 .
drwxrwxrwx 1 root root     512 Sep  6 11:48 ..
-rwxrwxrwx 1 root root 7744336 Sep  5 13:03 bugdroid_fight_intro.apk
drwxrwx--- 1 root root     512 Sep  5 13:03 output
```

We can now explore the source code of the app to find the flag. Usually in RE challs the goal is to understand an encryption process and manage to produce the password that once encrypted will match. But for this entry level chall the goal is just to find the flag splited in pieces all over the source code.

It's important to know the architecture of an APK to know where to search for the flag. There's 2 main directories to search :

**Main Source Code of the app :** `sources > com > example`

**Constant definitions :** `resources > res > > values `

After diving deeply into the code I have found the parts of the flag in those files : 

`Bugdroid\output\sources\com\example\reverseintro\MainActivityKt.java`

![[Pasted image 20240906140402.png]]

`Bugdroid\output\resources\res\values\strings.xml`

![[Pasted image 20240906140240.png]]

Flag : `Star{Br4v0_tU_as_f41t_un_prem13R_p4s_daNs_l3_r37eRse_Andr01d}`