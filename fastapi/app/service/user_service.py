from app.dal.schema.user import UserSchema
from app.model.user import UserCreateModel, UserModel
from app.util.database_client import database_client


class UserService:
    async def get_user(self, user_id: int) -> UserModel:
        async with database_client.get_session() as session:
            user = await session.get(UserSchema, user_id)
            return UserModel.model_validate(user)

    async def create_user(self, user: UserCreateModel):
        async with database_client.get_session() as session:
            session.add(UserSchema(name=user.name, email=user.email))
            await session.commit()
