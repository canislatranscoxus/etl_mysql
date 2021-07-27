
from I_Loader import I_Loader

class Loader_csv( I_Loader ):

    def load( self, row ):
        pass

    def load_batch( self, rows ):
        pass

    def __init__(self) -> None:
        self.conn = None