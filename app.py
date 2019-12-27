from flask import Flask, render_template, request, jsonify
from pusher import Pusher
import random 
import string 

# buat flask app
app = Flask(__name__)

# konfigurasi pusher object
pusher = Pusher(
  app_id='APP_ID',
  key='APP_KEY',
  secret='APP_SECRET',
  cluster='APP_CLUSTER',
  ssl=True
)

# buat id dengan generate huruf dan angka
def get_id():
  data = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
  return data

# menampilkan home
@app.route('/')
def index():
  return render_template('home.html')

# menampilkan semua post
@app.route('/posts')
def posts():
  return render_template('posts.html')

# membuat post
@app.route('/post', methods=['POST'])
def addPost():
  data = {
    'id': "{}".format(get_id()),
    'title': request.form.get('title'),
    'content': request.form.get('content'),
    'event_name': 'created'
  }
  pusher.trigger("blog", "post-added", data)
  return jsonify(data)



# run Flask dalam mode debug
app.run(debug=True)