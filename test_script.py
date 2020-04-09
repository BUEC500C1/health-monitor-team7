from blood_oxygen import read_blood_oxygen
from blood_pressure import get_bp_sys, get_bp_dia
from pulse import read_pulse


def test_blood_oxygen():
    oxy = read_blood_oxygen()
    assert isinstance(oxy, str)
    
    try:
        oxy_num = float(oxy)
        assert True
    except ValueError:
        assert False

    assert oxy_num < 1.00
    assert oxy_num > 0.90


def test_blood_pressure():
    get_bp_dia()
    get_bp_sys()
    assert 1 == 1


def test_pulse():
    read_pulse()
    assert 1 == 1
