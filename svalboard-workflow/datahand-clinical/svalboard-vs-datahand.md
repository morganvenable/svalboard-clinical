# Svalboard vs. DataHand: What Changed and Why It Matters

## DataHand Established the Category

The DataHand (debuted 1993, DataHand Systems, Inc., Phoenix, AZ) created the
finger-well keyboard category. Its clinical foundations are real and documented:

- **71% pain reduction** over 3.3 months (Kaiser & Koeneman, Harrington Arthritis
  Research Center, presented at RESNA 1994)
- **Typing force reduced to ~20% of flat keyboard levels** (Knight, Koeneman,
  Ferrell)
- **Fatigue resistance** over 6+ hour sessions, with 10-12% throughput advantage
  by end of day (Fernandez, Stanford)
- **Productivity at 116% of flat keyboard speeds** within 30 days across 33
  workers at 5 corporate sites
- **96.8% user satisfaction** with 94% of users reporting reduced wrist stress
  (University of Arizona, 1998)
- **~60% of surveyed users reported they could not work without it**

This evidence base is detailed in the companion document `digest.md`. The
clinical findings are not just marketing claims; the Harrington pain study was
peer-reviewed and presented at a RESNA conference.

The core ergonomic principles DataHand established remain valid:

1. Fingers rest in wells; keys activated by directional micro-movements
2. Hands fully supported; wrists in neutral posture
3. Minimal finger travel distance (~1/2 inch vs. inches on flat keyboards)
4. Low activation force (18-24 grams vs. 55-100 grams conventional)
5. Directional key distribution (20% per direction vs. 100% downward)
6. Integrated pointing, eliminating keyboard-mouse transitions

These principles are the foundation. Svalboard preserves every one of them
while addressing the limitations that prevented DataHand from serving all users.

---

## What DataHand Got Wrong

### Fit: Too Large for Many Users

The DataHand used a gantry-and-knob adjustment system. While it offered some
customization, the minimum achievable fit was still large. The finger wells
were sized for a particular hand geometry, and users with small hands found:

- **Excessive splay**: The spacing between finger wells forced the hand into
  more abduction than comfortable, stretching tendons and increasing the very
  strain the device was designed to reduce
- **Too much movement within the well**: With a small fingertip in an
  oversized well, the finger had to travel farther to reach the directional
  keys, partially negating the travel-reduction benefit
- **Exclusion of the small end of the bell curve**: DataHand's user base
  skewed toward larger-handed males, partly due to the programmer demographic
  of the era, but also because the hardware simply did not accommodate small
  hands well

The DataHand had adjustable finger well heights and some forward/backward
positioning via side knobs and dials. But these adjustments operated within
a physical geometry that assumed a particular hand size range. There was no
way to meaningfully change the splay between wells, the depth of the wells
relative to fingertip size, or the angular orientation of individual clusters
to match how a specific finger actually moves.

### Mechanical Switches

DataHand used mechanical key switches. These were light for their era but
still imposed fixed force profiles. There was no per-key force tuning. The
force curve increased with displacement (spring-based), meaning the user
fought increasing resistance throughout the keystroke.

### Fixed Geometry for a Non-Fixed Problem

Every human hand has a different shape. The physical structure and angles of
the fingers are distinct from the axes on which they actually move. A ring
finger's resting angle is not the same as its movement axis. An index finger
with an old fracture sits differently than one without. A hand with
Dupuytren's contracture at one MCP joint needs a completely different cluster
geometry for that finger than for the others.

DataHand's adjustment system could not address this level of individual
variation.

---

## What Svalboard Brings

### Extreme Anatomical Customizability

Svalboard provides continuous adjustment across multiple axes for every
key cluster and the palmrest, achieving millimeter and sub-degree fit
precision. This is not marketing language; it describes the mechanical
reality of the adjustment system.

#### Cluster Adjustment (5 axes per finger)

Each of the 10 finger/thumb clusters adjusts independently across:

| Axis | Direction | What It Controls |
|------|-----------|-----------------|
| **X** | East-west (lateral) | Splay between fingers; accommodates narrow or wide hand geometry |
| **Y** | North-south (toward/away from palm) | Finger length differences; ring vs. index vs. pinky reach |
| **Z** | Up-down (height) | Vertical position relative to palmrest; accommodates finger curl |
| **Roll** | Rotation around the Y axis | Tilts the cluster to match the natural resting angle of each finger |
| **Yaw** | Rotation around the Z axis | Angles the cluster to align with each finger's actual movement axis, which differs from its structural angle |

All five axes are continuously adjustable. There are no detents, no preset
positions, no "size S/M/L" steps. The cluster can be set to literally any
position and angle within its mechanical range, then locked with standard
screws. A 2.5mm hex wrench is the only tool needed.

#### Palmrest Adjustment (3 axes + height)

The palmrest carrier moves in X, Y, and yaw, plus vertical adjustment. Palm
rests are 3D-printed from PLA and can be thermoformed with a heat gun for a
custom contour matching the user's actual palm shape.

#### Fingertip Sizing

Key petals ship in three widths: 14mm, 16mm, and 18mm, measured at 6mm from
the fingertip. Users measure their own fingertips to select the right size,
and different fingers can use different sizes on the same board.

#### Tenting

6-15 degrees of tenting adjustment is inherent to the design. Beyond that
range, the Svalboard supports M5 legs, 3D-printed fixed tents at any angle,
and standard 1/4-20 camera tripod hardware. Users have mounted Svalboards on
chair arms, standing desk surfaces, and articulating monitor arms.

### Hand Size Range

| Measurement | DataHand | Svalboard |
|-------------|----------|-----------|
| Minimum palm width | ~70mm+ (practical limit) | ~60mm (documented users) |
| Minimum hand length | Not well documented; large hands only | ~140mm (documented users) |
| Maximum hand size | Accommodated | Accommodated |
| Splay reduction vs. DataHand | (baseline) | ~10mm (Lightly); ~19mm (Narrow prototype) |

Svalboard Lightly reduced splay by about 10mm across the fingertips
compared to the original Svalboard geometry (which was already smaller than
DataHand). The Narrow prototype demonstrated an additional ~9mm reduction.
Women with palm widths around 60mm and hand lengths around 140mm are using
Svalboards successfully, a population that was effectively excluded from
DataHand.

### Posture Flexibility

Because cluster position and angle are continuously adjustable, the Svalboard
accommodates different preferred postures:

- **Extended posture**: Fingers relatively straight, similar to DataHand's
  design assumption
- **Curled posture**: Fingers more curled, with clusters adjusted inward and
  at different heights to match the curled resting position. This is
  particularly relevant for users who find a curled posture more natural or
  who have conditions (contractures, arthritis) that prevent full extension.

This is not possible on DataHand, where the finger well geometry assumes a
particular finger extension.

### Per-Key Force Tuning

Svalboard uses optical sensing with magnetic actuation rather than mechanical
switches. The force profile follows an inverse-square curve: a crisp
breakaway at ~20 grams, then force drops precipitously. Total mechanical work
per keystroke is approximately 90% lower than conventional switches.

The offset between magnets can be adjusted during 3D printing to set
per-key force. The product ships with direction-specific force tuning
already applied: North keys (extension) are set to approximately 12 gf
to reduce load on the extensor tendons, while other directions use ~20 gf.
Force can be tuned further down to 8-10 gf for users with weakness or
pain sensitivity. Force is set by the key itself, and swapping keys is a
no-tool operation, so force can be tuned per-finger and per-direction,
then adjusted as clinical needs change.

This matters for users with muscular atrophy, who benefit dramatically
from customizing forces to their weaker fingers and to overall weakness.
But even users without specific pathology may prefer lighter forces on
certain directions or certain fingers. The per-key tunability is an
option, not a requirement.

DataHand's 18-24 gf specification was fixed across all keys and all
directions.

### Integrated Pointing

Both DataHand and Svalboard integrate pointing to eliminate the
keyboard-mouse transition. DataHand used index-finger directional control
with thumb activation. Svalboard integrates a Trackpoint and/or trackball
directly into the hand unit, operable without removing fingers from their
wells.

### Modern Firmware

DataHand had limited remapping capability (Professional model only, at extra
cost). Svalboard runs QMK firmware with full programmability: layers, macros,
tap-dance, leader keys, and real-time configuration via the keybard-ng web
editor. Every key can be anything on any layer.

### Open and Repairable

Apart from the circuitry and magnets, everything on a Svalboard is
3D-printed to open schematics and held together with standard screws. Any
part that wears or breaks can be reprinted and replaced. DataHand parts
became unobtainable after the company ceased production.

---

## Summary: What Transferred and What Improved

| Dimension | DataHand (1993) | Svalboard (2024) |
|-----------|----------------|-----------------|
| **Core paradigm** | Finger-well, 5-directional keys | Same (preserved) |
| **Clinical evidence** | Harrington pain study, Stanford fatigue study, productivity meta-study | Inherits paradigm evidence; same mechanisms apply |
| **Activation force** | 18-24 gf (fixed, all directions) | ~20 gf default; North keys ~12 gf (ships this way); tunable to 8-10 gf per key per direction |
| **Force profile** | Spring-based (increasing with displacement) | Magnetic breakaway (inverse-square drop) |
| **Total work per keystroke** | Lower than conventional | ~90% lower than conventional |
| **Cluster adjustment** | Gantry + knobs; limited range | 5-axis continuous (X/Y/Z/Roll/Yaw) per cluster |
| **Palmrest** | Fixed geometry | 3-axis + height, thermoformable PLA |
| **Minimum hand size** | ~70mm+ palm width | ~60mm palm width, ~140mm hand length |
| **Splay** | Fixed (too wide for small hands) | Continuously adjustable; 10-19mm reduction |
| **Posture options** | Extended only | Extended or curled, continuously adjustable |
| **Fingertip sizing** | One size | 14/16/18mm widths, per-finger |
| **Sensing** | Mechanical switches | Optical |
| **Pointing** | Index-finger directional | Integrated Trackpoint/trackball |
| **Firmware** | Limited remap (Pro model) | Full QMK: layers, macros, tap-dance, real-time config |
| **Repairability** | Proprietary, now unobtainable | Open schematics, 3D-printable, standard screws |
| **Tenting** | Limited built-in | 6-15 degrees inherent + arbitrary via hardware |
