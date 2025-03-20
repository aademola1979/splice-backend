from sqlmodel.ext.asyncio.session import AsyncSession
from address.models.state_model import StateModel
from address.models.local_government_model import LGAModel
from address.schemas.state_schema import StateSchema, CreateStateSchema, UpdateStateSchema, StateResponseSchema
from address.schemas.local_government_area_schema import LocalGovernmentAreaSchema
from sqlmodel import select, asc
from address.models.zone_model import ZoneModel
from uuid import UUID

class StateController:

    async def get_all_states(self, session:AsyncSession):
        statement = select(StateModel).order_by(asc(StateModel.name))

        result = await session.exec(statement=statement)
        return result.all()

    async def get_state_by_id(self, state_id:str, session:AsyncSession):
        statement = select(StateModel).where(StateModel.id == state_id)

        result = await session.exec(statement=statement)

        _state = result.first()

        return _state if _state is not None else None



    async def create_state(self, state_data:CreateStateSchema, session:AsyncSession):
        state_data_dict = state_data.model_dump()

        new_state =StateModel(**state_data_dict)

        session.add(new_state)

        await session.commit()

        return new_state

    async def update_state(self, state_id:UUID, update_data: UpdateStateSchema, session:AsyncSession):
        state_to_update = await self.get_state_by_id(state_id, session)

        if state_to_update is not None:
            update_data_dict = update_data.model_dump()
            for k, v in update_data_dict.items():
                setattr(state_to_update, k, v)
            
            await session.commit()
                
            return state_to_update
        
        else:
            return None

    
    async def delete_state(self, state_id:str, session:AsyncSession)->dict:
        state_to_delete = await self.get_state_by_id(state_id=state_id, session=session)

        if state_to_delete is not None:
            await session.delete(state_to_delete)
            await session.commit()
            return {"message":"Zone deleted successfully"}

        else:
            return None
        
    async def state_with_zone(self, session:AsyncSession, state_id:UUID):
        statement = select(
            (LGAModel.name).label("local_government_name"), 
            (StateModel.name).label("state_name"),
            (ZoneModel.name).label("zone_name"),
            (LGAModel.id).label("local_government_id"),
            ).where(StateModel.id == state_id).join(ZoneModel).where(StateModel.zone_id == ZoneModel.id).join(LGAModel).where(LGAModel.state_id == state_id)
        result = await session.exec(statement=statement)
        result = result.first()
        print(f'My result: {result}')

        return result if result is not None else None
