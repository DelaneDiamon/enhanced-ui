# STEP 03 — PVE Layout Slot & Attachment Mapping

Goal: Prepare HUD attach-only mapping and rely on widget spawning (official pattern).

Edits (override files placed in pak using exact paths):
- `ssl/ui/fusion/hud/hud_layout/ui_hud_pve_view.sso`
  - Add canvas child: `enhanced_ui_panel_attach` as an empty `UiFusionContainer` (attach-only), positioned where the prototype was.
  - In `componentsList.UiAttachmentsComponent.attachPoints`, add: `UiEnhancedTrackerPanelView: "enhanced_ui_panel_attach"`.

Validation:
- Build pak, launch PVE, verify no errors. The panel will appear only after Step 04 (screen spawn + asset registration).

Next: Verify and tweak placement.

---
## Web‑validated updates (2025-10-11)

### Minimal, Surgical Overrides
Keep the layout diff as small as possible:
- Add a single attach container (e.g., `enhanced_ui_panel_attach`) anchored where desired.
- Map `UiEnhancedTrackerPanelView` via `componentsList.UiAttachmentsComponent.attachPoints`.
- Do NOT embed the panel visuals in the HUD layout.

### Regression Tip
If the panel stops appearing after a patch:
- Rebuild your `.pak`
- Confirm path `root/mods`
- Consider generating a `.cache`
