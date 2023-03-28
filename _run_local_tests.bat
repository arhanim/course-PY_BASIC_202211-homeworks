@echo off
cls

echo ** pytest testing/test_homework_01 -s -vv
pytest testing/test_homework_01 -s -vv
pause

echo.
echo ** pytest testing/test_homework_02 -s -vv
pytest testing/test_homework_02 -s -vv
pause
