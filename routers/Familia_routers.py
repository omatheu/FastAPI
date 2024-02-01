from fastapi import HTTPException, APIRouter 
from schemas.Familia import FamiliaCreate, FamiliaUpdate
from db import database, Familia
from sqlalchemy import insert
from sqlalchemy.future import select

router = APIRouter(prefix="/familias")

# Rota para criar uma familia no banco de dados

@router.post("/inserir/", tags=["Familias"])
async def create_familia(familia: FamiliaCreate):
    try:
        familia_obj = await Familia.objects.create(**familia.dict())
        return {**familia.dict(), "id_familia": familia_obj.id_familia}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# Rota para listar todas as familias na database

@router.get("/listar-familias/", tags=["Familias"])
async def list_familias():
    try:
        familias = await Familia.objects.all()
        return familias
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# Rota para atualizar uma familia na database
@router.put("/atualizar/{id_familia}", tags=["Familias"])
async def update_familia(id_familia: int, familia: FamiliaUpdate, tags=["Familias"]):
    try:
        familia_obj = await Familia.objects.get(id_familia=id_familia)
        await familia_obj.update(**familia.dict())
        return {"message": "Familia atualizada com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# Rota para deletar uma familia na database
@router.delete("/deletar/{id_familia}", tags=["Familias"])
async def delete_familia(id_familia: int):
    try:
        familia_obj = await Familia.objects.get(id_familia=id_familia)
        await familia_obj.delete()
        return {"message": "Familia deletada com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
