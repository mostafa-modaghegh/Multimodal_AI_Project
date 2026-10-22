# روز یازدهم — آماده‌سازی Pipeline آموزش SmolVLM

## هدف

درک کامل مسیر آماده‌سازی داده تا قبل از شروع Fine-Tuning مدل.

---

# ۱. ساختار مدل

```text
Idefics3ForConditionalGeneration
│
├── vision_model
├── connector
└── text_model
```

اولین لایه ترنسفورمر:

```text
Self Attention
├── q_proj
├── k_proj
├── v_proj
└── o_proj

MLP

LayerNorm
```

---

# ۲. محل نصب LoRA

LoRA فقط روی لایه‌های زیر نصب شد:

* q_proj
* k_proj
* v_proj
* o_proj

و هرکدام شامل:

* Base Layer
* LoRA A
* LoRA B

هستند.

---

# ۳. نتیجه اعمال LoRA

```text
Trainable Params

2,727,936

All Params

259,212,864

≈1.05%
```

نتیجه:

فقط حدود ۱ درصد مدل آموزش می‌بیند.

---

# ۴. خروجی Processor

خروجی:

```text
input_ids
attention_mask
pixel_values
pixel_attention_mask
```

ابعاد:

```text
input_ids

(1,893)

attention_mask

(1,893)

pixel_values

(1,13,3,512,512)

pixel_attention_mask

(1,13,512,512)
```

---

# ۵. معنی Shape ها

Batch:

```text
1
```

Tileهای تصویر:

```text
13
```

کانال رنگ:

```text
RGB
```

ابعاد هر Tile:

```text
512×512
```

---

# ۶. Decode Prompt

Processor ساختار Messages را به Prompt واقعی تبدیل می‌کند.

ساختار کلی:

```text
User

Image Tokens

Question

Assistant

Answer
```

---

# ۷. Image Token

Image Token خود تصویر نیست.

فقط Placeholder است.

ویژگی واقعی تصویر داخل:

```text
pixel_values
```

قرار دارد.

---

# ۸. Labels

```python
labels = input_ids.clone()
```

سپس:

* Padding
* Image Tokens

به

```text
-100
```

تبدیل می‌شوند.

Loss فقط روی پاسخ Assistant محاسبه می‌شود.

---

# ۹. Data Collator

وظایف:

* ساخت Batch
* Padding
* ساخت Labels
* حذف Image Tokenها از Loss
* آماده‌سازی خروجی برای Trainer

---

# نکات مهم

* LoRA فقط روی Attention نصب می‌شود.
* Vision Encoder فریز است.
* Processor خودش Chat Template را می‌سازد.
* Prompt واقعی مدل شامل تعداد زیادی Image Token است.
* Image Token با داده تصویری واقعی تفاوت دارد.
* Data Collator آخرین مرحله قبل از Trainer است.

---

# وضعیت پروژه

✅ پایان روز یازدهم

گام بعد:

* مطالعه Data Collator رسمی
* Trainer
* شروع آموزش واقعی مدل
