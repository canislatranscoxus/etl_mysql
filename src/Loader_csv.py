import os
import pymysql

from I_Loader import I_Loader

class Loader_csv( I_Loader ):

    cur = None

    def connect( self ):
        try:
            MYSQL_NAME     = os.environ[ 'MYSQL_NAME'     ]
            MYSQL_USER     = os.environ[ 'MYSQL_USER'     ]
            MYSQL_PASSWORD = os.environ[ 'MYSQL_PASSWORD' ]
            MYSQL_HOST     = os.environ[ 'MYSQL_HOST'     ]

            self.conn = pymysql.connect(
                host     = MYSQL_HOST,
                user     = MYSQL_USER, 
                password = MYSQL_PASSWORD,
                db       = MYSQL_NAME,
                )
      
            self.cur = self.conn.cursor()

            '''self.cur.execute( "select @@version" )
            output = self.cur.fetchall()
            print(output)
            print( '\n ... debug' )'''

        except Exception as e:
            print( 'Loader_csv.connect(), error: {}'.format( e ) )

    def load( self, row ):
        pass

    def load_batch( self, rows ):
        try:
            sql = '''insert into ship_cp (
                d_codigo,d_asenta,d_tipo_asenta,D_mnpio,d_estado,
                d_ciudad,d_CP,c_estado,c_oficina,c_tipo_asenta,
                c_mnpio,id_asenta_cpcons,d_zona,c_cve_ciudad,c_CP 
                ) 
                values
                (
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s )                 
            '''

            self.cur.executemany( sql, rows )
            self.conn.commit()

        except Exception as e:
            print( 'Loader_csv.load_batch(), error: {}'.format( e ) )

    def __init__(self) -> None:
        self.conn = None

    def __del__( self ):
        try:
            self.cur = None
            self.conn.close()
        except Exception as e:
            print( 'Loader_csv.__del__(), error: {}'.format( e ) )
            
        print("Loader_csv.Destructor called ")        