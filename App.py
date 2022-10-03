from asyncio import tasks
from email import message
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {'id': 1, 'title': 'Play Game', 'description': 'Play some games', 'done': False},
    {'id': 2, 'title': 'Learn Python', 'description': 'Need to find a good tutorial', 'done': False}
]


@app.route('/add-task', methods=['POST'])
def addTask():
    if not request.json:
        return jsonify({
            'status': 'Error',
            'message': 'Please provide the data'
        }, 400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description'),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        'status': 'success',
        'message': 'Task added successfully'
    })


@app.route('/get-data')
def get_task():
    return jsonify({
        'data': tasks
    })


if (__name__ == '__main__'):
    app.run(debug=True)
