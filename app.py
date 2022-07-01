from flask import Flask
from controller.customer_controller import cc
from controller.accounts_controller import ac


if __name__ == '__main__':
    app = Flask(__name__)

    app.register_blueprint(cc)
    app.register_blueprint(ac)

    app.run(port=8082, debug=True)











