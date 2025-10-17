# STEP 04 — Build & Verify In-Game

Goal: Package and confirm the panel shows (after asset registration + screen spawn).

Procedure:
- Run `python3 build_pak.py` (deletes old pak, rebuilds, updates config).
- Start game → main menu should display "Mods detected".
- Load PVE; ensure both Status Effects and the new Enhanced Tracker panel are present.

If missing:
- Re-check `ui_asset_storage.sso` has `EnhancedTrackerPanel` holder with `__type = "UiEnhancedTrackerPanelView"` in HUD layer.
- Confirm `ui_pve_screen.sso` includes `EnhancedTrackerPanel = { __type = "UiEnhancedTrackerWidget" }`.
- Check HUD layout mapping for `UiEnhancedTrackerPanelView` and the attach container exists.
- Nudge offsets for placement.

Next: Add a real tile (UiAuraTile) and basic visuals (counter, blink, bar) for later data feeds.

---
## Web‑validated updates (2025-10-11)

### Success Signals
- Main menu acknowledges modded state (varies by build).
- In mission, the **magenta debug block** (if enabled) is visible at the intended location.

### Failure Matrix Additions
- **No panel but mod state detected:** wrong path (not in `root/mods`) or missing `.cache` in some environments.
- **Online blocked:** remove `root/mods` and verify game files.

### Notes
- Integration Studio + Vortex both support the documented folder map. Keep a clean profile for online sessions.
