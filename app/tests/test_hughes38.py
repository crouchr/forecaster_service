import pytest
import hughes38_method


@pytest.mark.parametrize(
    "pressure_str, expected",
    [
        ("999",  3),
        ("1008", 3),
        ("1009", 2),
        ("1022", 2),
        ("1023", 1),
        ("1024", 1),
    ]
)
def test_map_pressure_to_coeff(pressure_str, expected):
    coeff = hughes38_method.map_pressure_to_coeff(pressure_str)
    assert coeff == expected


@pytest.mark.parametrize(
    "ptrend_str, expected",
    [
        ("Rising",  1),
        ("Steady",  2),
        ("Falling", 3),
        ("rising",  1),
        ("steady",  2),
        ("falling", 3),
    ]
)
def test_map_ptrend_to_coeff(ptrend_str, expected):
    coeff = hughes38_method.map_ptrend_to_coeff(ptrend_str)
    assert coeff == expected


@pytest.mark.parametrize(
    "wind_dir_str, expected",
    [
        ("N",  1),
        ("NE", 4),
        ("E",  4),
        ("SE", 3),
        ("S",  2),
        ("SW", 2),
        ("W",  1),
        ("NW", 1)
    ]
)
def test_map_wind_dir_to_coeff(wind_dir_str, expected):
    coeff = hughes38_method.map_wind_dir_to_coeff(wind_dir_str)
    assert coeff == expected


@pytest.mark.parametrize(
    "pressure_index, ptrend_index, wind_dir_index, expected_forecast",
    [
        (1, 1, 1, 1),
        (1, 3, 2, 12),
        (2, 2, 2, 14),
        (2, 3, 2, 15),
        (3, 2, 4, 35),
        (3, 3, 4, 36),
        (3, 3, 5, 45),
    ]
)
def test_get_forecaster_index(pressure_index, ptrend_index, wind_dir_index, expected_forecast):
    """

    :return:
    """
    forecast_index = hughes38_method.get_forecaster_index(pressure_index, ptrend_index, wind_dir_index)
    assert forecast_index == expected_forecast


@pytest.mark.parametrize(
    "pressure_str, trend_str, wind_deg, expected",
    [
        ("1023",  "Falling", 185, "Fair for 6 to 12 hours, rising temperatures"),
        ("1010",  "Rising",  45, "Clear with colder weather"),
        ("1006",  "Steady",  181, "Continued stormy weather"),
        ("1001",  "Falling", 45, "Heavy rain, severe NE gale, colder temperatures")
    ]
)
def test_get_forecast_text(pressure_str, trend_str, wind_deg, expected):
    forecaster_text = hughes38_method.get_forecast_text(pressure_str, trend_str, wind_deg)

    assert forecaster_text == expected
