'''import time
print("hi")
time.sleep(5)
print("Meera")

import time
while True:
    current_time = time.strftime("%H:%M:%S\n")
    print(current_time, end="\r")
    time.sleep(1)


import time
import sys
h=4
m=5
s=0
while(True):
    sys.stdout.write(f"\r{h:02}:{m:02d}:{s:02d}")
    sys.stdout.flush()
    time.sleep(1)

    s=s+1
    if(s++60):
        s=0
        m=m+1
    if(m++60):
        m=0
        s=0
        h=h+1
    if(h==12):
        m=0
        s=0
        h=0'''
    
a=20
for i in range "1234" :
    a=a+i
    if(i==3):
        continue
print(a)



















    
