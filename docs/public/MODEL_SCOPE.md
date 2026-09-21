# Model Scope

## Current model
Version 0.1.0 provides a steady-state longitudinal road-load model.

Included:
- aerodynamic drag
- rolling resistance
- road grade
- drivetrain efficiency
- auxiliary power
- simple energy consumption
- simple usable-energy range estimate

Not yet included:
- acceleration/inertia
- regenerative braking
- transient SOC
- battery temperature dependence
- HVAC
- thermal-management loops
- route APIs
- weather APIs
- traffic
- precipitation physics beyond future planned extensions

## Wind convention
The current UI accepts signed longitudinal wind:
- positive: headwind
- negative: tailwind

Future route-aware releases will resolve wind vectors using route heading.

## Intended use
Engineering exploration, education, reproducible benchmarking and early-stage sensitivity studies.

## Not intended for
Certification, homologation, safety-critical limits or OEM production sign-off without appropriate independent validation.
