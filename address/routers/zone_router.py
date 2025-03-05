from fastapi import APIRouter, status, Depends
from address.models.zone_model import ZoneModel
from address.schemas.zone_schema import ZoneSchema, CreateZoneSchema, UpdateZoneSchema, ZoneResponseSchema
from fastapi.exceptions import HTTPException
from databse.database import get_session
from typing import List, Union
from sqlalchemy.ext.asyncio.session import AsyncSession
from address.services.zone_services import ZoneService
from uuid import UUID

zone_router = APIRouter(prefix='/api/zone')

service = ZoneService()


@zone_router.get("/", response_model=List[ZoneSchema])
async def get_all_zones(session: AsyncSession = Depends(get_session)):
    zones = await service.get_all_zone(session=session)
    return zones

@zone_router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_new_zone(zone_data:CreateZoneSchema, session: AsyncSession = Depends(get_session))->dict:
    new_zone = await service.create_zone(zone_data=zone_data, session=session)
    return new_zone

@zone_router.get("/{zone_id}", response_model=ZoneResponseSchema)
async def get_zone_by_id(zone_id:UUID, session: AsyncSession = Depends(get_session)):
    zone = await service.get_zone_by_id(zone_id=zone_id, session = session)
    if zone is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zone not found")
    return zone

@zone_router.put("/{zone_id}", response_model=ZoneResponseSchema)
async def update_zone(zone_id:UUID, update_data:UpdateZoneSchema, session: AsyncSession = Depends(get_session)):
    zone = await service.update_zone(zone_id=zone_id, update_data=update_data, session=session)
    if zone is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zone not found")
    return zone

@zone_router.delete("/{zone_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_user(zone_id:UUID, session: AsyncSession = Depends(get_session)):
    message: Union[str, None] = await service.delete_zone(zone_id=zone_id, session=session)
    if message is not None:
        return message
    return None


