from flask_restful import reqparse
from classes.errors import ERROR
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.State import AquaState
from controllers.controller_base import ControllerBase


class DeviceState(ControllerBase):
    def get(self):
        try:
            parser = DeviceState.parser.copy()
            parser.add_argument(
                'deviceId',
                type=int,
                location='args',
                required=False,
                )
            args = parser.parse_args()
            with Session(autoflush=False, bind=self._connection) as db:
                device = db.query(AquaState) \
                    .filter(
                        AquaState.id == args['deviceId']
                    ).first()
                if device != None:
                    return self.make_response_str(
                        ERROR.OK,
                        device.serizlize
                        ), 200
                return self.make_response_str(ERROR.UNKNOWN_DEVICE),200
        except (SQLAlchemyError, Exception) as e:
            response, code = self.handle_exception(e)
            return response, code
        

    
    def post(self):
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument(
                'deviceId',
                type=int,
                location='json',
                required=True,
                )
            parser.add_argument(
                'value',
                type=int,
                location='json',
                required=True,
                )        
            args = parser.parse_args()
            with Session(autoflush=False, bind=self._connection) as db:
                device = db.query(AquaState) \
                    .filter(
                        AquaState.id == args['deviceId']
                    ).first()
                if device == None:
                    return self.make_response_str(ERROR.UNKNOWN_DEVICE),200
                if device.device_type == 'sensor' :
                    return self.make_response_str(ERROR.UNABLE_CHANGE),200
                device.device_status = args['value']
                db.commit()
                return self.make_response_str(ERROR.OK, device.serizlize), 200
        except (SQLAlchemyError, Exception) as e:
            response, code = self.handle_exception(e)
            return response, code