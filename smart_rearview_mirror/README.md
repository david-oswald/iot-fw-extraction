# Junsun Smart Rearview Mirror

## Description
* Device runs Android 4.4.2
* Standard Android partition layout, e.g. data partition is at ```/dev/block/by-name/data``` (ext4)

## Extraction

* Enable Developer Options by opening Settings -> Tablet, and clicking on the model number (Q6) 10 times
* Enable USB debugging in the Developer Options now available in Settings
* Connect to PC via MicroUSB
* ```adb shell``` yields a root shell on the device
* For imaging, install busybox for netcat: ```adb install BusyBox v1.27.1 apkpure.com.apk``` (assuming you have the apk downloaded locally)
* Forward a port from the device to a local port: ```adb forward tcp:8888 tcp:8888```
* From the adb shell, start netcat on the device with the target partition (here data partition): ```busybox nc -l -p 8888 -e dd if=/dev/block/by-name/data```
* On the PC, receive image with netcat: ```nc 127.0.0.1 | pv -i 0.5 > data.img```
* For mounting the image, you may need to repair the ext4 filesystem using ```fsck.ext4 -v data.img```