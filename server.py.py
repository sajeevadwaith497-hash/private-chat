from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, send
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)

@socketio.on('message')
def handle_message(data):
    send(data['msg'], to=data['room'])

if __name__ == '__main__':
    # ഇന്റർനെറ്റിൽ ഓട്ടോമാറ്റിക് ആയി പോർട്ട് എടുക്കാൻ ഇത് സഹായിക്കും 
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host='0.0.0.0', port=port)