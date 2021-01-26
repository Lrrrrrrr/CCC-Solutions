#made by mohammed
p= int(input())
n= int(input)
r=int(input())
total = 0
newInfections = n

for day in range (0,11): 
  newInfections = newInfections*r
  total += newInfections
  
  if newInfections > p:
    print(day)
    break

