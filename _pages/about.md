---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<div class='anchor' id='about-me'></div>

I am a Ph.D. candidate in Computer Science at <a href="https://www.nd.edu/">University of Notre Dame</a> (graduating May 2027), advised by <a href="https://sites.nd.edu/xiangliang-zhang/">Prof. Xiangliang Zhang</a>. I build **RL post-training methods**, **agentic reasoning systems**, and **reward-aligned generative models**.

My work focuses on the hard problems that arise when LLMs must *act*, not just *predict*: how to shape reward signals that remain informative over long horizons, how to build agents that verify their own tool-use chains before committing (multi-agent orchestration, NeurIPS 2025), and how to dynamically allocate inference-time compute to match problem difficulty (*AdaReasoner*, NeurIPS 2025 Spotlight). I use scientific reasoning as a demanding testbed &mdash; where tool errors cascade, outputs require formal verification, and benchmarks I created (NeurIPS 2023, 300+ citations; NeurIPS 2024 Spotlight) have become community standards.

<div class="cta-banner">
  <strong>Seeking Internship:</strong> I am actively looking for <strong>Research Scientist / Applied Scientist Internships</strong> for <strong>Spring / Summer / Fall 2026</strong>. I bring hands-on experience with RL post-training at scale, multi-agent system design, and inference-time reasoning. <a href="mailto:kguo2@nd.edu">Reach out &rarr;</a>
</div>

## Research

**1. RL Post-Training and Inference-Time Reasoning.**
I develop methods that improve LLM behavior through reinforcement learning &mdash; at both training time and inference time. This includes principled reward-shaping frameworks for stable policy optimization ([CEPO](https://arxiv.org/abs/2509.23095)), adaptive inference-time reasoning that dynamically selects computation depth to reduce cost by 35% with no accuracy loss ([AdaReasoner](https://arxiv.org/abs/2505.17312), NeurIPS 2025 Spotlight), and ongoing work unifying reward-aligned generation with KL-regularized RL via optimal-transport coupling.

**2. Agentic Reasoning and Structured Tool Use.**
I build multi-agent architectures with explicit Router&ndash;Planner&ndash;Executor&ndash;Verifier pipelines where each tool call is verified before downstream steps proceed. Our orchestration framework ([ChemOrch](https://arxiv.org/abs/2509.16543), NeurIPS 2025) integrates 74+ structured tools and dramatically improves reliability on expert-level, multi-step reasoning. A follow-on system adds knowledge-graph grounding and self-evolving memory.

**3. Rigorous Evaluation of Frontier Models.**
I have led or co-led benchmark projects that identified fundamental capability gaps: [ChemLLMBench](https://github.com/ChemFoundationModels/ChemLLMBench) (NeurIPS 2023, 300+ citations) revealed silent failure modes in LLMs; [MolPuzzle](https://kehanguo2.github.io/Molpuzzle.io/) (NeurIPS 2024 Spotlight) exposed a multimodal perception gap (GPT-4o: 1.4% on expert tasks). These benchmarks are now community standards.

## News

<ul class="news-list">
  <li><strong>Seeking Internship:</strong> Actively looking for <strong>Research Scientist / Applied Scientist Internships</strong> for Spring/Summer/Fall 2026 &mdash; RL post-training, agentic systems, inference-time reasoning. <a href="mailto:kguo2@nd.edu">Reach out!</a></li>
  <li><strong>2026.03:</strong> Passed <strong>Ph.D. Candidacy Exam</strong>. Officially a Ph.D. candidate!</li>
  <li><strong>2025.12:</strong> New preprint: co-first author on <a href="https://arxiv.org/abs/2512.15567">Evaluating Large Language Models in Scientific Discovery</a> &mdash; a comprehensive multi-domain assessment across 10 scientific fields.</li>
  <li><strong>2025.09:</strong> Two papers accepted at <strong>NeurIPS 2025</strong>: <strong>ChemOrch</strong> (multi-agent orchestration for chemistry) and <em>AdaReasoner</em> (<span class="accent-highlight">Spotlight</span>, adaptive inference-time reasoning).</li>
  <li><strong>2025.08:</strong> Completed Applied Scientist Internship at <strong>Amazon AWS AI (Deep Engine Team)</strong> in NYC.</li>
  <li><strong>2025.04:</strong> Survey paper accepted at <strong>IJCAI 2025</strong> (Survey Track): <em>AI in Spectroscopy</em>.</li>
  <li><strong>2024.12:</strong> Selected for <strong>OpenAI Researcher Access Program</strong>.</li>
  <li><strong>2024.09:</strong> <a href="https://github.com/KehanGuo2/MolPuzzle">MolPuzzle</a> accepted at <em>NeurIPS 2024 Dataset and Benchmark Track</em> as <span class="accent-highlight">Spotlight</span> (top ~3%).</li>
  <li><strong>2024.09:</strong> One paper accepted at main conference of <strong>EMNLP 2024</strong>.</li>
  <li><strong>2024.06:</strong> Passed Ph.D. Qualification exam.</li>
  <li><strong>2023.09:</strong> First-author paper accepted at <strong>NeurIPS 2023</strong>: <em>ChemLLMBench</em> (300+ citations).</li>
</ul>


## Selected Publications ([Full Publications](https://scholar.google.com/citations?user=t8iRCLUAAAAJ&hl=en))

<div class="pub-entry">
  <div class="pub-title"><a href="https://kehanguo2.github.io/Molpuzzle.io/">Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation</a></div>
  <div class="pub-authors"><strong>Kehan Guo</strong>, Bozhao Nan, Yujun Zhou, Taicheng Guo, Zhichun Guo, Mihir Surve, Zhenwen Liang, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang</div>
  <div class="pub-venue"><em>NeurIPS</em>, 2024. <strong>Spotlight.</strong> <a href="https://kehanguo2.github.io/Molpuzzle.io/">[Paper]</a> &nbsp;<a href="https://github.com/KehanGuo2/MolPuzzle">[Code]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://github.com/ChemFoundationModels/ChemLLMBench">What can Large Language Models do in chemistry? A comprehensive benchmark on eight tasks</a></div>
  <div class="pub-authors">Taicheng Guo*, <strong>Kehan Guo</strong>*, Bozhao Nan, Zhenwen Liang, Zhichun Guo, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang</div>
  <div class="pub-venue"><em>NeurIPS</em>, 2023. 300+ citations. <a href="https://github.com/ChemFoundationModels/ChemLLMBench">[Paper]</a> &nbsp;<a href="https://github.com/ChemFoundationModels/ChemLLMBench">[Code]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://arxiv.org/abs/2512.15567">Evaluating Large Language Models in Scientific Discovery</a></div>
  <div class="pub-authors"><strong>Kehan Guo</strong>*, Ziqian Song*, Jiuding Lu*, and others</div>
  <div class="pub-venue"><em>arXiv preprint</em>, 2025. <a href="https://arxiv.org/abs/2512.15567">[Paper]</a> &nbsp;<a href="https://github.com/deepprinciple/lm-evaluation-harness/tree/main">[Code]</a> &nbsp;<a href="https://huggingface.co/deep-principle/datasets">[Dataset]</a> &nbsp;<a href="https://github.com/HowieHwong/sde-harness">[Oracle]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://arxiv.org/pdf/2502.09897">Artificial Intelligence in Spectroscopy: Advancing Chemistry from Prediction to Generation and Beyond</a></div>
  <div class="pub-authors"><strong>Kehan Guo</strong>, Yifan Shen, Gil A. Gonzalez-Montiel, Yue Huang, Yujun Zhou, Mihir Surve, Zhichun Guo, ...</div>
  <div class="pub-venue"><em>IJCAI</em>, 2025. Survey Track. <a href="https://arxiv.org/pdf/2502.09897">[Paper]</a> &nbsp;<a href="https://github.com/MINE-Lab-ND/SpectrumML_Survey_Papers">[Code]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://arxiv.org/abs/2505.17312">AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking</a></div>
  <div class="pub-authors">Xiangqi Wang, Yue Huang, Yanbo Wang, Xiaonan Luo, <strong>Kehan Guo</strong>, Yujun Zhou, Xiangliang Zhang</div>
  <div class="pub-venue"><em>NeurIPS</em>, 2025. <strong>Spotlight.</strong> <a href="https://arxiv.org/abs/2505.17312">[Paper]</a> &nbsp;<a href="https://github.com/XiangqiWang77/officialadareasoner">[Code]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://arxiv.org/abs/2509.16543">ChemOrch: Empowering LLMs with Chemical Intelligence via Synthetic Instructions</a></div>
  <div class="pub-authors">Yue Huang, Zhengzhe Jiang, Xiaonan Luo, <strong>Kehan Guo</strong>, Haomin Zhuang, Yujun Zhou, Zhengqing Yuan, Xiaoqi Sun, Jules Schleinitz, Yanbo Wang, Shuhao Zhang, Mihir Surve, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang</div>
  <div class="pub-venue"><em>NeurIPS</em>, 2025. <a href="https://arxiv.org/abs/2509.16543">[Paper]</a> &nbsp;<a href="https://github.com/HowieHwong/ChemOrch">[Code]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://arxiv.org/abs/2509.23095">Causally-Enhanced Reinforcement Policy Optimization</a></div>
  <div class="pub-authors">Xiangqi Wang, Yue Huang, Yujun Zhou, Xiaonan Luo, <strong>Kehan Guo</strong>, Xiangliang Zhang</div>
  <div class="pub-venue"><em>arXiv preprint</em>, 2025. <a href="https://arxiv.org/abs/2509.23095">[Paper]</a> &nbsp;<a href="https://github.com/XiangqiWang77/causalrl">[Code]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://arxiv.org/abs/2411.18797">SEUF: Is Unlearning One Expert Enough for Mixture-of-Experts LLMs?</a></div>
  <div class="pub-authors">Haomin Zhuang, Yizhuo Zhang, <strong>Kehan Guo</strong>, Jinghan Jia, Gang Liu, Sijia Liu, Xiangliang Zhang</div>
  <div class="pub-venue"><em>ACL</em>, 2025. <a href="https://arxiv.org/abs/2411.18797">[Paper]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://arxiv.org/abs/2502.13996">Beyond Single-Value Metrics: Evaluating and Enhancing LLM Unlearning with Cognitive Diagnosis</a></div>
  <div class="pub-authors">Yuang Lang, <strong>Kehan Guo</strong>, Yue Huang, Yujun Zhou, Haomin Zhuang, Tianyu Yang, Yuxuan Su, Xiangliang Zhang</div>
  <div class="pub-venue"><em>ACL Findings</em>, 2025. <a href="https://arxiv.org/abs/2502.13996">[Paper]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://www.nature.com/articles/s42004-024-01397-x">Unveiling the Power of Language Models in Chemical Research Question Answering</a></div>
  <div class="pub-authors">Xiuying Chen, Tairan Wang, Taicheng Guo, <strong>Kehan Guo</strong>, Jingwei Zhou, Hualin Li, Ziqian Song, Xiang Gao, Xiangliang Zhang</div>
  <div class="pub-venue"><em>Communications Chemistry</em>, 2025. <a href="https://www.nature.com/articles/s42004-024-01397-x">[Paper]</a> &nbsp;<a href="https://github.com/iriscxy/chemmatch">[Code]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://arxiv.org/abs/2402.13148">Defending Jailbreak Prompts via In-Context Adversarial Game</a></div>
  <div class="pub-authors">Yujun Zhou, Yufei Han, Haomin Zhuang, <strong>Kehan Guo</strong>, Zhenwen Liang, Hongyan Bao, Xiangliang Zhang</div>
  <div class="pub-venue"><em>EMNLP</em>, 2024. <a href="https://arxiv.org/abs/2402.13148">[Paper]</a> &nbsp;<a href="https://github.com/YujunZhou/In-Context-Adversarial-Game">[Code]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://scemqa.github.io/">SceMQA: A Scientific College Entrance Level Multimodal Question Answering Benchmark</a></div>
  <div class="pub-authors">Zhenwen Liang, <strong>Kehan Guo</strong>, Gang Liu, Taicheng Guo, Yujun Zhou, Tianyu Yang, Jiajun Jiao, Renjie Pi, Jipeng Zhang, ...</div>
  <div class="pub-venue"><em>ACL</em>, 2024. <a href="https://scemqa.github.io/">[Paper]</a> &nbsp;<a href="https://github.com/SceMQA/SceMQA">[Code]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/28668">Uncertainty-Aware Yield Prediction with Multimodal Molecular Features</a></div>
  <div class="pub-authors">Jiayuan Chen, <strong>Kehan Guo</strong>, Zhen Liu, Olexandr Isayev, Xiangliang Zhang</div>
  <div class="pub-venue"><em>AAAI</em>, 2024. <a href="https://ojs.aaai.org/index.php/AAAI/article/view/28668">[Paper]</a> &nbsp;<a href="https://github.com/jychen229/Multimodal-reaction-yield-prediction">[Code]</a></div>
</div>

<div class="pub-entry">
  <div class="pub-title"><a href="https://arxiv.org/abs/2207.04869">Graph-based Molecular Representation Learning</a></div>
  <div class="pub-authors">Zhichun Guo, <strong>Kehan Guo</strong>, Bozhao Nan, Yijun Tian, Roshni G. Iyer, Yihong Ma, Olaf Wiest, Xiangliang Zhang, Wei Wang, ...</div>
  <div class="pub-venue"><em>IJCAI</em>, 2023. <a href="https://arxiv.org/abs/2207.04869">[Paper]</a></div>
</div>


# Education
- *2022.09 - 2027.05 (Expected)*, Ph.D, <img src='images/Notre_Dame.png' class='inline-icon'> [University of Notre Dame](https://www.nd.edu/) &mdash; Advisor: Prof. Xiangliang Zhang
- *2020.09 - 2022.05*, M.S, <img src='images/bu.png' class='inline-icon'> [Boston University](https://www.bu.edu/)


# Awards
- *2025* NeurIPS Spotlight (top ~3%) &mdash; *AdaReasoner*
- *2024* NeurIPS Spotlight (top ~3%) &mdash; *MolPuzzle*
- *2024* OpenAI Researcher Access Program


# Professional Service
- **Reviewer:** NeurIPS (2024&ndash;25), ICLR (2025&ndash;26), ICML, AAAI, IJCAI, KDD, ACL Rolling Review, WWW, EMNLP
