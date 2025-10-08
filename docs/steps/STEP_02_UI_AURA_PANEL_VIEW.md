# STEP 02 — Author UiAuraPanelView (MVP container)

Goal: Create a minimal view that can be placed on the HUD. For now, a small container with a placeholder icon.

Deliverables:
- ssl/ui/fusion/hud/aura_panel/ui_aura_panel_view.sso
  - Fusion container (width/height ~ 100x100), hitTest disabled
  - Child: one UiElementBitmap placeholder icon

Validation: View renders when mapped into a layout slot (no data bindings yet).

Next: Add a PVE layout slot and map UiAuraPanelView to it.
