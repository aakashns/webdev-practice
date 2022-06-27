from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': '₹ 10,00,000 p.a.'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': '₹ 15,00,000 p.a.'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '₹ 12,00,000 p.a.'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  },
  {
    'id': 5,
    'title': 'Graphic Designer',
    'location': 'Delhi, India'
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS) 

@app.route("/api/jobs")
def jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='8080', debug=True)