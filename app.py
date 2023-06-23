from flask import Flask, request, make_response, render_template, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

SWAGGER_BLUPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "to do list API",
    }
)
app.register_blueprint(SWAGGER_BLUPRINT, url_prefix = SWAGGER_URL)

from controller import *

@app.route('/')
def welcome():
    return render_template("Basic.html")

if __name__ == '__main__':
    app.run(debug=True)