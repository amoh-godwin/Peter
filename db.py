import sqlite3

conn = sqlite3.connect('settings.db')
cursor = conn.cursor()

def create_table():
    sql = """CREATE TABLE general (parent_folder text)"""
    cursor.execute(sql)
    sql1 = """INSERT INTO general VALUES ('C:\\Deuteronomy Works\\Peter')"""
    cursor.execute(sql1)
    conn.commit()

def select():
    sql = """SELECT id FROM Servers"""
    cursor.execute(sql)
    al = cursor.fetchall()
    info = {}
    servers = []
    """for server in al:
        print(server)
        info['id'] = int(server[0])
        info['name'] = server[2]
        info['default_port'] = int(server[4])
        info['port'] = int(server[5])
        info['status'] = server[6]
        servers.append(info)

    print(info)
    print(servers)"""
    print(al)

def update():
    sql = """UPDATE Servers SET upath='C:/Deuteronomy Works/Peter/bin/Peterd'"""
    cursor.execute(sql)
    conn.commit()

conn.close()
