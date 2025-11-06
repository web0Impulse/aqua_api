from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from app_data.definitions import Base

class Role(Base):
    __tablename__ = "role"
    role_id = Column(Integer, autoincrement=True,       # ID  роли
                primary_key=True, nullable=False)       
    role_name = Column(String(20), nullable=False)      # Имя роли
    users = relationship('User', back_populates='role') # Навигационное свойство
    
    # Сериализатор
    @property
    def serialize(self):
        return {
            'role_id': self.role_id,
            'role_name': self.role_name,
        }