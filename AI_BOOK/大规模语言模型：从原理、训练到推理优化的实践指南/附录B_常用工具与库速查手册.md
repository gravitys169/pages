# 附录B：常用工具与库速查手册 (Toolkit and Library Quick Reference)

本附录汇总了在大型语言模型（LLM）的研究、开发、训练和部署过程中常用到的一些核心工具、库和框架。这些资源在本书的不同章节中有所提及，这里提供一个集中的速查列表，包含简要说明和官方链接（如果适用）。

## B.1 核心深度学习框架

*   **PyTorch:**
    *   **描述:** 目前最流行的深度学习框架之一，以其灵活性、易用性和强大的社区支持而闻名。广泛应用于 LLM 的研究和开发。
    *   **官网:** [https://pytorch.org/](https://pytorch.org/)
*   **JAX:**
    *   **描述:** Google 开发的高性能数值计算库，结合了 Autograd（自动微分）和 XLA（加速线性代数）编译器。特别适合大规模分布式训练和研究，以其函数式编程风格和高效的 TPU 支持著称。
    *   **官网:** [https://github.com/google/jax](https://github.com/google/jax)
*   **TensorFlow:**
    *   **描述:** Google 开发的另一个主流深度学习框架，拥有成熟的生态系统和强大的生产部署能力 (TensorFlow Serving, TensorFlow Lite)。
    *   **官网:** [https://www.tensorflow.org/](https://www.tensorflow.org/)

## B.2 Hugging Face 生态系统

*   **Transformers:**
    *   **描述:** Hugging Face 的核心库，提供了数千个预训练模型（包括众多 LLM）、易于使用的模型加载、训练、推理接口，以及 Tokenizer 等工具。是 LLM 领域的事实标准库之一。
    *   **官网:** [https://huggingface.co/docs/transformers/index](https://huggingface.co/docs/transformers/index)
*   **Datasets:**
    *   **描述:** 提供对数千个常用数据集的标准化访问接口，支持高效的数据加载、预处理和流式处理。
    *   **官网:** [https://huggingface.co/docs/datasets/](https://huggingface.co/docs/datasets/)
*   **Tokenizers:**
    *   **描述:** 高效的 Tokenizer 实现库，支持 BPE, WordPiece, SentencePiece 等主流算法，并提供训练自定义 Tokenizer 的功能。
    *   **官网:** [https://huggingface.co/docs/tokenizers/index](https://huggingface.co/docs/tokenizers/index)
*   **Accelerate:**
    *   **描述:** 简化 PyTorch 分布式训练和混合精度训练的库，只需少量代码修改即可在不同硬件配置（单卡、多卡、多节点、TPU）上运行训练脚本。
    *   **官网:** [https://huggingface.co/docs/accelerate/index](https://huggingface.co/docs/accelerate/index)
*   **PEFT (Parameter-Efficient Fine-Tuning):**
    *   **描述:** 集成了多种参数高效微调方法的库，如 LoRA, Prefix Tuning, Prompt Tuning, AdaLoRA 等，可以方便地对大模型进行低成本微调。
    *   **官网:** [https://github.com/huggingface/peft](https://github.com/huggingface/peft)
*   **Evaluate:**
    *   **描述:** 提供各种常用的机器学习评估指标（如 Accuracy, F1, BLEU, ROUGE, Perplexity）以及基准测试的加载和计算接口。
    *   **官网:** [https://huggingface.co/docs/evaluate/index](https://huggingface.co/docs/evaluate/index)
*   **TGI (Text Generation Inference):**
    *   **描述:** Hugging Face 开发的高性能文本生成推理服务器，专为 LLM 设计，支持连续批处理、张量并行、量化等优化。
    *   **官网:** [https://github.com/huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference)
*   **Transformers Agent:**
    *   **描述:** 允许 LLM 调用 Hugging Face 生态中其他模型和工具的实验性 Agent 框架。
    *   **文档:** [https://huggingface.co/docs/transformers/main/en/transformers_agents](https://huggingface.co/docs/transformers/main/en/transformers_agents)

## B.3 分布式训练框架

*   **DeepSpeed:**
    *   **描述:** Microsoft 开发的深度学习优化库，专注于大规模模型训练，提供了 ZeRO 系列显存优化技术、高效的分布式训练策略（DP, TP, PP）、MoE 支持以及推理优化功能。
    *   **官网:** [https://github.com/microsoft/DeepSpeed](https://github.com/microsoft/DeepSpeed)
*   **Megatron-LM:**
    *   **描述:** NVIDIA 开发的大规模 Transformer 模型训练框架，以其高效的张量并行 (TP) 和流水线并行 (PP) 实现而闻名。
    *   **官网:** [https://github.com/NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
*   **PyTorch FSDP (Fully Sharded Data Parallel):**
 