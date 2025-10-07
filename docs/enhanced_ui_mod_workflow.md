# Enhanced UI Mod Workflow

## Overview

This document records the end-to-end flow for editing data in `mods_source`, packaging it into the `Enhanced UI` mod, and verifying the changes in-game.

## Steps

1. **Edit Source Asset**
   - Modify the desired file directly under `mods_source`. Example: set `isEnabledInRetail = True` in `ssl/debug/debug_hot_keys/debug_hotkey_manager_client.sso` so retail builds honor debug hotkeys.

2. **Stage Files for Packaging**
   - Create a temporary build directory (e.g. `pack_ssl/`).
   - Mirror the in-game folder structure inside it and copy only the edited files. The TOP-LEVEL folder inside the pak MUST be `ssl/` (never `mods_source/`). Examples:
     - Debug hotkeys: `pack_ssl/ssl/debug/debug_hot_keys/debug_hotkey_manager_client.sso`
     - HUD icon test (current mod):
       - `pack_ssl/ssl/ui/fusion/hud/hud_layout/ui_hud_pve_view.sso`
       - `pack_ssl/ssl/ui/fusion/hud/hud_layout/ui_hud_pvp_view.sso`
       - `pack_ssl/ssl/ui/fusion/hud/hud_layout/ui_hud_hub_view.sso`

3. **Create the .pak**
   - From the game root (`client_pc/root`), compress the staged contents so the archive ROOT is `ssl/`:
     - PowerShell (Windows):
       ```powershell
       # stage is pack_ssl\ssl\...
       Compress-Archive -Path pack_ssl\* -DestinationPath mods\enhanced_ui.zip -Force
       Rename-Item mods\enhanced_ui.zip enhanced_ui.pak -Force
       ```
     - Git Bash (ZIP with ssl at root):
       ```bash
       ( cd pack_ssl && zip -r -9 ../mods/enhanced_ui.zip ssl )
       mv -f mods/enhanced_ui.zip mods/enhanced_ui.pak
       ```
   - Verify the pak root with 7‑Zip (or `unzip -l`). The first entry MUST be `ssl/`.

4. **Register the Pak**
   - Ensure `mods/pak_config.yaml` lists the pak so it always loads:
     ```
     - pak: enhanced_ui.pak
     ```

5. **Clean Up**
   - Remove the temporary build folder after packaging:
     ```powershell
     Remove-Item -Recurse -Force pack_ssl
     ```

6. **Verify In-Game**
   - Restart the game (mods load at startup only). The title screen should show "Mods detected".
   - For this mod, a Secure Stockpile perk icon is drawn in HUD layouts (see Current State doc). If testing debug hotkeys, press and HOLD `Ctrl+Alt+P` during gameplay; note retail builds may gate some debug UIs beyond `isEnabledInRetail`.

## Refreshing After Further Edits

Repeat steps 1–5 for any future changes, overwriting `mods/enhanced_ui.pak`, then restart the game to pick up the new data.

## Dependencies

No additional mods are required. `enhanced_ui.pak` loads independently through `pak_config.yaml`.

## Troubleshooting

- No "Mods detected" at launch:
  - The pak likely has the wrong root. Open `mods/enhanced_ui.pak` in 7‑Zip; the top-level must be `ssl/` (not `mods_source/`). Rebuild with the staging method above.
  - Ensure the file extension is `.pak`, not `.zip`.
  - Confirm `mods/pak_config.yaml` contains `- pak: enhanced_ui.pak`.
- UI not visible after repack:
  - Verify you overwrote the correct HUD layout files under `ssl/ui/fusion/hud/hud_layout/`.
  - Restart fully to desktop; hot reload is not supported for paks.

## Using a Known-Good Pak as a Base (Optional)

You can copy a working pak (e.g., Testing Menu) to `mods/enhanced_ui.pak`, open it in 7‑Zip, and drag your edited `ssl/...` files into the appropriate folders. This guarantees the archive root and structure are valid.


