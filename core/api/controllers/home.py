


from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/api')
def api_index():
    return jsonify({
        "name": "Imad"
    })
