# DroiBOX MGX

 * CPU: Amlogic S9 chipset (ARM Cortex A53)
 * UART baud rate: 115200
 * User is "shell", but "su" gives us root permissions
 * Firmware consists of individual block devices extracted from /dev/block
 * Firmware extracted via UART by inserting an external SD card and copying the block devices onto that
