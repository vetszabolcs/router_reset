from flask import Flask, render_template
from reset_router import reset_router

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reset')
def reset():
    reset_router()
    return render_template('index.html')


# if __name__ == "__main__":
#     app.run(debug=True, host="192.168.1.100:8080")

