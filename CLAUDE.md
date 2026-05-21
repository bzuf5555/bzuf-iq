# BZUF-IQ BOT — LOYIHA QONUNLARI
> Professional Senior Agent tomonidan yozilgan va tasdiqlangan

## AGENTLAR TIZIMI

| Agent | Model | Vazifa | Token sarfi |
|-------|-------|--------|-------------|
| **Architect Agent** | Opus | Arxitektura, murakkab algoritmlar, IQ hisoblash | Yuqori |
| **Developer Agent** | Sonnet | Handler'lar, DB operatsiyalar, o'rta murakkablik | O'rta |
| **Helper Agent** | Haiku | Shablonlar, formatlash, oddiy so'rovlar | Minimal |
| **Token Guard Agent** | Haiku | tasks.md ni kuzatish, done.md ga ko'chirish | Minimal |

### Token Guard Agent qoidalari
- `tasks.md` da har bir task `[HAIKU]`, `[SONNET]`, yoki `[OPUS]` bilan belgilanadi
- Task bajarilgandan so'ng `done.md` ga timestamp bilan ko'chiriladi
- Haiku: ≤ 3 soatlik ish; Sonnet: 3–8 soat; Opus: 8+ soat yoki kritik qarorlar

---

## MAJBURIY QONUNLAR (BUZISH MAN!)

### 1. BEPUL RESURSLAR QONUNI ⚡
> Loyihada ishlatiladigan barcha resurslar **100% BEPUL** bo'lishi SHART.
- MongoDB Atlas Free Tier (512MB) — ma'lumotlar bazasi
- Render.com Free Tier — hosting
- UptimeRobot Free Tier — 24/7 monitoring (har 5 daqiqada ping)
- GitHub Free — kod ombori
- python-telegram-bot / aiogram — bepul kutubxona
- **Hech qanday kredit kartasi yoki to'lov talab etilmaydi**

### 2. 24/7 ISHLASH QONUNI ⚡
> Bot **to'xtovsiz** ishlashi shart.
- Render free tier 15 daqiqa inaktivlikdan so'ng uxlaydi
- **Yechim**: UptimeRobot har 5 daqiqada `/health` endpoint'iga ping qiladi
- Webhook rejimi ishlatiladi (polling emas) — ishonchli va tezkor
- Barcha xatolar ushlanadi va loglanadi, bot hech qachon crash bo'lmaydi

### 3. MAJBURIY KONTAKT QONUNI
- Foydalanuvchi `/start` yuborganda telefon raqami so'raladi
- Kontakt ulashmasdan test o'tkazish mumkin emas
- MongoDB da bir marta saqlangan kontakt qayta so'ralmaydi
- `contact_shared: true` bo'lsa — to'g'ridan-to'g'ri test boshlanadi

### 4. KOD SIFATI QONUNI
- Barcha kod async bo'lishi shart (aiogram 3.x + motor)
- FSM (Finite State Machine) bilan holat boshqaruvi
- Har bir funksiya bitta vazifani bajaradi (SRP)
- `.env` faylida hech qanday maxfiy ma'lumot commit qilinmaydi
- Exception handling har yerda bo'lishi shart

### 5. MA'LUMOTLAR XAVFSIZLIGI QONUNI
- Telefon raqamlari faqat MongoDB da, shifrlangan muhitda
- Bot token `.env` da saqlanadi, kodda yozilmaydi
- Production da `DEBUG=False` bo'lishi shart

### 6. VIRAL MEXANIZM QONUNI
- Test natijasi ulashish tugmasi bo'lishi shart
- Ulashish matni jalb qiluvchi va qisqa bo'lishi kerak
- Bot link har doim natija xabarida ko'rsatiladi

### 7. TESTLAR SIFATI QONUNI
- Kamida 20 ta savol bo'lishi shart
- Savollar turli kognitiv sohalani qamrab olishi kerak
- Har bir savolda to'g'ri javob izohi bo'lishi shart
- IQ hisoblash psixometrik standartlarga asoslanishi kerak

---

## LOYIHA ARXITEKTURASI

```
bzuf-iq/
├── CLAUDE.md          # Loyiha qonunlari (shu fayl)
├── tasks.md           # Kutayotgan tasklar [HAIKU/SONNET/OPUS]
├── done.md            # Bajarilgan tasklar
├── .env.example       # Muhit o'zgaruvchilari namunasi
├── .env               # REAL muhit o'zgaruvchilari (git ignore!)
├── .gitignore
├── requirements.txt
├── render.yaml        # Render.com deploy konfiguratsiyasi
├── main.py            # Kirish nuqtasi (webhook + polling)
├── config.py          # Sozlamalar
├── database.py        # MongoDB ulanish va operatsiyalar
├── handlers/
│   ├── __init__.py
│   ├── start.py       # /start va kontakt handler
│   ├── test.py        # IQ test FSM handler
│   └── results.py     # Natijalar handler
├── data/
│   ├── __init__.py
│   └── questions.py   # 20+ IQ savol banki
└── utils/
    ├── __init__.py
    ├── iq_calculator.py  # IQ hisoblash algoritmi
    └── keyboards.py      # Telegram klaviaturalar
```

---

## DEPLOYMENT KETMA-KETLIGI

1. GitHub ga push qilinadi
2. Render.com GitHub repo bilan bog'lanadi
3. MongoDB Atlas cluster yaratiladi (free tier)
4. Render environment variables sozlanadi
5. UptimeRobot monitoring qo'shiladi
6. Webhook avtomatik o'rnatiladi

---

## MUHIT O'ZGARUVCHILARI

| O'zgaruvchi | Tavsif | Render da |
|-------------|--------|-----------|
| `BOT_TOKEN` | Telegram bot token | ✅ Shart |
| `MONGO_URI` | MongoDB Atlas URI | ✅ Shart |
| `WEBHOOK_URL` | Render app URL | ✅ Shart |
| `PORT` | Port (Render o'rnatadi) | Auto |
| `DEBUG` | Debug rejimi | False |
