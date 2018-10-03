# Smart-I Smartbell Plus door lock

The Smart-I WiFi Doorbell is a WiFi enabled unit that is installed outside the front door of a house. The doorbell has a camera, which is activated when a visitor presses the doorbell. The smart doorbell can also be equipped with an optional door release. Using an Android or iOS app, the user can see the video from the camera, speak to the visitor using the doorbell's built-in speakers, and open the door remotely.

## Firmware extraction process

 * UART is at 38400 baud
 * Boot into u-boot commandline
 * Set up serial terminal program to capture output to a file
 * Issue command in u-boot:  ```sf probe 0:0;sf read 0x8000000 0x0 0x800000;md.b 0x8000000 0x800000```
 * Manually remove junk from output with text editor
 * Convert hexdump to binary

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
## Analysis/decompression of image
Binwalk yields:

```
  root@localhost:~$ binwalk firm.bin
  
  DECIMAL       HEXADECIMAL     DESCRIPTION
  --------------------------------------------------------------------------------
  768048        0xBB830         CRC32 polynomial table, little endian
  928476        0xE2ADC         LZMA compressed data, properties: 0x5D, dictionary size: 33554432 bytes, uncompressed size: -1 bytes

  root@localhost:~$ dd if=firm.bin of=firm.lzma bs=1 skip=928476
  root@localhost:~$ unelzma firm.lzma
  root@localhost:~$ binwalk firm

  DECIMAL       HEXADECIMAL     DESCRIPTION
  --------------------------------------------------------------------------------
  157812        0x26874         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/config_8126", file name length: "0x00000013", file size: "0x00000AF0"
  160744        0x273E8         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/boot_vga.sh", file name length: "0x00000013", file size: "0x000007D4"
  162880        0x27C40         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/udhcpd_RT.conf", file name length: "0x00000016", file size: "0x00000BD1"
  166040        0x28898         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/ipc_ruanjin.cfg", file name length: "0x00000017", file size: "0x0000212E"
  174672        0x2AA50         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/isp_ov9710.cfg", file name length: "0x00000016", file size: "0x000076DE"
  205236        0x321B4         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/simple_ipc", file name length: "0x00000012", file size: "0x0002C806"
  387644        0x5EA3C         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/ipc.cfg", file name length: "0x0000000F", file size: "0x00002036"
  396020        0x60AF4         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/alarm.pcm", file name length: "0x00000011", file size: "0x00012FC0"
  473908        0x73B34         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/gmdvr_mem.cfg", file name length: "0x00000015", file size: "0x00001AB4"
  480876        0x7566C         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/gmdvr_mem_vga.cfg", file name length: "0x00000019", file size: "0x00001AB1"
  487848        0x771A8         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/gmdvr_mem_720p.cfg", file name length: "0x0000001A", file size: "0x00001AB4"
  494820        0x78CE4         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/wpa_supplicant_rt8192.conf", file name length: "0x00000022", file size: "0x000000B1"
  495144        0x78E28         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/ipc_ruanjin_vga.cfg", file name length: "0x0000001B", file size: "0x00001792"
  501320        0x7A648         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/udhcpd_RTL.conf", file name length: "0x00000017", file size: "0x00000BCF"
  504480        0x7B2A0         ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/deamon_pppp_device.sh", file name length: "0x0000001D", file size: "0x0000017F"
  1177360       0x11F710        ASCII cpio archive (SVR4 with no CRC), file name: "/manuf/wpa_supplicant_ar1021.conf", file name length: "0x00000022", file size: "0x000001D6"
  12968961      0xC5E401        Certificate in DER format (x509 v3), header length: 4, sequence length: 1364
  14565237      0xDE3F75        Certificate in DER format (x509 v3), header length: 4, sequence length: 1284
  16348385      0xF974E1        Certificate in DER format (x509 v3), header length: 4, sequence length: 1460
  16468028      0xFB483C        Linux kernel version "2.6.28 (root@larry-virtual-machine) (gcc version 4.4.1 (Sourcery G++ Lite 2009q3-67) ) #328 PREEMPT Tue Jan 20 12:09:47 CST 2015"
  16483656      0xFB8548        gzip compressed data, maximum compression, from Unix, last modified: 2015-01-17 02:24:07
  17266002      0x1077552       Copyright string: "Copyright (c) 2006-2007 BalaBit IT Ltd."
  17551728      0x10BD170       YAFFS filesystem
 ```

