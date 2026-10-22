# CLIP — Learning Transferable Visual Models From Natural Language Supervision

## مشخصات

- **Authors:** Alec Radford et al.
- **Conference:** ICML 2021
- **سال:** 2021
- **Dataset:** حدود 400 میلیون جفت Image-Text

## 1. مسئله
محدودیت های مدل های تصویری کلاسیک بینایی 

## 2. ایده اصلی
بجای مرتبط کردن تصویر به یک لیبل یا کلاس،‌ بگوییم این متن و این تصویر مرتبط اند

## 3. معماری
                 ┌──────────────────┐
                 │  Image Encoder   │
Image ──────────►│                  │
                 └────────┬─────────┘
                          │
                          ▼
                    Image Vector
                          │
                          │ Similarity
                          │
                          ▲
                    Text Vector
                          │
                 ┌────────┴─────────┐
Text ───────────►│   Text Encoder   │
                 └──────────────────┘


                 
## 4. هدف اصلی
 هدف اصلی آن Image-Text Alignment است، نه تولید پاسخ متنی به سؤال کاربر.

## 5. آموزش
۴۰۰ میلیون جفت image-text  >>>   Contrastive Language-Image Pre-training

## 6. دستاورد اصلی
می‌توانیم بدون آموزش اختصاصی روی آن task، از زبان برای تعریف کلاس‌ها استفاده کنیم.  >>>  Zero-Shot Transfer

## 7. محدودیت
CLIP مسئله‌ی «هم‌تراز کردن تصویر و زبان» را هدف گرفت، اما هنوز مسئله‌ی «تولید زبان درباره تصویر» را به شکل یک VLM مکالمه‌ای حل نکرده بود

## 8. منبع 
Radford, A. et al. (2021).
Learning Transferable Visual Models From Natural Language Supervision.
ICML 2021.
https://proceedings.mlr.press/v139/radford21a