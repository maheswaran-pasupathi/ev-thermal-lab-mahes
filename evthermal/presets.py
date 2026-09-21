from .vehicle import Vehicle

# Representative engineering presets. These are not OEM specifications.
VEHICLE_PRESETS = {
    "2W — Electric scooter": Vehicle(
        mass_kg=180, cd=0.75, frontal_area_m2=0.65, crr=0.015,
        drivetrain_efficiency=0.88, auxiliary_power_kw=0.08, battery_usable_kwh=3.5
    ),
    "3W — Electric cargo": Vehicle(
        mass_kg=650, cd=0.65, frontal_area_m2=1.75, crr=0.015,
        drivetrain_efficiency=0.88, auxiliary_power_kw=0.25, battery_usable_kwh=9.0
    ),
    "4W — Passenger EV": Vehicle(
        mass_kg=1850, cd=0.28, frontal_area_m2=2.30, crr=0.010,
        drivetrain_efficiency=0.92, auxiliary_power_kw=0.60, battery_usable_kwh=60.0
    ),
    "Bus — City EV": Vehicle(
        mass_kg=14000, cd=0.60, frontal_area_m2=8.0, crr=0.008,
        drivetrain_efficiency=0.91, auxiliary_power_kw=5.0, battery_usable_kwh=300.0
    ),
    "Truck — Heavy EV": Vehicle(
        mass_kg=30000, cd=0.55, frontal_area_m2=10.0, crr=0.007,
        drivetrain_efficiency=0.91, auxiliary_power_kw=4.0, battery_usable_kwh=500.0
    ),
}
