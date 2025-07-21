from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from logic import process_excel
import shutil

app = FastAPI()

# Permitir acesso do navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    path = f"uploads/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_excel(path)
    return {"juncoes": result}
