# Flamingo — a Visual Language Model for Few-Shot Learning 

## مشخصات

- **Authors:** Jean-Baptiste Alayrac et al.
- **Conference:** NeurIPS 2022
- **سال:** 2022
- **Dataset:** a mixture of vision and language datasets:
{MultiModal MassiveWeb(M3W) dataset
ALIGN dataset, composed of 1.8 billion images paired with alt-text
LTIP (Long Text & Image Pairs) which consists of 312 million image and text pairs
VTP (Video & Text Pairs) consists of 27 million short videos (approximately 22 seconds on average) paired with sentence descriptions}

## 1. مسئله
چگونه مدل‌های قدرتمند Vision و Language را به هم متصل کنیم تا
مدل بتواند درباره تصویر/ویدئو متن تولید کند و با چند مثال Task جدید را انجام دهد؟

## 2. ایده اصلی
استفاده از Vision Encoder و Language Model از پیش آموزش‌دیده
و ایجاد یک Bridge بین آنها.

## 3. معماری
Vision Encoder
      ↓
Perceiver Resampler
      ↓
Visual Tokens
      ↓
Gated Cross-Attention
      ↓
Language Model

Perceiver Resampler:
Featureهای تصویری با تعداد متغیر را به تعداد ثابتی Visual Token
تبدیل می‌کند. در مقاله 64 token تولید می‌شود.

Gated Cross-Attention:
Query از Language و Key/Value از Visual Features می‌آید.
این لایه‌ها بین لایه‌های Frozen Language Model قرار می‌گیرند.

## 4. هدف اصلی
مدل بتواند در مورد تصویر زبان تولید کند.

## 5. آموزش
Vision Encoder و بخش‌های اصلی Language Model فریز هستند.
بخش‌های جدید اتصال‌دهنده آموزش داده می‌شوند.

## 6. دستاورد اصلی
Few-Shot / In-Context Multimodal Learning

## 7. محدودیت
معماری نسبتاً پیچیده و مدل‌های بسیار بزرگ؛ بنابراین از نظر محاسباتی
برای سیستم‌های محدود مناسب نیست.

## 8. منبع 
Jean-Baptiste Alayrac et al. (2022).
Flamingo — a Visual Language Model for Few-Shot Learning
NeurIPS 2022
https://proceedings.neurips.cc/paper_files/paper/2022/hash/960a172bc7fbf0177ccccbb411a7d800-Abstract-Conference.html