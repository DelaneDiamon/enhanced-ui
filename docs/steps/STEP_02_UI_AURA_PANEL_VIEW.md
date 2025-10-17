# STEP 02 — Enhanced Tracker View + Resources

Goal: Create a view asset for the Enhanced Tracker panel and register it as a brand so it can be referenced by type (`UiEnhancedTrackerPanelView`). No HUD embedding yet.

Deliverables:
- `ssl/ui/fusion/hud/enhanced_tracker/ui_enhanced_tracker_panel_view.sso`
  - `UiFusionContainer` with a single tile (frame, icon, timer, label). Keep it minimal and static for now.
- `ssl/ui/fusion/hud/enhanced_tracker/ui_enhanced_tracker_panel_view.sso.resource`
  - `brandName: UiEnhancedTrackerPanelView`
  - references the `.sso`

Validation:
- Resource resolves (no missing type errors in logs when the asset is referenced).
Notes:
- Avoid custom engine classes. Use existing engine UI types (`UiFusionContainer`, `UiElementBitmap`, `UiFusionTextfield`).
- Keep the visual identical to the previously inlined prototype for continuity.
