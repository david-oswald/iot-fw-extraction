# AccuChek Insulin Pump

See also https://hackaday.io/project/41162-hardware-hacking-of-accu-chek-performa-insight/details

## Components

 * iMX233 processor (MCIMX233DJM4C) running WindowsCE 6.0
 * Flash memory (4SD12 NW164)
 
## Extraction

 * UART available on group of three larger pinheader holes (near to a pattern of 6 vias south of the iMX233)
 * UART gives bootlog, pressing space on prompt ```Press [ENTER] to download now or [SPACE] to cancel.``` drops to bootloader, but then requires password (bootloader version is "Microsoft Windows CE Bootloader Common Library Version 1.4 Built Aug 20 2014 13:17:16")
 * SJTAG adaptor with OpenOCD enables dumping the system image loaded to 0x80200000 (see https://hackaday.io/project/41162-hardware-hacking-of-accu-chek-performa-insight/details) for details
 * SJTAG pins are on the second larger 3-pin holes
 
## ToDo

 * Dump bootloader via SJTAG and find password for easier analysis (?)
 
