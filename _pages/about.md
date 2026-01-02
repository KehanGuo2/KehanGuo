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

I am a fourth-year Ph.D. student in the <a href="https://sites.nd.edu/xiangliang-zhang/">MINE Lab</a> at <a href="https://www.nd.edu/">Notre Dame</a>, advised by <a href="https://sites.nd.edu/xiangliang-zhang/">Prof. Xiangliang Zhang</a>.

I build <strong>Self-Evolving Scientific Agents</strong>—systems that use tools to reason, verify their own logic, and discover new chemistry. My work bridges <strong>Diffusion Language Models</strong>, <strong>Social-Choice GRPO</strong>, and <strong>Neuro-Symbolic Reasoning</strong>, aiming to create AI that doesn't just predict scientific data, but <em>understands</em> it.

<blockquote style="font-size: 16px; line-height: 1.6;">
I am always open to connecting with colleagues in my field and across interdisciplinary domains. If my research interests you, please feel free to reach out via <a href="mailto:kguo2@nd.edu">email</a>.
</blockquote>

</span>

&#128300; Research
------

<div style="text-align: center; margin: 20px 0;">
  <img src="images/research_architecture.jpg" alt="The Neuro-Symbolic Loop Architecture" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
  <p style="font-size: 14px; color: #555; margin-top: 12px;"><strong>Figure 1: The Neuro-Symbolic Loop.</strong> My architecture for <em>ChemOrch</em> (NeurIPS '25), integrating a Multi-Agent Workforce with a Unified World Graph.</p>
</div>




&#128293; News 
------

<ul style="font-size: 16px; line-height: 1.8; list-style-type: disc; padding-left: 20px;">
  <li><strong>Status:</strong> 🚀 Actively seeking <strong>Research Scientist Internships</strong> for Spring/Summer/Fall 2026 at top AI labs (DeepMind, Meta, OpenAI, etc.).</li>
  <li><strong>2025.12:</strong> New Preprint: Co-first author on <a href="https://arxiv.org/abs/2512.15567">Evaluating Large Language Models in Scientific Discovery</a> — a massive community benchmark for AI in Science.</li>
  <li><strong>2025.09:</strong> Two papers accepted to <strong>NeurIPS 2025</strong>: <strong>ChemOrch</strong> (Agentic Chemistry) and <em>AdaReasoner</em> (<span style="color: #e74c3c;">Spotlight</span>).</li>
  <li><strong>2025.08:</strong> Completed Applied Scientist Internship at <strong>Amazon AWS AI (Deep Engine Team)</strong> in NYC.</li>
  <li><strong>2024.12:</strong> Thrilled to be awarded OpenAI's Researcher Access Program.</li>
  <li><strong>2024.09:</strong> <a href="https://github.com/KehanGuo2/MolPuzzle">MolPuzzle</a> has been accepted by <em>NeurIPS 2024 Dataset and Benchmark Track</em> as a <span style="color: #e74c3c;">Spotlight</span>!</li>
  <li><strong>2024.09:</strong> One paper has been accepted by main conference of EMNLP 2024!</li>
  <li><strong>2024.06:</strong> I passed my Ph.D. Qualification exam!</li>
  <li><strong>2023.09:</strong> One first-author paper has been accepted by <em>NeurIPS 2023</em></li>
</ul>


&#128206; Selected Publications
------
See more publications in my [Google Scholar](https://scholar.google.com/citations?user=t8iRCLUAAAAJ&hl=en)


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024 Spotlight</div><img src='images/intro_spectrum.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![NeurIPS 2024](https://img.shields.io/badge/NeurIPS-2024-2024) [Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://kehanguo2.github.io/Molpuzzle.io/)

**Kehan Guo**, Bozhao Nan, Yujun Zhou, Taicheng Guo, Zhichun Guo, Mihir Surve, Zhenwen Liang, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang

[**Code**](https://github.com/KehanGuo2/MolPuzzle) [![](https://img.shields.io/github/stars/KehanGuo2/MolPuzzle)](https://github.com/KehanGuo2/MolPuzzle)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ArXiv 2025 — Co-First Author</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![ArXiv 2025](https://img.shields.io/badge/ArXiv-2025-b31b1b) [Evaluating Large Language Models in Scientific Discovery](https://arxiv.org/abs/2512.15567)

**Kehan Guo**\*, [Co-authors]\*, ... — *A massive community benchmark for AI in Science*

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025 — Mentored Project</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-2025) [ChemOrch: Empowering LLMs with Chemical Intelligence via Synthetic Instructions](https://github.com/)

Yue Huang, Zhengzhe Jiang, Xiaonan Luo, **Kehan Guo**, Haomin Zhuang, Yujun Zhou, Zhengqing Yuan, Xiaoqi Sun, Jules Schleinitz, Yanbo Wang, Shuhao Zhang, Mihir Surve, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang

*Note: Mentored project resulting in NeurIPS acceptance*

</div>
</div>


- ![IJCAI 2025](https://img.shields.io/badge/IJCAI-2025-%232F4F4F?style=plastic&logoColor=%2387CEFA) [Artificial Intelligence in Spectroscopy: Advancing Chemistry from Prediction to Generation and Beyond](https://arxiv.org/pdf/2502.09897), **Kehan Guo**, Yifan Shen, Gil A. Gonzalez-Montiel, Yue Huang, Yujun Zhou, Mihir Surve, Zhichun Guo, ... — *Survey*


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2023</div><img src='images/llmchem.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![NeurIPS 2023](https://img.shields.io/badge/NeurIPS-2023-2023) [What can Large Language Models do in chemistry? A comprehensive benchmark on eight tasks](https://github.com/ChemFoundationModels/ChemLLMBench)

Taicheng Guo\*, **Kehan Guo**\*, Bozhao Nan, Zhenwen Liang, Zhichun Guo, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang

[**Code**](https://github.com/ChemFoundationModels/ChemLLMBench) [![](https://img.shields.io/github/stars/ChemFoundationModels/ChemLLMBench)](https://github.com/ChemFoundationModels/ChemLLMBench)

</div>
</div>



<!-- # 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2016</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Deep Residual Learning for Image Recognition](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)

**Kaiming He**, Xiangyu Zhang, Shaoqing Ren, Jian Sun

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
</div>
</div> -->



<!-- # 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

# 📖 Educations
- *2022.09 - Present*, Ph.D, <img src='images/Notre_Dame.png' style='width: 1.2em;'> [University of Notre Dame](https://www.nd.edu/)  
- *2020.09 - 2022.05*, M.S,  <img src='images/bu.png' style='width: 1.2em;'> [Boston University](https://www.nd.edu/) 

<!-- 
- *2016.09 - 2020.05*, B.S,  <img src='images/UNI.png' style='width: 1.2em;'> [University of Nothern Iowa](https://uni.edu/)  -->

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->



# 💻 Services
- 2025, Reviewer for ICLR 2025, KDD 2025, WWW 2025, ACL 2025
- 2024, Reviewer for ACL 2024, WWW 2024

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


<!-- # 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China. -->