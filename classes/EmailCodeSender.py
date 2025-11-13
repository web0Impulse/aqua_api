from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from threading import Thread

class EmailCodeSender(object):
    def __init__(self, smtp_serv: str, 
                 source_email: str, port: int, password: str):
        self._port = port
        self._smtp_serv = smtp_serv
        self._source_email = source_email
        self._password = password
        
    def send(self, addr: str, subj: str, message: str, isHtml:bool = False) -> bool:
        try:
            self._smtp_obj = smtplib.SMTP_SSL(self._smtp_serv, self._port)
            self._smtp_obj.login(self._source_email, self._password)
            msg = MIMEMultipart()
            if isHtml:
                msg.attach(MIMEText(message, 'html'))
            else:
                msg.attach(MIMEText(message, 'plain'))
            msg['From'] = self._source_email
            msg['To'] = addr
            msg['Subject'] = subj
            errors = self._smtp_obj.send_message(msg)
            self._smtp_obj.quit()
            return True
        except Exception as e:
            self._smtp_obj.quit()
            return False
    
    def send_async(self, addr: str, subj: str, message: str) -> bool:
        Thread(target=self.send, args=(addr, subj, message)).start()
        return True