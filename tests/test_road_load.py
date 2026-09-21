import math

import pytest

from evthermal import Vehicle, steady_state_road_load


@pytest.fixture
def passenger_ev():
    return Vehicle(
        mass_kg=1800,
        cd=0.28,
        frontal_area_m2=2.3,
        crr=0.010,
        drivetrain_efficiency=0.92,
        auxiliary_power_kw=0.5,
        battery_usable_kwh=60,
    )


def test_flat_zero_wind_force_balance(passenger_ev):
    result = steady_state_road_load(passenger_ev, speed_kph=72)

    v = 20.0
    expected_aero = 0.5 * 1.225 * 0.28 * 2.3 * v**2
    expected_roll = 1800 * 9.80665 * 0.010

    assert result.aero_force_n == pytest.approx(expected_aero)
    assert result.rolling_force_n == pytest.approx(expected_roll)
    assert result.grade_force_n == pytest.approx(0.0, abs=1e-12)
    assert result.total_force_n == pytest.approx(expected_aero + expected_roll)


def test_headwind_increases_aero_load(passenger_ev):
    still = steady_state_road_load(passenger_ev, speed_kph=80, wind_kph=0)
    headwind = steady_state_road_load(passenger_ev, speed_kph=80, wind_kph=20)

    assert headwind.aero_force_n > still.aero_force_n
    assert headwind.battery_power_kw > still.battery_power_kw


def test_positive_grade_increases_power(passenger_ev):
    flat = steady_state_road_load(passenger_ev, speed_kph=60, grade_percent=0)
    climb = steady_state_road_load(passenger_ev, speed_kph=60, grade_percent=8)

    assert climb.grade_force_n > 0
    assert climb.battery_power_kw > flat.battery_power_kw


def test_range_is_energy_over_consumption(passenger_ev):
    result = steady_state_road_load(passenger_ev, speed_kph=80)
    expected = passenger_ev.battery_usable_kwh * 1000 / result.energy_wh_per_km
    assert result.estimated_range_km == pytest.approx(expected)


def test_rejects_invalid_speed(passenger_ev):
    with pytest.raises(ValueError):
        steady_state_road_load(passenger_ev, speed_kph=0)
