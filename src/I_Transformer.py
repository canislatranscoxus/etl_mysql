from abc import ABC


class I_Transformer( ABC ):

    def transform( self, row ):
        pass

    def transform_batch( self, rows ):
        pass


    def __init__( self ) -> None:
        pass