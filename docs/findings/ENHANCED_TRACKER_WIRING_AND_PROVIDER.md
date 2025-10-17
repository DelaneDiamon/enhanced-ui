# Enhanced Tracker – Wiring Diagram and Provider Stub

This document shows how the Enhanced Tracker panel is wired into the HUD (following the official Status Effects pattern) and explains the basic provider stub used for a static countdown.

## High‑Level Wiring

Mermaid (conceptual component flow):

```mermaid
flowchart LR
  subgraph AssetStorage
    A[EnhancedTrackerPanel → UiEnhancedTrackerPanelView]
  end

  subgraph HUDLayout
    B[UiAttachmentsComponent]
    C[enhanced_ui_panel_attach (UiFusionContainer)]
  end

  subgraph Screen(PVE Screen)
    D[UiEnhancedTrackerWidget\nprovider: UiEnhancedTrackerDataProvider]
  end

  A -->|layer: HUD| D
  D -->|assetLink: Hud.EnhancedTrackerPanel| A
  B -->|UiEnhancedTrackerPanelView = "enhanced_ui_panel_attach"| C
  D -->|instantiated view attaches into| C
```

File references:
- Asset holder: `mods_source/ssl/ui/systems/asset_managing/ui_asset_storage.sso`
  - `EnhancedTrackerPanel` has `__type = "UiEnhancedTrackerPanelView"`.
- HUD layout mapping + attach point: `mods_source/enhanced_ui/ssl/ui/fusion/hud/hud_layout/ui_hud_pve_view.sso`
  - `UiEnhancedTrackerPanelView = "enhanced_ui_panel_attach"`
  - `childs.enhanced_ui_panel_attach = UiFusionContainer` (empty attach‑only container at the desired position).
- Widget spawn (PVE): `mods_source/ssl/ui/fusion/hud/hud_layout/code/pve/ui_pve_screen.sso`
  - `EnhancedTrackerPanel = { providerDesc { __type = UiEnhancedTrackerDataProvider }, __type = UiEnhancedTrackerWidget }`.
- Widget + View assets (mod):
  - `ui_enhanced_tracker_widget.sso` (`assetLink = "Hud.EnhancedTrackerPanel"`).
  - `ui_enhanced_tracker_panel_view.sso` (the visual tile: frame, icon, timer text, label).

## Runtime Data Flow

```mermaid
sequenceDiagram
  participant Prov as UiEnhancedTrackerDataProvider
  participant Widg as UiEnhancedTrackerWidget
  participant View as UiEnhancedTrackerPanelView
  participant HUD as HUD Layout Attach

  Note over HUD: enhanced_ui_panel_attach container exists
  Widg->>HUD: Instantiate View into attach point
  Widg->>Prov: Start (subscribe/tick)
  loop every tickIntervalMs
    Prov->>Prov: remainingMs = max(remainingMs - tickIntervalMs, 0)
    Prov-->>Widg: Publish computed fields (timerText, remainingMs)
    Widg-->>View: Apply data to bound fields (future binding)
  end
```

Note: The current view is static; future binding will map provider fields to the `timer_text` and `label` when we integrate a small binding step or reuse an engine class that reads provider output.

## Provider Stub

Config file: `mods_source/enhanced_ui/ssl/ui/fusion/hud/enhanced_tracker/code/ui_enhanced_tracker_data_provider.sso`

- Purpose: Provide a minimal, self‑contained countdown entry used by the widget.
- Shape (current):
  - `entry.id = "restock"`
  - `entry.label = "Restock"`
  - `entry.totalMs = 60000` and `startRemainingMs = 60000`
  - `tickIntervalMs = 1000`
  - `__type = "UiEnhancedTrackerDataProviderBase"`

Widget hookup (currently disabled during investigation): normally lives in `ui_pve_screen.sso` as
```
EnhancedTrackerPanel = {
  providerDesc = { type = { __type = "UiEnhancedTrackerDataProvider" }, __type = "SslDesc" }
  __type = "UiEnhancedTrackerWidget"
}
```

### How the Stub Should Work
- On widget init, the provider starts with `remainingMs = startRemainingMs`.
- Every `tickIntervalMs`, it decrements remaining (floor at 0) and computes a `timerText` (e.g., `"60.0" → "59.0" ...`).
- The widget applies `timerText` to the view’s `timer_text` field and keeps `label` fixed. When `remainingMs == 0`, the tile can enter a “ready” state (future animation or glow).

### Current Limitations and Next Bindings
- The current view uses generic elements (`UiFusionContainer`, `UiFusionTextfield`). Without a binding step, text won’t change yet.
- Next iteration will add a small data‑binding:
  - Option A: Add a binding bridge similar to `UiWatermarkDataProvider` pattern (view exposes `timerTextfield` path; provider writes text).
  - Option B: Replace `timer_text` with an existing engine timer UI class used elsewhere (if available) that reads provider values.

### Validation
- Build and run. No errors should appear; the panel spawns and shows the static tile.
- Logs (if available) should show the provider active. Visual change will come after the binding step.

## Current State (2025-10-12)

- Enhanced Tracker wiring to engine systems remains disabled while we debug, but the panel’s visuals are now inlined directly inside `ui_hud_pve_view.sso` as `childs.enhanced_ui_panel` (static tile only).

- No custom attach mappings / asset holders / widgets are active. `ui_asset_storage.sso` and `ui_pve_screen.sso` stay untouched from vanilla; we override only `ui_hud_pve_view.sso` to host the static container.

- Latest `.pak` continues to ship just `ssl/ui/fusion/hud/hud_layout/ui_hud_pve_view.sso`, now containing the inline panel. Tracker-specific view/widget/provider files remain in `mods_source/` but are not packaged.

- Next step after validating mission stability with this static panel: experiment with lightweight data binding (e.g., manual timer text updates) before re-introducing asset holder/widget wiring.

- Reference screenshot: `docs/screenshots/progress/2025-10-12_static_panel.png` (static tile inline over vanilla HUD).
