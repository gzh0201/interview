# 21 lambda函数

# 其实就是一个匿名函数,为什么叫lambda?因为和后面的函数式编程有关.

# 22 Python函数式编程

# 这个需要适当的了解一下吧,毕竟函数式编程在Python中也做了引用.

# python中函数式编程支持:

# filter 函数的功能相当于过滤器。调用一个布尔函数bool_func来迭代遍历每个seq中的元素；返回一个使bool_seq返回值为true的元素的序列。

# >>>a = [1,2,3,4,5,6,7]
# >>>b = filter(lambda x: x > 5, a)
# >>>print b
# >>>[6,7]

# map函数是对一个序列的每个项依次执行函数，下面是对一个序列每个项都乘以2：
# >>> a = map(lambda x:x*2,[1,2,3])
# >>> list(a)
# [2, 4, 6]

# reduce函数是对一个序列的每个项迭代调用函数，下面是求3的阶乘：
# >>> reduce(lambda x,y:x*y,range(1,4))
# 6

# 23 Python里的拷贝
# 引用和copy(),deepcopy()的区别
# import copy

# a = [1, 2, 3, 4, ['a', 'b']]  #原始对象
# b = a  #赋值，传对象的引用
# c = copy.copy(a)  #对象拷贝，浅拷贝
# d = copy.deepcopy(a)  #对象拷贝，深拷贝
# a.append(5)  #修改对象a
# a[4].append('c')  #修改对象a中的['a', 'b']数组对象

# print 'a = ', a

# print 'b = ', b

# print 'c = ', c

# print 'd = ', d
# 输出结果：

# a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]

# b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]

# c =  [1, 2, 3, 4, ['a', 'b', 'c']]

# d =  [1, 2, 3, 4, ['a', 'b']]

# 24 Python垃圾回收机制

# Python GC主要使用引用计数（reference counting）来跟踪和回收垃圾。在引用计数的基础上，通过“标记-清除”（mark and sweep）解决容器对象可能产生的循环引用问题，通过“分代回收”（generation collection）以空间换时间的方法提高垃圾回收效率。

# 1 引用计数

# PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。当一个对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少.引用计数为0时，该对象生命就结束了。

# 优点:

# 简单
# 实时性
# 缺点:

# 维护引用计数消耗资源
# 循环引用
# 2 标记-清除机制

# 基本思路是先按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发，遍历以对象为节点、以引用为边构成的图，把所有可以访问到的对象打上标记，然后清扫一遍内存空间，把所有没标记的对象释放。

# 3 分代技术

# 分代回收的整体思想是：将系统中的所有内存块根据其存活时间划分为不同的集合，每个集合就成为一个“代”，垃圾收集频率随着“代”的存活时间的增大而减小，存活时间通常利用经过几次垃圾回收来度量。

# Python默认定义了三代对象集合，索引数越大，对象存活时间越长。

# 举例：
# 当某些内存块M经过了3次垃圾收集的清洗之后还存活时，我们就将内存块M划到一个集合A中去，而新分配的内存都划分到集合B中去。当垃圾收集开始工作时，大多数情况都只对集合B进行垃圾回收，而对集合A进行垃圾回收要隔相当长一段时间后才进行，这就使得垃圾收集机制需要处理的内存少了，效率自然就提高了。在这个过程中，集合B中的某些内存块由于存活时间长而会被转移到集合A中，当然，集合A中实际上也存在一些垃圾，这些垃圾的回收会因为这种分代的机制而被延迟。

# 25 Python的List
# 定义
# python中在[ ]内，用逗号隔开的任意数据类型

# l1 = [1, 'a', [2, 2, 3]]
# 类型转换
# PS：但凡能被for循环遍历的数据类型，均可传递list()转换为列表类型，list()将会像for一样遍历数据类型的每一个元素然后放到列表中

# print(list('str'))  # 字符串
# print(list((1, 2, 3)))  # 元组
# print(list({1, 2, 3, 4}))  # 数组
# print(list([1, 2, 3, 4]))  # 列表
# print((list({'name': 'yyh', 'age': 18})))  # 字典
# 操作方式
# 复制代码
# # 1.按索引取值，正为从左往右，负为从右往左
# my_list = [1, 2, 3, 4, 5]
# print(my_list[1])
# print(my_list[-1])

# # 2.切片,起始：结束：步长
# my_list = [1, 2, 3, 4, 5]
# print(my_list[1:4])
# print(my_list[::2])
# print(my_list[::-1])  # 逆序输出列表

# # 3.长度
# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))

# # 4.in和not in
# my_list = [1, 3, 5, 7, 9]
# for i in range(10):
#     if i in my_list:
#         print(i)
#     if i not in my_list:
#         print(i * i)

# # 5.1 append()和extend()
# my_list = [1, 2, 3, 4, 5]
# my_list.append([6, 7, 8, 9])
# print(my_list)  # [1, 2, 3, 4, 5, [6, 7, 8, 9]]
# my_list = [1, 2, 3, 4, 5]
# my_list.extend([6, 7, 8, 9])
# print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # 5.2 insert() 要插入的位置，和插入的元素
# my_list = [1, 2, 3, 4, 5]
# my_list.insert(2,2222)
# print(my_list)
# 复制代码
 

# 复制代码
# # 6.1 删除元素 del(),remove(),pop()
# my_list = [1, 2, 3, 4, 5]
# my_list.pop()
# print(my_list)
# del my_list[2]  # del 指定要删除的索引
# my_list.remove(1)  # remove 指定要删除的元素
# print(my_list)

# # 7.reverse()将列表逆置
# my_list = [1, 3, 2, 5, 7]
# my_list.reverse()
# print(my_list)

# # 8.sort()将列表按升序排列,参数reverse为True则为降序
# my_list = [3, 1, 2, 5, 6, 0]
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)

# # 9.列表比较大小，依次比较对应元素的大小，直至比较出大小。
# my_list1 = ['1',3,1]
# my_list2 = ['1',4]
# print(my_list1 > my_list2)

# # 10.循环
# for char in my_list1:
#     print(char)
