# Tutorial Pusher
Realtime aplikasi dengan menggunakan Pusher bisa dilihat pada:
[Idmore Blog]()
[Pusher Blog](https://blog.pusher.com/build-realtime-activity-feed-flask-pusher/).

Cara menjalankan di Local:
- Clone/Download repo - `git clone https://github.com/idmore/realtime_app_with_pusher.git`
- [Optional] Buat local virtual environment - `virtualenv .venv`
- [Optional] Aktifkan virtual environment - `source .venv/bin/activate`
- Install depedensi - `pip install -r requirements.txt`
- Buat akun Pusher dan dapatkan credentialnya pada websitenya, meliputi:
 `APP_ID`, `APP_KEY`, `APP_SECRET`, `APP_CLUSTER` 
 [Pusher dashboard](https://dashboard.pusher.com/).
- Run aplikasi - `python3 app.py` atau `python app.py`
- [localhost:5000](http://localhost:5000/)
