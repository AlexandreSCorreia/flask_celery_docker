from flask import Flask, jsonify
from tasks import ola_mundo

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    task = ola_mundo.delay()
    return jsonify({"task_id": task.id}), 202

@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    task = ola_mundo.AsyncResult(task_id)
    if task.state == 'SUCCESS':
        response = {
            "state": task.state,
            "result": task.result
        }
    else:
        response = {
            "state": task.state,
            "result": None
        }
    return jsonify(response), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
