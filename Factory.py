from Extractor_pandas   import Extractor_pandas
from Extractor_csv      import Extractor_csv
from Extractor_txt      import Extractor_txt

from Transformer_pandas import Transformer_pandas
from Transformer_csv    import Transformer_csv
from Transformer_txt    import Transformer_txt

from Loader_pandas      import Loader_pandas
from Loader_txt         import Loader_txt


class Factory:

    def create_extractor( self, type, file_path ):
        try:
            extractor = None

            if type == 'pandas':
                extractor = Extractor_pandas( file_path )
            elif type == 'csv':
                extractor = Extractor_csv( file_path )
            else:
                extractor = Extractor_txt( file_path )

            return extractor
        except Exception as e:
            print( 'Factory.create_extractor(), error: {}'.format( e ) )            

    def create_transformer( self, type ):
        try:

            transformer = None
            if type == 'pandas':
                transformer = Transformer_pandas()
            elif type == 'csv':
                transformer = Transformer_csv()
            else:
                transformer = Transformer_txt()

            return transformer

        except Exception as e:
            print( 'Factory.create_transformer(), error: {}'.format( e ) )            


    def create_loader( self, type ):
        try:

            loader = None
            if type == 'pandas':
                loader = Loader_pandas()
            else:
                loader = Loader_txt()

            return loader

        except Exception as e:
            print( 'Factory.create_extractor(), error: {}'.format( e ) )            
