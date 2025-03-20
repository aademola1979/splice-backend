from fastapi import APIRouter, status, Depends
from address.models.state_model import StateModel
from address.schemas.local_government_area_schema import LocalGovernmentAreaWithStateSchema, LocalGovernmentAreaSchema
from fastapi.exceptions import HTTPException
from database.database import get_session
from typing import List, Union
from sqlalchemy.ext.asyncio.session import AsyncSession
from address.controller.local_government_controller import LocalGovernmentController
from uuid import UUID

lga_router = APIRouter(prefix="/api/lga")

controller = LocalGovernmentController()

@lga_router.get("/", response_model=List[LocalGovernmentAreaSchema])
async def read_lga(session:AsyncSession=Depends(get_session)):
    data = await controller.read_local_government_areas(session=session)

    if data is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return data

@lga_router.get("/{lga_id}", response_model=LocalGovernmentAreaSchema)
async def read_single_lga(lga_id:UUID, session:AsyncSession = Depends(get_session)):
    data = await controller.read_single_lga(session=session, lga_id=lga_id)
    if data is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return data


@lga_router.get("/detailed_lga/{lga_id}", response_model=Union[LocalGovernmentAreaWithStateSchema, None])
async def lga_info(lga_id: UUID, session: AsyncSession = Depends(get_session)):
    data = await controller.state_with_zone(session=session, lga_id=lga_id)
    if data is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return data