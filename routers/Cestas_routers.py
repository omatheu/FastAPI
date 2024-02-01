#Provavelmente terei que criar novas rotas para a cesta básica.

from fastapi import HTTPException, APIRouter 
from db import database, CestaBasica
from schemas.CestaBasica import CestaBasicaCreate

router = APIRouter(prefix="/cestas")

# Rota para criar uma cesta básica no banco de dados
@router.post("/inserir/", tags=["Cestas"])
async def create_cesta(cesta: CestaBasicaCreate):
    try:
        cesta_obj = await CestaBasica.objects.create(**cesta.dict())
        return {**cesta.dict(), "id": cesta_obj.id_cesta_basica}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")