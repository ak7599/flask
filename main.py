from flask import Flask, render_template, url_for,jsonify
from blueprints.basic_calculator import basic_calculator_bp
from blueprints.api_calculator import api_calculator_bp

app = Flask(__name__)

app.register_blueprint(basic_calculator_bp)
app.register_blueprint(api_calculator_bp, url_prefix="/api")

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
