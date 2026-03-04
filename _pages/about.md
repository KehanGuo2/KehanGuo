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

I am a Ph.D. candidate in Computer Science at <a href="https://www.nd.edu/">University of Notre Dame</a> (graduating May 2027), advised by <a href="https://sites.nd.edu/xiangliang-zhang/">Prof. Xiangliang Zhang</a>. I build **RL post-training methods**, **agentic reasoning systems**, and **reward-aligned generative models** &mdash; training and evaluating at scales from 7B to 70B parameters on 64-GPU clusters.

My work focuses on the hard problems that arise when LLMs must *act*, not just *predict*: how to shape reward signals that remain informative over long horizons, how to build agents that verify their own tool-use chains before committing (multi-agent orchestration, NeurIPS 2025), and how to dynamically allocate inference-time compute to match problem difficulty (*AdaReasoner*, NeurIPS 2025 Spotlight). I use scientific reasoning as a demanding testbed &mdash; where tool errors cascade, outputs require formal verification, and benchmarks I created (NeurIPS 2023, 300+ citations; NeurIPS 2024 Spotlight) have become community standards.

<div class="cta-banner">
  <strong>Seeking Internship:</strong> I am actively looking for <strong>Research Scientist / Applied Scientist Internships</strong> for <strong>Spring / Summer / Fall 2026</strong>. I bring hands-on experience with RL post-training at scale, multi-agent system design, and inference-time reasoning. <a href="mailto:kguo2@nd.edu">Reach out &rarr;</a>
</div>

## Research

I work on four interconnected problems at the frontier of LLM capability:

**1. RL Post-Training and Reward Design.**
Policy gradient methods for LLMs struggle with sparse, delayed, or multi-objective reward signals. I develop principled reward-shaping frameworks that make RLHF-style training more stable and sample-efficient &mdash; training at 7B&ndash;70B scale on 64-GPU clusters with DeepSpeed ZeRO-3. Ongoing work establishes a formal equivalence between optimal-transport coupling in flow matching and KL-regularized RL, unifying reward-aligned generation with policy optimization.

**2. Agentic Reasoning and Structured Tool Use.**
Free-form chain-of-thought hallucinates on tasks requiring precise procedural knowledge. I build multi-agent architectures with explicit Router&ndash;Planner&ndash;Executor&ndash;Verifier pipelines where each tool call is verified before downstream steps proceed. This design dramatically improves reliability on expert-level, multi-step reasoning &mdash; and generalizes to any domain where tool errors cascade. Our orchestration framework (NeurIPS 2025) integrates 74+ structured tools; a follow-on system (6,500+ LOC, deployed) adds knowledge-graph grounding and self-evolving memory.

**3. Adaptive Inference-Time Computation.**
Not every query deserves the same compute budget. *AdaReasoner* (NeurIPS 2025 Spotlight) dynamically selects reasoning depth at inference time, reducing cost by 35% with no accuracy loss. This connects to the broader question of how to allocate test-time compute optimally &mdash; a first-order concern for deploying reasoning models at scale.

**4. Rigorous Evaluation of Frontier Models.**
Reliable progress requires reliable measurement. I have led or co-led benchmark projects that identified fundamental capability gaps in frontier models: *ChemLLMBench* (NeurIPS 2023, 300+ citations) revealed silent failure modes where models produce confident but incorrect outputs; *MolPuzzle* (NeurIPS 2024 Spotlight) exposed a multimodal perception gap (GPT-4o: 1.4% on expert tasks). These benchmarks established reference points now used across the research community.

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


## Selected Publications

See full list (20+ papers, 300+ citations) on my [Google Scholar](https://scholar.google.com/citations?user=t8iRCLUAAAAJ&hl=en)


- ![NeurIPS 2025 Spotlight](https://img.shields.io/badge/NeurIPS_Spotlight-2025-blue?style=plastic) [AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking](https://arxiv.org/abs/2505.17312), X Wang, Y Huang, Y Wang, X Luo, **Kehan Guo**, Y Zhou, X Zhang

- ![NeurIPS 2024 Spotlight](https://img.shields.io/badge/NeurIPS_Spotlight-2024-blue?style=plastic) [Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://kehanguo2.github.io/Molpuzzle.io/), **Kehan Guo**, B Nan, Y Zhou, T Guo, Z Guo, M Surve, Z Liang, N Chawla, O Wiest, X Zhang [**Code**](https://github.com/KehanGuo2/MolPuzzle) [![](https://img.shields.io/github/stars/KehanGuo2/MolPuzzle)](https://github.com/KehanGuo2/MolPuzzle)

- ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-blue?style=plastic) [ChemOrch: Empowering LLMs with Chemical Intelligence via Synthetic Instructions](https://arxiv.org/abs/2509.16543), Y Huang, Z Jiang, X Luo, **Kehan Guo**, H Zhuang, Y Zhou, Z Yuan, X Sun, J Schleinitz, Y Wang, S Zhang, M Surve, N Chawla, O Wiest, X Zhang

- ![ArXiv 2025](https://img.shields.io/badge/ArXiv-2025-b31b1b?style=plastic) [Evaluating Large Language Models in Scientific Discovery](https://arxiv.org/abs/2512.15567), **Kehan Guo**\*, [Co-authors]\*, ...

- ![IJCAI 2025](https://img.shields.io/badge/IJCAI-2025-%232F4F4F?style=plastic&logoColor=%2387CEFA) [Artificial Intelligence in Spectroscopy: Advancing Chemistry from Prediction to Generation and Beyond](https://arxiv.org/pdf/2502.09897), **Kehan Guo**, Y Shen, G Gonzalez-Montiel, Y Huang, Y Zhou, M Surve, Z Guo, ... &mdash; *Survey*

- ![NeurIPS 2023](https://img.shields.io/badge/NeurIPS-2023-blue?style=plastic) [What can Large Language Models do in chemistry? A comprehensive benchmark on eight tasks](https://github.com/ChemFoundationModels/ChemLLMBench), T Guo\*, **Kehan Guo**\*, B Nan, Z Liang, Z Guo, N Chawla, O Wiest, X Zhang &mdash; *300+ citations* [**Code**](https://github.com/ChemFoundationModels/ChemLLMBench) [![](https://img.shields.io/github/stars/ChemFoundationModels/ChemLLMBench)](https://github.com/ChemFoundationModels/ChemLLMBench)

- ![ACL 2025](https://img.shields.io/badge/ACL-2025-blue?style=plastic) [SEUF: Is Unlearning One Expert Enough for Mixture-of-Experts LLMs?](https://arxiv.org/abs/2411.18797), H Zhuang, Y Zhang, **Kehan Guo**, J Jia, G Liu, S Liu, X Zhang

- ![ACL Findings 2025](https://img.shields.io/badge/ACL_Findings-2025-blue?style=plastic) [Beyond Single-Value Metrics: Evaluating and Enhancing LLM Unlearning with Cognitive Diagnosis](https://arxiv.org/abs/2502.13996), Y Lang, **Kehan Guo**, Y Huang, Y Zhou, H Zhuang, T Yang, Y Su, X Zhang

- ![Nature Comms Chem 2025](https://img.shields.io/badge/Comms_Chem-2025-green?style=plastic) [Unveiling the Power of Language Models in Chemical Research Question Answering](https://www.nature.com/articles/s42004-024-01397-x), X Chen, T Wang, T Guo, **Kehan Guo**, J Zhou, H Li, Z Song, X Gao, X Zhang

- ![EMNLP 2024](https://img.shields.io/badge/EMNLP-2024-purple?style=plastic) [Defending Jailbreak Prompts via In-Context Adversarial Game](https://arxiv.org/abs/2402.13148), Y Zhou, Y Han, H Zhuang, **Kehan Guo**, Z Liang, H Bao, X Zhang

- ![ACL 2024](https://img.shields.io/badge/ACL-2024-blue?style=plastic) [SceMQA: A Scientific College Entrance Level Multimodal Question Answering Benchmark](https://scemqa.github.io/), Z Liang, **Kehan Guo**, G Liu, T Guo, Y Zhou, T Yang, J Jiao, R Pi, J Zhang, ...

- ![AAAI 2024](https://img.shields.io/badge/AAAI-2024-orange?style=plastic) [Uncertainty-Aware Yield Prediction with Multimodal Molecular Features](https://ojs.aaai.org/index.php/AAAI/article/view/28668), J Chen, **Kehan Guo**, Z Liu, O Isayev, X Zhang

- ![IJCAI 2023](https://img.shields.io/badge/IJCAI-2023-%232F4F4F?style=plastic) [Graph-based Molecular Representation Learning](https://arxiv.org/abs/2207.04869), Z Guo, **Kehan Guo**, B Nan, Y Tian, R Iyer, Y Ma, O Wiest, X Zhang, W Wang, ...


# Education
- *2022.09 - 2027.05 (Expected)*, Ph.D, <img src='images/Notre_Dame.png' class='inline-icon'> [University of Notre Dame](https://www.nd.edu/) &mdash; Advisor: Prof. Xiangliang Zhang
- *2020.09 - 2022.05*, M.S, <img src='images/bu.png' class='inline-icon'> [Boston University](https://www.bu.edu/)


# Awards
- *2025* NeurIPS Spotlight (top ~3%) &mdash; *AdaReasoner*
- *2024* NeurIPS Spotlight (top ~3%) &mdash; *MolPuzzle*
- *2024* OpenAI Researcher Access Program


# Professional Service
- **Reviewer:** NeurIPS (2024&ndash;25), ICLR (2025&ndash;26), ICML, AAAI, IJCAI, KDD, ACL Rolling Review, WWW, EMNLP
