from sqlmodel.ext.asyncio.session import AsyncSession
from address.models.zone_model import ZoneModel
from address.schemas.zone_schema import ZoneSchema, CreateZoneSchema, UpdateZoneSchema, ZoneResponseSchema
from sqlmodel import select, asc

class ZoneController:

    async def get_all_zone(self, session:AsyncSession):
        statement = select(ZoneModel).order_by(asc(ZoneModel.name))

        result = await session.exec(statement=statement)
        return result.all()

    async def get_zone_by_id(self, zone_id:str, session:AsyncSession):
        statement = select(ZoneModel).where(ZoneModel.id == zone_id)

        result = await session.exec(statement=statement)

        zone = result.first()

        return zone if zone is not None else None



    async def create_zone(self, zone_data:CreateZoneSchema, session:AsyncSession):
        zone_data_dict = zone_data.model_dump()

        new_zone =ZoneModel(**zone_data_dict)

        session.add(new_zone)

        await session.commit()

        return new_zone

    async def update_zone(self, zone_id:str, update_data: UpdateZoneSchema, session:AsyncSession):
        zone_to_update = await self.get_zone_by_id(zone_id, session)

        if zone_to_update is not None:
            update_data_dict = update_data.model_dump()
            for k, v in update_data_dict.items():
                setattr(zone_to_update, k, v)
            
            await session.commit()
                
            return zone_to_update
        
        else:
            return None

    
    async def delete_zone(self, zone_id:str, session:AsyncSession)->dict:
        zone_to_delete = await self.get_zone_by_id(zone_id=zone_id, session=session)

        if zone_to_delete is not None:
            await session.delete(zone_to_delete)
            await session.commit()
            return {"message":"Zone deleted successfully"}

        else:
            return None
        