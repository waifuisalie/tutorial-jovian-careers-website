from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
db_connection_string = os.getenv('DB_CONNECTION_STRING')

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem", 
        }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        result_all = result.all()
        jobs = [dict(zip(result.keys(), row)) for row in result_all]
        return jobs
    

def load_job_from_db(id):
    with engine.connect() as conn:
        query = text('SELECT * FROM jobs WHERE id = :id')
        result = conn.execute(query, 
                              {
                            'id':id
                              })
        rows = result.all()

        check_row = [dict(zip(result.keys(), row)) for row in rows]
        if len(check_row) == 0:
            return 0
        else:
            return check_row
    
def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url) ")
        
        conn.execute(query,
                    {
                    'job_id':job_id,
                    'full_name':data['full_name'],
                    'email':data['email'],
                    'linkedin_url':data['linkedin_url'],
                    'education':data['education'],
                    'work_experience':data['work_experience'],
                    'resume_url':data['resume_url']
                    })
                     