# STEP 04 — Build & Verify In-Game

Goal: Package and confirm the panel shows.

Procedure:
- Run python3 build_pak.py (deletes old pak, rebuilds, updates config)
- Start game → main menu should display "Mods detected".
- Load PVE; ensure the panel is visible near grenades.

If missing:
- Re-check file paths inside pak, and attachment mapping.
- Nudge offsetMin/offsetMax to adjust position.

Next: Add a real tile (UiAuraTile) and basic visuals (counter, blink, bar) for later data feeds.
