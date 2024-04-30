"""
作者：legionb
日期：2024年04月30日
"""
from transformers import BertTokenizer, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

text1 = "I like dogs."
text2 = "I love dogs."
inputs1 = tokenizer(text1, return_tensors='pt')
inputs2 = tokenizer(text2, return_tensors='pt')

outputs1 = model(**inputs1)
outputs2 = model(**inputs2)

similarity = torch.cosine_similarity(outputs1.last_hidden_state.mean(dim=1), outputs2.last_hidden_state.mean(dim=1), dim=1)
print(similarity.item())
