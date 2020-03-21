import globals
from random import gauss


def get_bp():

    # sys reperesents the systolic blood pressure (numerator)
    # dia reperesents the diastolic blood pressure (denominator)
    sys = round(gauss(120,15))
    dia = round(gauss(70,15))


    # blood pressure starting at 130/80 is considered at risk of hypertension
    if sys >= 130 or dia >=80:
        globals.bp_flag = True
    else:
        globals.bp_flag = False

    globals.bp_value = (sys, dia)

    return str(sys)+"/"+str(dia)
