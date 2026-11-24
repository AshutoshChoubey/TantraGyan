"""
Formula Simplifier Agent (Google Antigravity SDK Pattern)
Translates dense astronomical formulas and equations into step-by-step layman arithmetic.
"""

from typing import Dict, Any, List


class FormulaSimplifierAgent:
    """Agent that translates complex astronomical & astrological equations into plain arithmetic."""

    def __init__(self):
        pass

    def simplify_tithi(self, moon_deg: float, sun_deg: float) -> Dict[str, Any]:
        """Explains Tithi calculation step-by-step."""
        diff = (moon_deg - sun_deg) % 360.0
        tithi_index = int(diff // 12.0) + 1
        paksha = "Shukla Paksha (Waxing)" if tithi_index <= 15 else "Krishna Paksha (Waning)"
        adjusted_tithi = tithi_index if tithi_index <= 15 else tithi_index - 15
        elapsed_pct = round(((diff % 12.0) / 12.0) * 100, 2)

        return {
            "formula_name": "Tithi (तिथी गणना)",
            "plain_explanation": "चंद्रमा और सूर्य के बीच की कोणीय दूरी को 12 से भाग देकर प्राप्त संख्या ही तिथि है।",
            "step_1": f"चंद्रमा का भोगांश ({moon_deg}°) - सूर्य का भोगांश ({sun_deg}°) = {round(diff, 4)}°",
            "step_2": f"कुल अंतर ({round(diff, 4)}°) को 12° से भाग दें = {round(diff / 12.0, 4)}",
            "step_3": f"पूर्णांक में 1 जोड़ें = {tithi_index}",
            "result_tithi": f"{paksha} की {adjusted_tithi}वीं तिथि",
            "elapsed_percentage": f"{elapsed_pct}%",
        }

    def simplify_dasha_balance(self, moon_nak_deg: float, nak_span: float = 13.3333, total_years: int = 19) -> Dict[str, Any]:
        """Explains Dasha balance at birth."""
        elapsed = moon_nak_deg
        remaining = nak_span - elapsed
        rem_fraction = remaining / nak_span
        balance_years = rem_fraction * total_years
        years = int(balance_years)
        months = int((balance_years - years) * 12)
        days = int((((balance_years - years) * 12) - months) * 30.4375)

        return {
            "formula_name": "Balance of Dasha at Birth (जन्म समय दशा भोग्य शेष)",
            "plain_explanation": "जिस नक्षत्र में जन्म हुआ, उसका जितना भाग अभी पार होना बाकी है, उसी अनुपात में दशा के वर्ष मिलते हैं।",
            "step_1": f"नक्षत्र में चंद्रमा की चली गई दूरी: {round(elapsed, 4)}° (कुल 13°20' = 13.3333° में से)",
            "step_2": f"शेष बची दूरी: 13.3333° - {round(elapsed, 4)}° = {round(remaining, 4)}°",
            "step_3": f"शेष अनुपात: {round(remaining, 4)} / 13.3333 = {round(rem_fraction * 100, 2)}%",
            "step_4": f"कुल महादशा वर्ष ({total_years}) × {round(rem_fraction, 4)} = {round(balance_years, 2)} वर्ष",
            "result_balance": f"{years} वर्ष, {months} माह, {days} दिन",
        }

    def simplify_ashtakavarga_average(self, total_bindus: int = 337, total_houses: int = 12) -> Dict[str, Any]:
        """Explains the 337 bindus distribution rule."""
        avg = total_bindus / total_houses
        return {
            "formula_name": "Ashtakavarga Benchmark Rule (अष्टकवर्ग 28 बिंदु स्वर्ण-नियम)",
            "plain_explanation": "337 शुभ बिंदुओं को 12 भावों में बांटने पर प्रति भाव औसत 28 बिंदु आते हैं।",
            "step_1": "337 कुल बिंदु ÷ 12 भाव = 28.08 बिंदु (लगभग 28)",
            "rule_auspicious": "28 या उससे अधिक बिंदु: वह भाव जीवन में सहज सफलता और प्रचुर लाभ देता है।",
            "rule_moderate": "25 से 27 बिंदु: सामान्य फल, प्रयास के अनुपात में फल।",
            "rule_challenging": "24 या उससे कम बिंदु: उस भाव से संबंधित कार्यों में अधिक श्रम और सावधानी आवश्यक।",
        }
