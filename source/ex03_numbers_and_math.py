# coding=utf-8
# 习题 3: 数字和数学计算

# 1. 学习一下各种常见数学运算符的Englishi Name：
#   + plus 加号
#   - minus 减号
#   / slash 斜杠
#   * asterisk 星号
#   % percent 百分号
#   < less-than 小于号
#   > greater-than 大于号
#   <= less-than-equal 小于等于号
#   >= greater-than-equal 大于等于号
# 2. 需要把字符串和计算结果一起打印的时候，使用格式化语法输出，可读性更好

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print("Roosters %d" % (100 - 25 * 3 % 4))

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print("Is it greater or equal? %s" % str(5 >= -2))
print "Is it less or equal?", 5 <= -2

print('Two is %d' % (1 + 1))
