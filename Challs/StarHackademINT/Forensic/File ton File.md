We download a file but impossible to open it... Let's check the magic number of it : 

```bash
00000000   00 8B 08 00  1A 3B AF 66  00 03 CB CD  4C CC 2F D5  CD 05 91 0C  .....;.f....L./.....
00000014   B4 02 06 06  06 66 66 26  0A 40 DA D0  DC D4 00 99  86 02 63 03  .....ff&.@........c.
00000028   05 43 13 33  53 63 33 63  63 63 73 03  05 03 43 13  03 33 03 06  .C.3Sc3cccs...C..3..
0000003C   05 03 9A B9  08 09 94 16  97 24 16 01  9D 52 92 91  9F 9B 58 8C  .........$...R....X.
00000050   5B 1D 21 79  88 4F 14 E0  F4 10 01 C1  40 DF 57 A7  19 E6 18 17  [.!y.O......@.W.....
00000064   C7 9B 14 19  C7 17 18 94  1B 17 A5 95  E6 D4 0E B4  BB 46 C1 28  .................F.(
00000078   18 05 A3 60  14 D0 16 00  00 E5 75 CA  DE 00 08 00  00           ...`......u......
```

No magic number starts with 00 8B so we search online for a magic number where the second octet is 8B and we find that gzip file have 1F 8B as magic number. Let's edit the file in order to read the flag. 

| File type    | Typical  <br>extension | Hex digits  <br>xx = variable | Ascii digits  <br>. = not an ascii char |
| ------------ | ---------------------- | ----------------------------- | --------------------------------------- |
| Bzip         | .bz                    | 42 5a                         | BZ                                      |
| Compress     | .Z                     | 1f 9d                         | ..                                      |
| gzip format  | .gz                    | 1f 8b                         | ..                                      |
| pkzip format | .zip                   | 50 4b 03 04                   | PK..                                    |

```bash
00000000   1F 8B 08 00  1A 3B AF 66  00 03 CB CD  4C CC 2F D5  CD 05 91 0C  .....;.f....L./.....
00000014   B4 02 06 06  06 66 66 26  0A 40 DA D0  DC D4 00 99  86 02 63 03  .....ff&.@........c.
00000028   05 43 13 33  53 63 33 63  63 63 73 03  05 03 43 13  03 33 03 06  .C.3Sc3cccs...C..3..
0000003C   05 03 9A B9  08 09 94 16  97 24 16 01  9D 52 92 91  9F 9B 58 8C  .........$...R....X.
00000050   5B 1D 21 79  88 4F 14 E0  F4 10 01 C1  40 DF 57 A7  19 E6 18 17  [.!y.O......@.W.....
00000064   C7 9B 14 19  C7 17 18 94  1B 17 A5 95  E6 D4 0E B4  BB 46 C1 28  .................F.(
00000078   18 05 A3 60  14 D0 16 00  00 E5 75 CA  DE 00 08 00  00           ...`......u......
```

Then we give the file it's extension back : 

```
cp file file.gz
```

And we unzip the file and read the flag :

```
[Sep 06, 2024 - 13:47:33 (UTC)] exegol-full original # gunzip ./file.gz -k
gzip: ./file already exists; do you wish to overwrite (y or n)? y

[Sep 06, 2024 - 13:47:44 (UTC)] exegol-full original # ls
file  file.gz

[Sep 06, 2024 - 13:47:47 (UTC)] exegol-full original # cat file
miaou-miaou000664 001750 001750 00000000030 14653633370 014060 0ustar00thomasthomas000000 000000 Star{f1l3s_4r3_p0w3rful}#
```

Flag : `Star{f1l3s_4r3_p0w3rful}`



