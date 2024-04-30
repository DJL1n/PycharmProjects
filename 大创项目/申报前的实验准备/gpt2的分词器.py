"""
作者：legionb
日期：2024年04月30日
"""
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 加载预训练的GPT-2模型和分词器
model_name = "gpt2-medium"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

max_length = 100
prompt_text = "Once upon a time, there was a king who ruled over a vast kingdom. "

input_ids = tokenizer.encode(prompt_text, return_tensors="pt")
output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, do_sample=True)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated Text:\n", generated_text)
