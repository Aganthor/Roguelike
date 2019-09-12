echo off
IF %1==32 GOTO 32bit
if %1==64 GOTO 64bit

:32bit
copy /Y .\dll\32bits\*.dll .

:64bit
copy /Y .\dll\64bits\*.dll .