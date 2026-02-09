from time import time
from flask import current_app
import os

class Camera(object):
    def __init__(self) -> None:
        folder = current_app.config['APP_PATH']
        self.frames = [open(folder + os.sep +'images'+os.sep+f+'.jpg', 'rb').read() for f in ['1','2','3','4','5', '6', '7', '8', '9', '10']]

    def get_frame(self):
        return self.frames[int(time()) % 5]