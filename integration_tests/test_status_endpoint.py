
import definitions
import call_rest_api


def test_status():
    """
    Test /status
    :return:
    """
    status_code, response_dict = call_rest_api.call_rest_api(definitions.endpoint_base + '/status', None)

    if response_dict is None:
        return None

    assert status_code == 200
    assert response_dict['status'] == 'OK'
    assert 'version' in response_dict
