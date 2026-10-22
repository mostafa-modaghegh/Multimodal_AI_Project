# SmolVLM — Redefining Small and Efficient Multimodal Models

## مشخصات

- **Authors:** Andrés Marafioti et al.
- **سال:** 2025
- **Model Family:** SmolVLM
- **Language Backbone:** SmolLM2
- **تمرکز:** Small and Efficient Vision-Language Models

## 1. مسئله
مدل‌های بزرگ VLM توانایی بالایی دارند، اما به حافظه و محاسبات زیادی نیاز دارند و اجرای آن‌ها روی سیستم‌های محدود دشوار است.

## 2. ایده اصلی
طراحی یک VLM کوچک و کارآمد با کاهش تعداد پارامترها و فشرده‌سازی مؤثر اطلاعات تصویری، بدون از دست دادن شدید قابلیت‌های چندوجهی.

## 3. معماری
Image
  ↓
Vision Encoder
  ↓
Visual Features
  ↓
Pixel Shuffle / Token Compression
  ↓
Visual Tokens
  ↓
SmolLM2
  ↓
Text Response


SmolVLM از معماری Idefics3 الهام گرفته است، اما Language Backbone را از Llama 3.1 8B به SmolLM2 تغییر داده و فشرده‌سازی visual information را شدیدتر کرده است.

## 4. هدف اصلی
ایجاد یک VLM با **حافظه و هزینه محاسباتی پایین** که بتواند روی سخت‌افزارهای محدود و حتی دستگاه‌های مصرفی اجرا شود.

## 5. آموزش
از مجموعه‌داده‌های چندوجهی مانند **The Cauldron** و **Docmatix** استفاده شده و داده‌های مربوط به captioning، document understanding، visual reasoning و instruction following در آموزش نقش دارند.

## 6. دستاورد اصلی
SmolVLM نشان می‌دهد که می‌توان با تعداد پارامتر بسیار کمتر، عملکرد قابل‌قبولی در وظایف مختلف چندوجهی به دست آورد.
مدل‌های خانواده SmolVLM در اندازه‌های کوچک مانند 256M و 500M پارامتر نیز ارائه شده‌اند.

## 7. ارتباط با پروژه ما
به دلیل محدودیت سخت‌افزاری پروژه، استفاده از یک VLM کوچک و کم‌مصرف منطقی‌تر از مدل‌های بزرگ بود.
ما از SmolVLM به‌عنوان مدل پایه استفاده کردیم و آن را برای **License Plate Reading** روی داده تخصصی خودمان Fine-Tune کردیم.

## 8. محدودیت
کوچک بودن مدل باعث می‌شود در برخی وظایف پیچیده، عملکرد آن نسبت به VLMهای بزرگ‌تر پایین‌تر باشد.

## 9. منبع
Andrés Marafioti et al. (2025).
SmolVLM: Redefining small and efficient multimodal models.
https://arxiv.org/abs/2504.05299