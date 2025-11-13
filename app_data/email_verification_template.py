VERIFICATION_EMAIL_HTML_TEMPLATE = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
    <html lang="ru">
    <head>
        <meta charset="UTF-8" />
    </head>
    <body style="
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 20px;
    ">
        <div style="
                max-width: 600px;
                margin: auto;
                background-color: #ffffff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
        ">
            <h2 style="color: #333333; margin-top: 0;">Подтверждение регистрации</h2>
            <p style="color:#555555">Здравствуйте!</p>
            <p style="color:#555555">Чтобы завершить регистрацию, введите следующий код подтверждения:</p>
            <div style="
                display: inline-block;
                font-size: 24px;
                font-weight: bold;
                padding: 10px 20px;
                margin: 20px 0;
                background-color: #efefef;
                border-radius: 4px;
                letter-spacing: 2px;
            ">
                {confirm_code}
            </div>
            <p style="color:#555555">Если вы не запрашивали регистрацию, проигнорируйте это письмо.</p>
        </div>
    </body>
    </html>'''