

from abc import ABC

class I_Loader( ABC):

    conn = None

    def load( self, rows ):
        pass

    def load_batch( self, rows ):
        pass


    def __init__(self) -> None:
        self.conn = None