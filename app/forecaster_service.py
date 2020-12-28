# microservice for various meteorological forecasting functions

from flask import Flask, jsonify, request

import zambretti_method
import hughes38_method

app = Flask(__name__)
version = '1.0.0'


# fixme : this does not give info about the actual exception
@app.errorhandler(500)
def error_handling(error):
    answer = {}
    answer['error'] = str(error)
    response = jsonify(answer, 500)
    return response


# an endpoint that can be polled with little overhead
@app.route('/status')
def status():
    answer = {}
    answer['status'] = 'OK'
    answer['version'] = version

    response = jsonify(answer)

    return response


@app.route('/get_forecast_zambretti')
def get_zambretti_forecast_api():
    try:
        answer = {}

        pressure = int(request.args.get('pressure', None))
        month_id = int(request.args.get('month_id', None))
        wind_deg = int(request.args.get('wind_deg', None))
        trend = int(request.args.get('trend', None))

        forecast_text = zambretti_method.get_forecast_text(pressure, month_id, wind_deg, trend)

        # Create response
        answer['forecast_text_english'] = forecast_text

        response = jsonify(answer)
        return response

    except Exception as e:
        answer['function'] = 'get_zambretti_forecast_api()'
        answer['error'] = str(e)
        response = jsonify(answer, 500)
        return response


@app.route('/get_forecast_hughes38')
def get_hughes38_forecast_api():
    try:
        answer = {}

        pressure = int(request.args.get('pressure', None))
        wind_deg = int(request.args.get('wind_deg', None))
        trend_str = int(request.args.get('trend_str', None))

        forecast_text = hughes38_method.get_forecast_text(pressure, wind_deg, trend_str)

        # Create response
        answer['forecast_text_english'] = forecast_text

        response = jsonify(answer)

        return response

    except Exception as e:
        answer['function'] = 'get_hughes38_forecast_api()'
        answer['error'] = str(e)
        response = jsonify(answer, 500)
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9501)
