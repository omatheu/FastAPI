from fastapi import HTTPException, APIRouter 
from db import database, Coleta
from schemas.Coleta import ColetaCreate, ColetaUpdate

router = APIRouter(prefix="/coletas")

# Pensar um pouco melhor nessas rotas, porque não esta fazendo muitp sentido fazer um post sem associar a uma familia e um get apenas com uma familia associada

@router.get("/buscar/{id_familia}", tags=["Coleta"])
async def get_coletas(id_familia: int):
    try:
        coletas = await Coleta.objects.filter(id_familia=id_familia).order_by('-data_coleta').all()
        if coletas:
            return coletas
        else:
            return []
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/criar/", tags=["Coleta"])
async def create_coleta(coleta: ColetaCreate):
    try:
        coleta_obj = await Coleta.objects.create(**coleta.dict())
        return {**coleta.dict(), "id": coleta_obj.id_coleta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.put("/atualizar/{id_coleta}", tags=["Coleta"])
async def update_coleta(id_coleta: int, coleta: ColetaUpdate):
    try:
        coleta_obj = await Coleta.objects.get(id_coleta=id_coleta)
        await coleta_obj.update(**coleta.dict())
        return {"message": "Coleta updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")