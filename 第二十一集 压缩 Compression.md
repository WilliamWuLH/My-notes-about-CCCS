# 计算机科学速成课 Crash Course Computer Science

### 第二十一集 压缩 Compression

.txt .wav .bmp 这些格式虽然管用并且现在还在用，但是它们的简单性意味着效率不高，我们希望文件能小一点，这样能存大量文件，传输也会更快一些。解决方法是压缩，把数据占用的空间压得更小，用更少的位（bit）来表示数据。

#### 图像

图像一般存成一长串像素值，为了知道一行在哪里结束，图像要有元数据，写明尺寸等属性。每个像素的颜色是三种原色的组合：红，绿，蓝，每个颜色用一个字节存，数字范围是0到255，如果红绿蓝都是255会得到白色，如果混合255红色和255绿色将会得到黄色。一个图像有16个像素（4*4），每个像素3个字节，总共占48个字节，但可以压缩到少于48个字节。

#### 消除冗余——游程编码

一种方法是减少重复信息，最简单的方法叫游程编码（Run-Length Encoding），适合经常出现相同值的文件。比如吃豆人图像有7个连续黄色像素，与其全部存下来：黄色，黄色……可以插入一个额外字节，代表有7个连续黄色像素，然后删掉后面的重复数据。为了让计算机能分辨哪些字节是“长度“哪些字节是”颜色“，格式要一致，所以我们需要给所有像素前面标上长度，有时候数据会反而变得更多。同时，我们没有损失任何数据，可以轻易恢复到原来的数据，这叫做”无损压缩“（lossless compression），没有丢失任何数据，解压缩后，数据和压缩前完全一样。

#### 紧凑的表示方法——霍夫曼树

另一种无损压缩用更加紧凑的方式表示数据块，简写为 DFTBA（don't forget to be awesome），为此我们需要一个字典存储“代码”和“数据”间的对应关系。我们可以把图像看成一块块，而不是一个个像素，一些块出现的频率较高，我们希望用最紧凑的形式来表示它，一些块出现频率低则可以用更长的东西来表示。

1950年代大卫·霍夫曼发明了一种高效编码方式叫“霍夫曼树”（Huffman Tree），当时他还是麻省理工学院的学生，算法如下：首先列出所有块和出现的频率，每轮选取两个最低的频率，把这两个组成一个树，频率是这两个的频率之和，这就完成了一轮算法；需要重复这样做，选取频率最低的两个放在一起，并记录总频率；最后将全部的块组成一棵树就完成了。

霍夫曼树有一个很COOL的属性：按频率排列，频率低的在树的下面。将霍夫曼树变成字典：可以把每个分支用0和1标注，这样就可以生成字典。最COOL的地方在于每个块的编码绝对不会冲突，因为树的每条路径都是唯一的，意味着代码是“无前缀”（prefix-free）的，没有代码是以另一个代码开头的。

#### 无损压缩

“消除冗余”（removing redundancies）和“用更紧凑的表示方法”（using more compact representations）这两种方法通常会组合使用，几乎所有无损压缩格式都用了它们，比如GIF，PNG，PDF，ZIP。游程编码和字典编码都是无损压缩，压缩时不会丢失信息，解压后数据和之前的完全一样。

#### 有损压缩

其他有一些文件丢掉一些数据没什么关系，比如丢掉那些人类看不出区别的数据，大多数有损压缩技术都用到了这一点。以声音为例，人类的听觉不是完美的，有些频率我们很敏感，但其他一些我们根本听不见，比如超声波，在录音乐时超声波数据都可以舍弃，因为人类听不到超声波，另一方面人类对人声很敏感，所以应该尽可能保持原样，低音介于两者之间，人类能听到但是不敏感。

有损音频压缩利用这一点，用不同精度编码不同频段，听不出区别，所以不会明显影响体验。压缩音频是为了让更多人能同时打电话，如果网速变慢了，压缩算法会删去更多数据，进一步降低音频质量。和没压缩的音频格式相比，比如 WAV 或 FLAC，压缩音频文件如 MP3 能小10倍甚至更多。

#### 感知编码

这种删掉人类无法感知的数据的方法称为“感知编码”（perceptual coding），它依赖于人类的感知模型，模型来自“心理物理学”（psychophysics）领域，这是各种“有损压缩图像格式”的基础，最著名的是 JPEG。我们善于看到尖锐对比如物体的边缘，但是我们看不出颜色的细微变化，JPEG利用这一点把图像分解成8*8像素块，然后删掉大量高频率空间数据。

#### 视频压缩

视频只是一长串连续图片，所以图片的很多方面也适用于视频，但视频可以做一些小技巧，因为帧与帧之间很多像素一样，这叫时间冗余（temporal redundancy），视频里不用每一帧都存这些像素，可以只存变了的部分。当帧和帧之间有小小的差异时，很多视频编码格式只存变化的部分，这比存所有像素更有效率。更高级的视频压缩格式会更进一步，找出帧和帧之间相似的补丁，然后用简单效果实现，比如移动和旋转，变亮和变暗。

MPEG-4 是常见标准，可以比原文件小20倍到200倍，但用补丁的移动和旋转来更新画面当压缩太严重时会出错，没有足够空间更新补丁内的像素。

学习压缩可以高效存储图片，音乐，视频。

