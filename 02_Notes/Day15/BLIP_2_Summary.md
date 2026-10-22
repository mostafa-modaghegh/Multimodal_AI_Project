# BLIP-2 — Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

## مشخصات

- **Authors:** Junnan Li et al.
- **Conference:** ICML 2023
- **سال:** 2023

## 1. مسئله
هزینه بالای آموزش مدل‌های Vision-Language بزرگ و نیاز به آموزش تعداد زیادی پارامتر.

## 2. ایده اصلی
Vision Encoder و LLM از پیش‌آموزش‌دیده عملکرد خوبی دارند؛ بنابراین به‌جای آموزش مجدد آن‌ها، هر دو را Freeze کنیم و یک Bridge سبک بین آن‌ها آموزش دهیم.

## 3. معماری
Vision Encoder
      ↓
Visual Features
      ↓
Q-Former
      ↓
Projection
      ↓
LLM


**Q-Former:**
یک Transformer سبک است که با استفاده از Learnable Queryها، اطلاعات بصری مرتبط را از Vision Encoder استخراج و فشرده می‌کند.
در نتیجه به‌عنوان یک **Bridge / Information Bottleneck** بین Vision و Language عمل می‌کند.

## 4. آموزش
آموزش Q-Former در دو مرحله انجام می‌شود:
1. یادگیری ارتباط بین Visual Features و Language
2. یادگیری انتقال اطلاعات تصویری به شکلی که LLM بتواند از آن برای تولید متن استفاده کند

Vision Encoder و LLM اصلی در طول این فرایند Freeze هستند.

## 5. دستاورد اصلی
کاهش قابل توجه تعداد پارامترهای قابل آموزش و هزینه محاسباتی، در حالی که عملکرد قدرتمندی در وظایف Vision-Language حفظ می‌شود.
BLIP-2 در مقاله با **54 برابر پارامتر قابل آموزش کمتر** نسبت به Flamingo-80B، روی Zero-Shot VQAv2 حدود **8.7٪ بهتر** عمل کرد.

## 6. محدودیت
اگرچه Q-Former هزینه آموزش را کاهش می‌دهد، اما عملکرد مدل همچنان به توانایی Vision Encoder و LLM انتخاب‌شده وابسته است.
مدل میتواند به سوالات درمورد تصویر پاسخ دهد اما توانایی گفتگو مانند دستیار و فهم طیف مختلفی از سوالات را ندارد.

## 8. منبع
Junnan Li et al. (2023).
BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models.
ICML 2023.
https://proceedings.mlr.press/v202/li23q