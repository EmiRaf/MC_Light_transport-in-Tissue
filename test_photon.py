import pytest
from Photon import Trayect


@pytest.mark.parametrize(
	"input_a, input_b, input_c, expected",
		[
			(3, 2, -2, (3, 2, -2)),
			(2, 3, -2.3, (2, 3, -2.3)),
			(0, 0.0, -0, (0, 0.0, -0)),
			(-0.0, -1000, -0.0001, (-0.0, -1000, -0.0001))
		]
	)
def test_Trayect(input_a, input_b, input_c, expected):
    photon = Trayect(input_a, input_b, input_c)
    x = photon.ux
    y = photon.uy
    z = photon.uz
    assert (x,y,z) == expected