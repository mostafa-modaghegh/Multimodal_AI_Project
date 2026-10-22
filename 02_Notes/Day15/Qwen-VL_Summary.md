# Qwen-VL — A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond

## مشخصات

- **Authors:** Jinze Bai et al.
- **سال:** 2023
- **Base Model:** Qwen-LM

## 1. مسئله
مدل‌های VLM علاوه بر درک کلی تصویر، باید بتوانند قابلیت‌های دقیق‌تری مانند خواندن متن داخل تصویر و تشخیص موقعیت اشیاء را نیز انجام دهند.

## 2. ایده اصلی
افزودن قابلیت Vision به Qwen-LM با استفاده از یک Vision Encoder و یک Visual Receptor و آموزش مدل برای وظایف مختلف Vision-Language.

## 3. معماری
Image
  ↓
Vision Encoder
  ↓
Visual Features
  ↓
Visual Receptor
  ↓
Visual Tokens
  ↓
Qwen-LM
  ↓
Text Output

**Visual Receptor:**
ویژگی‌های تصویری را به representationهای فشرده‌ای تبدیل می‌کند که Qwen-LM بتواند از آن‌ها در کنار اطلاعات زبانی استفاده کند.

## 4. قابلیت‌های اصلی
- Image Understanding
- Visual Question Answering
- Text Reading / OCR
- Visual Grounding
- Object Localization

## 5. آموزش
Qwen-VL با یک **3-Stage Training Pipeline** آموزش داده شد:
1. Image-Text Alignment
2. Multimodal Pre-training
3. Visual Instruction Tuning

برای قابلیت‌های Grounding و Text Reading از داده‌هایی شامل **Image + Caption + Bounding Box** استفاده شد.

## 6. دستاورد اصلی
Qwen-VL علاوه بر درک و گفت‌وگو درباره تصاویر، قابلیت‌هایی مانند **Text Reading، Grounding و Localization** را نیز به مدل اضافه کرد.

## 7. محدودیت
Qwen-VL نسبت به مدل‌های کوچک‌تر، مدل و pipeline محاسباتی بزرگ‌تری دارد و اجرای آن روی سیستم‌های محدود دشوارتر است.

## 9. منبع
Jinze Bai et al. (2023).
Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond.
https://arxiv.org/abs/2308.12966