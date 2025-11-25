from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/scan-traffic")
def scan():
    # Dummy example, replace later with real OpenCV detection
    return jsonify({
        "lane1": 40.5,
        "lane2": 12.3
    })

app.run(host="0.0.0.0", port=5000)
