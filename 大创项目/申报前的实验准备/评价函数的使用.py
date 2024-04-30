"""
作者：legionb
日期：2024年04月30日
"""
# from evaluate import list_evaluation_modules
#
# # 获取评价模块的列表
# evaluation_modules_list = list_evaluation_modules()
#
# # 打印评价模块的列表长度和列表本身
# print(len(evaluation_modules_list), evaluation_modules_list)
from datasets import load_metric

#加载一个评价指标
metric = load_metric('glue', 'mrpc')

# print(metric.inputs_description)

#计算一个评价指标
predictions = [0, 1, 0]
references = [0, 1, 1]

final_score = metric.compute(predictions=predictions, references=references)

print(final_score)