import os 
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(
        os.getenv('login_sql'), 
        os.getenv('senha_sql'), 
        os.getenv('host_sql'), 
        os.getenv('database_sql')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
