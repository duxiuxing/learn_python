# coding=utf-8
# 习题 9: 打印，打印，打印
# 1. \n表示换行
# 2. 打印段落可以使用三引号（三个单引号或者三个双引号都支持）
# 3. %r和%s对\n的处理是不一样的

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

print "-" * 10
print "%r" % months
print "%s" % months
