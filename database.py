from sqlalchemy import create_engine, text
import os 

db_connection_string = os.getenv("DB_CONNECTION_STRING")
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/home/ashutosh/Desktop/Learners-Career-website-v2/Learners-Career-website-v2/ca.pem"
        }
    },
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = [row._asdict() for row in result]  # Convert Row to dictionary
    return jobs
