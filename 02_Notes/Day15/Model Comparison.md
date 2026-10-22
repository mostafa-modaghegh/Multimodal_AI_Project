| مدل          | مسئله اصلی                      | Bridge / اتصال                    | قابلیت برجسته                    | جهت تکامل                    |
| ------------ | ------------------------------- | --------------------------------- | -------------------------------- | ---------------------------- |
| **CLIP**     | ارتباط Vision و Language        | Dual Encoder                      | Alignment / Zero-Shot            | Image ↔ Text                 |
| **Flamingo** | اتصال مدل‌های Vision و Language | Perceiver + Cross-Attention       | Multimodal Generation / Few-Shot | Vision → LLM                 |
| **BLIP-2**   | کاهش هزینه اتصال                | Q-Former                          | Efficient Multimodal Learning    | Vision → Q-Former → LLM      |
| **LLaVA**    | تعامل با کاربر                  | Projection                        | Visual Instruction Following     | Image + Instruction → Answer |
| **Qwen-VL**  | درک دقیق تصویر                  | Visual Receptor                   | OCR / Grounding / Localization   | Fine-grained Understanding   |
| **InternVL** | تقویت Vision                    | Vision Encoder + MLP              | Strong Vision + High Resolution  | Scaling Vision               |
| **SmolVLM**  | کاهش هزینه                      | Efficient visual-token processing | Small / Efficient VLM            | Capability per Compute       |



| مدل          |  سال | ایده محوری                     | اتصال Vision و Language           | قابلیت برجسته                                 |
| ------------ | ---: | ------------------------------ | --------------------------------- | --------------------------------------------- |
| **CLIP**     | 2021 | Alignment                      | دو Encoder + Contrastive Learning | Zero-Shot / Image-Text Alignment              |
| **Flamingo** | 2022 | اتصال مدل‌های ازپیش‌آموزش‌دیده | Perceiver + Gated Cross-Attention | Multimodal Generation + Few-Shot              |
| **BLIP-2**   | 2023 | Bridge کارآمد                  | Q-Former                          | Efficient Vision-Language Alignment           |
| **LLaVA**    | 2023 | Instruction Following          | Projection / MLP                  | Visual Chat                                   |
| **Qwen-VL**  | 2023 | درک دقیق تصویر                 | Visual Receptor                   | OCR + Grounding + Localization                |
| **InternVL** | 2024 | تقویت Vision                   | InternViT + MLP                   | Strong Vision + High-Resolution Understanding |


| Model    | Main Question                                             | Key Mechanism                       | Main Capability              |
| -------- | --------------------------------------------------------- | ----------------------------------- | ---------------------------- |
| CLIP     | How can vision and language be aligned?                   | Dual Encoder + Contrastive Learning | Zero-Shot                    |
| Flamingo | How can pretrained vision and language models interact?   | Resampler + Cross-Attention         | Few-Shot Multimodal Learning |
| BLIP-2   | How can this connection be made more efficiently?         | Q-Former                            | Efficient VLM                |
| LLaVA    | How can a VLM follow user instructions?                   | Vision Projection + LLM             | Visual Chat                  |
| Qwen-VL  | How can a VLM understand fine-grained visual information? | Visual Receptor + LLM               | OCR / Grounding              |
| InternVL | How far can visual capability be scaled?                  | Large Vision Encoder + Alignment    | Strong Visual Understanding  |
