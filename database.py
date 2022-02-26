class DevDatabase(object):
    username = 'root'
    password = 'root'
    host = 'localhost'
    port = 3306
    database = 'flask_restful_template'
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s:%s/%s" % (username, password, host, port, database)
    SQLALCHEMY_ECHO = True


class ProdDatabase(object):
    username = 'root'
    password = '123456'
    host = 'localhost'
    port = 3306
    database = 'flask_restful_template'
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s:%s/%s" % (username, password, host, port, database)
    SQLALCHEMY_ECHO = False
