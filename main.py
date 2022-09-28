from http.client import HTTPException
import json
from fastapi import FastAPI
from pydantic import BaseModel

class mahasiswa_item(BaseModel):
    Nama: str
    NIM: int

data = []

with open("mahasiswa.json", "r") as read_file: 
    data = json.load(read_file)

app = FastAPI()
@app.get('/mahasiswa/{NIM}')
async def read_mahasiswa(NIM: int):
    for mahasiswa in data['mahasiswa']:
        if mahasiswa['NIM'] == NIM:
            return mahasiswa
    raise HTTPException(
        status_code=404, detail=f'Item not found')

@app.post("/mahasiswa")
async def add_mahasiswa(mahasiswa_baru: mahasiswa_item):
    new_mahasiswa = [
        {
            "NIM": mahasiswa_baru.NIM,
            "NAMA": mahasiswa_baru.Nama
        }
    ]
    data['mahasiwa'].append(new_mahasiswa)
    return data