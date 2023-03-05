from flask import Flask, render_template, jsonify

app = Flask(__name__)

#simulating a database
JOBS = [
    {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs 1,00,000',
    },
    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs 15,00,000',
    },
    {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    },
    {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': 'R$ 120,000',
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)     # so you can use in replit with browser in browser: app.run(host='0.0.0.0', deb)
