ai , bi = input().split()
ci,di =  input().split()
t = int(input())

a, b = int(ai), int(bi)

c, d = int(ci), int(di)

Distance = 0
Difference = 0
# Vertical

if a > c:
  Distance += a - c
else:
  Distance += c - a

# Horizontal 

if b>d:
  Distance += b - d
else:
  Distance += d - b
if t == Distance:
  print("Y")
else:
  if (t>Distance):
    Difference = t - Distance 
  else: 
    Difference = Distance - t
  if (Difference % 2 == 0):
    print ("Y")
  else:
    print ("N")



# -138 - 825

# 258 # 130

# 8358