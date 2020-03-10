# 3.1数据结构和序列
# 元组
tup = 4, 5, 6
tup
# 组成元素是元组的元组
nested_tup = (4, 5, 6), (7, 8)
nested_tup
# 使用tuple函数将任意序列或迭代器转换为元组
tuple([4, 0, 2])
tup = tuple('string')
tup
# python中的序列索引是从0开始的
tup[0]
# 元组一旦创建，各个位置上的对象是无法被修改的
tup = tuple(['foo', [1, 2], True])
tup[2] = Flase
# 如果元组中的一个对象是可变的，例如列表，可以再内部进行修改，这里的修改其实是对tup这个元组中第二位的元组[1,2]进行了修改
tup[1].append(3)
tup
# 可以使用+号链接来生成更长的元组,这里bar之后还要添加一个逗号，如果不添加的话会报错。
(4, None, 'foo') + (6, 0) + ('bar', )
# 将元组乘以整数，会和列表一样，生成含有多份拷贝的元组
('foo', 'bar') * 4
# 对象本身并没有复制，只是指向他们的引用进行了复制
# 3.1.1.1元组拆包
# 如果想要将元组型的表达式赋值给变量，Python会对等号右边的值进行拆包
tup = (4, 5, 6)
a, b, c = tup
c
# 这里相当于先将(4,5,6)复制给tup,然后a,b,c与tup这个变量进行绑定位置一一对应
# 即使是嵌套的元组也可以进行拆包
tup = 4, 5, (6, 7)
a, b, (c, d) = tup
d
# 使用这个功能能够轻易交换变量名。
a, b = 1, 2
a
b
# 拆包常用场景遍历元组或列表组成的序列
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print('a={0},b={1},c={2}'.format(a, b, c))
# 个人理解，这个for循环是定义a,b,c分别为一个元组的第一二三个元素，从seq元组中的第一个第二个第三个元组依次取值
# 更为高级的拆包方法
values = 1, 2, 3, 4, 5
a, b, *rest = values
a, b
rest
# rest部分有时是想要去除的数据，rest这个变量名并没有特指的意义，为了方便，很多python编程者会使用_来表示不想要的变量
a, b, *_ = values

# 第二节
# 元组方法
# 由于元组的内容和长度是无法改变的，它的实例方法很少。可以使用count，用于计量某个数值在元组中出现的次数。
a = (1, 2, 2, 2, 3, 4, 2)
a.count(2)  # 计量2在a这个元组中出现的次数

# 3.1.2列表
# 与元组不同，列表的长度是可变的，它所包含的内容也是可以修改的。可以使用中括号[]或者list类型函数来定义列表
a_list = [2, 3, 7, None]
tup = ('foo', 'bar', 'baz')
b_list = list(tup)
b_list
b_list[1] = 'peekaboo'  # 将列表b中的第二个元素替换为peekaboo
b_list

# 列表与元组非常相似（尽管元组不可修改），很多函数用法是相似的。
# list函数在数据处理中常用于将迭代器或者生成器转化为列表
gen = range(10)
gen  # 此时gen为0，10的区域范围
list(gen)  # 将gen转化为列表
gen

#  3.1.2.1 增加删除元素
# 使用append方法可以将元素添加到列表的尾部
b_list.append('dwarf')
b_list
# 使用insert方法可以将元素插入到指定列表位置
b_list.insert(1, 'red')  # 在列表b的第二个位置插入red
b_list
# 插入位置的范围在0到列表长度之间。

# insert与append相比，消耗的内存更大。因为子序列要为新元素的插入移动而腾出空间。如果想要再序列的
# 头部和尾部都插入新元素，应该尝试collections.deque,这是一个双端序列，可以满足头尾部都增加的要求。
# insert的反操作是pop,该操作会将特定位置的元素移除并返回：
b_list.pop(2)
b_list
# 元素可以通过remove方法移除，这个方法会定位第一个符合要求的值并移除它：
b_list.append('foo')
b_list # 将foo添加到最后一个位置
b_list.remove('foo') # 去掉第一个定位到该元素的foo
b_list


# 使用in关键字可以查询一个值是否在列表中
'dwarf' in b_list

# not关键词可以用作in的反义词，表示“不在”
'dwarf' not in b_list
# 与字典、集合相比，检查列表中是否包含一个值是十分缓慢的。这是因为
# python中在列表中进行了逐个线性扫描，而在字典和集合中Python是同时
# 检查所有元素的(基于哈希表）


# 3.1.2.2连接和联合列表
# 与元组类似，两个列表可以使用+号连接：
['4',None,'foo']+[7,8,(2,3)]
# 如果有一个已经定义的列表，可以用extend方法向该列表添加多个元素
x = [4,None,'foo']
x.extend([7,8,(2,3)])
x
# 注意通过添加内容来连接列表是一种相对高代价的操作，因为在连接过程中
# 创建了新列表，并且还要复制对象。

#3.1.2.3排序
# 可以使用列表的sort方法对列表进行内部排序（无须新建一个对象）
a=[7,2,5,1,3]
a.sort()
a
# sort有一些选项偶尔会排上用场。其中一项是传递一个二级排序key--一个
# 用于生成排序值的函数。例如，我们可以通过字符串长度的长度进行排序
b=['saw','small','He','foxes','six']
b.sort(key=len)
b

# 3.1.2.4二分搜索和已排序列表的维护
# 内部的bisect模块实现了二分搜索和已排序列表的插值。bisect.bisect
# 会找到元素应当被插入的位置。并保持序列排序，而bisect.insort将元素
# 插入到相应位置
import bisect
c=[1,2,2,2,3,4,7]
bisect.bisect(c,2)
# 上面代码意义是如果将2插入这个列表中，2应该在第4个位置插入，注意
# python中的位置是从0开始的
bisect.insort(c,6)
# 这段代码是将6插入到列表c中，不过是按照从小到大的顺序在第一个位置插入
c
# bisect模块的函数并不会检查列表是否已经排序，因为这么做代价太大
# 因此，对未排序的列表使用bisect的函数虽然不会报错，但可能导致不正确的结果。

# 3.1.2.5切片
# 使用切片符号可以对大多数序列类型选取其子集，它的基本形式是将start:stop
# 传入到索引符号[]中：
seq=[7,2,3,7,5,6,0,1]
seq[1:5]
# 取出了seq中1到五的元素
# 切片还可以将序列赋值给变量
seq[3:4]=[6,3]
seq
# 由于起始位置start的索引是包含的，而结束位置stop的索引并不包含，因此
# 元素的数量是stop-start
# start和stop是可以省略的，如果省略的话会默认传入序列的起始位置或结束
# 位置
seq[:5]
seq[3:]
# 负索引可以从序列的尾部进行索引
seq[-4:]
# 之前使用R，切片语义需要适应。图3-1有助于理解通过正数或负数进行切片
# 在图中，索引值被显示在“箱体边远”，有助于展示使用整数或负数进行切片
# 选择的起始位置和结束位置
# 步进值step可以在第二个冒号后面使用，意思是每个多少个数取一个值
seq[::2]
# 当需要对列表或元组进行翻转时，一种很简便的做法是向步进值-1
seq[::-1]

# 3.1.3 内建序列函数
# enumerate函数
# 我们经常需要在遍历一个序列的同时追踪当前元素的索引。一种自行实现的方法像下面的示例
i = 0
for value in collection:
    # 使用值
    i += 1 
# 由于这种场景很常见，所以python内建了enumerate函数，返回了(i,value)元组的序列，
# 其中value是元素的值，i是元素的索引
for i,value in enumerate(collection):
    #使用值做点事
# 当需要对数据建立索引时，一种有效的模式就是使用enumerate构造一个字典，将
# 序列值（假设是唯一的）映射到索引位置上：
some_list=['foo','bar','baz']
mapping={}
for i, v in enumerate(some_list):
    mapping[v]=i
mapping
# 以上代码将列表中的元素的索引输出

# 3.1.3.2 sorted
# sorted函数返回一个根据任意序列中的元素新建的已排序列表：
sorted([7,1,2,6,0,3,2])
sorted('horse race')
# sorted函数接受的参数与列表的sort方法一致

# 3.1.3.3 zip
# zip将列表、元组或其他序列的元素配对，新建一个元组构成的列表
seq1 = ['foo','bar','baz']
seq2 = ['one','two','three']
zipped = zip(seq1,seq2)
list(zipped)
# zip可以处理任意长度的序列，生成列表长度由最短的序列决定
seq3 = [False,True]
list(zip(seq1,seq2,seq3))
# zip的常用场景为同时遍历多个序列，有时会和enumerate同时使用；
for i,(a,b) in enumerate(zip(seq1,seq2)):
    print('{0}:{1},{2}'.format(i,a,b))
# 给定一个已经配对的序列时，zip函数有一种机智的方法去“拆分”序列。这种
# 方式的另一种思路就是将行的列表转换为列的列表。
pitchers=[('Nolan','Ryan'),('Roger','Clemens'),('Schilling','Curt')]
first_names,last_names= zip(*pitchers)
first_names
last_names

