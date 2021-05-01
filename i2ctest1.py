from smbus import SMBus
import time

addr=0x8
bus=SMBus(1) #/dev/ic2-1
#bus.write_byte(addr,0x0)
#bus.write_byte(addr,0x1)
while True:
    ans=input("1 --- LED ON / 0 --- LED OFF  ")
    #ans=1;
    if str(ans)=="1":
        bus.write_byte(addr,0x1)
        print("Ans is 1");
    elif str(ans)=="0":
        bus.write_byte(addr,0x0)
        print("Ans is 0");
        
    time.sleep(2);
        
    number = bus.read_byte(addr);
    print("Data Recieved from Arduino :"+str(number));