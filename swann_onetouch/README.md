# Swann OneTouch hub

1. Connect UART
2. Prepare XModem transfer of ```u-boot-spl.bin```
3. Power device, wait for CCCCC... then transfer ```u-boot-spl.bin``` via XModem
4. Now, YModem transfer ```u-boot.img```
5. Device will try to boot from flash, fail, drop into U-boot shell

From there, you can boot the kernel as follows:

```
nand read 0x80F80000 0x989000 0x800000
nand read 0x80200000 0x580000 0x800000
bootz 0x80200100 - 0x80F80DC8
```

You can also use ```dump.py``` (which uses UBoot ```nand dump```), but this is really slow and unoptimised.

However, with none of the below bootargs we could actually manage to fully get the system up:

```
setenv bootargs console=ttyO0,115200n8 root=/dev/mtdblock7 rootfstype=ubifs rootwait=1
setenv bootargs console=ttyO0,115200n8 root=ubi0:rootfs rw ubi.mtd=7,2048 rootfstype=ubifs rootwait=1
setenv bootargs 'console=ttyO0,115200n8 noinitrd ip=off mem=256M rootwait=1 rw ubi.mtd=7,2048 rootfstype=ubifs root=/dev/mtd7 init=/init'
```

Btw, binwalk shows the following offsets:

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
5505024       0x540000        JFFS2 filesystem, little endian
5767168       0x580000        ASCII cpio archive (SVR4 with no CRC), file name: "cpiosize.txt", file name length: "0x0000000d", file size: "0x00000010"
5767424       0x580100        Linux kernel ARM boot executable zImage (little-endian)
5783727       0x5840AF        gzip compressed data, maximum compression, from Unix, last modified: 1970-01-01 00:00:00 (null date)
10001864      0x989DC8        device tree image (dtb)
10037628      0x99297C        device tree image (dtb)
10073408      0x99B540        device tree image (dtb)
10109060      0x9A4084        ASCII cpio archive (SVR4 with no CRC), file name: "TRAILER!!!", file name length: "0x0000000b", file size: "0x00000000"
12058624      0xB80000        ASCII cpio archive (SVR4 with no CRC), file name: "cpiosize.txt", file name length: "0x0000000d", file size: "0x00000010"
12058880      0xB80100        Linux kernel ARM boot executable zImage (little-endian)
12075183      0xB840AF        gzip compressed data, maximum compression, from Unix, last modified: 1970-01-01 00:00:00 (null date)
16432404      0xFABD14        device tree image (dtb)
16468168      0xFB48C8        device tree image (dtb)
16503948      0xFBD48C        device tree image (dtb)
16539596      0xFC5FCC        ASCII cpio archive (SVR4 with no CRC), file name: "TRAILER!!!", file name length: "0x0000000b", file size: "0x00000000"
18350080      0x1180000       UBI erase count header, version: 1, EC: 0x2, VID header offset: 0x800, data offset: 0x1000
```

So we actually boot the recovery kernel, and only one device tree - it may make sense to try other kernels and DTs, and try to find the bootargs in the dump.bin that are actually used normally.

Note that all nand read have to be page-aligned, so we have to actually read from 0x580000 and then add the offset (0x100)
in the boot command. Same for the device tree images.
