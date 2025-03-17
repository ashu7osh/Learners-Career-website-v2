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

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            {"val": id}  # Pass parameters as a dictionary
        )
        rows = result.all()
        if len(rows ) == 0:
            return None 
        else:
            return rows[0]._asdict()  # Convert Row object to dictionary
        
def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("""
    INSERT INTO applications (job_id, name, email, linkedin, education, experience, resume) 
    VALUES (:job_id, :name, :email, :linkedin, :education, :experience, :resume)
""")

    conn.execute(
        query,
        job_id=job_id,
        name=data['full_name'],
        email=data['email'],
        education=data['education'],
        experience=data['experience'],
        resume=data['resume']
    )
