from dataclasses import dataclass
from math import atan, cos, sin

from .vehicle import Vehicle

G = 9.80665


@dataclass(frozen=True)
class RoadLoadResult:
    aero_force_n: float
    rolling_force_n: float
    grade_force_n: float
    total_force_n: float
    wheel_power_kw: float
    battery_power_kw: float
    energy_wh_per_km: float
    estimated_range_km: float
    relative_air_speed_kph: float


def steady_state_road_load(
    vehicle: Vehicle,
    speed_kph: float,
    grade_percent: float = 0.0,
    wind_kph: float = 0.0,
    air_density_kg_m3: float = 1.225,
) -> RoadLoadResult:
    """Calculate steady-state road load.

    wind_kph uses a signed longitudinal convention:
    positive = headwind, negative = tailwind.
    """

    vehicle.validate()

    if speed_kph <= 0:
        raise ValueError("speed_kph must be greater than zero")
    if air_density_kg_m3 <= 0:
        raise ValueError("air_density_kg_m3 must be greater than zero")

    speed_m_s = speed_kph / 3.6
    relative_air_speed_m_s = max(0.0, (speed_kph + wind_kph) / 3.6)
    theta = atan(grade_percent / 100.0)

    aero_force = (
        0.5
        * air_density_kg_m3
        * vehicle.cd
        * vehicle.frontal_area_m2
        * relative_air_speed_m_s**2
    )
    rolling_force = vehicle.mass_kg * G * vehicle.crr * cos(theta)
    grade_force = vehicle.mass_kg * G * sin(theta)
    total_force = aero_force + rolling_force + grade_force

    wheel_power_kw = total_force * speed_m_s / 1000.0

    if wheel_power_kw >= 0:
        battery_power_kw = (
            wheel_power_kw / vehicle.drivetrain_efficiency
            + vehicle.auxiliary_power_kw
        )
    else:
        battery_power_kw = vehicle.auxiliary_power_kw

    energy_wh_per_km = battery_power_kw * 1000.0 / speed_kph
    estimated_range_km = (
        vehicle.battery_usable_kwh * 1000.0 / energy_wh_per_km
        if energy_wh_per_km > 0
        else float("inf")
    )

    return RoadLoadResult(
        aero_force_n=aero_force,
        rolling_force_n=rolling_force,
        grade_force_n=grade_force,
        total_force_n=total_force,
        wheel_power_kw=wheel_power_kw,
        battery_power_kw=battery_power_kw,
        energy_wh_per_km=energy_wh_per_km,
        estimated_range_km=estimated_range_km,
        relative_air_speed_kph=relative_air_speed_m_s * 3.6,
    )
