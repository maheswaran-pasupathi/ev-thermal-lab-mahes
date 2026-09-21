from dataclasses import dataclass


@dataclass(frozen=True)
class Vehicle:
    """Minimal vehicle definition for longitudinal road-load calculations."""

    mass_kg: float
    cd: float
    frontal_area_m2: float
    crr: float
    drivetrain_efficiency: float = 0.90
    auxiliary_power_kw: float = 0.5
    battery_usable_kwh: float = 60.0

    def validate(self) -> None:
        if self.mass_kg <= 0:
            raise ValueError("mass_kg must be greater than zero")
        if self.cd <= 0:
            raise ValueError("cd must be greater than zero")
        if self.frontal_area_m2 <= 0:
            raise ValueError("frontal_area_m2 must be greater than zero")
        if self.crr < 0:
            raise ValueError("crr cannot be negative")
        if not 0 < self.drivetrain_efficiency <= 1:
            raise ValueError("drivetrain_efficiency must be in (0, 1]")
        if self.auxiliary_power_kw < 0:
            raise ValueError("auxiliary_power_kw cannot be negative")
        if self.battery_usable_kwh <= 0:
            raise ValueError("battery_usable_kwh must be greater than zero")
