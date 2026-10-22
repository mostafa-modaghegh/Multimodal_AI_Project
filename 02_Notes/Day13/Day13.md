# Day 13 — End-to-End Fine-Tuning Pipeline Completed

## هدف امروز

تکمیل پروژه عملی Fine-Tuning مدل SmolVLM و اجرای موفق Inference با استفاده از Checkpoint آموزش‌دیده.

---

# کارهای انجام شده

## 1. تکمیل فایل train.py

- بارگذاری مدل
- بارگذاری Processor
- بارگذاری Dataset
- ایجاد Data Collator
- ایجاد Trainer
- آغاز فرآیند آموزش

---

## 2. رفع خطاهای Trainer

### نصب TensorBoard

RuntimeError:
TensorBoardCallback requires tensorboard

حل شد با:

```bash
pip install tensorboard
```

---

### remove_unused_columns

Trainer ستون messages را حذف می‌کرد.

حل شد با:

```python
remove_unused_columns=False
```

در TrainingArguments

---

## 3. مدیریت خطای CUDA Out Of Memory

به علت محدودیت GPU چهار گیگابایتی:

- کاهش Batch Size
- Gradient Checkpointing
- Gradient Accumulation
- FP16

---

## 4. انتقال آموزش به Google Colab

تمام پروژه روی Google Drive منتقل شد.

ساختار پروژه حفظ شد.

---

## 5. پایان آموزش

Checkpointهای زیر ایجاد شدند:

- checkpoint-125
- checkpoint-250
- checkpoint-375
- checkpoint-500
- checkpoint-625
- final_checkpoint

به علت پر شدن فضای Drive بخشی از فایل‌ها ناقص ذخیره شدند.

---

## 6. بازیابی مدل

فایل:

load_checkpoint.py

ایجاد شد.

مدل Fine-Tuned مجدداً بارگذاری شد.

---

## 7. اجرای Inference

نمونه خروجی:

Prompt

Read the license plate number.

Prediction

99 س 699 ایران 69

---

# نکات مهم

- هدف پروژه دقت بالا نبود.
- هدف اجرای کامل Pipeline بود.
- Pipeline با موفقیت اجرا شد.

---

# Pipeline نهایی

Dataset

↓

JSONL

↓

Processor

↓

Data Collator

↓

Trainer

↓

Fine-Tuning

↓

Checkpoint

↓

Inference

↓

Prediction

---

# مشکلات مهم

- محدودیت GPU
- محدودیت فضای Google Drive
- ناقص ذخیره شدن Checkpoint
- بازیابی مدل از فایل‌های موجود

---

# نتیجه

پروژه عملی Fine-Tuning به پایان رسید.

از اینجا به بعد تمرکز پروژه روی مطالعه مقالات و آماده‌سازی ارائه خواهد بود.