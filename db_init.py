from models.User import User
from models.Role import Role
from models.State import AquaState
from models.Candidate import Candidate
from app_data.definitions import mysql_connection, Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=mysql_connection)

with Session(autoflush=False, bind=mysql_connection) as db:
    # Создаем новую роль
    role1 = Role(
        role_name = 'admin'
    )
    db.add(role1)
    role2 = Role(
        role_name = 'user'
    )
    db.add(role2)
    # Создаем нового пользователя (админ)
    user = User(
        surname = 'Иванов',
        firstname = 'Иван',
        middlename = 'Иванович',
        phone = '+79121234567',
        email = 'ivanov@mail.ru',
        password = '12345678',
    )
    user.role = role1
    db.add(user)
    
    s1 = AquaState(
        device_name = 'Air pump',
        device_type = 'switch',
        device_status = 0,
    )
    
    s2 = AquaState(
        device_name = 'Light',
        device_type = 'switch',
        device_status = 0,
    )
    
    s3 = AquaState(
        device_name = 'Temperature sensor',
        device_type = 'sensor',
        device_status = 0,
    )    
    db.add_all([s1, s2, s3])
    db.commit()
    print(f'user={user.id},d1={s1.id},d2={s2.id},d3={s3.id},role1={role1.role_id},role2={role2.role_id}')