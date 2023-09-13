from flask import Blueprint, render_template, request, jsonify,url_for
import json
import math

basic_calculator_bp = Blueprint('basic_calculator', __name__,template_folder="templates")

@basic_calculator_bp.route('/basic_calculator', methods=['GET', 'POST'])
def basic_calculator():
    entry = ''

    if request.method == 'POST':
        var_1 = float(request.form['var_1'])
        var_2 = float(request.form['var_2'])
        operation = request.form['operation']

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
                result = 'math_error'

        entry = result

    return render_template('basic_calculator.html', entry=entry)

@basic_calculator_bp.route('/scientific_calculator', methods=['GET', 'POST'])
def scientific_calculator():
    entry = ''

    if request.method == 'POST':
        var_1 = float(request.form['var_1'])
        operation = request.form['operation']

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
                result = 'math_error'
        elif operation == 'Sin':
            result = math.sin(var_1)
        elif operation == 'Cos':
            result = math.cos(var_1)
        elif operation == 'Tan':
            result = math.tan(var_1)
        else:
            result = 'operation_not_supported'

        entry = result

    return render_template('scientific_calculator.html', entry=entry)


