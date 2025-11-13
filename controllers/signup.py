from controllers.controller_unauth import ControllerUnauth
from hashlib import sha256
import secrets
from flask_restful import reqparse
from classes.errors import ERROR
from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timedelta
from random import randint
from threading import Thread
from models.Candidate import Candidate
from models.User import User
from classes.EmailCodeSender import EmailCodeSender
from app_data.definitions import smtp_serv, source_mail, smtp_port, smtp_serv_pass

class SignUp(ControllerUnauth):
    # подтверждение учетной записи
    def get(self):
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument('phone', type=str, required=True,
                                location='args')
            parser.add_argument('code', type=str, required=True,
                                location='args')
            args = parser.parse_args()
            with Session(autoflush=False, bind=self._connection) as db:
                # try:
                #     candidate = db.query(Candidate)\
                #         .filter(
                #             Candidate.confirm_code_expired < datetime.now()
                #         )
                #     candidate.delete(synchronize_session='fetch')
                #     db.commit()
                # except:
                #     pass 
                    candidate = db.query(Candidate)\
                        .filter(
                            Candidate.phone == args['phone'],
                            Candidate.confirm_code_hash ==
                                sha256(args['code'].encode('utf-8')).hexdigest()
                        ).first()
                    if candidate == None:
                        return self.make_response_str(
                            ERROR.INVALID_CONFIRMATION_CODE
                            ),200
                    token = secrets.token_hex(32)
                    user = User(
                        firstname = candidate.firstname,
                        surname = candidate.surname,
                        middlename = candidate.middlename,
                        phone = candidate.phone,
                        email = candidate.email,                        
                        password = candidate.password,
                        token_hash = sha256(token.encode('utf-8')).hexdigest(),
                        token_created = datetime.now(),
                        user_role = 2,
                    )
                    db.add(user)
                    db.delete(candidate)
                    db.commit()
                    data = {'token':token}
                    return self.make_response_str(ERROR.OK, data), 200
        except (SQLAlchemyError, Exception) as e:
            response, code = self.handle_exception(e)
            return response, code
    
    # регистрация пользователя
    def post(self):
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument('phone', type=str, required=True,
                                location='json')
            parser.add_argument('email', type=str, required=True,
                                location='json')
            parser.add_argument('password', type=str, required=True,
                                location='json')
            parser.add_argument('name', type=str, required=True,
                                location='json')
            parser.add_argument('surname', type=str, required=False,
                                location='json')
            parser.add_argument('middlename', type=str, required=False,
                                location='json')   
            args=parser.parse_args()
            
            with Session(autoflush=False, bind=self._connection) as db:
                user = db.query(User)\
                    .filter(
                        or_(
                            User.email == args['email'],
                            User.phone == args['phone'],
                        ),
                    ).first()
                if user != None:
                    return self.make_response_str(
                        ERROR.PHONE_OR_EMAIL_IN_USE
                        ),200
                confirm_code = '{:06}'.format(randint(0,999999))
                service = args['email']
                if not (self.send_confirm_code(service, confirm_code)):
                    return self.make_response_str(
                        ERROR.CONFIRMATION_CODE_SEND_ERROR
                        ),200
                candidate = Candidate(
                    firstname = args['name'],
                    surname = args['surname'],
                    middlename = args['middlename'],
                    phone = args['phone'],
                    email = args['email'],
                    password = sha256(args['password']
                                      .encode('utf-8')).hexdigest(),
                    confirm_code_hash = sha256(confirm_code
                                      .encode('utf-8')).hexdigest(),
                    confirm_code_expired = datetime.now() +
                            timedelta(days=0, hours=0, minutes=30),
                )
                db.add(candidate)
                db.commit()
            return self.make_response_str(ERROR.OK), 200
        except (SQLAlchemyError, Exception) as e:
            response, code = self.handle_exception(e)
            return response, code
        
        
    def send_confirm_code(self, service, confirm_code):
        sender = EmailCodeSender(
            smtp_serv,
            source_mail,
            smtp_port,
            smtp_serv_pass
        )
        res = sender.send(
            service,
            'Подтверждение регистрации на AquaService',
            f'Код подтверждения регистрации: {confirm_code}'
        )
        return res