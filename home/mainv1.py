from flask import Flask, render_template, jsonify
import os
import time
import papermill as pm


app = Flask(__name__)



@app.route('/')
def home():
    return 'ETL API'


@app.route('/run_job_lc')
def run_job():

    pm.execute_notebook(
           '/home/notebooks/job1.ipynb',
           '/home/logs/job1.ipynb')
    
    return jsonify({"status": 200})
   

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)




