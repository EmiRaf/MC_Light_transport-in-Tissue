class Position:
    """Position gives x,y,z position
    
    >>>photon = Position(1,2,2)
    >>>x = photon.x
    >>>y = photon.y
    >>>z = photon.z
    >>>(x,y,z)==(1,2,2)
    True
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
       
class Trayect:
    """Gives you direction to where it moves"""
    
    def __init__(self, ux, uy, uz):
        self.ux = ux
        self.uy = uy
        self.uz = uz
        
class Spin:
    """
    Gives you direction to where it moves
    temporary values used during SPIN for new trajectory
    """
    
    def __init__(self, uxx, uyy, uzz):
        self.uxx = uxx
        self.uyy = uyy
        self.uzz = uzz
        
class Move:
    """Properties to step size and direction"""
    
    def __init__(self, s, cost, sint, cosp, sinp, p)
        self.s = s
        self.cost = cost
        self.sint = sint
        self.cosp = cosp
        self.sinp = sinp
        self.p = p

class weight:
    """ Photon Status """
    
    def __init__(self, weight, absorb, photon_status):
    self.weight = weight
    self.absorb = absorb
    self.photon_status = photon_status

