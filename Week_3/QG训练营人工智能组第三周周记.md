# QG训练营人工智能组第三周周记

### 生活随记



### 一周总结

#### 大组任务:

**一.排序算法:**

1. 

1. 选择排序:
   大致思路就是从头至尾扫描序列，找出最小的一个元素，和第一个元素交换，接着从剩下的元素中继续这种选择和交换方式，最终得到一个有序序列。将数组开始时视为无序数组,则找出最小的元素放在第一个位置,并划分为有序数组和无序数组,再循环找出无序序列中的最小值放在无序序列的第一个位置.

2. 插入排序:

   先看图解:

   ![插入排序](https://img-blog.csdnimg.cn/img_convert/6d867acd56e40fb32975f9e91d041fa9.png)
   插入排序酷似我们打扑克排时插入牌的过程,将待排序数据在有序序列(我们开始时假定第一个数是有序的)中依次向前比较,如果比待插入数大则向后移动一位,直到前面的数小于待插入数据则将数据插入,以此类推.

3. 归并排序:

   归并排序采用了分治的思想,即分而治之,先将待排序序列分成n个只含一个元素的数组,再两两合并.

   ![](https://img-blog.csdnimg.cn/20201025193048401.gif#pic_center)

   <img src="https://img-blog.csdnimg.cn/20201025193248506.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTY3MjE3OA==,size_16,color_FFFFFF,t_70#pic_center" style="zoom:50%;" />

   而归并算法的实现,我是使用了三个函数来完成的,如下:

   ```c
   /* 归并排序,提供给用户使用的接口 */
   void MergeSort(int *arr, int length); 
   
   /* 执行归并排序的合并操作 */
   void MergeArray(int *arr, int *temp, int left, int mid, int right); /* temp是临时数组 */
   
   /* 执行归并排序的划分操作 */
   void Merge_sort(int *arr, int *temp, int left, int right);  /* temp是临时数组 */
   ```

4. 快速排序:

   图片来自CSDN

   ![](https://img-blog.csdnimg.cn/20210515134431451.gif#pic_center#pic_center)
     快速排序的递归实现较为简单,关键是找到枢轴值所应在索引位置.

     而快速排序的非递归实现,其实质也就是把函数的递归调用改为了进出栈操作,并且两者的枢轴划分操作完全相同.

     再附上两种方法的比较:

   ```c
   /* 快速排序,递归版 */
   void QuickSort_Recursion(int *arr, int left, int right)
   {
   	if (left < right)
   	{
   		int index = Partition(arr, left, right);
   		QuickSort_Recursion(arr, left, index - 1);  /* 递归操作 */
   		QuickSort_Recursion(arr, index + 1, right);
   	}
   }
   
   /* 快速排序,非递归实现 */
   void QuickSort(int *arr, int length)
   {
   	int left = 0;
   	int right = length - 1;
   	int del;
   	Linkstack st;
   	InitLstack(&st);              /* 此处用的是前几次作业中自定义的链栈 */
   	PushLstack(&st, right);
   	PushLstack(&st, left);
   
   	while (isempty(&st) != TRUE)
   	{
   		PopLstack(&st, &left);
   		PopLstack(&st, &right);
   
   		if (left < right)
   		{
   			int index = Partition(arr, left, right);
               if (index > left)
               {
   				PushLstack(&st, index - 1);
   				PushLstack(&st, left);
               }
               if (right > index)
               {
   				PushLstack(&st, right);
   				PushLstack(&st, index+1);
               }
   		}
   	}
       DestroyLstack(&st);
   }
   ```

5.计数排序:  (空间优化的稳定计数排序)

​	先用一个题目引入桶排序,来自于CSDN

![](https://s2.loli.net/2022/04/03/yqrUwPDRkO91eVB.png)

​	经优化后的计数排序为稳定排序,所谓的前缀和就是将计数序列每个元素都加上前面所有的元素之和

![](https://img-blog.csdnimg.cn/20200531162701287.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTg1NTE5,size_16,color_FFFFFF,t_70)

​	这样也就达到了实现稳定排序的目的,而计数序列中的键是原数组中的数值,键对应的值则是键出现的次数.

​	再附上动图:

![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015231740840-6968181.gif)

​	简而言之,就是**计数,统计,分配**三步走.

6.基数计数排序:

​	基本思路:

1. 将所有待比较数值 **统一为同样的数位长度**，数位较短的数 **前面补零**
2. 然后从最低位开始，依次进行一次排序
3. 这样从最低位排序一直到最高位排序完成以后，序列就变成了一个有序序列

![](https://s2.loli.net/2022/04/04/yp4NcjwE2YfvWOZ.png)

7.颜色排序:

​	![](https://imgconvert.csdnimg.cn/aHR0cHM6Ly90dWNodWFuZzY2Ni5vc3MtY24tc2hlbnpoZW4uYWxpeXVuY3MuY29tL2ltZy9naWYyOS5naWY)

​	这种单遍历的双指针方法需要注意,当p1与p2对应的值交换时,要循环保证p2对应的值**不再为2**为止

```
for (p1 = 0; p1 < length;p1++)
	{
		while (p1<p2 && arr[p1] == 2)  /* 进行交换之后新的值可能仍然是2也可能是0,然而此时我们已经结束了交换,就会出现2在前的错误 */
		{
			swap(&arr[p2], &arr[p1]);
			p2--;
		}
		if (arr[p1] == 0)
		{
			swap(&arr[p0], &arr[p1]);
			p0++;
		}
	}
```

8.找到第K大/小的值:

​	我们可以使用快速排序优化后的快速选择算法



### 存在问题


### 下周规划

