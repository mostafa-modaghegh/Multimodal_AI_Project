# Day 05 - Notes

## بارگذاری و اجرای اولین Vision Language Model

---

# مسیر بارگذاری مدل

```text
Hugging Face
      ↓
Cache
      ↓
config.json
      ↓
ساخت معماری
      ↓
بارگذاری وزن‌ها
      ↓
مدل آماده اجرا
```

---

# فایل‌های مهم

### config.json

* معماری مدل
* تعداد لایه‌ها
* Hidden Size
* تعداد Attention Head
* تنظیمات مدل

> وزن‌ها داخل این فایل نیستند.

---

### model.safetensors

* وزن‌های آموزش‌دیده
* پارامترهای واقعی مدل

---

### Processor

* پیش‌پردازش تصویر
* پیش‌پردازش متن
* تبدیل ورودی به Tensor

---

# ساخت مدل

ابتدا معماری از روی Config ساخته می‌شود.

سپس وزن‌ها داخل همان معماری بارگذاری می‌شوند.

---

# انتقال مدل به GPU

```python
model.to("cuda")
```

ورودی‌ها نیز باید روی همان Device قرار بگیرند.

```python
inputs = {k: v.to(model.device) for k, v in inputs.items()}
```

در غیر این صورت:

```
Device Mismatch Error
```

---

# مشخصات SmolVLM-256M

Architecture

```
Idefics3ForConditionalGeneration
```

Device

```
CUDA
```

Hidden Size

```
576
```

Vocabulary

```
49280
```

Decoder Layers

```
30
```

Tensor Type

```
bfloat16
```

---

# Pipeline اجرای VLM

```text
Image
   ↓
Processor
   ↓
pixel_values
   ↓
Vision Encoder
   ↓
Projector
   ↓
LLM
   ↓
Generated Tokens
   ↓
Answer
```

---

# Cache

* فایل‌ها فقط یک بار دانلود می‌شوند.
* اجرای بعدی از Cache انجام می‌شود.
* مسیر پیش‌فرض:

```
~/.cache/huggingface/hub
```

(در ویندوز)

```
C:\Users\<User>\.cache\huggingface\hub
```

همچنین می‌توان مسیر Cache را تغییر داد.

---

# نکات مهم

✅ معماری قبل از وزن‌ها ساخته می‌شود.

✅ وزن‌ها بعداً داخل معماری قرار می‌گیرند.

✅ Processor جزئی از مدل نیست؛ ورودی را آماده می‌کند.

✅ مدل و ورودی باید روی یک Device باشند.

✅ مدل‌های کوچک ممکن است بخشی از پاسخ را حدس بزنند.

✅ خروجی `model.generate()` توکن است و سپس توسط Processor/Tokenizer به متن تبدیل می‌شود.

---

# خطاهای امروز

### ImportError

علت:

نسخه قدیمی Transformers

راه‌حل:

به‌روزرسانی کتابخانه

---

### Device Mismatch

علت:

مدل روی GPU ولی ورودی روی CPU

راه‌حل:

```python
inputs = {k: v.to(model.device) for k, v in inputs.items()}
```

---

# خروجی عملی

* دانلود اولین مدل
* بررسی Cache
* استخراج مشخصات مدل
* اجرای مدل روی GPU
* اجرای اولین Vision Language Model
* تولید اولین پاسخ از روی تصویر

---

# سؤال‌هایی که باید همیشه بتوانم پاسخ دهم

* Config چه کاری انجام می‌دهد؟
* وزن‌ها کجا ذخیره می‌شوند؟
* Processor چه وظیفه‌ای دارد؟
* چرا Hidden Size مهم است؟
* چرا Projector لازم است؟
* چرا باید مدل و ورودی روی یک Device باشند؟
* مسیر کامل اجرای یک VLM از تصویر تا متن چیست؟
