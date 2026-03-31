# Lab: Blind SQL injection with conditional responses

## Url

https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

## prob describe

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and no error messages are displayed. But the application includes a Welcome back message in the page if the query returns any rows.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user.

You can assume that the password only contains lowercase, alphanumeric characters.

## solve

If satisfy the condition, they'll show the sign of `Welcome back`.

TrackingId of Cookie is set in the SQL query, so there is a SQL injection in TrackingId.

```
TrackingId=AAAABBBB' AND '1'='1'-- satisfy the condition, they'll show the sign of `Welcome back`
TrackingId=AAAABBBB' AND '1'='2'-- do not satisfy the condition, they won't show the sign of `Welcome back`
```

python script in Blind-SQL-with-cond-resp.py.
