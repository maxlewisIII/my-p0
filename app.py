from flask import Flask

app = Flask(__name__)


users = {
    "Max": {
        "phone": "828-446-0001"
    }
}

@app.route('/users')
def get_all_users():
    return users




app.run(port=8080)