from controllers.controller_base import ControllerBase, ControllerUnauth
from classes.errors import ERROR
from flask import Response
from classes.camera import Camera


class GetVideo(ControllerUnauth):
    def get(self):
        return Response(self.generate_frame(Camera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    
    def generate_frame(self, camera):
        while True:
            frame = camera.get_frame()
            yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')