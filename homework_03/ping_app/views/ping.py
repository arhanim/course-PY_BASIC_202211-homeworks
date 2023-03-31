""" 'ping' VIEW """

import json

from fastapi import APIRouter, Response


router = APIRouter(tags=["Ping queries"])


# 'GET /ping/'  ['get http://localhost:8000/ping/']
@router.get("/ping/")
def get_ping():
    return Response(  # use "Response" when needed to return some data as json
        content=json.dumps({"message": "pong"}),
        media_type="application/json",  # Response here is JSON! =)
    )
    # for Testing:
    #   curl -X 'GET http://localhost:8000/ping/' -H 'accept: application/json'
