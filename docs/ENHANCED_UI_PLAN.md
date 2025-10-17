# Enhanced UI Tracker Mod – Implementation Plan

## Goals
- Add a configurable HUD panel that displays player talents/buffs/abilities/perks with cooldowns/readiness.
- Start with a static prototype (single secure_stockpile icon), then iterate to live data via data providers.

## Phased Steps

1) Baseline + Packaging
- Ensure `mods` and `mods_source` symlinks work; verify `build_pak.py` builds `enhanced_ui.pak` into the game `mods` folder.
- Validation: run `python build_pak.py`, confirm `mods/enhanced_ui.pak` appears.

2) Minimal HUD Injection (Revisited)
- Current build keeps HUD overrides minimal; the Enhanced Tracker attach point is temporarily removed while we debug mission loading.
- Validation: HUD behaves like vanilla aside from our prior layout clean-up.

3) Perk-Style Tile (DONE)
- Replaced the debug square with a perk-style frame and centered the secure_stockpile icon.
- Added label (“Restock”) and timer placeholder (“60.0”) to define typography.
- Validation: tile renders with frame, timer stub, and caption in PVE.

4) Reusable Panel Prefab (Paused)
- View/widget/provider assets exist in the repo but are not currently loaded. We’ll reintroduce them after confirming the reduced override set loads reliably.

4) Registry of Trackables
- Author a registry SSO mapping game abilities/perks/status-effects to: icon key/asset, trigger conditions, color/tint rules, stack display, sort priority.
- Seed the registry with a small set (e.g., ultimate ability, a couple status effects, and 2–3 perks).
- Validation: debug log or temporary panel shows the resolved icons from the registry.

5) Data Provider (Client)
- Implement a client-side SSL data provider that subscribes to: ability manager (cooldowns), perk activation events, and status effect subscriptions.
- Normalize output to a list of entries: `{id, iconKey, remainingMs, totalMs, stacks, ready}`.
- Validation: instrument provider with temporary text or logging; check values change when using abilities.

6) Dynamic UI Binding (Later)
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

## Working Notes: SM2 UI Modding (Current Understanding)

- Formats and layering
  - `SSO` are text objects (canvas, views, assets); `SSL` is script/logic; `CLS/PROP` are actors/properties. UI is largely SSO with engine UI classes.
  - Mods overlay the base game by path. Our pak must preserve `ssl/...` paths; only include files we override to minimize risk.
  - HUD roots (e.g., `ui_hud_pve_view.sso`) use `UiAttachmentsComponent` to expose named attach points; widgets attach there via screen code (see `ui_pve_screen.sso`).

- Canvas and layout semantics
  - HUD canvas authored for 1920×1080; anchors (`anchorMin/Max`) define origin; offsets are in canvas pixels and scale to actual resolution.
  - Bottom-right anchoring uses `x = 1, y = 1`; offsets are typically negative to move inward from that corner.
  - Use `UiFusionContainer` for grouping, `UiElementBitmap` for images, `UiFusionTextfield` for text; avoid undefined custom `__type` classes (causes loader crash).

- Safe composition patterns
  - Inline new UI under existing canvases first; defer prefab extraction until we can reference via proven mechanisms (e.g., asset holders or widget classes already registered).
  - Prefer existing textures (e.g., armory perk frames, switcher perk icons) to match style and ensure assets exist.
  - For icon libraries, refer to switchers like `ssl/ui/fusion/assets/switchers/perk_icons/ui_switcher_perk_icons.sso` to discover available icon keys/assets.

- Data flow and providers
  - Many widgets are declared as `UiDataProviderBased` and are driven by SSL providers (see `ui_status_effect_panel_data_provider.sso`).
  - For ability/ultimate visuals, study weapon panel files (`ui_weapon_panel_ability_slot.sso`, `ui_ultimate_image.sso`, `ui_ultimate_counter.sso`) to reuse progress bars/counters/animations.
  - Status effects panel demonstrates a list of items with progress overlays (`UiStatusEffectPanelView` + `UiStatusEffectPanelProgress`).

- Packaging & config
  - `build_pak.py` creates `mods/enhanced_ui.pak` with `ssl/` at root and appends `- pak: enhanced_ui.pak` to `pak_config.yaml` under the game’s `mods` folder.
  - Validate by listing `mods/` and ensuring the entry exists in `pak_config.yaml`.

- Debugging strategies
  - Add temporary backgrounds/tints and text to confirm placement and layering before adding logic.
  - If the game crashes on “Loading Resources”, suspect invalid `__type` or missing texture paths. Revert to last known-good inline UI.
  - Make one change at a time; rebuild pak and retest. Keep screenshots with a consistent naming convention (`progress_step_XX_shortdesc.png`).

- Roadmap guardrails
  - Visual first (tiles, labels, timer placeholders) → mock logic (local 60→0 countdown) → real data provider (subscribe to ability/perk systems) → polish (animations, alerts).
  - Avoid replacing large HUD files unnecessarily; keep diffs minimal and focused to reduce incompatibilities.

---
## Web‑validated updates (2025-10-11)

### Live Status Seeds (Patch 10.x example)
Add early entries to your **Trackables Registry** (IDs, icons, tints, stack rules), e.g.:
```json
[
  {"id":"burning","iconKey":"ui/icon_status_burning","priority":80,"tint":"#FF4A4A","stackRule":"add","sort":"timeAsc"},
  {"id":"suppressed","iconKey":"ui/icon_status_suppressed","priority":60,"tint":"#A0A0FF","stackRule":"replace","sort":"prioDesc"}
]
```

### Distribution Strategy
Prefer **attachment‑point diffs** over whole‑file HUD replacements. This minimizes conflicts with other HUD/UI mods and future patches.

### Online Play Reminder
Ship a prominent note: “Using this HUD panel will mark the game as modded. Remove the `.pak` from `root/mods` before online play.”
