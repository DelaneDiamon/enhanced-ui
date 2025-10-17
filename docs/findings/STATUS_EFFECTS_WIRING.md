# Status Effects HUD Wiring (Reference)

This document summarizes how the official client wires the Status Effects panel into the HUD. It serves as the pattern to follow for the Enhanced Tracker panel.

## Chain Overview
- Asset holder registers the view type
  - File: `mods_source/ssl/ui/systems/asset_managing/ui_asset_storage.sso:1086-1100`
  - Entry: `StatusEffectPanel` → `__type = "UiStatusEffectPanelView"`, `layer = "HUD"`.

- HUD layout maps view type to an attach point
  - File: `mods_source/ssl/ui/fusion/hud/hud_layout/ui_hud_pve_view.sso:59-61`
  - Mapping: `UiStatusEffectPanelView = "status_effect"`.
  - Attach container: `childs.status_effect` is a simple `UiFusionContainer` (no content), e.g. `:337-357`.

- Screen spawns the widget instance
  - File: `mods_source/ssl/ui/fusion/hud/hud_layout/code/pve/ui_pve_screen.sso:140-147`
  - Widget: `__type = "UiStatusEffectPanelWidget"` with `providerDesc` of `UiStatusEffectPanelDataProvider`.
  - The widget’s asset file links to the asset holder via `assetLink = "Hud.StatusEffectPanel"`.

- View visuals and logic
  - File: `mods_source/ssl/ui/fusion/hud/status_fx/ui_status_effect_panel_view.sso`
  - Uses engine UI classes: `UiStatusEffectPulse`, `UiStatusEffectPanelProgress`, `UiStatusEffectFx`, etc.
  - Data-driven by `ui_status_effect_panel_data_provider.sso`.

## Key Points To Mirror
- HUD layout should only declare attach points (containers), not embed the panel’s visuals.
- Add a new asset holder in `ui_asset_storage.sso` for the new view type (e.g., `UiEnhancedTrackerPanelView`).
- Create a widget with an `assetLink` (e.g., `Hud.EnhancedTrackerPanel`) and optionally a provider.
- Update the HUD screen (`ui_pve_screen.sso`) to spawn the widget instance.
- Map the new view type to a named attach container in the HUD layout.

## File References (for convenience)
- Asset holder: `mods_source/ssl/ui/systems/asset_managing/ui_asset_storage.sso:1086-1100`
- HUD layout mapping: `mods_source/ssl/ui/fusion/hud/hud_layout/ui_hud_pve_view.sso:59-61`
- HUD layout attach container: `mods_source/ssl/ui/fusion/hud/hud_layout/ui_hud_pve_view.sso:337-357`
- Screen spawn: `mods_source/ssl/ui/fusion/hud/hud_layout/code/pve/ui_pve_screen.sso:140-147`
- Widget defaults: `mods_source/ssl/ui/fusion/hud/status_fx/code/ui_status_effect_panel_widget.sso`
- Provider: `mods_source/ssl/ui/fusion/hud/status_fx/code/ui_status_effect_panel_data_provider.sso`

