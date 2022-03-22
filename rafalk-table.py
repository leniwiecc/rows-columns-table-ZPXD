def funkcja(r, c):
   i=0
   for a in range(0, r):
      temp=[]
      for b in range(0, c):
         temp.append(i)
         if i ==9:
            i=0
         else:
            i +=1
      print(*temp)
      temp.clear()
funkcja(3,4)
