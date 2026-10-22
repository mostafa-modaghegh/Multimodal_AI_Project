## نوت‌های روز دهم پروژه

بررسی معماری داخلی SmolVLM و محل نصب LoRA

۱. معماری SmolVLM

مدل SmolVLM یک معماری مستقل نیست.
این مدل بر پایه معماری زیر ساخته شده است:
Idefics3ForConditionalGeneration 

۲. ساختار کلی مدل

Idefics3ForConditionalGeneration │ ├── model └── lm_head 

model شامل تمام اجزای اصلی مدل چندوجهی است.

lm_head وظیفه تولید خروجی نهایی مدل را بر عهده دارد.

۳. اجزای اصلی مدل

model ├── vision_model ├── connector └── text_model 

vision_model

همان Vision Encoder است.
وظیفه آن تبدیل تصویر به بردارهای ویژگی (Visual Embedding) است.
Image ↓ Visual Embedding 

connector

همان Projector است.
وظیفه آن تبدیل خروجی Vision Encoder به فضای ویژگی مدل زبانی است.
Visual Embedding ↓ Hidden Size = 576 

text_model

مدل زبانی استفاده‌شده در SmolVLM از نوع:
LlamaModel 
است.

۴. ساختار داخلی Llama

LlamaModel ├── embed_tokens ├── layers ├── norm └── rotary_emb 

embed_tokens

توکن‌های متنی را به بردارهای Embedding تبدیل می‌کند.
Input IDs ↓ Embedding Vector 

layers

شامل تمام لایه‌های Transformer است.
تمام عملیات اصلی مدل در این قسمت انجام می‌شود.

norm

آخرین لایه نرمال‌سازی (RMSNorm) قبل از خروجی مدل.

rotary_emb

پیاده‌سازی Rotary Positional Embedding (RoPE)
برای انتقال اطلاعات موقعیت توکن‌ها به مدل استفاده می‌شود.

۵. ساختار هر Transformer Layer

Layer ├── input_layernorm ├── self_attn ├── post_attention_layernorm └── mlp 

Self Attention

شامل چهار لایه اصلی است:
q_proj k_proj v_proj o_proj 
هر چهار لایه از نوع:
Linear 
هستند.

MLP

وظیفه پردازش و تبدیل ویژگی‌ها پس از Attention را بر عهده دارد.
به طور کلی:

Attention مسئول انتخاب اطلاعات مهم است.

MLP مسئول پردازش و غنی‌تر کردن نمایش‌های ویژگی است.

۶. دلیل نصب LoRA روی Attention

LoRA معمولاً روی لایه‌های:
q_proj k_proj v_proj o_proj 
نصب می‌شود.
دلیل آن این است که:
Attention تعیین می‌کند مدل برای پاسخ به هر سؤال به کدام قسمت از اطلاعات تصویر یا متن توجه کند.
در حالی که:
MLP بیشتر مسئول پردازش دانش کلی مدل است و معمولاً کمتر نیاز به تغییر دارد.

۷. ایده اصلی LoRA

وزن اصلی مدل تغییر نمی‌کند.
اگر وزن اصلی را با W نمایش دهیم:
W 
LoRA تنها یک اصلاح کوچک روی آن یاد می‌گیرد:
ΔW 
و در نهایت:
Wnew = W + ΔW 
که:
ΔW = BA 
است.
به همین دلیل تعداد پارامترهای قابل آموزش بسیار کمتر از آموزش کامل مدل خواهد بود.

۸. مسیرهای مهم داخل مدل

Vision Encoder

model.model.vision_model 

Projector

model.model.connector 

مدل زبانی

model.model.text_model 

اولین لایه Transformer

model.model.text_model.layers[0] 

Self Attention

model.model.text_model.layers[0].self_attn 

محل نصب LoRA

q_proj k_proj v_proj o_proj 

جمع‌بندی

در روز دهم معماری داخلی SmolVLM به صورت کامل بررسی شد.
برای اولین بار ساختار واقعی مدل استخراج گردید و مشخص شد که LoRA دقیقاً روی کدام بخش از مدل نصب خواهد شد.
از این مرحله به بعد وارد پیاده‌سازی عملی LoRA خواهیم شد.