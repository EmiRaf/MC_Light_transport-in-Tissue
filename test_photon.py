import pytest
from Photon import Spin


@pytest.mark.parametrize(
	"input_a, input_b, input_c, expected",
		[
			(3, 2, -2, (3, 2, -2)),
			(2, 3, -2.3, (2, 3, -2.3)),
			(0, 0.0, -0, (0, 0.0, -0)),
			(-0.0, -1000, -0.0001, (-0.0, -1000, -0.0001))
		]
	)
def test_Spin(input_a, input_b, input_c, expected):
    photon = Spin(input_a, input_b, input_c)
    x = photon.uxx
    y = photon.uyy
    z = photon.uzz
    assert (x,y,z) == expected