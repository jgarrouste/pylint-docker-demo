"""Simple pylint Demo"""
from flask import Flask, jsonify
APP = Flask(__name__)

MESSAGES = [
    {
        'id': 1,
        'message': u'Paris',
    },
    {
        'id': 2,
        'message': u'Container Training',
    },
]

@APP.route('/', methods=['GET'])
def messages():
    """Return JSON object"""
    return jsonify({'messages': MESSAGES})

if __name__ == '__main__':
    APP.run(host='0.0.0.0')
