# SmartI Smartbell Plus door lock

## Firmware extraction process

 1. Boot into u-boot commandline
 2. Set up minicom to capture output to a file
 3. Issue command in u-boot:  ```sf probe 0:0;sf read 0x8000000 0x0 0x800000;md.b 0x8000000 0x800000```
 4. Manually remove junk from output with text editor
 5. Convert hexdump to binary

The resulting binary contains u-boot and lzma-compressed flash contents
Extracted lzma archive from binary image using: 

```dd if=firmware_smartbell_plus.bin of=fs.lzma skip=928476 bs=1```

```lzma -d fs.lzma```  worked only once for some reason; Trying the command now gives corrupt lzma archive

## U-Boot environment variables

```=> printenv                                                                                                                                                                                                          
bootargs=                                                                                                                                                                                                            
bootcmd=sf probe 0:0;sf read 0x4000000 0xd6100 0x800000;go 0x4000000                                                                                                                                                 
bootdelay=3                                                                                                                                                                                                          
baudrate=38400                                                                                                                                                                                                       
ethaddr=00:42:70:00:30:22                                                                                                                                                                                            
ipaddr=10.0.1.52                                                                                                                                                                                                     
serverip=10.0.1.51                                                                                                                                                                                                   
gatewayip=10.0.1.51                                                                                                                                                                                                  
netmask=255.0.0.0                                                                                                                                                                                                    
ethact=FTMAC110#0                                                                                                                                                                                                    
ver=U-Boot 2008.10 (Jun 27 2011 - 09:46:43
```
