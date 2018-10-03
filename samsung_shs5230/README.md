# Samsung Smart Lock SHS-5230

## Components

 * Mainboard uses Atmega64A
 * RF board uses Atmega88PA
 * Fingerprint module uses unknown CPU
 
## Extraction

### Mainboard

* JTAG port is available on 10 pins of a 16 pin connector near the backside of the battery holder
* Readout protection is inactive
* Firmware can be read with any JTAG-capable AVR programmer (e.g. AVRDragon)

### RF board
* Board labelled (in silkscreen) as GC41-0731A Rev 01
* ISP port is available on 6-pin connector labelled J2
* Readout protection is inactive
* Firmware can be read with any ISP-capable AVR programmer (e.g. AVRDragon)
