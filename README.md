# EV Thermal Performance Lab

Physics-based vehicle energy, road-load, battery and thermal-performance analysis.

**Production app target:** https://ev-thermal-lab-mahes.streamlit.app

EV Thermal Performance Lab is an open engineering tool for transparent first-principles analysis across electric 2-wheelers, 3-wheelers, passenger vehicles, buses and trucks. The project is designed to grow from road-load and range calculations into route-, weather-, battery- and thermal-management-aware simulation.

## Current release scope — v0.1.0
- benchmark vehicle presets for 2W, 3W, 4W, bus and truck
- custom vehicle inputs
- steady-state aerodynamic, rolling and grade forces
- wheel power and battery-power estimate
- simple energy-consumption and range estimate
- headwind / tailwind input
- transparent equations and assumptions
- downloadable calculation summary

## Engineering model

```text
F_total = F_aero + F_roll + F_grade
F_aero  = 0.5 * rho * Cd * A * v_rel^2
F_roll  = m * g * Crr * cos(theta)
F_grade = m * g * sin(theta)
P_wheel = F_total * v
```

Battery power is estimated from wheel power using a user-defined drivetrain efficiency and auxiliary load.

## Planned capabilities
- standard drive cycles and uploaded speed traces
- SOC trajectory and regenerative braking
- real-route elevation and grade
- weather, wind direction and precipitation
- battery SOH and temperature effects
- LFP/NMC electro-thermal models
- battery cooling and thermal-management demand
- HVAC / heat-pump loads
- fast charging and preconditioning
- scenario comparison
- public validation benchmarks

## Installation

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Python package

The physics layer is kept separate from the web interface so it can also be reused programmatically.

```python
from evthermal import Vehicle, steady_state_road_load

vehicle = Vehicle(
    mass_kg=1800,
    cd=0.28,
    frontal_area_m2=2.3,
    crr=0.010,
)

result = steady_state_road_load(
    vehicle=vehicle,
    speed_kph=80,
    grade_percent=0,
    wind_kph=0,
)
print(result)
```

## Benchmark data

The built-in benchmark vehicles use representative public/synthetic engineering values. They are not OEM specifications and must not be interpreted as confidential or production vehicle data.

## Validation status

The current release is a first-principles engineering baseline. Analytical checks are included in the test suite. Vehicle-specific experimental validation will be added incrementally and documented explicitly.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md), open an issue for proposed model changes, or submit a focused pull request with verification evidence.

## License

Apache License 2.0. See [LICENSE](LICENSE).

Maintained by **Maheswaran Pasupathi**.
