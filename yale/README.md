# Yale EasyFit
The Yale Easy Fit Smartphone Alarm is a wireless home alarm system that can be fully controlled from an mobile app. The alarm kit consists of motion sensors, wireless cameras, keypad, wireless remote, central unit and a siren. The alarm can be disabled or enabled from the mobile app. When the system is armed, the mobile app pushes notifications in case the motion sensors go off. The central unit will be the focus of our research.

## Components

 * Freescale MK60 CPU

## Extraction

 * UART available on CON3 near CPU, but only outputs proprietary debug info; does not respond to input
 * JTAG available on J3 with mounted header and standard pinout
 * Use any JTAG programmer for MK60 to extract binary, e.g. with J-Link: ```savebin firmware.bin 0x0 0x80000```
 