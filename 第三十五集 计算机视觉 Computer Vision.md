# 计算机科学速成课 Crash Course Computer Science

### 第三十五集 计算机视觉 Computer Vision

视觉是信息最多的感官，比如周围的世界是怎么样的，如何和世界交互，因此半个世纪来，计算机科学家一直在想办法让计算机有视觉，因此诞生了“计算机视觉”（Computer Vision——CV）这个领域。目标是让计算机理解图像和视频，正如计算机视觉教授李飞飞最近说的：“Just like to hear is the not the same as to listen. To take pictures is not the same as to see.”

#### 跟踪一个颜色物体

图像是像素网格，每个像素的颜色通过三种基色定义：红，绿，蓝，通过组合三种颜色的强度，可以得到任何颜色，也叫RGB值。

最简单的计算机视觉算法最适合拿来入门——跟踪一个颜色物体，例如一个粉色球，首先，需要记下球的颜色，保存最中心像素的RGB值，然后给程序喂入图像，让它找最接近这个颜色的像素。算法可以从图像的左上角开始，逐个检查像素，计算和目标颜色的差异；检查了每个像素后，最贴近的像素很可能就是球。

不只是这张图片，可以在视频的每一帧图片跑这个算法来跟踪球的位置。因为光线，阴影和其他影响，球的颜色会有变化，不会和存的RGB值完全一样，情况更极端一些，比如比赛是在晚上，追踪效果可能会很差，如果球衣颜色和球一样，算法就完全失效，因此很少用这类颜色跟踪算法，除非环境可以严格控制。

#### 块

颜色跟踪算法是一个个像素搜索，因为颜色是在一个像素里，但是这种方法不适合占多个像素的特征，比如物体的边缘是多个像素组成的。为了识别这些特征，算法要一块块像素来处理，每一块都叫“块”（patches）。

#### 核

例如找垂直边缘的算法，假设用来帮无人机躲避障碍，为了简单可以把图片转成灰度，大部分算法都可以处理颜色，可以容易判断出杆子的左边缘从何开始，因为有垂直的颜色变化，可以制定规则：某像素是垂直边缘的可能性取决于左右两边像素的颜色差异程度，左右像素的区别越大，这个像素越可能是边缘，若色差很小则不是边缘，这个操作的数学符号可以表示如下图，称为核（kernel）或过滤器（filter）。里面的数字用来做像素乘法，总和存到中心像素里。

![image-20200311210005910](https://github.com/WilliamWuLH/My-notes-about-CCCS/blob/master/image/image-20200311210005910.png)

#### 卷积

首先将所有像素转成灰度值，把核的中心对准感兴趣的像素，这指定了每个像素要乘的值，然后把所有数字加起来的结果作为新的像素值，把核应用于像素块，这种操作叫卷积（convolution）。

如果把核用于照片中的每个像素，得到的结果是垂直边缘的像素值很高，注意：水平边缘是几乎看不见的，如果要突出某些特征，就需要用不同的核，比如对于水平边缘敏感的核。这两个边缘增强的核叫做“Prewitt算子”（Prewitt Operators），这只是众多核的两个例子，核能做很多种图像转换。

#### Viola-Jones Face Detection

例如有的核能够锐化图像，有的核可以模糊图像，核可以匹配特定的形状，这类核可以描述简单的形状，比如鼻梁往往比鼻子两侧更亮，所以线段敏感的核对这里的值更高，眼睛也很独特，一个黑色圆圈被外层更亮的一层像素包着，有核会对这种模式敏感。当计算机扫描图像时，最常见的是用一个窗口来扫描，可以找出人脸的特征组合，虽然每个核单独找出脸的能力很弱，但是组合在一起会相当准确。这是一个早期很有影响力的算法的基础，称为Viola-Jones Face Detection。

#### 卷积神经网络

如今热门算法“卷积神经网络”（Convolutional Neural Networks），神经网络的最基本单位是神经元，它有多个输入，然后会把每个输入乘一个权重值，然后求总和，这个过程类似卷积。实际上，如果我们给神经元输入二维像素，完全像卷积那样，输入权重等于核的值，但是和预定义的核不同，神经网络可以学习对自己有用的核来识别图像中的特征。

卷积神经网络用一堆神经元处理图像数据，每个都会输出一个新图像，本质上是被不同的核处理了，输出会被后面一层神经元处理，卷积卷积再卷积，在第一层可能会发现“边缘”这样的特征，下一层可以在这些基础上识别，比如由“边缘”组成的角落，然后下一层可以在“角落”上继续卷积，是一些可能有识别简单物体的神经元，如嘴巴或眉毛，然后不断重复，逐渐增加复杂度，直到某一层把所有特征放到一起。

卷积神经网络不是非要很多很多层，但是一般会有很多层来识别复杂物体和场景，也是一种深度学习。

#### 情感识别算法

在识别出人类的脸部之后，可以用更专用的计算机视觉算法来定位面部标志。有了标志点，判断眼睛有没有张开就很简单了，只是点和点之间的距离，也可以跟踪眉毛的位置，眉毛相对眼睛的位置可以分析出表情，根据嘴巴的标志点检测出是否微笑。这些信息可以用“情感识别算法”来完成，然后计算机会根据你的情绪适当行动。

#### 生物识别

面部标记点也可以捕捉脸的形状，比如两只眼睛之间的距离，以及前额有多高，做生物识别（biometric data），让有摄像头的计算机能认出你，应用于手机解锁，或者是政府用摄像头跟踪人。

抽象是构建复杂系统的关键，硬件层面，有工程师在造更好的摄像头，让计算机有越来越好的视力，用来自摄像头的数据可以用视觉算法找出脸和手，然后可以用其他算法接着处理，解释图片中的东西，比如用户的表情和手势，有了这些，人们可以做出新的交互体验，比如智能电视和智能辅导系统会根据用户的手势和表情来回应。
