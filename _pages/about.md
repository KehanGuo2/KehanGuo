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

<span class='anchor' id='about-me' style="font-size: 16px;">

I am a Ph.D. candidate in Computer Science at <a href="https://www.nd.edu/">University of Notre Dame</a> (graduating May 2027), advised by <a href="https://sites.nd.edu/xiangliang-zhang/">Prof. Xiangliang Zhang</a> in the <a href="https://sites.nd.edu/xiangliang-zhang/">MINE Lab</a>.

My research sits at the intersection of <strong>RL post-training</strong>, <strong>LLM agents</strong>, and <strong>AI for Science</strong>. I build systems that go beyond next-token prediction: agents that use structured tools, verify their own reasoning, and adapt their compute budget to problem difficulty. At <strong>Amazon AWS AI</strong> (Summer 2025), I developed <strong>Social-Choice GRPO</strong>, a reward shaping framework achieving an <strong>8.9% relative accuracy gain on BBEH</strong> over PPO baselines. 

<blockquote style="font-size: 16px; line-height: 1.6;">
I am actively seeking <strong>Research Scientist / Applied Scientist Internships</strong> for <strong>Spring / Summer / Fall 2026</strong>. If my work resonates with your team, please reach out at <a href="mailto:kguo2@nd.edu">kguo2@nd.edu</a>.
</blockquote>

</span>


&#128300; Research
------

I work on three interconnected problems:

<div style="font-size: 15px; line-height: 1.7;">

<p><strong>RL Post-Training and Reward Design.</strong>
Standard RLHF struggles with sparse, delayed, or ambiguous reward signals on long-horizon reasoning tasks. I develop principled reward shaping methods that make policy gradient updates more stable and sample-efficient. My <em>Social-Choice GRPO</em> framework applies social choice aggregation to implicit rollout preferences, extracting dense training signal without additional human annotation.</p>

<p><strong>LLM Agents with Structured Tool Use.</strong>
Free-form chain-of-thought hallucinates on tasks requiring precise procedural knowledge. My <em>ChemOrch</em> system (NeurIPS 2025) integrates 74+ domain-specific tools into a structured reasoning loop where each tool call is verified before downstream steps proceed &mdash; a neuro-symbolic design that dramatically improves reliability on expert-level multi-step tasks. This architecture generalizes beyond chemistry to any domain where tool errors cascade.</p>

<p><strong>Rigorous Evaluation and Benchmarking.</strong>
I have led or co-led three benchmark projects &mdash; <em>ChemLLMBench</em> (NeurIPS 2023, 600+ citations), <em>MolPuzzle</em> (NeurIPS 2024 Spotlight), and a Scientific Discovery evaluation suite &mdash; that identified fundamental capability gaps in frontier models and established reference points for the AI-for-Science community.</p>

</div>

<div style="text-align: center; margin: 20px 0;">
  <img src="images/research_architecture.jpg" alt="The Neuro-Symbolic Loop Architecture" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
  <p style="font-size: 14px; color: #555; margin-top: 12px;"><strong>Figure 1: The Neuro-Symbolic Loop.</strong> Architecture for <em>ChemOrch</em> (NeurIPS '25), integrating a Multi-Agent Workforce with a Unified World Graph.</p>
</div>


&#128293; News
------

<ul style="font-size: 16px; line-height: 1.8; list-style-type: disc; padding-left: 20px;">
  <li><strong>Seeking Internship:</strong> Actively looking for <strong>Research Scientist / Applied Scientist Internships</strong> for Spring/Summer/Fall 2026. <a href="mailto:kguo2@nd.edu">Reach out!</a></li>
  <li><strong>2025.12:</strong> New preprint: co-first author on <a href="https://arxiv.org/abs/2512.15567">Evaluating Large Language Models in Scientific Discovery</a> &mdash; a comprehensive multi-domain assessment across 10 scientific fields.</li>
  <li><strong>2025.09:</strong> Two papers accepted at <strong>NeurIPS 2025</strong>: <strong>ChemOrch</strong> (multi-agent orchestration for chemistry) and <em>AdaReasoner</em> (<span style="color: #e74c3c;">Spotlight</span>, adaptive inference-time reasoning).</li>
  <li><strong>2025.08:</strong> Completed Applied Scientist Internship at <strong>Amazon AWS AI (Deep Engine Team)</strong> in NYC. Developed Social-Choice GRPO; 8.9% gain on BBEH.</li>
  <li><strong>2025.04:</strong> Survey paper accepted at <strong>IJCAI 2025</strong> (Survey Track): <em>AI in Spectroscopy</em>.</li>
  <li><strong>2024.12:</strong> Selected for <strong>OpenAI Researcher Access Program</strong>.</li>
  <li><strong>2024.09:</strong> <a href="https://github.com/KehanGuo2/MolPuzzle">MolPuzzle</a> accepted at <em>NeurIPS 2024 Dataset and Benchmark Track</em> as <span style="color: #e74c3c;">Spotlight</span> (top ~3%).</li>
  <li><strong>2024.09:</strong> One paper accepted at main conference of <strong>EMNLP 2024</strong>.</li>
  <li><strong>2024.06:</strong> Passed Ph.D. Qualification exam.</li>
  <li><strong>2023.09:</strong> First-author paper accepted at <strong>NeurIPS 2023</strong>: <em>ChemLLMBench</em> (600+ citations).</li>
</ul>


&#128206; Selected Publications
------
See full list (20+ papers, 600+ citations) on my [Google Scholar](https://scholar.google.com/citations?user=t8iRCLUAAAAJ&hl=en)


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025 Spotlight</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-blue) [AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking](https://arxiv.org/abs/2505.17312)

Xiangqi Wang, Yue Huang, Yanbo Wang, Xiaonan Luo, **Kehan Guo**, Yujun Zhou, Xiangliang Zhang

*Adaptive inference-time reasoning via dynamic depth selection. Reduces inference cost by 35% with no accuracy loss.*

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024 Spotlight</div><img src='images/intro_spectrum.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![NeurIPS 2024](https://img.shields.io/badge/NeurIPS-2024-2024) [Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://kehanguo2.github.io/Molpuzzle.io/)

**Kehan Guo**, Bozhao Nan, Yujun Zhou, Taicheng Guo, Zhichun Guo, Mihir Surve, Zhenwen Liang, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang

[**Code**](https://github.com/KehanGuo2/MolPuzzle) [![](https://img.shields.io/github/stars/KehanGuo2/MolPuzzle)](https://github.com/KehanGuo2/MolPuzzle)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-blue) [ChemOrch: Empowering LLMs with Chemical Intelligence via Synthetic Instructions](https://arxiv.org/abs/2509.16543)

Yue Huang, Zhengzhe Jiang, Xiaonan Luo, **Kehan Guo**, Haomin Zhuang, Yujun Zhou, Zhengqing Yuan, Xiaoqi Sun, Jules Schleinitz, Yanbo Wang, Shuhao Zhang, Mihir Surve, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang

*Mentored project: multi-agent orchestration integrating 74+ chemistry tools.*

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ArXiv 2025 &mdash; Co-First Author</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![ArXiv 2025](https://img.shields.io/badge/ArXiv-2025-b31b1b) [Evaluating Large Language Models in Scientific Discovery](https://arxiv.org/abs/2512.15567)

**Kehan Guo**\*, [Co-authors]\*, ... &mdash; *Comprehensive multi-domain benchmark for AI in Science*

</div>
</div>


- ![IJCAI 2025](https://img.shields.io/badge/IJCAI-2025-%232F4F4F?style=plastic&logoColor=%2387CEFA) [Artificial Intelligence in Spectroscopy: Advancing Chemistry from Prediction to Generation and Beyond](https://arxiv.org/pdf/2502.09897), **Kehan Guo**, Yifan Shen, Gil A. Gonzalez-Montiel, Yue Huang, Yujun Zhou, Mihir Surve, Zhichun Guo, ... &mdash; *Survey*


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2023</div><img src='images/llmchem.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![NeurIPS 2023](https://img.shields.io/badge/NeurIPS-2023-2023) [What can Large Language Models do in chemistry? A comprehensive benchmark on eight tasks](https://github.com/ChemFoundationModels/ChemLLMBench)

Taicheng Guo\*, **Kehan Guo**\*, Bozhao Nan, Zhenwen Liang, Zhichun Guo, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang

[**Code**](https://github.com/ChemFoundationModels/ChemLLMBench) [![](https://img.shields.io/github/stars/ChemFoundationModels/ChemLLMBench)](https://github.com/ChemFoundationModels/ChemLLMBench)

*600+ citations. The first comprehensive LLM evaluation for chemistry.*

</div>
</div>


# 📖 Education
- *2022.09 - 2027.05 (Expected)*, Ph.D, <img src='images/Notre_Dame.png' style='width: 1.2em;'> [University of Notre Dame](https://www.nd.edu/) &mdash; Advisor: Prof. Xiangliang Zhang
- *2020.09 - 2022.05*, M.S,  <img src='images/bu.png' style='width: 1.2em;'> [Boston University](https://www.bu.edu/)


# 🎖 Awards
- *2025* NeurIPS Spotlight (top ~3%) &mdash; *AdaReasoner*
- *2024* NeurIPS Spotlight (top ~3%) &mdash; *MolPuzzle*
- *2024* OpenAI Researcher Access Program


# 💻 Professional Service
- **Reviewer:** NeurIPS (2024&ndash;25), ICLR (2025&ndash;26), ICML, AAAI, IJCAI, KDD, ACL Rolling Review, WWW, EMNLP


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Map Widget</title>
    <style>
        .map-container {
            width: 300px;
            margin: 0 auto;
            text-align: center;
        }
        .map-container iframe {
            width: 100%;
            height: 300px;
        }
    </style>
</head>
<body>
    <div class="map-container">
<script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=j0c1_fHIloUhG4VJOq9LgaxK6GKOZ6MwrAZbEqZLjM4&cl=ffffff&w=a"></script>
    </div>
</body>
</html>
