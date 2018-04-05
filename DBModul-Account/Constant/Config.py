class config_local:
    DATABASE_HOST           = 'localhost'
    DATABASE_USER           = 'root'
    DATABASE_PASSWORD       = 'tikitaka'
    DATABASE_NAME           = 'kontraktor_online'
    DATABASE_PORT           = 3306


class config_prod:
    DATABASE_HOST = 'kontraktor-online.cvjxqk7avvra.ap-southeast-1.rds.amazonaws.com'
    DATABASE_USER = 'kontraktor'
    DATABASE_PASSWORD = 'k0ntrakt0r'
    DATABASE_NAME = 'kontraktor_online'
    DATABASE_PORT = 3306