import os
import pymysql


class Test_mysql( ):

    cur         = None


    def run( self ):
        try:
            MYSQL_NAME     = os.environ[ 'MYSQL_NAME'     ]
            MYSQL_USER     = os.environ[ 'MYSQL_USER'     ]
            MYSQL_PASSWORD = os.environ[ 'MYSQL_PASSWORD' ]
            MYSQL_HOST     = os.environ[ 'MYSQL_HOST'     ]


            print( '\nconnecting to mysql' )
            self.conn = pymysql.connect(
                host     = MYSQL_HOST,
                user     = MYSQL_USER, 
                password = MYSQL_PASSWORD,
                db       = MYSQL_NAME,
                )

            print( 'executing query' )      
            self.cur = self.conn.cursor()
            #self.cur.execute( "select @@version" )
            self.cur.execute( "select * from stg_mty_metro_area;" )

            print( 'displaying rows from table ... \n' )
            rows = self.cur.fetchall()
            for row in rows:
                print( row )

            print( '\n ... test end. \n' )

        except Exception as e:
            print( 'Loader_csv.connect(), error: {}'.format( e ) )
            raise


if __name__ == '__main__':
    t = Test_mysql()
    t.run()
