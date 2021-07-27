from abc import ABC

class I_Extractor( ABC):

    file_path   = ''
    current_row = None
    batch_size  = None
    reader      = None

    def get_reader( self ):
        pass

    def get_next( self ):
        pass

    def get_next_batch( self ):
        pass

    def get_all( self ):
        pass

    def __init__( self, file_path ):
        
        self.file_path = file_path 