
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\35 AI-Generated Video Detection\AI-Generated Video Detection via Perceptual Straightening.pdf"
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
 - 'authoryear_round'  = Authors' names and the year places insince round brackets (e.g., (Dignum et al., 2025))
                      -> Multiple references are separated by a semicolon (e.g., (Dignum et al. 2025; Caliskan et al. 2017))
                      -> Please note that the author and year are *not* separated
 - 'authoryear_square' = Authors' names and the year places insince square brackets (e.g., [Dignum et al., 2025])
                      -> Multiple references are separated by a comma (e.g., [Dignum et al., 2025, Caliskan et al., 2017])
                      -> Please note that the author and year are also separated by a comma
Enter a supported referencing template (['numeric', 'authoryear_round', 'authoryear_square']): numeric
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 2
- Found following heading '2 - Related work: detecting AI–generated videos' on page 3
- Found following heading '3 - Perceptual straightening definition' on page 3
- Found following heading '4 - Perceptual straightening of natural videos in DINOv2' on page 4
- Found following heading '5 - Analyzing characteristics of perceptual trajectories' on page 5
- Found following heading '6 - Video classifier to detect AI-generated content' on page 6
- Found following heading '7 - Benchmark results' on page 7
- Found following heading '8 - Discussion' on page 9
=> Found references/literature section on page 10
- Found heading after References '9 - AI Video Generation' on page 16
- Found heading after References '10 - Qualitative and Quantitative Analysis' on page 16
- Found heading after References '11 - Ablation Studies' on page 16
- Found heading after References '12 - Computational Environment' on page 16
- Found heading after References '13 - Dataset Licenses and Sources' on page 16
- Found heading after References '13 - Dataset Licenses and Sources' on page 21
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 16
All found references: 86
-> Warning: Could not parse year in reference 'OpenAI. Sora: Video generation models as world simulators.'!
-> Warning: Malformed author string: 'OpenAI'
-> Warning: Malformed author string: 'OpenAI'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                         link  valid
0       1  Olivier J Hénaff, Robbe LT Goris, and Eero P S...  ...                                                None
1       2  Olivier J Hénaff, Yoon Bai, Julie A Charlton, ...  ...                                                None
2       3                            Wenhao Wang and Yi Yang  ...  https://openreview.net/forum?id=pYNl76onJL.   None
3       4  Yingqing He, Tianyu Yang, Yong Zhang, Ying Sha...  ...                                                None
4       5  Yaohui Wang, Xinyuan Chen, Xin Ma, Shangchen Z...  ...                                                None
..    ...                                                ...  ...                                          ...    ...
81     82  Jiahao Shao, Yuanbo Yang, Hongyu Zhou, Youmin ...  ...   https://doi.org/10.48550/arXiv.2406.01493.   None
82     83  Dan Kondratyuk, Lijun Yu, Xiuye Gu, José Lezam...  ...            https://arxiv.org/abs/2312.14125.   None
83     84  Bingyi Kang, Yang Yue, Rui Lu, Zhijie Lin, Yan...  ...            https://arxiv.org/abs/2411.02385.   None
84     85                    David Ha and Jürgen Schmidhuber  ...           https://zenodo.org/record/1207631.   None
85     86  Xiaofeng Wang, Zheng Zhu, Guan Huang, Boyuan W...  ...    https://arxiv.org/abs/2401.09985.Appendix   None

[86 rows x 10 columns]
- Checking reference 1/86:
  -> INFO: Now checking 7 results for matching title: 'Perceptual straightening of natural videos'
       -> INFO: All authors matched!
- Checking reference 2/86:
  -> INFO: Now checking 10 results for matching title: 'Primary visual cortex straightens natural video trajectories'
       -> INFO: All authors matched!
- Checking reference 3/86:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=pYNl76onJL.
  -> INFO: Now checking 1 results for matching title: 'Vidprom: A million-scale real prompt-gallery dataset for text-tovideo diffusion models.'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Vidprom: A million-scale real prompt-gallery dataset for text-tovideo diffusion models.'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://openreview.net/forum?id=pYNl76onJL. manually and check the results.
        -> Author(s): Wenhao Wang and Yi Yang
        -> Title:     Vidprom: A million-scale real prompt-gallery dataset for text-tovideo diffusion models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 4/86:
  -> INFO: Now checking 10 results for matching title: 'Latent video diffusion models for high-fidelity long video generation'
       -> INFO: All authors matched!
- Checking reference 5/86:
  -> INFO: Now checking 10 results for matching title: 'Lavie: High-quality video generation with cascaded latent diffusion models'
       -> WARNING: Not all 20 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Guo, Wu, Si, Jiang, Loy, Dai, Lin, Qiao, Liu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 6/86:
  -> INFO: Now checking 1 results for matching title: 'A survey on generative ai and llm for video generation, understanding, and streaming'
       -> INFO: All authors matched!
- Checking reference 7/86:
  -> INFO: Now checking 4 results for matching title: 'Mocogan: Decomposing motion and content for video generation'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/86:
  -> Checking if provided link is pingable: https://doi.org/10.1145/3386569.3392457.
  -> INFO: Now checking 10 results for matching title: 'Learning temporal coherence via self-supervision for gan-based video generation'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Leal-Taix'e'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/86:
  -> INFO: Now checking 3 results for matching title: 'Exploring the evolution of physics cognition in video generation'
  -> WARNING: None of the 3 results matched the expected title!
  -> INFO: Now checking 25 results for matching title: 'Exploring the evolution of physics cognition in video generation'
  -> WARNING: None of the 25 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Exploring+the+evolution+of+physics+cognition+in+video+generation manually and check the results.
        -> Author(s): Wentao Lei, Jinting Wang, Fengji Ma, Guanjie Huang, and Li Liu
        -> Title:     Exploring the evolution of physics cognition in video generation
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 10/86:
  -> INFO: Now checking 10 results for matching title: 'Foundation models for video understanding: A survey'
       -> INFO: All authors matched!
- Checking reference 11/86:
  -> INFO: Now checking 3 results for matching title: 'Survey of video diffusion models: Foundations, implementations, and applications'
       -> INFO: All authors matched!
- Checking reference 12/86:
  -> INFO: Now checking 10 results for matching title: 'Denoising diffusion probabilistic models'
       -> INFO: All authors matched!
- Checking reference 13/86:
  -> INFO: Now checking 10 results for matching title: 'Attention is all you need'
       -> INFO: All authors matched!
- Checking reference 14/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2010.11929.
  -> INFO: Now checking 1 results for matching title: 'An image is worth 16x16 words: Transformers for image recognition at scale.'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'An image is worth 16x16 words: Transformers for image recognition at scale.'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 10)
                   Unmatched authors = '0003, 0001'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 15/86:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Deepfakes and synthetic media: The state of play, potential societal impacts, and policy responses
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 33 results for matching title: 'Deepfakes and synthetic media: The state of play, potential societal impacts, and policy responses'
  -> WARNING: None of the 33 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepfakes+and+synthetic+media:+The+state+of+play%2C+potential+societal+impacts%2C+and+policy+responses manually and check the results.
        -> Author(s): Mika Westerlund
        -> Title:     Deepfakes and synthetic media: The state of play, potential societal impacts, and policy responses
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 16/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2002.00133.
  -> INFO: Now checking 2 results for matching title: 'Global texture enhancement for fake face detection in the wild.'
  -> WARNING: None of the 2 results matched the expected title!
  -> INFO: Now checking 8 results for matching title: 'Global texture enhancement for fake face detection in the wild.'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0001'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0001, Jia'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2501.11340.
  -> INFO: Now checking 2 results for matching title: 'Genvidbench: A challenging benchmark for detecting ai-generated video.'
  -> WARNING: None of the 2 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ni', 'Yan', 'Huang', 'Yuan', 'Tang', 'Hu', 'Chen', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Genvidbench:+A+challenging+benchmark+for+detecting+ai-generated+video. manually and check the results.
        -> Author(s): Zhenliang Ni, Qiangyu Yan, Mouxiao Huang, Tianning Yuan, Yehui Tang, Hailin Hu, Xinghao Chen, and Yunhe Wang
        -> Title:     Genvidbench: A challenging benchmark for detecting ai-generated video.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 18/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2307.01426.
  -> INFO: Now checking 10 results for matching title: 'Deepfakebench: A comprehensive benchmark of deepfake detection.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yan', 'Zhang', 'Yuan', 'Lyu', 'Wu', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepfakebench:+A+comprehensive+benchmark+of+deepfake+detection. manually and check the results.
        -> Author(s): Zhiyuan Yan, Yong Zhang, Xinhang Yuan, Siwei Lyu, and Baoyuan Wu
        -> Title:     Deepfakebench: A comprehensive benchmark of deepfake detection.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 19/86:
  -> INFO: Now checking 10 results for matching title: 'An overview of digital video watermarking'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/86:
  -> INFO: Now checking 10 results for matching title: 'Scalable watermarking for identifying large language model outputs'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 21/86:
  -> INFO: Now checking 1 results for matching title: 'Resolving rightful ownerships with invisible watermarking techniques: Limitations, attacks, and implications'
       -> INFO: All authors matched!
- Checking reference 22/86:
  -> INFO: Now checking 1 results for matching title: 'Watermarks in the sand: Impossibility of strong watermarking for generative models'
       -> INFO: All authors matched!
- Checking reference 23/86:
  -> Checking if provided link is pingable: https://proceedings.neurips.cc/paper_files/paper/2023/file/88dddaf430b5bc38ab8228902bb61821-Paper-Conference.pdf.
  -> INFO: Now checking 1 results for matching title: 'Large language models implicitly learn to straighten neural sentence trajectories to construct a predictive representation of natural language'
       -> INFO: All authors matched!
- Checking reference 24/86:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=fYfliutfHX.
  -> INFO: Now checking 1 results for matching title: 'Learning predictable and robust neural representations by straightening image sequences'
       -> INFO: All authors matched!
- Checking reference 25/86:
  -> INFO: Now checking 10 results for matching title: 'Dinov2: Learning robust visual representations without supervision'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Oquab', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dinov2:+Learning+robust+visual+representations+without+supervision manually and check the results.
        -> Author(s): M  Oquab et al
        -> Title:     Dinov2: Learning robust visual representations without supervision
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 26/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2501.09038.
  -> INFO: Now checking 10 results for matching title: 'Do generative video models understand physical principles?.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Motamed', 'Culp', 'Swersky', 'Jaini', 'Geirhos', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Do+generative+video+models+understand+physical+principles?. manually and check the results.
        -> Author(s): Saman Motamed, Laura Culp, Kevin Swersky, Priyank Jaini, and Robert Geirhos
        -> Title:     Do generative video models understand physical principles?.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 27/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2310.17419.
  -> INFO: Now checking 1 results for matching title: 'Antifakeprompt: Prompt-tuned vision-language models are fake image detectors.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chang', 'Yeh', 'Chiu', 'Yu', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Antifakeprompt:+Prompt-tuned+vision-language+models+are+fake+image+detectors. manually and check the results.
        -> Author(s): You-Ming Chang, Chen Yeh, Wei-Chen Chiu, and Ning Yu
        -> Title:     Antifakeprompt: Prompt-tuned vision-language models are fake image detectors.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 28/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1912.11035.
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Cnngenerated images are surprisingly easy to spot
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Wang', 'Zhang', 'Owens', 'Efros', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Cnngenerated+images+are+surprisingly+easy+to+spot manually and check the results.
        -> Author(s): Sheng-Yu Wang, Oliver Wang, Richard Zhang, Andrew Owens, and Alexei A  Efros
        -> Title:     Cnngenerated images are surprisingly easy to spot
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 29/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2401.06506.
  -> INFO: Now checking 10 results for matching title: 'Frequency masking for universal deepfake detection.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Doloriel', 'Cheung', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Frequency+masking+for+universal+deepfake+detection. manually and check the results.
        -> Author(s): Chandler Timm Doloriel and Ngai-Man Cheung
        -> Title:     Frequency masking for universal deepfake detection.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 30/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2003.08685.
  -> INFO: Now checking 10 results for matching title: 'Leveraging frequency analysis for deep fake image recognition.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Frank', 'Eisenhofer', 'Schönherr', 'Fischer', 'Kolossa', 'Holz', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Leveraging+frequency+analysis+for+deep+fake+image+recognition. manually and check the results.
        -> Author(s): Joel Frank, Thorsten Eisenhofer, Lea Schönherr, Asja Fischer, Dorothea Kolossa, and Thorsten Holz
        -> Title:     Leveraging frequency analysis for deep fake image recognition.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 31/86:
  -> INFO: Now checking 8 results for matching title: 'Learning on gradients: Generalized artifacts representation for gan-generated images detection'
       -> INFO: All authors matched!
- Checking reference 32/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2311.00962.
  -> INFO: Now checking 10 results for matching title: 'Detecting generated images by real images only.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Bi', 'Liu', 'Yang', 'Xiao', 'Li', 'Huang', 'Cosman', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Detecting+generated+images+by+real+images+only. manually and check the results.
        -> Author(s): Xiuli Bi, Bo Liu, Fan Yang, Bin Xiao, Weisheng Li, Gao Huang, and Pamela C  Cosman
        -> Title:     Detecting generated images by real images only.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 33/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2302.10174.
  -> INFO: Now checking 5 results for matching title: 'Towards universal fake image detectors that generalize across generative models.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ojha', 'Li', 'Lee', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Towards+universal+fake+image+detectors+that+generalize+across+generative+models. manually and check the results.
        -> Author(s): Utkarsh Ojha, Yuheng Li, and Yong Jae Lee
        -> Title:     Towards universal fake image detectors that generalize across generative models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 34/86:
  -> INFO: Now checking 10 results for matching title: 'Tsm: Temporal shift module for efficient video understanding'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 35/86:
  -> INFO: Now checking 3 results for matching title: 'Quo vadis, action recognition? a new model and the kinetics dataset'
       -> INFO: All authors matched!
- Checking reference 36/86:
  -> INFO: Now checking 10 results for matching title: 'Slowfast networks for video recognition'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 37/86:
  -> INFO: Now checking 10 results for matching title: 'X3d: Expanding architectures for efficient video recognition'
       -> INFO: All authors matched!
- Checking reference 38/86:
  -> INFO: Now checking 1 results for matching title: 'Mvitv2: Improved multiscale vision transformers for classification and detection'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 39/86:
  -> INFO: Now checking 10 results for matching title: 'Video swin transformer'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 40/86:
  -> INFO: Now checking 1 results for matching title: 'Tall–swin: Thumbnail layout transformer for generalised deepfake video detection'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Tall–swin:+Thumbnail+layout+transformer+for+generalised+deepfake+video+detection manually and check the results.
        -> Author(s): Jiahui Liu and et al
        -> Title:     Tall–swin: Thumbnail layout transformer for generalised deepfake video detection
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 41/86:
  -> INFO: Now checking 10 results for matching title: 'Temporal pyramid network for action recognition'
       -> INFO: All authors matched!
- Checking reference 42/86:
  -> INFO: Now checking 1 results for matching title: 'Uniformerv2: Spatiotemporal learning by arming image vits with video uniformer'
       -> INFO: All authors matched!
- Checking reference 43/86:
  -> INFO: Now checking 1 results for matching title: 'Is space-time attention all you need for video understanding? In ICML.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Bertasius', 'Wang', 'Torresani', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Is+space-time+attention+all+you+need+for+video+understanding?+In+ICML. manually and check the results.
        -> Author(s): Gedas Bertasius, Heng Wang, and Lorenzo Torresani
        -> Title:     Is space-time attention all you need for video understanding? In ICML.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 44/86:
  -> Checking if provided link is pingable: https://pikalabs.com.
  -> INFO: Now checking 10 results for matching title: 'Pika labs'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://pikalabs.com. manually and check the results.
        -> Author(s): Pika Labs Team
        -> Title:     Pika labs
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 45/86:
  -> Checking if provided link is pingable: https://doi.org/10.1016/j.cviu.2024.103997.
  -> INFO: Now checking 3 results for matching title: 'The 2023 video similarity dataset and challenge'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 46/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2209.14792.
  -> INFO: Now checking 10 results for matching title: 'Make-a-video: Text-to-video generation without text-video data.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Singer', 'Polyak', 'Hayes', 'Yin', 'An', 'Zhang', 'Hu', 'Yang', 'Ashual', 'Gafni', 'Parikh', 'Gupta', 'Taigman', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Make-a-video:+Text-to-video+generation+without+text-video+data. manually and check the results.
        -> Author(s): Uriel Singer, Adam Polyak, Thomas Hayes, Xi Yin, Jie An, Songyang Zhang, Qiyuan Hu, Harry Yang, Oron Ashual, Oran Gafni, Devi Parikh, Sonal Gupta, and Yaniv Taigman
        -> Title:     Make-a-video: Text-to-video generation without text-video data.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 47/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2308.06571.
  -> INFO: Now checking 10 results for matching title: 'Modelscope text-to-video technical report.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Yuan', 'Chen', 'Zhang', 'Wang', 'Zhang', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Modelscope+text-to-video+technical+report. manually and check the results.
        -> Author(s): Jiuniu Wang, Hangjie Yuan, Dayou Chen, Yingya Zhang, Xiang Wang, and Shiwei Zhang
        -> Title:     Modelscope text-to-video technical report.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 48/86:
  -> Checking if provided link is pingable: https://openai.com,
  -> INFO: Now checking 10 results for matching title: 'Sora: Video generation models as world simulators'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['OpenAI', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Sora:+Video+generation+models+as+world+simulators manually and check the results.
        -> Author(s): OpenAI
        -> Title:     Sora: Video generation models as world simulators
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 49/86:
  -> Checking if provided link is pingable: https://runwayml.com.
  -> INFO: Now checking 10 results for matching title: 'Runway'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://runwayml.com. manually and check the results.
        -> Author(s): Runway Team
        -> Title:     Runway
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 50/86:
  -> INFO: Now checking 10 results for matching title: 'Imagenet classification with deep convolutional neural networks'
       -> INFO: All authors matched!
- Checking reference 51/86:
  -> INFO: Now checking 10 results for matching title: 'Very deep convolutional networks for large-scale image recognition'
       -> INFO: All authors matched!
- Checking reference 52/86:
  -> INFO: Now checking 10 results for matching title: 'Deep residual learning for image recognition'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 53/86:
  -> INFO: Now checking 5 results for matching title: 'Imagenet-trained cnns are biased towards texture; increasing shape bias improves accuracy and robustness'
       -> INFO: All authors matched!
- Checking reference 54/86:
  -> INFO: Now checking 5 results for matching title: 'A simple framework for contrastive learning of visual representations'
       -> INFO: All authors matched!
- Checking reference 55/86:
  -> INFO: Now checking 10 results for matching title: 'Bootstrap your own latent-a new approach to self-supervised learning'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Grill', 'Strub', 'Altché', 'Tallec', 'Richemond', 'Buchatskaya', 'Doersch', 'Pires', 'Guo', 'Azar', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Bootstrap+your+own+latent-a+new+approach+to+self-supervised+learning manually and check the results.
        -> Author(s): Jean-Bastien Grill, Florian Strub, Florent Altché, Corentin Tallec, Pierre Richemond, Elena Buchatskaya, Carl Doersch, Bernardo Avila Pires, Zhaohan Guo, Mohammad Gheshlaghi Azar, et al
        -> Title:     Bootstrap your own latent-a new approach to self-supervised learning
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 56/86:
  -> INFO: Now checking 10 results for matching title: 'Learning transferable visual models from natural language supervision'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 57/86:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Videocrafter: A diffusion-based toolkit for high-quality video generation
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chen', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Videocrafter:+A+diffusion-based+toolkit+for+high-quality+video+generation manually and check the results.
        -> Author(s): Y  Chen et al
        -> Title:     Videocrafter: A diffusion-based toolkit for high-quality video generation
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 58/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2303.13439.
  -> INFO: Now checking 6 results for matching title: 'Text2video-zero: Text-to-image diffusion models are zero-shot video generators.'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Khachatryan', 'Movsisyan', 'Tadevosyan', 'Henschel', 'Wang', 'Navasardyan', 'Shi', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Text2video-zero:+Text-to-image+diffusion+models+are+zero-shot+video+generators. manually and check the results.
        -> Author(s): Levon Khachatryan, Andranik Movsisyan, Vahram Tadevosyan, Roberto Henschel, Zhangyang Wang, Shant Navasardyan, and Humphrey Shi
        -> Title:     Text2video-zero: Text-to-image diffusion models are zero-shot video generators.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 59/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2401.09047.
  -> INFO: Now checking 10 results for matching title: 'Videocrafter2: Overcoming data limitations for high-quality video diffusion models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chen', 'Zhang', 'Cun', 'Xia', 'Wang', 'Weng', 'Shan', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Videocrafter2:+Overcoming+data+limitations+for+high-quality+video+diffusion+models. manually and check the results.
        -> Author(s): Haoxin Chen, Yong Zhang, Xiaodong Cun, Menghan Xia, Xintao Wang, Chao Weng, and Ying Shan
        -> Title:     Videocrafter2: Overcoming data limitations for high-quality video diffusion models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 60/86:
  -> Checking if provided link is pingable: https://openai.com/index/sora/.
  -> INFO: Now checking 10 results for matching title: 'Sora: OpenAI’s Multimodal Agent'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['OpenAI', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://openai.com/index/sora/. manually and check the results.
        -> Author(s): OpenAI
        -> Title:     Sora: OpenAI’s Multimodal Agent
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 61/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2403.05530.
  -> INFO: Now checking 10 results for matching title: 'Gemini 1'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', 'Georgiev', 'authors', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gemini+1 manually and check the results.
        -> Author(s): Gemini Team, Petko Georgiev, and 1133 other authors
        -> Title:     Gemini 1
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 62/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2301.00704.
  -> INFO: Now checking 4 results for matching title: 'Muse: Text-to-image generation via masked generative transformers.'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chang', 'Zhang', 'Barber', 'Maschinot', 'Lezama', 'Jiang', 'Yang', 'Murphy', 'Freeman', 'Rubinstein', 'Li', 'Krishnan', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Muse:+Text-to-image+generation+via+masked+generative+transformers. manually and check the results.
        -> Author(s): Huiwen Chang, Han Zhang, Jarred Barber, AJ Maschinot, Jose Lezama, Lu Jiang, MingHsuan Yang, Kevin Murphy, William T  Freeman, Michael Rubinstein, Yuanzhen Li, and Dilip Krishnan
        -> Title:     Muse: Text-to-image generation via masked generative transformers.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 63/86:
  -> INFO: Now checking 10 results for matching title: 'Stable video diffusion'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Blattmann', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Stable+video+diffusion manually and check the results.
        -> Author(s): Christian Blattmann et al
        -> Title:     Stable video diffusion
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 64/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2205.15868.
  -> INFO: Now checking 2 results for matching title: 'Cogvideo: Large-scale pretraining for text-to-video generation via transformers.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hong', 'Ding', 'Zheng', 'Liu', 'Tang', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Cogvideo:+Large-scale+pretraining+for+text-to-video+generation+via+transformers. manually and check the results.
        -> Author(s): Wenyi Hong, Ming Ding, Wendi Zheng, Xinghan Liu, and Jie Tang
        -> Title:     Cogvideo: Large-scale pretraining for text-to-video generation via transformers.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 65/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2403.13248.
  -> INFO: Now checking 1 results for matching title: 'Mora: Enabling generalist video generation via a multi-agent framework.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yuan', 'Liu', 'Cao', 'Sun', 'Jia', 'Chen', 'Li', 'Lin', 'Yuan', 'He', 'Wang', 'Ye', 'Sun', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Mora:+Enabling+generalist+video+generation+via+a+multi-agent+framework. manually and check the results.
        -> Author(s): Zhengqing Yuan, Yixin Liu, Yihan Cao, Weixiang Sun, Haolong Jia, Ruoxi Chen, Zhaoxu Li, Bin Lin, Li Yuan, Lifang He, Chi Wang, Yanfang Ye, and Lichao Sun
        -> Title:     Mora: Enabling generalist video generation via a multi-agent framework.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 66/86:
  -> INFO: Now checking 1 results for matching title: 'Towards nonlinear disentanglement in natural data with temporal sparse coding'
       -> INFO: All authors matched!
- Checking reference 67/86:
  -> INFO: Now checking 1 results for matching title: 'Evidence for an intuitive physics engine in the human brain'
       -> INFO: All authors matched!
- Checking reference 68/86:
  -> INFO: Now checking 3 results for matching title: 'The psychology of causal perception and reasoning'
       -> INFO: All authors matched!
- Checking reference 69/86:
  -> INFO: Now checking 10 results for matching title: 'Learning and using the arrow of time'
       -> INFO: All authors matched!
- Checking reference 70/86:
  -> INFO: Now checking 1 results for matching title: 'Perceiving the arrow of time in autoregressive motion'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Scholkopf'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 71/86:
  -> INFO: Now checking 1 results for matching title: 'The social harms of ai-generated fake news: Addressing deepfake and ai political manipulation'
       -> INFO: All authors matched!
- Checking reference 72/86:
  -> Checking if provided link is pingable: https://globaltaiwan.org/2025/05/the-malicious-exploitation-of-deepfake-technology/.Accessed
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: The Malicious Exploitation of Deepfake Technology: Political Manipulation, Disinformation, and Privacy Violations in Taiwan
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tulga', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://globaltaiwan.org/2025/05/the-malicious-exploitation-of-deepfake-technology/.Accessed manually and check the results.
        -> Author(s): Ahmet Yi˘gitalp Tulga
        -> Title:     The Malicious Exploitation of Deepfake Technology: Political Manipulation, Disinformation, and Privacy Violations in Taiwan
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 73/86:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Fraud attempts with deepfakes have increased by 2137% over the last three years
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tulga', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Fraud+attempts+with+deepfakes+have+increased+by+2137%+over+the+last+three+years manually and check the results.
        -> Author(s): Ahmet Tulga
        -> Title:     Fraud attempts with deepfakes have increased by 2137% over the last three years
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 74/86:
  -> INFO: Now checking 10 results for matching title: 'Data-Driven Fairness Generalization for Deepfake Detection.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Masood', 'Guri', 'Nadimpalli', 'Ju', 'Lyu', 'Rattani', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Data-Driven+Fairness+Generalization+for+Deepfake+Detection. manually and check the results.
        -> Author(s): Madeeha Masood, Mehar Guri, S L V Swetha Nadimpalli, Yan Ju, Siwei Lyu, and Ajita Rattani
        -> Title:     Data-Driven Fairness Generalization for Deepfake Detection.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 75/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2405.10271.
  -> INFO: Now checking 10 results for matching title: 'Federated hybrid model pruning through loss landscape exploration.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Internò', 'Raponi', 'Stein', 'Bäck', 'Olhofer', 'Jin', 'Hammer', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Federated+hybrid+model+pruning+through+loss+landscape+exploration. manually and check the results.
        -> Author(s): Christian Internò, Elena Raponi, Niki van Stein, Thomas Bäck, Markus Olhofer, Yaochu Jin, and Barbara Hammer
        -> Title:     Federated hybrid model pruning through loss landscape exploration.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 76/86:
  -> INFO: Now checking 3 results for matching title: 'Federated loss exploration for improved convergence on non-iid data'
       -> INFO: All authors matched!
- Checking reference 77/86:
  -> INFO: Now checking 2 results for matching title: 'Adoption of Watermarking for Generative AI Systems in Practice and Implications under the new EU AI Act.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Bird', 'Surden', 'Saveliev', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Adoption+of+Watermarking+for+Generative+AI+Systems+in+Practice+and+Implications+under+the+new+EU+AI+Act. manually and check the results.
        -> Author(s): Eliza Bird, Harry Surden, and Alex Saveliev
        -> Title:     Adoption of Watermarking for Generative AI Systems in Practice and Implications under the new EU AI Act.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 78/86:
  -> INFO: Now checking 10 results for matching title: 'Generating videos with scene dynamics'
       -> INFO: All authors matched!
- Checking reference 79/86:
  -> INFO: Now checking 10 results for matching title: 'Stochastic variational video prediction'
       -> INFO: All authors matched!
- Checking reference 80/86:
  -> INFO: Now checking 10 results for matching title: 'Highresolution image synthesis with latent diffusion models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Rombach', 'Blattmann', 'Lorenz', 'Esser', 'Ommer', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Highresolution+image+synthesis+with+latent+diffusion+models manually and check the results.
        -> Author(s): Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer
        -> Title:     Highresolution image synthesis with latent diffusion models
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 81/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2210.02303.
  -> INFO: Now checking 10 results for matching title: 'Imagen video: High definition video generation with diffusion models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ho', 'Chan', 'Saharia', 'Whang', 'Gao', 'Gritsenko', 'Kingma', 'Poole', 'Norouzi', 'Fleet', 'Salimans', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Imagen+video:+High+definition+video+generation+with+diffusion+models. manually and check the results.
        -> Author(s): Jonathan Ho, William Chan, Chitwan Saharia, Jay Whang, Ruiqi Gao, Alexey Gritsenko, Diederik P  Kingma, Ben Poole, Mohammad Norouzi, David J  Fleet, and Tim Salimans
        -> Title:     Imagen video: High definition video generation with diffusion models.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 82/86:
  -> Checking if provided link is pingable: https://doi.org/10.48550/arXiv.2406.01493.
  -> INFO: Now checking 10 results for matching title: 'Learning temporally consistent video depth from video diffusion priors'
       -> INFO: All authors matched!
- Checking reference 83/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2312.14125.
  -> INFO: Now checking 3 results for matching title: 'Videopoet: A large language model for zero-shot video generation.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kondratyuk', 'Yu', 'Gu', 'Lezama', 'Huang', 'Schindler', 'Hornung', 'Birodkar', 'Yan', 'Chiu', 'Somandepalli', 'Akbari', 'Alon', 'Cheng', 'Dillon', 'Gupta', 'Hahn', 'Hauth', 'Hendon', 'Martinez', 'Minnen', 'Sirotenko', 'Sohn', 'Yang', 'Adam', 'Yang', 'Essa', 'Wang', 'Ross', 'Seybold', 'Jiang', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Videopoet:+A+large+language+model+for+zero-shot+video+generation. manually and check the results.
        -> Author(s): Dan Kondratyuk, Lijun Yu, Xiuye Gu, José Lezama, Jonathan Huang, Grant Schindler, Rachel Hornung, Vighnesh Birodkar, Jimmy Yan, Ming-Chang Chiu, Krishna Somandepalli, Hassan Akbari, Yair Alon, Yong Cheng, Josh Dillon, Agrim Gupta, Meera Hahn, Anja Hauth, David Hendon, Alonso Martinez, David Minnen, Mikhail Sirotenko, Kihyuk Sohn, Xuan Yang, Hartwig Adam, Ming-Hsuan Yang, Irfan Essa, Huisheng Wang, David A  Ross, Bryan Seybold, and Lu Jiang
        -> Title:     Videopoet: A large language model for zero-shot video generation.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 84/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2411.02385.
  -> INFO: Now checking 10 results for matching title: 'How far is video generation from world model: A physical law perspective.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kang', 'Yue', 'Lu', 'Lin', 'Zhao', 'Wang', 'Huang', 'Feng', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=How+far+is+video+generation+from+world+model:+A+physical+law+perspective. manually and check the results.
        -> Author(s): Bingyi Kang, Yang Yue, Rui Lu, Zhijie Lin, Yang Zhao, Kaixin Wang, Gao Huang, and Jiashi Feng
        -> Title:     How far is video generation from world model: A physical law perspective.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 85/86:
  -> Checking if provided link is pingable: https://zenodo.org/record/1207631.
  -> INFO: Now checking 10 results for matching title: 'World models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ha', 'Schmidhuber', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://zenodo.org/record/1207631. manually and check the results.
        -> Author(s): David Ha and Jürgen Schmidhuber
        -> Title:     World models
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 86/86:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2401.09985.Appendix
  -> INFO: Now checking 1 results for matching title: 'Worlddreamer: Towards general world models for video generation via predicting masked tokens.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Zhu', 'Huang', 'Wang', 'Chen', 'Lu', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Worlddreamer:+Towards+general+world+models+for+video+generation+via+predicting+masked+tokens. manually and check the results.
        -> Author(s): Xiaofeng Wang, Zheng Zhu, Guan Huang, Boyuan Wang, Xinze Chen, and Jiwen Lu
        -> Title:     Worlddreamer: Towards general world models for video generation via predicting masked tokens.
        -> Year:      2024
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: defined as ∆zi = zi+1 −zi, for i = 1, . . . , T −1. The magnitude of this displacement, which we
-> Invalid unicode use found on p. 3: i = 1, . . . , T −2. The curvature θi (Equation 1), defined for each discrete step i along the trajectory
-> Invalid unicode use found on p. 3: (ranging from 1 to T −2, where T is the total number of sampled frames), is computed from the cosine
-> Invalid unicode use found on p. 3: 2-second window is suitable for the videos considered in Section 7 (≈2 −5s long with 12 −30 FPS),
-> Invalid unicode use found on p. 3: with an temporal based sample frame of ∆t = 2s/(24 −1). Nevertheless, we hypothesize that using
-> Invalid unicode use found on p. 4: significantly larger mean curvature difference (∆θ = θAI −θNat) between their trajectories.
-> Invalid unicode use found on p. 4: T −1
-> Invalid unicode use found on p. 4: T −1
-> Invalid unicode use found on p. 4: i(di −µd)2
-> Invalid unicode use found on p. 4: (d): t = −14.27, p = 5.53 × 10−46; Curvature (θ): t = −44.02, p ≈0. An ANOVA comparing
-> Invalid unicode use found on p. 5: [3] and Sora [60]). We sample frames and we obtain the signals of distance {di}T −1
-> Invalid unicode use found on p. 5: i }T −2
 -> WARNING: Found a non-breaking space that seems invalid.
 -> INFO: Found a correctly used non-breaking space to connect a word and a reference
      --> page 7, line: Acc. (%)
 -> WARNING: Found a non-breaking space that seems invalid.
 -> WARNING: Found a non-breaking space that seems invalid.
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Bracket content [' Consecutive Displacement z}|{ ∆zi · Consecutive Displacement z }| { ∆zi+1 ∥∆zi∥2 | {z } Temporal 
Distance (di) ∥∆zi+1∥2 | {z } Temporal Distance (di+1) | {z } Cosine similarity between ∆zi and ∆zi+1 '] on p. 4 could not be 
matched to a reference.
   -> Sentence:  Following [1, 2], the curvature θi of the representation trajectory is defined as the angle between successive 
displacement vectors, ∆zi and ∆zi+1: θi = Curvature z }| { arccos[ Consecutive Displacement z}|{ ∆zi · Consecutive Displacement z 
}| { ∆zi+1 ∥∆zi∥2 | {z } Temporal Distance (di) ∥∆zi+1∥2 | {z } Temporal Distance (di+1) | {z } Cosine similarity between ∆zi and 
∆zi+1 ], (1) zi zi+1 zi+2 θi ∆zi ∆zi+1 Figure 3: Trajectory curvature Eq
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 652 sentences on 10 pages -> Avg. of 73.44444444444444 sentences per page
-> Warning: Reference '78' never used in the document's text.
-> Warning: Reference '79' never used in the document's text.
-> Warning: Reference '80' never used in the document's text.
-> Warning: Reference '81' never used in the document's text.
-> Warning: Reference '82' never used in the document's text.
-> Warning: Reference '83' never used in the document's text.
-> Warning: Reference '84' never used in the document's text.
-> Warning: Reference '85' never used in the document's text.
-> Warning: Reference '86' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
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
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
-> Missing an abstract for reference with index 40 (Ref. ID = 41); Skipping LLM check...
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
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
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
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
  -> Found 4 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 5 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 144 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 11
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━╸━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   9% 0:04:07
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 12
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 13
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 14
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 15
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
###############################
# Starting Author Check
###############################
-> Saved chapter_fig on try 1
-> Saved lit_fig on try 1
-> Saved rank_fig on try 1
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\35 AI-Generated Video Detection\PAU_results.md
```