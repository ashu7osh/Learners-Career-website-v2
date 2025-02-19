from sqlalchemy import create_engine, text
from config import DB_CONNECTION_STRING

db_connection_string = DB_CONNECTION_STRING
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ca": "/home/ashutosh/Desktop/ca.pem"
        }
    },
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = [row._asdict() for row in result]  # Convert Row to dictionary
    return jobs
