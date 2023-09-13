from flask import Blueprint, render_template, request, jsonify, url_for
import json
import math

api_calculator_bp = Blueprint('scientific_calculator', __name__)

@api_calculator_bp.route('/basic_calculator', methods=['GET','POST'])
def api_basic_calculator():
    if request.method == 'GET':
        return jsonify({'message':'GET method for basic calculator'})
    if request.method == 'POST':
        try:
            payload = json.loads(request.data)
            var_1 = float(payload['var_1'])
            var_2 = float(payload['var_2'])
            operation = payload['operation']

            if operation == 'Addition':
                result = var_1 + var_2
            elif operation == 'Subtraction':
                result = var_1 - var_2
            elif operation == 'Multiplication':
                result = var_1 * var_2
            elif operation == 'Division':
                if var_2 != 0:
                    result = var_1 / var_2
                else:
                    return jsonify({'error': 'Division by zero'}), 400

            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 400

@api_calculator_bp.route('/scientific_calculator', methods=['GET', 'POST'])
def api_scientific_calculator():
    if request.method == 'GET':
        return jsonify({'message': 'GET method for scientific calculator'})

    if request.method == 'POST':
        try:
            payload = json.loads(request.data)
            var_1 = float(payload['var_1'])
            operation = payload.get('operation', 'Log')

            if operation == 'SquareRoot':
                result = math.sqrt(var_1)
            elif operation == 'Square':
                result = var_1 ** 2
            elif operation == 'Cube':
                result = var_1 ** 3
            elif operation == 'Log':
                if var_1 > 0:
                    result = math.log(var_1)
                else:
                    return jsonify({'error': 'Invalid input for logarithm'}), 400
            elif operation == 'Sin':
                result = math.sin(var_1)
            elif operation == 'Cos':
                result = math.cos(var_1)
            elif operation == 'Tan':
                result = math.tan(var_1)
            else:
                return jsonify({'error': 'Operation not supported'}), 400

            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
