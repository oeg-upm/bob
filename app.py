from flask import Flask, render_template, jsonify, request, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



