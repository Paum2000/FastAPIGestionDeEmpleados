from sqlalchemy import URL
from sqlmodel import create_engine, Session
from app.core.config import config

# Verificamos si es SQLite para aplicar argumentos específicos
connect_args = {}
if config.db_type.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
    database_url = "sqlite:///./database.db"
else:
    database_url = URL.create(
        drivername=config.db_type,
        username=config.db_user,
        password=config.db_password,
        host=config.db_host,
        port=int(config.db_port),
        database=config.db_name,
    )

# Usamos settings.DATABASE_URL
engine = create_engine(
    database_url,
    echo=config.debug,
    connect_args=connect_args
)

def get_session():
    with Session(engine) as session:
        yield session