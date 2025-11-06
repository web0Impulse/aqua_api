from models.State import AquaState
from app_data.definitions import mysql_connection, Base
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound, MultipleResultsFound, SQLAlchemyError

with Session(autoflush=False, bind=mysql_connection) as db:
    devices = db.query(AquaState) \
        .all()
        
    for d in devices:
        print(f'id={d.id}, name={d.device_name}, status={d.device_status}')

    try:
        temp = db.query(AquaState) \
            .filter(AquaState.device_type == 'switch') \
            .all()
        for d in temp:
            print(f'id={d.id}, name={d.device_name}, status={d.device_status}')

        print(f'id={d.id}, name={d.device_name}, status={d.device_status}')
            
        #temp.device_status = 22
        #db.commit()
    except NoResultFound as e:
        print('Неверный номер устройства')
    except MultipleResultsFound as e:
        print('Найдено несколько записей, хотя требуется одна')
    