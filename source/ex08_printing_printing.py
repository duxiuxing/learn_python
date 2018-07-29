# coding=utf-8
# 习题 8: 打印，打印
# %r主要用于调试和排错，因此没必要非打印出多好看的格式，下面这两个规则并不重要：
#   - 如果字符串内容中不包含单引号，那么%r打印出来的字符串是单引号的
#   - 如果字符串内容中包含单引号，那么%r打印出来的字符串是双引号的

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",  # 留意一下，这一句打印出来的是双引号
    "So I said goodnight."
)
