from webtest import TestApp
from forecaster_service import app

import definitions


def test_status():
    """
    Test /status
    :return:
    """
    browser = TestApp(app)
    response = browser.get(definitions.endpoint_base + '/status')
    response_dict = response.json

    assert response.status_code == 200
    assert response_dict['status'] == 'OK'
    assert 'version' in response_dict
