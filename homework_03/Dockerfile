#
# __ Containerized FastAPI's  "ping" App __
#
# To build this Docker image and run it as a container, type in shell (CMD, bash, etc):
#
#    cd <folder_with_current_Dockerfile>
#    docker build .  --tag hmw_03-py3.9
#    docker run --rm  -it  -p 8000:8000 hmw_03-py3.9
#
#    [and then open http://localhost:8000 in your browser]
#


FROM python:3.9-buster

EXPOSE 8000
ENV PYTHONUNBUFFERED=1
RUN pip install poetry==1.4.1
RUN poetry config virtualenvs.create false

WORKDIR /var/ping_app
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY ./ping_app ./
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
