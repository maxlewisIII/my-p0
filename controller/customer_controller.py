from flask import Blueprint, request
from model.customer import Customer

cc = Blueprint('customer_controller', __name__)

@cc.route('/test')
def test():
    return "test"

