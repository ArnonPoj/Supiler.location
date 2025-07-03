from flask import Flask, render_template
import folium
import os

app = Flask(__name__)

@app.route('/')
def index():
    location = [13.7563, 100.5018]
    m = folium.Map(location=location, zoom_start=12)
    folium.Marker(location, tooltip='กรุงเทพ').add_to(m)
    m.save('templates/map.html')
    return render_template('map.html')

@app.route('/click-map')
def click_map():
    return render_template('click_map.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # ✅ สำคัญ
    app.run(host='0.0.0.0', port=port)
