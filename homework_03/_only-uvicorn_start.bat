@echo off

echo.
echo ################################################################################
echo # To start a Uvicorn (asgi http) server with 'main.py:app' in current dir, run:#
echo #                                                                              #
echo #    uvicorn.exe  main:app  --port=8000  --reload                              #
echo #                                                                              #
echo #    (VENV with 'Uvicorn[.exe]' must be activated beforehand!!)                #
echo #                                                                              #
echo ################################################################################
echo.
timeout /t 1 > nul


echo.
echo.
echo ** cd ping_app
cd ping_app
echo.
echo ** ..\.venv\Scripts\uvicorn.exe --port:8000 --reload  main:app
echo.
..\.venv\Scripts\uvicorn.exe --port:8000 --reload  main:app


echo.
echo.
echo (As no parameter was given to the current .bat - we do a pause before exit:)
if "%1"=="" pause
