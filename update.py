import Initglobal

def update_value(value):
    Initglobal.previous_time = value

def get_value():
    return Initglobal.previous_time
