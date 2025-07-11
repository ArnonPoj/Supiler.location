from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def map_clickable():
    return render_template("map_clickable.html")

@app.route('/pluscode')
def map_pluscode():
    return render_template("map_pluscode.html")

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
