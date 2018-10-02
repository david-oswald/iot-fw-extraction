## Amazon Echo Dot v2

CPU: Texas Instruments DM3725CUS100 (ARM Cortex A8)

## FW extraction
 * eMMC dump using easyJTAG, as documented in http://www.osdfcon.org/presentations/2017/Moran_Hyde-Alexa-are-you-skynet.pdf
 * No differences in pinout/process to Echo Plus

## Resources
 * Echo Dot V2 used to do firmware updates over HTTP
 * Full firmware update image still available at http://amzdigitaldownloads.edgesuite.net/obfuscated-otav3-9/1b9718ec2da663bb299676df977055c9/update-kindle-full_biscuit-272.5.6.4_user_564196920.bin
 * Echo Dot V2 now performs updates over HTTPS on softwareupdates.amazon.com
 * DEFCon 2018 rooting / exploits: https://github.com/tencentbladeteam/Exploit-Amazon-Echo

## OS
 * Running Android-based OS
 * Fastboot available if Amazon button is pressed during boot. Light ring turns green to indicate recovery mode.
 * Bootloader is locked, with no way of unlocking it without a key
