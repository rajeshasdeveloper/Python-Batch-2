from app import app
from flask import jsonify, make_response, request

# importing controller functions
from controllers.auth.signup import register

@app.route('/')
def home_route():
    return make_response(jsonify({"message": "Welcome to Flask app"}), 200)


@app.route('/auth/signup', methods=["POST"])
def register_method():
    request_body = request.get_json()
    signup_status = register(request_body)
    response = signup_status
    status_code = 201
    if signup_status != True:
        response = signup_status
        status_code = 400
        if signup_status["error"] == "Unknown error":
            status_code = 500
    else:
        response = {
            "message": f'Registered successfully the user {request_body["username"]}'
        }
    return make_response(jsonify(response), status_code)