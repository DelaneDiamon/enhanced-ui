# Ability Cooldown Research

This document summarizes player-facing abilities and equipment exposing cooldown or duration signals for HUD tracking. Entries list icon mapping, resource model, controller hooks, and open questions.

## Class Abilities

### `ability_auspex_scan`
- Icon(s): `auspex` / chaos `auspex_chaos`
- Slot: `ULTIMATE`
- Resource model: settingsType=CHARGES; maxCharges=1.0; startingCharges=1.0; recoverSpeed=1.1; ticksPerSec=20.0; regenDelay=1.0; regenType=TimerRegen
- Controller: `ability_controller_desc_auspex_scan.sso` (type `AbilityControllerDescAuspexScan`)
- Exposed events: n/a
- Energy subscription: No; OnMinEnergy callback: No

### `ability_banner_ultramar`
- Icon(s): `banner` / chaos `banner_chaos`
- Slot: `ULTIMATE`
- Resource model: settingsType=CHARGES; maxCharges=1.0; startingCharges=1.0; recoverSpeed=0.8; ticksPerSec=20.0; regenDelay=1.0; regenType=TimerRegen
- Controller: `ability_controller_desc_banner_ultramar.sso` (type `AbilityControllerDescBannerUltramar`)
- Exposed events: n/a
- Energy subscription: No; OnMinEnergy callback: No

### `ability_barrier`
- Icon(s): `barrier` / chaos `barrier_chaos`
- Slot: `ULTIMATE`
- Resource model: settingsType=PERCENT; maxCharges=1.0; startingCharges=1.0; activationThreshold=100.0; recoverSpeed=1.5; ticksPerSec=20.0; regenDelay=1.0; energyDrainRate=6.7; regenType=TimerRegen
- Controller: `ability_controller_desc_barrier.sso` (type `AbilityControllerDescBarrier`)
- Exposed events: broken, created
- Energy subscription: Yes; OnMinEnergy callback: Yes

### `ability_camouflage`
- Icon(s): `camo_cloak` / chaos `camo_cloak_chaos`
- Slot: `ULTIMATE`
- Resource model: activationThreshold=100.0; recoverSpeed=0.8; ticksPerSec=20.0; regenDelay=1.0; energyDrainRate=10.0; regenType=TimerRegen
- Controller: `ability_controller_desc_camouflage.sso` (type `AbilityControllerDescCamouflage`)
- Exposed events: IndicateEnding, remove_camouflage_status_effect
- Energy subscription: Yes; OnMinEnergy callback: Yes

### `ability_grappling_hook`
- Icon(s): `grapnel_launcher` / chaos `grapnel_launcher_chaos`
- Slot: `ULTIMATE`
- Resource model: settingsType=CHARGES; recoverSpeed=1.1; ticksPerSec=20.0; regenDelay=1.0; regenType=TimerRegen
- Controller: `ability_controller_desc_grappling_hook.sso` (type `AbilityControllerDescGrapplingHook`)
- Exposed events: hook_attack, hook_damage, hook_flight_start, hook_stuck, launch_success
- Energy subscription: No; OnMinEnergy callback: No

### `ability_jetpack`
- Icon(s): `jet_pack` / chaos `jet_pack_chaos`
- Slot: `ULTIMATE`
- Resource model: settingsType=CHARGES; recoverSpeed=30.0; ticksPerSec=20.0; regenDelay=1.0; regenType=TimerRegen
- Controller: `ability_controller_desc_jetpack.sso` (type `AbilityControllerDescJetpack`)
- Exposed events: air_dash_finished, rushing_ready
- Energy subscription: No; OnMinEnergy callback: No

### `ability_jetpack_pve`
- Icon(s): `jet_pack` / chaos `jet_pack_chaos`
- Slot: `ULTIMATE`
- Resource model: settingsType=CHARGES; recoverSpeed=1.23; ticksPerSec=20.0; regenDelay=0.0; regenType=TimerRegen
- Controller: `ability_controller_desc_jetpack_pve.sso` (type `AbilityControllerDescJetpackPve`)
- Exposed events: finish_ability, max_rushing_charge, rushing_ready
- Energy subscription: No; OnMinEnergy callback: No

### `ability_pc_helbrute_healing`
- Icon(s): `hellbrute_ability_icon` / chaos `hellbrute_ability_icon`
- Slot: `ULTIMATE`
- Resource model: settingsType=CHARGES; maxCharges=1.0; startingCharges=0.0; recoverSpeed=1.2; regenType=TimerRegen
- Controller: not mapped (likely NPC-only or handled elsewhere)
- Exposed events: n/a
- Energy subscription: No; OnMinEnergy callback: No

### `ability_rage`
- Icon(s): `rage_mode`
- Slot: `ULTIMATE`
- Resource model: activationThreshold=100.0; recoverSpeed=0.25; ticksPerSec=60.0; regenDelay=1.0; energyDrainRate=10.0; regenType=TimerRegen
- Controller: `ability_controller_desc_rage.sso` (type `AbilityControllerDescRage`)
- Exposed events: TimeWarping
- Energy subscription: Yes; OnMinEnergy callback: Yes

### `ability_threatening_battle_cry`
- Icon(s): `battle_cry` / chaos `battle_cry`
- Slot: `ULTIMATE`
- Resource model: settingsType=CHARGES; maxCharges=1.0; startingCharges=1.0; recoverSpeed=2.0; ticksPerSec=60.0; regenType=TimerRegen
- Controller: `ability_controller_desc_threatening_battle_cry.sso` (type `AbilityControllerDescThreateningBattleCry`)
- Exposed events: TimeWarping, ability_effect
- Energy subscription: No; OnMinEnergy callback: No

## Equipment & Consumables

### `equipment_buff_crate`
- Icon: `icon`
- Slot: `ROUTINE`
- Resource model: settingsType=CHARGES; maxCharges=1.0; startingCharges=1.0; regenType=CraftPoints
- Controller type: `AbilityControllerDescThrow`
- Events: n/a (inspect equipment panel logic)

### `equipment_combat_stimulants`
- Icon: `combat_stimulant`
- Slot: `NONE`
- Resource model: settingsType=CHARGES; startingCharges=2.0; regenType=CraftPoints
- Controller type: `AbilityControllerDescCombatStimulants`
- Events: n/a (inspect equipment panel logic)

### `equipment_frag_grenade`
- Icon: `frag_grenade`
- Slot: `ROUTINE`
- Resource model: settingsType=CHARGES; maxCharges=3.0; startingCharges=3.0; regenType=CraftPoints
- Controller type: `AbilityControllerDescAimedThrow`
- Events: n/a (inspect equipment panel logic)

### `equipment_healing_injector`
- Icon: `healing_injector`
- Slot: `INJECTOR`
- Resource model: settingsType=CHARGES; startingCharges=2.0; regenType=CraftPoints
- Controller type: `AbilityControllerDescHealingInjector`
- Events: n/a (inspect equipment panel logic)

### `equipment_krak_grenade`
- Icon: `krak_grenade`
- Slot: `ROUTINE`
- Resource model: settingsType=CHARGES; startingCharges=2.0; regenType=CraftPoints
- Controller type: `AbilityControllerDescAimedThrow`
- Events: n/a (inspect equipment panel logic)

### `equipment_melta_charge`
- Icon: `melta_charge`
- Slot: `ROUTINE`
- Resource model: settingsType=CHARGES; maxCharges=1.0; startingCharges=1.0; regenType=CraftPoints
- Controller type: `AbilityControllerDescThrowAndDetonate`
- Events: n/a (inspect equipment panel logic)

### `equipment_shock_grenade`
- Icon: `shock_grenade`
- Slot: `ROUTINE`
- Resource model: settingsType=CHARGES; startingCharges=2.0; regenType=CraftPoints
- Controller type: `AbilityControllerDescAimedThrow`
- Events: n/a (inspect equipment panel logic)

## HUD Integration Notes

### Equipment Panel
- `ui_equipment_panel_view.sso` instantiates `UiEquipmentSlot`/`UiEquipmentSubSlot` widgets, each bundling icon switchers, a `UiEquipmentCounter`, and pulse/zero-blink states tied to ability charge data.
- `ui_equipment_panel_data_provider.sso` simply enumerates the ability/equipment UIDs for each slot while inheriting behaviour from `UiEquipmentPanelDataProviderBase`; the engine supplies charge counts and cooldown readiness without extra scripting.
- `UiEquipmentSlot` exposes named children (`counter`, `pulse`, `icon`, etc.) that animate based on those provider updates, giving us a proven contract for showing charges and “last use” feedback.
- The same slot/provider pattern appears in other UI modules (e.g., scoreboard inventory), reinforcing that these contracts are reusable for a separate cooldown strip.

### Ultimate Ability Slot
- `ui_weapon_panel_view.sso` embeds `UiWeaponPanelAbilitySlot`, which wraps `UiUltimateImage`, `UiUltimateBar`, `UiUltimateCounter`, and `UiUltimateBlink` to show icon, radial fill, numeric value, and ready-state animations.
- `ui_weapon_panel_data_provider.sso` inherits from `UiWeaponPanelDataProviderBase`; this base feeds energy percentage, ready flags, and icon keys directly into the slot’s named bindings (`abilityIcon`, `abilityBar`, `counter`, `blink`).
- Because the ultimate slot already consumes the player’s ability resource through these components, we can mirror its structure to tap into the same data stream for any new HUD cooldown widget.
- Barrier/camouflage-specific events (e.g., `broken`, `IndicateEnding`) can layer on top by listening to ability custom events if we need supplementary visual states.
- The `*DataProviderBase` classes themselves are not defined in the unpacked SSL tree (likely engine-authored); we will rely on their exposed contracts rather than reimplementing resource fetch logic.

## Follow-Up Items

- Decide whether to subclass the existing slot widgets or build lightweight containers that replicate their required fields while keeping layout flexibility for the new cooldown row.
- Track down where `UiEquipmentPanelDataProviderBase` and `UiWeaponPanelDataProviderBase` pull their data (likely player HUD controllers) so a bespoke data provider can share the same interfaces.
- Determine if custom ability events (e.g., barrier `broken`, grappling `hook_flight_start`) require explicit routing into the new widget beyond what the base providers offer.
