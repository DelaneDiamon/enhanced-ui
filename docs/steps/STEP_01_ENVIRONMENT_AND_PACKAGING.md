# STEP 01 — Environment & Packaging

Goal: Ensure we can pack SSOs into a .pak, place it in the game mods folder, and have pak_config.yaml list it.

What we did:
- Created symlinks to Windows game directories under WSL.
- Added build_pak.py that:
  - Deletes old mods/enhanced_ui.pak if it exists
  - Packs ssl/** with ZIP_STORED into mods/enhanced_ui.pak
  - Ensures C:\...\root\mods\pak_config.yaml contains - pak: enhanced_ui.pak

Validate:
- Run python3 build_pak.py
- Confirm mods/enhanced_ui.pak exists and pak_config.yaml in game dir lists the pak.

Next: Author a minimal panel view and map it into the HUD layout.
