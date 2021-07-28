import unidecode
from Timer import  Timer


def ut_1():
    ''' clean_data '''

    a = [
        'Apodaca', 
        'Cadereyta Jiménez', 
        'Escobedo', 
        'García', 
        'Guadalupe', 
        'Juárez', 
        'Monterrey', 
        'Salinas Victoria', 
        'San Nicolás de los Garza', 
        'San Pedro Garza García', 
        'Santa Catarina', 
        'Santiago', 
    ] 
    for i in a:
        i = unidecode.unidecode( i.lower() )
        print( i )

def ut_2():
    ''' Timer '''
    timer = Timer()
    timer.start()

    for i in range( 0, 1000 ):
        x = i * i * i
        print( 'This is number : {}, cube: {}'.format( i, x )  )

    timer.stop()


if __name__ == '__main__':
    print( '\n ... test begin' )    
    ut_2()
    print( '\n ... test end' )    
