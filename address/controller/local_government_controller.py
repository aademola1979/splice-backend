from sqlmodel.ext.asyncio.session import AsyncSession
from address.models.state_model import StateModel
from address.models.local_government_model import LGAModel
from address.schemas.local_government_area_schema import LocalGovernmentAreaSchema, CreateLocalGovernmentAreaSchema, UpdateLGASchema
from sqlmodel import select, asc
from address.models.zone_model import ZoneModel
from uuid import UUID


class LocalGovernmentController:

    async def read_local_government_areas(self, session: AsyncSession):
        statement= select(LGAModel)
        result = await session.exec(statement=statement)
        result = result.all()

        return result if result is not None else None
    
    async def get_lga_by_id(self, lga_id:UUID, session: AsyncSession):
        statement = select(LGAModel).where(LGAModel.id == lga_id)
        statement = await session.exec(statement=statement)
        result = statement.first()
        
        return result if result is not None else None



    async def get_lga_with_detail_by_id(self, session:AsyncSession, lga_id:UUID):
        statement = select(
            (LGAModel.name).label("local_government_name"),
            (LGAModel.code).label("local_government_code"),
            (LGAModel.id).label("local_government_id"), 
            (StateModel.name).label("state_name"),
            (StateModel.code).label("state_code"),
            (StateModel.id).label("state_id"),
            (ZoneModel.name).label("zone_name"),
            (ZoneModel.code).label("zone_code"),
            (ZoneModel.id).label("zone_id"),
            ).where(LGAModel.id == lga_id).join_from(StateModel, LGAModel).where(LGAModel.state_id == StateModel.id).join(ZoneModel).where(ZoneModel.id == StateModel.zone_id)
        result = await session.exec(statement=statement)
        result = result.first()
        return result if result is not None else None
    
    async def create_lga(self, lga_data:CreateLocalGovernmentAreaSchema, session:AsyncSession):
        lga_data_dict = lga_data.model_dump()

        new_lga = lga_data(**lga_data_dict)

        session.add(new_lga)

        await session.commit()

        return new_lga
    
    async def update_lga(self, lga_id: UUID, update_data:UpdateLGASchema, session:AsyncSession):
        lga_to_update= await self.get_lga_by_id(lga_id, session=session)

        if lga_to_update is not None:
            update_data_dict = update_data.model_dump()
            for k, v, in update_data_dict.items():
                setattr(lga_to_update, k, v)

            await session.commit()

            return lga_to_update
        else:
            return None

        