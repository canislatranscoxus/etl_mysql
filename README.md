# etl_mysql
etl using mysql

This project is a small example of how we can organize our Etl project.
We read a csv file, transform it to clean data, and load to mysql database.
The idea is to have all the data about zipcodes in the database and next
use only the necesary in a specific table, for example the zipcodes for
the Monterrey Metropolitan Area.
  

### Etl Process 1. Csv to Landing Zone

we downloaded the zipcode from sepomex as a csv file and saved to utf8 unicode.


Extract   --->    Transform             --->   Load

csv               clean data                    delete rows from lz_sepomex_cp
                  convert to lower case         load to DataBase
                  remove accents


### Etl Process 2. Landing Zone to Stage

Using only SQL script lz_2_stg.sql, we copy from landing to Stage table. 

lz_sepomex_cp   --->    stg_mty_metro_area


### Etl Process 3. Stage to Final

Using only SQL script stg_2_final.sql, we copy from Stage to final table. 

stg_mty_metro_area   --->    ship_mty_metro_area




### Virtual environment

create a virtual environment
```
sh
python3 -m pip install venv ~/git/env_mysql
```


load the vitual environment
```
sh
source ~/git/env_mysql/bin/activate
```


intall the libraries
```
sh
cd ~/git/etl_mysql/doc
python -m pip install -r requirements.txt
```


### links

* dowload sepomex zipcodes 
https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx

* importing bulk csv data

https://python.plainenglish.io/comparison-of-methods-for-importing-bulk-csv-data-into-mysql-using-python-5890dbf57419



https://stackoverflow.com/questions/3635166/how-do-i-import-csv-file-into-a-mysql-table


https://dev.mysql.com/doc/connector-net/en/connector-net-programming-bulk-loader.html


