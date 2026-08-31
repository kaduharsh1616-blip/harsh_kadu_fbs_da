###userid and password display a 4 digit random number and ask user to enter the
##same. If user enters the same number then show him success message or failed

correct_userid = "harshkadu"
correct_password = "7777"
correct_capta = "1234"

userid = (input('enter the userid:'))
password = (input('enter the password:'))
capta =int(input('enter the capta:'))


if (userid == correct_userid ,  password == correct_password):
  print('password is correct:')
  if( capta == correct_capta):
    print('sucessful:')
  else:
    print('uncessful:')

else:
  print('passwoed is incorrect:')
        
       
