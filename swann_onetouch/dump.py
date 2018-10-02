#!/usr/bin/python
import serial

offset = 0;

pagesize = 2048;
cnt = 65536

startp = 26012;


#COM_PORT = 'com22'
COM_PORT = 'com5'
BAUDRATE = 115200

# stopped at page 26012


ser = serial.Serial(COM_PORT, BAUDRATE, timeout=1)


fp = open('dump.txt','w') 
 
for p in range(startp, cnt):
    
    print "== Page " + str(p)
    
    buf = 'nand dump 0x{:08X}\n'.format(offset + p*pagesize)

    ser.write(buf)

    # Get answer
    ser.readline()
    ser.readline()
    
    rx = ''
    
    for l in range (128):
        rx += ser.readline()
        
    # read remaining data
    for l in range (9):
        ser.readline()
    
    rx = rx.replace('\t', '')
    rx = rx.replace('  ', ' ')
    rx = rx.replace('\n', '')
   
    print rx
    fp.write(rx)    
    
    ser.flush()
    

fp.close()
ser.close()
