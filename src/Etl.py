
from Extractor_csv  import Extractor_csv
from Loader_txt     import Loader_txt
from Factory        import Factory

class Etl:

    extractor   = None
    transformer = None
    loader      = None


    def transform( self ):
        pass

    def load( self ):
        pass

    def run( self ):
        try:
            self.loader.connect()
            clean_data = []
            batch_size = 20
            i = 0
            for row in self.extractor.get_reader():
                print( row )

                r = self.transformer.transform( row )
                clean_data.append( r )

                print( r )

                i = i+1
                if i % batch_size == 0 :
                    #self.load_batch( clean_data )
                    clean_data.clear()

                if i > 5:
                    break

        except Exception as e:
            print( 'Etl.run(), error: {}'.format( e ) )            


    def __init__( self ):
        file_path = '/home/art/data/nuevo_leon_cp_data_utf-8.csv'
        #file_path = '/home/art/data/cp_data_header_utf-8.csv'

        factory = Factory()

        self.extractor   = factory.create_extractor  ( 'csv', file_path )
        self.transformer = factory.create_transformer( 'csv' )
        self.loader      = factory.create_loader     ( 'csv' )

        print( 'Etl.__init__() ... end' )
