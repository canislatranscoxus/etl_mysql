# CP zipcodes observations

Mty Metropolitan area has the next cities:

    Apodaca             
    Cadereyta Jiménez
    Escobedo
    García
    Guadalupe
    Juárez
    Monterrey
    Salinas Victoria
    San Nicolás de los Garza
    San Pedro Garza García
    Santa Catarina
    Santiago

Mr Envios coberage is
    apodaca
    escobedo
    garcia
    guadalupe
    juarez
    monterrey
    san nicolas de los garza
    san pedro garza garcia
    santa catarina

```
sql
SELECT min(d_codigo), max(d_codigo) , D_mnpio #, d_ciudad, d_asenta 
FROM   ship_cp
WHERE  D_mnpio in (
    'apodaca',
    #'cadereyta jimenez',
    'escobedo',
    'garcia',
    'guadalupe',
    'juarez',
    'monterrey',
    #'salinas victoria',
    'san nicolas de los garza',
    'san pedro garza garcia',
    'santa catarina'
    #'santiago'
)
group by D_mnpio 
order by 1
;

```
