import pytest
import mainf

@pytest.mark.parametrize("ar", [([7, 0, -6, -8, -17]), ([20553, 68847, 675, -8299]), ([568, -345, -123456, 874]), ([5676, -780, 347, 35])])
def test_max(ar):
    assert mainf._max(ar) == max(ar)

@pytest.mark.parametrize("ar", [([7, 0, -6, -8, -17]), ([20553, 68847, 675, -8299]), ([568, -345, -123456, 874]), ([5676, -780, 347, 35])])
def test_min(ar):
    assert mainf._min(ar) == min(ar)

@pytest.mark.parametrize("ar", [([7, 0, -6, -8, -17]), ([20553, 68847, 675, -8299]), ([568, -345, -123456, 874]), ([5676, -780, 347, 35])])
def test_sum(ar):
    assert mainf._sum(ar) == sum(ar)

@pytest.mark.parametrize("ar,e", [([7, 0, -6, -8, -17], 0), ([20553, 68847, 675, -8299], -7926651787213575), ([568, -345, -123456, 874], 21144190602240), ([5676, -780, 347, 35],  -53769315600)])
def test_mult(ar, e):
    assert mainf._mult(ar) == e

@pytest.mark.parametrize("ar", [([7, 0, -6, -8, -17]), ([20553, 68847, 675, -8299]), ([568, -345, -123456, 874]), ([5676, -780, 347, 35])])
def test_1bal(ar):
    assert mainf._min(ar) < mainf._max(ar)
