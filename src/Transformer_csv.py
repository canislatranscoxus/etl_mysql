import unidecode
from I_Transformer import I_Transformer

class Transformer_csv( I_Transformer ):

    def transform( self, row ):
        '''Convert list to tuple'''
        try:
            a = []
            for i in row:
                i = unidecode.unidecode( i.lower() )
                a.append( i )

            t = tuple( a )
            return t
        except Exception as e:
            print( 'Etl.run(), error: {}'.format( e ) )            


    def transform_batch( self, rows ):
        pass


    def __init__( self ):
        print( 'Transformer_csv.__init__()... end' )