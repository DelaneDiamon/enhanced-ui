# STEP 03 — PVE Layout Slot & Attachment Mapping

Goal: Make the HUD spawn our panel by defining a slot and mapping the view to it.

Edits (override files placed in pak using exact paths):
- ssl/ui/fusion/hud/hud_layout/ui_hud_pve_view.sso
  - Add canvas child: aura_panel_attach with UiCanvasSlot near grenades (anchorMin/Max at bottom center, offset ~ y=160)
  - In componentsList.UiAttachmentsComponent.attachPoints, add: UiAuraPanelView: aura_panel_attach

Validation:
- Build pak, launch PVE, the panel appears at bottom center area near equipment.

Next: Verify and tweak placement.
