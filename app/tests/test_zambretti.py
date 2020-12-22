# author : R.Crouch
# Test zambretti functions

import pytest
import zambretti_method


# ----------
# @pytest.mark.parametrize(
#     "zambretti_letter, expected_zambretti_text",
#     [
#         ('A', 'Settled fine'),
#         ('J', 'Changeable, mending'),
#         ('Z', 'Stormy, much rain')
#     ]
# )
# def test_calc_zambretti_code(zambretti_letter, expected_zambretti_text):
#     zambretti_text = zambretti_method.get_forecast_text(zambretti_letter)
#
#     assert zambretti_text == expected_zambretti_text


# test against : http://www.beteljuice.co.uk/zambretti/forecast.html
@pytest.mark.parametrize(
    "pressure, month_id, wind_deg, trend, expected_text",
    [
        (1000, 12, 0, 0, 'Showery, bright intervals'),
        (1000, 12, 45, 2, 'Fairly fine, possible showers early'),
        (1000, 12, 90, 2, 'Showery early, improving'),
        (1000, 12, 135, 2, 'Showery early, improving'),
        (1006, 12, 190, -1, 'Rain at times, very unsettled'),
    ]
)
def test_get_forecast_text(pressure, month_id, wind_deg, trend, expected_text):
    """

    :param pressure: int mbar
    :param month_id: 12 = December
    :param wind_dir: degrees
    :param trend: mBar per hour
    :param expected_text:
    :return:
    """
    zambretti_text = zambretti_method.get_forecast_text(pressure, month_id, wind_deg, trend)

    assert zambretti_text == expected_text
