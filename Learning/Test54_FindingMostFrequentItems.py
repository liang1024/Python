'''
Finding Most Frequent Items:查找最常用的项目
'''
from collections import Counter

text = "Swift is a high-performance system programming language. It has a clean and modern syntax, " \
       "offers seamless access to existing C and Objective-C code and frameworks, and is memory safe by default." \
       "Although inspired by Objective-C and many other languages, Swift is not itself a C-derived language." \
       " As a complete and independent language, Swift packages core features like flow control, data structures," \
       " and functions, with high-level constructs like objects, protocols, closures, and generics. Swift embraces modules," \
       " eliminating the need for headers and the code duplication they entail."
# 分割
words=text.split()

counter=Counter(words)
#找出出现次数最多的3个字符
top_three=counter.most_common(3)
print(top_three)
