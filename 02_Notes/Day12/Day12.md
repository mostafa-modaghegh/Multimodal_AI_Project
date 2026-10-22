# Day 12 — Data Collator & Training Pipeline

---

# اهداف

* تکمیل Data Collator
* درک کامل مسیر ورود داده به مدل
* تولید Batch مناسب برای Trainer
* ساخت Labels صحیح
* تست کامل Data Collator

---

# مسیر کامل آموزش

```text
Dataset
      ↓
Conversation
      ↓
Processor
      ↓
Tokenizer + Vision Processor
      ↓
Data Collator
      ↓
Batch
      ↓
Trainer
      ↓
Model
      ↓
Loss
      ↓
Backward
      ↓
Optimizer
```

---

# وظیفه Data Collator

Data Collator مسئول است که:

* چند Sample را به یک Batch تبدیل کند.
* تصاویر را بارگذاری کند.
* Prompt را بسازد.
* Processor را اجرا کند.
* Labels را تولید کند.
* Padding را انجام دهد.
* خروجی را به Trainer تحویل دهد.

---

# چرا Labels را Clone می‌کنیم؟

```python
labels = batch["input_ids"].clone()
```

اگر Clone نکنیم:

* هر تغییری روی Labels
* روی Input_ids نیز اعمال می‌شود.

---

# چرا Image Tokenها حذف می‌شوند؟

مدل قرار نیست تصویر را پیش‌بینی کند.

پس:

```python
labels[labels == image_token_id] = -100
```

---

# چرا Padding حذف می‌شود؟

Padding فقط برای یکسان شدن طول توکن‌هاست.

نباید داخل Loss شرکت کند.

```python
labels[labels == pad_token_id] = -100
```

---

# خروجی Processor

```text
pixel_values
pixel_attention_mask
input_ids
attention_mask
labels
```

---

# شکل Tensorها

```text
pixel_values

(2,13,3,512,512)
```

تفسیر:

* Batch = 2
* Image Tokens = 13
* Channels = 3
* Resolution = 512×512

---

```text
input_ids

(2,893)
```

یعنی هر نمونه بعد از Tokenize شدن:

893 Token دارد.

---

# اصلاح مسیر تصاویر

به جای مسیر نسبی:

```text
images/plate001.jpg
```

از:

```python
Image.open(full_path)
```

استفاده شد.

---

# نسخه نهایی Data Collator

* بارگذاری تصاویر
* ساخت Prompt
* اجرای Processor
* ساخت Labels
* حذف Padding
* حذف Image Tokens

---

# تست موفق

خروجی نهایی:

```text
pixel_values
pixel_attention_mask
input_ids
attention_mask
labels
```

همگی بدون خطا تولید شدند.

---

# نتیجه

اکنون Pipeline آماده‌سازی داده‌ها کاملاً آماده است و تنها مراحل زیر باقی مانده‌اند:

* Trainer
* train.py
* شروع Fine-Tuning
* ذخیره Adapter
* Inference
