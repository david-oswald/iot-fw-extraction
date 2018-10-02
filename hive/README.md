# Hive nano v2

 * CPU: Texas Instruments AM3352BZCE30 (MPU ARM Cortex A8 32-Bit RISC Processor)
 * Memory dump by connecting to eMMC
 * Hub Manager daemon (Apache QPid AMQP Java Broker) running on port 5672 (might listen just on localhost) - username & pass: "guest"
 * Uses opkg with client-side certificate for updates
 * Binary tlsdate is used to get NTP time from google servers. It checks the server's certificate, but looks like it accepts the connection even if certificate doesn't match. If incorrect time is supplied package update would fail, as packages would appear out of date.
 * Device has functions for both NAND and eMMC FLASH. Maybe legacy support? (Hive Nano v1)
