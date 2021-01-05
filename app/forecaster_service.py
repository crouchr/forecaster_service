# microservice for various meteorological forecasting functions

from flask import Flask, jsonify, request

import zambretti_method
import hughes38_method
import forecaster_service_funcs

app = Flask(__name__)

# fixme : this does not give info about the actual exception
@app.errorhandler(500)
def error_handling(error):
    answer = {}
    answer['error'] = str(error)
    print('get_zambretti_forecast_api() : error : ' + error.__str__())
    response = jsonify(answer, 500)

    return response


# an endpoint that can be polled with little overhead
@app.route('/status')
def status():
    answer = {}
    answer['status'] = 'OK'
    answer['version'] = version
    print('status() : version=' + version)
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

        print('get_forecast_zambretti() : pressure=' + pressure.__str__() +
              ', month_id=' + month_id.__str__() +
              ', wind_deg=' + wind_deg.__str__() +
              ', trend=' + trend.__str__())

        forecast_text = zambretti_method.get_forecast_text(pressure, month_id, wind_deg, trend)
        print('get_forecast_zambretti() : forecast_text=' + forecast_text)

        # Create response
        answer['forecast_text_english'] = forecast_text

        response = jsonify(answer)

        return response

    except Exception as e:
        answer['function'] = 'get_zambretti_forecast_api()'
        answer['error'] = str(e)
        print('get_zambretti_forecast_api() : error : ' + e.__str__())
        response = jsonify(answer, 500)

        return response


@app.route('/get_forecast_hughes38')
def get_hughes38_forecast_api():
    try:
        answer = {}

        pressure = int(request.args.get('pressure', None))
        wind_deg = int(request.args.get('wind_deg', None))
        trend_str = request.args.get('trend_str', None)

        print('get_forecast_hughes38() : pressure=' + pressure.__str__() +
              ', wind_deg=' + wind_deg.__str__() +
              ', trend_str=' + trend_str.__str__())

        forecast_text = hughes38_method.get_forecast_text(pressure, trend_str, wind_deg)
        print('get_forecast_hughes38() : forecast_text=' + forecast_text)

        # Create response
        answer['forecast_text_english'] = forecast_text

        response = jsonify(answer)

        return response

    except Exception as e:
        answer['function'] = 'get_hughes38_forecast_api()'
        answer['error'] = str(e)
        print('get_hughes38_forecast_api() : error : ' + e.__str__())
        response = jsonify(answer, 500)

        return response


if __name__ == '__main__':
    version = forecaster_service_funcs.get_version()  # container version
    print('forecaster_service started, version=' + version)

    #app.run(host='0.0.0.0', port=9501)
    app.run(port=9501)