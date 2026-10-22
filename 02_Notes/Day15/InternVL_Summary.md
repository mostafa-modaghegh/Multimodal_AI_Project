# InternVL — Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks

## مشخصات

- **Authors:** Zhe Chen et al.
- **Conference:** CVPR 2024
- **سال:** 2024
- **Vision Encoder:** InternViT-6B

## 1. مسئله
در بسیاری از VLMها، Language Model بسیار بزرگ و قدرتمند است، اما Vision Encoder نسبتاً کوچک‌تر است.
ایده مقاله این است که برای استفاده بهتر از توانایی LLM، بخش Vision نیز باید بسیار قوی‌تر شود.

## 2. ایده اصلی
به‌جای تمرکز فقط روی یک Bridge سبک بین Vision و Language، خود Vision Foundation Model را تا مقیاس بزرگ‌تر توسعه دهیم و سپس آن را به LLM متصل و هم‌تراز کنیم.

## 3. معماری
Image
  ↓
InternViT-6B
  ↓
Visual Features
  ↓
MLP Projector
  ↓
Visual Tokens
  ↓
LLM
  ↓
Text / Multimodal Output

**InternViT-6B:**
یک Vision Transformer بزرگ است که وظیفه اصلی آن استخراج ویژگی‌های قدرتمند از تصویر است.

## 4. هدف اصلی
افزایش توانایی Visual Understanding و ایجاد یک Vision Foundation Model قدرتمند که بتواند در کنار LLM برای وظایف مختلف Vision-Language استفاده شود.

## 5. آموزش
آموزش InternVL به صورت Progressive و در سه مرحله انجام می‌شود:
1. Vision-Language Contrastive Training
2. Vision-Language Generative Training
3. Supervised Fine-Tuning

در مرحله اول از داده‌های بسیار بزرگ Image-Text استفاده می‌شود و ویژگی‌های Vision و Language با یکدیگر Alignment می‌شوند.

## 6. دستاورد اصلی
InternVL نشان داد که می‌توان یک Vision Encoder بزرگ و قدرتمند را با LLM هم‌تراز کرد و از آن برای طیف گسترده‌ای از وظایف Visual و Vision-Language استفاده کرد.

## 7. ویژگی مهم
تمرکز InternVL بیشتر از مدل‌های قبلی روی **Scaling Vision** است.
یعنی:
Vision Encoder قوی‌تر
+
Alignment با LLM
=
Visual Understanding قوی‌تر

## 8. محدودیت
مقیاس بزرگ Vision Encoder و کل مدل باعث افزایش شدید هزینه محاسباتی و نیاز به سخت‌افزار قدرتمند می‌شود.

## 9. منبع
Zhe Chen et al. (2024).
InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks.
CVPR 2024.
https://openaccess.thecvf.com/content/CVPR2024/html/Chen_InternVL_Scaling_up_Vision_Foundation_Models_and_Aligning_for_Generic_CVPR_2024_paper.html