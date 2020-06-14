import datetime 

now = datetime.datetime.now()

filename = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute)

f = open(filename, "w+")
f.close()

