from sqlalchemy import SmallInteger, Integer, String, Column
from app_data.definitions import Base

class AquaState(Base):
    __tablename__ = 'state'
    id = Column(Integer, autoincrement=True,       # ID  устройства
            primary_key=True, nullable=False) 
    device_name = Column(String(30), nullable=False) # Имя устройства
    device_type = Column(String(30), nullable=False) # Тип устройства
    device_status = Column(SmallInteger)           # Статус устройства
    
    # Сериализатор
    @property
    def serizlize(self):
        return {
            'id': self.id,
            'name': self.device_name,
            'type': self.device_type,
            'status': self.device_status,
        }
    
    
    