from http.client import HTTPException
import json
from fastapi import FastAPI

with open ("mahasiswa.json", "r") as read_file:
    data =  json.load(read_file)
app = FastAPI()
@app.get("/mahasiswa/{NIM_mhs}")
async def read_mahasiswa(NIM_mhs: int):
    for mahasiswa_item in data['mahasiswa']:
        if mahasiswa_item['NIM'] == NIM_mhs:
            return mahasiswa_item
    raise HTTPException(status_code=404, detail=f'Not found')