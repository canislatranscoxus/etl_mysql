import unidecode

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