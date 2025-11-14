from flask_restful import reqparse
from classes.errors import ERROR
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from flask import request
from models.User import User
from controllers.controller_base import ControllerBase
from hashlib import sha256

class UserData(ControllerBase):
    def get(self, user_id):
        try:
            with Session(autoflush=False, bind=self._connection) as db:
                # Получаем токен обращающегося пользователя
                # TODO: вынести в родительский класс
                
                # auth_header = request.headers.get('Authorization')
                # parts = auth_header.split()
                # token = sha256(parts[1].encode('utf-8')).hexdigest()
                # # Ищем пользователя по этому токену
                # current_user = db.query(User) \
                #     .filter(
                #         User.token_hash == token
                #     ).first()
                # auth_header = request.headers.get('Authorization')
                # parts = auth_header.split()
                # token = sha256(parts[1].encode('utf-8')).hexdigest()
                # Ищем пользователя по этому токену
                current_user = db.query(User) \
                    .filter(
                        User.id == self._user_id
                    ).first()
                # Проверка на то является ли пользователь администратором
                if current_user.role.role_id == 1:
                #if current_user.serialize['role']['role_id'] == 1:
                    # Все ОК -> Ищем пользователя по переданному ИД
                    user = db.query(User) \
                        .filter(
                            User.id == user_id
                        ).first()
                    # Возвращаем найденного пользователя
                    if user != None:
                        user_data = user.serialize
                        user_data['role'] = user_data['role']['role_id']
                        return self.make_response_str(
                            ERROR.OK,
                            user_data
                            ), 200
                    # Если такого ИД не существует возвращаем 404
                    return self.make_response_str(
                        ERROR.OBJ_NOT_FOUND
                    ), 404
                # Если пользователь не администратор отказываем в доступе
                return self.make_response_str(
                    ERROR.FORBIDDEN                
                ), 403
        except (SQLAlchemyError, Exception) as e:
            response, code = self.handle_exception(e)
            return response, code