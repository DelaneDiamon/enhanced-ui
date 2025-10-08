# Enhanced UI – Implementation Plan

## Goal
- Surface a modular HUD strip that shows the player’s active kit (class ability, grapple, support tools, consumables) and communicates internal cooldowns, durations, and charge states with clear iconography and timers.
- Deliver a reusable data layer so new abilities or perks can plug in without touching HUD layouts.
- Maintain compatibility across Hub, PvE, and PvP HUD variants while staying within the safe UI zone.

## Phase 0 – Baseline & References
- Restore the current mod scaffolding (HUD layout overrides plus secure stockpile widget) into `ssl/` so the build script has working inputs.
- Snapshot pristine copies of the vanilla HUD layouts and weapon/ability widget assets from the live game install for quick diffing when troubleshooting regressions.
- Confirm the packaging flow by running `./build_enhanced_ui_pak.sh` and validating the pak mounts cleanly (`client_pc/root/mods/pak_config.yaml` lists `enhanced_ui.pak`).

## Phase 1 – Ability Inventory & Timer Requirements
- Enumerate every player-facing ability that exhibits a cooldown or duration by scanning `game_mods_source/ssl/abilities/ui/ui_abilities_library.sso` and the class mastery bindings in `game_mods_source/ssl/ui/fusion/hud/squad_panel/code/ui_character_library.sso`.
- For each ability, inspect the matching controller blueprint (e.g., `ability_controller_desc_barrier.sso`, `ability_controller_desc_grappling_hook.sso`) to locate events and float variables that expose:
  - Cast start / completion
  - Cooldown start / length
  - Active duration or lingering effects
  - Stack or charge counters
- Categorise abilities into timer archetypes (simple cooldown, active duration with cooldown, charge-based, resource/energy driven) and document the UI semantics expected for each class in a new planning note.
- Flag abilities lacking clean client events so we can either approximate (e.g., energy bar percentage) or hide them from the initial milestone.

## Phase 2 – HUD Layout & Visual Container
- Introduce a shared attachment container (`ability_timers_attach`) to each HUD layout override:
  - `ssl/ui/fusion/hud/hud_layout/ui_hud_pve_view.sso`
  - `ssl/ui/fusion/hud/hud_layout/ui_hud_pvp_view.sso`
  - `ssl/ui/fusion/hud/hud_layout/ui_hud_hub_view.sso`
- Position the container just above the existing weapon/equipment panel, respecting the secure stockpile attachment and safe zone guidelines; author width scaling rules that collapse into two rows if the screen is narrower than 16:9.
- Build a dedicated widget asset (e.g., `ssl/ui/fusion/hud/ability_timers/ui_player_ability_timers_view.sso`) that instantiates a configurable number of tile children (each tile can reuse `ssl/ui/fusion/hud/ability_timers/ui_ability_timer_tile.sso` created during Phase 1 research).
- Register the widget in the UI asset storage (`game_mods_source/ssl/ui/systems/asset_managing/ui_asset_storage.sso`) so the HUD can request it through the attachments component.

## Phase 3 – Ability Tile Component
- Create a reusable tile prefab (`ui_player_ability_tile.sso`) using existing patterns from `ui_weapon_panel_ability_slot.sso`:
  - `UiSwitcherAbilityIcons` (or equipment switchers) to draw the correct icon variant.
  - A radial `UiElementShapeWipe` for cooldown fill.
  - Optional text overlay (small italic font) for numeric countdown or stack count.
  - Blink/ready state containers driven by animation states.
- Expose bindable fields for `iconKey`, `cooldownPercent`, `timeRemaining`, `state`, and `charges` so the data provider can update without modifying the SSO.
- Author a simple animation sequence (idle, cooldown ticking, ready blink) that mirrors the ultimate slot behaviour but with muted colours to avoid confusing it with the ultimate gauge.

## Phase 4 – Data Provider & Blueprint Plumbing
- Implement a HUD-side data provider blueprint (`ui_player_ability_timers_data_provider.sso`) that subscribes to the local player’s ability systems:
  - Leverage existing widget visibility rules (`WidgetVisibilityRuleActivateAbility`) to tap into activation events where possible.
  - Subscribe directly to ability components for persistent data (cooldown float, energy resource) using client blueprint nodes.
  - Normalize events into UI-friendly messages (e.g., `AbilityTimerStarted`, `AbilityTimerTick`, `AbilityReady`, `AbilityChargeConsumed`).
- Extend or wrap the HUD view delegate so it instantiates the new widget and feeds it the provider (likely via `UiDataDrivenComponent`).
- Ensure the provider gracefully handles ability swaps (loadout changes) by clearing stale entries and repopulating when the player respawns or changes class.
- Add config-driven mapping (`ui_ability_timer_config.sso`) that links ability UID → tile slot order, display mode, and timer behaviour to avoid hardcoding logic in the blueprint.

## Phase 5 – Timer Logic Per Archetype
- **Simple cooldowns**: start timer on cast completion, compute `readyTime = currentTime + cooldownLength`, tick every 0.1s, and snap to ready if an authoritative ready event fires earlier.
- **Duration + cooldown**: display active duration countdown first (highlighted border), then transition into cooldown fill with muted colours.
- **Charge-based abilities**: show max charges in the text overlay, grey out when all charges spent, and animate when a charge regenerates (rare for SM2 but future-proof).
- **Energy/resource abilities**: use percentage fill or hide timer if values fluctuate too rapidly; consider secondary indicators (e.g., energy threshold marker).
- Include fallbacks for missing data (show icon with a question overlay or hide slot entirely) to avoid misleading players.

## Phase 6 – Testing & Validation
- Build test scenarios in a local Training/Menu environment to trigger each ability repeatedly; capture video to evaluate timing accuracy.
- Validate layout scaling on 16:9, 21:9, and 16:10 by forcing windowed resolutions; adjust anchors/padding if tiles drift.
- Verify multiplayer edge cases (spectating teammates, hub zones, downed states) to ensure widget hides or updates appropriately.
- Run a full pak build and smoke test on a live client to confirm no crashes or undefined behaviour occur when abilities fire rapidly.

## Phase 7 – Packaging & Release
- Stage final SSO changes plus any new directories under `pack_ssl/ssl/…`.
- Execute `./build_enhanced_ui_pak.sh` to regenerate `enhanced_ui.pak`; confirm the archive root is `ssl/`.
- Update release notes/readme with ability coverage, known gaps, and instructions for mod managers.
- Tag the repository milestone once QA passes, keeping raw source assets committed for future iterations.

## Immediate Integration Steps
- Trace `UiEquipmentPanelDataProviderBase`/`UiWeaponPanelDataProviderBase` in the runtime to understand how they surface charges and energy so the new timers can subscribe without duplicating logic.
- Compose `ui_player_ability_timers_view.sso` to host multiple `ui_ability_timer_tile.sso` instances and expose attachment slots for the HUD layouts.
- Extend each HUD layout to include the new `ability_timers_attach` point and ensure attachment order plays nicely with `secure_stockpile_attach` and existing weapon panel placements.
- Build a lightweight data provider blueprint that mirrors the ultimate/equipment panel patterns (subscribe to ability energy + equipment charges) and fan-out the data into the new slots; this is the milestone where in-game testing becomes meaningful to verify cooldown visuals update under real combat scenarios.

## Follow-Up Ideas
- Add user settings to toggle individual ability tiles or swap between numeric timers and percent-only mode.
- Explore sharing the data provider with squad HUD elements so teammates’ ability cooldowns can be surfaced in a future update.
- Consider exposing the framework as a library pak so other modders can register additional abilities without forking the HUD layouts.
