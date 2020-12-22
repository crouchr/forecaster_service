from webtest import TestApp
from forecaster_service import app

import definitions


def test_error():
    """
    Test /status
    :return:
    """
    browser = TestApp(app)
    response = browser.get(definitions.endpoint_base + '/nonexist')
    response_dict = response.json

    assert response.status_code == 404

