input = int(input())
hour = 12
minute = 0
counter = 0 

for i in range (input):
  minute = int(minute)
  hour = int(hour)
  minute += 1 
  if minute >= 60:
    minute -= 60
    if hour + 1 < 13:
      hour += 1
    else:
      hour = (hour + 1) % 12
  if minute < 10:
    minute = "0" + str(minute)
  else:
    minute = minute 
  minute = str(minute)
  hour = str(hour)
  time = hour + minute
  lengthtime = len(time)
  if lengthtime == 3:
    if (int(time[2]) - int(time[1])) == (int(time[1]) - int(time[0])):
      counter += 1 
  else:
    if ((int(time[3]) - int(time[2])) == (int(time[2]) - int(time[1]))) and ((int(time[2]) - int(time[1])) == (int(time[1]) - int(time[0]))):
      counter += 1 
  
print(counter)