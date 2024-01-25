from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    contents = {"Message": "This is basic structure for FastApi project"}
    return JSONResponse(content=contents, status_code=status.HTTP_200_OK)