# coding=utf-8
# 习题 7: 更多打印
# 1. ex04展示过print在拼接输出内容的时候，会自动加空格
#   本题最后还展示了逗号在print语句的另外一个用法：保持不换行，
#   使用这种技巧可以把长字符串拆成多行代码来实现
# 2. 使用星号操作符，以后用print打印分割线，有更加简单的实现办法了

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
