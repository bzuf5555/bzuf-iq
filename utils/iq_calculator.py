# OPUS Agent: psixometrik standartlarga asoslangan IQ hisoblash
# Mean=100, SD=15 standart taqsimot modeli

from data.questions import MAX_POINTS


IQ_LABELS: list[tuple[int, str, str]] = [
    (145, "🏆 Daho darajasi",        "Siz nadir iqtidor sohibisiz! Dunyodagi eng yuqori intellekt darajasiga egasiz."),
    (130, "🥇 Juda yuqori intellekt", "Siz aqliy jihatdan o'ta rivojlangansiz. Ilmiy yoki ijodiy sohalarda zo'r natijalarga erisha olasiz."),
    (120, "🥈 Yuqori intellekt",      "Intellektingiz o'rtachadan ancha yuqori. Murakkab muammolarni osonlik bilan hal qila olasiz."),
    (110, "🥉 O'rtachadan yuqori",    "Intellektingiz o'rtachadan yuqori. Yangi narsalarni tez o'zlashtirasiz."),
    (100, "✅ O'rtacha intellekt",    "Siz normal intellekt darajasiga egasiz — dunyodagi ko'pchilik odamlar darajasida."),
    (90,  "📊 O'rtachadan past",      "Intellektingiz o'rtachadan biroz past, lekin harakatlar bilan rivojlantirishingiz mumkin."),
    (80,  "📉 Past o'rtacha",         "Muayyan sohalarda ko'proq mashq qilish tavsiya etiladi."),
    (0,   "📋 Chegaraviy",           "Muntazam aqliy mashqlar va o'qish orqali ko'rsatkichni oshirish mumkin."),
]


def calculate_iq(earned_points: int, time_seconds: int) -> tuple[int, str, str]:
    """
    Psixometrik formula:
      raw_ratio  = earned / max  (0.0–1.0)
      z_score    = (raw_ratio - 0.5) * 4  (taxminan -2 dan +2 gacha)
      iq         = 100 + 15 * z_score     (70 – 130 yadro diapazon)
      time_bonus = tezroq = +1..+5 xol
    """
    raw_ratio = earned_points / MAX_POINTS
    z_score = (raw_ratio - 0.5) * 4.0
    base_iq = 100 + (15 * z_score)

    # Vaqt bonusi: 20 ta savol uchun o'rtacha ideal vaqt ~25 sek/savol
    avg_per_question = time_seconds / 20
    if avg_per_question < 10:
        time_bonus = 5
    elif avg_per_question < 20:
        time_bonus = 3
    elif avg_per_question < 30:
        time_bonus = 1
    else:
        time_bonus = 0

    iq = int(round(base_iq + time_bonus))
    iq = max(65, min(145, iq))

    for threshold, label, desc in IQ_LABELS:
        if iq >= threshold:
            return iq, label, desc

    return iq, "📋 Chegaraviy", IQ_LABELS[-1][2]


def iq_percentile(iq: int) -> int:
    """Taxminiy foizlik daraja."""
    table = {
        145: 99, 130: 98, 125: 95, 120: 91, 115: 84,
        110: 75, 105: 63, 100: 50, 95: 37, 90: 25,
        85: 16, 80: 9, 75: 5, 70: 2, 65: 1,
    }
    for threshold, pct in sorted(table.items(), reverse=True):
        if iq >= threshold:
            return pct
    return 1


def progress_bar(current: int, total: int) -> str:
    filled = int((current / total) * 10)
    return "▓" * filled + "░" * (10 - filled)
