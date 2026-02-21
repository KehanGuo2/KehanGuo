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

<span class='anchor' id='about-me'>

I am a Ph.D. candidate in Computer Science at <a href="https://www.nd.edu/">University of Notre Dame</a> (graduating May 2027), advised by <a href="https://sites.nd.edu/xiangliang-zhang/">Prof. Xiangliang Zhang</a> in the <a href="https://sites.nd.edu/xiangliang-zhang/">MINE Lab</a>.

My research sits at the intersection of **RL post-training**, **LLM agents**, and **AI for Science**. I build systems that go beyond next-token prediction: agents that use structured tools, verify their own reasoning, and adapt their compute budget to problem difficulty.

<div class="cta-banner">
  <strong>Seeking Internship:</strong> I am actively looking for <strong>Research Scientist / Applied Scientist Internships</strong> for <strong>Spring / Summer / Fall 2026</strong>. If my work resonates with your team, please reach out at <a href="mailto:kguo2@nd.edu">kguo2@nd.edu</a>.
</div>

</span>

## Research

**RL Post-Training.** Principled reward shaping for stable policy gradient updates. Social-Choice GRPO applies social choice aggregation to implicit rollout preferences, extracting dense training signal without additional human annotation.

**LLM Agents.** Structured tool use with verification at each boundary. ChemOrch (NeurIPS 2025) integrates 74+ domain-specific tools in a neuro-symbolic loop that dramatically improves reliability on expert-level multi-step tasks.

**Evaluation.** Three benchmark projects identifying capability gaps in frontier models. 600+ citations across ChemLLMBench (NeurIPS 2023), MolPuzzle (NeurIPS 2024 Spotlight), and a Scientific Discovery evaluation suite.

<div class="research-figure">
  <img src="images/research_architecture.jpg" alt="The Neuro-Symbolic Loop Architecture">
  <p><strong>Figure 1: The Neuro-Symbolic Loop.</strong> Architecture for <em>ChemOrch</em> (NeurIPS '25), integrating a Multi-Agent Workforce with a Unified World Graph.</p>
</div>


## News

<ul class="news-list">
  <li><strong>Seeking Internship:</strong> Actively looking for <strong>Research Scientist / Applied Scientist Internships</strong> for Spring/Summer/Fall 2026. <a href="mailto:kguo2@nd.edu">Reach out!</a></li>
  <li><strong>2025.12:</strong> New preprint: co-first author on <a href="https://arxiv.org/abs/2512.15567">Evaluating Large Language Models in Scientific Discovery</a> &mdash; a comprehensive multi-domain assessment across 10 scientific fields.</li>
  <li><strong>2025.09:</strong> Two papers accepted at <strong>NeurIPS 2025</strong>: <strong>ChemOrch</strong> (multi-agent orchestration for chemistry) and <em>AdaReasoner</em> (<span class="accent-highlight">Spotlight</span>, adaptive inference-time reasoning).</li>
  <li><strong>2025.08:</strong> Completed Applied Scientist Internship at <strong>Amazon AWS AI (Deep Engine Team)</strong> in NYC.</li>
  <li><strong>2025.04:</strong> Survey paper accepted at <strong>IJCAI 2025</strong> (Survey Track): <em>AI in Spectroscopy</em>.</li>
  <li><strong>2024.12:</strong> Selected for <strong>OpenAI Researcher Access Program</strong>.</li>
  <li><strong>2024.09:</strong> <a href="https://github.com/KehanGuo2/MolPuzzle">MolPuzzle</a> accepted at <em>NeurIPS 2024 Dataset and Benchmark Track</em> as <span class="accent-highlight">Spotlight</span> (top ~3%).</li>
  <li><strong>2024.09:</strong> One paper accepted at main conference of <strong>EMNLP 2024</strong>.</li>
  <li><strong>2024.06:</strong> Passed Ph.D. Qualification exam.</li>
  <li><strong>2023.09:</strong> First-author paper accepted at <strong>NeurIPS 2023</strong>: <em>ChemLLMBench</em> (600+ citations).</li>
</ul>


## Selected Publications

See full list (20+ papers, 600+ citations) on my [Google Scholar](https://scholar.google.com/citations?user=t8iRCLUAAAAJ&hl=en)


- ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-blue) [AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking](https://arxiv.org/abs/2505.17312), Xiangqi Wang, Yue Huang, Yanbo Wang, Xiaonan Luo, **Kehan Guo**, Yujun Zhou, Xiangliang Zhang &mdash; *NeurIPS 2025 Spotlight*


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024 Spotlight</div><img src='images/intro_spectrum.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![NeurIPS 2024](https://img.shields.io/badge/NeurIPS-2024-2024) [Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://kehanguo2.github.io/Molpuzzle.io/)

**Kehan Guo**, Bozhao Nan, Yujun Zhou, Taicheng Guo, Zhichun Guo, Mihir Surve, Zhenwen Liang, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang

[**Code**](https://github.com/KehanGuo2/MolPuzzle) [![](https://img.shields.io/github/stars/KehanGuo2/MolPuzzle)](https://github.com/KehanGuo2/MolPuzzle)

</div>
</div>


- ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-blue) [ChemOrch: Empowering LLMs with Chemical Intelligence via Synthetic Instructions](https://arxiv.org/abs/2509.16543), Yue Huang, Zhengzhe Jiang, Xiaonan Luo, **Kehan Guo**, Haomin Zhuang, Yujun Zhou, Zhengqing Yuan, Xiaoqi Sun, Jules Schleinitz, Yanbo Wang, Shuhao Zhang, Mihir Surve, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang &mdash; *NeurIPS 2025*


- ![ArXiv 2025](https://img.shields.io/badge/ArXiv-2025-b31b1b) [Evaluating Large Language Models in Scientific Discovery](https://arxiv.org/abs/2512.15567), **Kehan Guo**\*, [Co-authors]\*, ... &mdash; *Co-First Author, Comprehensive multi-domain benchmark for AI in Science*


- ![IJCAI 2025](https://img.shields.io/badge/IJCAI-2025-%232F4F4F?style=plastic&logoColor=%2387CEFA) [Artificial Intelligence in Spectroscopy: Advancing Chemistry from Prediction to Generation and Beyond](https://arxiv.org/pdf/2502.09897), **Kehan Guo**, Yifan Shen, Gil A. Gonzalez-Montiel, Yue Huang, Yujun Zhou, Mihir Surve, Zhichun Guo, ... &mdash; *Survey*


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2023</div><img src='images/llmchem.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![NeurIPS 2023](https://img.shields.io/badge/NeurIPS-2023-2023) [What can Large Language Models do in chemistry? A comprehensive benchmark on eight tasks](https://github.com/ChemFoundationModels/ChemLLMBench)

Taicheng Guo\*, **Kehan Guo**\*, Bozhao Nan, Zhenwen Liang, Zhichun Guo, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang

[**Code**](https://github.com/ChemFoundationModels/ChemLLMBench) [![](https://img.shields.io/github/stars/ChemFoundationModels/ChemLLMBench)](https://github.com/ChemFoundationModels/ChemLLMBench)

*600+ citations. The first comprehensive LLM evaluation for chemistry.*

</div>
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

<div class="map-container">
<script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=j0c1_fHIloUhG4VJOq9LgaxK6GKOZ6MwrAZbEqZLjM4&cl=ffffff&w=a"></script>
</div>
