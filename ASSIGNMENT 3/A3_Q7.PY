##a program to check if user has entered correct userid and password.

correct_userid = "harshkadu"
correct_password = "7777"


userid = (input('enter the userid:'))
password= (input('enter the password:'))


if (userid == correct_userid and  password == correct_password ):
  print('password is correct:')
else:
  print('passwoed is incorrect:')
