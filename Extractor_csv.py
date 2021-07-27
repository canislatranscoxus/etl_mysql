import csv

from I_Extractor import I_Extractor



class Extractor_csv( I_Extractor ):

    file_path   = None
    file_reader = None
    encoding    = 'utf-8'
    #encoding    ='ISO-8859-1'  # Windows Latin

    def get_reader( self ):
        try:
            #reader = csv.reader( open('4956984.csv', 'rb') )
            reader = None
            self.file_reader = open( self.file_path, encoding = self.encoding ) 

            reader = csv.reader( self.file_reader, delimiter='|' )
            #reader = csv.DictReader( self.file_reader, delimiter='|' )

            '''
            # print 5 rows
            i = 0
            for row in reader:
                print( '{d_codigo}, {d_asenta}, {d_ciudad}, {d_estado}  '.format( **row )   )
                i = i + 1
                if i > 5:
                    break
            print( '\n\n rows: {}'.format( i ) )'''

            return reader

        except Exception as e:
            print( 'Extractor_csv.get_reader(), error: {}'.format( e ) )            


    def get_next( self):
        pass

    def get_next_batch( self ):
        pass

    def get_all( self ):
        pass 

    def __init__( self, file_path ):
        self.file_path = file_path 

    # Calling destructor
    def __del__(self):
        try:
            self.file_reader.close()

        except Exception as e:
            print( 'Extractor_csv.__del__(), error: {}'.format( e ) )            

        print("Extractor_csv.Destructor called ")        