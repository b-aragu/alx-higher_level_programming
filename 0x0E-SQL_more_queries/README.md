## Creating and Granting Users permission
__Creating new User__
- You can create a new user using the __CREATE USER__ statement. The general syntax is:
```mysql
CREATE USER `username` @ `host` IDENTIFIED WITH authentication_plugin BY `password`;
```
*host* - Hostname the user will connect
- It creates a user with no privileges.
- You can leave the `auth_socket` plugin (`authentication_plugin`) to use mysql default one.
- If you are not sure you can use the `ALTER` command to change.

__Granting a User permissions__
- The general syntax for granting User privileges is as follows:
```mysql
GRANT PRIVILEGE ON database.table TO `username` @ `host`;
```
- e.g granting user global privileges `ON *.*` - apply to all databases in mysql server.
```mysql
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO `username` @ `localhost` WITH GRANT OPTION;
```
__`WITH GRANT OPTION`__ - allows the user to grant permissions he has to other users in the system.
__`ALL PRIVILEGES`__ - grant users with broad super user privileges akin to the root users priviledges

- **Proxy user privileges** allow one user to be a proxy for another. The proxy user gets all the privileges of the proxied user. For example:
`GRANT PROXY  ON root  TO alice@localhost;`, `alice@localhost` assumes all privileges of the user `root`.
- To revoke permission, the syntax is:
```mysql
REVOKE type_of_permission ON database.table_name FROM `username` @ `host`;
```
- To review user currents permission run:
```mysql
SHOW GRANTS FOR `username` @ `host`;
```
- You can use drop to delete a user just as you can delete a database.
```mysql
DROP USER `username` @ `localhost`;
```
- In the future to log in as a new user, you can use the command:
```bash
mysql -u username -p
```
-p ~ prompt for mysql user password.

---
## MYSQL Constraints
- Constraints are placed on columns or tables and they limit the data that can be inserted into tables.
```
1. NOT NULL
2. UNIQUE
3. PRIMARY KEY
4. FOREIGN KEY
5. ENUM
6. SET
```
__NOT NULL__ - a column with not null constraint cannot have null values.
__UNIQUE__ - Ensures that all data are unique in a column.
The primary key constraint automatically has a unique constraint defined on it.
Primary key cant be null unique can. There can only be one primary key in a table , there can be more unique columns.
__PRIMARY KEY__ - uniquely identifies each record in a database table.
__`DESCRIBE table;`__ - shows information about the column in a table.

__FOREIGN KEY__ - one table pointss to a primary key in another table.

__ENUM__ - string object with a value chosen from a list of permitted values. They are enumerated explicitly in the column specification at table creation time.

__SET__ - Can have zero or more values. Each of the values must be choosen from a list of permitted values.

### Normalization 
It is a technique that reduces data redundancy and eliminates undesirable characteeristics like insertion, update and deletion anomalies.
