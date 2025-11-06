from enum import Enum

class ERROR(Enum):
    OK = 0
    UNAUTHORIZED = 1
    DATABASE_ERROR = 2
    BAD_REQUEST = 3
    INTERNAL_ERROR = 4
    OBJ_NOT_FOUND = 5
    UNKNOWN_DEVICE = 6
    UNABLE_CHANGE = 7
    FAIL_CHANGE = 8
    INVALID_USER = 9
    INTEGRITY_ERROR = 10
    PHONE_OR_EMAIL_IN_USE = 11
    CONFIRMATION_CODE_SEND_ERROR = 12
    INVALID_CONFIRMATION_CODE = 13
    FORBIDDEN = 14
    CONTENT_TOO_LARGE = 15
    UNSUPPORTED_FORMAT = 16
    
class APIError:
    errors = {
        0: 'Ok',
        1: 'Не авторизован',
        2: 'Ошибка базы данных',
        3: 'Неверный запрос',
        4: 'Внутренняя ошибка',
        5: 'Объект, указанный в запросе не найден',
        6: 'Неверный идентификатор устройства',
        7: 'Невозможно изменить состояние данного устройства',
        8: 'Не удалось изменить состояние устройства',
        9: 'Неверное имя пользователя или пароль',
        10: 'Ошибка целостности базы данных',
        11: 'Телефон или email уже используется',
        12: 'Ошибка отправки кода подтверждения',
        13: 'Неверный или устаревший код подтверждения',
        14: 'Доступ запрещен',
        15: 'Загружаемый контент очень большой',
        16: 'Неподдерживаемый формат',       
    }
    
    debug_error_list = []
    info_error_list = [0,5,6,13,14,15,]
    warn_error_list = [1,3,9,11,]
    error_error_list = [2,4,7,8,10,12,16,]
    
    def err(e: ERROR):
        return APIError.errors[e if type(e) == int else e.value]
    
    def err_type(e: ERROR):
        er = e if type(e) == int else e.value 
        if er in APIError.info_error_list: return 1
        if er in APIError.warn_error_list: return 2
        if er in APIError.error_error_list: return 3
        if er in APIError.debug_error_list: return 4        
        return 0