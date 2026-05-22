
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\2 Unmasking Puppeteers\Unmasking Puppeteers ArXiv v1.pdf" 
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
- Found Introduction on page 1
- Found following heading '2 - Background and Related Work' on page 2
- Found following heading '3 - Problem Formulation' on page 3
- Found following heading '4 - Proposed Approach' on page 4
- Found following heading '5 - Experiments and Results' on page 7
- Found following heading '6 - Ablation Study' on page 8
- Found following heading '7 - Discussion' on page 9
- Found following heading '8 - Conclusion' on page 10
=> Found references/literature section on page 10
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 17
All found references: 71
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                           link  valid
0       1                              Hao Wang and Li Zhang  ...  https://ieeexplore.ieee.org/document/3214567.   None
1       2                      Min-Jun Lee and Soo-Young Kim  ...   https://ieeexplore.ieee.org/document/001234.   None
2       3                            John Smith and Jane Doe  ...  https://ieeexplore.ieee.org/document/3071234.   None
3       4  Michael Stengel, Koki Nagano, Chao Liu, Matthe...  ...                                                  None
4       5  Shwetha Rajaram, Nels Numan, Balasaravanan Tho...  ...                                                  None
..    ...                                                ...  ...                                            ...    ...
66     67  Junshu Tang, Bo Zhang, Binxin Yang, Ting Zhang...  ...                                                  None
67     68                            Fa-Ting Hong and Dan Xu  ...                                                  None
68     69  Nikita Drobyshev, Antoni Bigata Casademunt, Ko...  ...                                                  None
69     70  Stella Bounareli, Vasileios Argyriou, and Geor...  ...                                                  None
70     71  Jianzhu Guo, Dingyun Zhang, Xiaoqiang Liu, Zhi...  ...                                                  None

[71 rows x 10 columns]
- Checking reference 1/71:
  -> Checking if provided link is pingable: https://ieeexplore.ieee.org/document/3214567.
  -> INFO: Now checking 10 results for matching title: 'Synthesizing realistic avatars for enhanced virtual communication'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Synthesizing realistic avatars for enhanced virtual communication'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://ieeexplore.ieee.org/document/3214567. manually and check the results.
        -> Author(s): Hao Wang and Li Zhang
        -> Title:     Synthesizing realistic avatars for enhanced virtual communication
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 2/71:
  -> Checking if provided link is pingable: https://ieeexplore.ieee.org/document/001234.
  -> INFO: Now checking 10 results for matching title: 'Generative adversarial networks for hyper-realistic avatar creation'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Generative adversarial networks for hyper-realistic avatar creation'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://ieeexplore.ieee.org/document/001234. manually and check the results.
        -> Author(s): Min-Jun Lee and Soo-Young Kim
        -> Title:     Generative adversarial networks for hyper-realistic avatar creation
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 3/71:
  -> Checking if provided link is pingable: https://ieeexplore.ieee.org/document/3071234.
  -> INFO: Now checking 9 results for matching title: 'Deep learning techniques for avatar-based interaction in virtual environments'
  -> WARNING: None of the 9 results matched the expected title!
  -> INFO: Now checking 127 results for matching title: 'Deep learning techniques for avatar-based interaction in virtual environments'
  -> WARNING: None of the 127 results matched the expected title!
     -> You could also open https://ieeexplore.ieee.org/document/3071234. manually and check the results.
        -> Author(s): John Smith and Jane Doe
        -> Title:     Deep learning techniques for avatar-based interaction in virtual environments
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 4/71:
  -> INFO: Now checking 10 results for matching title: 'Ai-mediated 3d video conferencing'
       -> INFO: All authors matched!
- Checking reference 5/71:
  -> INFO: Now checking 2 results for matching title: 'Blendscape: Enabling unified and personalized video-conferencing environments through generative ai'
       -> INFO: All authors matched!
- Checking reference 6/71:
  -> INFO: Now checking 2 results for matching title: 'Faivconf: Face enhancement for ai-based video conference with low bit-rate'
       -> INFO: All authors matched!
- Checking reference 7/71:
  -> INFO: Now checking 1 results for matching title: 'Multimodal active speaker detection and virtual cinematography for video conferencing'
       -> INFO: All authors matched!
- Checking reference 8/71:
  -> INFO: Now checking 6 results for matching title: 'One-shot free-view neural talking-head synthesis for video conferencing'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/71:
  -> INFO: Now checking 7 results for matching title: 'Multimodal semantic communication for generative audio-driven video conferencing'
       -> INFO: All authors matched!
- Checking reference 10/71:
  -> INFO: Now checking 3 results for matching title: 'Defending low-bandwidth talking head videoconferencing systems from real-time puppeteering attacks'
       -> INFO: All authors matched!
- Checking reference 11/71:
  -> INFO: Now checking 2 results for matching title: 'Avatar fingerprinting for authorized use of synthetic talking-head videos'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/71:
  -> INFO: Now checking 6 results for matching title: 'Combining efficientnet and vision transformers for video deepfake detection'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/71:
  -> INFO: Now checking 10 results for matching title: 'Video face manipulation detection through ensemble of cnns'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 14/71:
  -> INFO: Now checking 3 results for matching title: 'Tall: Thumbnail layout for deepfake video detection'
       -> INFO: All authors matched!
- Checking reference 15/71:
  -> INFO: Now checking 3 results for matching title: 'Supervised contrastive learning for generalizable and explainable deepfakes detection'
       -> INFO: All authors matched!
- Checking reference 16/71:
  -> INFO: Now checking 3 results for matching title: 'Laa-net: Localized artifact attention network for quality-agnostic and generalizable deepfake detection'
       -> INFO: All authors matched!
- Checking reference 17/71:
  -> INFO: Now checking 3 results for matching title: 'Videofact: detecting video forgeries using attention, scene context, and forensic traces'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/71:
  -> INFO: Now checking 10 results for matching title: 'Beyond deepfake images: Detecting ai-generated videos'
       -> INFO: All authors matched!
- Checking reference 19/71:
  -> INFO: Now checking 1 results for matching title: 'Distinguish any fake videos: Unleashing the power of large-scale data and motion features'
       -> INFO: All authors matched!
- Checking reference 20/71:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: What matters in detecting ai-generated videos like sora? arXiv preprint arXiv:2406
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 7 results for matching title: 'What matters in detecting ai-generated videos like sora? arXiv preprint arXiv:2406'
  -> WARNING: None of the 7 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=What+matters+in+detecting+ai-generated+videos+like+sora?+arXiv+preprint+arXiv:2406 manually and check the results.
        -> Author(s): Chirui Chang, Zhengzhe Liu, Xiaoyang Lyu, and Xiaojuan Qi
        -> Title:     What matters in detecting ai-generated videos like sora? arXiv preprint arXiv:2406
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 21/71:
  -> INFO: Now checking 1 results for matching title: 'Towards a universal synthetic video detector: From face or background manipulations to fully ai-generated content'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 47 results for matching title: 'Towards a universal synthetic video detector: From face or background manipulations to fully ai-generated content'
  -> WARNING: None of the 47 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Towards+a+universal+synthetic+video+detector:+From+face+or+background+manipulations+to+fully+ai-generated+content manually and check the results.
        -> Author(s): Yuezun Li, Ming-Ching Chang, and Siwei Lyu
        -> Title:     Towards a universal synthetic video detector: From face or background manipulations to fully ai-generated content
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 22/71:
  -> INFO: Now checking 10 results for matching title: 'Generalizable and animatable gaussian head avatar'
       -> INFO: All authors matched!
- Checking reference 23/71:
  -> INFO: Now checking 4 results for matching title: 'Emoca: Emotion driven monocular face capture and animation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Daněček'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 24/71:
  -> INFO: Now checking 10 results for matching title: 'Audio2head: Audio-driven one-shot talking-head generation with natural head motion'
       -> INFO: All authors matched!
- Checking reference 25/71:
  -> INFO: Now checking 10 results for matching title: 'Emotalker: Audio driven emotion aware talking head generation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Khan, Elhoseiny'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/71:
  -> INFO: Now checking 4 results for matching title: 'Expressive talking head video encoding in stylegan2 latent space'
       -> INFO: All authors matched!
- Checking reference 27/71:
  -> INFO: Now checking 10 results for matching title: 'Talking-head generation with rhythmic head motion'
       -> INFO: All authors matched!
- Checking reference 28/71:
  -> INFO: Now checking 10 results for matching title: 'Compressing video calls using synthetic talking heads'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/71:
  -> INFO: Now checking 4 results for matching title: 'Depth-aware generative adversarial network for talking head video generation'
       -> INFO: All authors matched!
- Checking reference 30/71:
  -> INFO: Now checking 4 results for matching title: 'Dagan++: Depth-aware generative adversarial network for talking head video generation'
       -> INFO: All authors matched!
- Checking reference 31/71:
  -> INFO: Now checking 3 results for matching title: 'Implicit warping for animation with image sets'
       -> INFO: All authors matched!
- Checking reference 32/71:
  -> INFO: Now checking 4 results for matching title: 'Anifacegan: Animatable 3d-aware face image generation for video avatars'
       -> INFO: All authors matched!
- Checking reference 33/71:
  -> INFO: Now checking 10 results for matching title: 'Talking face generation with multilingual tts'
       -> INFO: All authors matched!
- Checking reference 34/71:
  -> INFO: Now checking 10 results for matching title: 'High-fidelity and freely controllable talking head video generation'
       -> INFO: All authors matched!
- Checking reference 35/71:
  -> INFO: Now checking 1 results for matching title: 'Discohead: Audio-and-video-driven talking head generation by disentangled control of head pose and facial expressions'
       -> INFO: All authors matched!
- Checking reference 36/71:
  -> INFO: Now checking 2 results for matching title: 'Emotivetalk: Expressive talking head generation through audio information decoupling and emotional video diffusion'
       -> INFO: All authors matched!
- Checking reference 37/71:
  -> INFO: Now checking 10 results for matching title: 'Interactive conversational head generation'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 500
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Weng', 'Li', 'Guo', 'Du', 'Niu', 'Ma', 'He', 'Wu', 'Hu', 'Yin', 'Liu', 'Liu', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Interactive+conversational+head+generation manually and check the results.
        -> Author(s): Haotian Wang, Yuzhe Weng, Yueyan Li, Zilu Guo, Jun Du, Shutong Niu, Jiefeng Ma, Shan He, Xiaoyan Wu, Qiming Hu, Bing Yin, Cong Liu, and Qingfeng Liu
        -> Title:     Interactive conversational head generation
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 38/71:
  -> INFO: Now checking 2 results for matching title: 'R2-talker: Realistic real-time talking head synthesis with hash grid landmarks encoding and progressive multilayer conditioning'
       -> INFO: All authors matched!
- Checking reference 39/71:
  -> INFO: Now checking 10 results for matching title: 'Efficient conditioned face animation using frontally-viewed embedding'
       -> INFO: All authors matched!
- Checking reference 40/71:
  -> INFO: Now checking 3 results for matching title: 'Txt2vid: Ultra-low bitrate compression of talking-head videos via text'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Doe', 'Smith', 'Turing', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Txt2vid:+Ultra-low+bitrate+compression+of+talking-head+videos+via+text manually and check the results.
        -> Author(s): John Doe, Jane Smith, and Alan Turing
        -> Title:     Txt2vid: Ultra-low bitrate compression of talking-head videos via text
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 41/71:
  -> INFO: Now checking 10 results for matching title: 'Project starline: A high-fidelity telepresence system'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Overbeck, Prives, Roth, Newman'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 42/71:
  -> INFO: Now checking 1 results for matching title: 'Fakeout: Leveraging out-of-domain self-supervision for multi-modal video deepfake detection'
       -> INFO: All authors matched!
- Checking reference 43/71:
  -> INFO: Now checking 4 results for matching title: 'Exposing gan-generated faces using inconsistent corneal specular highlights'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 44/71:
  -> INFO: Now checking 10 results for matching title: 'Detecting deep-fake videos from phonemeviseme mismatches'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Li', 'Yang', 'Sun', 'Qi', 'Lyu', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Detecting+deep-fake+videos+from+phonemeviseme+mismatches manually and check the results.
        -> Author(s): Yuezun Li, Xin Yang, Pu Sun, Honggang Qi, and Siwei Lyu
        -> Title:     Detecting deep-fake videos from phonemeviseme mismatches
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 45/71:
  -> INFO: Now checking 1 results for matching title: 'Deeprhythm: Exposing deepfakes with attentional visual heartbeat rhythms'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 16 results for matching title: 'Deeprhythm: Exposing deepfakes with attentional visual heartbeat rhythms'
  -> WARNING: None of the 16 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deeprhythm:+Exposing+deepfakes+with+attentional+visual+heartbeat+rhythms manually and check the results.
        -> Author(s): Yuezun Li, Ming-Ching Chang, and Siwei Lyu
        -> Title:     Deeprhythm: Exposing deepfakes with attentional visual heartbeat rhythms
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 46/71:
  -> INFO: Now checking 1 results for matching title: 'Fakecatcher: Detection of synthetic portrait videos using biological signals'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 47/71:
  -> INFO: Now checking 10 results for matching title: 'Capturing the lighting inconsistency for deepfake detection'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wu, Zhou, Fang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/71:
  -> INFO: Now checking 3 results for matching title: 'Illumination enlightened spatial-temporal inconsistency for deepfake video detection'
  -> WARNING: None of the 3 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Illumination enlightened spatial-temporal inconsistency for deepfake video detection'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Illumination+enlightened+spatial-temporal+inconsistency+for+deepfake+video+detection manually and check the results.
        -> Author(s): Wei-Ming Zhang, Xue-Jie Zhang, and Yu-Feng Li
        -> Title:     Illumination enlightened spatial-temporal inconsistency for deepfake video detection
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 49/71:
  -> INFO: Now checking 1 results for matching title: 'Lideepdet: Deepfake detection via image decomposition and inconsistency analysis'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Lideepdet: Deepfake detection via image decomposition and inconsistency analysis'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Lideepdet:+Deepfake+detection+via+image+decomposition+and+inconsistency+analysis manually and check the results.
        -> Author(s): Wei-Ming Zhang, Xue-Jie Zhang, and Yu-Feng Li
        -> Title:     Lideepdet: Deepfake detection via image decomposition and inconsistency analysis
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 50/71:
  -> INFO: Now checking 1 results for matching title: 'Deepfake detection by exploiting surface anomalies: The surfake approach'
       -> INFO: All authors matched!
- Checking reference 51/71:
  -> INFO: Now checking 1 results for matching title: 'Aim-bone: Texture discrepancy generation and localization for generalized deepfake detection'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Liu, Zhang, Ling, Wang, Zhang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 52/71:
  -> INFO: Now checking 6 results for matching title: 'Deepfake detection and localization using multi-view inconsistency measurement'
  -> WARNING: None of the 6 results matched the expected title!
  -> INFO: Now checking 34 results for matching title: 'Deepfake detection and localization using multi-view inconsistency measurement'
  -> WARNING: None of the 34 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepfake+detection+and+localization+using+multi-view+inconsistency+measurement manually and check the results.
        -> Author(s): Zhiwei Xiong, Wei Wang, and Xiaochun Cao
        -> Title:     Deepfake detection and localization using multi-view inconsistency measurement
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 53/71:
  -> INFO: Now checking 10 results for matching title: 'Artifacts-disentangled adversarial learning for deepfake detection'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ni, Yang, Fu, Zhao'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/71:
  -> INFO: Now checking 1 results for matching title: 'The ryerson audio-visual database of emotional speech and song (ravdess): A dynamic, multimodal set of facial and vocal expressions in north american english'
       -> INFO: All authors matched!
- Checking reference 55/71:
  -> INFO: Now checking 10 results for matching title: 'Crema-d: Crowd-sourced emotional multimodal actors dataset'
       -> INFO: All authors matched!
- Checking reference 56/71:
  -> INFO: Now checking 1 results for matching title: 'Synergizing motion and appearance: Multiscale compensatory codebooks for talking head video generation'
  -> WARNING: None of the 1 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhao', 'Hong', 'Huang', 'Xu', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Synergizing+motion+and+appearance:+Multiscale+compensatory+codebooks+for+talking+head+video+generation manually and check the results.
        -> Author(s): Shuling Zhao, Fa-Ting Hong, Xiaoshui Huang, and Dan Xu
        -> Title:     Synergizing motion and appearance: Multiscale compensatory codebooks for talking head video generation
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 57/71:
  -> INFO: Now checking 10 results for matching title: 'Say anything with any style'
       -> INFO: All authors matched!
- Checking reference 58/71:
  -> INFO: Now checking 1 results for matching title: 'Cvthead: One-shot controllable head avatar with vertex-feature transformer'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/71:
  -> INFO: Now checking 10 results for matching title: 'Learning dynamic facial radiance fields for few-shot talking head synthesis'
       -> INFO: All authors matched!
- Checking reference 60/71:
  -> INFO: Now checking 2 results for matching title: 'Sadtalker: Learning realistic 3d motion coefficients for stylized audio-driven single image talking face animation'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 61/71:
  -> INFO: Now checking 10 results for matching title: 'Latent image animator: Learning to animate images via latent space navigation'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Brémond'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 62/71:
  -> INFO: Now checking 10 results for matching title: 'Audio-visual face reenactment'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 63/71:
  -> INFO: Now checking 10 results for matching title: 'Cosface: Large margin cosine loss for deep face recognition'
       -> INFO: All authors matched!
- Checking reference 64/71:
  -> INFO: Now checking 10 results for matching title: 'Adaface: Quality adaptive margin for face recognition'
       -> INFO: All authors matched!
- Checking reference 65/71:
  -> INFO: Now checking 10 results for matching title: 'Generalization analysis for contrastive representation learning'
       -> INFO: All authors matched!
- Checking reference 66/71:
  -> INFO: Now checking 7 results for matching title: 'Understanding contrastive learning through the lens of margins'
       -> INFO: All authors matched!
- Checking reference 67/71:
  -> INFO: Now checking 10 results for matching title: '3dfaceshop: Explicitly controllable 3d-aware portrait generation'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 68/71:
  -> INFO: Now checking 2 results for matching title: 'Implicit identity representation conditioned memory compensation network for talking head video generation'
       -> INFO: All authors matched!
- Checking reference 69/71:
  -> INFO: Now checking 2 results for matching title: 'Emoportraits: Emotion-enhanced multimodal one-shot head avatars'
       -> INFO: All authors matched!
- Checking reference 70/71:
  -> INFO: Now checking 2 results for matching title: 'Finding directions in gan’s latent space for neural face reenactment'
       -> INFO: All authors matched!
- Checking reference 71/71:
  -> INFO: Now checking 1 results for matching title: 'Liveportrait: Efficient portrait animation with stitching and retargeting control'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 4: LP = 1 −b
-> Invalid unicode use found on p. 5: N −1
-> Invalid unicode use found on p. 5: each speaker’s front-facing reference portrait Rk as their pose-averaged center ||Rk −µk||2 ≤0.5°.
-> Invalid unicode use found on p. 5: ≥1 −ϵ,
-> Invalid unicode use found on p. 5: N −1
-> Invalid unicode use found on p. 5: ≤−γ,
-> Invalid unicode use found on p. 5: ≤1 −(ϵ + γ),
-> Invalid unicode use found on p. 6: LLSTM = −t log(y) −(1 −t) log(1 −y).
-> Invalid unicode use found on p. 14: −
-> Invalid unicode use found on p. 16: All vectors live on the unit hypersphere Sd−1 = {x ∈Rd : ∥x∥2 = 1}. For any
-> Invalid unicode use found on p. 16: a, b ∈Sd−1 we write ∠(a, b) = arccos
-> Invalid unicode use found on p. 16: ∠(a, b) −∠(b, c)
-> Invalid unicode use found on p. 16: cos(v+, rk) ≥1 −ε,
-> Invalid unicode use found on p. 16: N −1
-> Invalid unicode use found on p. 16: cos(v+, rℓ,p) ≤−γ,
-> Invalid unicode use found on p. 16: cos(v+, rℓ⋆,p) ≤−γ.
-> Invalid unicode use found on p. 16: θ = ∠(v+, rk) = arccos(1 −ε),
-> Invalid unicode use found on p. 16: ϕ = ∠(v+, rℓ⋆,p) ≥arccos(−γ).
-> Invalid unicode use found on p. 16: Because 1 −ε > 0 and −γ < 0, we have θ ∈[0, π
-> Invalid unicode use found on p. 16: ∠(rk, rℓ⋆,p) ≥ϕ −θ ≥arccos(−γ) −arccos(1 −ε).
-> Invalid unicode use found on p. 16: ψ = ϕ −θ > 0.
-> Invalid unicode use found on p. 16: ∠(rk, µℓ⋆) ≥ψ −ξ.
-> Invalid unicode use found on p. 16: obtains ψ −ξ ≥arccos
-> Invalid unicode use found on p. 16: 1 −(ε + γ)
-> Invalid unicode use found on p. 16: ≤1 −(ε + γ),
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
Backend tkagg is interactive backend. Turning interactive mode on.
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 593 sentences on 10 pages -> Avg. of 66.88888888888889 sentences per page
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
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
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
-> Missing an abstract for reference with index 65 (Ref. ID = 66); Skipping LLM check...
  // LLM calling counter = 17
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 67 (Ref. ID = 68); Skipping LLM check...
-> Missing an abstract for reference with index 68 (Ref. ID = 69); Skipping LLM check...
-> Missing an abstract for reference with index 69 (Ref. ID = 70); Skipping LLM check...
-> Missing an abstract for reference with index 70 (Ref. ID = 71); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 5 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 108 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 18
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 19
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 20
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 21
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━  92% 0:00:01
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 22
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
###############################
# Starting Author Check
###############################
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\2 Unmasking Puppeteers\PAU_results.md
```

---

v1:
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\2 Unmasking Puppeteers\Unmasking Puppeteers ArXiv v1.pdf"
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
- Found Introduction on page 1
- Found following heading '2 - Background and Related Work' on page 2
- Found following heading '3 - Problem Formulation' on page 3
- Found following heading '4 - Proposed Approach' on page 4
- Found following heading '5 - Experiments and Results' on page 7
- Found following heading '6 - Ablation Study' on page 8
- Found following heading '7 - Discussion' on page 9
- Found following heading '8 - Conclusion' on page 10
=> Found references/literature section on page 10
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 17
All found references: 71
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                           link  valid
0       1                              Hao Wang and Li Zhang  ...  https://ieeexplore.ieee.org/document/3214567.   None
1       2                      Min-Jun Lee and Soo-Young Kim  ...   https://ieeexplore.ieee.org/document/001234.   None
2       3                            John Smith and Jane Doe  ...  https://ieeexplore.ieee.org/document/3071234.   None
3       4  Michael Stengel, Koki Nagano, Chao Liu, Matthe...  ...                                                  None
4       5  Shwetha Rajaram, Nels Numan, Balasaravanan Tho...  ...                                                  None
..    ...                                                ...  ...                                            ...    ...
66     67  Junshu Tang, Bo Zhang, Binxin Yang, Ting Zhang...  ...                                                  None
67     68                            Fa-Ting Hong and Dan Xu  ...                                                  None
68     69  Nikita Drobyshev, Antoni Bigata Casademunt, Ko...  ...                                                  None
69     70  Stella Bounareli, Vasileios Argyriou, and Geor...  ...                                                  None
70     71  Jianzhu Guo, Dingyun Zhang, Xiaoqiang Liu, Zhi...  ...                                                  None

[71 rows x 10 columns]
- Checking reference 1/71:
  -> Checking if provided link is pingable: https://ieeexplore.ieee.org/document/3214567.
  -> INFO: Now checking 10 results for matching title: 'Synthesizing realistic avatars for enhanced virtual communication'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Synthesizing realistic avatars for enhanced virtual communication'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://ieeexplore.ieee.org/document/3214567. manually and check the results.
        -> Author(s): Hao Wang and Li Zhang
        -> Title:     Synthesizing realistic avatars for enhanced virtual communication
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 2/71:
  -> Checking if provided link is pingable: https://ieeexplore.ieee.org/document/001234.
  -> INFO: Now checking 10 results for matching title: 'Generative adversarial networks for hyper-realistic avatar creation'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Generative adversarial networks for hyper-realistic avatar creation'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://ieeexplore.ieee.org/document/001234. manually and check the results.
        -> Author(s): Min-Jun Lee and Soo-Young Kim
        -> Title:     Generative adversarial networks for hyper-realistic avatar creation
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 3/71:
  -> Checking if provided link is pingable: https://ieeexplore.ieee.org/document/3071234.
  -> INFO: Now checking 9 results for matching title: 'Deep learning techniques for avatar-based interaction in virtual environments'
  -> WARNING: None of the 9 results matched the expected title!
  -> INFO: Now checking 127 results for matching title: 'Deep learning techniques for avatar-based interaction in virtual environments'
  -> WARNING: None of the 127 results matched the expected title!
     -> You could also open https://ieeexplore.ieee.org/document/3071234. manually and check the results.
        -> Author(s): John Smith and Jane Doe
        -> Title:     Deep learning techniques for avatar-based interaction in virtual environments
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 4/71:
  -> INFO: Now checking 10 results for matching title: 'Ai-mediated 3d video conferencing'
       -> INFO: All authors matched!
- Checking reference 5/71:
  -> INFO: Now checking 2 results for matching title: 'Blendscape: Enabling unified and personalized video-conferencing environments through generative ai'
       -> INFO: All authors matched!
- Checking reference 6/71:
  -> INFO: Now checking 2 results for matching title: 'Faivconf: Face enhancement for ai-based video conference with low bit-rate'
       -> INFO: All authors matched!
- Checking reference 7/71:
  -> INFO: Now checking 1 results for matching title: 'Multimodal active speaker detection and virtual cinematography for video conferencing'
       -> INFO: All authors matched!
- Checking reference 8/71:
  -> INFO: Now checking 6 results for matching title: 'One-shot free-view neural talking-head synthesis for video conferencing'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/71:
  -> INFO: Now checking 7 results for matching title: 'Multimodal semantic communication for generative audio-driven video conferencing'
       -> INFO: All authors matched!
- Checking reference 10/71:
  -> INFO: Now checking 3 results for matching title: 'Defending low-bandwidth talking head videoconferencing systems from real-time puppeteering attacks'
       -> INFO: All authors matched!
- Checking reference 11/71:
  -> INFO: Now checking 2 results for matching title: 'Avatar fingerprinting for authorized use of synthetic talking-head videos'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/71:
  -> INFO: Now checking 6 results for matching title: 'Combining efficientnet and vision transformers for video deepfake detection'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/71:
  -> INFO: Now checking 10 results for matching title: 'Video face manipulation detection through ensemble of cnns'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 14/71:
  -> INFO: Now checking 3 results for matching title: 'Tall: Thumbnail layout for deepfake video detection'
       -> INFO: All authors matched!
- Checking reference 15/71:
  -> INFO: Now checking 3 results for matching title: 'Supervised contrastive learning for generalizable and explainable deepfakes detection'
       -> INFO: All authors matched!
- Checking reference 16/71:
  -> INFO: Now checking 3 results for matching title: 'Laa-net: Localized artifact attention network for quality-agnostic and generalizable deepfake detection'
       -> INFO: All authors matched!
- Checking reference 17/71:
  -> INFO: Now checking 3 results for matching title: 'Videofact: detecting video forgeries using attention, scene context, and forensic traces'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/71:
  -> INFO: Now checking 10 results for matching title: 'Beyond deepfake images: Detecting ai-generated videos'
       -> INFO: All authors matched!
- Checking reference 19/71:
  -> INFO: Now checking 1 results for matching title: 'Distinguish any fake videos: Unleashing the power of large-scale data and motion features'
       -> INFO: All authors matched!
- Checking reference 20/71:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: What matters in detecting ai-generated videos like sora? arXiv preprint arXiv:2406
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 7 results for matching title: 'What matters in detecting ai-generated videos like sora? arXiv preprint arXiv:2406'
  -> WARNING: None of the 7 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=What+matters+in+detecting+ai-generated+videos+like+sora?+arXiv+preprint+arXiv:2406 manually and check the results.
        -> Author(s): Chirui Chang, Zhengzhe Liu, Xiaoyang Lyu, and Xiaojuan Qi
        -> Title:     What matters in detecting ai-generated videos like sora? arXiv preprint arXiv:2406
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 21/71:
  -> INFO: Now checking 1 results for matching title: 'Towards a universal synthetic video detector: From face or background manipulations to fully ai-generated content'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 47 results for matching title: 'Towards a universal synthetic video detector: From face or background manipulations to fully ai-generated content'
  -> WARNING: None of the 47 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Towards+a+universal+synthetic+video+detector:+From+face+or+background+manipulations+to+fully+ai-generated+content manually and check the results.
        -> Author(s): Yuezun Li, Ming-Ching Chang, and Siwei Lyu
        -> Title:     Towards a universal synthetic video detector: From face or background manipulations to fully ai-generated content
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 22/71:
  -> INFO: Now checking 10 results for matching title: 'Generalizable and animatable gaussian head avatar'
       -> INFO: All authors matched!
- Checking reference 23/71:
  -> INFO: Now checking 4 results for matching title: 'Emoca: Emotion driven monocular face capture and animation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Daněček'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 24/71:
  -> INFO: Now checking 10 results for matching title: 'Audio2head: Audio-driven one-shot talking-head generation with natural head motion'
       -> INFO: All authors matched!
- Checking reference 25/71:
  -> INFO: Now checking 10 results for matching title: 'Emotalker: Audio driven emotion aware talking head generation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Khan, Elhoseiny'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/71:
  -> INFO: Now checking 4 results for matching title: 'Expressive talking head video encoding in stylegan2 latent space'
       -> INFO: All authors matched!
- Checking reference 27/71:
  -> INFO: Now checking 10 results for matching title: 'Talking-head generation with rhythmic head motion'
       -> INFO: All authors matched!
- Checking reference 28/71:
  -> INFO: Now checking 10 results for matching title: 'Compressing video calls using synthetic talking heads'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/71:
  -> INFO: Now checking 4 results for matching title: 'Depth-aware generative adversarial network for talking head video generation'
       -> INFO: All authors matched!
- Checking reference 30/71:
  -> INFO: Now checking 4 results for matching title: 'Dagan++: Depth-aware generative adversarial network for talking head video generation'
       -> INFO: All authors matched!
- Checking reference 31/71:
  -> INFO: Now checking 3 results for matching title: 'Implicit warping for animation with image sets'
       -> INFO: All authors matched!
- Checking reference 32/71:
  -> INFO: Now checking 4 results for matching title: 'Anifacegan: Animatable 3d-aware face image generation for video avatars'
       -> INFO: All authors matched!
- Checking reference 33/71:
  -> INFO: Now checking 10 results for matching title: 'Talking face generation with multilingual tts'
       -> INFO: All authors matched!
- Checking reference 34/71:
  -> INFO: Now checking 10 results for matching title: 'High-fidelity and freely controllable talking head video generation'
       -> INFO: All authors matched!
- Checking reference 35/71:
  -> INFO: Now checking 1 results for matching title: 'Discohead: Audio-and-video-driven talking head generation by disentangled control of head pose and facial expressions'
       -> INFO: All authors matched!
- Checking reference 36/71:
  -> INFO: Now checking 2 results for matching title: 'Emotivetalk: Expressive talking head generation through audio information decoupling and emotional video diffusion'
       -> INFO: All authors matched!
- Checking reference 37/71:
  -> INFO: Now checking 10 results for matching title: 'Interactive conversational head generation'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Wang', 'Weng', 'Li', 'Guo', 'Du', 'Niu', 'Ma', 'He', 'Wu', 'Hu', 'Yin', 'Liu', 'Liu', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Interactive+conversational+head+generation manually and check the results.
        -> Author(s): Haotian Wang, Yuzhe Weng, Yueyan Li, Zilu Guo, Jun Du, Shutong Niu, Jiefeng Ma, Shan He, Xiaoyan Wu, Qiming Hu, Bing Yin, Cong Liu, and Qingfeng Liu
        -> Title:     Interactive conversational head generation
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 38/71:
  -> INFO: Now checking 2 results for matching title: 'R2-talker: Realistic real-time talking head synthesis with hash grid landmarks encoding and progressive multilayer conditioning'
       -> INFO: All authors matched!
- Checking reference 39/71:
  -> INFO: Now checking 10 results for matching title: 'Efficient conditioned face animation using frontally-viewed embedding'
       -> INFO: All authors matched!
- Checking reference 40/71:
  -> INFO: Now checking 3 results for matching title: 'Txt2vid: Ultra-low bitrate compression of talking-head videos via text'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Doe', 'Smith', 'Turing', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Txt2vid:+Ultra-low+bitrate+compression+of+talking-head+videos+via+text manually and check the results.
        -> Author(s): John Doe, Jane Smith, and Alan Turing
        -> Title:     Txt2vid: Ultra-low bitrate compression of talking-head videos via text
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 41/71:
  -> INFO: Now checking 10 results for matching title: 'Project starline: A high-fidelity telepresence system'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Overbeck, Prives, Roth, Newman'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 42/71:
  -> INFO: Now checking 1 results for matching title: 'Fakeout: Leveraging out-of-domain self-supervision for multi-modal video deepfake detection'
       -> INFO: All authors matched!
- Checking reference 43/71:
  -> INFO: Now checking 4 results for matching title: 'Exposing gan-generated faces using inconsistent corneal specular highlights'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 44/71:
  -> INFO: Now checking 10 results for matching title: 'Detecting deep-fake videos from phonemeviseme mismatches'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Li', 'Yang', 'Sun', 'Qi', 'Lyu', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Detecting+deep-fake+videos+from+phonemeviseme+mismatches manually and check the results.
        -> Author(s): Yuezun Li, Xin Yang, Pu Sun, Honggang Qi, and Siwei Lyu
        -> Title:     Detecting deep-fake videos from phonemeviseme mismatches
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 45/71:
  -> INFO: Now checking 1 results for matching title: 'Deeprhythm: Exposing deepfakes with attentional visual heartbeat rhythms'
  -> WARNING: None of the 1 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Li', 'Chang', 'Lyu', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deeprhythm:+Exposing+deepfakes+with+attentional+visual+heartbeat+rhythms manually and check the results.
        -> Author(s): Yuezun Li, Ming-Ching Chang, and Siwei Lyu
        -> Title:     Deeprhythm: Exposing deepfakes with attentional visual heartbeat rhythms
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 46/71:
  -> INFO: Now checking 1 results for matching title: 'Fakecatcher: Detection of synthetic portrait videos using biological signals'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 47/71:
  -> INFO: Now checking 10 results for matching title: 'Capturing the lighting inconsistency for deepfake detection'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wu, Zhou, Fang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/71:
  -> INFO: Now checking 3 results for matching title: 'Illumination enlightened spatial-temporal inconsistency for deepfake video detection'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Zhang', 'Li', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Illumination+enlightened+spatial-temporal+inconsistency+for+deepfake+video+detection manually and check the results.
        -> Author(s): Wei-Ming Zhang, Xue-Jie Zhang, and Yu-Feng Li
        -> Title:     Illumination enlightened spatial-temporal inconsistency for deepfake video detection
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 49/71:
  -> INFO: Now checking 1 results for matching title: 'Lideepdet: Deepfake detection via image decomposition and inconsistency analysis'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Zhang', 'Li', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Lideepdet:+Deepfake+detection+via+image+decomposition+and+inconsistency+analysis manually and check the results.
        -> Author(s): Wei-Ming Zhang, Xue-Jie Zhang, and Yu-Feng Li
        -> Title:     Lideepdet: Deepfake detection via image decomposition and inconsistency analysis
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 50/71:
  -> INFO: Now checking 1 results for matching title: 'Deepfake detection by exploiting surface anomalies: The surfake approach'
       -> INFO: All authors matched!
- Checking reference 51/71:
  -> INFO: Now checking 1 results for matching title: 'Aim-bone: Texture discrepancy generation and localization for generalized deepfake detection'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Liu, Zhang, Ling, Wang, Zhang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 52/71:
  -> INFO: Now checking 6 results for matching title: 'Deepfake detection and localization using multi-view inconsistency measurement'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Xiong', 'Wang', 'Cao', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepfake+detection+and+localization+using+multi-view+inconsistency+measurement manually and check the results.
        -> Author(s): Zhiwei Xiong, Wei Wang, and Xiaochun Cao
        -> Title:     Deepfake detection and localization using multi-view inconsistency measurement
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 53/71:
  -> INFO: Now checking 10 results for matching title: 'Artifacts-disentangled adversarial learning for deepfake detection'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ni, Yang, Fu, Zhao'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/71:
  -> INFO: Now checking 1 results for matching title: 'The ryerson audio-visual database of emotional speech and song (ravdess): A dynamic, multimodal set of facial and vocal expressions in north american english'
       -> INFO: All authors matched!
- Checking reference 55/71:
  -> INFO: Now checking 10 results for matching title: 'Crema-d: Crowd-sourced emotional multimodal actors dataset'
       -> INFO: All authors matched!
- Checking reference 56/71:
  -> INFO: Now checking 1 results for matching title: 'Synergizing motion and appearance: Multiscale compensatory codebooks for talking head video generation'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhao', 'Hong', 'Huang', 'Xu', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Synergizing+motion+and+appearance:+Multiscale+compensatory+codebooks+for+talking+head+video+generation manually and check the results.
        -> Author(s): Shuling Zhao, Fa-Ting Hong, Xiaoshui Huang, and Dan Xu
        -> Title:     Synergizing motion and appearance: Multiscale compensatory codebooks for talking head video generation
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 57/71:
  -> INFO: Now checking 10 results for matching title: 'Say anything with any style'
       -> INFO: All authors matched!
- Checking reference 58/71:
  -> INFO: Now checking 1 results for matching title: 'Cvthead: One-shot controllable head avatar with vertex-feature transformer'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/71:
  -> INFO: Now checking 10 results for matching title: 'Learning dynamic facial radiance fields for few-shot talking head synthesis'
       -> INFO: All authors matched!
- Checking reference 60/71:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 2 results for matching title: 'Sadtalker: Learning realistic 3d motion coefficients for stylized audio-driven single image talking face animation'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 61/71:
  -> INFO: Now checking 10 results for matching title: 'Latent image animator: Learning to animate images via latent space navigation'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Brémond'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 62/71:
  -> INFO: Now checking 10 results for matching title: 'Audio-visual face reenactment'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 63/71:
  -> INFO: Now checking 10 results for matching title: 'Cosface: Large margin cosine loss for deep face recognition'
       -> INFO: All authors matched!
- Checking reference 64/71:
  -> INFO: Now checking 10 results for matching title: 'Adaface: Quality adaptive margin for face recognition'
       -> INFO: All authors matched!
- Checking reference 65/71:
  -> INFO: Now checking 10 results for matching title: 'Generalization analysis for contrastive representation learning'
       -> INFO: All authors matched!
- Checking reference 66/71:
  -> INFO: Now checking 7 results for matching title: 'Understanding contrastive learning through the lens of margins'
       -> INFO: All authors matched!
- Checking reference 67/71:
  -> INFO: Now checking 10 results for matching title: '3dfaceshop: Explicitly controllable 3d-aware portrait generation'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 68/71:
  -> INFO: Now checking 2 results for matching title: 'Implicit identity representation conditioned memory compensation network for talking head video generation'
       -> INFO: All authors matched!
- Checking reference 69/71:
  -> INFO: Now checking 2 results for matching title: 'Emoportraits: Emotion-enhanced multimodal one-shot head avatars'
       -> INFO: All authors matched!
- Checking reference 70/71:
  -> INFO: Now checking 2 results for matching title: 'Finding directions in gan’s latent space for neural face reenactment'
       -> INFO: All authors matched!
- Checking reference 71/71:
  -> INFO: Now checking 1 results for matching title: 'Liveportrait: Efficient portrait animation with stitching and retargeting control'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 4: LP = 1 −b
-> Invalid unicode use found on p. 5: N −1
-> Invalid unicode use found on p. 5: each speaker’s front-facing reference portrait Rk as their pose-averaged center ||Rk −µk||2 ≤0.5°.
-> Invalid unicode use found on p. 5: ≥1 −ϵ,
-> Invalid unicode use found on p. 5: N −1
-> Invalid unicode use found on p. 5: ≤−γ,
-> Invalid unicode use found on p. 5: ≤1 −(ϵ + γ),
-> Invalid unicode use found on p. 6: LLSTM = −t log(y) −(1 −t) log(1 −y).
-> Invalid unicode use found on p. 14: −
-> Invalid unicode use found on p. 16: All vectors live on the unit hypersphere Sd−1 = {x ∈Rd : ∥x∥2 = 1}. For any
-> Invalid unicode use found on p. 16: a, b ∈Sd−1 we write ∠(a, b) = arccos
-> Invalid unicode use found on p. 16: ∠(a, b) −∠(b, c)
-> Invalid unicode use found on p. 16: cos(v+, rk) ≥1 −ε,
-> Invalid unicode use found on p. 16: N −1
-> Invalid unicode use found on p. 16: cos(v+, rℓ,p) ≤−γ,
-> Invalid unicode use found on p. 16: cos(v+, rℓ⋆,p) ≤−γ.
-> Invalid unicode use found on p. 16: θ = ∠(v+, rk) = arccos(1 −ε),
-> Invalid unicode use found on p. 16: ϕ = ∠(v+, rℓ⋆,p) ≥arccos(−γ).
-> Invalid unicode use found on p. 16: Because 1 −ε > 0 and −γ < 0, we have θ ∈[0, π
-> Invalid unicode use found on p. 16: ∠(rk, rℓ⋆,p) ≥ϕ −θ ≥arccos(−γ) −arccos(1 −ε).
-> Invalid unicode use found on p. 16: ψ = ϕ −θ > 0.
-> Invalid unicode use found on p. 16: ∠(rk, µℓ⋆) ≥ψ −ξ.
-> Invalid unicode use found on p. 16: obtains ψ −ξ ≥arccos
-> Invalid unicode use found on p. 16: 1 −(ε + γ)
-> Invalid unicode use found on p. 16: ≤1 −(ε + γ),
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 593 sentences on 10 pages -> Avg. of 66.88888888888889 sentences per page
-> Warning: Reference '28' never used in the document's text.
-> Warning: Reference '29' never used in the document's text.
-> Warning: Reference '30' never used in the document's text.
-> Warning: Reference '31' never used in the document's text.
-> Warning: Reference '32' never used in the document's text.
-> Warning: Reference '33' never used in the document's text.
-> Warning: Reference '56' never used in the document's text.
-> Warning: Reference '58' never used in the document's text.
-> Warning: Reference '59' never used in the document's text.
-> Warning: Reference '60' never used in the document's text.
-> Warning: Reference '61' never used in the document's text.
-> Warning: Reference '62' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> WARNING: Reference with index 27 (Ref. ID = 28) has no associated sentence!
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
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
-> WARNING: Reference with index 57 (Ref. ID = 58) has no associated sentence!
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> WARNING: Reference with index 59 (Ref. ID = 60) has no associated sentence!
-> WARNING: Reference with index 60 (Ref. ID = 61) has no associated sentence!
-> WARNING: Reference with index 61 (Ref. ID = 62) has no associated sentence!
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
-> Missing an abstract for reference with index 65 (Ref. ID = 66); Skipping LLM check...
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 67 (Ref. ID = 68); Skipping LLM check...
-> Missing an abstract for reference with index 68 (Ref. ID = 69); Skipping LLM check...
-> Missing an abstract for reference with index 69 (Ref. ID = 70); Skipping LLM check...
-> Missing an abstract for reference with index 70 (Ref. ID = 71); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 5 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 108 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 13
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━  97% 0:00:01
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 14
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 15
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━  97% 0:00:01
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 16
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 17
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
###############################
# Starting Author Check
###############################
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\2 Unmasking Puppeteers\PAU_results.md

```

--

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\2 Unmasking Puppeteers\Unmasking Puppeteers ArXiv v1.pdf"
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
- Found Introduction on page 1
- Found following heading '2 - Background and Related Work' on page 2
- Found following heading '3 - Problem Formulation' on page 3
- Found following heading '4 - Proposed Approach' on page 4
- Found following heading '5 - Experiments and Results' on page 7
- Found following heading '6 - Ablation Study' on page 8
- Found following heading '7 - Discussion' on page 9
- Found following heading '8 - Conclusion' on page 10
=> Found references/literature section on page 10
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 17
All found references: 71
-----------
 -> Parsed references DataFrame:
   ref_id  ... valid
0       1  ...  None
1       2  ...  None
2       3  ...  None
3       4  ...  None
4       5  ...  None
..    ...  ...   ...
66     67  ...  None
67     68  ...  None
68     69  ...  None
69     70  ...  None
70     71  ...  None

[71 rows x 10 columns]
- Checking reference 1/71:
  -> Checking if provided link is pingable: https://ieeexplore.ieee.org/document/3214567.
  -> INFO: Now checking 10 results for matching title: 'Synthesizing realistic avatars for enhanced virtual communication'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zhong, Liu, Zhao, Wei'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/71:
  -> Checking if provided link is pingable: https://ieeexplore.ieee.org/document/001234.
  -> INFO: Now checking 10 results for matching title: 'Generative adversarial networks for hyper-realistic avatar creation'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'C'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/71:
  -> Checking if provided link is pingable: https://ieeexplore.ieee.org/document/3071234.
  -> INFO: Now checking 9 results for matching title: 'Deep learning techniques for avatar-based interaction in virtual environments'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Harichandana, Misra, Nagendra, Anandaraj'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/71:
  -> INFO: Now checking 10 results for matching title: 'Ai-mediated 3d video conferencing'
       -> INFO: All authors matched!
- Checking reference 5/71:
  -> INFO: Now checking 2 results for matching title: 'Blendscape: Enabling unified and personalized video-conferencing environments through generative ai'
       -> INFO: All authors matched!
- Checking reference 6/71:
  -> INFO: Now checking 2 results for matching title: 'Faivconf: Face enhancement for ai-based video conference with low bit-rate'
       -> INFO: All authors matched!
- Checking reference 7/71:
  -> INFO: Now checking 1 results for matching title: 'Multimodal active speaker detection and virtual cinematography for video conferencing'
       -> INFO: All authors matched!
- Checking reference 8/71:
  -> INFO: Now checking 6 results for matching title: 'One-shot free-view neural talking-head synthesis for video conferencing'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
       -> WARNING: Not all 10 authors from the found ref. were matched (only 5)
                   Unmatched authors = 'Zhang, Zhao, Chen, Zhang, Bo'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/71:
  -> INFO: Now checking 7 results for matching title: 'Multimodal semantic communication for generative audio-driven video conferencing'
       -> INFO: All authors matched!
- Checking reference 10/71:
  -> INFO: Now checking 3 results for matching title: 'Defending low-bandwidth talking head videoconferencing systems from real-time puppeteering attacks'
       -> INFO: All authors matched!
- Checking reference 11/71:
  -> INFO: Now checking 2 results for matching title: 'Avatar fingerprinting for authorized use of synthetic talking-head videos'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/71:
  -> INFO: Now checking 6 results for matching title: 'Combining efficientnet and vision transformers for video deepfake detection'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/71:
  -> INFO: Now checking 10 results for matching title: 'Video face manipulation detection through ensemble of cnns'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 14/71:
  -> INFO: Now checking 3 results for matching title: 'Tall: Thumbnail layout for deepfake video detection'
       -> INFO: All authors matched!
- Checking reference 15/71:
  -> INFO: Now checking 3 results for matching title: 'Supervised contrastive learning for generalizable and explainable deepfakes detection'
       -> INFO: All authors matched!
- Checking reference 16/71:
  -> INFO: Now checking 3 results for matching title: 'Laa-net: Localized artifact attention network for quality-agnostic and generalizable deepfake detection'
       -> INFO: All authors matched!
- Checking reference 17/71:
  -> INFO: Now checking 3 results for matching title: 'Videofact: detecting video forgeries using attention, scene context, and forensic traces'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2024)!
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Saga, Khalid, Sani, Abdalla, Syahputra, Wijaya'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/71:
  -> INFO: Now checking 10 results for matching title: 'Beyond deepfake images: Detecting ai-generated videos'
       -> INFO: All authors matched!
- Checking reference 19/71:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'Distinguish any fake videos: Unleashing the power of large-scale data and motion features'
       -> INFO: All authors matched!
- Checking reference 20/71:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: What matters in detecting ai-generated videos like sora? arXiv preprint arXiv:2406
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 7 results for matching title: 'What matters in detecting ai-generated videos like sora? arXiv preprint arXiv:2406'
       -> WARNING: Not all 71 authors from the found ref. were matched (only 9)
                   Unmatched authors = '0001, 0001, 0005, 0001, Zhang, Gao, Huang, Zhang, Sun, 0002, Wang, Zhang, Vidgen, Kailkhura, Xiong, Xing, Huang, 0001, 0001, 0001, Yao, Kellis, Zitnik, 0001, Bansal, 0001, 0001, 0001, 0001, 0001, Tang, 0001, Vanschoren, Mitchell, Shu, Xu, 0001, 0001, Huang, 0001, Gong, Chen, Gu, 0001, Ying, Ji, Jana, 0001, 0001, 0001, 0001, 0001, 0001, 0012, 0001, Chen, Wang, 0002, 0001, Cao, 0016, 0016'
       -> WARNING: Not all 66 authors from the found ref. were matched (only 6)
                   Unmatched authors = '0001, 0001, 0005, 0001, Zhang, Gao, Huang, 0001, 0002, Wang, 0001, Kailkhura, Xiong, Xing, Huang, 0007, 0001, 0001, 0001, Yao, Kellis, Zitnik, 0001, Bansal, 0001, 0001, 0001, 0001, 0001, 0001, Tang, 0001, Mitchell, Shu, Xu, 0001, 0001, Huang, 0001, Gong, Chen, Gu, 0001, Ying, Ji, Jana, 0001, 0001, 0001, 0001, 0001, 0001, 0012, 0001, Chen, Wang, 0002, 0001, Cao, 0016'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = '0001'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Tao, 0001, Zou, 0001'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zhao, Chu, Cao, Wu, Qin, Qin'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0010, Wang, Qiu, 0117, 0001, 0003, 0001, 0002'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 21/71:
  -> INFO: Now checking 1 results for matching title: 'Towards a universal synthetic video detector: From face or background manipulations to fully ai-generated content'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 47 results for matching title: 'Towards a universal synthetic video detector: From face or background manipulations to fully ai-generated content'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, Ye, 0001'
       -> WARNING: Not all 71 authors from the found ref. were matched (only 5)
                   Unmatched authors = '0001, 0001, 0005, 0001, Zhang, Gao, Huang, Zhang, Sun, Liu, 0002, Wang, Zhang, Vidgen, Kailkhura, Xiong, Xiao, Xing, Huang, Liu, 0001, 0001, 0001, Yao, Kellis, Zitnik, 0001, Bansal, 0001, 0001, Liu, 0001, 0001, 0001, Tang, 0001, Vanschoren, Mitchell, Shu, Xu, 0001, 0001, Huang, 0001, Gong, Chen, Gu, 0001, Ying, Ji, Jana, 0001, 0001, 0001, 0001, 0001, 0001, 0012, 0001, Chen, Wang, 0002, 0001, Cao, 0016, 0016'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 3)
                   Unmatched authors = '0001, Su, Huan, 0044, Chen, 0005, Xin, Shen'
       -> WARNING: Not all 66 authors from the found ref. were matched (only 4)
                   Unmatched authors = '0001, 0001, 0005, 0001, Zhang, Gao, Huang, 0001, Liu, 0002, Wang, 0001, Kailkhura, Xiong, Xiao, Xing, Huang, 0007, 0001, 0001, 0001, Yao, Kellis, Zitnik, 0001, Bansal, 0001, 0001, 0001, 0001, 0001, 0001, Tang, 0001, Mitchell, Shu, Xu, 0001, 0001, Huang, 0001, Gong, Chen, Gu, 0001, Ying, Ji, Jana, 0001, 0001, 0001, 0001, 0001, 0001, 0012, 0001, Chen, Wang, 0002, 0001, Cao, 0016'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 3)
                   Unmatched authors = '0044, 0001, Ma, Huang, Su, Chen, Shen'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0013, Wang, Liu, Wang, Wang, Ji'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Peng'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Zhi, Bi, 0001, Zeng, Shan, Yan, 0001, 0002, 0001'
       -> WARNING: Not all 17 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Geng, 0010, Lai, Zou, She, Guo, Zhao, 0001, Zhao, 0042, 0001, 0006, Huang'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Zhi, Bi, 0001, Zeng, Shan, Yan, 0001, 0002, 0001'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Shen, Kong, Yang, Lu, Dong, Guo, Shu, 0002, Leeser, 0001, 0001'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lv, Zhong'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Cheng, Huang, Xu, 0001, 0037, Xiang'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang, Sun, Bai, Lu'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Chiang, 0009, Banerjee, Schäf, Nguyen, Tripp'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0001, Nguyen, Hömke'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0001, Nguyen, Hömke'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang, Sun, Bai, Lu'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zhao, Gong, 0003, Hoang, Yi'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Liu, Liu, Fu, Cheng, Yin'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Song, Qin, 0003'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0010, Liu'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wen, 0014, Liang, Zhang'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Tao, 0001, Liu, Zou, 0001'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0010, Zhe, Liu, Quan'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Hu, 0002, Xiong, Wang, 0001, Guan, Hu, Fan'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0082, Xiao, Lei, Tian, 0004, Zhou, Tang, 0001'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zhao, Chu, Liu, Cao, Wu, Qin, Qin'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0010, Zhe, Liu, Quan'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zhao, Ji, Xu, 0001, Wang, 0002, Lin, Wu, Beyah'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zhou, You, 0004'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0003, Liang, 0001'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lin, Liu, Tang, Liang, Song'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Gu, Bi, Yan, 0001, Zhou, Cui, 0001, Zhang, 0001'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Xiong, Hu, Huang, 0001, Guan, Fang, Jiang, Zhou, Hu, 0002, Fan'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0001, 0001'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Tiel, Fopp, Brun, Hoogen, Karger, Casadei, Tuia, Zimmermann, Crowther, Pellissier'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Tiel, Fopp, Brun, Hoogen, Karger, Casadei, Tuia, Zimmermann, Crowther, Pellissier'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Tiel, Fopp, Brun, Hoogen, Karger, Casadei, Tuia, Zimmermann, Crowther, Pellissier'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Xiong, Hu, Huang, 0001, Guan, Fang, Jiang, Zhou, Hu, 0002, Fan'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lin, Liu, Tang, Liang, Song'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ye, Jiang, Liu'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Liu, 0001'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0003, Liang, 0001'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Hu, 0003, Huang, Sun, Zhu, Gui, Cai'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 22/71:
  -> INFO: Now checking 10 results for matching title: 'Generalizable and animatable gaussian head avatar'
       -> INFO: All authors matched!
- Checking reference 23/71:
  -> INFO: Now checking 4 results for matching title: 'Emoca: Emotion driven monocular face capture and animation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Daněček'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 24/71:
  -> INFO: Now checking 10 results for matching title: 'Audio2head: Audio-driven one-shot talking-head generation with natural head motion'
       -> INFO: All authors matched!
- Checking reference 25/71:
  -> INFO: Now checking 10 results for matching title: 'Emotalker: Audio driven emotion aware talking head generation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Khan, Elhoseiny'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Qiu, Fu, Zhang, Cao, Lai, Gao'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Xu, Cheng, Bi'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zhu, Yu, Sun, Zheng'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Yu'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Xu, Le, Shu, Tsai, Samaras'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zeng'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/71:
  -> INFO: Now checking 4 results for matching title: 'Expressive talking head video encoding in stylegan2 latent space'
       -> INFO: All authors matched!
- Checking reference 27/71:
  -> INFO: Now checking 10 results for matching title: 'Talking-head generation with rhythmic head motion'
       -> INFO: All authors matched!
- Checking reference 28/71:
  -> INFO: Now checking 10 results for matching title: 'Compressing video calls using synthetic talking heads'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2021)!
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Sen'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/71:
  -> INFO: Now checking 4 results for matching title: 'Depth-aware generative adversarial network for talking head video generation'
       -> INFO: All authors matched!
- Checking reference 30/71:
  -> INFO: Now checking 4 results for matching title: 'Dagan++: Depth-aware generative adversarial network for talking head video generation'
       -> INFO: All authors matched!
- Checking reference 31/71:
  -> INFO: Now checking 3 results for matching title: 'Implicit warping for animation with image sets'
       -> INFO: All authors matched!
- Checking reference 32/71:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 4 results for matching title: 'Anifacegan: Animatable 3d-aware face image generation for video avatars'
       -> INFO: All authors matched!
- Checking reference 33/71:
  -> INFO: Now checking 10 results for matching title: 'Talking face generation with multilingual tts'
       -> INFO: All authors matched!
- Checking reference 34/71:
  -> INFO: Now checking 10 results for matching title: 'High-fidelity and freely controllable talking head video generation'
       -> INFO: All authors matched!
- Checking reference 35/71:
  -> INFO: Now checking 1 results for matching title: 'Discohead: Audio-and-video-driven talking head generation by disentangled control of head pose and facial expressions'
       -> INFO: All authors matched!
- Checking reference 36/71:
  -> INFO: Now checking 2 results for matching title: 'Emotivetalk: Expressive talking head generation through audio information decoupling and emotional video diffusion'
       -> INFO: All authors matched!
- Checking reference 37/71:
  -> INFO: Now checking 10 results for matching title: 'Interactive conversational head generation'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Chen, Huang, Zhou, Zhang, Yang'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Zhen, Wei'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 6)
                   Unmatched authors = 'Xu'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Chen, Cui, Zhang, Zhang, Zhou, Tang, Liao, Chen'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 6)
                   Unmatched authors = 'Pan, Guan, Huang, Zhou'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zhu, Shou'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 38/71:
  -> INFO: Now checking 2 results for matching title: 'R2-talker: Realistic real-time talking head synthesis with hash grid landmarks encoding and progressive multilayer conditioning'
       -> INFO: All authors matched!
- Checking reference 39/71:
  -> INFO: Now checking 10 results for matching title: 'Efficient conditioned face animation using frontally-viewed embedding'
       -> INFO: All authors matched!
- Checking reference 40/71:
  -> INFO: Now checking 3 results for matching title: 'Txt2vid: Ultra-low bitrate compression of talking-head videos via text'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Doe', 'Smith', 'Turing', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Txt2vid:+Ultra-low+bitrate+compression+of+talking-head+videos+via+text manually and check the results.
        -> Author(s): John Doe, Jane Smith, and Alan Turing
        -> Title:     Txt2vid: Ultra-low bitrate compression of talking-head videos via text
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 41/71:
  -> INFO: Now checking 10 results for matching title: 'Project starline: A high-fidelity telepresence system'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Overbeck, Prives, Roth, Newman'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 12)
                   Unmatched authors = 'RICARDOMARTIN-BRUALLA'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 42/71:
  -> INFO: Now checking 1 results for matching title: 'Fakeout: Leveraging out-of-domain self-supervision for multi-modal video deepfake detection'
       -> INFO: All authors matched!
- Checking reference 43/71:
  -> INFO: Now checking 4 results for matching title: 'Exposing gan-generated faces using inconsistent corneal specular highlights'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Guo, Wang, Chang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 44/71:
  -> INFO: Now checking 10 results for matching title: 'Detecting deep-fake videos from phonemeviseme mismatches'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'M, J., K'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 45/71:
  -> INFO: Now checking 1 results for matching title: 'Deeprhythm: Exposing deepfakes with attentional visual heartbeat rhythms'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 16 results for matching title: 'Deeprhythm: Exposing deepfakes with attentional visual heartbeat rhythms'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zhu, Shi, Liu, Wang'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zeng, 0049, 0001, 0001, King'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zeng, 0049, 0001, 0001, King'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0006, 0001, Fan, Xu'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0006, Gan, 0001, 0001, 0001, Zhang'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, 0004, 0001, Hu, 0002, 0002, 0001, Chen'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0006, 0001, Jin'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, 0004, 0001, Hu, 0002, 0002, 0001, Chen'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0006, Gan, 0001, 0001, 0001, Zhang'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wen, Du, Cai, 0001, Qi, Lim, 0001'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 3)
                   Unmatched authors = '0001, Liu, Zhang'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Zhong, 0001'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zhang, Nie, 0001, Yang, 0001'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zhang, Nie, 0001, Yang, 0001'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang, Hu, Liu, Zhang, Liu, Gu, Huang, Zhang, Tong, Hong, Liu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 46/71:
  -> INFO: Now checking 1 results for matching title: 'Fakecatcher: Detection of synthetic portrait videos using biological signals'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 47/71:
  -> INFO: Now checking 10 results for matching title: 'Capturing the lighting inconsistency for deepfake detection'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wu, Zhou, Fang'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Liang, Tian, Yi, Alsolai, Liu, Hu'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Chen, Du, Hu, Duan, Zhu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/71:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 3 results for matching title: 'Illumination enlightened spatial-temporal inconsistency for deepfake video detection'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Liang, Tian, Yi, Alsolai, Liu, Hu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 49/71:
  -> INFO: Now checking 1 results for matching title: 'Lideepdet: Deepfake detection via image decomposition and inconsistency analysis'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lai, Wang, Wu, Jiang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 50/71:
  -> INFO: Now checking 1 results for matching title: 'Deepfake detection by exploiting surface anomalies: The surfake approach'
       -> INFO: All authors matched!
- Checking reference 51/71:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'Aim-bone: Texture discrepancy generation and localization for generalized deepfake detection'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Liu, Zhang, Ling, Wang, Zhang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 52/71:
  -> INFO: Now checking 6 results for matching title: 'Deepfake detection and localization using multi-view inconsistency measurement'
  -> WARNING: None of the 6 results matched the expected title!
  -> INFO: Now checking 34 results for matching title: 'Deepfake detection and localization using multi-view inconsistency measurement'
       -> WARNING: Not all 52 authors from the found ref. were matched (only 3)
                   Unmatched authors = '0001, Ma, Wu, Yu, 0001, 0002, Peng, Yum, Aghvami, Li, 0001, Gao, Tang, Thompson, Wong, Chen, Debbah, Dustdar, Eliassen, 0011, Duan, Sun, 0001, 0001, 0001, 0001, 0002, 0001, 0001, 0004, Ge, 0001, 0001, Zhang, Ci, Mao, Li, Shao, 0006, Liang, 0022, Wu, Sun, 0001, Liu, 0001, 0012, Gao, Shu'
       -> WARNING: Not all 101 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Vasluianu, Seizinger, Timofte, Cui, Huang, Tian, 0002, Zhang, 0003, 0002, Gustafsson, 0004, Sjölund, Schön, Dong, Zhang, Li, Leng, Yeo, Oh, Lee, Ryu, Luo, Jiang, Han, 0017, Lin, Yu, 0002, 0005, Fan, Liu, Xu, Song, 0006, Zhang, 0001, 0001, Zhao, Zheng, Gao, 0072, Ren, 0004, Kondo, Miyata, Yasue, Naruki, Ukita, Chang, Yang, Chen, Chiang, Huang, Chen, Chen, Hsieh, Kuo, Li, Fu, Liu, Ma, Fu, He, She, 0030, Nathan, Kansal, Zhang, Yang, 0059, Zhang, Phutke, Kulkarni, Khan, Murala, Vipparthi, Ye, Liu, Yang, Liu, Wu, Jing, Yu, Zheng, 0017, Long, Yao, 0004, Zhao, Ye, Shen, Li'
       -> WARNING: Not all 72 authors from the found ref. were matched (only 7)
                   Unmatched authors = '0001, Min, 0029, 0001, 0008, Timofte, Zhai, Gao, Kou, Dong, Jia, Li, 0002, Deng, 0011, 0012, 0011, 0003, 0008, Cong, 0073, Fu, Zhang, Zhang, Shi, Xu, Ma, Agarla, Celona, Rota, Schettini, Huang, 0006, Lei, Liu, Hong, Chuang, Lin, Guan, Chen, Lou, Huang, Tasi, Kao, Fan, Kong, Zhou, 0026, Lai, Chen, 0001, Chen, Zhu, Guo, Zhao, Yin, Meftah, Fezza, Hamidouche, Déforges, Shi, Mansouri, Motamednia, Bakhtiari, Aznaveh'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Yuan, Xu, Zhao, Sun, Zhou, Xu, Chen'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Li'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = '0003'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0001, Jiang, 0006, 0003'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Joshi, Gui'
       -> WARNING: Not all 31 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0001, Min, 0029, 0001, 0008, Timofte, Zhai, Gao, Kou, Dong, Jia, Li, 0011, Cong, Shi, Ma, Agarla, Huang, Liu, Chuang, Fan, Zhou, Lai, 0001, Zhu, Zhao, Meftah, Shi, Mansouri'
       -> WARNING: Not all 36 authors from the found ref. were matched (only 4)
                   Unmatched authors = '0002, Yang, Li, Zhou, Feng, Dai, Sun, Zhu, Loy, Gu, Yu, Liu, Yu, Ge, Zhang, Jia, 0042, Yin, Zuo, 0017, Lin, 0005, Jiang, Han, 0002, Luo, Yu, Fan, Liu, Guan, Xu, Yao'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Li, Hays, Ramanan, Gui'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Joshi, Gui'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Joshi, Gui'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Li, Hays, Ramanan, Gui'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Sun, 0001, Liu, Li, Shen, 0001, Gui, 0002, Keutzer, Darrell'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Li, Zheng, Guo, Yin, Xie, Yang, Han, 0004, Li, Liang'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Xu, Zhu, Zhong, Li'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Yu, Zheng, Liu, Bi, Duan, Xue, Wu, Cheng, Sun'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0003, Zhai, Xu, Zhu, 0002'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zheng, 0001, Zhang, Xing, 0012'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Chén, Bodelet, Saraiva, Phan, Di, Nagels, Schwantje, Gou, Reinen, 0002, Vos'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Jiang, Jiang, 0004, Li, Ma, Xu'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Sun, Lu, 0006, 0002, He, 0001'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Liu, 0001, 0015, 0001'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0003, Liu'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Han, Geng, Zhu'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lei, Sherratt, 0001'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Shen, 0016, Yin, Liu, Li, Guo, Huang, Zheng, Liang, 0004, 0001'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Cai, Liu, Zhang, 0001'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0003, Zhang, Zhang, Kou, Poon, Jin, 0001'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Cai, Liu, Zhang, 0001'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Xin, Zheng, Li, Liu, Huang, Shi, Xie, 0001, Li, Liao, Liang'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Shen, 0016, Yin, Liu, Li, Guo, Huang, Zheng, Liang, 0004, 0001'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0015, 0010, Zha, 0037, 0021, 0001'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 53/71:
  -> INFO: Now checking 10 results for matching title: 'Artifacts-disentangled adversarial learning for deepfake detection'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ni, Yang, Fu, Zhao'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cheng, Zhang, Zou, Yan, Liang, Wang'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Perumal'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Ren, Wang, Cao'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/71:
  -> INFO: Now checking 1 results for matching title: 'The ryerson audio-visual database of emotional speech and song (ravdess): A dynamic, multimodal set of facial and vocal expressions in north american english'
       -> INFO: All authors matched!
- Checking reference 55/71:
  -> INFO: Now checking 10 results for matching title: 'Crema-d: Crowd-sourced emotional multimodal actors dataset'
       -> INFO: All authors matched!
- Checking reference 56/71:
  -> INFO: Now checking 1 results for matching title: 'Synergizing motion and appearance: Multiscale compensatory codebooks for talking head video generation'
       -> INFO: All authors matched!
- Checking reference 57/71:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Say anything with any style'
       -> INFO: All authors matched!
- Checking reference 58/71:
  -> INFO: Now checking 1 results for matching title: 'Cvthead: One-shot controllable head avatar with vertex-feature transformer'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/71:
  -> INFO: Now checking 10 results for matching title: 'Learning dynamic facial radiance fields for few-shot talking head synthesis'
       -> INFO: All authors matched!
- Checking reference 60/71:
  -> INFO: Now checking 2 results for matching title: 'Sadtalker: Learning realistic 3d motion coefficients for stylized audio-driven single image talking face animation'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 61/71:
  -> INFO: Now checking 10 results for matching title: 'Latent image animator: Learning to animate images via latent space navigation'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Brémond'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Brémond'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Ma, Chen, Dai, Qiao'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Feng, Wu, Sun, Dong, Mian'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Jiang, Li, Lv'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zhao, Cai, Liu, Wu'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Chen, Brémond, Qiao'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ge, Zhou, Li'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 62/71:
  -> INFO: Now checking 10 results for matching title: 'Audio-visual face reenactment'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 63/71:
  -> INFO: Now checking 10 results for matching title: 'Cosface: Large margin cosine loss for deep face recognition'
       -> INFO: All authors matched!
- Checking reference 64/71:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Adaface: Quality adaptive margin for face recognition'
       -> INFO: All authors matched!
- Checking reference 65/71:
  -> INFO: Now checking 10 results for matching title: 'Generalization analysis for contrastive representation learning'
       -> INFO: All authors matched!
- Checking reference 66/71:
  -> INFO: Now checking 7 results for matching title: 'Understanding contrastive learning through the lens of margins'
       -> INFO: All authors matched!
- Checking reference 67/71:
  -> INFO: Now checking 10 results for matching title: '3dfaceshop: Explicitly controllable 3d-aware portrait generation'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
       -> WARNING: Not all 8 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Cheng, Yin, Yu, Liu, Feng'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wei, Shen'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wei, Shen'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Qiu, Liu, Fu, Cao, Lai, Gao'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zhou, Guo, Zou, Liu, Xu, Liang, Cao, Liu'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Hao, Yi, Hong, Cao, Wang, Wang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 68/71:
  -> INFO: Now checking 2 results for matching title: 'Implicit identity representation conditioned memory compensation network for talking head video generation'
       -> INFO: All authors matched!
- Checking reference 69/71:
  -> INFO: Now checking 2 results for matching title: 'Emoportraits: Emotion-enhanced multimodal one-shot head avatars'
       -> INFO: All authors matched!
- Checking reference 70/71:
  -> INFO: Now checking 2 results for matching title: 'Finding directions in gan’s latent space for neural face reenactment'
       -> INFO: All authors matched!
- Checking reference 71/71:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'Liveportrait: Efficient portrait animation with stitching and retargeting control'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 4: LP = 1 −b
-> Invalid unicode use found on p. 5: N −1
-> Invalid unicode use found on p. 5: each speaker’s front-facing reference portrait Rk as their pose-averaged center ||Rk −µk||2 ≤0.5°.
-> Invalid unicode use found on p. 5: ≥1 −ϵ,
-> Invalid unicode use found on p. 5: N −1
-> Invalid unicode use found on p. 5: ≤−γ,
-> Invalid unicode use found on p. 5: ≤1 −(ϵ + γ),
-> Invalid unicode use found on p. 6: LLSTM = −t log(y) −(1 −t) log(1 −y).
-> Invalid unicode use found on p. 14: −
-> Invalid unicode use found on p. 16: All vectors live on the unit hypersphere Sd−1 = {x ∈Rd : ∥x∥2 = 1}. For any
-> Invalid unicode use found on p. 16: a, b ∈Sd−1 we write ∠(a, b) = arccos
-> Invalid unicode use found on p. 16: ∠(a, b) −∠(b, c)
-> Invalid unicode use found on p. 16: cos(v+, rk) ≥1 −ε,
-> Invalid unicode use found on p. 16: N −1
-> Invalid unicode use found on p. 16: cos(v+, rℓ,p) ≤−γ,
-> Invalid unicode use found on p. 16: cos(v+, rℓ⋆,p) ≤−γ.
-> Invalid unicode use found on p. 16: θ = ∠(v+, rk) = arccos(1 −ε),
-> Invalid unicode use found on p. 16: ϕ = ∠(v+, rℓ⋆,p) ≥arccos(−γ).
-> Invalid unicode use found on p. 16: Because 1 −ε > 0 and −γ < 0, we have θ ∈[0, π
-> Invalid unicode use found on p. 16: ∠(rk, rℓ⋆,p) ≥ϕ −θ ≥arccos(−γ) −arccos(1 −ε).
-> Invalid unicode use found on p. 16: ψ = ϕ −θ > 0.
-> Invalid unicode use found on p. 16: ∠(rk, µℓ⋆) ≥ψ −ξ.
-> Invalid unicode use found on p. 16: obtains ψ −ξ ≥arccos
-> Invalid unicode use found on p. 16: 1 −(ε + γ)
-> Invalid unicode use found on p. 16: ≤1 −(ε + γ),
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Bracket content ['1–3'] on p. 1 could not be matched to a reference.
   -> Sentence:  This has led to the development of many new technologies, including both 
avatar-based communication systems [1–3] and AI-based videoconferencing systems [4–7]
-> Warning: Bracket content ['4–7'] on p. 1 could not be matched to a reference.
   -> Sentence:  This has led to the development of many new technologies, including both 
avatar-based communication systems [1–3] and AI-based videoconferencing systems [4–7]
-> Warning: Bracket content ['12–17'] on p. 2 could not be matched to a reference.
   -> Sentence:  While many forensic approaches, such as deepfake [12–17] and synthetic video 
detectors [18–21], aim to expose unauthorized AI-generated media, they operate by identifying 
evidence that a video has been synthetically generated
-> Warning: Bracket content ['18–21'] on p. 2 could not be matched to a reference.
   -> Sentence:  While many forensic approaches, such as deepfake [12–17] and synthetic video 
detectors [18–21], aim to expose unauthorized AI-generated media, they operate by identifying 
evidence that a video has been synthetically generated
-> Warning: Bracket content ['24–27'] on p. 2 could not be matched to a reference.
   -> Sentence:  Talking-head systems synthesize facial motion and speech in real time by 
transmitting low-dimensional embeddings of pose and expression rather than full video frames 
[24–27]
-> Warning: Bracket content ['34–40'] on p. 3 could not be matched to a reference.
   -> Sentence:  maintaining high visual fidelity [34–40]
-> Warning: Bracket content ['12–17', ' 42'] on p. 3 could not be matched to a reference.
   -> Sentence:  Deepfake detectors [12–17, 42] leverage semantic cues [43–46], lighting 
inconsistencies [47–50], and facial texture artifacts [51–53], while synthetic video detectors 
[18–21] focus on identifying AI-generated traces
-> Warning: Bracket content ['43–46'] on p. 3 could not be matched to a reference.
   -> Sentence:  Deepfake detectors [12–17, 42] leverage semantic cues [43–46], lighting 
inconsistencies [47–50], and facial texture artifacts [51–53], while synthetic video detectors 
[18–21] focus on identifying AI-generated traces
-> Warning: Bracket content ['47–50'] on p. 3 could not be matched to a reference.
   -> Sentence:  Deepfake detectors [12–17, 42] leverage semantic cues [43–46], lighting 
inconsistencies [47–50], and facial texture artifacts [51–53], while synthetic video detectors 
[18–21] focus on identifying AI-generated traces
-> Warning: Bracket content ['51–53'] on p. 3 could not be matched to a reference.
   -> Sentence:  Deepfake detectors [12–17, 42] leverage semantic cues [43–46], lighting 
inconsistencies [47–50], and facial texture artifacts [51–53], while synthetic video detectors 
[18–21] focus on identifying AI-generated traces
-> Warning: Bracket content ['18–21'] on p. 3 could not be matched to a reference.
   -> Sentence:  Deepfake detectors [12–17, 42] leverage semantic cues [43–46], lighting 
inconsistencies [47–50], and facial texture artifacts [51–53], while synthetic video detectors 
[18–21] focus on identifying AI-generated traces
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 593 sentences on 10 pages -> Avg. of 66.88888888888889 sentences per page
-> Warning: Reference '1' never used in the document's text.
-> Warning: Reference '2' never used in the document's text.
-> Warning: Reference '3' never used in the document's text.
-> Warning: Reference '4' never used in the document's text.
-> Warning: Reference '6' never used in the document's text.
-> Warning: Reference '7' never used in the document's text.
-> Warning: Reference '9' never used in the document's text.
-> Warning: Reference '17' never used in the document's text.
-> Warning: Reference '18' never used in the document's text.
-> Warning: Reference '19' never used in the document's text.
-> Warning: Reference '20' never used in the document's text.
-> Warning: Reference '21' never used in the document's text.
-> Warning: Reference '23' never used in the document's text.
-> Warning: Reference '24' never used in the document's text.
-> Warning: Reference '25' never used in the document's text.
-> Warning: Reference '26' never used in the document's text.
-> Warning: Reference '27' never used in the document's text.
-> Warning: Reference '28' never used in the document's text.
-> Warning: Reference '29' never used in the document's text.
-> Warning: Reference '30' never used in the document's text.
-> Warning: Reference '31' never used in the document's text.
-> Warning: Reference '32' never used in the document's text.
-> Warning: Reference '33' never used in the document's text.
-> Warning: Reference '34' never used in the document's text.
-> Warning: Reference '35' never used in the document's text.
-> Warning: Reference '36' never used in the document's text.
-> Warning: Reference '37' never used in the document's text.
-> Warning: Reference '38' never used in the document's text.
-> Warning: Reference '39' never used in the document's text.
-> Warning: Reference '40' never used in the document's text.
-> Warning: Reference '42' never used in the document's text.
-> Warning: Reference '43' never used in the document's text.
-> Warning: Reference '44' never used in the document's text.
-> Warning: Reference '45' never used in the document's text.
-> Warning: Reference '46' never used in the document's text.
-> Warning: Reference '47' never used in the document's text.
-> Warning: Reference '48' never used in the document's text.
-> Warning: Reference '49' never used in the document's text.
-> Warning: Reference '50' never used in the document's text.
-> Warning: Reference '51' never used in the document's text.
-> Warning: Reference '52' never used in the document's text.
-> Warning: Reference '53' never used in the document's text.
-> Warning: Reference '56' never used in the document's text.
-> Warning: Reference '58' never used in the document's text.
-> Warning: Reference '59' never used in the document's text.
-> Warning: Reference '60' never used in the document's text.
-> Warning: Reference '61' never used in the document's text.
-> Warning: Reference '62' never used in the document's text.
-> Warning: Reference '64' never used in the document's text.
-> Warning: Reference '66' never used in the document's text.
---
-> WARNING: Reference with index 0 (Ref. ID = 1) has no associated sentence!
-> WARNING: Reference with index 1 (Ref. ID = 2) has no associated sentence!
-> WARNING: Reference with index 2 (Ref. ID = 3) has no associated sentence!
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> WARNING: Reference with index 16 (Ref. ID = 17) has no associated sentence!
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> WARNING: Reference with index 22 (Ref. ID = 23) has no associated sentence!
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> WARNING: Reference with index 27 (Ref. ID = 28) has no associated sentence!
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> WARNING: Reference with index 36 (Ref. ID = 37) has no associated sentence!
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
-> WARNING: Reference with index 42 (Ref. ID = 43) has no associated sentence!
-> WARNING: Reference with index 43 (Ref. ID = 44) has no associated sentence!
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
-> WARNING: Reference with index 45 (Ref. ID = 46) has no associated sentence!
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
-> WARNING: Reference with index 47 (Ref. ID = 48) has no associated sentence!
-> WARNING: Reference with index 48 (Ref. ID = 49) has no associated sentence!
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> WARNING: Reference with index 50 (Ref. ID = 51) has no associated sentence!
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
-> WARNING: Reference with index 52 (Ref. ID = 53) has no associated sentence!
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
-> WARNING: Reference with index 57 (Ref. ID = 58) has no associated sentence!
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> WARNING: Reference with index 59 (Ref. ID = 60) has no associated sentence!
-> WARNING: Reference with index 60 (Ref. ID = 61) has no associated sentence!
-> WARNING: Reference with index 61 (Ref. ID = 62) has no associated sentence!
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
-> Missing an abstract for reference with index 65 (Ref. ID = 66); Skipping LLM check...
-> Missing an abstract for reference with index 66 (Ref. ID = 67); Skipping LLM check...
-> Missing an abstract for reference with index 67 (Ref. ID = 68); Skipping LLM check...
-> Missing an abstract for reference with index 68 (Ref. ID = 69); Skipping LLM check...
-> Missing an abstract for reference with index 69 (Ref. ID = 70); Skipping LLM check...
-> Missing an abstract for reference with index 70 (Ref. ID = 71); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 5 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 108 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 6
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 7
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 8
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 9
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 10
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━  94% 0:00:01
###############################
# Starting Author Check
###############################
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\2 Unmasking Puppeteers\PAU_results.md
```