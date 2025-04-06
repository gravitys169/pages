# 附录A：数学基础快速回顾 (Math Essentials Refresher)

理解大型语言模型（LLM）的内部工作原理，离不开一些核心的数学概念。本附录旨在快速回顾与 LLM 最相关的数学基础知识，包括线性代数、微积分、概率论与信息论。这并非详尽的数学教程，而是为读者提供一个概要性的回顾和关键概念索引，以便更好地理解书中的技术细节。

## A.1 线性代数 (Linear Algebra)

线性代数是描述和操作向量与空间的基础，在 LLM 中无处不在，尤其是在表示数据（如词嵌入）、模型参数（权重矩阵）以及执行计算（矩阵乘法）等方面。

*   **标量 (Scalar):** 单个数字，例如 $5$, $-3.14$, $\\pi$。
*   **向量 (Vector):** 有序的数字列表，表示空间中的一个点或方向。通常用小写粗体字母表示，例如 $\\mathbf{x} = [x_1, x_2, ..., x_n]$。向量可以看作是一维数组。
    *   **维度 (Dimension):** 向量中元素的数量。
    *   **运算:** 向量加法、标量乘法、点积 (Dot Product)。
    *   **点积 (Dot Product / Inner Product):** 两个维度相同的向量 $\\mathbf{a}$ 和 $\\mathbf{b}$ 的点积定义为 $\\mathbf{a} \\cdot \\mathbf{b} = \\sum_{i=1}^n a_i b_i$。结果是一个标量。点积与向量间的角度和投影有关。在 LLM 中，点积常用于计算相似度（如注意力机制中的 Query-Key 相似度）。
*   **矩阵 (Matrix):** 二维数字数组，通常用大写粗体字母表示，例如 $\\mathbf{A}$。
    *   **维度:** $m \\times n$ 矩阵表示有 $m$ 行和 $n$ 列。
    *   **运算:** 矩阵加法、标量乘法、矩阵乘法 (Matrix Multiplication)、转置 (Transpose)。
    *   **矩阵乘法:** 两个矩阵 $\\mathbf{A}$ ($m \\times k$) 和 $\\mathbf{B}$ ($k \\times n$) 的乘积是一个 $m \\times n$ 矩阵 $\\mathbf{C} = \\mathbf{A} \\mathbf{B}$，其中 $C_{ij} = \\sum_{l=1}^k A_{il} B_{lj}$。矩阵乘法是神经网络（包括 Transformer）中的核心计算步骤，用于线性变换和特征提取。
    *   **转置:** 矩阵 $\\mathbf{A}$ 的转置 $\\mathbf{A}^T$ 是将 $\\mathbf{A}$ 的行和列互换得到的矩阵。$(A^T)_{ij} = A_{ji}$。
*   **张量 (Tensor):** 矩阵向更高维度的推广。标量是 0 阶张量，向量是 1 阶张量，矩阵是 2 阶张量。LLM 中的数据（输入、参数、激活值）通常表示为高阶张量，例如，一个批次的词嵌入可以表示为 3 阶张量 (batch\_size, sequence\_length, embedding\_dimension)。
*   **线性变换 (Linear Transformation):** 通过矩阵乘法将一个向量映射到另一个向量的操作 $\\mathbf{y} = \\mathbf{W} \\mathbf{x}$，其中 $\\mathbf{W}$ 是变换矩阵。神经网络中的线性层（全连接层）执行的就是线性变换（加上偏置项）。
*   **特征值与特征向量 (Eigenvalues and Eigenvectors):** 对于方阵 $\\mathbf{A}$，如果存在标量 $\\lambda$ 和非零向量 $\\mathbf{v}$ 使得 $\\mathbf{A} \\mathbf{v} = \\lambda \\mathbf{v}$，则 $\\lambda$ 称为特征值，$\\mathbf{v}$ 称为对应的特征向量。特征值和特征向量描述了矩阵变换的主要方向和尺度。
*   **奇异值分解 (Singular Value Decomposition, SVD):** 将任意 $m \\times n$ 矩阵 $\\mathbf{A}$ 分解为 $\\mathbf{A} = \\mathbf{U} \\mathbf{\\Sigma} \\mathbf{V}^T$ 的形式，其中 $\\mathbf{U}$ 和 $\\mathbf{V}$ 是正交矩阵，$\\mathbf{\\Sigma}$ 是对角矩阵（对角线元素为奇异值）。SVD 在降维（如 PCA）、推荐系统和理解矩阵性质方面有广泛应用。

## A.2 微积分 (Calculus)

微积分，特别是微分学，是理解 LLM 训练过程（梯度下降）和优化的基础。

*   **导数 (Derivative):** 衡量函数 $f(x)$ 在某一点 $x$ 处随自变量变化的瞬时速率，记作 $f'(x)$ 或 $\\frac{df}{dx}$。它表示函数曲线在该点的切线斜率。
*   **偏导数 (Partial Derivative):** 对于多元函数 $f(x_1, x_2, ..., x_n)$，它衡量函数在某一点处仅沿一个自变量 $x_i$ 方向变化的速率，记作 $\\frac{\\partial f}{\\partial x_i}$。
*   **梯度 (Gradient):** 多元函数 $f$ 在某一点处的梯度是一个向量，包含了函数在该点处沿所有自变量方向的偏导数，记作 $\\nabla f = [\\frac{\\partial f}{\\partial x_1}, \\frac{\\partial f}{\\partial x_2}, ..., \\frac{\\partial f}{\\partial x_n}]$。梯度向量指向函数值增长最快的方向，其大小表示增长速率。
*   **链式法则 (Chain Rule):** 用于计算复合函数的导数。如果 $z = f(y)$ 且 $y = g(x)$，则 $z$ 对 $x$ 的导数为 $\\frac{dz}{dx} = \\frac{dz}{dy} \\frac{dy}{dx}$。对于多元复合函数，链式法则更为复杂，但核心思想相同。链式法则是神经网络**反向传播算法 (Backpropagation)** 的数学基础，使得我们能够高效地计算损失函数 L 相对于网络中所有参数（如权重 $\\mathbf{W}$）的梯度 $\\nabla_{\\mathbf{W}} L$。
*   **梯度下降 (Gradient Descent):** 一种常用的优化算法，用于寻找函数的最小值（例如，最小化损失函数）。它通过迭代地沿着梯度的**负方向**更新参数来逐步逼近最小值点：$\\mathbf{w}_{new} = \\mathbf{w}_{old} - \\eta \\nabla_{\\mathbf{w}} L$，其中 $\\eta$ 是学习率 (learning rate)，控制每次更新的步长。本书中讨论的 AdamW 等优化器是梯度下降算法的变种。
*   **雅可比矩阵 (Jacobian Matrix):** 对于一个从 $\\mathbb{R}^n$ 映射到 $\\mathbb{R}^m$ 的向量函数 $\\mathbf{f}(\\mathbf{x})$，其雅可比矩阵是一个 $m \\times n$ 矩阵，包含了所有一阶偏导数 $J_{ij} = \\frac{\\partial f_i}{\\partial x_j}$。
*   **海森矩阵 (Hessian Matrix):** 对于一个标量函数 $f(\\mathbf{x})$，其海森矩阵是一个 $n \\times n$ 的方阵，包含了所有二阶偏导数 $H_{ij} = \\frac{\\partial^2 f}{\\partial x_i \\partial x_j}$。海森矩阵描述了函数的局部曲率，可用于二阶优化方法（如牛顿法），但计算成本较高。

## A.3 概率论 (Probability Theory)

概率论用于量化不确定性，是理解 LLM 输出的随机性、评估模型性能以及许多建模方法（如 VAE）的基础。

*   **随机变量 (Random Variable):** 一个其值是随机现象数值结果的变量。
*   **概率分布 (Probability Distribution):** 描述随机变量取不同可能值的可能性。对于离散随机变量，是概率质量函数 (Probability Mass Function, PMF)；对于连续随机变量，是概率密度函数 (Probability Density Function, PDF)。
    *   **均匀分布 (Uniform Distribution):** 所有可能结果具有相同的概率。
    *   **伯努利分布 (Bernoulli Distribution):** 单次试验，只有两个可能结果（如成功/失败）。
    *   **二项分布 (Binomial Distribution):** n 次独立伯努利试验中成功次数的分布。
    *   **分类分布 (Categorical Distribution):** 单次试验，有 K 个可能结果。
    *   **多项分布 (Multinomial Distribution):** n 次独立分类试验的结果分布。
    *   **正态分布 (Normal Distribution / Gaussian Distribution):** 自然界和许多领域中常见的钟形曲线分布，由均值 $\\mu$ 和方差 $\\sigma^2$ (或标准差 $\\sigma$) 定义。
*   **联合概率 (Joint Probability):** 多个随机变量同时取特定值的概率，记作 $P(X=x, Y=y)$。
*   **边缘概率 (Marginal Probability):** 联合概率分布中，只考虑某个子集变量的概率分布。$P(X=x) = \\sum_y P(X=x, Y=y)$。
*   **条件概率 (Conditional Probability):** 在已知某个事件 Y 发生的情况下，另一个事件 X 发生的概率，记作 $P(X=x | Y=y) = \\frac{P(X=x, Y=y)}{P(Y=y)}$。
*   **贝叶斯定理 (Bayes' Theorem):** 描述了在获得新证据时如何更新对假设的信念。$P(H|E) = \\frac{P(E|H) P(H)}{P(E)}$，其中 $H$ 是假设， $E$ 是证据。$P(H)$ 是先验概率，$P(H|E)$ 是后验概率，$P(E|H)$ 是似然，$P(E)$ 是证据的边缘概率。
*   **期望 (Expectation):** 随机变量取值的加权平均值，权重为其概率。$E[X] = \\sum_x x P(x)$ (离散) 或 $E[X] = \\int x p(x) dx$ (连续)。
*   **方差 (Variance):** 衡量随机变量取值与其期望值的偏离程度。$Var(X) = E[(X - E[X])^2]$。
*   **独立性 (Independence):** 如果两个随机变量 $X$ 和 $Y$ 的联合概率等于它们各自概率的乘积 $P(X, Y) = P(X)P(Y)$，则它们是相互独立的。
*   **最大似然估计 (Maximum Likelihood Estimation, MLE):** 一种常用的参数估计方法，旨在找到一组参数 $\\theta$，使得观测到的数据 $D$ 出现的概率（似然）$P(D|\\theta)$ 最大化。LLM 的预训练通常可以看作是基于 MLE 的。

## A.4 信息论 (Information Theory)

信息论研究信息的量化、存储和通信。在 LLM 中，它常用于定义损失函数和评估模型性能。

*   **熵 (Entropy):** 衡量随机变量不确定性的度量。对于概率分布 $P(X)$，熵定义为 $H(X) = - \\sum_x P(x) \\log_b P(x)$ (通常底数 b=2，单位为比特)。熵越大，表示不确定性越高，需要的信息量越多。
*   **交叉熵 (Cross-Entropy):** 衡量使用基于概率分布 $Q$ 的编码方式来表示来自概率分布 $P$ 的样本所需的平均比特数。$H(P, Q) = - \\sum_x P(x) \\log Q(x)$。
    *   **交叉熵损失 (Cross-Entropy Loss):** 在机器学习分类任务中，交叉熵常被用作损失函数。它衡量模型预测的概率分布 $Q$ 与真实的标签分布 $P$ 之间的差异。最小化交叉熵损失等价于最大化对数似然。这是训练 LLM (如语言建模) 最常用的损失函数。
*   **KL 散度 (Kullback-Leibler Divergence):** 衡量两个概率分布 $P$ 和 $Q$ 之间差异的度量。$D_{KL}(P || Q) = \\sum_x P(x) \\log \\frac{P(x)}{Q(x)} = H(P, Q) - H(P)$。KL 散度总是非负的，当且仅当 $P=Q$ 时为零。它不是对称的 ($D_{KL}(P || Q) \\neq D_{KL}(Q || P)$)。
*   **互信息 (Mutual Information):** 衡量两个随机变量 $X$ 和 $Y$ 之间相互依赖性的度量。$I(X; Y) = \\sum_{x,y} P(x,y) \\log \\frac{P(x,y)}{P(x)P(y)} = H(X) - H(X|Y) = H(Y) - H(Y|X)$。它表示知道一个变量能提供多少关于另一个变量的信息。
*   **困惑度 (Perplexity):** 常用于评估语言模型的性能，定义为交叉熵损失的指数形式：$Perplexity(P, Q) = 2^{H(P, Q)}$。困惑度可以直观地理解为模型在预测下一个词时不确定性的平均分支因子。困惑度越低，表示模型性能越好。

掌握这些数学基础将有助于您更深入地理解本书中涉及的模型架构、训练算法和评估指标。

---