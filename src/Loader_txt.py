
from I_Loader import I_Loader

class Loader_txt( I_Loader ):

    def connect( self ):
        pass

    def load( self, row ):
        pass

    def load_batch( self, rows ):
        pass

    def __init__(self) -> None:
        self.conn = None