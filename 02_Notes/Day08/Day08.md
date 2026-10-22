# Day 08 — Dataset Design for Vision-Language Models (VLM)

## هدف امروز

* یادگیری ساختار دیتاست‌های VLM
* تفاوت Dataset معمولی و Conversation Dataset
* طراحی اولین دیتاست پروژه
* ساخت اولین فایل `train.jsonl`
* طراحی Question Bank
* آشنایی با Validation دیتاست

---

# نکات کلیدی

## ساختار کلی VLM

Image

↓

Vision Encoder

↓

Projector

↓

LLM

↓

Answer

---

## هدف Fine-tuning

هدف:

یاد دادن زبان نیست.

هدف:

ایجاد ارتباط بهتر بین تصویر و فضای زبانی مدل است.

---

## Conversation Dataset

هر Sample شامل:

* تصویر
* سؤال
* پاسخ

است.

ساختار:

messages

↓

user

↓

assistant

---

## دلیل چند سؤال برای یک تصویر

یک تصویر فقط یک مفهوم ندارد.

مثال:

* OCR
* Detection
* Captioning
* Attribute
* Knowledge

---

## Question Bank

نمونه سؤال‌ها:

* Read the license plate number.
* Is there a license plate visible?
* Which city does this plate belong to?
* What is the color of the vehicle?
* Describe this image.

---

## ساختار پروژه

First_Dataset/

images/

train.jsonl

validate_dataset.py

dataset_info.md

---

## ساختار train.jsonl

هر Sample:

Image

*

Question

↓

Answer

همه Sampleها داخل یک فایل ذخیره می‌شوند.

---

## Dataset Version 1

Images:

5

Questions per image:

5

Training Samples:

25

---

## Validation

قبل از شروع Fine-tuning باید بررسی شود:

* JSON سالم باشد.
* مسیر تصاویر درست باشد.
* همه تصاویر وجود داشته باشند.
* ساختار messages صحیح باشد.

---

## ارتباط Dataset و LoRA

معمولاً:

Vision Encoder → Freeze

LLM → Freeze

Projector / LoRA → Train

---

## نتیجه امروز

اولین دیتاست واقعی پروژه ساخته شد و پروژه وارد مرحله آماده‌سازی برای Fine-tuning شد.
