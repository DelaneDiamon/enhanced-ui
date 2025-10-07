# Enhanced UI – Current State

## Mod Identity
- Pak file: `client_pc/root/mods/enhanced_ui.pak`
- Config: `client_pc/root/mods/pak_config.yaml` contains `- pak: enhanced_ui.pak`
- Packaging rule: pak root is `ssl/` (never `mods_source/`).

## Features (as of now)
- Draws a Secure Stockpile perk icon on the main HUD in all contexts:
  - Hub (hangar), PvE, and PvP HUD layouts.
- Icon placement: bottom-center, above ability/equipment HUD.
- Icon size: 64x64 (for visibility without obstruction).
- Purpose: verify a reliable HUD draw path before wiring timing/toggle logic.

## Files Overridden by the Mod
- `ssl/ui/fusion/hud/hud_layout/ui_hud_pve_view.sso`
- `ssl/ui/fusion/hud/hud_layout/ui_hud_pvp_view.sso`
- `ssl/ui/fusion/hud/hud_layout/ui_hud_hub_view.sso`

Each layout includes a static element:
```text
secure_stockpile_icon (UiElementBitmap)
  anchor: bottom-center (anchorMin = anchorMax = (0.5, 0))
  offsetMin: (0, 145)
  size: 64x64
  texture: textures/ui/weapon_progression/weapon_perk_icons/pve_soldier_restore_equipment_team_perk.asset/pve_soldier_restore_equipment_team_perk.texture.asset
```

## Known Good Build Flow
1) Stage edited files under `pack_ssl/ssl/...` matching game paths.
2) Zip the staging so the top-level entry is `ssl/`.
3) Rename `.zip` → `.pak` and place into `mods/`.
4) Confirm title shows "Mods detected" on launch.

## Notes on Debug Paths
- Retail builds may ignore some debug toggles even with `isEnabledInRetail = True`.
- Testing Menu demonstrates input→UI via class blueprints and scenario events; we will mirror that after validating the HUD path.

## Next Steps
- Add input-driven toggle (Testing Menu style): bind a key to an existing scenario event to show/hide the icon on demand.
- Replace static icon with a small HUD widget that can display a countdown (60s Secure Stockpile cooldown).
- Make the widget conditional on the Tactical class being in party.
