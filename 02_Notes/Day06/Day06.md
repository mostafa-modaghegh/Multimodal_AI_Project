# Day 06 — Generation & Inference

## موضوعات

- Processor
- input_ids
- pixel_values
- attention_mask
- pixel_attention_mask
- Visual Tokens
- Vision Encoder
- Projector
- Generate()
- max_new_tokens
- do_sample
- temperature
- Hallucination
- Repetition

---

## نکات مهم

- Processor متن و تصویر را به ورودی مدل تبدیل می‌کند.
- Vision Encoder فقط یک بار تصویر را پردازش می‌کند.
- خروجی Vision Encoder مجموعه‌ای از Visual Tokenها است.
- Projector این بردارها را وارد فضای مدل زبانی می‌کند.
- مدل متن را Token به Token تولید می‌کند.
- max_new_tokens فقط طول خروجی را محدود می‌کند.
- Temperature میزان تصادفی بودن انتخاب Token بعدی را کنترل می‌کند.
- Temperature زیاد می‌تواند باعث Hallucination شود.
- تکرار متن معمولاً ناشی از رفتار مدل زبانی است نه Vision Encoder.
- OCR و Plate Recognition معمولاً به Temperature پایین نیاز دارند.

---

## آزمایش‌های انجام شده

✅ max_new_tokens = 5

✅ max_new_tokens = 20

✅ max_new_tokens = 200

✅ do_sample=True

✅ temperature=0.5

✅ temperature=1.5