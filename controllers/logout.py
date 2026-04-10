from classes.errors import ERROR
from controllers.controller_unauth import ControllerUnauth
from flask import session

class LogOut(ControllerUnauth):

    def post(self):
        try:
            session.clear()
            return self.make_response_str(ERROR.OK, {}), 200
        except (Exception) as e:
            response, code  = self.handle_exception(e)
            return response, code