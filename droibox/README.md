# DroiBOX MGX

## Components
 * CPU: Amlogic S9 chipset (ARM Cortex A53) 
 * OS: Android 4.4.2 Jelly Bean
 * Internal Storage: 8GB NAND Flash
 
## Extraction
 * UART baud rate 115200
 * User is "shell", but "su" gives us root permissions
 * Firmware consists of individual block devices extracted from /dev/block
 * Firmware extracted via UART by inserting an external SD card and copying the block devices onto that:
 
 ```
  shell:/ # su
  root:/ # mount /dev/mmcblk0p4 /mnt
  root:/ # cat /dev/block/boot > /mnt/boot
  root:/ # cat /dev/block/cache > /mnt/cache
  root:/ # cat /dev/block/crypt > /mnt/crypt
  root:/ # cat /dev/block/data > /mnt/data
  root:/ # cat /dev/block/instaboot > /mnt/instaboot
  root:/ # cat /dev/block/logo > /mnt/logo
  root:/ # cat /dev/block/misc > /mnt/misc
  root:/ # cat /dev/block/recovery > /mnt/recovery
  root:/ # cat /dev/block/rsv > /mnt/rsv
  root:/ # cat /dev/block/system > /mnt/system
 ```
