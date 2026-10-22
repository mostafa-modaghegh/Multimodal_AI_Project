# ایده CLIP
       Image
         │
         ▼
   Vision Encoder
         │
         ▼
   Image Embedding
         │
         │
         │ similarity
         │
         ▼
    Text Embedding
         ▲
         │
    Text Encoder
         ▲
         │
"This is a dog"


## در مقاله، مسئله‌ی pre-training به شکل تشخیص این طراحی شده که کدام caption با کدام image جفت است.

Zero-Shot یعنی چه؟
مدل بدون اینکه مستقیماً برای این classification task آموزش دیده باشد، می‌تواند از زبان برای تعریف کلاس‌ها استفاده کند.

### CLIP به ما کمک کرد تصویر و زبان را در یک فضای معنایی به هم نزدیک کنیم؛ نسل‌های بعدی از این ایده و Vision Encoderهای مشابه استفاده کردند تا تصویر را وارد LLM کنند و مدل بتواند درباره‌ی تصویر زبان تولید کند.

Traditional CV
    ↓
Fixed Labels

CLIP
    ↓
Image ↔ Text Alignment
    ↓
Zero-Shot Transfer

Later VLMs
    ↓
Image
  ↓
Vision Encoder
  ↓
Projector
  ↓
LLM
  ↓
Natural Language Response

## VLM TimeLine


                  تکامل VLM
                      │
                      ▼
┌─────────────────────────────────────┐
│ CLIP                                │
│ Image ↔ Text Alignment              │
│ Zero-Shot Transfer                  │
└─────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────┐
│ Flamingo                            │
│ اتصال Vision به Language Model      │
│ Few-Shot Multimodal Learning        │
└─────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────┐
│ BLIP-2                              │
│ Vision → Q-Former → LLM             │
│ اتصال کارآمدتر مدل‌های موجود        │
└─────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────┐
│ LLaVA                               │
│ Vision Encoder → Projector → LLM    │
│ Visual Instruction Tuning            │
└─────────────────────────────────────┘
                      │
                      ▼
              نسل‌های جدید
          Qwen-VL / InternVL / ...
                      │
                      ▼
                  SmolVLM


# معماری پایه هر VLM
          IMAGE
            │
            ▼
    ┌────────────────┐
    │ Vision Encoder │
    └────────────────┘
            │
            ▼
     Visual Features
            │
            ▼
    ┌────────────────┐
    │   Connector    │
    │   / Projector  │
    └────────────────┘
            │
            ▼
     Visual Tokens
            │
            ▼
    ┌────────────────┐
    │      LLM       │
    └────────────────┘
            │
            ▼
      Text Response

# مقایسه ۴ نسل

      
| مدل          | ایده اصلی                    | رابط Vision/Language        | خروجی مولد |
| ------------ | ---------------------------- | --------------------------- | ---------- |
| **CLIP**     | Image-Text Alignment         | فضای embedding مشترک        | ❌          |
| **Flamingo** | Multimodal Few-Shot Learning | Cross-Attention             | ✅          |
| **BLIP-2**   | اتصال کارآمد مدل‌های frozen  | Q-Former                    | ✅          |
| **LLaVA**    | Visual Instruction Tuning    | Projector                   | ✅          |
| **SmolVLM2** | VLM کوچک و کارآمد            | Idefics3-based architecture | ✅          |

CLIP
Image ↔ Text
       ↓
Flamingo
Image + Text → LLM
       ↓
BLIP-2
Efficient Vision → LLM
       ↓
LLaVA
Vision + Instruction → LLM
       ↓
SmolVLM
Compact + Efficient Multimodal LLM


## «فرق Projector در LLaVA با Q-Former در BLIP-2 چیست؟ چرا اصلاً به این Connector نیاز داریم؟»

# «چرا اصلاً بین Vision Encoder و LLM یک Connector لازم است؟»
چون Vision Encoder و LLM در دو فضای متفاوت کار می‌کنند. Vision Encoder نمایش تصویری تولید می‌کند، در حالی که LLM ورودی را در فضای embedding خودش پردازش می‌کند. Connector وظیفه دارد اطلاعات تصویری را به نمایشی تبدیل کند که LLM بتواند آن را در کنار tokenهای متنی پردازش کند.
# «Projector و Q-Former چه فرقی دارند؟»
هر دو نقش پل بین vision و language را دارند، اما Projector عمدتاً یک نگاشت ساده‌ی featureها به فضای LLM است، در حالی که Q-Former یک Transformer با queryهای قابل‌آموزش است که می‌تواند اطلاعات مرتبط‌تری را از featureهای تصویری استخراج و فشرده کند.


#### Training Pipeline
                 DATASET
                    │
                    ▼
          Image + Instruction
                    │
                    ▼
              Data Collator
                    │
                    ▼
               Processor
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
        Image                Text
          │                   │
          ▼                   ▼
   Vision Encoder           Tokenizer
          │                   │
          ▼                   ▼
   Visual Features        Text Tokens
          │                   │
          ▼                   │
      Connector               │
          │                   │
          └─────────┬─────────┘
                    ▼
                   LLM
                    │
                    ▼
                Prediction
                    │
                    ▼
                   Loss
                    │
                    ▼
                Backward
                    │
                    ▼
              Weight Update