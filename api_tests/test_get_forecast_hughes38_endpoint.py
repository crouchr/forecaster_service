from webtest import TestApp
from forecaster_service import app
import pytest

import definitions


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

    browser = TestApp(app)
    response = browser.get(definitions.endpoint_base + '/get_forecast_hughes38', params=query)
    response_dict = response.json
    status_code = response.status_code

    assert status_code == 200
    assert response_dict['forecast_text'] == expected_text
