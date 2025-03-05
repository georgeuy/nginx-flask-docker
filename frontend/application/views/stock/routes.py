import requests
from flask import request, render_template, redirect, url_for

from . import stock_bp

PREFIX_PATH = '/api/v1/stock'

@stock_bp.route(f'{PREFIX_PATH}/list')
def get_stock():
    data = []
    error = ''
    try:
        response = requests.get("http://micro-1:3000/")
        response_data = response.json()

        if response_data and response_data['success']:
            data = response_data['data']
        else:
            error = response_data['error']

    except requests.exceptions.RequestException as e:
        print('get_stock():', str(e))
        error = 'No se pudo conectar al micro-1'
    
    return render_template('stock/list.html', data=data, error=error)


@stock_bp.route(f'{PREFIX_PATH}/add', methods=['GET', 'POST'])
def post_stock():
    
    error = ''
    data = {}

    if request.method == 'POST':

        data['id'] = int(request.form.get('product_id', '0'))
        data['name'] = request.form.get('product_name', '')

        try:
            response = requests.post("http://micro-1:3000/", json=data)  # Agregamos json=data
            response_data = response.json()  # Obtenemos la respuesta en formato JSON

            if response_data and response_data['success']:
                return redirect(url_for('.get_stock'))
            else:
                error = response_data['error']

        except requests.exceptions.RequestException as e:
            print('post_stock():', str(e))
            error = 'No se pudo conectar al micro-1'

    return render_template('stock/add.html', error=error, data=data)