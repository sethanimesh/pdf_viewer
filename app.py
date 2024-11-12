from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

# SocketIO events
@socketio.on('connect')
def handle_connect():
    print('Client connected:', request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected:', request.sid)

@socketio.on('page-change')
def handle_page_change(data):
    # Broadcast the page change to all clients except the sender
    emit('page-update', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True)