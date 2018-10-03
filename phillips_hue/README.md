# Philips Hue
The Phillips Hue Lights is a smart lighting system that can be controlled via a smartphone app, or even Amazon Alexa. The Phillips Hue Bridge is the central control of the lighting system. It processes commmands and executes them on the smart lights.

## Components

 * QCA4531-BL3A Qualcomm Wi-Fi Chip
 * Winbond W9751G6KB-25 512 MB RAM
 * Qualcomm QCA4531 SoC (MIPS CPU)
 * SKY 2438T 326FV ZigBee Chip
 * PL2303SA USB to Serial Bridge Controller
	
## Firmware extraction

See also procedure in https://forum.archive.openwrt.org/viewtopic.php?id=66346

 * UART running at 115200 baud
 * U-Boot available on UART, but bootdelay is set to 0, so the booting process cannot be interrupted by a key press.
 * Two different flash chips, the most probable case is that U-Boot resides on the NOR flash chip, while the firmware resides on the NAND flash chip. It is therefore possible to interrupt the booting process by disabling CPU access to NAND flash.
 * Pin R31 was identified as the data line between the processor and the NAND flash chip. It can be disconnected from the CPU by shorting pin R31 using a piece of wire connected to GND
 * With flash disabled, U-Boot starts, but fails to boot from NAND, dropping into the U-Boot CLI
 * Examining the U-Boot environment variables, we can see an interesting ```security''' variable with a value that looks like a UNIX shadow file entry. By changing this variable to the hash of a known password, the UART shell can be accessed (after re-enabling the NAND flash), yielding root permission.