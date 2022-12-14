# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/17.
Author: 
    Sarah Shen
Date: 
    2022/8/17
"""


# 快排的任务是，在L R上进行排序
# 定义一个任务类，给定 arr 和 L，R， 回把arr上从L到R上进行排序
# 将任务放入栈中，
# 如果栈不为空，则拿出一个任务划分子任务放入栈中
# 如果等于区域的第一个位置，如果大于此时L，则有小于区域，才有左边的子任务，往栈里丢
# 如果等于区域的最后一个位置，小于此时的R，才有大于区域，才有右边的子任务，往栈里丢
# 这里没用任何递归，全部是迭代。

# 用对数器检查排序函数的正确与否。
