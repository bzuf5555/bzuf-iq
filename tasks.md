# TASKS — KUTAYOTGAN VAZIFALAR
> Token Guard Agent tomonidan boshqariladi

## OPUS — Murakkab vazifalar
- [x] [OPUS] Loyiha arxitekturasini tahlil qilish va CLAUDE.md yozish
- [x] [OPUS] IQ hisoblash algoritmini psixometrik standartlarga asoslab loyihalash
- [x] [OPUS] 54 ta kognitiv IQ savoli yaratish (random + shuffle)
- [x] [OPUS] FSM state machine arxitekturasini loyihalash

## SONNET — O'rta murakkablik
- [x] [SONNET] `main.py` — webhook + polling dual-mode
- [x] [SONNET] `config.py` — muhit o'zgaruvchilari
- [x] [SONNET] `database.py` — MongoDB motor async
- [x] [SONNET] `handlers/start.py` — /start, majburiy kontakt FSM
- [x] [SONNET] `handlers/test.py` — IQ test FSM + random + shuffle
- [x] [SONNET] `handlers/results.py` — IQ natija + tahlil
- [x] [SONNET] `utils/iq_calculator.py` — psixometrik IQ formula
- [x] [SONNET] `utils/keyboards.py` — inline/reply klaviaturalar
- [x] [SONNET] `render.yaml` — Render.com deploy
- [x] [SONNET] Global error handler middleware — crash oldini olish
- [x] [SONNET] `/mystats` komandasi — foydalanuvchi oldingi natijalari
- [x] [SONNET] Bot startup `set_my_commands` — BotFather menyusi
- [x] [SONNET] Throttling middleware — spam bosishdan himoya

## HAIKU — Oddiy vazifalar
- [x] [HAIKU] `requirements.txt`
- [x] [HAIKU] `.gitignore`
- [x] [HAIKU] `.env.example`
- [x] [HAIKU] `data/questions.py` — 54 ta savol banki
- [x] [HAIKU] `/help` komandasi — bot haqida ma'lumot
- [ ] [HAIKU] UptimeRobot monitoring (qo'lda)
- [ ] [HAIKU] Render env vars (qo'lda)
- [ ] [HAIKU] MongoDB Atlas cluster (qo'lda)

---
_Oxirgi yangilanish: 2026-05-21 | Token Guard Agent_
