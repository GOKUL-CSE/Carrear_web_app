from re import DEBUG, template
from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOB = [{
    "role": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000"
}, {
    "role": "Data Scientist",
    "location": "Delhi, India",
}, {
    "role": "Frontend Developer",
    "location": "Remote",
    "salary": "Rs. 12,00,000"
}, {
    "role": "Backend Developer",
    "location": "San Francisco, USA",
    "salary": "Rs. 150,000"
}]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOB, company_name='Jovian')


@app.route('/jobs')
def list_jobs():
    return jsonify(JOB)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
