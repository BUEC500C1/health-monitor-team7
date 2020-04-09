from blood_oxygen import read_blood_oxygen
from blood_pressure import get_bp_sys, get_bp_dia
from pulse import read_pulse


def test_blood_oxygen():
    for i in range(10000):
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
    for i in range(10000):
        dia = get_bp_dia()
        sys = get_bp_sys()

        assert isinstance(dia, int)
        assert isinstance(sys, int)

        assert dia > 0
        assert sys > 0

        assert dia < 350
        assert sys < 200


def test_pulse():
    read_pulse()
    assert 1 == 1
