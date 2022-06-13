from flask import Flask, request, jsonify
from model import get_sentiment 


app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def main():
    try:
        song_title = request.form.get('song_title')
        artist_name = request.form.get('artist_name')
    except Exception as e:
        return jsonify({'message': f'Invalid request, {e}'}), 500
    prediction = get_sentiment(song_title, artist_name)
    return jsonify({"output": prediction})


    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)