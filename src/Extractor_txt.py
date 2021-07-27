from I_Extractor import I_Extractor

class Extractor_txt( I_Extractor ):

    file_path = None

    def get_reader( self ):
        pass

    def get_next( self):
        pass

    def get_next_batch( self ):
        pass

    def get_all( self ):
        pass 

    def __init__( self, file_path ):
        
        self.file_path = file_path 