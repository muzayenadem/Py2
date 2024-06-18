da = [1,2,3,4,5,6,7,8]

k = 0
for i in da:
   if i  == 4 :
      db = da[:k]
      db2 = da[k+1:]
      con= db + db2
      print(db)
      print(db2)
      print(con)
   k+=1
   
