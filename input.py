import serial
import time

#Setting
SerialPort = 'COM3'
directory = "D:\\data.xml"

ard = serial.Serial(SerialPort)

while 1:
   obj = ard.next()

   for i in range(len(obj)):
      if obj[i]=='C':
        j=i
      if obj[i]=='P':
         k=i

   tem = float(obj[0:(j-1)])
   hu = float(obj[(j+1):(k-1)])
   print tem,'C', hu,'%'
   year = time.localtime().tm_year
   mon = time.localtime().tm_mon
   day = time.localtime().tm_mday
   hour = time.localtime().tm_hour
   min = time.localtime().tm_min
   sec = time.localtime().tm_sec
   f = open(directory,'w')
   data = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<data>\n<temperature>\n"+ obj[0:(j-1)] + "\n</temperature>\n<humidity>\n" + obj[(j+1):(k-1)] + "\n</humidity>\n<year>\n"+str(year)+"\n</year>\n<mon>\n"+str(mon)+"\n</mon>\n<day>\n"+str(day)+"\n</day>\n<hour>\n"+str(hour)+"\n</hour>\n<min>\n"+str(min)+"\n</min>\n<sec>\n"+str(sec)+"\n</sec>\n</data>\n"
   f.write(data)
   f.close()