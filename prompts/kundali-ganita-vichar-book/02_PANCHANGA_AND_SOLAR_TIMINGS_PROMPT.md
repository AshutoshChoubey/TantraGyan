# 📜 Prompt 02: Panchanga & Solar Timings Mathematical Specifications
## Source Engine: `02_PANCHANGA_AND_SOLAR_TIMINGS.md`

---

## 1. Mathematical Formulas to Demystify
1. **Tithi (Lunar Phase):**
   $$\theta_{\text{tithi}} = (\lambda_{\text{Moon}} - \lambda_{\text{Sun}}) \pmod{360^\circ}$$
   $$\text{Tithi Index} = \lfloor \theta_{\text{tithi}} / 12^\circ \rfloor + 1 \in \{1, \dots, 30\}$$
2. **Vaara (Solar Weekday):**
   Determined from local sunrise to sunrise, governed by the 7 classical lords (Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn).
3. **Nakshatra (Lunar Mansion):**
   $$\text{Nakshatra Index} = \lfloor \lambda_{\text{Moon}} / 13^\circ 20' \rfloor \in \{0, \dots, 26\}$$
   $$\text{Pada Index} = \lfloor (\lambda_{\text{Moon}} \pmod{13^\circ 20'}) / 3^\circ 20' \rfloor + 1 \in \{1, 2, 3, 4\}$$
4. **Yoga (Solilunar Sum):**
   $$\text{Yoga Index} = \lfloor (\lambda_{\text{Sun}} + \lambda_{\text{Moon}}) / 13^\circ 20' \rfloor + 1 \in \{1, \dots, 27\}$$
5. **Karana (Half-Tithi):**
   $$\text{Karana Index} = \lfloor \theta_{\text{tithi}} / 6^\circ \rfloor + 1 \in \{1, \dots, 60\}$$
   (4 Fixed Karanas: Shakuni, Chatushpada, Naga, Kintughna; 7 Repeating Karanas: Bava, Balava, Kaulava, Taitila, Gara, Vanija, Vishti/Bhadra).
6. **Inauspicious Muhurta Windows (Rahu Kalam & Yamaghanta):**
   Dividing the daytime (Sunrise to Sunset) into 8 equal portions ($D / 8$):
   - Rahu Kalam: Mon (2nd), Sat (3rd), Fri (4th), Wed (5th), Thu (6th), Tue (7th), Sun (8th).
7. **11 Upagraha Points:**
   Gulika and Mandi (Saturn's dark sons), Yamakantaka (Jupiter), Ardhyama (Mercury), Kala (Sun), etc.

---

## 2. Layman Storytelling Script (How to Explain)
- **The Parable of the 5 Cosmic Hands:**
  Imagine Time as a living celestial deity with 5 fingers:
  1. *Tithi* (The breath/phase of the Moon, dictating emotional relationships and prosperity).
  2. *Vaara* (The physical energy of the Sun, dictating vitality and health).
  3. *Nakshatra* (The inner mind and karmic memory of the Moon).
  4. *Yoga* (The synthesis of spirit and mind, Sun + Moon).
  5. *Karana* (The physical action and execution power).
- **Point-to-Point Steps:**
  - Why is Tithi 12 degrees? Because the Moon runs faster than the Sun; every time the Moon pulls 12 degrees ahead, one lunar day is born!
  - What happens during Vishti (Bhadra) Karana? Why do ancient texts advise pausing major financial celebrations during Bhadra?
  - Step-by-step calculation for Benchmark Native 'Alpha' (जातक 'क'): Moon at $103.17^\circ$, Sun at $190.48^\circ \implies \theta = 272.70^\circ \implies$ Krishna Ashtami (Jaya Tithi, ruled by Shiva/Rudra).

---

## 3. Required Output Artifacts
- Step-by-step arithmetic equations rendered in clean markdown.
- Visual diagram of the 5 limbs connecting the Sun and Moon.
- Reference table of 27 Yogas and 11 Karanas with their practical karmic impacts.
