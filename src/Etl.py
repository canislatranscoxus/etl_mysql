
from Extractor_csv  import Extractor_csv
from Loader_txt     import Loader_txt
from Factory        import Factory

class Etl:
    file_path   = None
    batch_size  = 50


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
            self.loader.delete_table()
            clean_data = []
            i = 0
            reader = self.extractor.get_reader()

            print( 'file_path : {}'.format( self.file_path ) )
            print( 'batch_size: {}'.format( self.batch_size ) )

            for row in reader:

                r = self.transformer.transform( row )
                clean_data.append( r )
                i = i+1
                
                
                #print( '{} - {}, {}'.format( i, r[ 0 ], r[ 1 ] ) )
                print( i )

                if i % self.batch_size == 0 :
                    self.loader.load_batch( clean_data )
                    clean_data.clear()

                #if i > 10:
                #    break

            # upload the last batch
            if len( clean_data ) > 0:
                self.loader.load_batch( clean_data )
                clean_data.clear()


        except Exception as e:
            print( 'Etl.run(), error: {}'.format( e ) )            


    def __init__( self ):
        self.file_path = '/home/art/data/nuevo_leon_cp_data_utf-8.csv'
        #self.file_path = '/home/art/data/nuevo_leon_cp_data_utf-8_small.csv'

        #self.file_path = '/home/art/data/cp_data_header_utf-8.csv'

        factory = Factory()

        self.extractor   = factory.create_extractor  ( 'csv', self.file_path )
        self.transformer = factory.create_transformer( 'csv' )
        self.loader      = factory.create_loader     ( 'csv' )

        print( 'Etl.__init__() ... end' )
