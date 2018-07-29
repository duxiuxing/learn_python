# coding=utf-8
# 习题 10: 那是什么？
# 常用的转义符有：
#   转义符 功能
#   \\    Backslash (\) 反斜杠
#   \'    Single-quote (') 单引号
#   \"    Double-quote (") 双引号
#   \n    ASCII linefeed (LF) 换行符
#   \r    ASCII carriage return (CR) 回车符
#   \t    ASCII horizontal tab (TAB) 制表符

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
