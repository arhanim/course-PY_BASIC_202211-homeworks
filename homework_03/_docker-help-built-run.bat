@echo off
chcp 1251 > nul

echo.
echo -------------------------------------------------------------------------------
echo !                                                                             !
echo ! Docker install under Windows:                                               !
echo !    download 'Docker Desktop' application, or use 'WSL2' linux subsystem!    !
echo !                                                                             !
echo -------------------------------------------------------------------------------
echo.
echo.
echo # Docker client version:
echo      docker --version
echo.
echo # List (locally available or downloaded) images:
echo      docker images
echo.
echo # List containers (will connect to Docker engine, so Docker must be running!):
echo      docker ps
echo.
echo # Run container, 'hello-world' or 'getting-started' for ex.: [download if not found locally]
echo      docker run hello-world
echo      docker run -d -p 80:80 docker/getting-started
echo.
echo # Build image from '.\Dockerfile' content:
echo      docker build . --tag py3.10
echo.
echo # Run a command in a new container:
echo      docker run --rm -it  -p 8080:8000 py3.10 bash
echo.
echo # Example:
echo      docker run --rm -it  -p 8000:8000 hmw_03-py3.9  [--detach]
echo         [where:  --rm  'remove container when it exits',
echo                  -it   '...',
echo                  -p == --port??  '...',
echo                  --detach  ==  -d  'run in background'.]
echo -------------------------------------------------------------------------------
timeout /t 1 > nul


echo.
echo.
echo @
echo @ NOW let's build our docker image:
echo @
echo.
echo ** docker build . --tag hmw_03-py3.9
echo.
docker build . --tag hmw_03-py3.9


echo.
echo.
echo @
echo @ and RUN it as a container:
echo @
echo.
echo ** docker run --rm -it  -p 8000:8000 hmw_03-py3.9
echo.
docker run --rm -it  -p 8000:8000 hmw_03-py3.9

echo.
echo.
echo (As no parameter was given to the current .bat  -  we do a pause before exit:)
if "%1"=="" pause
