fname = input('enter your first name : ')
lname = input('enter your last name : ')
email = input('enter your email : ')
phone = input('enter your phone number : ')
password = input('enter your password : ')
confirmPassword = input('confirm your password : ')


if (fname != '' and email != '' and lname != '' and phone != '' and password != '' and confirmPassword != ''):
   if password == confirmPassword :
      try:
         with open('employe.csv') as file:
            with open('employe.csv', 'a') as file :
               file.write(f"{fname},{lname},{email},{phone},{password}\n")
               print('your account successfully created')
      except FileNotFoundError : 
         with open('employe.csv', 'a') as file:
            file.write('fname,lname,email,phone,password\n')
            file.write(f"{fname},{lname},{email},{phone},{password}\n")
            print('your account successfully created')
   else: print('password not matched')  
else : print('not filled')