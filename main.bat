@echo off
:menu
cls
echo \\\\\\\\\\\\\\\\\\\\\\\\\\
echo \\         MENU         \\
echo \\    1. NEW RAPORT     \\
echo \\    2. BACKUP         \\
echo \\    3. EXIT           \\
echo \\\\\\\\\\\\\\\\\\\\\\\\\\
set /p in="Select option: "
if %in%==1 goto newRaport
if %in%==2 goto backup
if %in%==3 goto end
goto menu
:newRaport
cls
echo Wait...
if not exist input mkdir input
if not exist output mkdir output
if not exist report mkdir report
for /f %%x in ('dir /b input\') do ( charCounter.exe %%x
if errorlevel 0 echo DONE FOR: %%x
)
main.py
echo Done...
pause
goto menu
:backup
cls
echo Wait...
if not exist backup mkdir backup
set backupName=backup_%date:~10,4%-%date:~7,2%-%date:~4,2%_%time:~0,2%-%time:~3,2%.html
if exist "backup\%backupName%" echo Already exists
if not exist "backup\%backupName%" copy "report\report.html" "backup\%backupName%"
echo Done...
pause
goto menu
:end
