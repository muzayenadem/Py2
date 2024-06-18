import csv
print('login your account to delete')
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
           return  {'index':i,'data':user}
        i += 1
asure = asure()        
if asure == None:print('not such data')
else :
  beforeIndex = users[:asure['index']]
  afterIndex = users[asure['index']+1:]
  users = beforeIndex + afterIndex
  print(users)
  with open('employe.csv', 'w') as file:
      file.write('fname,lname,email,phone,password\n')
      print('your account successfully deleted')
      for user in users :
         file.write(f"{user['fname']},{user['lname']},{user['email']},{user['phone']},{user['password']}\n")
          