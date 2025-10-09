# Enhanced UI Tracker Mod – Implementation Plan

## Goals
- Add a configurable HUD panel that displays player talents/buffs/abilities/perks with cooldowns/readiness.
- Start with a static prototype (single secure_stockpile icon), then iterate to live data via data providers.

## Phased Steps

1) Baseline + Packaging
- Ensure `mods` and `mods_source` symlinks work; verify `build_pak.py` builds `enhanced_ui.pak` into the game `mods` folder.
- Validation: run `python build_pak.py`, confirm `mods/enhanced_ui.pak` appears.

2) Minimal HUD Injection (DONE)
- Copied the game’s `ui_hud_pve_view.sso` and added `enhanced_ui_panel` anchored bottom-right.
- Placed a static `secure_stockpile` icon and added a temporary magenta debug background.
- Validation: confirmed icon renders in PVE; anchor semantics verified.

3) Perk-Style Tile (IN PROGRESS)
- Replace debug background with a perk-style square frame and keep the secure_stockpile icon centered.
- Add a small text label placeholder under the icon (e.g., “Restock”).
- Validation: icon appears on a square perk frame; label visible below.

4) Reusable Panel Prefab (NEXT)
- Extract the tile into `ssl/ui/fusion/hud/enhanced_panel/ui_enhanced_ui_panel_view.sso` and attach via `UiAttachmentsComponent`.
- Validation: same visuals; HUD layout remains clean.

4) Registry of Trackables
- Author a registry SSO mapping game abilities/perks/status-effects to: icon key/asset, trigger conditions, color/tint rules, stack display, sort priority.
- Seed the registry with a small set (e.g., ultimate ability, a couple status effects, and 2–3 perks).
- Validation: debug log or temporary panel shows the resolved icons from the registry.

5) Data Provider (Client)
- Implement a client-side SSL data provider that subscribes to: ability manager (cooldowns), perk activation events, and status effect subscriptions.
- Normalize output to a list of entries: `{id, iconKey, remainingMs, totalMs, stacks, ready}`.
- Validation: instrument provider with temporary text or logging; check values change when using abilities.

6) Dynamic UI Binding
- Update the panel view to bind to the provider entries and auto-spawn item slots.
- Each slot: icon, radial or linear progress, numeric countdown, optional stack badge and readiness glow.
- Validation: trigger abilities/perks/status effects; the panel updates and animations play.

7) Config + UX
- Add a lightweight config SSO (e.g., `ssl/ui/enhanced_ui/config.sso`) to toggle tracked items, order, and alert thresholds.
- Add simple keyboard toggle to hide/show panel if desired.
- Validation: edit config, rebuild, and verify changes in-game without code changes.

8) Polish + Packaging
- Add gentle animations, fade rules to respect scoping/QTE, and HUD layering sanity.
- Document installation and troubleshooting.
- Validation: full playtest across classes to ensure correctness and no visual clashes.

## Test Loop
- After each step, rebuild with `python build_pak.py` and ensure the updated `enhanced_ui.pak` appears under the game `mods` folder.
- Relaunch the game (or reload level) to see changes.
