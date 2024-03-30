"""
作者：legionb
日期：2024年03月11日
"""
import ahocorasick

def build_ac_automaton(keywords):
    A = ahocorasick.Automaton()
    for index, keyword in enumerate(keywords):
        A.add_word(keyword, (index, keyword))
    A.make_automaton()
    return A

def search_ac_automaton(text, ac_automaton):
    results = []
    for end_index, (keyword_index, original_keyword) in ac_automaton.iter(text):
        start_index = end_index - len(original_keyword) + 1
        results.append({
            'start_index': start_index,
            'end_index': end_index,
            'keyword': original_keyword,
            'keyword_index': keyword_index
        })
    return results

# 示例用法
keywords = ["apple", "banana", "orange", "pear"]
text = "I like apples and oranges, but not bananas."

ac_automaton = build_ac_automaton(keywords)
matches = search_ac_automaton(text, ac_automaton)

for match in matches:
    print(f"Found '{match['keyword']}' at positions {match['start_index']}-{match['end_index']}")
