# 📜 Prompt 01: Astronomical Ephemeris, Lagna Geometry & Planetary Dignities
## Source Engine: `01_JANM_KUNDLI_EPHEMERIS_CALCULATIONS.md`

---

## 1. Mathematical Formulas to Demystify
1. **Local Time to Universal Time (UT):**
   $$\text{UT Hour} = \text{Local Hour} - \text{TZ Offset}$$
2. **Astronomical Julian Day Number ($JD_{\text{UT}}$):**
   $$JD = \lfloor 365.25 \times (Y + 4716) \rfloor + \lfloor 30.6001 \times (M + 1) \rfloor + D + \frac{UT}{24} + B - 1524.5$$
3. **Chitrapaksha / Lahiri Ayanamsha ($\Delta\psi$):**
   $$\lambda_{\text{Sidereal}} = \lambda_{\text{Tropical}} - \Delta\psi_{\text{Lahiri}} \pmod{360^\circ}$$
4. **Ascendant (Lagna) & Local Sidereal Time ($LST$):**
   $$LST = GMST + \frac{\text{Longitude}}{15^\circ}$$
   $$\tan(\lambda_{\text{Asc}}) = \frac{-\cos(RAMC)}{\sin(RAMC)\cos(\epsilon) + \tan(\phi)\sin(\epsilon)}$$
5. **Combustion Orbs (Asta):**
   Moon ($12^\circ$), Mars ($17^\circ$), Mercury ($14^\circ$ direct, $12^\circ$ retrograde), Jupiter ($11^\circ$), Venus ($10^\circ$ direct, $8^\circ$ retrograde), Saturn ($15^\circ$).
6. **5-Fold Friendship (Panchadha Maitri):**
   $$\text{Compound Relationship} = \text{Natural (Naisargika)} + \text{Temporal (Tatkalika)}$$
   - Mitra + Mitra = Adhi Mitra (Great Friend, +2)
   - Mitra + Sama = Mitra (Friend, +1)
   - Shatru + Shatru = Adhi Shatru (Great Enemy, -2)
7. **Planetary States (Avasthas):**
   - Baladi (Infant $0-6^\circ$, Youth $6-12^\circ$, Adolescent $12-18^\circ$, Old $18-24^\circ$, Dead $24-30^\circ$)
   - Jagradadi (Awake, Dreaming, Sleeping)
   - Diptadi (Exalted = Deepta, Moolatrikona = Dina, Swakshetra = Swastha, Debilitated = Vikal)

---

## 2. Layman Storytelling Script (How to Explain)
- **The Parable of the Celestial Clock & Traveler:**
  Explain the Earth as a rotating carousel under a cosmic sky dome. Greenwich is one mark, but where you were born is your unique window into the sky. Local standard time is just a human convention for railways and offices; the cosmos only cares about the true angle of the Sun and stars at that exact geographic longitude!
- **Point-to-Point Steps:**
  1. What is Julian Day? Simply counting every single day continuously since 4713 BCE so astronomers never get confused by leap years and changing calendars!
  2. What is Ayanamsha? The slow, gentle wobble of Earth's axis (precession) like a spinning top, slipping roughly $1^\circ$ every 72 years.
  3. What is Lagna? The exact eastern zodiac sign rising on the horizon at the first breath of life—the lens through which the native views the universe.
  4. Worked calculations using Native Ashutosh ($JD = 2449653.427$, Lahiri $= 23^\circ 47'$, Virgo Lagna at $09^\circ 21'$ Uttara Phalguni Pada 4).

---

## 3. Required Output Artifacts
- Plain language text explaining each formula with zero mathematical terror.
- Clean comparison table of Combustion orbs and Panchadha Maitri scoring.
- High-contrast SVG diagram illustrating the eastern horizon (Lagna) intersecting the 360° ecliptic wheel.
