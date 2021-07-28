from Etl                import Etl
from Extractor_csv      import Extractor_csv

def run():
    ''' Run etl process. 
    extract data from cvs file,
    transform, lowercase and remove accents,
    load to  lz_sepomex_cp table'''

    etl =  Etl( )
    etl.run()


if __name__ == '__main__':
    print( '\n Etl begin ....' )
    run()
    print( '\n end.' )