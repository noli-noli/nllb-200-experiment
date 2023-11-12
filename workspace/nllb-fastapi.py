from transformers import (
    AutoModelForSeq2SeqLM, 
    AutoTokenizer,
)
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import torch

app = FastAPI()

custom_headers = {"Access-Control-Allow-Origin": "*",}

model = AutoModelForSeq2SeqLM.from_pretrained("models/nllb-200-3.3B")

if torch.cuda.is_available():
    print("Using GPU")
    model = model.to("cuda")
else:
    print("Using CPU")
    model = model.to("cpu")

@app.get("/items/")
def run_model(text:str,input_code:str,output_code:str,max_length:int):
    print(f"output_code: {output_code}")
    print(f"text: {text}")
    tokenizer = AutoTokenizer.from_pretrained("models/nllb-200-3.3B",src_lang=input_code)
    input = tokenizer(text.replace("\n",""), return_tensors="pt")
    with torch.no_grad():
        output_ids = model.generate(
            **input.to(model.device),
            forced_bos_token_id=tokenizer.lang_code_to_id[output_code],
            max_length=max_length
        )   
    result = tokenizer.decode(output_ids.tolist()[0]).replace(f"{output_code}", "").replace("</s>", "")
    return JSONResponse(content=result, headers=custom_headers)
