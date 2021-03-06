# QG训练营人工智能组第二周周记

2022年 3月 月29  日

### 生活随记

有的时候，是真的会为了一个目标而废寝忘食，放手一搏的，很难想象，上周还在学习python基本语法，还不知道python里的class有哪些成分，if(__name__==__main__)和一些专有名称的功能的自己，能够在这短短的几天内，看完了十几个小时的三剑客学习视频，大致学会了使用pandad, numpy和matplotlib,并且还学习到了机器学习的算法，每每相到这些，总是会让我感到心潮澎湃。在走向成功的道路上，在变得越来越优秀的过程中，总是需要有一些值得追求的事物的，总是希望谈笑有鸿儒的。

这几天又突然想起之前看的动漫《国王排名》，看了一些影评，有所感悟:传统的弱势群体中，人们遇事总会去希冀能有救世主解救自己于水深火热中。在这样的弱势思维下，个人的缺陷就会不断被放大不能精进。应当明白，我们自己才是自己的救世主。在极度渴望成功的情况下，就会不断激发自己的潜力，寻找出破局的办法。而盲目的埋怨，放弃，只会混淆得失，搅浑思路的流动。直面问题，奋力学习，把握核心，一点击破。当然，也不要忘记劳逸结合哈哈哈.

###  一周总结

#### 大组任务

首先，对于大组作业，由于之前很长时间都在使用C++编写程序，所以这周的大组任务转为使用C语言开始还有些不适应，在使用的过程中，也温习了C语言的语法。第一个作业是实现链栈，我自定义了LinkStack结构，并针对上一周师兄师姐提出来的建议对文件结构和交互式菜单进行了改善，其实链栈的实现还算简单，毕竟上周就已经掌握了单链表和双链表的结构，而链栈也是链式储存结构，所以我们无非就是增加一个指向栈顶的top指正即可。第二，要求实现一个泛型编程的链式队列，个人认为链式队列本身是比较好实现的，但增加了泛型的要求则需要提供对void＊进行处理的方法，也就增大了难度。

#### 小组任务

小组任务对我个人来说还是比较有挑战性的，但并不是数学方面的难以理解(我一直对自己的数学充满信心滴)，而是因为我对于python,可以说是新手上路，所以在完成了大组任务后，我首先就制定了自己的学习任务，也按着自己我安排完成了小组任务，先是理解师兄所讲的关于最小二乘和梯度下降的数学逻辑，包括一些对矩阵求导公式的推导等，然后，观看了三剑客和数据分析的学习视频，基本了解了三剑客和一些库的主要功能。基础准备后开始完成作业，编写了自定义的LinearRegression. py并使用该模块在jupyter note book里完成了对波士顿房价的预测分析。

###  存在问题

**在大组任务和小组任务的完成过程中也有许多问题:**

1. 一些细节的编程习惯导致出现难以发现的错误，例如，用于储存scanf_s的变量应申明为全局，若在封装的函数中声明，在函数调用之后会丢失储存在该数值(但会保留地址，地址上的值是不确定的)
2. main函数的结构仍有优化空间
3. python的特殊语法不够熟悉牢固，毕竟用的太少
4. 关于波士顿房价的预测分析

采用的是利用最小二乘法的解析方法来求W和b，但存在模型拟合度不高的问题，决定系数也不能让人满意

应当采用梯度下降法来优化模型，减小误差

可视化的图例和标记可以优化，还有一些有价值的对比曲线也可以展示

### 下周规划

- [ ] 打牢python基础语法
- [ ] 学习机器学习算法
- [ ] 全力以赴完成中期考核