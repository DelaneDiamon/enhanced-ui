# STEP 01 — Environment & Packaging

Goal: Ensure we can pack SSOs into a .pak, place it in the game mods folder, and have pak_config.yaml list it.

What we did:
- Created symlinks to Windows game directories under WSL.
- Added build_pak.py that:
  - Deletes old mods/enhanced_ui.pak if it exists
- Packs `ssl/**` with ZIP_STORED into `mods/enhanced_ui.pak`
  - Ensures C:\...\root\mods\pak_config.yaml contains - pak: enhanced_ui.pak

Validate:
- Run python3 build_pak.py
- Confirm mods/enhanced_ui.pak exists and pak_config.yaml in game dir lists the pak.

Include:
- Ensure your `ssl/` tree contains the Enhanced UI overrides only (attach-only HUD, new widget/view `.sso`, and their `.resource` brand files). Resource files are required for the engine to resolve `UiEnhancedTrackerPanelView` and `UiEnhancedTrackerWidget` types.

Next: Author a minimal panel view and map it into the HUD layout.

---
## Web‑validated updates (2025-10-11)

### Install Targets
- **.pak →** `client_pc/root/mods`
- **Loose files →** `client_pc/root/local`

### Best Practices
- Avoid editing `default_other.pak` directly in releases; keep experiments local and prefer packaged overlays.
- If post‑patch the mod disappears, try generating a `.cache` for your `.pak` (some setups benefit).

### Vanilla Toggle
- To return to online play: remove `root/mods`, verify files, and restart the launcher.
