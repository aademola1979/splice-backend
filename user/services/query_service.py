
from user.models.user_account_model import UserModel
from user.models.user_personal_info_model import UserPersonalInfoModel as PersonalInfo
from address.models.local_government_model import LGAModel
from address.models.state_model import StateModel
from address.models.zone_model import ZoneModel
from sqlmodel import select, desc, or_
from sqlmodel import text


all_users_query = select(UserModel).order_by(desc(UserModel.created_at))

def get_user_by_id_query(user_id: str):
    query = select(UserModel).where(UserModel.id == user_id)
    return query

def detailed_address(search_string:str)->str:
    query = select(
                (UserModel.id).label('id'),
                (UserModel.first_name).label('first_name'), 
                (UserModel.middle_name).label('middle_name'), 
                (UserModel.last_name).label('last_name'),
                (UserModel.email).label('email'),
                (PersonalInfo.street).label('street'), 
                (PersonalInfo.city).label('city'),
                (PersonalInfo.DOB).label('DOB'),
                (PersonalInfo.telephone).label('telephone'), 
                (LGAModel.name).label('lga_name'),
                (StateModel.name).label('state_name'),
                (ZoneModel.name).label('zone_name') 
                ).join_from(UserModel, PersonalInfo).join_from(PersonalInfo, LGAModel).join_from(LGAModel, StateModel).join_from(StateModel, ZoneModel).where(
                     or_(
                          text(f"user_account.first_name ILIKE '%{search_string}%'"),
                          text(f"user_account.last_name ILIKE '%{search_string}%'"),
                          text(f"user_account.middle_name ILIKE '%{search_string}%'")

                          )).order_by(UserModel.first_name)
    return query
    
all_detailed_address_query = select(
                (UserModel.id).label('id'),
                (UserModel.first_name).label('first_name'), 
                (UserModel.middle_name).label('middle_name'), 
                (UserModel.last_name).label('last_name'),
                (UserModel.email).label('email'),
                (PersonalInfo.DOB).label('DOB'),
                (PersonalInfo.telephone).label('telephone'),
                (PersonalInfo.street).label('street'), 
                (PersonalInfo.city).label('city'), 
                (LGAModel.name).label('lga_name'),
                (StateModel.name).label('state_name'),
                (ZoneModel.name).label('zone_name') 
                ).join_from(UserModel, PersonalInfo).join_from(PersonalInfo, LGAModel).join_from(LGAModel, StateModel).join_from(StateModel, ZoneModel).order_by(UserModel.first_name)


def get_user_by_id_query(user_id:str)->str:
    query = select(
            (UserModel.id).label('id'),
            (UserModel.first_name).label('first_name'), 
            (UserModel.middle_name).label('middle_name'), 
            (UserModel.last_name).label('last_name'),
            (UserModel.email).label('email'),
            (PersonalInfo.DOB).label('DOB'),
            (PersonalInfo.telephone).label('telephone'),
            (PersonalInfo.street).label('street'), 
            (PersonalInfo.city).label('city'), 
            (LGAModel.name).label('lga_name'),
            (StateModel.name).label('state_name'),
            (ZoneModel.name).label('zone_name') 
            ).join_from(UserModel, PersonalInfo).join_from(PersonalInfo, LGAModel).join_from(LGAModel, StateModel).join_from(StateModel, ZoneModel).where(UserModel.id == user_id)
    return query
