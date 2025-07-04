from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('map_clickable.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    address = request.form['address']
    latlng = request.form['latlng']
    contact_person = request.form['contact_person']
    phone = request.form['phone']

    # 🌟 ทำอะไรก็ได้กับข้อมูล เช่น save, print, log, หรือส่งกลับ
    print("Supplier info:", name, address, latlng, contact_person, phone)

    return f"""
    <h2>✅ บันทึกข้อมูลเรียบร้อยแล้ว</h2>
    <p><strong>ชื่อ:</strong> {name}</p>
    <p><strong>ที่อยู่:</strong> {address}</p>
    <p><strong>พิกัด:</strong> {latlng}</p>
    <p><strong>ผู้ติดต่อ:</strong> {contact_person}</p>
    <p><strong>เบอร์:</strong> {phone}</p>
    <p><a href="/">← กลับไปหน้าแผนที่</a></p>
    """

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
