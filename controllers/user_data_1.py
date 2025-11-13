from flask_restful import reqparse
from classes.errors import ERROR
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from flask import request
from models.User import User
from controllers.controller_base import ControllerBase
from hashlib import sha256
from classes.custom_error import CustomError

class UserData1(ControllerBase):
    def get(self):
        try:
            with Session(autoflush=False, bind=self._connection) as db:
                # Получаем токен обращающегося пользователя
                # TODO: вынести в родительский класс
                auth_header = request.headers.get('Authorization')
                parts = auth_header.split()
                token = sha256(parts[1].encode('utf-8')).hexdigest()
                # Ищем пользователя по этому токену
                current_user = db.query(User) \
                    .filter(
                        User.token_hash == token
                    ).first()
                # Возвращаем
                user_data = current_user.serialize
                user_data['role'] = user_data['role']['role_id']
                return self.make_response_str(
                    ERROR.OK,
                    user_data
                ), 200
        except (SQLAlchemyError, Exception) as e:
            response, code = self.handle_exception(e)
            return response, code
        
    def post(self):
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument('phone', type=str, required=False,
                                location='json')
            parser.add_argument('email', type=str, required=False,
                                location='json')
            parser.add_argument('password', type=str, required=False,
                                location='json')
            parser.add_argument('firstname', type=str, required=False,
                                location='json')
            parser.add_argument('surname', type=str, required=False,
                                location='json')
            parser.add_argument('middlename', type=str, required=False,
                                location='json')
            parser.add_argument('newPassword', type=str, required=False,
                               location='json')
            parser.add_argument('oldPassword', type=str, required=False,
                               location='json')
            args=parser.parse_args()
            
            with Session(autoflush=False, bind=self._connection) as db:
                # Получаем токен обращающегося пользователя
                # TODO: вынести в родительский класс
                auth_header = request.headers.get('Authorization')
                parts = auth_header.split()
                token = sha256(parts[1].encode('utf-8')).hexdigest()
                # Ищем пользователя по этому токену
                current_user = db.query(User) \
                    .filter(
                        User.token_hash == token
                    ).first()
                
                # Записываем новые данные
                if args['firstname'] != None:
                    current_user.firstname = args['firstname']
                if args['surname'] != None:
                    current_user.surname = args['surname']
                if args['middlename'] != None:
                    current_user.middlename = args['middlename']
                if args['email'] != None:
                    current_user.email = args['email']
                if args['phone'] != None:
                    current_user.phone = args['phone']
                if args['newPassword'] != None:
                    # Проверяем наличие старого пароля
                    if args['oldPassword'] == None:
                        # Если старый пароль отсутствует в запросе
                        raise CustomError("Требуется старый пароль")
                    # Сравниваем если есть
                    old_pass_hash = sha256(args['oldPassword'].encode('utf-8')).hexdigest()
                    if current_user.password != old_pass_hash:
                        # Если он не совпадает
                        raise CustomError("Старый пароль не совпадает")
                    # Если подходит записываем новый
                    current_user.password = sha256(args['newPassword'].encode('utf-8')).hexdigest()
                db.commit()
                # Возвращаем
                user_data = current_user.serialize
                user_data['role'] = user_data['role']['role_id']
                return self.make_response_str(
                    ERROR.OK,
                    user_data
                ), 200
        except (SQLAlchemyError, Exception) as e:
            response, code = self.handle_exception(e)
            return response, code