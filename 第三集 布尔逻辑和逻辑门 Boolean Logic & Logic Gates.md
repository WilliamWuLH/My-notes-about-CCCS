

# 计算机科学速成课 Crash Course Computer Science

### 第三集 布尔逻辑和逻辑门 Boolean Logic & Logic Gates

#### 二进制

二进制（Binary）为用两种状态表示，若只需要表示true和false，则两个值足够。电路闭合，电流流过，代表“真”，电路断开，无电流流过，代表“假”，二进制也可以表示为1和0。

一些早期的电子计算机是三进制的，有三种状态，甚至五进制，问题在于状态越多就越难区分信号，所以将两种信号尽可能分开，只用on和off两种状态可以尽可能减少这类问题。

#### 布尔代数

布尔代数（Boolean Algebra）专门处理true和false，已经解决了所有法则和运算，这也是计算机使用二进制的原因。

乔治·布尔（George Boole）是布尔二字的由来，布尔用逻辑方程系统而正式的证明真理，他在1847年的第一本书“逻辑的数学分析”（The Mathematical Analysis of Logic）中介绍过。

在布尔代数中，变量的值是true和false能进行逻辑操作，布尔代数中有三个基本操作：NOT，AND和OR。

#### NOT

NOT操作把布尔值反转，把true进行NOT就会变成false，反之亦然。

| INPUT | OUTPUT |
| ----- | ------ |
| TRUE  | FALSE  |
| FALSE | TRUE   |

晶体管：把控制线当做输入（input），把底部的电极当做输出（output），一个晶体管有一个输入和一个输出。如果打开输入（input on），输出也会打开（output on），因为电流可以流过；如果关闭输入（input off），输出也会关闭（output off），因为电流无法通过。

使用晶体管实现NOT GATE：把控制线当做输入（input），把上面的电极当做输出（output），下面的电极接地。

<img src=".\image\image-20200208160130051.png" alt="image-20200208160130051" style="zoom:50%;" />

<img src=".\image\image-20200208160314332.png" alt="image-20200208160314332" style="zoom:50%;" />![image-20200208160345472](.\image\image-20200208160345472.png)<img src=".\image\image-20200208160314332.png" alt="image-20200208160314332" style="zoom:50%;" />![image-20200208160345472](.\image\image-20200208160345472.png)

#### AND

AND操作有2个输入，1个输出。

| INPUT A | INPUT B | OUTPUT |
| ------- | ------- | ------ |
| TRUE    | TRUE    | TRUE   |
| TRUE    | FALSE   | FALSE  |
| FALSE   | TRUE    | FALSE  |
| FALSE   | FALSE   | FALSE  |

晶体管实现AND GATE：需要两个晶体管连在一起，这样有2个输入和1个输出。

<img src=".\image\image-20200208161241194.png" alt="image-20200208161241194" style="zoom:50%;" />

<img src=".\image\image-20200208161314443.png" alt="image-20200208161314443" style="zoom:50%;" />

<img src=".\image\image-20200208161344867.png" alt="image-20200208161344867" style="zoom:50%;" />

#### OR

OR操作有2个输入，1个输出。

| INPUT A | INPUT B | OUTPUT |
| ------- | ------- | ------ |
| TRUE    | TRUE    | TRUE   |
| TRUE    | FALSE   | TRUE   |
| FALSE   | TRUE    | TRUE   |
| FALSE   | FALSE   | FALSE  |

晶体管实现OR GATE：除了晶体管之外还要额外的线。

<img src=".\image\image-20200208204048454.png" alt="image-20200208204048454" style="zoom:50%;" />

<img src=".\image\image-20200208204237304.png" alt="image-20200208204237304" style="zoom:50%;" />

<img src=".\image\image-20200208204314642.png" alt="image-20200208204314642" style="zoom:50%;" />

<img src=".\image\image-20200208204342388.png" alt="image-20200208204342388" style="zoom:50%;" />

#### 符号抽象

进行抽象：

1. NOT门的画法是三角形前面一个圆点：<img src=".\image\image-20200208204825357.png" alt="image-20200208204825357"  />
2. AND门：![image-20200208204928646](.\image\image-20200208204928646.png)
3. OR门：![image-20200208205001206](.\image\image-20200208205001206.png)

晶体管和电线依然在那里，只是用符号来代表。

#### XOR

另一个有用的布尔操作：异或XOR

XOR操作有2个输入，1个输出。

| INPUT A | INPUT B | OUTPUT |
| ------- | ------- | ------ |
| TRUE    | TRUE    | FALSE  |
| TRUE    | FALSE   | TRUE   |
| FALSE   | TRUE    | TRUE   |
| FALSE   | FALSE   | FALSE  |

可以通过前面提到的3种门来做XOR门：可以先放一个OR门，因为OR和XOR的逻辑表很相似，现在的问题是当A和B都为true时，OR的输出和想要的XOR输出不一样，通过以下的电路可以实现：

![image-20200208210015191](.\image\image-20200208210015191.png)

XOR门：<img src=".\image\image-20200208210112131.png" alt="image-20200208210112131"  />