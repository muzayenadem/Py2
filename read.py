import csv
data = []

with open('employe.csv') as file:
   read = csv.DictReader(file)
   for read in read:
      data.append(read)
for user in sorted(data, key= lambda user : user['fname']):
   print(f"{user['fname']} {user['lname']}" )

def userData():
   for user in data:
      if user['fname'] == 'Muzayen':
         return user

if userData() == None:
   print('there is no such data')
else:
   print(userData())