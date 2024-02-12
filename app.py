from fastapi import FastAPI, File, UploadFile
from database import Database
from uuid import uuid4

app = FastAPI()
db = Database()

@app.get("/v1/find")
async def find_files(filename: str = "", date: str = ""):
    return await db.find_files(filename, date)

@app.post("/v2/upload")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_content = await file.read()
    uuid = str(uuid4())
    await db.save_file(uuid, filename, file_content)
    return {"uuid": uuid}

@app.get("/v1/download")
async def download_file(uuid: str):
    file_data = await db.get_file(uuid)
    if file_data is None:
        return {"error": "File not found"}
    return {"filename": file_data[1], "content": file_data[2]}
