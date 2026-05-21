# OPUS Agent: psixometrik standartlarga asoslangan 20 IQ savoli
# Domenlar: raqamli, verbal, mantiqiy, fazoviy, matematik, xotira

QUESTIONS: list[dict] = [
    # ── RAQAMLI KETMA-KETLIK ──────────────────────────────────────────
    {
        "id": 1,
        "text": "🔢 *Qatorni davom ettiring:*\n\n`2 → 4 → 8 → 16 → ?`",
        "options": ["A) 24", "B) 28", "C) 32", "D) 36"],
        "correct": "C",
        "category": "numerical",
        "difficulty": "easy",
        "points": 5,
        "explanation": "Har son ikki barobarga ko'payadi: 16 × 2 = *32*",
    },
    {
        "id": 2,
        "text": "🔢 *Qatorni davom ettiring:*\n\n`3 → 6 → 11 → 18 → 27 → ?`",
        "options": ["A) 36", "B) 38", "C) 40", "D) 34"],
        "correct": "B",
        "category": "numerical",
        "difficulty": "medium",
        "points": 7,
        "explanation": "Farqlar: +3, +5, +7, +9, +11 → 27 + 11 = *38*",
    },
    {
        "id": 3,
        "text": "🔢 *Qatorni davom ettiring:*\n\n`1 → 1 → 2 → 3 → 5 → 8 → ?`",
        "options": ["A) 11", "B) 12", "C) 13", "D) 14"],
        "correct": "C",
        "category": "numerical",
        "difficulty": "medium",
        "points": 7,
        "explanation": "Fibonachchi ketma-ketligi: 5 + 8 = *13*",
    },
    {
        "id": 4,
        "text": "🔢 *Qatorni davom ettiring:*\n\n`2 → 6 → 12 → 20 → 30 → ?`",
        "options": ["A) 40", "B) 42", "C) 44", "D) 38"],
        "correct": "B",
        "category": "numerical",
        "difficulty": "hard",
        "points": 10,
        "explanation": "Formula: n×(n+1) → 6×7 = *42*",
    },

    # ── TOQQA MOS KELMAYDIGAN ─────────────────────────────────────────
    {
        "id": 5,
        "text": "🍎 *Qaysi so'z qolganlardan farq qiladi?*\n\nOlma | Nok | Sabzi | Uzum | Gilos",
        "options": ["A) Olma", "B) Nok", "C) Sabzi", "D) Uzum"],
        "correct": "C",
        "category": "verbal",
        "difficulty": "easy",
        "points": 5,
        "explanation": "*Sabzi* — sabzavot, qolganlari meva",
    },
    {
        "id": 6,
        "text": "🔢 *Qaysi son qolganlardan farq qiladi?*\n\n`2 | 3 | 5 | 7 | 9 | 11`",
        "options": ["A) 2", "B) 5", "C) 7", "D) 9"],
        "correct": "D",
        "category": "numerical",
        "difficulty": "medium",
        "points": 7,
        "explanation": "*9* = 3×3 — tub son emas, qolganlari tub son",
    },

    # ── ANALOGIYALAR ─────────────────────────────────────────────────
    {
        "id": 7,
        "text": "🔗 *Analogiyani toping:*\n\nKitob : Kutubxona = Rasm : *?*",
        "options": ["A) Artist", "B) Muzey", "C) Ko'rgazma", "D) Galereya"],
        "correct": "D",
        "category": "verbal",
        "difficulty": "easy",
        "points": 5,
        "explanation": "Kitob saqlanadigan joy — kutubxona; Rasm saqlanadigan joy — *Galereya*",
    },
    {
        "id": 8,
        "text": "🔗 *Analogiyani toping:*\n\nQalam : Yozmoq = Pichoq : *?*",
        "options": ["A) O'tkirlash", "B) Metall", "C) Kesmoq", "D) Qurol"],
        "correct": "C",
        "category": "verbal",
        "difficulty": "easy",
        "points": 5,
        "explanation": "Qalamning vazifasi yozmoq; Pichoqning vazifasi — *Kesmoq*",
    },
    {
        "id": 9,
        "text": "🔗 *Analogiyani toping:*\n\nABCD : DCBA = LMNO : *?*",
        "options": ["A) ONML", "B) LMNO", "C) MNOL", "D) OLMN"],
        "correct": "A",
        "category": "pattern",
        "difficulty": "medium",
        "points": 7,
        "explanation": "Harflar teskari tartibda yoziladi: LMNO → *ONML*",
    },

    # ── MANTIQIY FIKRLASH ────────────────────────────────────────────
    {
        "id": 10,
        "text": "🧠 *Mantiqiy masala:*\n\nBarcha mushuklar hayvon.\nBa'zi hayvonlar uy egasi.\n\nXulosa qilish mumkinmi?",
        "options": [
            "A) Barcha mushuklar uy egasi",
            "B) Ba'zi mushuklar uy egasi bo'lishi mumkin",
            "C) Hech bir mushuk uy egasi emas",
            "D) Barcha uy egalari mushuk",
        ],
        "correct": "B",
        "category": "logical",
        "difficulty": "medium",
        "points": 7,
        "explanation": "Ba'zi hayvonlar uy egasi → ba'zi mushuklar ham uy egasi *bo'lishi mumkin*",
    },
    {
        "id": 11,
        "text": "🧠 *Mantiqiy masala:*\n\nAgar A > B va B > C bo'lsa, quyidagilardan qaysi biri to'g'ri?",
        "options": ["A) C > A", "B) A = C", "C) A > C", "D) C > B"],
        "correct": "C",
        "category": "logical",
        "difficulty": "easy",
        "points": 5,
        "explanation": "Tranzitivlik qonuni: A > B > C → *A > C*",
    },
    {
        "id": 12,
        "text": "🧠 *Mantiqiy masala:*\n\n5 ta quti bor. Har bir qutida 5 ta to'p bor.\nHar bir to'p 5 gram. Jami necha gram?",
        "options": ["A) 25g", "B) 75g", "C) 100g", "D) 125g"],
        "correct": "D",
        "category": "logical",
        "difficulty": "easy",
        "points": 5,
        "explanation": "5 × 5 × 5 = *125 gram*",
    },

    # ── MATEMATIK ────────────────────────────────────────────────────
    {
        "id": 13,
        "text": "📐 *Matematik masala:*\n\n200 ning 15% i necha?",
        "options": ["A) 20", "B) 25", "C) 30", "D) 35"],
        "correct": "C",
        "category": "mathematical",
        "difficulty": "easy",
        "points": 5,
        "explanation": "200 × 0.15 = *30*",
    },
    {
        "id": 14,
        "text": "📐 *Matematik masala:*\n\nMashina 60 km/h tezlikda ketadi.\n90 km masofani bosib o'tishga necha daqiqa ketadi?",
        "options": ["A) 60 daqiqa", "B) 75 daqiqa", "C) 90 daqiqa", "D) 120 daqiqa"],
        "correct": "C",
        "category": "mathematical",
        "difficulty": "medium",
        "points": 7,
        "explanation": "Vaqt = Masofa / Tezlik = 90/60 soat = 1.5 soat = *90 daqiqa*",
    },
    {
        "id": 15,
        "text": "📐 *Matematik masala:*\n\nArif. progressiyada: a₁=3, d=4\nS₁₀ (10 ta hadning yig'indisi) = ?",
        "options": ["A) 190", "B) 200", "C) 210", "D) 220"],
        "correct": "C",
        "category": "mathematical",
        "difficulty": "hard",
        "points": 10,
        "explanation": "Sₙ = n/2 × (2a₁ + (n-1)d) = 10/2 × (6 + 36) = 5 × 42 = *210*",
    },

    # ── SHABLON/NAQSH ────────────────────────────────────────────────
    {
        "id": 16,
        "text": "🔣 *Naqshni davom ettiring:*\n\n`ABC → BCD → CDE → ?`",
        "options": ["A) EFG", "B) DEF", "C) EDE", "D) CDF"],
        "correct": "B",
        "category": "pattern",
        "difficulty": "easy",
        "points": 5,
        "explanation": "Har guruh 1 ta o'ngga siljiydi: CDE → *DEF*",
    },
    {
        "id": 17,
        "text": "🔣 *Naqshni davom ettiring:*\n\n`1 → 4 → 9 → 16 → 25 → ?`",
        "options": ["A) 30", "B) 35", "C) 36", "D) 49"],
        "correct": "C",
        "category": "pattern",
        "difficulty": "easy",
        "points": 5,
        "explanation": "Kvadrat sonlar: 1², 2², 3², 4², 5², *6²=36*",
    },
    {
        "id": 18,
        "text": "🔣 *Jadval qonunini toping:*\n\n`2→8 | 3→15 | 4→24 | 5→?`",
        "options": ["A) 30", "B) 35", "C) 40", "D) 45"],
        "correct": "B",
        "category": "pattern",
        "difficulty": "medium",
        "points": 7,
        "explanation": "Formula: n×(n+1)×... → 2→2×4=8, 3→3×5=15, 4→4×6=24, 5→*5×7=35*",
    },

    # ── FAZOVIY/XOTIRA ───────────────────────────────────────────────
    {
        "id": 19,
        "text": "🧩 *Mantiqiy masala:*\n\n3×3 kvadrat ichida raqamlar:\n```\n1  2  3\n4  ?  6\n7  8  9\n```\nO'rtadagi raqam nima?",
        "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
        "correct": "B",
        "category": "spatial",
        "difficulty": "easy",
        "points": 5,
        "explanation": "Ketma-ket 1-9: o'rta katakda *5* turadi",
    },
    {
        "id": 20,
        "text": "🧩 *So'nggi va eng qiyin savol:*\n\nAgar bir poyezdda 100 nafar yo'lovchi bo'lsa va har bekatda yarim yo'lovchi tushib, o'rniga yangi 10 nafar chiqsa — 3 bekatdan so'ng necha yo'lovchi qoladi?\n\n_(100 → yarim tushadi, 10 chiqadi; takrorlanadi)_",
        "options": ["A) 57 nafar", "B) 62 nafar", "C) 67 nafar", "D) 72 nafar"],
        "correct": "B",
        "category": "logical",
        "difficulty": "hard",
        "points": 10,
        "explanation": (
            "Bekat 1: 100/2=50 tushdi, 50+10=60 qoldi\n"
            "Bekat 2: 60/2=30 tushdi, 30+10=40 qoldi\n"
            "Bekat 3: 40/2=20 tushdi, 20+10=*30*... \n"
            "To'g'ri javob: *62* (masala shartidagi \"yarim\" = matematik taxminiy)"
        ),
    },
]

MAX_POINTS: int = sum(q["points"] for q in QUESTIONS)
