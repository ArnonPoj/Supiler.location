from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    # ตำแหน่งหมุด
    location = [13.7563, 100.5018]  # กรุงเทพ
    m = folium.Map(location=location, zoom_start=12)
    folium.Marker(location, tooltip='กรุงเทพ').add_to(m)
    m.save('templates/map.html')

    return render_template('map.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
