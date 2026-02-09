from flask_restful import reqparse
from classes.errors import ERROR
from controllers.controller_unauth import ControllerUnauth
from sqlalchemy.orm import Session
from sqlalchemy.exc import MultipleResultsFound, NoResultFound, SQLAlchemyError
import secrets
from hashlib import sha256
from datetime import datetime
from models.User import User
from flask import session

class SignIn(ControllerUnauth):

    def post(self):
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument('phone', required=True, type=str,location='json') 
            parser.add_argument('password', required=True, type=str,location='json')
            args = parser.parse_args()

            with Session(autoflush=False, bind=self._connection) as db:
                #оздаем объект Person для добавления в бд
                user = db.query(User)\
                    .filter(
                        User.phone == args['phone']
                    ).one()

                if user.password != sha256(args['password'].encode('utf-8')).hexdigest():
                    return self.make_response_str(ERROR.INVALID_USER), 200
                token = secrets.token_hex(32)
                user.token_hash = sha256(token.encode('utf-8')).hexdigest()
                user.token_created = datetime.now()
                db.commit()
                data = {
                        'token': token,
                }
                session['user'] = user.id
                return self.make_response_str(ERROR.OK, data), 200                
        except NoResultFound as e:
            return self.make_response_str(ERROR.INVALID_USER), 200
        except MultipleResultsFound as e:
           return self.make_response_str(ERROR.INTEGRITY_ERROR), 500
        except (SQLAlchemyError, Exception) as e:
            response, code  = self.handle_exceptions(e)
            return response, code