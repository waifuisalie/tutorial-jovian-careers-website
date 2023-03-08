from flask import Flask, render_template, jsonify
from database import load_jobs_from_db


app = Flask(__name__)

@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=jobs,
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)     # so you can use in replit with browser in browser: app.run(host='0.0.0.0', deb)
