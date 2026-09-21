# Changelog

All notable user-facing changes are documented here.

The project follows Semantic Versioning.

## [0.1.0] - 2026-09-21

### Added
- production repository foundation
- Streamlit road-load calculator
- 2W, 3W, 4W, bus and truck representative presets
- custom vehicle inputs
- aerodynamic, rolling and grade force calculation
- wheel-power and battery-power estimation
- simple Wh/km and range estimates
- downloadable result summary
- unit tests and CI
- contribution, support, security and issue-management templates

### Known limitations
- steady-state analysis only
- wind is currently entered as a signed longitudinal component
- no transient SOC model in this release
- no thermal network, HVAC or route API integration yet
- benchmark vehicles are representative, not OEM-specific
