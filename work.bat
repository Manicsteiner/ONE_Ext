@echo off
setlocal enabledelayedexpansion

for %%F in (*.atx.bytes) do (
    set "filename=%%~nF"
    
    if not exist "!filename!" (
        mkdir "!filename!"
    )

    cd "!filename!"

    C:\Soft\GARbro\GARbro.Console.exe -x "..\%%F"
    ..\imgdec.py
    for %%I in (*.png) do (
        move %%I ..\
    )
    cd ..
    rmdir /s /q "!filename!"
)