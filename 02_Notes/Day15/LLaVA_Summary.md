# LLaVA — Visual Instruction Tuning
Large Language And Vision Assistant

## مشخصات

- **Authors:** Haotian Liu et al.
- **Conference:** NeurIPS 2023
- **سال:** 2023
- **Base Models:** CLIP Vision Encoder + LLM

## 1. مسئله
مدل‌های Vision-Language می‌توانند تصویر را به زبان مرتبط کنند، اما برای تعامل طبیعی با کاربر باید بتوانند **دستورهای زبانی درباره تصویر را بفهمند و پاسخ مناسب تولید کنند.**

## 2. ایده اصلی
استفاده از یک Vision Encoder از پیش‌آموزش‌دیده و یک LLM و آموزش یک اتصال ساده بین آن‌ها، سپس انجام **Visual Instruction Tuning** برای آموزش مدل به پاسخ‌گویی به دستورهای چندوجهی.

## 3. معماری
Image
  ↓
Vision Encoder
  ↓
Visual Features
  ↓
Projection Layer
  ↓
LLM
  ↓
Text Response

**Projection Layer:**
ویژگی‌های تصویری را به representationای تبدیل می‌کند که LLM بتواند در کنار اطلاعات زبانی خود از آن استفاده کند.

## 4. هدف اصلی
تبدیل یک مدل Vision + Language به یک **Multimodal Assistant** که بتواند به دستورها و سؤال‌های کاربر درباره تصویر پاسخ دهد.

## 5. آموزش
دو مرحله اصلی:
1. **Feature Alignment:** اتصال Vision Encoder به LLM با یک Projection Layer
2. **Visual Instruction Tuning:** آموزش مدل روی داده‌های Image + Question + Answer

برای تولید داده‌های instruction چندوجهی از GPT-4 استفاده شد.

## 6. دستاورد اصلی
نشان داد که با یک معماری نسبتاً ساده و داده‌های Visual Instruction می‌توان قابلیت **Multimodal Chat / Instruction Following** را به مدل اضافه کرد.

## 7. محدودیت

LLaVA اولیه یک مدل نسبتاً بزرگ و پرهزینه برای آموزش بود و برای سیستم‌های محدود مناسب نبود.

## 8. منبع

Haotian Liu et al. (2023).
Visual Instruction Tuning.
NeurIPS 2023.
https://arxiv.org/abs/2304.08485