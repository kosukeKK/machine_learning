# 便利だけど忘れやすいやつ、覚えたら消してく
#coding: UTF-8

from collections import OrderedDict
aa = OrderedDict()
aa["key1"] = "value1"
aa["key2"] = "value2"
print(aa)
for index, name in enumerate(["apple", "banana", "soccer"]):
    print(index, name)
