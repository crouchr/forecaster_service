#!/usr/bin/python3
# Implement the local forecast algorithm as per hughes38.com
# FIXME : add the no wind variation
# FIXME : move some of these functions to metfuncs

forecast = []
forecast.append('Error')
# NW Quadrant
forecast.append('Continued fair for 24 hours, lower temperatures')
forecast.append('Continued fair for 48 hours, same temperature')
forecast.append('Continued fair for 24 hours, slowly rising temperatures')
forecast.append('Fair for 48 hours, lower temperatures')
forecast.append('Continued fair weather')
forecast.append('Fair for 12 to 24 hours, temperature stable')
forecast.append('Clearing within a few hours, lower temperatures')
forecast.append('Continued threatening weather, lower temperatures')
forecast.append('Changing weather')
# SW Quadrant
forecast.append('Continued fair for 12 hours')
forecast.append('Continued fair for 12 hours, same temperature')
forecast.append('Fair for 6 to 12 hours, rising temperatures')
forecast.append('Fair for 48 hours, lower temperatures')
forecast.append('Fair for 12 hours, same temperature')
forecast.append('Rain imminent')
forecast.append('Clearing within 6 hours')
forecast.append('Continued stormy weather')
forecast.append('Increasing rain, clearing within 12 hours')
# SE Quadrant
forecast.append('Fair weather')
forecast.append('Rain within 24 to 48 hours')
forecast.append('Rain within 12 hours, stronger wind, rising temperatures')
forecast.append('Fair')
forecast.append('Rain within 12 to 24 hours')
forecast.append('Rain within 6 to 12 hours, stronger wind, rising temperatures')
forecast.append('Clearing weather')
forecast.append('Continued rain or no change')
forecast.append('Severe storm imminent, clearing within 24 hours')
# NE Quadrant
forecast.append('Clear and cool')
forecast.append('Continued fair, lower temperatures')
forecast.append('Rain within 24 to 48 hours')
forecast.append('Clear with colder weather')
forecast.append('No change')
forecast.append('Rain within 12 hours')
forecast.append('Clearer and cooling')
forecast.append('Rainy weather, clearing in 12 to 24 hours')
forecast.append('Heavy rain, severe NE gale, colder temperatures')


def map_pressure_to_coeff(pressure_str):
    """

    :param str pressure:
    :return:

    """
    pressure = int(pressure_str)
    if pressure <= 1008:
        pressure_coeff = 3
    elif pressure >= 1023:
        pressure_coeff = 1
    else:
        pressure_coeff = 2

    return pressure_coeff


def map_ptrend_to_coeff(ptrend_str):
    """
    Map 'Rising', ' Falling', 'Steady' to an integer
    :param str ptrend_str:
    :return:

    """
    ptrend_map = {
        'R': 1,
        'S': 2,
        'F': 3
    }
    ptrend = ptrend_str[0].upper()
    ptrend_coeff = ptrend_map[ptrend]

    return ptrend_coeff


def map_wind_dir_to_coeff(wind_dir_str):
    """

    :param wind_dir_str:
    :return:
    """

    wind_dir_map = {
        'N'   : 1,
        'NNE' : 4,
        'NE'  : 4,
        'ENE' : 4,
        'E'   : 4,
        'ESE' : 3,
        'SE'  : 3,
        'SSE' : 3,
        'S'   : 2,
        'SSW' : 2,
        'SW'  : 2,
        'WSW' : 2,
        'W'   : 1,
        'WNW' : 1,
        'NW'  : 1,
        'NNW' : 1
    }

    wind_dir = wind_dir_str.upper()
    wind_dir_coeff = wind_dir_map[wind_dir]

    return wind_dir_coeff


def get_forecaster_index(pressure_coeff, trend_coeff, wind_dir_coeff):
    """
    Forecast next n hours based on pressure, trend and wind quadrant
    :param int pressure_coeff:
    :param int trend_coeff:
    :param int wind_dir_coeff:
    :return: str Forecast ID on my Powerpoint
    """

    forecast_index = ((pressure_coeff - 1) * 3) + trend_coeff + ((wind_dir_coeff -1) * 9)

    return forecast_index


# This is the function used within applications
def get_forecast_text(pressure, trend_str, wind_deg):
    """
    Return forecast based on Pressure, pressure trend and wind direction
    :param pressure: pressure in mBar
    :param trend_str: pressure trend ['Rising', 'Falling', 'Steady']
    :param wind_deg: e.g. 'NNE'
    :return:
    """
    try:
        wind_quadrant = wind_deg_to_wind_quadrant(wind_deg)     # e.g. SSW

        pressure_coeff = map_pressure_to_coeff(pressure)
        trend_coeff = map_ptrend_to_coeff(trend_str)
        wind_dir_coeff = map_wind_dir_to_coeff(wind_quadrant)

        forecaster_id = get_forecaster_index(pressure_coeff, trend_coeff, wind_dir_coeff)
        forecaster_text = forecast[forecaster_id]

    except Exception as e:
        print(e)

    return forecaster_text, forecaster_id


# FIXME : move this to metfuncs.windrose
def wind_deg_to_wind_quadrant(wind_deg):
    """
    Convert wind degree to windrose
    :param wind_deg:
    :return:
    """
    if wind_deg >= 0 and wind_deg <= 90:
        quadrant = "NE"
    elif wind_deg > 90 and wind_deg <= 180:
        quadrant = "SE"
    elif wind_deg > 180 and wind_deg <= 270:
        quadrant = "SW"
    else:
        quadrant = "NW"

    return quadrant
