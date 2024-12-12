#1
import re
def replace_longest_n_sequence(s):
    matches = re.findall(r'н+', s)
    longest_seq_length = max(len(match) for match in matches) if matches else 0
    new_string = re.sub('н{' + str(longest_seq_length) + '}', '!' * longest_seq_length, s)
    return new_string, longest_seq_length
s = "аннааааннннвввнннннннвн"
new_s, length = replace_longest_n_sequence(s)
print(new_s)
print(length)

#2
def extract_bracket_content(s):
    start_index = s.find('(')
    end_index = s.rfind(')')
    if start_index == -1 or end_index == -1 or start_index >= end_index:
        return "Нет подходящих скобок."
    return s[start_index+1:end_index]
string = "Hello (world)! This is a test string."
content = extract_bracket_content(string)
print(content)

#3
def find_words_with_conditions(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if word.lower().startswith('а') or word.lower().endswith('я'):
            result.append(word)
    return result
sentence = "Абстракция, авария, аллея, книга, яблоко, радость"
words = find_words_with_conditions(sentence)
print(words)