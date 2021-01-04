import cx_Oracle
from configparser import ConfigParser

class DatabaseCon:
    
    connection = None
    username = None
    passwd = None
    url = None

    def __init__(self):
        #code for DB connection parameters
        
        if DatabaseCon.username is None or DatabaseCon.passwd is None or DatabaseCon.url is None:
            configur = ConfigParser()
            configur.read('dbconfig.ini')
            DatabaseCon.username = configur.get('database config','username')
            DatabaseCon.passwd = configur.get('database config','password')
            DatabaseCon.url = configur.get('database config','url')

    def getConnection(self):
        if DatabaseCon.connection is None:
            DatabaseCon.connection = cx_Oracle.connect(DatabaseCon.username,DatabaseCon.passwd,DatabaseCon.url,encoding="UTF-8")
        return DatabaseCon.connection
    
    def createExecuteBuyOrderExpJob(self,con,nid):
        SQLB = '''
        BEGIN
            DBMS_SCHEDULER.CREATE_JOB (
            job_name           =>  'jobnum''' + nid + '''',
            job_type           =>  'PLSQL_BLOCK',
            job_action => 'BEGIN update orders set status=''E'' where (status=''P'' or status=''A'') and order_id=''' + nid + '''; commit; END;',
            start_date => sysdate + 5/(24*60),
            repeat_interval => NULL,
        enabled => TRUE);
        END;
        '''
        cur = con.cursor()
        cur.execute(SQLB)
        con.commit()
        
    def createExecuteSellOrderExpJob(self,con,nid):
        SQLB = '''
        BEGIN
            DBMS_SCHEDULER.CREATE_JOB (
            job_name           =>  'jobnum''' + nid + '''',
            job_type           =>  'PLSQL_BLOCK',
            job_action => 'BEGIN update orders set status=''E'' where status=''P'' and order_id=''' + nid + '''; commit; END;',
            start_date => sysdate + 5/(24*60),
            repeat_interval => NULL,
        enabled => TRUE);
        END;
        '''
        cur = con.cursor()
        cur.execute(SQLB)
        con.commit()