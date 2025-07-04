from flask import Flask, render_template
import os  # << ใส่ import os ด้วย

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('map_clickable.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # รับ port จากระบบของ Render
    app.run(host='0.0.0.0', port=port)        # เปิดให้ Render เข้าถึงได้
