# etl_mysql
etl using mysql

This project is a small example of how we can organize our Etl project.
We read a csv file, transform it to clean data, and load to mysql database.


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




* importing bulk csv data

https://python.plainenglish.io/comparison-of-methods-for-importing-bulk-csv-data-into-mysql-using-python-5890dbf57419



https://stackoverflow.com/questions/3635166/how-do-i-import-csv-file-into-a-mysql-table


https://dev.mysql.com/doc/connector-net/en/connector-net-programming-bulk-loader.html


