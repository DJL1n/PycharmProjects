"""
作者：legionb
日期：2024年04月30日
"""
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 加载预训练的GPT-2模型和分词器
model_name = "gpt2-medium"  # 您也可以选择其他规模的模型，例如"gpt2"或"gpt2-large"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# 设定生成文本的长度
max_length = 100

# 要生成的初始文本
prompt_text = "Once upon a time, there was a king who ruled over a vast kingdom. "

# 将文本转换为token
input_ids = tokenizer.encode(prompt_text, return_tensors="pt")

# 使用模型生成新文本
output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, do_sample=True)

# 将生成的token转换回文本
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated Text:\n", generated_text)
