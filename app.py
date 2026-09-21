import pandas as pd
import streamlit as st

from evthermal import Vehicle, steady_state_road_load
from evthermal.presets import VEHICLE_PRESETS

st.set_page_config(
    page_title="EV Thermal Performance Lab",
    page_icon="⚡",
    layout="wide",
)

st.title("EV Thermal Performance Lab")
st.caption("Physics-based vehicle energy, road-load and range analysis")

with st.sidebar:
    st.header("Vehicle setup")
    preset_name = st.selectbox(
        "Vehicle",
        list(VEHICLE_PRESETS) + ["Custom"],
    )

    if preset_name == "Custom":
        base = Vehicle(
            mass_kg=1800,
            cd=0.28,
            frontal_area_m2=2.3,
            crr=0.010,
            drivetrain_efficiency=0.92,
            auxiliary_power_kw=0.6,
            battery_usable_kwh=60,
        )
    else:
        base = VEHICLE_PRESETS[preset_name]

    mass = st.number_input("Total mass [kg]", 50.0, 60000.0, float(base.mass_kg), 10.0)
    cd = st.number_input("Drag coefficient Cd [-]", 0.05, 1.50, float(base.cd), 0.01)
    area = st.number_input("Frontal area [m²]", 0.2, 15.0, float(base.frontal_area_m2), 0.1)
    crr = st.number_input("Rolling resistance Crr [-]", 0.001, 0.050, float(base.crr), 0.001, format="%.3f")
    efficiency = st.slider("Drivetrain efficiency", 0.50, 1.00, float(base.drivetrain_efficiency), 0.01)
    aux = st.number_input("Auxiliary power [kW]", 0.0, 30.0, float(base.auxiliary_power_kw), 0.1)
    battery = st.number_input("Usable battery energy [kWh]", 0.5, 1500.0, float(base.battery_usable_kwh), 0.5)

    st.header("Operating condition")
    speed = st.slider("Vehicle speed [km/h]", 5, 160, 80)
    grade = st.slider("Road grade [%]", -20.0, 25.0, 0.0, 0.5)
    wind = st.slider("Longitudinal wind [km/h]", -60, 60, 0, help="Positive = headwind; negative = tailwind")
    rho = st.number_input("Air density [kg/m³]", 0.80, 1.40, 1.225, 0.005, format="%.3f")

vehicle = Vehicle(
    mass_kg=mass,
    cd=cd,
    frontal_area_m2=area,
    crr=crr,
    drivetrain_efficiency=efficiency,
    auxiliary_power_kw=aux,
    battery_usable_kwh=battery,
)

try:
    result = steady_state_road_load(
        vehicle=vehicle,
        speed_kph=float(speed),
        grade_percent=float(grade),
        wind_kph=float(wind),
        air_density_kg_m3=float(rho),
    )
except ValueError as exc:
    st.error(str(exc))
    st.stop()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Battery power", f"{result.battery_power_kw:.1f} kW")
k2.metric("Energy consumption", f"{result.energy_wh_per_km:.0f} Wh/km")
k3.metric("Estimated range", f"{result.estimated_range_km:.0f} km")
k4.metric("Total road load", f"{result.total_force_n:.0f} N")

st.subheader("Road-load breakdown")
forces = pd.DataFrame(
    {
        "Component": ["Aerodynamic", "Rolling", "Grade"],
        "Force [N]": [
            result.aero_force_n,
            result.rolling_force_n,
            result.grade_force_n,
        ],
    }
)
st.bar_chart(forces.set_index("Component"))

c1, c2 = st.columns(2)
with c1:
    st.subheader("Power")
    st.write(f"Wheel power: **{result.wheel_power_kw:.2f} kW**")
    st.write(f"Battery power: **{result.battery_power_kw:.2f} kW**")
    st.write(f"Relative air speed: **{result.relative_air_speed_kph:.1f} km/h**")
with c2:
    st.subheader("Assumptions")
    st.write("Steady speed, constant grade and constant longitudinal wind.")
    st.write("Positive wind is a headwind; negative wind is a tailwind.")
    st.write("Benchmark vehicles use representative engineering values, not OEM specifications.")
    st.write("Range is a first-order estimate from usable battery energy divided by steady-state Wh/km.")

st.subheader("Equations")
st.latex(r"F_{aero}=\frac{1}{2}\rho C_d A v_{rel}^{2}")
st.latex(r"F_{roll}=mgC_{rr}\cos(\theta)")
st.latex(r"F_{grade}=mg\sin(\theta)")
st.latex(r"P_{wheel}=F_{total}v")

summary = pd.DataFrame(
    {
        "metric": [
            "aero_force_n",
            "rolling_force_n",
            "grade_force_n",
            "total_force_n",
            "wheel_power_kw",
            "battery_power_kw",
            "energy_wh_per_km",
            "estimated_range_km",
        ],
        "value": [
            result.aero_force_n,
            result.rolling_force_n,
            result.grade_force_n,
            result.total_force_n,
            result.wheel_power_kw,
            result.battery_power_kw,
            result.energy_wh_per_km,
            result.estimated_range_km,
        ],
    }
)
st.download_button(
    "Download result CSV",
    summary.to_csv(index=False).encode("utf-8"),
    file_name="ev_thermal_lab_result.csv",
    mime="text/csv",
)

st.caption("v0.1.0 · Apache-2.0 · Maintained by Maheswaran Pasupathi")
