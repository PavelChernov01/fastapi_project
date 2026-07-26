from sqlalchemy.orm import Session
from typing import List, Optional
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate, UserResponse

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
    
    def get_user(self, user_id: int) -> Optional[UserResponse]:
        user = self.repository.get_by_id(user_id)
        return UserResponse.model_validate(user) if user else None
    
    def get_users(self, skip: int = 0, limit: int = 100) -> List[UserResponse]:
        users = self.repository.get_all(skip, limit)
        return [UserResponse.model_validate(user) for user in users]
    
    def create_user(self, user_data: UserCreate) -> UserResponse:
        if self.repository.get_by_email(user_data.email):
            raise ValueError("Email already registered")
        if self.repository.get_by_username(user_data.username):
            raise ValueError("Username already taken")
        
        user = self.repository.create(user_data)
        return UserResponse.model_validate(user)
    
    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[UserResponse]:
        user = self.repository.update(user_id, user_data)
        return UserResponse.model_validate(user) if user else None
    
    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id)
