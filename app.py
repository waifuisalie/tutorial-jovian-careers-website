from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db


app = Flask(__name__)

@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=jobs,
                           )


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
    data_fetch = load_job_from_db(id)
    if not data_fetch:
        return "Job not Found", 404
    job = data_fetch[0]
    print(job['responsabilities'].split('\n'))
    return render_template('jobpage.html', 
                           job=job
                           )
    
if __name__ == '__main__':
    app.run(debug=True)     # so you can use in replit with browser in browser: app.run(host='0.0.0.0', deb)
