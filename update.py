import csv
print('login your account to update ')
email = input('enter your email : ')
password = input('enter your password : ')
users = []
try:
   with open('employe.csv') as file:
      reader  = csv.DictReader(file)
      for user in reader:
         users.append(user)
except FileNotFoundError :
   print('there is no such file here')


def asure():
      i = 0
      for user in users:
        if user['email'] == email and user['password'] == password :
           fname = input(f"enter new first name to replace {user['fname']} : ")
           lname = input(f"enter new last name to replace {user['lname']} : ")
           email2 = input(f"enter new email to replace {user['email']} : ")
           phone = input(f"enter new phone to replace {user['phone']} : ")
           password2 = input(f"enter new password to replace {user['password']} : ")
           newdata = {'fname':fname,'lname':lname,'email':email2,'phone':phone,'password':password2}
           return  {'index':i,'data':newdata}
        i += 1
asure = asure()        
if asure == None:print('not such data')
else :
   print(users)
   users[asure['index']] = asure['data']
   with open('employe.csv', 'w') as file:
      file.write('fname,lname,email,phone,password\n')
      for user in users :
         file.write(f"{user['fname']},{user['lname']},{user['email']},{user['phone']},{user['password']}\n")