from sqlalchemy import DateTime, Integer, String, Column, ForeignKey
from app_data.definitions import Base

class Candidate(Base):
    __tablename__ = "candidates"
    id = Column(Integer, autoincrement=True,        # ID  пользователя
                primary_key=True, nullable=False)
    surname = Column(String(30), nullable=True)     # Фамилия
    firstname = Column(String(30), nullable=False)  # Имя
    middlename = Column(String(30), nullable=True)  # Отчество
    phone = Column(String(12), nullable=False)      # Телефон
    email = Column(String(60), nullable=False)      # Email
    password = Column(String(128), nullable=False)  # хеш пароля
    confirm_code_hash = Column(String(128), nullable=True) # хеш кода подтверждения
    confirm_code_expired = Column(DateTime(), nullable=True) # дата/время истечения срока годности кода
   