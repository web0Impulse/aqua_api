from sqlalchemy import DateTime, Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app_data.definitions import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True,        # ID  пользователя
                primary_key=True, nullable=False)
    surname = Column(String(30), nullable=True)     # Фамилия
    firstname = Column(String(30), nullable=False)  # Имя
    middlename = Column(String(30), nullable=True)  # Отчество
    phone = Column(String(12), nullable=False)      # Телефон
    email = Column(String(60), nullable=False)      # Email
    password = Column(String(128), nullable=False)  # хеш пароля
    token_hash = Column(String(128), nullable=True) # хеш токена
    token_created = Column(DateTime(), nullable=True) # дата/время создания токена
    user_role = Column(Integer, ForeignKey('role.role_id'), nullable=True)
    role = relationship('Role', back_populates='users') # Навигационное свойство
    
    # сериализатор
    @property
    def serialize(self):
        return {
            'id': self.id,
            'surname': self.surname,
            'firstname': self.firstname,
            'middlename': self.middlename,
            'phone': self.phone,
            'email': self.email,
            'role': self.role.serialize,
        }