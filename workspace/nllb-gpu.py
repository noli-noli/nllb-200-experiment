from transformers import (
    AutoModelForSeq2SeqLM, 
    AutoTokenizer,
)
import torch

tokenizer = AutoTokenizer.from_pretrained("models/nllb-moe-54b",src_lang="eng_Latn")
model = AutoModelForSeq2SeqLM.from_pretrained("models/nllb-moe-54b")

if torch.cuda.is_available():
    print("Using GPU")
    model = model.to("cuda")
else:
    print("Using CPU")
    model = model.to("cpu")

article = """In the first broadcast, a 15-minute version of each episode, divided into three parts, was broadcast for a total of 15 episodes. In addition, all 5 episodes of the 30-minute version were aired in the rebroadcast. There are various foreshadowings that have not been revealed, and the ending of the final episode hints that there will be a continuation of the story, but no sequel has been produced to date. What is unique about this work is that there was no announcement at all before it aired, and it was a sudden appearance that could be described as guerrilla-like. It can be said that it is positioned as a fill-in-the-blank work because it was treated as the B-side of Bottle Fairy, which was in the same frame, and because the first episode was divided into three parts."""
inputs = tokenizer(article, return_tensors="pt")
with torch.no_grad():
    output_ids = model.generate(
        **inputs.to(model.device),
        forced_bos_token_id=tokenizer.lang_code_to_id["jpn_Jpan"],
        max_length=10000    )
result = tokenizer.decode(output_ids.tolist()[0])
print(
    result.replace("jpn_Jpan ", "")
    .replace("</s>", "")
    .replace(".", "。")
    .replace(",", "、")
)