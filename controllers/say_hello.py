from controllers.controller_unauth import ControllerUnauth
from classes.errors import ERROR

class SayHello(ControllerUnauth):
    def get(self):
        return self.make_response_str(
            ERROR.OK,
            {'answer' :'hello!'}
            ), 200
