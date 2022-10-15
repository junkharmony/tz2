import random
import pytest
import main
import time


@pytest.mark.parametrize("ar,exp", [([0, 3, -4, -5, -6], -12),
                                            ([100023, 36247, 5555, -3249], 138576),
                                            ([12346, 695, -123, 38743], 51661),
                                            ([85123, -543680, 272, 12],  -458273)])
def test_sum(ar, exp):
    assert main._sum(ar) == exp

@pytest.mark.parametrize("ar,exp", [([0, 3, -4, -5, -6], 0),
                                            ([100023, 36247, 5555, -3249], -65434338853755795),
                                            ([12346, 695, -123, -38743], 40889277352830),
                                            ([85123, -543680, 272, 12],  -151056851496960)])
def test_mult(ar, exp):
    assert main._mult(ar) == exp

@pytest.mark.parametrize("ar,exp", [([0, 3, -4, -5, -6, -6, 3], 3),
                                            ([100023, 36247, 5555, -3249], 100023),
                                            ([12346, 695, -123, -38743], 12346),
                                            ([85123, -543680, 272, 12],  85123)])
def test_max(ar, exp):
    assert main._max(ar) == exp

@pytest.mark.parametrize("ar,exp", [([0, 3, -4, -5, -6, -6], -6),
                                            ([100023, 36247, 5555, -3249], -3249),
                                            ([12346, 695, -123, -38743], -38743),
                                            ([85123, -543680, 272, 12],  -543680)])
def test_min(ar, exp):
    assert main._min(ar) == exp


