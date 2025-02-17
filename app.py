from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {'id':1,
   'title':'Data Analyst',
   'location': 'Bangluru, India',
   'salary': 'Rs 12,00,000'
  },
  {'id':2,
   'title':'Data Scientist',
   'location': 'Chennai, India',
   'salary': 'Rs 15,00,000'
  },
  {'id':3,
   'title':'Front-End',
   'location': 'Delhi, India',
   'salary': 'Rs 10,00,000'
  },
  {'id':4,
   'title':'Back-End',
   'location': 'Remote',
   'salary': 'Rs 15,00,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,static_folder='static', company_name='Learners')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)