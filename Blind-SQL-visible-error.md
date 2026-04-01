# Lab: Visible error-based SQL injection

## Url

https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based

## prob describe

This lab contains a SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie. The results of the SQL query are not returned.

The database contains a different table called users, with columns called username and password. To solve the lab, find a way to leak the password for the administrator user, then log in to their account.

## solve

```
TrackingId=' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--
```

In the response, notice the verbose error message. When an error occured, there will be a error message. Use the `CAST(var AS TYPE)` to show the password of the administrator user.
