from Etl                import Etl
from Extractor_csv      import Extractor_csv

def t_01():
    #file_path = '/home/art/data/nuevo_leon_cp_data_utf-8.csv'
    file_path = '/home/art/data/cp_data_header_utf-8.csv'

    extractor =  Extractor_csv( file_path )
    reader = extractor.get_reader()

def t_02():

    etl =  Etl( )
    etl.run()


if __name__ == '__main__':
    t_02()

    print( '\n end test.' )