from fastapi import APIRouter, status, Depends
from address.models.state_model import StateModel
from address.schemas.state_schema import StateSchema, CreateStateSchema, UpdateStateSchema, StateResponseSchema
from fastapi.exceptions import HTTPException
from databse.database import get_session
from typing import List, Union
from sqlalchemy.ext.asyncio.session import AsyncSession
from address.services.state_services import  StateService
from uuid import UUID

state_router = APIRouter(prefix='/api/state')

service = StateService()


@state_router.get("/", response_model=List[StateSchema])
async def get_all_states(session: AsyncSession = Depends(get_session)):
    _states = await service.get_all_states(session=session)
    return _states

@state_router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_new_state(state_data:CreateStateSchema, session: AsyncSession = Depends(get_session))->dict:
    new_state = await service.create_state(state_data=state_data, session=session)
    return new_state

@state_router.get("/{state_id}", response_model=StateResponseSchema)
async def get_state_by_id(state_id:UUID, session: AsyncSession = Depends(get_session)):
    _state = await service.get_state_by_id(state_id=state_id, session = session)
    if _state is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="State not found")
    return _state

@state_router.put("/{state_id}", response_model=StateResponseSchema)
async def update_state(state_id:UUID, update_data:UpdateStateSchema, session: AsyncSession = Depends(get_session)):
    _state = await service.update_state(state_id=state_id, update_data=update_data, session=session)
    if _state is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="State not found")
    return _state

@state_router.delete("/{state_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_state(state_id:UUID, session: AsyncSession = Depends(get_session)):
    message: Union[str, None] = await service.delete_state(zone_id=state_id, session=session)
    if message is not None:
        return message
    return None


