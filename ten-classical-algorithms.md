# 十大经典排序算法

## 冒泡排序

> 也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

### 算法步骤

1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。

2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。

3. 针对所有的元素重复以上的步骤，除了最后一个。

4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

### 代码实现

        function bubbleSort(arr) {
            var len = arr.length;
            for (var i = 0; i < len - 1; i++) {
                for (var j = 0; j < len - 1 - i; j++) {
                    if (arr[j] > arr[j+1]) {        // 相邻元素两两对比
                        var temp = arr[j+1];        // 元素交换
                        arr[j+1] = arr[j];
                        arr[j] = temp;
                    }
                }
            }
            return arr;
        }
        =================================================
        def bubbleSort(arr):
            for i in range(1, len(arr)):
                for j in range(0, len(arr)-i):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr

### 动图演示

![插入排序](./ten-classical-algorithms-img/bubbleSort.gif)

## 选择排序

> 选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。

### 算法步骤

1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置

2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

3. 重复第二步，直到所有元素均排序完毕

### 代码实现

        function selectionSort(arr) {
            var len = arr.length;
            var minIndex, temp;
            for (var i = 0; i < len - 1; i++) {
                minIndex = i;
                for (var j = i + 1; j < len; j++) {
                    if (arr[j] < arr[minIndex]) {     // 寻找最小的数
                        minIndex = j;                 // 将最小数的索引保存
                    }
                }
                temp = arr[i];  // 保存当前循环这一项的值
                arr[i] = arr[minIndex]; // 将在后面中选出来的最小值赋值给当前循环的这一项
                arr[minIndex] = temp; // 再让前面保存的循环这一项的值赋值给下一轮需要循环的项
            }
            return arr;
        }

        =========================================================

        def selectionSort(arr):
            for i in range(len(arr) - 1):
                # 记录最小数的索引
                minIndex = i
                for j in range(i + 1, len(arr)):
                    if arr[j] < arr[minIndex]:
                        minIndex = j
                # i 不是最小数时，将 i 和最小数进行交换
                if i != minIndex:
                    arr[i], arr[minIndex] = arr[minIndex], arr[i]
            return arr

### 动图演示

![插入排序](./ten-classical-algorithms-img/selectionSort.gif)

## 插入排序

> 插入排序的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，但它的原理应该是最容易理解的了，因为只要打过扑克牌的人都应该能够秒懂。插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。  
> 插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。

### 算法步骤

1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）

### 代码实现

        function insertionSort(arr) {
            var len = arr.length;
            var preIndex, current;
            for (var i = 1; i < len; i++) {
                preIndex = i - 1;
                current = arr[i];
                while(preIndex >= 0 && arr[preIndex] > current) {
                    arr[preIndex+1] = arr[preIndex];
                    preIndex--;
                }
                arr[preIndex+1] = current;
            }
            return arr;
        }
        ==============================================
        def insertionSort(arr):
            for i in range(len(arr)):
                preIndex = i-1
                current = arr[i]
                while preIndex >= 0 and arr[preIndex] > current:
                    arr[preIndex+1] = arr[preIndex]
                    preIndex-=1
                arr[preIndex+1] = current
            return arr

### 动图演示

![插入排序](./ten-classical-algorithms-img/insertionSort.gif)

## 希尔排序

## 归并排序

## 快速排序

## 堆排序

## 计数排序

## 桶排序

## 基数排序
