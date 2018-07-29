# coding=utf-8
# 习题 6: 字符串和文本
# 字符串的格式符是%s，只有在想要获取某些东西的调试信息时才能用得到%r

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# 用%r来输出字符串，输出内容会带上单引号
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# 用%r来输出布尔值，那就是字符串形式的True或者False
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# 字符串可以直接用加号来拼接
print w + e
