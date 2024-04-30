"""
作者：legionb
日期：2024年04月30日
"""
from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

text = "I love this product! It's amazing."
inputs = tokenizer(text, return_tensors='pt')
outputs = model(**inputs)

predicted_label = torch.argmax(outputs.logits).item()
print(predicted_label)  # 1 表示积极
