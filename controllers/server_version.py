from controllers.controller_unauth import ControllerUnauth
from classes.errors import ERROR

class ServerVersion(ControllerUnauth):
    def get(self):
        return self.make_response_str(
            ERROR.OK,
            {'version' : '1.0.1'}
            ), 200
