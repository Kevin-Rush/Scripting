@echo off

rem For each file in  folder
for %%a in (".\*") do (
    rem check if the file has an extension and if it is not the script
    if "%%~xa" NEQ "" if "%%~dpxa" NEQ "%~dpx0"(
        rem check if extension folder exists, if not create
        if not exist "%%~xa" mkdir "%%~xa"
        rem move file to dir
        move "%%a" "%%~dpa%%~xa\"
    )
)