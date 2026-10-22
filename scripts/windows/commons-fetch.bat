@echo off
call "%~dp0_lib.bat"
set "RC="
rem Изображение с Wikimedia Commons → media/ урока и credits.toml (аргументы — как у scripts/commons_fetch.py или по запросу)
if "%~1"=="" goto ask
%PY% scripts\commons_fetch.py %*
goto end
:ask
set "SRC=" & set "DST=" & set "NAME=" & set "CAP="
set /p "SRC=Файл Commons (File:… или URL страницы): "
set /p "DST=Урок (.md) или каталог урока: "
set /p "NAME=Имя файла латиницей без расширения (Enter — из имени на Commons): "
set /p "CAP=Подпись (Enter — без подписи): "
set "ARGS="
if defined NAME set ARGS=--name "%NAME%"
if defined CAP set ARGS=%ARGS% --caption "%CAP%"
%PY% scripts\commons_fetch.py "%SRC%" "%DST%" %ARGS%
:end
if not defined RC set "RC=%ERRORLEVEL%"
rem Двойной щелчок: окно остаётся открытым, пока его не закроет пользователь (cmd /k вместо pause)
if not defined NOPAUSE echo %CMDCMDLINE% | find /i " /c" >nul && (echo. & echo Введите exit или закройте окно. & cmd /k)
exit /b %RC%
