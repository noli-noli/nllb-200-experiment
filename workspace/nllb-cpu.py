from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("models/nllb-moe-54b")
model = AutoModelForSeq2SeqLM.from_pretrained("models/nllb-moe-54b")

article = "こんにちは、私はハレです。"
inputs = tokenizer(article, return_tensors="pt")

translated_tokens = model.generate(
    **inputs, forced_bos_token_id=tokenizer.lang_code_to_id["eng_Latn"], max_length=10000
)
result=tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
print(result)