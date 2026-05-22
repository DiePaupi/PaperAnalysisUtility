
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\8 Grounded Reinforcement Learning\Grounded Reinforcement Learning.pdf"
---
INFO:
 - 'springer' = Has two headerlines to skip (1st = Shortitle/Author; 2nd = page number)
 - 'acm'      = Has no headerlines to skip
Enter a supported formatting template (['springer', 'acm']): acm
---
INFO:
 - 'LFflTOY' = Lastname, Firstname (firstletter), Title, Outlet, Year
            -> This is, for example, used by Springer Nature
 - 'LFflYTO' = Lastname, Firstname (firstletter), Year, Title, Outlet
            -> This is, for example, used by the AAAI/ACM Conference
 - 'FLYTO'   = Firstname, Lastname, Year, Title, Outlet
            -> This is, for example, used by ACM
 - 'FLTOY'  = Firstname, Lastname, Title, Outlet, Year
            -> This is, for example, used by the NeurIPS Conference
Enter a supported bibliography layout (['LFflTOY', 'LFflYTO', 'FLYTO', 'FLTOY']): FLTOY
---
INFO:
 - 'natbib'           = No numbering; reference in 'References' section starts with the authors' names
 - 'numbered_squares' = Reference in 'References' section starts with, e.g., '[1]'
 - 'number_with_dot'  = Reference in 'References' section starts with, e.g., '1.'
Enter a supported bibliography numbering (['natbib', 'numbered_squares', 'number_with_dot']): numbered_squares
---
INFO:
 - 'numeric'           = A number placed inside square brackets (e.g., [28])
                      -> Multiple references are separated by a comma (e.g., [28,29])
 - 'authoryear_round'  = Authors' names and the year places insince round brackets (e.g., (Speckmann et al., 2025))
                      -> Multiple references are separated by a semicolon (e.g., (Speckmann et al. 2025; Janiesch et al. 2021))
                      -> Please note that the author and year are *not* separated
 - 'authoryear_square' = Authors' names and the year places insince square brackets (e.g., [Speckmann et al., 2025])
                      -> Multiple references are separated by a comma (e.g., [Speckmann et al., 2025, Janiesch et al., 2021])
                      -> Please note that the author and year are also separated by a comma
Enter a supported referencing template (['numeric', 'authoryear_round', 'authoryear_square']): numeric
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 2
- Found following heading '2 - Related Work' on page 3
- Found following heading '3 - Preliminaries' on page 4
- Found following heading '4 - Visually Grounded Reinforcement Learning (ViGoRL)' on page 5
- Found following heading '5 - Experiments' on page 7
- Found following heading '6 - Conclusion and Discussion' on page 10
=> Found references/literature section on page 11
- Found heading after References '8 - Gradient accumulation' on page 21
- Found heading after References '8 - Rollout engine' on page 21
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 21
All found references: 94
-> Warning: Malformed author string: 'Openai'
-> Warning: Malformed author string: 'NVIDIA'
-> Warning: Malformed author string: ':'
-> Warning: Malformed author string: 'et'
-> Warning: Malformed author string: 'et'
-> Warning: Could not parse year in reference 'xAI. Grok-1.5 vision preview.'!
-> Warning: Malformed author string: 'xAI'
-> Warning: Could not parse year in reference 'Yaowei Zheng, Shenzhi Wang Junting Lu, Zhangchi Feng, Dongdong Kuang, and Yuwen Xiong. Easyr1: An efficient, scalable, multi-modality rl training framework.'!
-> Warning: Could not parse year in reference 'Richard Zhuang*, Trung Vu*, Alex Dimakis, and Maheswaran Sathiamoorthy. Improving multi-turn tool use with reinforcement learning.'!
-> Warning: Could not parse year in reference 'A1 Appendix Overview The structure of this Appendix is as follows: • Section A2 contains limitations and future work. • Section A3 contains broader impacts. • Section A4 contains additional discussion and connection to cognitive science. • Section A5 contains additional methods details. • Section A6 contains additional details on the model behavioral analysis. • Section A7 contains additional details on the human evaluation. • Section A8 contains additional experimental results. • Section A9 contains example model outputs. A2 Limitations and Future Work While our approach demonstrates strong improvements in visual reasoning performance, several limitations remain and open avenues for future research: Intermediate Reward. Our current reinforcement learning setup provides rewards only at the final answer level. In spatial reasoning tasks, this sometimes results in reward hacking, where the model receives positive reward despite generating partially incorrect or underspecified reasoning. Although our human evaluation confirms that the majority of grounding predictions are accurate and helpful, there remains measurable room for improvement. We hypothesize that introducing dense intermediate rewards—for both correct reasoning steps and accurate grounding—could mitigate these issues and improve alignment between grounding, reasoning, and reward. We leave this exploration to future work. Expanded Tool Use and Adaptive Control. While our model can point, crop, and zoom into visual regions, other forms of tool-augmented perception (e.g., highlighting, region comparison, or 3D navigation) may further support compositional reasoning. Future work could explore mechanisms that learn to balance visual actions dynamically. Learning When and How Much to Reason. We observe that the model often generates long reasoning chains, even for relatively simple questions. This inefficiency echoes known challenges in language-only chain-of-thought models [65, 30], where reasoning is applied uniformly regardless of task complexity. A promising direction for future work is to develop methods that help models learn when to reason and how much reasoning is necessary, adapting the depth of their chain-of-thought to the demands of the task. Interpreting Attention Patterns. Although our behavioral and human studies demonstrate that explicit grounding amplifies structured visual behaviors and improves interpretability, the mechanisms through which grounding improves reasoning remain underexplored. Future work should examine how explicit grounding influences a model’s internal attention dynamics and whether these patterns resemble human gaze behaviors. Further comparisons to human cognitive strategies—such as visual routines [62], task-directed attention [78], and deictic planning [4]—could yield deeper insights into both model behavior and human cognition. A3 Broader Impacts Positive Societal Impacts. Grounded reasoning improves model transparency by producing interpretable chains of thought that reference specific image regions. This interpretability is especially valuable in high-stakes domains such as medical imaging, accessibility tools, assistive robotics, and scientific image analysis, where understanding the basis for model decisions is crucial. Additionally, our approach may enhance human-AI collaboration by making the model’s internal decision process legible and actionable for human users. Because the model reasons over localized visual subproblems, it can better align with human intuition, which may foster trust and oversight. Potential Negative Impacts. Despite its benefits, the ability to produce detailed visual reasoning traces could be misused for surveillance or automated profiling. A grounded model that can isolate visual elements, track reasoning over time, and justify actions may inadvertently enable more fine-grained tracking of individuals or objects in sensitive contexts. Moreover, models that appear interpretable may be perceived as more reliable than they truly are; if the reasoning trace is superficially plausible but incorrect, users may over-trust the model’s output. This risk is particularly relevant in domains where visual ambiguity or annotation bias affects ground truth. Our approach also assumes the availability of visual data and may propagate or amplify dataset biases, especially in domains where certain object types, environments, or affordances are overrepresented. Spatial grounding mechanisms may lock the model’s attention onto biased or stereotyped regions of the image, reinforcing existing disparities unless care is taken in dataset construction and evaluation. Mitigation Strategies. To mitigate these risks, future work could incorporate uncertainty estimation or confidence calibration into the reasoning trace, explicitly marking when the model is uncertain about a grounding decision. It is also important to develop tools that allow users to audit the reasoning trace and provide corrections. In addition, efforts to diversify training data and evaluate model behavior across demographic and situational axes are essential for fair deployment. Finally, deployment in sensitive settings should involve human-in-the-loop oversight, particularly when grounded outputs inform consequential decisions. A4 Additional Discussion Our results show that explicitly grounding reasoning steps in spatial coordinates substantially improves performance across visual reasoning benchmarks. To better understand why, we draw from both the recent machine learning literature and long-standing cognitive science theories that point to grounding as a core mechanism in human and artificial reasoning. Grounding as a Cognitive Scaffold. Classic studies in visual cognition suggest that humans reason about complex scenes by sequentially directing attention to spatially localized regions in service of goal-driven subproblems. Yarbus [78] demonstrated that eye movement patterns depend heavily on task demands, suggesting a deep link between overt visual attention and internal reasoning. Ullman [62] introduced the concept of visual routines, showing that reasoning over a scene involves decomposable, spatially localized operations. Ballard et al. [4] formalized this via deictic codes, where visual fixations and gestures act as pointers binding abstract variables to perceptual content. These mechanisms reduce cognitive load (as opposed to raw computational load), support compositionality, and facilitate subgoal execution by grounding symbolic reasoning in visual input. Grounding Reduces Hallucination and Enhances Generalization. In machine learning, recent studies demonstrate that grounding in visual regions curbs hallucination and promotes generalization. Ghosh et al. [14] show that large VLMs hallucinate less and reason more accurately when first prompted to generate grounded visual descriptions. Qi et al. [44] propose a chain-of-manipulations method where VLMs perform spatially localized actions (e.g., zoom, crop, verify), achieving stronger generalization and interpretability. These findings echo Treisman’s seminal Feature Integration Theory [61], which argues that spatial attention is essential for integrating visual features, and Harnad’s symbol grounding problem [20], which proposes that abstract reasoning is only meaningful when connected to perceptual representations. Object-centric and Compositional Inductive Biases. Explicit grounding may also encourage models to adopt object-centric and modular representations. Ding et al. [9] show that attention over learned object embeddings improves structured visual reasoning. Gupta et al. [18] demonstrate that language-guided neural modules that condition on spatial cues improve the compositional generalization of the model. These results align with the cognitive perspective that humans naturally build scene representations around individual entities and their relations [4]. Overall, the convergence of cognitive science and ML literature suggests that explicit grounding does not merely reduce the search space, but acts as a structural inductive bias that enhances compositionality, verification, and goal-directed reasoning, core ingredients for generalization in both human and machine learners.'!
-> Warning: Could not parse year in reference 'A5 Additional Methodological Details A5.1 Group Relative Policy Optimization (GRPO) Group Relative Policy Optimization (GRPO) [50] stabilizes policy learning from long-form trajectories by computing group-normalized advantages and applying clipped token-level PPO-style updates. Specifically, for a group of G trajectories O = {τ (i)}G i=1 conditioned on input x, each trajectory τ (i) has a scalar reward r(i) = R(τ (i)). GRPO computes the centered advantage ˆA(i) = r(i) −¯R, where ¯R = 1 G P i r(i) is the group mean. Let τ (i) t be the t-th token of trajectory τ (i). GRPO minimizes the following clipped surrogate loss: LGRPO(θ) = −1 G G X i=1 1 |τ (i)| X t min h ρ(i) t ˆA(i), clip(ρ(i) t , 1−ε, 1+ε) ˆA(i)i + β KL[πθ∥πref], (1) where ρ(i) t = πθ(τ (i) t |τ (i) <t ,x) πold(τ (i) t |τ (i) <t ,x) is the importance weight, ε = 0.2 is the clipping parameter, and β is the KL penalty coefficient. This approach stabilizes learning in long-horizon, multimodal reasoning settings. A5.2 RL Reward Functions Task Rewards. We define reward functions specific to each benchmark: • Spatial Reasoning (SAT-2). A binary reward: rtask = 1 if the predicted answer matches the ground truth, and 0 otherwise. • Web Grounding (OS-Atlas). A binary reward: rtask = 1 if the predicted coordinate lies inside the annotated bounding box. • Web Action Prediction (ICAL). A decomposed reward: rtask = rtype + rarg, where rtype = 0.5 if the predicted action type matches, and rarg = 0.5 if the predicted argument (e.g., DOM ID, string) matches. A5.3 Multi-turn Reinforcement Learning Details We first apply supervised fine-tuning (SFT) on multi-turn traces. These are derived from the same MCTS chains used to train the single-turn model, but reformatted into multi-turn training data by: (1) For each node, formulating the text in a think block followed by taking the coordinate and formulating it into a tool call. If it is a terminal node, a think block is added with any remaining text followed by the predicted answer in answer tags. (2) Cropping around the coordinate to obtain the feedback image, and appending this image to the training data as a user turn in the sample to be used for SFT. (3) Continuing (1) and (2) until terminal. We additionally include backtracking as described in Section 4.2. For multi-turn scenarios, we apply GRPO over full dialog trajectories. Observation tokens are masked from the loss, ensuring gradients flow solely through the language model while retaining visual input to the encoder. We additionally mask samples not ending in an EOS token [80]. Termination Enforcement. During RL rollouts, if a dialog reaches Tmax = 5 turns without emitting an <answer> block, we append a soft prompt to the final assistant message: <think> Please provide your response now </think> This maintains structural fidelity and bounds rollout length. KL collapse. While concurrent work observed occasional KL collapse in multi-turn RL when applied to base model with vision inputs [64, 92], we found that our initial warm start enabled stable training and allowed us to maintain a moderate KL coefficient (0.01). Diversity bonus. We introduced the concept of a diversity turn bonus into our reward formulation in Section 4.3 of the main paper. In Figure A1, we show the response length over RL training with and without the diversity bonus. Without the diversity bonus, the model quickly converges to single turn outputs (green line), whereas the model avoids this and outputs >1 turn on average with the bonus reward (blue line). Figure A1: Response length with and without turn bonus. Without the bonus, the model converges to always taking a single turn (as also verified by examining model outputs), whereas the bonus enables the model to stabilize multi-turn. A5.4 Training Implementation Details General Setup. Training is conducted on 8 A100 GPUs with Qwen2.5-VL models (3B and 7B). Supervised fine-tuning uses 3 epochs, while GRPO is applied for 500 rollout-update iterations. Evaluation uses decoding temperature of 0.5. We build on Llama-Factory [89] for SFT, and EasyR1 [90, 52] for GRPO. Training Hyperparameters Overview We provide all training hyperparameters used in SFT, and single- and multi-turn RL in Tables A1-A3. Table A1: Supervised FineTuning (SFT). Hyperparameter Value Epochs 3 Learning rate 1e-6 Weight decay 0.01 Warmup ratio 0.03 Batch size'!
 -> Found dublicated ref_ids:
                                       full_reference ref_id  ... link valid
93  A5 Additional Methodological Details A5.1 Grou...         ...       None

[1 rows x 11 columns]
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                               link  valid
0       1                                             Openai  ...                                                      None
1       2  Jean-Baptiste Alayrac, Jeff Donahue, Pauline L...  ...                                                      None
2       3  Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wan...  ...                                                      None
3       4  Dana H Ballard, Mary M Hayhoe, Polly K Pook, a...  ...                                                      None
4       5  Xi Chen, Xiao Wang, Soravit Changpinyo, AJ Pie...  ...                  https://arxiv.org/abs/2209.06794.   None
..    ...                                                ...  ...                                                ...    ...
89     90  Yaowei Zheng, Shenzhi Wang Junting Lu, Zhangch...  ...                 https://github.com/hiyouga/EasyR1,   None
90     91  Qiji Zhou, Ruochen Zhou, Zike Hu, Panzhong Lu,...  ...                  https://arxiv.org/abs/2405.13872.   None
91     92  Richard Zhuang*, Trung Vu*, Alex Dimakis, and ...  ...  https://www.bespokelabs.ai/blog/improvingmulti...   None
92      a  A1 Appendix Overview The structure of this App...  ...                                                      None
93      b            A5 Additional Methodological Details A5  ...                                                      None

[94 rows x 10 columns]
- Checking reference 1/94:
  -> INFO: Now checking 10 results for matching title: 'gpt-4 technical report'
       -> INFO: All authors matched!
- Checking reference 2/94:
  -> INFO: Now checking 10 results for matching title: 'Flamingo: a visual language model for few-shot learning'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 3/94:
  -> INFO: Now checking 10 results for matching title: 'Qwen2'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Qwen2'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Qwen2 manually and check the results.
        -> Author(s): Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang, Humen Zhong, Yuanzhi Zhu, Mingkun Yang, Zhaohai Li, Jianqiang Wan, Pengfei Wang, Wei Ding, Zheren Fu, Yiheng Xu, Jiabo Ye, Xi Zhang, Tianbao Xie, Zesen Cheng, Hang Zhang, Zhibo Yang, Haiyang Xu, and Junyang Lin
        -> Title:     Qwen2
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 4/94:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Deictic codes for the embodiment of cognition
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Ballard', 'Hayhoe', 'Pook', 'Rao', '1997']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deictic+codes+for+the+embodiment+of+cognition manually and check the results.
        -> Author(s): Dana H Ballard, Mary M Hayhoe, Polly K Pook, and Rajesh PN Rao
        -> Title:     Deictic codes for the embodiment of cognition
        -> Year:      1997
     -> Manual search was skipped by the user.
- Checking reference 5/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2209.06794.
  -> INFO: Now checking 10 results for matching title: 'Pali: A jointly-scaled multilingual language-image model.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Chen', 'Wang', 'Changpinyo', 'Piergiovanni', 'Padlewski', 'Salz', 'Goodman', 'Grycner', 'Mustafa', 'Beyer', 'Kolesnikov', 'Puigcerver', 'Ding', 'Rong', 'Akbari', 'Mishra', 'Xue', 'Thapliyal', 'Bradbury', 'Kuo', 'Seyedhosseini', 'Jia', 'Ayan', 'Riquelme', 'Steiner', 'Angelova', 'Zhai', 'Houlsby', 'Soricut', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Pali:+A+jointly-scaled+multilingual+language-image+model. manually and check the results.
        -> Author(s): Xi Chen, Xiao Wang, Soravit Changpinyo, AJ Piergiovanni, Piotr Padlewski, Daniel Salz, Sebastian Goodman, Adam Grycner, Basil Mustafa, Lucas Beyer, Alexander Kolesnikov, Joan Puigcerver, Nan Ding, Keran Rong, Hassan Akbari, Gaurav Mishra, Linting Xue, Ashish Thapliyal, James Bradbury, Weicheng Kuo, Mojtaba Seyedhosseini, Chao Jia, Burcu Karagol Ayan, Carlos Riquelme, Andreas Steiner, Anelia Angelova, Xiaohua Zhai, Neil Houlsby, and Radu Soricut
        -> Title:     Pali: A jointly-scaled multilingual language-image model.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 6/94:
  -> INFO: Now checking 1 results for matching title: 'Seeclick: Harnessing gui grounding for advanced visual gui agents'
       -> INFO: All authors matched!
- Checking reference 7/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2305.06500.
  -> INFO: Now checking 8 results for matching title: 'Instructblip: Towards general-purpose vision-language models with instruction tuning.'
  -> WARNING: None of the 8 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Dai', 'Li', 'Li', 'Tiong', 'Zhao', 'Wang', 'Li', 'Fung', 'Hoi', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Instructblip:+Towards+general-purpose+vision-language+models+with+instruction+tuning. manually and check the results.
        -> Author(s): Wenliang Dai, Junnan Li, Dongxu Li, Anthony Meng Huat Tiong, Junqi Zhao, Weisheng Wang, Boyang Li, Pascale Fung, and Steven Hoi
        -> Title:     Instructblip: Towards general-purpose vision-language models with instruction tuning.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 8/94:
  -> INFO: Now checking 2 results for matching title: 'Molmo and pixmo: Open weights and open data for state-of-the-art multimodal models'
       -> WARNING: Not all 51 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Anderson, Bransom, Ehsani, Ngo, Chen, Patel, Yatskar, Callison-Burch, Head, Hendrix, Bastani, VanderBilt, Lambert, Chou, Chheda, Sparks, Skjonsberg, Schmitz, Sarnat, Bischoff, Walsh, Newell, Wolters, Gupta, Zeng, Borchardt, Groeneveld, Dumas, Nam, Lebrecht, Wittlif, Schoenick, Michel, Krishna, Weihs, Smith, Hajishirzi, Girshick, Farhadi, Kembhavi'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/94:
  -> INFO: Now checking 10 results for matching title: 'Attention over learned object embeddings enables complex visual reasoning'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Hill, Santoro, Reynolds, Botvinick'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2411.14432.
  -> INFO: Now checking 10 results for matching title: 'Insight-v: Exploring long-chain visual reasoning with multimodal large language models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Dong', 'Liu', 'Sun', 'Yang', 'Hu', 'Rao', 'Liu', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Insight-v:+Exploring+long-chain+visual+reasoning+with+multimodal+large+language+models. manually and check the results.
        -> Author(s): Yuhao Dong, Zuyan Liu, Hai-Long Sun, Jingkang Yang, Winston Hu, Yongming Rao, and Ziwei Liu
        -> Title:     Insight-v: Exploring long-chain visual reasoning with multimodal large language models.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 11/94:
  -> INFO: Now checking 1 results for matching title: 'Blink: Multimodal large language models can see but not perceive'
       -> INFO: All authors matched!
- Checking reference 12/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2501.05452.
  -> INFO: Now checking 1 results for matching title: 'Refocus: Visual editing as a chain of thought for structured image understanding.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Fu', 'Liu', 'Yang', 'Corring', 'Lu', 'Yang', 'Roth', 'Florencio', 'Zhang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Refocus:+Visual+editing+as+a+chain+of+thought+for+structured+image+understanding. manually and check the results.
        -> Author(s): Xingyu Fu, Minqian Liu, Zhengyuan Yang, John Corring, Yijuan Lu, Jianwei Yang, Dan Roth, Dinei Florencio, and Cha Zhang
        -> Title:     Refocus: Visual editing as a chain of thought for structured image understanding.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 13/94:
  -> INFO: Now checking 1 results for matching title: 'Cognitive behaviors that enable self-improving reasoners, or, four habits of highly effective stars'
       -> INFO: All authors matched!
- Checking reference 14/94:
  -> INFO: Now checking 10 results for matching title: 'Grounded decoding with visual descriptions reduces hallucination in large vision-language models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ghosh', 'Lee', 'Alayrac', 'Zhai', 'Feichtenhofer', 'Carreira', 'Misra', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Grounded+decoding+with+visual+descriptions+reduces+hallucination+in+large+vision-language+models manually and check the results.
        -> Author(s): Sarthak Ghosh, Ben Lee, Jean-Baptiste Alayrac, Xuhong Zhai, Christoph Feichtenhofer, Joao Carreira, and Ishan Misra
        -> Title:     Grounded decoding with visual descriptions reduces hallucination in large vision-language models
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 15/94:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=kxnoqaisCT.
  -> INFO: Now checking 1 results for matching title: 'Navigating the digital world as humans do: Universal visual grounding for GUI agents'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/94:
  -> INFO: Now checking 10 results for matching title: 'The llama 3 herd of models'
       -> WARNING: Not all 500 authors from the found ref. were matched (only 16)
                   Unmatched authors = 'Yang, Fan, Goyal, Hartshorn, Yang, Mitra, Sravankumar, Korenev, Hinsvark, Rao, Zhang, Rodriguez, Gregerson, Spataru, Rozière, Biron, Tang, Chern, Caucheteux, Nayak, Bi, Marra, McConnell, Keller, Touret, Wu, Wong, Ferrer, Nikolaidis, Allonsius, Song, Pintz, Livshits, Esiobu, Choudhary, Mahajan, Garcia-Olano, Perino, Hupkes, Lakomkin, AlBadawy, Lobanova, Dinan, Smith, Radenovic, Zhang, Synnaeve, Lee, Anderson, Nail, Mialon, Pang, Cucurell, Nguyen, Korevaar, Xu, Touvron, Zarov, Ibarra, Kloumann, Misra, Evtimov, Copet, Lee, Geffert, Vranes, Park, Mahadeokar, Shah, Linde, Billock, Hong, Lee, Fu, Chi, Huang, Liu, Wang, Bitton, Spisak, Park, Rocca, Johnstun, Saxe, Jia, Alwala, Upasani, Plawiak, Li, Heafield, Stone, El-Arini, Iyer, Malik, Chiu, Bhalla, Rantala-Yeary, Maaten, Chen, Tan, Jenkins, Martin, Madaan, Malo, Blecher, Landzaat, Oliveira, Muzzi, Pasupuleti, Singh, Paluri, Kardas, Oldham, Rita, Pavlova, Kambadur, Lewis, Si, Singh, Hassan, Goyal, Torabi, Bashlykov, Bogoychev, Chatterji, Duchenne, cCelebi, Alrassy, Zhang, Li, Vasić, Weng, Bhargava, Dubal, Krishnan, Koura, Xu, Dong, Srinivasan, Ganapathy, Calderer, Cabral, Stojnic, Raileanu, Girdhar, Patel, Sauvestre, Polidoro, Sumbaly, Taylor, Silva, Hou, Wang, Hosseini, Chennabasappa, Singh, Bell, Kim, Edunov, Nie, Narang, Raparthy, Shen, Wan, Bhosale, Zhang, Vandenhende, Batra, Whitman, Sootla, Collot, Gururangan, Borodinsky, Herman, Fowler, Sheasha, Georgiou, Scialom, Speckbacher, Mihaylov, Xiao, Karn, Goswami, Gupta, Ramanathan, Kerkez, Gonguet, Do, Vogeti, Petrovic, Chu, Xiong, Fu, Meers, Martinet, Wang, Tan, Xie, Jia, Wang, Goldschlag, Gaur, Babaei, Wen, Song, Zhang, Li, Mao, Coudert, Yan, Chen, Papakipos, Singh, Jain, Kelsey, Shajnfeld, Gangidi, Victoria, Goldstand, Menon, Sharma, Boesenberg, Baevski, Feinstein, Kallet, Sangani, Yunus, Lupu, Alvarado, Caples, Gu, Ho, Poulton, Ryan, Ramchandani, Franco, Saraf, Chowdhury, Gabriel, Bharambe, Eisenman, Yazdan, James, Maurer, Leonhardi, Huang, Loyd, Paola, Paranjape, Liu, Wu, Ni, Hancock, Wasti, Spence, Stojkovic, Gamido, Montalvo, Parker, Burton, Mejia, Wang, Kim, Zhou, Chu, Cai, Tindal, Feichtenhofer, Civin, Beaty, Kreymer, Li, Wyatt, Adkins, Xu, Testuggine, David, Parikh, Liskovich, Foss, Wang, Holland, Dowling, Jamil, Montgomery, Presani, Hahn, Wood, Brinkman, Arcaute, Dunbar, Smothers, Sun, Kreuk, Tian, Ozgenel, Caggioni, Guzmán, Kanayet, Seide, Florez, Schwarz, Badeer, Swee, Halpern, Thattai, Herman, Sizov, Zhang, Lakshminarayanan, Shojanazeri, Zou, Wang, Zha, Habeeb, Rudolph, Suk, Aspegren, Goldman, Molybog, Tufanov, Veliche, Gat, Weissman, Geboski, Kohli, Asher, Gaya, Marcus, Tang, Chan, Zhen, Reizenstein, Teboul, Zhong, Jin, Yang, Cummings, Carvill, Shepard, McPhie, Torres, Ginsburg, Wang, Wu, KamHou, Saxena, Prasad, Khandelwal, Zand, Matosich, Veeraraghavan, Michelena, Li, Huang, Chawla, Lakhotia, Huang, Chen, Garg, Lavender, Silva, Bell, Zhang, Guo, Moshkovich, Wehrstedt, Khabsa, Avalani, Bhatt, Tsimpoukelli, Mankus, Hasson, Lennie, Reso, Groshev, Naumov, Lathi, Keneally, Seltzer, Valko, Restrepo, Patel, Vyatskov, Samvelyan, Clark, Macey, Wang, Hermoso, Metanat, Rastegari, Bansal, Santhanam, Parks, White, Bawa, Singhal, Egebo, Usunier, Laptev, Dong, Zhang, Cheng, Chernoguz, Hart, Salpekar, Kalinli, Kent, Parekh, Saab, Balaji, Rittner, Bontrager, Roux, Dollár, Zvyagina, Ratanchandani, Yuvraj, Liang, Alao, Rodriguez, Ayub, Murthy, Nayani, Mitra, Li, Hogan, Battey, Wang, Maheswari, Howes, Rinott, Bondu, Datta, Chugh, Hunt, Dhillon, Sidorov, Verma, Yamamoto, Ramaswamy, Lindsay, Feng, Lin, Zha, Shankar, Zhang, Wang, Agarwal, Sajuyigbe, Chintala, Max, Chen, Kehoe, Satterfield, Govindaprasad, Gupta, Cho, Virk, Subramanian, Choudhury, Goldman, Remez, Glaser, Best, Kohler, Robinson, Li, Zhang, Matthews, Chou, Shaked, Vontimitta, Ajayi, Montanez, Mohan, Kumar, Mangla, Ionescu, Poenaru, Mihailescu, Ivanov, Li, Wang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/94:
  -> INFO: Now checking 10 results for matching title: 'Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Guo', 'Yang', 'Zhang', 'Song', 'Zhang', 'Xu', 'Zhu', 'Ma', 'Wang', 'Bi', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepseek-r1:+Incentivizing+reasoning+capability+in+llms+via+reinforcement+learning manually and check the results.
        -> Author(s): Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al
        -> Title:     Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 18/94:
  -> INFO: Now checking 10 results for matching title: 'Robust compositional visual reasoning via language-guided neural module networks'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gupta', 'Lin', 'Zhang', 'Galley', 'Gao', 'Ferrer', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Robust+compositional+visual+reasoning+via+language-guided+neural+module+networks manually and check the results.
        -> Author(s): Arjun Gupta, Xi Victoria Lin, Chunyuan Zhang, Michel Galley, Jianfeng Gao, and Carlos Guestrin Ferrer
        -> Title:     Robust compositional visual reasoning via language-guided neural module networks
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 19/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2211.11559.
  -> INFO: Now checking 10 results for matching title: 'Visual programming: Compositional visual reasoning without training.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gupta', 'Kembhavi', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Visual+programming:+Compositional+visual+reasoning+without+training. manually and check the results.
        -> Author(s): Tanmay Gupta and Aniruddha Kembhavi
        -> Title:     Visual programming: Compositional visual reasoning without training.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 20/94:
  -> INFO: Now checking 10 results for matching title: 'The symbol grounding problem'
       -> INFO: All authors matched!
- Checking reference 21/94:
  -> INFO: Now checking 5 results for matching title: 'Cogagent: A visual language model for gui agents'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 22/94:
  -> INFO: Now checking 2 results for matching title: 'Multi-step planning of eye movements in visual search'
       -> INFO: All authors matched!
- Checking reference 23/94:
  -> INFO: Now checking 1 results for matching title: 'Visual sketchpad: Sketching as a visual chain of thought for multimodal language models'
       -> INFO: All authors matched!
- Checking reference 24/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2406.09403.
  -> INFO: Now checking 1 results for matching title: 'Visual sketchpad: Sketching as a visual chain of thought for multimodal language models.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hu', 'Shi', 'Fu', 'Roth', 'Ostendorf', 'Zettlemoyer', 'Smith', 'Krishna', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Visual+sketchpad:+Sketching+as+a+visual+chain+of+thought+for+multimodal+language+models. manually and check the results.
        -> Author(s): Yushi Hu, Weijia Shi, Xingyu Fu, Dan Roth, Mari Ostendorf, Luke Zettlemoyer, Noah A Smith, and Ranjay Krishna
        -> Title:     Visual sketchpad: Sketching as a visual chain of thought for multimodal language models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 25/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2312.03052.
  -> INFO: Now checking 1 results for matching title: 'Visual program distillation: Distilling tools and programmatic reasoning into vision-language models.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hu', 'Stretcu', 'Lu', 'Viswanathan', 'Hata', 'Luo', 'Krishna', 'Fuxman', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Visual+program+distillation:+Distilling+tools+and+programmatic+reasoning+into+vision-language+models. manually and check the results.
        -> Author(s): Yushi Hu, Otilia Stretcu, Chun-Ta Lu, Krishnamurthy Viswanathan, Kenji Hata, Enming Luo, Ranjay Krishna, and Ariel Fuxman
        -> Title:     Visual program distillation: Distilling tools and programmatic reasoning into vision-language models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 26/94:
  -> INFO: Now checking 10 results for matching title: 'Openai o1 system card'
       -> WARNING: Not all 1 authors from the found ref. were matched (only 1)
                   Unmatched authors = ''
       -> WARNING: Not all 1 authors from the found ref. were matched (only 1)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 27/94:
  -> INFO: Now checking 10 results for matching title: 'Scaling up visual and vision-language representation learning with noisy text supervision'
       -> INFO: All authors matched!
- Checking reference 28/94:
  -> INFO: Now checking 10 results for matching title: 'Segment anything'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 29/94:
  -> INFO: Now checking 10 results for matching title: 'Visualwebarena: Evaluating multimodal agents on realistic visual web tasks'
       -> INFO: All authors matched!
- Checking reference 30/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2205.11916.
  -> INFO: Now checking 10 results for matching title: 'Large language models are zero-shot reasoners.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kojima', 'Gu', 'Reid', 'Matsuo', 'Iwasawa', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Large+language+models+are+zero-shot+reasoners. manually and check the results.
        -> Author(s): Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa
        -> Title:     Large language models are zero-shot reasoners.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 31/94:
  -> Checking if provided link is pingable: https://likaixin2000.github.io/papers/ScreenSpot_Pro.pdf.Preprint.
  -> INFO: Now checking 2 results for matching title: 'Screenspot-pro: Gui grounding for professional high-resolution computer use.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Li', 'Meng', 'Lin', 'Luo', 'Tian', 'Ma', 'Huang', 'Chua', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Screenspot-pro:+Gui+grounding+for+professional+high-resolution+computer+use. manually and check the results.
        -> Author(s): Kaixin Li, Ziyang Meng, Hongzhan Lin, Ziyang Luo, Yuchen Tian, Jing Ma, Zhiyong Huang, and Tat-Seng Chua
        -> Title:     Screenspot-pro: Gui grounding for professional high-resolution computer use.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 32/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2504.06958.
  -> INFO: Now checking 5 results for matching title: 'Videochat-r1: Enhancing spatio-temporal perception via reinforcement fine-tuning.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Li', 'Yan', 'Meng', 'Dong', 'Zeng', 'He', 'Wang', 'Qiao', 'Wang', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Videochat-r1:+Enhancing+spatio-temporal+perception+via+reinforcement+fine-tuning. manually and check the results.
        -> Author(s): Xinhao Li, Ziang Yan, Desen Meng, Lu Dong, Xiangyu Zeng, Yinan He, Yali Wang, Yu Qiao, Yi Wang, and Limin Wang
        -> Title:     Videochat-r1: Enhancing spatio-temporal perception via reinforcement fine-tuning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 33/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2405.16919.
  -> INFO: Now checking 3 results for matching title: 'Vocot: Unleashing visually grounded multi-step reasoning in large multi-modal models.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Li', 'Luo', 'Zhang', 'Qiu', 'Huang', 'Wei', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vocot:+Unleashing+visually+grounded+multi-step+reasoning+in+large+multi-modal+models. manually and check the results.
        -> Author(s): Zejun Li, Ruipu Luo, Jiwen Zhang, Minghui Qiu, Xuanjing Huang, and Zhongyu Wei
        -> Title:     Vocot: Unleashing visually grounded multi-step reasoning in large multi-modal models.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 34/94:
  -> INFO: Now checking 4 results for matching title: 'Showui: One vision-language-action model for gui visual agent'
       -> INFO: All authors matched!
- Checking reference 35/94:
  -> INFO: Now checking 10 results for matching title: 'Improved baselines with visual instruction tuning.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', 'Li', 'Li', 'Lee', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Improved+baselines+with+visual+instruction+tuning. manually and check the results.
        -> Author(s): Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee
        -> Title:     Improved baselines with visual instruction tuning.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 36/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2503.20783.
  -> INFO: Now checking 10 results for matching title: 'Understanding r1-zero-like training: A critical perspective.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', 'Chen', 'Li', 'Qi', 'Pang', 'Du', 'Lee', 'Lin', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Understanding+r1-zero-like+training:+A+critical+perspective. manually and check the results.
        -> Author(s): Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin
        -> Title:     Understanding r1-zero-like training: A critical perspective.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 37/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2503.01785.
  -> INFO: Now checking 10 results for matching title: 'Visual-rft: Visual reinforcement fine-tuning.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', 'Sun', 'Zang', 'Dong', 'Cao', 'Duan', 'Lin', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Visual-rft:+Visual+reinforcement+fine-tuning. manually and check the results.
        -> Author(s): Ziyu Liu, Zeyi Sun, Yuhang Zang, Xiaoyi Dong, Yuhang Cao, Haodong Duan, Dahua Lin, and Jiaqi Wang
        -> Title:     Visual-rft: Visual reinforcement fine-tuning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 38/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2503.21620.
  -> INFO: Now checking 4 results for matching title: 'Ui-r1: Enhancing action prediction of gui agents by reinforcement learning.'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lu', 'Chai', 'Guo', 'Yin', 'Liu', 'Wang', 'Xiao', 'Ren', 'Xiong', 'Li', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Ui-r1:+Enhancing+action+prediction+of+gui+agents+by+reinforcement+learning. manually and check the results.
        -> Author(s): Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Han Xiao, Shuai Ren, Guanjing Xiong, and Hongsheng Li
        -> Title:     Ui-r1: Enhancing action prediction of gui agents by reinforcement learning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 39/94:
  -> INFO: Now checking 4 results for matching title: 'Ui-r1: Enhancing action prediction of gui agents by reinforcement learning'
       -> INFO: All authors matched!
- Checking reference 40/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2501.19393.
  -> INFO: Now checking 10 results for matching title: 's1: Simple test-time scaling.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Muennighoff', 'Yang', 'Shi', 'Li', 'Fei-Fei', 'Hajishirzi', 'Zettlemoyer', 'Liang', 'Candès', 'Hashimoto', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=s1:+Simple+test-time+scaling. manually and check the results.
        -> Author(s): Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, and Tatsunori Hashimoto
        -> Title:     s1: Simple test-time scaling.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 41/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2503.15558.
  -> INFO: Now checking 1 results for matching title: 'Cosmos-reason1: From physical common sense to embodied reasoning.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['NVIDIA', ':', 'Azzolini', 'Brandon', 'Chattopadhyay', 'Chen', 'Chu', 'Cui', 'Diamond', 'Ding', 'Ferroni', 'Govindaraju', 'Gu', 'Gururani', 'Hanafi', 'Hao', 'Huffman', 'Jin', 'Johnson', 'Khan', 'Kurian', 'Lantz', 'Lee', 'Li', 'Li', 'Lin', 'Lin', 'Liu', 'Luo', 'Mathau', 'Ni', 'Pavao', 'Ping', 'Romero', 'Smelyanskiy', 'Song', 'Tchapmi', 'Wang', 'Wang', 'Wang', 'Wei', 'Xu', 'Xu', 'Yang', 'Yang', 'Zeng', 'Zhang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Cosmos-reason1:+From+physical+common+sense+to+embodied+reasoning. manually and check the results.
        -> Author(s): NVIDIA, :, Alisson Azzolini, Hannah Brandon, Prithvijit Chattopadhyay, Huayu Chen, Jinju Chu, Yin Cui, Jenna Diamond, Yifan Ding, Francesco Ferroni, Rama Govindaraju, Jinwei Gu, Siddharth Gururani, Imad El Hanafi, Zekun Hao, Jacob Huffman, Jingyi Jin, Brendan Johnson, Rizwan Khan, George Kurian, Elena Lantz, Nayeon Lee, Zhaoshuo Li, Xuan Li, Tsung-Yi Lin, Yen-Chen Lin, Ming-Yu Liu, Alice Luo, Andrew Mathau, Yun Ni, Lindsey Pavao, Wei Ping, David W  Romero, Misha Smelyanskiy, Shuran Song, Lyne Tchapmi, Andrew Z  Wang, Boxin Wang, Haoxiang Wang, Fangyin Wei, Jiashu Xu, Yao Xu, Xiaodong Yang, Zhuolin Yang, Xiaohui Zeng, and Zhe Zhang
        -> Title:     Cosmos-reason1: From physical common sense to embodied reasoning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 42/94:
  -> INFO: Now checking 10 results for matching title: 'Training language models to follow instructions with human feedback'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 43/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2408.07199.
  -> INFO: Now checking 3 results for matching title: 'Agent q: Advanced reasoning and learning for autonomous ai agents.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Putta', 'Mills', 'Garg', 'Motwani', 'Finn', 'Garg', 'Rafailov', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Agent+q:+Advanced+reasoning+and+learning+for+autonomous+ai+agents. manually and check the results.
        -> Author(s): Pranav Putta, Edmund Mills, Naman Garg, Sumeet Motwani, Chelsea Finn, Divyansh Garg, and Rafael Rafailov
        -> Title:     Agent q: Advanced reasoning and learning for autonomous ai agents.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 44/94:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Cogcom: Compositional visual reasoning with chain-of-manipulations
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Qi', 'Zhang', 'Chen', 'Li', 'Zhang', 'Chang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Cogcom:+Compositional+visual+reasoning+with+chain-of-manipulations manually and check the results.
        -> Author(s): Jinyi Qi, Tao Zhang, Rui Chen, Xiaoxue Li, Yizhou Zhang, and Kai-Wei Chang
        -> Title:     Cogcom: Compositional visual reasoning with chain-of-manipulations
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 45/94:
  -> INFO: Now checking 1 results for matching title: 'Ui-tars: Pioneering automated gui interaction with native agents'
       -> WARNING: Not all 35 authors from the found ref. were matched (only 17)
                   Unmatched authors = 'Zhong, Yang, Miao, Lin, Liu, Jiang, Ma, Xiao, Cai, Zheng, Jin, Zhou, Chen, Yang, Liu, Lin, Peng, Liu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 46/94:
  -> INFO: Now checking 10 results for matching title: 'Learning transferable visual models from natural language supervision'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 47/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2407.06581.
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Vision language models are blind: Failing to translate detailed visual features into words.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Rahmanzadehgervi', 'Bolton', 'Taesiri', 'Nguyen', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vision+language+models+are+blind:+Failing+to+translate+detailed+visual+features+into+words. manually and check the results.
        -> Author(s): Pooyan Rahmanzadehgervi, Logan Bolton, Mohammad Reza Taesiri, and Anh Totti Nguyen
        -> Title:     Vision language models are blind: Failing to translate detailed visual features into words.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 48/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2412.07755.
  -> INFO: Now checking 1 results for matching title: 'Sat: Dynamic spatial aptitude training for multimodal language models.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ray', 'Duan', 'Brown', 'Tan', 'Bashkirova', 'Hendrix', 'Ehsani', 'Kembhavi', 'Plummer', 'Krishna', 'Zeng', 'Saenko', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Sat:+Dynamic+spatial+aptitude+training+for+multimodal+language+models. manually and check the results.
        -> Author(s): Arijit Ray, Jiafei Duan, Ellis Brown, Reuben Tan, Dina Bashkirova, Rose Hendrix, Kiana Ehsani, Aniruddha Kembhavi, Bryan A  Plummer, Ranjay Krishna, Kuo-Hao Zeng, and Kate Saenko
        -> Title:     Sat: Dynamic spatial aptitude training for multimodal language models.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 49/94:
  -> INFO: Now checking 1 results for matching title: 'Vlm agents generate their own memories: Distilling experience into embodied programs of thought'
       -> INFO: All authors matched!
- Checking reference 50/94:
  -> Checking if provided link is pingable: https://arxiv.
  -> INFO: Now checking 2 results for matching title: 'Deepseekmath: Pushing the limits of mathematical reasoning in open language models.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Shao', 'Wang', 'Zhu', 'Xu', 'Song', 'Bi', 'Zhang', 'Zhang', 'Li', 'Wu', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepseekmath:+Pushing+the+limits+of+mathematical+reasoning+in+open+language+models. manually and check the results.
        -> Author(s): Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al
        -> Title:     Deepseekmath: Pushing the limits of mathematical reasoning in open language models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 51/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2504.07615.
  -> INFO: Now checking 3 results for matching title: 'Vlm-r1: A stable and generalizable r1-style large vision-language model.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Shen', 'Liu', 'Li', 'Fang', 'Ma', 'Liao', 'Shen', 'Zhang', 'Zhao', 'Zhang', 'Xu', 'Zhao', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vlm-r1:+A+stable+and+generalizable+r1-style+large+vision-language+model. manually and check the results.
        -> Author(s): Haozhan Shen, Peng Liu, Jingcheng Li, Chunxin Fang, Yibo Ma, Jiajia Liao, Qiaoli Shen, Zilun Zhang, Kangjia Zhao, Qianqian Zhang, Ruochen Xu, and Tiancheng Zhao
        -> Title:     Vlm-r1: A stable and generalizable r1-style large vision-language model.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 52/94:
  -> INFO: Now checking 9 results for matching title: 'Hybridflow: A flexible and efficient rlhf framework'
       -> INFO: All authors matched!
- Checking reference 53/94:
  -> INFO: Now checking 1 results for matching title: 'RoboSpatial: Teaching spatial understanding to 2D and 3D vision-language models for robotics'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/94:
  -> INFO: Now checking 1 results for matching title: 'Vipergpt: Visual inference via python execution for reasoning'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Sur'is'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 55/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2503.20752.
  -> INFO: Now checking 10 results for matching title: 'Reason-rft: Reinforcement fine-tuning for visual reasoning.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tan', 'Ji', 'Hao', 'Lin', 'Wang', 'Wang', 'Zhang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Reason-rft:+Reinforcement+fine-tuning+for+visual+reasoning. manually and check the results.
        -> Author(s): Huajie Tan, Yuheng Ji, Xiaoshuai Hao, Minglan Lin, Pengwei Wang, Zhongyuan Wang, and Shanghang Zhang
        -> Title:     Reason-rft: Reinforcement fine-tuning for visual reasoning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 56/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2403.05530.
  -> WARNING: Skipping search (due to not enough info) for reference titled 'Al'
           -> Author(s): Gemini Team, Petko Georgiev, Ving Ian Lei, Ryan Burnell, Libin Bai, Anmol Gulati, Garrett Tanzer, and et
           -> Year: 2024
- Checking reference 57/94:
  -> Checking if provided link is pingable: https://arxiv.
  -> INFO: Now checking 10 results for matching title: 'Kimi k1'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', 'Du', 'Gao', 'Xing', 'Jiang', 'Chen', 'Li', 'Xiao', 'Du', 'Liao', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Kimi+k1 manually and check the results.
        -> Author(s): Kimi Team, A Du, B Gao, B Xing, C Jiang, C Chen, C Li, C Xiao, C Du, C Liao, et al
        -> Title:     Kimi k1
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 58/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2501.12599.
  -> INFO: Now checking 10 results for matching title: 'Kimi k1'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', 'Du', 'Gao', 'Xing', 'Jiang', 'Chen', 'Li', 'Xiao', 'Du', 'Liao', 'Tang', 'Wang', 'Zhang', 'Yuan', 'Lu', 'Tang', 'Sung', 'Wei', 'Lai', 'Guo', 'Zhu', 'Ding', 'Hu', 'Yang', 'Zhang', 'Yao', 'Zhao', 'Lu', 'Li', 'Yu', 'Gao', 'Zheng', 'Yuan', 'Chen', 'Guo', 'Su', 'Wang', 'Zhao', 'Zhang', 'Liu', 'Yan', 'Wu', 'Shi', 'Ye', 'Yu', 'Dong', 'Zhang', 'Ma', 'Pan', 'Gong', 'Liu', 'Ma', 'Wei', 'Cao', 'Huang', 'Jiang', 'Gao', 'Xiong', 'He', 'Huang', 'Wu', 'He', 'Wei', 'Jia', 'Wu', 'Xu', 'Zu', 'Zhou', 'Pan', 'Charles', 'Li', 'Hu', 'Liu', 'Chen', 'Wang', 'Liu', 'Qin', 'Liu', 'Yang', 'Bao', 'Du', 'Wu', 'Wang', 'Zhou', 'Wang', 'Li', 'Zhu', 'Zhang', 'Wang', 'Yang', 'Huang', 'Huang', 'Xu', 'Yang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Kimi+k1 manually and check the results.
        -> Author(s): Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, Chuning Tang, Congcong Wang, Dehao Zhang, Enming Yuan, Enzhe Lu, Fengxiang Tang, Flood Sung, Guangda Wei, Guokun Lai, Haiqing Guo, Han Zhu, Hao Ding, Hao Hu, Hao Yang, Hao Zhang, Haotian Yao, Haotian Zhao, Haoyu Lu, Haoze Li, Haozhen Yu, Hongcheng Gao, Huabin Zheng, Huan Yuan, Jia Chen, Jianhang Guo, Jianlin Su, Jianzhou Wang, Jie Zhao, Jin Zhang, Jingyuan Liu, Junjie Yan, Junyan Wu, Lidong Shi, Ling Ye, Longhui Yu, Mengnan Dong, Neo Zhang, Ningchen Ma, Qiwei Pan, Qucheng Gong, Shaowei Liu, Shengling Ma, Shupeng Wei, Sihan Cao, Siying Huang, Tao Jiang, Weihao Gao, Weimin Xiong, Weiran He, Weixiao Huang, Wenhao Wu, Wenyang He, Xianghui Wei, Xianqing Jia, Xingzhe Wu, Xinran Xu, Xinxing Zu, Xinyu Zhou, Xuehai Pan, Y  Charles, Yang Li, Yangyang Hu, Yangyang Liu, Yanru Chen, Yejie Wang, Yibo Liu, Yidao Qin, Yifeng Liu, Ying Yang, Yiping Bao, Yulun Du, Yuxin Wu, Yuzhi Wang, Zaida Zhou, Zhaoji Wang, Zhaowei Li, Zhen Zhu, Zheng Zhang, Zhexu Wang, Zhilin Yang, Zhiqi Huang, Zihao Huang, Ziyao Xu, and Zonghan Yang
        -> Title:     Kimi k1
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 59/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2504.07491.
  -> WARNING: Skipping search (due to not enough info) for reference titled 'Al'
           -> Author(s): Kimi Team, Angang Du, Bohong Yin, Bowei Xing, Bowen Qu, and et
           -> Year: 2025
- Checking reference 60/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2204.03162.
  -> INFO: Now checking 1 results for matching title: 'Winoground: Probing vision and language models for visio-linguistic compositionality.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Thrush', 'Jiang', 'Bartolo', 'Singh', 'Williams', 'Kiela', 'Ross', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Winoground:+Probing+vision+and+language+models+for+visio-linguistic+compositionality. manually and check the results.
        -> Author(s): Tristan Thrush, Ryan Jiang, Max Bartolo, Amanpreet Singh, Adina Williams, Douwe Kiela, and Candace Ross
        -> Title:     Winoground: Probing vision and language models for visio-linguistic compositionality.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 61/94:
  -> INFO: Now checking 10 results for matching title: 'A feature-integration theory of attention'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Treisman', 'Gelade', '1980']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+feature-integration+theory+of+attention manually and check the results.
        -> Author(s): Anne M  Treisman and Garry Gelade
        -> Title:     A feature-integration theory of attention
        -> Year:      1980
     -> Manual search was skipped by the user.
- Checking reference 62/94:
  -> INFO: Now checking 10 results for matching title: 'Visual routines'
       -> INFO: All authors matched!
- Checking reference 63/94:
  -> INFO: Now checking 1 results for matching title: 'Qwen2-vl: Enhancing visionlanguage model’s perception of the world at any resolution'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Bai', 'Tan', 'Wang', 'Fan', 'Bai', 'Chen', 'Liu', 'Wang', 'Ge', 'Fan', 'Dang', 'Du', 'Ren', 'Men', 'Liu', 'Zhou', 'Zhou', 'Lin', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Qwen2-vl:+Enhancing+visionlanguage+model’s+perception+of+the+world+at+any+resolution manually and check the results.
        -> Author(s): Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Yang Fan, Kai Dang, Mengfei Du, Xuancheng Ren, Rui Men, Dayiheng Liu, Chang Zhou, Jingren Zhou, and Junyang Lin
        -> Title:     Qwen2-vl: Enhancing visionlanguage model’s perception of the world at any resolution
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 64/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2504.20073.
  -> INFO: Now checking 5 results for matching title: 'Ragen: Understanding self-evolution in llm agents via multi-turn reinforcement learning.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Wang', 'Wang', 'Zhang', 'Li', 'Yang', 'Jin', 'Yu', 'Nguyen', 'Liu', 'Gottlieb', 'Lu', 'Cho', 'Wu', 'Fei-Fei', 'Wang', 'Choi', 'Li', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Ragen:+Understanding+self-evolution+in+llm+agents+via+multi-turn+reinforcement+learning. manually and check the results.
        -> Author(s): Zihan Wang, Kangrui Wang, Qineng Wang, Pingyue Zhang, Linjie Li, Zhengyuan Yang, Xing Jin, Kefan Yu, Minh Nhat Nguyen, Licheng Liu, Eli Gottlieb, Yiping Lu, Kyunghyun Cho, Jiajun Wu, Li Fei-Fei, Lijuan Wang, Yejin Choi, and Manling Li
        -> Title:     Ragen: Understanding self-evolution in llm agents via multi-turn reinforcement learning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 65/94:
  -> INFO: Now checking 10 results for matching title: 'Chain of thought prompting elicits reasoning in large language models'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 7)
                   Unmatched authors = 'Xia'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 66/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2303.04671.
  -> INFO: Now checking 1 results for matching title: 'Visual chatgpt: Talking, drawing and editing with visual foundation models.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'Yin', 'Qi', 'Wang', 'Tang', 'Duan', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Visual+chatgpt:+Talking%2C+drawing+and+editing+with+visual+foundation+models. manually and check the results.
        -> Author(s): Chenfei Wu, Shengming Yin, Weizhen Qi, Xiaodong Wang, Zecheng Tang, and Nan Duan
        -> Title:     Visual chatgpt: Talking, drawing and editing with visual foundation models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 67/94:
  -> INFO: Now checking 1 results for matching title: 'V*: Guided visual search as a core mechanism in multimodal llms'
       -> INFO: All authors matched!
- Checking reference 68/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2410.10630.
  -> INFO: Now checking 10 results for matching title: 'Thinking llms: General instruction following with thought generation.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'Lan', 'Yuan', 'Jiao', 'Weston', 'Sukhbaatar', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Thinking+llms:+General+instruction+following+with+thought+generation. manually and check the results.
        -> Author(s): Tianhao Wu, Janice Lan, Weizhe Yuan, Jiantao Jiao, Jason Weston, and Sainbayar Sukhbaatar
        -> Title:     Thinking llms: General instruction following with thought generation.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 69/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2404.03622.
  -> INFO: Now checking 1 results for matching title: 'Mind’s eye of llms: Visualization-of-thought elicits spatial reasoning in large language models.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'Mao', 'Zhang', 'Xia', 'Dong', 'Cui', 'Wei', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Mind’s+eye+of+llms:+Visualization-of-thought+elicits+spatial+reasoning+in+large+language+models. manually and check the results.
        -> Author(s): Wenshan Wu, Shaoguang Mao, Yadong Zhang, Yan Xia, Li Dong, Lei Cui, and Furu Wei
        -> Title:     Mind’s eye of llms: Visualization-of-thought elicits spatial reasoning in large language models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 70/94:
  -> INFO: Now checking 2 results for matching title: 'Os-atlas: A foundation action model for generalist gui agents'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 71/94:
  -> Checking if provided link is pingable: https://x.ai/blog/grok-1.5v,
  -> INFO: Now checking 10 results for matching title: 'Grok-1'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['xAI', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://x.ai/blog/grok-1.5v, manually and check the results.
        -> Author(s): xAI
        -> Title:     Grok-1
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 72/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2411.10440.
  -> INFO: Now checking 1 results for matching title: 'Llava-cot: Let vision language models reason step-by-step.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Xu', 'Jin', 'Li', 'Song', 'Sun', 'Yuan', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Llava-cot:+Let+vision+language+models+reason+step-by-step. manually and check the results.
        -> Author(s): Guowei Xu, Peng Jin, Hao Li, Yibing Song, Lichao Sun, and Li Yuan
        -> Title:     Llava-cot: Let vision language models reason step-by-step.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 73/94:
  -> INFO: Now checking 1 results for matching title: 'Thinking in space: How multimodal large language models see, remember, and recall spaces'
       -> INFO: All authors matched!
- Checking reference 74/94:
  -> INFO: Now checking 3 results for matching title: 'Active sensing in the categorization of visual patterns'
       -> INFO: All authors matched!
- Checking reference 75/94:
  -> INFO: Now checking 10 results for matching title: 'Theoretical perspectives on active sensing'
       -> INFO: All authors matched!
- Checking reference 76/94:
  -> INFO: Now checking 1 results for matching title: 'Mm-react: Prompting chatgpt for multimodal reasoning and action'
       -> INFO: All authors matched!
- Checking reference 77/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2412.18319.
  -> INFO: Now checking 1 results for matching title: 'Mulberry: Empowering mllm with o1-like reasoning and reflection via collective monte carlo tree search.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yao', 'Huang', 'Wu', 'Zhang', 'Wang', 'Liu', 'Wang', 'Song', 'Feng', 'Shen', 'Tao', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Mulberry:+Empowering+mllm+with+o1-like+reasoning+and+reflection+via+collective+monte+carlo+tree+search. manually and check the results.
        -> Author(s): Huanjin Yao, Jiaxing Huang, Wenhao Wu, Jingyi Zhang, Yibo Wang, Shunyu Liu, Yingjie Wang, Yuxin Song, Haocheng Feng, Li Shen, and Dacheng Tao
        -> Title:     Mulberry: Empowering mllm with o1-like reasoning and reflection via collective monte carlo tree search.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 78/94:
  -> INFO: Now checking 10 results for matching title: 'Eye Movements and Vision'
       -> INFO: All authors matched!
- Checking reference 79/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2502.03373.
  -> INFO: Now checking 3 results for matching title: 'Demystifying long chain-of-thought reasoning in llms.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yeo', 'Tong', 'Niu', 'Neubig', 'Yue', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Demystifying+long+chain-of-thought+reasoning+in+llms. manually and check the results.
        -> Author(s): Edward Yeo, Yuxuan Tong, Morry Niu, Graham Neubig, and Xiang Yue
        -> Title:     Demystifying long chain-of-thought reasoning in llms.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 80/94:
  -> Checking if provided link is pingable: https://arxiv.
  -> INFO: Now checking 4 results for matching title: 'Dapo: An open-source llm reinforcement learning system at scale.'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yu', 'Zhang', 'Zhu', 'Yuan', 'Zuo', 'Yue', 'Fan', 'Liu', 'Liu', 'Liu', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dapo:+An+open-source+llm+reinforcement+learning+system+at+scale. manually and check the results.
        -> Author(s): Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Tiantian Fan, Gaohong Liu, Lingjun Liu, Xin Liu, et al
        -> Title:     Dapo: An open-source llm reinforcement learning system at scale.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 81/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2311.16502.
  -> INFO: Now checking 1 results for matching title: 'Mmmu: A massive multi-discipline multimodal understanding and reasoning benchmark for expert agi.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yue', 'Ni', 'Zhang', 'Zheng', 'Liu', 'Zhang', 'Stevens', 'Jiang', 'Ren', 'Sun', 'Wei', 'Yu', 'Yuan', 'Sun', 'Yin', 'Zheng', 'Yang', 'Liu', 'Huang', 'Sun', 'Su', 'Chen', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Mmmu:+A+massive+multi-discipline+multimodal+understanding+and+reasoning+benchmark+for+expert+agi. manually and check the results.
        -> Author(s): Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu Jiang, Weiming Ren, Yuxuan Sun, Cong Wei, Botao Yu, Ruibin Yuan, Renliang Sun, Ming Yin, Boyuan Zheng, Zhenzhu Yang, Yibo Liu, Wenhao Huang, Huan Sun, Yu Su, and Wenhu Chen
        -> Title:     Mmmu: A massive multi-discipline multimodal understanding and reasoning benchmark for expert agi.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 82/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2504.13837.
  -> INFO: Now checking 1 results for matching title: 'Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model?.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yue', 'Chen', 'Lu', 'Zhao', 'Wang', 'Yue', 'Song', 'Huang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Does+reinforcement+learning+really+incentivize+reasoning+capacity+in+llms+beyond+the+base+model?. manually and check the results.
        -> Author(s): Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, and Gao Huang
        -> Title:     Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model?.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 83/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2203.14465.
  -> INFO: Now checking 7 results for matching title: 'Star: Bootstrapping reasoning with reasoning.'
  -> WARNING: None of the 7 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zelikman', 'Wu', 'Mu', 'Goodman', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Star:+Bootstrapping+reasoning+with+reasoning. manually and check the results.
        -> Author(s): Eric Zelikman, Yuhuai Wu, Jesse Mu, and Noah D  Goodman
        -> Title:     Star: Bootstrapping reasoning with reasoning.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 84/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2405.10292.
  -> INFO: Now checking 10 results for matching title: 'Fine-tuning large vision-language models as decision-making agents via reinforcement learning.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhai', 'Bai', 'Lin', 'Pan', 'Tong', 'Zhou', 'Suhr', 'Xie', 'LeCun', 'Ma', 'Levine', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Fine-tuning+large+vision-language+models+as+decision-making+agents+via+reinforcement+learning. manually and check the results.
        -> Author(s): Yuexiang Zhai, Hao Bai, Zipeng Lin, Jiayi Pan, Shengbang Tong, Yifei Zhou, Alane Suhr, Saining Xie, Yann LeCun, Yi Ma, and Sergey Levine
        -> Title:     Fine-tuning large vision-language models as decision-making agents via reinforcement learning.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 85/94:
  -> INFO: Now checking 10 results for matching title: 'Chain of preference optimization: Improving chain-of-thought reasoning in llms'
       -> INFO: All authors matched!
- Checking reference 86/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2302.00923.
  -> INFO: Now checking 10 results for matching title: 'Multimodal chain-of-thought reasoning in language models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Zhang', 'Li', 'Zhao', 'Karypis', 'Smola', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Multimodal+chain-of-thought+reasoning+in+language+models. manually and check the results.
        -> Author(s): Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis, and Alex Smola
        -> Title:     Multimodal chain-of-thought reasoning in language models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 87/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2504.12680.
  -> INFO: Now checking 1 results for matching title: 'Embodied-r: Collaborative framework for activating embodied spatial reasoning in foundation models via reinforcement learning.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhao', 'Wang', 'Fang', 'Gao', 'Man', 'Cui', 'Wang', 'Chen', 'Li', 'Zhu', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Embodied-r:+Collaborative+framework+for+activating+embodied+spatial+reasoning+in+foundation+models+via+reinforcement+learning. manually and check the results.
        -> Author(s): Baining Zhao, Ziyou Wang, Jianjie Fang, Chen Gao, Fanhang Man, Jinqiang Cui, Xin Wang, Xinlei Chen, Yong Li, and Wenwu Zhu
        -> Title:     Embodied-r: Collaborative framework for activating embodied spatial reasoning in foundation models via reinforcement learning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 88/94:
  -> INFO: Now checking 10 results for matching title: 'Instruction-guided visual masking'
       -> INFO: All authors matched!
- Checking reference 89/94:
  -> Checking if provided link is pingable: http://arxiv.org/abs/2403.13372.
  -> INFO: Now checking 10 results for matching title: 'Llamafactory: Unified efficient fine-tuning of 100+ language models'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 6)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 90/94:
  -> Checking if provided link is pingable: https://github.com/hiyouga/EasyR1,
  -> INFO: Now checking 10 results for matching title: 'Easyr1: An efficient, scalable, multi-modality rl training framework'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zheng', 'Lu', 'Feng', 'Kuang', 'Xiong', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Easyr1:+An+efficient%2C+scalable%2C+multi-modality+rl+training+framework manually and check the results.
        -> Author(s): Yaowei Zheng, Shenzhi Wang Junting Lu, Zhangchi Feng, Dongdong Kuang, and Yuwen Xiong
        -> Title:     Easyr1: An efficient, scalable, multi-modality rl training framework
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 91/94:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2405.13872.
  -> INFO: Now checking 10 results for matching title: 'Image-ofthought prompting for visual reasoning refinement in multimodal large language models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhou', 'Zhou', 'Hu', 'Lu', 'Gao', 'Zhang', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Image-ofthought+prompting+for+visual+reasoning+refinement+in+multimodal+large+language+models. manually and check the results.
        -> Author(s): Qiji Zhou, Ruochen Zhou, Zike Hu, Panzhong Lu, Siyang Gao, and Yue Zhang
        -> Title:     Image-ofthought prompting for visual reasoning refinement in multimodal large language models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 92/94:
  -> Checking if provided link is pingable: https://www.bespokelabs.ai/blog/improvingmulti-turn-tool-use-with-reinforcement-learning,
  -> INFO: Now checking 10 results for matching title: 'Improving multi-turn tool use with reinforcement learning'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhuang*', 'Vu*', 'Dimakis', 'Sathiamoorthy', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Improving+multi-turn+tool+use+with+reinforcement+learning manually and check the results.
        -> Author(s): Richard Zhuang*, Trung Vu*, Alex Dimakis, and Maheswaran Sathiamoorthy
        -> Title:     Improving multi-turn tool use with reinforcement learning
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 93/94:
  -> INFO: Now checking 10 results for matching title: '• Section A3 contains broader impacts'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['limitations', 'work', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=•+Section+A3+contains+broader+impacts manually and check the results.
        -> Author(s): A1 Appendix Overview The structure of this Appendix is as follows: • Section A2 contains limitations and future work
        -> Title:     • Section A3 contains broader impacts
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 94/94:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: 1 Group Relative Policy Optimization (GRPO) Group Relative Policy Optimization (GRPO) [50] stabilizes policy learning from long-form trajectories by computing group-normalized advantages and applying clipped token-level PPO-style updates
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['A5', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=1+Group+Relative+Policy+Optimization+(GRPO)+Group+Relative+Policy+Optimization+(GRPO)+[50]+stabilizes+policy+learning+from+long-form+trajectories+by+computing+group-normalized+advantages+and+applying+clipped+token-level+PPO-style+updates manually and check the results.
        -> Author(s): A5 Additional Methodological Details A5
        -> Title:     1 Group Relative Policy Optimization (GRPO) Group Relative Policy Optimization (GRPO) [50] stabilizes policy learning from long-form trajectories by computing group-normalized advantages and applying clipped token-level PPO-style updates
        -> Year:      0
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 19: has a scalar reward r(i) = R(τ (i)). GRPO computes the centered advantage ˆA(i) = r(i) −¯R, where
-> Invalid unicode use found on p. 19: LGRPO(θ) = −1
-> Invalid unicode use found on p. 19: t , 1−ε, 1+ε) ˆA(i)i
 -> WARNING: Found a non-breaking space that seems invalid.
 -> WARNING: Found a non-breaking space that seems invalid.
 -> WARNING: Found a non-breaking space that seems invalid.
 -> WARNING: Found a non-breaking space that seems invalid.
 -> WARNING: Found a non-breaking space that seems invalid.
 -> WARNING: Found a non-breaking space that seems invalid.
 -> WARNING: Found a non-breaking space that seems invalid.
 -> WARNING: Found a non-breaking space that seems invalid.
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 636 sentences on 11 pages -> Avg. of 64.6 sentences per page
-> Warning: Reference '9' never used in the document's text.
-> Warning: Reference '18' never used in the document's text.
-> Warning: Reference '44' never used in the document's text.
-> Warning: Reference '52' never used in the document's text.
-> Warning: Reference '64' never used in the document's text.
-> Warning: Reference '71' never used in the document's text.
-> Warning: Reference '80' never used in the document's text.
-> Warning: Reference '81' never used in the document's text.
-> Warning: Reference '89' never used in the document's text.
-> Warning: Reference '90' never used in the document's text.
-> Warning: Reference '92' never used in the document's text.
-> Warning: Reference 'a' never used in the document's text.
-> Warning: Reference 'b' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> WARNING: Reference with index 8 (Ref. ID = 9) has no associated sentence!
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
-> Missing an abstract for reference with index 40 (Ref. ID = 41); Skipping LLM check...
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
-> Missing an abstract for reference with index 57 (Ref. ID = 58); Skipping LLM check...
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
-> Missing an abstract for reference with index 61 (Ref. ID = 62); Skipping LLM check...
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 65 (Ref. ID = 66); Skipping LLM check...
-> Missing an abstract for reference with index 66 (Ref. ID = 67); Skipping LLM check...
-> Missing an abstract for reference with index 67 (Ref. ID = 68); Skipping LLM check...
-> Missing an abstract for reference with index 68 (Ref. ID = 69); Skipping LLM check...
-> Missing an abstract for reference with index 69 (Ref. ID = 70); Skipping LLM check...
-> Missing an abstract for reference with index 70 (Ref. ID = 71); Skipping LLM check...
-> Missing an abstract for reference with index 71 (Ref. ID = 72); Skipping LLM check...
-> Missing an abstract for reference with index 72 (Ref. ID = 73); Skipping LLM check...
-> Missing an abstract for reference with index 73 (Ref. ID = 74); Skipping LLM check...
-> Missing an abstract for reference with index 74 (Ref. ID = 75); Skipping LLM check...
-> Missing an abstract for reference with index 75 (Ref. ID = 76); Skipping LLM check...
-> Missing an abstract for reference with index 76 (Ref. ID = 77); Skipping LLM check...
-> Missing an abstract for reference with index 77 (Ref. ID = 78); Skipping LLM check...
-> Missing an abstract for reference with index 78 (Ref. ID = 79); Skipping LLM check...
-> Missing an abstract for reference with index 79 (Ref. ID = 80); Skipping LLM check...
-> Missing an abstract for reference with index 80 (Ref. ID = 81); Skipping LLM check...
-> Missing an abstract for reference with index 81 (Ref. ID = 82); Skipping LLM check...
-> Missing an abstract for reference with index 82 (Ref. ID = 83); Skipping LLM check...
-> Missing an abstract for reference with index 83 (Ref. ID = 84); Skipping LLM check...
-> Missing an abstract for reference with index 84 (Ref. ID = 85); Skipping LLM check...
-> Missing an abstract for reference with index 85 (Ref. ID = 86); Skipping LLM check...
-> Missing an abstract for reference with index 86 (Ref. ID = 87); Skipping LLM check...
-> Missing an abstract for reference with index 87 (Ref. ID = 88); Skipping LLM check...
-> WARNING: Reference with index 88 (Ref. ID = 89) has no associated sentence!
-> Missing an abstract for reference with index 89 (Ref. ID = 90); Skipping LLM check...
-> Missing an abstract for reference with index 90 (Ref. ID = 91); Skipping LLM check...
-> Missing an abstract for reference with index 91 (Ref. ID = 92); Skipping LLM check...
-> Missing an abstract for reference with index 92 (Ref. ID = a); Skipping LLM check...
-> Missing an abstract for reference with index 93 (Ref. ID = b); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 11 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 5 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 69 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 8
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━━━  86% 0:00:01
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 9
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━╸━━━━━━━━━━━━━━━━━━━━━━━━━━━━  30% -:--:--
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 10
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  26% -:--:--
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 11
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━╸━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  21% 0:00:53
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 12
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━  94% -:--:--
###############################
# Starting Author Check
###############################
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\8 Grounded Reinforcement Learning\PAU_results.md
```