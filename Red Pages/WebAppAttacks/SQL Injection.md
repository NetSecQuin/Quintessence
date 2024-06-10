# SQL Injection

SQL Injection is a code injection vulnerability that relies on running unauthorized SQL queries in order to preform unintended actions such as viewing, editing, or deleted data inside an SQL database. Depending on the permissions of the system account used for the SQL database, it is also possible that it can be used for code execution on the system (at a user or administrative level)

## Exploitable Fields
SQL Injection exploits can be inserted into any forms that interact with SQL databases without proper validation or sanatizing the inputs with prepared statements.

- User login forms (e.g., username and password fields)
- Search boxes
- URL parameters
- Any input fields that directly interact with the database


## Impact

- Data Breach: Unauthorized access to sensitive data.
- Data Manipulation: Altering or deleting data.
- Authentication Bypass: Gaining administrative access without valid credentials.
- Data Integrity Issues: Compromising the integrity of the database.
- Full System Compromise: If the database has system-level access, it can lead to complete system takeover.

## Types of SQL Injection

### Traditional SQL Injection

Works by inserting a 'OR must be true' statement into an SQL paramenter. For instance inserting `admin` into a username field and `password' OR '1'='1` into the password field. In a vulnerable input, the injected SQL query would also provide a true result, and SELECT the requested data.

In this example, the following injected SQL query was exectued:
``` SELECT * FROM users WHERE username = 'admin' AND password = 'password' OR '1'='1'; ```

### Union-Based SQL Injection:
This type of attack leverages the UNION SQL operator to combine the results of two or more SELECT statements into a single result set.
A Union-Based SQL Injection may bypass WAF filtering or situations where only one of the inputs are not configured to be 'prepared statements' that validate and sanatize inputs. An example would be where the input of: 

username: `' UNION SELECT username, password FROM admin_table --`
password: ` ` , which would result in the SQL being executed:

``` SELECT username, password FROM users WHERE username = '' UNION SELECT username, password FROM admin_table --' AND password = ''; ```

### Blind SQL Injection
Blind SQL Injection does not rely on error messages but infers information based on the application’s response time or the content of responses.
This injection can be used to identify true or false statements through differences in response time. Examples of a true vs a false statement:

True :` ' AND (SELECT CASE WHEN (1=1) THEN 1 ELSE 0 END) = 1 -- `
False: `' AND (SELECT CASE WHEN (1=0) THEN 1 ELSE 0 END) = 1 -- `

## Vulnerable Code Example
The following code block recieves an SQL input as one entire SQL request. This does not seperate or sanatize the input. 

```
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class SQLInjectionVulnerable {
    public static void main(String[] args) {
        String username = "admin";
        String password = "password' OR '1'='1";
        
        try {
            Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "root", "password");
            Statement statement = connection.createStatement();
            String query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";
            ResultSet resultSet = statement.executeQuery(query);
            
            while (resultSet.next()) {
                System.out.println("User authenticated: " + resultSet.getString("username"));
            }
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## Remediated Code Example 
The following updated code block takes in the input as "prepared statements". By accepting input this way, the input is stored seperatly as data, therefore it can not be executed as an SQL statement. Additionally by storing it as data, the input escapes and special characters like quotes thus sanatizing the input. 

```
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class SQLInjectionFixed {
    public static void main(String[] args) {
        String username = "admin";
        String password = "password' OR '1'='1";  // This input will no longer work for SQL Injection

        try {
            Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "root", "password");
            String query = "SELECT * FROM users WHERE username = ? AND password = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            preparedStatement.setString(1, username);
            preparedStatement.setString(2, password);
            ResultSet resultSet = preparedStatement.executeQuery();
            
            while (resultSet.next()) {
                System.out.println("User authenticated: " + resultSet.getString("username"));
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
