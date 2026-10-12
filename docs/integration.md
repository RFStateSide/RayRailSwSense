# Electrical Interface and Integration

J1 is the DC input terminal. F1 feeds the U1 supply tab (pad 9).
U1 pins 5–8 feed J2, the switched output. The design uses a common ground;
it is not a galvanically isolated switch or measurement interface.

## Six-Pin J3

Pin numbers below are KiCad pad numbers. Check the connector's physical
orientation against the PCB; do not infer it from a cable's viewing direction.

| Pin | Function | Circuit |
|---|---|---|
| 1 | Raw switched Vout | Direct connection to J2; not an ADC-level signal |
| 2 | Divided Vout | R5 = 82 kΩ, R6 = 4.7 kΩ |
| 3 | External 3.3 V input | FB1 feeds the local rail and R2 = 4.7 kΩ to DEN |
| 4 | Switch control | R1 = 4.7 kΩ to U1 IN; active high |
| 5 | Current/diagnostic sense | IS/R4 node through R3 = 4.7 kΩ; C2 = 10 nF to ground |
| 6 | Ground | Measurement and logic return |

The 3.3 V input supplies the diagnosis-enable network; it is not an onboard
regulated output. DEN is enabled from that rail rather than independently
controlled through J3. Use the manufacturer's IN/DEN timing and fault-reset
requirements in the host controller.

## Saved RaySspaController Revisions

The inspected controller PCB's J4–J7 connectors assign pin 1 to voltage sense,
pin 2 to +12 V, and pins 3–6 to 3.3 V, switch control, current sense and ground.
This differs materially from this board's J3 pins 1 and 2.

**Do not connect a straight-through six-wire cable.** For that saved interface,
a candidate signal mapping is rail J3-2 to controller voltage-sense pin 1,
J3-3/4/5/6 to matching controller functions, with controller +12 V pin 2 and
rail raw-output pin 1 kept out of the signal cable. Confirm receiver circuitry,
grounding and voltage ranges for the actual controller revision before use.
This map is not a reconstruction of the historical tested harness.

## Calculated Scaling

For a high-impedance receiver, V(J3-2) ≈ Vout × 4.7/(82 + 4.7).
The nominal divisor is 18.4468; at 32 V, the divided output is about 1.735 V.
This measures switched output voltage, not unswitched input voltage.

With R4 = 2 kΩ, V(IS) ≈ Iload × 2000/k, before device offset and receiver loading:

| Device | Typical differential sense ratio k | Nominal slope |
|---|---:|---:|
| BTH500301LUAAUMA1 | 34,000 | 58.8 mV/A |
| BTH500151LUAAUMA1 | 52,000 | 38.5 mV/A |

The earlier 200 Ω record would give one-tenth these slopes and does not describe
the confirmed assembly. Use calibration for the actual device, resistor,
temperature and ADC path; these values are calculations, not measured results.
The retained controller firmware supports slope/offset calibration, but no
portable historical calibration dataset accompanies this hardware release.

## Diagnostics and Protection Boundaries

IS carries diagnosis as well as load-current information. For the BTH50030,
the specified fault current can reach 5.2 mA under its stated conditions:
2 kΩ would correspond to 10.4 V before compliance/loading effects. J3-5 is
therefore not a universally bounded 0–3.3 V output. R3 limits current but does
not clamp voltage. The receiving circuit must provide suitable input protection
and distinguish faults from normal measurements.

The switch's integrated protection is conditional and does not establish
complete-system protection. Respect polarity, wiring, source energy, inductive
loads and retry behavior. Do not treat the off state as safety isolation.
See [known limitations](known-limitations.md).

Sources: [BTH50030 datasheet](https://www.infineon.com/assets/row/public/documents/10/49/infineon-bth50030-1lua-datasheet-en.pdf),
[BTH50015 datasheet](https://www.infineon.com/assets/row/public/documents/10/49/infineon-bth50015-1lua-datasheet-en.pdf).
