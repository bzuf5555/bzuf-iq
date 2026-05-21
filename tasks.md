# TASKS — KUTAYOTGAN VAZIFALAR
> Token Guard Agent tomonidan boshqariladi
> Format: `- [ ] [MODEL] Vazifa tavsifi`

## OPUS — Murakkab vazifalar (Arxitektura darajasi)

- [x] [OPUS] Loyiha arxitekturasini tahlil qilish va CLAUDE.md yozish
- [x] [OPUS] IQ hisoblash algoritmini psixometrik standartlarga asoslab loyihalash
- [x] [OPUS] 20+ kognitiv IQ savollari yaratish (turli domenlar: raqamli, verbal, mantiqiy, fazoviy)
- [x] [OPUS] FSM state machine arxitekturasini loyihalash

## SONNET — O'rta murakkablik (Developer darajasi)

- [x] [SONNET] `main.py` — webhook + polling dual-mode entry point
- [x] [SONNET] `config.py` — muhit o'zgaruvchilari va sozlamalar
- [x] [SONNET] `database.py` — MongoDB motor async operatsiyalar
- [x] [SONNET] `handlers/start.py` — /start, kontakt majburiy ulashish
- [x] [SONNET] `handlers/test.py` — IQ test FSM (savollar, javoblar, progress)
- [x] [SONNET] `handlers/results.py` — IQ natija, tahlil, ulashish
- [x] [SONNET] `utils/iq_calculator.py` — IQ hisoblash va label berish
- [x] [SONNET] `utils/keyboards.py` — inline va reply klaviaturalar
- [x] [SONNET] `render.yaml` — Render.com deploy konfiguratsiyasi
- [x] [SONNET] Error handling middleware va logging sozlash

## HAIKU — Oddiy vazifalar (Helper darajasi)

- [x] [HAIKU] `requirements.txt` — barcha dependencylar
- [x] [HAIKU] `.gitignore` — maxfiy fayllarni himoya
- [x] [HAIKU] `.env.example` — muhit o'zgaruvchilari namunasi
- [x] [HAIKU] `data/questions.py` — savol banki JSON strukturasi
- [ ] [HAIKU] UptimeRobot monitoring sozlash (qo'lda bajariladi)
- [ ] [HAIKU] Render dashboard da env vars qo'shish (qo'lda bajariladi)
- [ ] [HAIKU] MongoDB Atlas cluster yaratish (qo'lda bajariladi)
- [ ] [HAIKU] GitHub remote push (qo'lda bajariladi)

---
_Oxirgi yangilanish: 2026-05-21 | Token Guard Agent_
