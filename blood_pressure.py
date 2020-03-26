import globals
from random import gauss


def get_bp_sys():

    # sys reperesents the systolic blood pressure (numerator)
    sys = round(gauss(120,15))

    # blood pressure starting at 130/80 is considered at risk of hypertension
    if sys >= 130:
        globals.bp_sys_flag = True
    else:
        globals.bp_sys_flag = False

    globals.bp_sys_value = sys

    return sys

def get_bp_dia():
    # dia reperesents the diastolic blood pressure (denominator)
    dia = round(gauss(70,15))

    # blood pressure starting at 130/80 is considered at risk of hypertension
    if dia >=80:
        globals.bp_dia_flag = True
    else:
        globals.bp_dia_flag = False

    globals.bp_dia_value = dia

    return dia
