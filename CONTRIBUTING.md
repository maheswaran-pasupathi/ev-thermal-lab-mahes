# Contributing

Thank you for helping improve EV Thermal Performance Lab.

## Good contributions
- reproducible physics or numerical improvements
- public validation cases with traceable sources
- unit tests and benchmark checks
- route, weather, battery or thermal-model extensions
- documentation improvements
- accessibility and user-experience improvements
- bug reports with a minimal reproducible example

## Before opening a pull request
1. Open or reference an issue for non-trivial model changes.
2. Keep the change focused.
3. Add or update tests.
4. Document equations, assumptions, units and limitations.
5. Use only data you are legally permitted to share.
6. Do not include confidential employer, OEM, customer or proprietary data.
7. Run:
   ```bash
   pytest
   ```
8. Update the changelog when the change affects users.

## Engineering contribution standard
A new physical submodel should document:
- purpose
- inputs and units
- equations
- outputs
- assumptions
- numerical limits
- verification method
- validation status

## Pull requests
Maintainers may request changes when:
- units are unclear
- assumptions are hidden
- validation claims are unsupported
- source data are not redistributable
- changes make the model harder to reproduce

By contributing, you agree that your contribution is provided under the repository's Apache-2.0 license.
