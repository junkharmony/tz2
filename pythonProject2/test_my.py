import pytest
import main

@pytest.mark.parametrize("ar,e", [([7, 0, -6, -8, -17], 7), ([20553, 68847, 675, -8299], 68847), ([568, -345, -123456, 874], 874), ([5676, -780, 347, 35],  5676)])
def test_max(ar, e):
    assert main._max(ar) == e

@pytest.mark.parametrize("ar,e", [([7, 0, -6, -8, -17], -17), ([20553, 68847, 675, -8299], -8299), ([568, -345, -123456, 874], -123456), ([5676, -780, 347, 35],  -780)])
def test_min(ar, e):
    assert main._min(ar) == e

@pytest.mark.parametrize("ar,e", [([7, 0, -6, -8, -17], -24), ([20553, 68847, 675, -8299], 81776), ([568, -345, -123456, 874], -122359), ([5676, -780, 347, 35], 5278)])
def test_sum(ar, e):
    assert main._sum(ar) == e

@pytest.mark.parametrize("ar,e", [([7, 0, -6, -8, -17], 0), ([20553, 68847, 675, -8299], -7926651787213575), ([568, -345, -123456, 874], 21144190602240), ([5676, -780, 347, 35],  -53769315600)])
def test_mult(ar, e):
    assert main._mult(ar) == e

@pytest.mark.parametrize("ar", [([7, 0, -6, -8, -17]), ([20553, 68847, 675, -8299]), ([568, -345, -123456, 874]), ([5676, -780, 347, 35])])
def test_1bal(ar):
    assert main._min(ar) < main._max(ar)
