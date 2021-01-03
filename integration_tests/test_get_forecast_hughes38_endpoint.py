from webtest import TestApp
from forecaster_service import app
import pytest

import definitions
import call_rest_api


@pytest.mark.parametrize(
    "pressure, trend_str, wind_deg, expected_text",
    [
        (1000, 'Rising', 0, 'Clearer and cooling'),
        (1000, 'Steady', 45, 'Rainy weather, clearing in 12 to 24 hours'),
        (1000, 'Falling', 90, 'Heavy rain, severe NE gale, colder temperatures')
    ]
)
def test_get_forecast_hughes38(pressure, trend_str, wind_deg, expected_text):
    """
    Test /status
    :return:
    """
    query = {}

    query['pressure'] = pressure
    query['trend_str'] = trend_str
    query['wind_deg'] = wind_deg

    status_code, response_dict = call_rest_api.call_rest_api(definitions.endpoint_base + '/get_forecast_hughes38',
                                                             query)

    assert status_code == 200
    assert response_dict['forecast_text_english'] == expected_text
