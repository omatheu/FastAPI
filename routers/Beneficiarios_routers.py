from fastapi import HTTPException, APIRouter 
from db import database, Beneficiario
from schemas.Beneficiario import BeneficiarioCreate, BeneficiarioUpdate

router = APIRouter(prefix="/beneficiario")

# Rota para listar todos os beneficiarios na database
@router.get("/listar", tags=["Beneficiario"])
async def list_beneficiarios():
    try:
        beneficiarios = await Beneficiario.objects.all()
        return beneficiarios
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(err)}")
    
# Rota para criar um beneficiario no banco de dados
@router.post("/", tags=["Beneficiario"])
async def create_beneficiario(beneficiario: BeneficiarioCreate):
    try:
        beneficiario_obj = await Beneficiario.objects.create(**beneficiario.dict())
        return {**beneficiario.dict(), "id": beneficiario_obj.id_beneficiario}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(err)}")

@router.delete("/{id}", tags=["Beneficiario"])
async def delete_beneficiario(id_beneficiario: int):
    try:
        beneficiario = await Beneficiario.objects.get(id_beneficiario=id_beneficiario)
        await beneficiario.delete()
        return {"message": "Beneficiario deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# Rota para atualizar um beneficiario no banco de dados
@router.put("/{id}", tags=["Beneficiario"])
async def update_beneficiario(id: int, beneficiario: BeneficiarioUpdate):
    """
    Atualiza um beneficiário existente.

    Esta rota recebe um ID de beneficiário e um objeto BeneficiarioUpdate.
    O beneficiário com o ID fornecido será atualizado com os valores no objeto BeneficiarioUpdate.
    """
    try:
        beneficiario_obj = await Beneficiario.objects.get(id_beneficiario=id)
        await beneficiario_obj.update(**beneficiario.dict())
        return {"message": "Beneficiario updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")