from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from db import database, Familia, CestaBasica, Beneficiario, Coleta, Ong
from routers import Familias_router, Beneficiarios_router, Coletas_router, Cestas_router, Ongs_router

# Criar uma instância do aplicativo FastAPI
app = FastAPI(title= "API da ONG", version="1.0.0")

app.include_router(Familias_router)
app.include_router(Beneficiarios_router)
app.include_router(Coletas_router)
app.include_router(Cestas_router)
app.include_router(Ongs_router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["*"]
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, log_level="info")
