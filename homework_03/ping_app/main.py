""" FastAPI 'Ping' app for uvicorn[.exe] """


from fastapi import FastAPI
from views.ping import router as ping_router


app = FastAPI()
app.include_router(ping_router)  # routes to "/ping[/....]"


# 'GET /'  ['get http://localhost:8000/']
@app.get("/")
def get_root():
    root_msg = (
        "This is the answer to 'GET /'.  You may also try 'GET /ping/' and 'GET /docs/'"
    )
    return root_msg
    # for Testing:
    #   curl -X 'GET http://localhost:8000/' -H 'accept: application/json'


def main():
    print("\nFastAPI's 'ping' app:  <./homework_03/main.py>\n")
    print(
        " * please launch me with something like 'uvicorn[.exe] main:app'\n"
        " * then open  http://localhost/docs"
    )


if __name__ == "__main__":
    main()
