
Note: This paper uses a new referencing style
- "(Author et al., 2023)" or "(FirstAuthor, 2021; SecondAuthor, 2025)"
- `(Wu et al., 2023)`
- `(Bartlett et al., 2006; Belkin et al., 2018; Montanari et al., 2019; Thrampoulidis et al., 2020; Chatterji & Long, 2021; Cao et al., 2021; Wang & Thrampoulidis, 2022; Deng et al., 2022)`
- `Lelarge & Miolane (2019)`

23:
- `Pilanci and Ergen (2020)`
 - `(Candes and Tao (2005); Chartrand (2007); Chartrand and Staneva (2008); Foucart and Lai (2009))`
- `(Parhi and Nowak (2021, 2022); Shenouda et al. (2024))`

41:
- `Chen et al. (2020)`
- `(Radford et al., 2019)`
- `(Schulz, 1933; Ben-Israel, 1965; Higham, 2008; Fu et al., 2024)`
- `Candès and Recht (2009); Candès and Tao (2010); Davenport and Romberg (2016)`

46:
- `(Chen et al., 2020a)
- `Chen et al. (2020a)`

50:
- `Lattimore and Szepesvári, 2020`
- `Camilleri et al. (2021)`
- `Shao et al. (2018); Xue et al. (2020)`
- `(Shao et al., 2018)`
- `[Chowdhury and Gopalan (2019)]`
- `[Lugosi and Mendelson (2019a); Catoni (2012)]`

---

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\14 When and How Unlabeled Data Provably Improve\When and How Unlabeled Data Provably Improve.pdf"
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
Enter a supported bibliography numbering (['natbib', 'numbered_squares', 'number_with_dot']): natbib
---
INFO:
 - 'numeric'     = A number placed inside square brackets (e.g., [28])
                -> Multiple references are separated by a comma (e.g., [28,29])
 - 'authoryear'  = Authors' names and the year places insince brackets with or withou a comma in between (e.g., (Dignum et al., 2025))
                -> Multiple references are separated by a semicolon or comma (e.g., (Dignum et al. 2025; Caliskan et al. 2017))
Enter a supported referencing template (['numeric', 'authoryear']): authoryear
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Problem Setup and Preliminaries' on page 3
- Found following heading '3 - Loss Landscape of One-layer Linear Attention under SS-ICL' on page 5
- Found following heading '4 - Multi-layer Attention and the Benefits of Depth' on page 7
- Found following heading '5 - Experiments' on page 10
- Found following heading '6 - Discussion and Limitations' on page 14
=> Found references/literature section on page 15
- Found first appendix 'A - Analysis of Single-layer Linear Attention' on page 19
- Found following appendix 'B - Analysis of Multi-layer Linear Attention' on page 25
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 15 -- 19
All found references: 55
Backend tkagg is interactive backend. Turning interactive mode on.
-> Warning: Could not parse year in reference 'Association for Computational Linguistics. doi: 10.18653/v1/2023.findings-acl.247.'!
-> Warning: Malformed author string: 'pp'
-> Warning: Could not parse year in reference 'Contents A'!
-----------
 -> Parsed references DataFrame:
                         ref_id                                            authors  ...                                               link  valid
0            Agarwal et al 2024  Rishabh Agarwal, Avi Singh, Lei M Zhang, Bernd...  ...                                                      None
1                Ahn et al 2023  Kwangjun Ahn, Xiang Cheng, Hadi Daneshmand, an...  ...                                                      None
2            Akyürek et al 2023  Ekin Akyürek, Dale Schuurmans, Jacob Andreas, ...  ...        https://openreview.net/forum?id=0g0X4H8yN4I   None
3                Bai et al 2023  Yu Bai, Fan Chen, Huan Wang, Caiming Xiong, an...  ...                                                      None
4       Balakrishnan et al 2017  Sivaraman Balakrishnan, Martin J Wainwright, a...  ...                                                      None
5           Bartlett et al 2006  Peter L Bartlett, Michael I Jordan, and Jon D ...  ...                                                      None
6             Belkin et al 2018     Mikhail Belkin, Daniel J Hsu, and Partha Mitra  ...                                                      None
7              Brown et al 2020  Tom Brown, Benjamin Mann, Nick Ryder, Melanie ...  ...                                                      None
8                Cao et al 2021          Yuan Cao, Quanquan Gu, and Mikhail Belkin  ...                                                      None
9       Chatterji and Long 2021              Niladri S Chatterji and Philip M Long  ...                                                      None
10              Chen et al 2025  Zihan Chen, Song Wang, Zhen Tan, Jundong Li, a...  ...                                                      None
11           Collins et al 2024  Liam Collins, Advait Parulekar, Aryan Mokhtari...  ...                                                      None
12               Dai et al 2023  Damai Dai, Yutao Sun, Li Dong, Yaru Hao, Shumi...  ...                                                      None
13                Linguistics 0          Association for Computational Linguistics  ...     https://aclanthology.org/2023.findings-acl.247   None
14              Deng et al 2022  Zeyu Deng, Abla Kammoun, and Christos Thrampou...  ...                                                      None
15           Devroye et al 2013       Luc Devroye, László Györfi, and Gábor Lugosi  ...                                                      None
16               Fan et al 2023  Chuang Fan, Shipeng Liu, Seyed Motamed, Shiyu ...  ...                                                      None
17              Garg et al 2022  Shivam Garg, Dimitris Tsipras, Percy S Liang, ...  ...                                                      None
18               Guo et al 2025  Daya Guo, Dejian Yang, Haowei Zhang, Junxiao S...  ...                                                      None
19            Hastie et al 2009  Trevor Hastie, Robert Tibshirani, Jerome H Fri...  ...                                                      None
20          Hollmann et al 2022  Noah Hollmann, Samuel Müller, Katharina Eggens...  ...                                                      None
21          Hollmann et al 2025  Noah Hollmann, Samuel Müller, Lennart Purucker...  ...                                                      None
22      Krishnapuram et al 2004  Balaji Krishnapuram, David Williams, Ya Xue, L...  ...                                                      None
23             Kumar et al 2020  Ashish Kumar, Logan Engstrom, Andrew Ilyas, an...  ...                                                      None
24      Kwon and Caramanis 2020           Jeongyeol Kwon and Constantine Caramanis  ...                                                      None
25     Laurent and Massart 2000                Beatrice Laurent and Pascal Massart  ...                                                      None
26     Lelarge and Miolane 2019                       Marc Lelarge and Léo Miolane  ...                                                      None
27         (CAMSAP) and pp 2019                   Adaptive Processing (CAMSAP), pp  ...                                                      None
28                Li et al 2023  Yingcong Li, Muhammed Emrullah Ildiz, Dimitris...  ...                                                      None
29                Li et al 2024        Yingcong Li, Ankit S Rawat, and Samet Oymak  ...                                                      None
30                Li et al 2025  Yingcong Li, Davoud Ataee Tarzanagh, Ankit Sin...  ...                                                      None
31         Mahankali et al 2024  Arvind V Mahankali, Tatsunori Hashimoto, and T...  ...         https://openreview.net/forum?id=8p3fu56lKc   None
32               Min et al 2022  Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Arte...  ...                                                      None
33         Montanari et al 2019  Andrea Montanari, Feng Ruan, Youngtak Sohn, an...  ...                                                      None
34                 Neopane 2018                                      Ojash Neopane  ...  https://www.stat.cmu.edu/~arinaldo/Teaching/36...   None
35             Nigam et al 2000  Kamal Nigam, Andrew Kachites McCallum, Sebasti...  ...                                                      None
36         Oymak and Gulcu 2021                  Samet Oymak and Talha Cihad Gulcu  ...                                                      None
37                Qu et al 2025  Jingang Qu, David Holzmüller, Gaël Varoquaux, ...  ...                                                      None
38   Ratsaby and Venkatesh 1995               Joel Ratsaby and Santosh S Venkatesh  ...                                                      None
39              Shen et al 2024     Wei Shen, Ruida Zhou, Jing Yang, and Cong Shen  ...                                                      None
40             Snell et al 2024  Charlie Snell, Jaehoon Lee, Kelvin Xu, and Avi...  ...                                                      None
41     Thrampoulidis et al 2020  Christos Thrampoulidis, Samet Oymak, and Mahdi...  ...                                                      None
42            Oswald et al 2023  Johannes Von Oswald, Eyvind Niklasson, Ettore ...  ...                                                      None
43  Wang and Thrampoulidis 2022                 Ke Wang and Christos Thrampoulidis  ...                                                      None
44              Wang et al 2024  Yifei Wang, Yuyang Wu, Zeming Wei, Stefanie Je...  ...                                                      None
45               Wei et al 2021  Colin Wei, Kendrick Shen, Yining Chen, and Ten...  ...                                                      None
46                Wu et al 2023  Jingfeng Wu, Difan Zou, Zixiang Chen, Vladimir...  ...                                                      None
47               Xie et al 2022  Sang Michael Xie, Aditi Raghunathan, Percy Lia...  ...        https://openreview.net/forum?id=RdJVFCHjUMI   None
48                Xu et al 2021  Jialin Xu, Zixuan Li, Sayan Mukherjee, and Dav...  ...                                                      None
49              Yang et al 2024  Tong Yang, Yu Huang, Yingbin Liang, and Yuejie...  ...                                                      None
50                Ye et al 2025          Han-Jia Ye, Si-Yang Liu, and Wei-Lun Chao  ...                                                      None
51             Zhang et al 2023    Ruiqi Zhang, Spencer Frei, and Peter L Bartlett  ...                                                      None
52             Zhang et al 2024    Ruiqi Zhang, Spencer Frei, and Peter L Bartlett  ...                                                      None
53              Zhou et al 2024  Yucheng Zhou, Xiang Li, Qianning Wang, and Jia...  ...                                                      None
54                          A 0                                         Contents A  ...                                                      None

[55 rows x 10 columns]
- Checking reference 1/55:
  -> INFO: Now checking 10 results for matching title: 'Many-shot in-context learning'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Behbahani, Faust, Larochelle'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/55:
  -> INFO: Now checking 2 results for matching title: 'Transformers learn to implement preconditioned gradient descent for in-context learning'
       -> INFO: All authors matched!
- Checking reference 3/55:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=0g0X4H8yN4I
  -> INFO: Now checking 10 results for matching title: 'What learning algorithm is in-context learning? investigations with linear models'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/55:
  -> INFO: Now checking 1 results for matching title: 'Transformers as statisticians: Provable in-context learning with in-context algorithm selection'
       -> INFO: All authors matched!
- Checking reference 5/55:
  -> INFO: Now checking 3 results for matching title: 'Statistical guarantees for the EM algorithm: From population to sample-based analysis'
       -> INFO: All authors matched!
       -> WARNING: Year (2014) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 6/55:
  -> INFO: Now checking 10 results for matching title: 'Convexity, classification, and risk bounds'
       -> INFO: All authors matched!
- Checking reference 7/55:
  -> INFO: Now checking 1 results for matching title: 'Overfitting or perfect fitting? risk bounds for classification and regression rules that interpolate'
       -> INFO: All authors matched!
- Checking reference 8/55:
  -> INFO: Now checking 10 results for matching title: 'Language models are few-shot learners'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 9/55:
  -> INFO: Now checking 1 results for matching title: 'Risk bounds for over-parameterized maximum margin classification on sub-gaussian mixtures'
       -> INFO: All authors matched!
- Checking reference 10/55:
  -> INFO: Now checking 1 results for matching title: 'Finite-sample analysis of interpolating linear classifiers in the overparameterized regime'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/55:
  -> INFO: Now checking 1 results for matching title: 'Maple: Many-shot adaptive pseudo-labeling for in-context learning'
       -> INFO: All authors matched!
- Checking reference 12/55:
  -> INFO: Now checking 1 results for matching title: 'In-context learning with transformers: Softmax attention adapts to function lipschitzness'
       -> INFO: All authors matched!
- Checking reference 13/55:
  -> INFO: Now checking 2 results for matching title: 'Why can GPT learn in-context? language models secretly perform gradient descent as meta-optimizers'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 6)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 14/55:
  -> Checking if provided link is pingable: https://aclanthology.org/2023.findings-acl.247
  -> INFO: Now checking 10 results for matching title: 'doi: 10.18653/v1/2023'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'doi: 10.18653/v1/2023'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://aclanthology.org/2023.findings-acl.247 manually and check the results.
        -> Author(s): Association for Computational Linguistics
        -> Title:     doi: 10.18653/v1/2023
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 15/55:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: A model of double descent for highdimensional binary linear classification
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Deng', 'Kammoun', 'Thrampoulidis', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+model+of+double+descent+for+highdimensional+binary+linear+classification manually and check the results.
        -> Author(s): Zeyu Deng, Abla Kammoun, and Christos Thrampoulidis
        -> Title:     A model of double descent for highdimensional binary linear classification
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 16/55:
  -> INFO: Now checking 4 results for matching title: 'A probabilistic theory of pattern recognition, volume 31'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Devroye', 'Györfi', 'Lugosi', '2013']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+probabilistic+theory+of+pattern+recognition%2C+volume+31 manually and check the results.
        -> Author(s): Luc Devroye, László Györfi, and Gábor Lugosi
        -> Title:     A probabilistic theory of pattern recognition, volume 31
        -> Year:      2013
     -> Manual search was skipped by the user.
- Checking reference 17/55:
  -> INFO: Now checking 10 results for matching title: 'Expectation maximization pseudo labels'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Xu, Zhou, Jin, Groot, Alexander, Oxtoby, Jacob'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/55:
  -> INFO: Now checking 1 results for matching title: 'What can transformers learn in-context? a case study of simple function classes'
       -> INFO: All authors matched!
- Checking reference 19/55:
  -> INFO: Now checking 10 results for matching title: 'Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Guo', 'Yang', 'Zhang', 'Song', 'Zhang', 'Xu', 'Zhu', 'Ma', 'Wang', 'Bi', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepseek-r1:+Incentivizing+reasoning+capability+in+llms+via+reinforcement+learning manually and check the results.
        -> Author(s): Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al
        -> Title:     Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 20/55:
  -> INFO: Now checking 10 results for matching title: 'The elements of statistical learning: data mining, inference, and prediction, volume 2'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hastie', 'Tibshirani', 'Friedman', 'Friedman', '2009']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+elements+of+statistical+learning:+data+mining%2C+inference%2C+and+prediction%2C+volume+2 manually and check the results.
        -> Author(s): Trevor Hastie, Robert Tibshirani, Jerome H Friedman, and Jerome H Friedman
        -> Title:     The elements of statistical learning: data mining, inference, and prediction, volume 2
        -> Year:      2009
     -> Manual search was skipped by the user.
- Checking reference 21/55:
  -> INFO: Now checking 1 results for matching title: 'Tabpfn: A transformer that solves small tabular classification problems in a second'
       -> INFO: All authors matched!
- Checking reference 22/55:
  -> INFO: Now checking 4 results for matching title: 'Accurate predictions on small data with a tabular foundation model'
       -> INFO: All authors matched!
- Checking reference 23/55:
  -> INFO: Now checking 10 results for matching title: 'On semi-supervised classification'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Krishnapuram', 'Williams', 'Xue', 'Carin', 'Figueiredo', 'Hartemink', '2004']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=On+semi-supervised+classification manually and check the results.
        -> Author(s): Balaji Krishnapuram, David Williams, Ya Xue, Lawrence Carin, Mário Figueiredo, and Alexander Hartemink
        -> Title:     On semi-supervised classification
        -> Year:      2004
     -> Manual search was skipped by the user.
- Checking reference 24/55:
  -> INFO: Now checking 10 results for matching title: 'Understanding self-training for gradient-boosted trees'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kumar', 'Engstrom', 'Ilyas', 'Tsipras', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Understanding+self-training+for+gradient-boosted+trees manually and check the results.
        -> Author(s): Ashish Kumar, Logan Engstrom, Andrew Ilyas, and Dimitris Tsipras
        -> Title:     Understanding self-training for gradient-boosted trees
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 25/55:
  -> INFO: Now checking 2 results for matching title: 'The em algorithm gives sample-optimality for learning mixtures of well-separated gaussians'
       -> INFO: All authors matched!
- Checking reference 26/55:
  -> INFO: Now checking 4 results for matching title: 'Adaptive estimation of a quadratic functional by model selection'
       -> INFO: All authors matched!
       -> WARNING: Year (2001) does not match expected year (2000)!
       -> INFO: All authors matched!
- Checking reference 27/55:
  -> INFO: Now checking 3 results for matching title: 'Asymptotic bayes risk for gaussian mixture in a semi-supervised setting'
       -> INFO: All authors matched!
- Checking reference 28/55:
  -> INFO: Now checking 10 results for matching title: '639–643'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['(CAMSAP)', 'pp', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=639–643 manually and check the results.
        -> Author(s): Adaptive Processing (CAMSAP), pp
        -> Title:     639–643
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 29/55:
  -> INFO: Now checking 1 results for matching title: 'Transformers as algorithms: Generalization and stability in in-context learning'
       -> INFO: All authors matched!
- Checking reference 30/55:
  -> INFO: Now checking 1 results for matching title: 'Fine-grained analysis of in-context linear estimation: Data, architecture, and beyond'
       -> INFO: All authors matched!
- Checking reference 31/55:
  -> INFO: Now checking 4 results for matching title: 'Gating is weighting: Understanding gated linear attention through in-context learning'
       -> INFO: All authors matched!
- Checking reference 32/55:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=8p3fu56lKc
  -> INFO: Now checking 1 results for matching title: 'One step of gradient descent is provably the optimal in-context learner with one layer of linear self-attention'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/55:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Rethinking the role of demonstrations: What makes in-context learning work? arXiv preprint arXiv:2202.12837.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Min', 'Lyu', 'Holtzman', 'Artetxe', 'Lewis', 'Hajishirzi', 'Zettlemoyer', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Rethinking+the+role+of+demonstrations:+What+makes+in-context+learning+work?+arXiv+preprint+arXiv:2202.12837. manually and check the results.
        -> Author(s): Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi, and Luke Zettlemoyer
        -> Title:     Rethinking the role of demonstrations: What makes in-context learning work? arXiv preprint arXiv:2202.12837.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 34/55:
  -> INFO: Now checking 3 results for matching title: 'The generalization error of max-margin linear classifiers: High-dimensional asymptotics in the overparametrized regime'
       -> INFO: All authors matched!
- Checking reference 35/55:
  -> INFO: Skipping validity check of link ending with '.pdf': https://www.stat.cmu.edu/~arinaldo/Teaching/36709/S19/Scribed_Lectures/Feb26_Ojash.pdf
  -> INFO: Now checking 10 results for matching title: 'Lecture notes on high-dimensional statistics'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Neopane', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Lecture+notes+on+high-dimensional+statistics manually and check the results.
        -> Author(s): Ojash Neopane
        -> Title:     Lecture notes on high-dimensional statistics
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 36/55:
  -> INFO: Now checking 10 results for matching title: 'Text classification from labeled and unlabeled documents using em'
       -> INFO: All authors matched!
- Checking reference 37/55:
  -> INFO: Now checking 1 results for matching title: 'A theoretical characterization of semi-supervised learning with self-training for gaussian mixture models'
       -> INFO: All authors matched!
- Checking reference 38/55:
  -> INFO: Now checking 2 results for matching title: 'Tabicl: A tabular foundation model for in-context learning on large data'
       -> INFO: All authors matched!
- Checking reference 39/55:
  -> INFO: Now checking 1 results for matching title: 'Learning from a mixture of labeled and unlabeled examples with parametric side information'
       -> INFO: All authors matched!
- Checking reference 40/55:
  -> INFO: Now checking 1 results for matching title: 'On the training convergence of transformers for in-context classification'
       -> INFO: All authors matched!
- Checking reference 41/55:
  -> INFO: Now checking 10 results for matching title: 'Scaling llm test-time compute optimally can be more effective than scaling model parameters'
       -> INFO: All authors matched!
- Checking reference 42/55:
  -> INFO: Now checking 1 results for matching title: 'Theoretical insights into multiclass classification: A high-dimensional asymptotic view'
       -> INFO: All authors matched!
- Checking reference 43/55:
  -> INFO: Now checking 10 results for matching title: 'Transformers learn in-context by gradient descent'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 44/55:
  -> INFO: Now checking 1 results for matching title: 'Binary classification of gaussian mixtures: Abundance of support vectors, benign overfitting, and regularization'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 45/55:
  -> INFO: Now checking 1 results for matching title: 'A theoretical understanding of self-correction through in-context alignment'
       -> INFO: All authors matched!
- Checking reference 46/55:
  -> INFO: Now checking 7 results for matching title: 'Theoretical analysis of self-training with deep networks on unlabeled data'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 47/55:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: How many pretraining tasks are needed for in-context learning of linear regression? arXiv preprint arXiv:2310.08391.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'Zou', 'Chen', 'Braverman', 'Gu', 'Bartlett', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=How+many+pretraining+tasks+are+needed+for+in-context+learning+of+linear+regression?+arXiv+preprint+arXiv:2310.08391. manually and check the results.
        -> Author(s): Jingfeng Wu, Difan Zou, Zixiang Chen, Vladimir Braverman, Quanquan Gu, and Peter L Bartlett
        -> Title:     How many pretraining tasks are needed for in-context learning of linear regression? arXiv preprint arXiv:2310.08391.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 48/55:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=RdJVFCHjUMI
  -> INFO: Now checking 1 results for matching title: 'An explanation of in-context learning as implicit bayesian inference'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 49/55:
  -> INFO: Now checking 10 results for matching title: 'Towards understanding deep learning with persistent homology'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Xu', 'Li', 'Mukherjee', 'Taylor', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Towards+understanding+deep+learning+with+persistent+homology manually and check the results.
        -> Author(s): Jialin Xu, Zixuan Li, Sayan Mukherjee, and David Taylor
        -> Title:     Towards understanding deep learning with persistent homology
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 50/55:
  -> INFO: Now checking 1 results for matching title: 'In-context learning with representations: Contextual generalization of trained transformers'
       -> INFO: All authors matched!
- Checking reference 51/55:
  -> INFO: Now checking 1 results for matching title: 'A closer look at tabpfn v2: Strength, limitation, and extension'
       -> INFO: All authors matched!
- Checking reference 52/55:
  -> INFO: Now checking 10 results for matching title: 'Trained transformers learn linear models in-context'
       -> INFO: All authors matched!
- Checking reference 53/55:
  -> INFO: Now checking 10 results for matching title: 'Trained transformers learn linear models in-context'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/55:
  -> INFO: Now checking 10 results for matching title: 'Visual in-context learning for large vision-language models'
       -> INFO: All authors matched!
- Checking reference 55/55:
  -> INFO: Now checking 10 results for matching title: 'Contents A'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['A', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Contents+A manually and check the results.
        -> Author(s): Contents A
        -> Title:     Contents A
        -> Year:      0
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 1: model, we have xi ∼N(µyi, σ2I) and yi ∈{−1, 1}, i ∈[n], and the component means µ±1 that
-> Invalid unicode use found on p. 1: total samples have correct labels (m ≤n) either −1 or 1, and remaining labels are unknown and fed to
-> Invalid unicode use found on p. 1: ˆyi = X ˆµi−1 and training (maximization) ˆµi = X⊤ˆyi steps. Corroborating this, we show that
-> Invalid unicode use found on p. 3: −1,
-> Invalid unicode use found on p. 3: denotes the feature vector and yi ∈{−1, 0, 1} represents the corresponding observed label, with yi = 0
-> Invalid unicode use found on p. 3: 1 −p
-> Invalid unicode use found on p. 3: −1,
-> Invalid unicode use found on p. 3: Here µ ∼Unif(Sd−1) denotes the task mean, which is sampled uniformly from the unit sphere, and
-> Invalid unicode use found on p. 3: i denotes the true class label that is uniform over {−1, 1}. Observe that p = 1
-> Invalid unicode use found on p. 4: Zℓ= Zℓ−1 + att(Zℓ−1; Wℓ−1)
-> Invalid unicode use found on p. 4: corresponds to a randomly sampled task vector µ ∼Unif(Sd−1) and let ℓ(·) : R →R be the loss
-> Invalid unicode use found on p. 5: (cf. (7)) with L = 1 and squared loss function ℓ(y, ˆy) = (y −ˆy)2, and denote the optimal prediction as
-> Invalid unicode use found on p. 5: d−1
-> Invalid unicode use found on p. 5: 1 −10dε2
-> Invalid unicode use found on p. 5: + e−d + e−1/8ε2
-> Invalid unicode use found on p. 5: of the SPI estimator, and the red dotted curves depict the accuracy 1 −P(y⋆
-> Invalid unicode use found on p. 5: unlabeled data lies in the expectation structure. In our isotropic GMM setting where µ ∼Unif(Sd−1),
-> Invalid unicode use found on p. 6: • Label propagation: A = c QL−1
-> Invalid unicode use found on p. 6: I + cℓX⊤X for arbitrary constants {c, c1, · · · , cL−1};
-> Invalid unicode use found on p. 6: ℓ∈[L −1]
-> Invalid unicode use found on p. 7: ℓXℓ)xℓ, for ℓ∈[L −1]
-> Invalid unicode use found on p. 7: (3L−3)/2
-> Invalid unicode use found on p. 7: · · · a(3L−3)/2]⊤lie on a manifold of dimension at most 2L as a can
-> Invalid unicode use found on p. 7: be expressed as a = g(c) for some smooth function g : R2L →R(3L−3)/2 with c representing the
-> Invalid unicode use found on p. 7: the form (X⊤X/n −σ2I)k.
-> Invalid unicode use found on p. 7: µµ⊤+ σ2I, and the top eigenvector of the centered covariance matrix (X⊤X/n −σ2I) asymptotically
-> Invalid unicode use found on p. 7: aligns with either µ or −µ. Therefore, with a substantial amount of unlabeled data, we propose the
-> Invalid unicode use found on p. 7: ˆµss-k = αˆµs + (1 −α)(X⊤X/n −σ2I)k ˆµs
-> Invalid unicode use found on p. 8: n, d and p. Note that as k →∞, the term (X⊤X/n −σ2I)k converges (up to scaling) to a rankone projection onto the top eigenvector of the debiased covariance matrix, effectively serving as an
-> Invalid unicode use found on p. 8: + Q( √np/σ) −2Q(1/σ)Q( √np/σ).
-> Invalid unicode use found on p. 8: attention can output x⊤(X⊤X/n −σ2I)ˆµs. As n →∞, the empirical covariance converges to its
-> Invalid unicode use found on p. 8: expectation, i.e., X⊤X/n −σ2I →µµ⊤. The results in Figure 1c validate Theorem 3, showing that
-> Invalid unicode use found on p. 9: 1 −C √d/n
-> Invalid unicode use found on p. 9: + e−d.
-> Invalid unicode use found on p. 10: In Figures 2a and 2b, we empirically examine the optimal values of α. Given µ ∼Unif(Sd−1), we
-> Invalid unicode use found on p. 11: −1|, |ˆysoft
-> Invalid unicode use found on p. 12: 1.68 (−)
-> Invalid unicode use found on p. 12: 0.28 (−)
-> Invalid unicode use found on p. 12: −1
-> Invalid unicode use found on p. 18: yixi −y
-> Invalid unicode use found on p. 18: training a single-layer linear attention with squared loss, that is, L = 1 and ℓ(y, ˆy) = (y −ˆy)2. Recall
-> Invalid unicode use found on p. 19: Next, recall the loss from (7) and consider the squared loss function, ℓ(y, ˆy) = (y −ˆy)2. We have
-> Invalid unicode use found on p. 19: (fatt-1(Z) −y)2i
-> Invalid unicode use found on p. 19: −y
-> Invalid unicode use found on p. 19: −1
-> Invalid unicode use found on p. 20: −1
-> Invalid unicode use found on p. 20: xi −1
-> Invalid unicode use found on p. 20: xi −1
-> Invalid unicode use found on p. 20: i∈I xi −1)(x⊤( ¯WX⊤Xh1 + mhw1))] = 0. To prove it, we first expand
-> Invalid unicode use found on p. 20: xi −1)(x⊤( ¯WX⊤Xh1 + mhw1))
-> Invalid unicode use found on p. 20: −x⊤¯WX⊤Xh1
-> Invalid unicode use found on p. 20: −mhx⊤w1
-> Invalid unicode use found on p. 20: value zero. First note that since µ ∼Unif(Sd−1) and (ξi)n
-> Invalid unicode use found on p. 21: xi −1
-> Invalid unicode use found on p. 21: i∈I xi −1)2] = ˜L( ˜W) where ˜L( ˜W) is defined in (15).
-> Invalid unicode use found on p. 21: xi −1
-> Invalid unicode use found on p. 22: xi −1)2
-> Invalid unicode use found on p. 22: (µ + ξi) −1)2
-> Invalid unicode use found on p. 22: ((µ + ξ)⊤W(mµ + √mξ′) −1)2i
-> Invalid unicode use found on p. 22: −2 E
-> Invalid unicode use found on p. 22: + E[m]σ4tr(WW⊤) + 1 −2 E[m]
-> Invalid unicode use found on p. 22: W + 2 E[m]σ4W −2 E[m]
-> Invalid unicode use found on p. 23: d−1.
-> Invalid unicode use found on p. 23: d−1 denotes chi-squared distribution with (d −1) degrees of freedom. Then, we get
-> Invalid unicode use found on p. 23: att-1(Z) , y). Let c := ε−1
-> Invalid unicode use found on p. 23: = Eg≥−c
-> Invalid unicode use found on p. 23: + Eg<−c
-> Invalid unicode use found on p. 23: ≤Eg≥−c
-> Invalid unicode use found on p. 23: = Eg≥−c
-> Invalid unicode use found on p. 24: where the inequality comes from the fact that P(g ≤−c/2) = Q(c/2) and Q(x) ≤1 for any x ∈R. Next,
-> Invalid unicode use found on p. 24: 1 + h/(c + g)2 ≥1 −1
-> Invalid unicode use found on p. 24: (c + g)2 ≥1 −2h
-> Invalid unicode use found on p. 24: 1+x ≥1 −1
-> Invalid unicode use found on p. 24: 2 x and the second utilizes that g ≥−c
-> Invalid unicode use found on p. 24: h ≥d −1 + 2
-> Invalid unicode use found on p. 24: (d −1)t1 + 2t1
-> Invalid unicode use found on p. 24: ≤e−t1.
-> Invalid unicode use found on p. 24: Therefore, we have that with probability at least 1 −e−t1
-> Invalid unicode use found on p. 24: 1 + h/(c + g)2 ≥1 −2(d −1 + 2 √(d −1)t1 + 2t1)
-> Invalid unicode use found on p. 24: Setting t1 = d, we get with probability at least 1 −e−d
-> Invalid unicode use found on p. 24: 1 + h/(c + g)2 ≥1 −10d
-> Invalid unicode use found on p. 24: Combining the result with (24), since Q(x) ≤1 for x ∈R and Q(x) ≤e−x2/2 for x > 1, we get that
-> Invalid unicode use found on p. 24: att-1(Z) , y) ≤e−d + Q(c/2) + Q
-> Invalid unicode use found on p. 24: 1 −10d
-> Invalid unicode use found on p. 24: ≤e−d + e−1/8ε2
-> Invalid unicode use found on p. 24: 1 −10dε2
-> Invalid unicode use found on p. 25: L−1
-> Invalid unicode use found on p. 25: L−1
-> Invalid unicode use found on p. 25: L−1
-> Invalid unicode use found on p. 26: XL = aL−1XL−1(X⊤
-> Invalid unicode use found on p. 26: L−1XL−1)
-> Invalid unicode use found on p. 26: = aL−1a3
-> Invalid unicode use found on p. 26: L−2XL−2(X⊤
-> Invalid unicode use found on p. 26: L−2XL−2)
-> Invalid unicode use found on p. 26: = aL−1a3
-> Invalid unicode use found on p. 26: L−2a32
-> Invalid unicode use found on p. 26: L−3XL−3(X⊤
-> Invalid unicode use found on p. 26: L−3XL−3)
-> Invalid unicode use found on p. 26: = aL−1a3
-> Invalid unicode use found on p. 26: L−2a32
-> Invalid unicode use found on p. 26: L−3...a3L−2
-> Invalid unicode use found on p. 26: L = aL−1x⊤
-> Invalid unicode use found on p. 26: L−1(X⊤
-> Invalid unicode use found on p. 26: L−1XL−1)
-> Invalid unicode use found on p. 26: = aL−1a3
-> Invalid unicode use found on p. 26: L−2x⊤
-> Invalid unicode use found on p. 26: L−2(X⊤
-> Invalid unicode use found on p. 26: L−2XL−2)
-> Invalid unicode use found on p. 26: = aL−1a3
-> Invalid unicode use found on p. 26: L−2a32
-> Invalid unicode use found on p. 26: L−3x⊤
-> Invalid unicode use found on p. 26: L−3(X⊤
-> Invalid unicode use found on p. 26: L−3XL−3)
-> Invalid unicode use found on p. 26: = aL−1a3
-> Invalid unicode use found on p. 26: L−2a32
-> Invalid unicode use found on p. 26: L−3...a3L−2
-> Invalid unicode use found on p. 26: L−1
-> Invalid unicode use found on p. 26: a3L−1−ℓ
-> Invalid unicode use found on p. 27: and let e = [e0 e2 · · · e(3L−3)/2]⊤∈RK+1.
-> Invalid unicode use found on p. 27: L−1(I + aL−1X⊤
-> Invalid unicode use found on p. 27: L−1XL−1)2(I + bL−1X⊤
-> Invalid unicode use found on p. 27: L−1XL−1)X⊤
-> Invalid unicode use found on p. 27: L−1yL−1
-> Invalid unicode use found on p. 27: depend on the model parameters cbL and (aℓ, bℓ)L−1
-> Invalid unicode use found on p. 27: ℓ=1 , which together have at most 2L −1 degrees
-> Invalid unicode use found on p. 27: of freedom. Let c = [cbL a1 · · · aL−1 b1 · · · bL−1]⊤. This means there exists a smooth function
-> Invalid unicode use found on p. 27: g : R2L−1 →RK such that: e = g(c).
-> Invalid unicode use found on p. 27: X⊤X up to degree (3L −3)/2.
-> Invalid unicode use found on p. 28: L−1(X⊤
-> Invalid unicode use found on p. 28: L−1XL−1)3X⊤
-> Invalid unicode use found on p. 28: L−1yL−1)
-> Invalid unicode use found on p. 28: L−2(X⊤
-> Invalid unicode use found on p. 28: L−2XL−2)(X⊤
-> Invalid unicode use found on p. 28: L−2XL−2)32(X⊤
-> Invalid unicode use found on p. 28: L−2XL−2)2X⊤
-> Invalid unicode use found on p. 28: L−2yL−2)
-> Invalid unicode use found on p. 28: L−2(X⊤
-> Invalid unicode use found on p. 28: L−2XL−2)32+3X⊤
-> Invalid unicode use found on p. 28: L−2yL−2)
-> Invalid unicode use found on p. 28: L−3(X⊤
-> Invalid unicode use found on p. 28: L−3XL−3)(X⊤
-> Invalid unicode use found on p. 28: L−3XL−3)33+32(X⊤
-> Invalid unicode use found on p. 28: L−3XL−3)2X⊤
-> Invalid unicode use found on p. 28: L−3yL−3)
-> Invalid unicode use found on p. 28: L−3(X⊤
-> Invalid unicode use found on p. 28: L−3XL−3)33+32+3X⊤
-> Invalid unicode use found on p. 28: L−3yL−3)
-> Invalid unicode use found on p. 28: = P(x⊤(X⊤X)3L−1+···+32+3X⊤y)
-> Invalid unicode use found on p. 28: = 3L−1 + · · · + 32 + 3 = 3L −3
-> Invalid unicode use found on p. 29: (λ−1
-> Invalid unicode use found on p. 29: (λ−1
-> Invalid unicode use found on p. 29: ∆(−ˆµs) = ∆(ˆµs).
-> Invalid unicode use found on p. 29: First, note that for any x > 0, Q(x) < 0.5 < Q(−x). Therefore, the optimal choice of v1 ∈Rd
-> Invalid unicode use found on p. 29: f(ˆµs) ≥f(−ˆµs)
-> Invalid unicode use found on p. 30: + f(−ˆµs)Q
-> Invalid unicode use found on p. 30: −µ⊤ˆµs
-> Invalid unicode use found on p. 30: (f(ˆµs) −f(−ˆµs)) Q
-> Invalid unicode use found on p. 30: + f(−ˆµs)d ˆµs.
-> Invalid unicode use found on p. 30: (f(ˆµs) −f(−ˆµ)) Q
-> Invalid unicode use found on p. 30: + f(−ˆµs)d ˆµs
-> Invalid unicode use found on p. 30: 1 −Q
-> Invalid unicode use found on p. 30: −
-> Invalid unicode use found on p. 30: 1 −Q
-> Invalid unicode use found on p. 30: 1 −Q
-> Invalid unicode use found on p. 30: 1 −Q
-> Invalid unicode use found on p. 30: −2Q
-> Invalid unicode use found on p. 30: fatt-L(Z) = x⊤(X⊤X/n −σ2I)ˆµs.
-> Invalid unicode use found on p. 31: A := X⊤X/n −σ2I. We get
-> Invalid unicode use found on p. 31: n X⊤X −σ2I
-> Invalid unicode use found on p. 31: −σ2I
-> Invalid unicode use found on p. 31: −I
-> Invalid unicode use found on p. 31: ∆:= A −µµ⊤= σ
-> Invalid unicode use found on p. 31: −I
-> Invalid unicode use found on p. 31: 1 −e−t1 (assuming t1 ≥d), the first term of (36) can be bounded by
-> Invalid unicode use found on p. 31: Additionally, from Neopane (2018), we have that with probability at least 1 −e−t2 (assuming t2 ≥d),
-> Invalid unicode use found on p. 31: −I
-> Invalid unicode use found on p. 31: Combining (37) and (38), we get with probability at least 1 −2e−t (for t ≥d)
-> Invalid unicode use found on p. 31: probability at least 1 −e−t3 (assuming 2d ≤t3 ≤m/4σ2), we can bound
-> Invalid unicode use found on p. 31: at least 1 −3e−min(t,t3) and suppose that µ⊤ˆµs > 0.5, we can bound
-> Invalid unicode use found on p. 31: −µ⊤µµ⊤ˆµs
-> Invalid unicode use found on p. 31: −µ⊤µµ⊤ˆµs
-> Invalid unicode use found on p. 31: µ⊤ˆµs −∥∆∥· ∥ˆµs∥
-> Invalid unicode use found on p. 32: −µ⊤µµ⊤ˆµs
-> Invalid unicode use found on p. 32: 1 −C2
-> Invalid unicode use found on p. 32: + 3e−min(t,t3)
-> Invalid unicode use found on p. 32: 1 −C2
-> Invalid unicode use found on p. 32: + 3e−min(t,t3) + Q
-> Invalid unicode use found on p. 32: 1 −C2
-> Invalid unicode use found on p. 32: + 3e−2d + 0.5e−d
-> Invalid unicode use found on p. 32: 1 −C2
-> Invalid unicode use found on p. 32: + e−d.
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Skipping possible_ref_id 'xi yi' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'µyi σ2I' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text references '(['Hollmann et al', ' 2022', ' 2025'])' in bracket on p. 2!
-> Couldn't parse in-text references '(['query', ' responsei', ' rewardi'])' in bracket on p. 3!
-> Skipping possible_ref_id 'xi yi' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '0 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '0 σ2I' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'xi yi' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text (sub) reference '(Z)' in bracket 'Z; W' on p. 4!
-> Couldn't parse in-text (sub) reference '( W)' in bracket 'Z; W' on p. 4!
-> Couldn't parse in-text (sub) reference '(Z)' in bracket 'Z; W' on p. 4!
-> Couldn't parse in-text (sub) reference '( W)' in bracket 'Z; W' on p. 4!
-> Couldn't parse in-text (sub) reference '(Zℓ−1)' in bracket 'Zℓ−1; Wℓ−1' on p. 5!
-> Couldn't parse in-text (sub) reference '( Wℓ−1)' in bracket 'Zℓ−1; Wℓ−1' on p. 5!
-> Couldn't parse in-text (sub) reference '(ZL)' in bracket 'ZL; WL' on p. 5!
-> Couldn't parse in-text (sub) reference '( WL)' in bracket 'ZL; WL' on p. 5!
-> Skipping possible_ref_id 'W(L) h' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'W(L) h' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'y fatt-L(Z)' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'ξi yi' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'xi yi' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'y⋆ att-1(Z) y' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '0 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'y⋆ att-1(Z) y' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'x1 x2' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '· · · xn' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'Xℓ xℓ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '0 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'xi yi' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'ˆyA y' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'ˆyµµ⊤ y' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'ˆyµµ⊤ y' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'y⋆ att-L(Z) y' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'y⋆ att-L(Z) y' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '0 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'cosine_similarity(µss-k µ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text references '(['Dlab', ' Dunlab', ' K'])' in bracket on p. 12!
-> Skipping possible_ref_id '|ˆysoft i −1| |ˆysoft i + 1|' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '['black dotted']' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'xi ˆysoft i' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 587 sentences on 15 pages -> Avg. of 42.92857142857143 sentences per page
-> Warning: Reference 'Chatterji and Long 2021' never used in the document's text.
-> Warning: Reference 'Linguistics 0' never used in the document's text.
-> Warning: Reference 'Laurent and Massart 2000' never used in the document's text.
-> Warning: Reference '(CAMSAP) and pp 2019' never used in the document's text.
-> Warning: Reference 'Neopane 2018' never used in the document's text.
-> Warning: Reference 'Oswald et al 2023' never used in the document's text.
-> Warning: Reference 'Wang and Thrampoulidis 2022' never used in the document's text.
-> Warning: Reference 'Zhang et al 2024' never used in the document's text.
-> Warning: Reference 'A 0' never used in the document's text.
---
  // LLM calling counter = 1
  => WARNING: A Syntax Error occured during parsing: invalid syntax (<string>, line 3)
     Structurally parsing response as string: [(sentence, True, "supports") for (sentence, _, _) in _] 

Explanation: The abstract explicitly reports "significant performance gains" when going from few-shot to many-shot (i.e., pushing more examples into the context), so each provided sentence is thematically related and supported by the abstract.
  -> Warning: The LLM response has not 3 values per sentence;                 len(response_splitted) % 3 = 1
  -> LLM list extracted as follows:
[['so each provided sentence is thematically related and supported by the abstract.', '_) in _ \n\nExplanation: The abstract explicitly reports "significant performance gains" when going from few-shot to many-shot (i.e.', 'pushing more examples into the context)'], ['so each provided sentence is thematically related and supported by the abstract.', '_) in _ \n\nExplanation: The abstract explicitly reports "significant performance gains" when going from few-shot to many-shot (i.e.', 'pushing more examples into the context)']]
-> Missing an abstract for reference with index 1 (Ref. ID = Ahn et al 2023); Skipping LLM check...
  // LLM calling counter = 2
  => WARNING: A Syntax Error occured during parsing: unterminated string literal (detected at line 13) (<string>, line 13)
     Structurally parsing response as string: I updated all tuples. For every tuple whose sentence is:

- " This prompt model is well studied under various fully-supervised settings (Garg et al, 2022; Von Oswald et al, 2023; Ahn et al, 2023; Akyürek et al, 2023; Mahankali et al, 2024; Collins et al, 2024; Shen et al, 2024) where each demonstration includes a clearly labeled output"

I set: (True, "not enough information").

For every tuple whose sentence is:

- " Akyürek et al (2023), Von Oswald et al (2023) and Dai et al (2023) demonstrated that transformers emulate gradient descent during ICL"

I set: (True, "not enough information").

Reasoning summary: The abstract is thematically relevant to both sentences because it discusses in-context learning from labeled examples and shows transformers can implement and reproduce gradient-descent-like predictors. However the abstract does not provide evidence about the specific external claims (that the listed works specifically demonstrated those findings or that the prompt model is "well studied" under those particular citations), so the stance for those exact claims is "not enough information.
  -> LLM list extracted as follows:
[['Von Oswald et al (2023) and Dai et al (2023) demonstrated that transformers emulate gradient descent during ICL"\n\nI set: (True', 'not enough information").\n\nReasoning summary: The abstract is thematically relevant to both sentences because it discusses in-context learning from labeled examples and shows transformers can implement and reproduce gradient-descent-like predictors. However the abstract does not provide evidence about the specific external claims (that the listed works specifically demonstrated those findings or that the prompt model is "well studied" under those particular citations)', 'so the stance for those exact claims is "not enough information.'], ['Von Oswald et al (2023) and Dai et al (2023) demonstrated that transformers emulate gradient descent during ICL"\n\nI set: (True', 'not enough information").\n\nReasoning summary: The abstract is thematically relevant to both sentences because it discusses in-context learning from labeled examples and shows transformers can implement and reproduce gradient-descent-like predictors. However the abstract does not provide evidence about the specific external claims (that the listed works specifically demonstrated those findings or that the prompt model is "well studied" under those particular citations)', 'so the stance for those exact claims is "not enough information.'], ['Von Oswald et al (2023) and Dai et al (2023) demonstrated that transformers emulate gradient descent during ICL"\n\nI set: (True', 'not enough information").\n\nReasoning summary: The abstract is thematically relevant to both sentences because it discusses in-context learning from labeled examples and shows transformers can implement and reproduce gradient-descent-like predictors. However the abstract does not provide evidence about the specific external claims (that the listed works specifically demonstrated those findings or that the prompt model is "well studied" under those particular citations)', 'so the stance for those exact claims is "not enough information.'], ['Von Oswald et al (2023) and Dai et al (2023) demonstrated that transformers emulate gradient descent during ICL"\n\nI set: (True', 'not enough information").\n\nReasoning summary: The abstract is thematically relevant to both sentences because it discusses in-context learning from labeled examples and shows transformers can implement and reproduce gradient-descent-like predictors. However the abstract does not provide evidence about the specific external claims (that the listed works specifically demonstrated those findings or that the prompt model is "well studied" under those particular citations)', 'so the stance for those exact claims is "not enough information.']]
-> Missing an abstract for reference with index 3 (Ref. ID = Bai et al 2023); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 5 (Ref. ID = Bartlett et al 2006); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = Belkin et al 2018); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = Brown et al 2020); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = Cao et al 2021); Skipping LLM check...
-> WARNING: Reference with index 9 (Ref. ID = Chatterji and Long 2021) has no associated sentence!
-> Missing an abstract for reference with index 10 (Ref. ID = Chen et al 2025); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = Collins et al 2024); Skipping LLM check...
  // LLM calling counter = 4
  => WARNING: A Syntax Error occured during parsing: invalid syntax (<string>, line 3)
     Structurally parsing response as string: [(" Akyürek et al (2023), Von Oswald et al (2023) and Dai et al (2023) demonstrated that transformers emulate gradient descent during ICL", True, "supports")]

Note: All tuples in your input list are the same sentence; I have assessed each occurrence identically. Each has been marked thematically related (True) and the abstract supports the statement ("supports").
  -> Warning: The LLM response has not 3 values per sentence;                 len(response_splitted) % 3 = 1
  -> LLM list extracted as follows:
[['supports")\n\nNote: All tuples in your input list are the same sentence; I have assessed each occurrence identically. Each has been marked thematically related (True) and the abstract supports the statement ("supports").', 'Von Oswald et al (2023) and Dai et al (2023) demonstrated that transformers emulate gradient descent during ICL', 'True']]
-> Missing an abstract for reference with index 13 (Ref. ID = Linguistics 0); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = Deng et al 2022); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = Devroye et al 2013); Skipping LLM check...
  // LLM calling counter = 5
  => WARNING: A Syntax Error occured during parsing: unterminated string literal (detected at line 1) (<string>, line 1)
     Structurally parsing response as string: All of the provided sentences are thematically related to the abstract (both concern pseudo-labelling and its connection to EM), but the abstract does not provide information about Nigam et al. (2000)"s empirical results on text classification using unlabeled documents. Therefore I update every tuple to: (same sentence, True, "not enough information").

For example:
[(" Nigam et al (2000) demonstrated empirically that EM (viewable as iterative pseudo-labeling Fan et al (2023)) with pseudo-labels significantly reduces text classification error using unlabeled documents", True, "not enough information"),
 (" Nigam et al (2000) demonstrated empirically that EM (viewable as iterative pseudo-labeling Fan et al (2023)) with pseudo-labels significantly reduces text classification error using unlabeled documents", True, "not enough information"),
 ... ]

(Every tuple in your input list has been updated in the same way.)
  -> Warning: The LLM response has not 3 values per sentence;                 len(response_splitted) % 3 = 1
  -> LLM list extracted as follows:
[['... \n\n(Every tuple in your input list has been updated in the same way.)', 'True', 'not enough information")'], ['... \n\n(Every tuple in your input list has been updated in the same way.)', 'True', 'not enough information")'], ['... \n\n(Every tuple in your input list has been updated in the same way.)', 'True', 'not enough information")']]
-> Missing an abstract for reference with index 17 (Ref. ID = Garg et al 2022); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = Guo et al 2025); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = Hastie et al 2009); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = Hollmann et al 2022); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = Hollmann et al 2025); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = Krishnapuram et al 2004); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = Kumar et al 2020); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = Kwon and Caramanis 2020); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = Laurent and Massart 2000); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = Lelarge and Miolane 2019); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = (CAMSAP) and pp 2019); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = Li et al 2023); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = Li et al 2024); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = Li et al 2025); Skipping LLM check...
  // LLM calling counter = 6
  => WARNING: A Syntax Error occured during parsing: invalid syntax (<string>, line 1)
     Structurally parsing response as string: I updated the tuples, applying the same assessment to every repeated occurrence of each sentence. Because the abstract discusses in-context learning, one-layer linear self-attention, and results about (preconditioned) single-step gradient-descent behavior, all of the sentences you supplied are thematically related to the abstract; however the abstract does not provide the specific factual support or attribution those sentences assert (e.g., attribution to particular prior authors, claims about "optimality", or procedural details about constructing prompts). Therefore each sentence is marked True for relevance and "not enough information" for stance.

Mapping applied to every matching tuple in your list:
- Sentence: "This prompt model is well studied under various fully-supervised settings (Garg et al, 2022; Von Oswald et al, 2023; Ahn et al, 2023; Akyürek et al, 2023; Mahankali et al, 2024; Collins et al, 2024; Shen et al, 2024) where each demonstration includes a clearly labeled output"
  - Updated tuple: (same sentence, True, "not enough information")

- Sentence: "Ahn et al (2023) established they implement preconditioned gradient descent, and Mahankali et al (2024) proved one-step gradient descent is optimal for single-layer linear attention"
  - Updated tuple: (same sentence, True, "not enough information")

- Sentence: "2 In-context Learning and Linear Attention We build on the setting of (Garg et al, 2022; Mahankali et al, 2024; Zhang et al, 2023; Li et al, 2024) and construct the in-context prompts with examples drawn from the model (2) as follows"
  - Updated tuple: (same sentence, True, "not enough information")

- Sentence: "3 Loss Landscape of One-layer Linear Attention under SS-ICL Previous work (Ahn et al, 2023; Li et al, 2024; Mahankali et al, 2024) has shown that an optimized single-layer linear attention implements a form of preconditioned gradient descent over the linear in-context demonstrations provided within the prompt"
  - Updated tuple: (same sentence, True, "not enough information")

If you need the full explicit list returned with every duplicate tuple expanded (i.e., the enormous list with each tuple written out), I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.
  -> LLM list extracted as follows:
[['not enough information")\n\nIf you need the full explicit list returned with every duplicate tuple expanded (i.e.', 'the enormous list with each tuple written out)', 'I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.'], ['not enough information")\n\nIf you need the full explicit list returned with every duplicate tuple expanded (i.e.', 'the enormous list with each tuple written out)', 'I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.'], ['not enough information")\n\nIf you need the full explicit list returned with every duplicate tuple expanded (i.e.', 'the enormous list with each tuple written out)', 'I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.'], ['not enough information")\n\nIf you need the full explicit list returned with every duplicate tuple expanded (i.e.', 'the enormous list with each tuple written out)', 'I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.'], ['not enough information")\n\nIf you need the full explicit list returned with every duplicate tuple expanded (i.e.', 'the enormous list with each tuple written out)', 'I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.'], ['not enough information")\n\nIf you need the full explicit list returned with every duplicate tuple expanded (i.e.', 'the enormous list with each tuple written out)', 'I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.'], ['not enough information")\n\nIf you need the full explicit list returned with every duplicate tuple expanded (i.e.', 'the enormous list with each tuple written out)', 'I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.'], ['not enough information")\n\nIf you need the full explicit list returned with every duplicate tuple expanded (i.e.', 'the enormous list with each tuple written out)', 'I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.'], ['not enough information")\n\nIf you need the full explicit list returned with every duplicate tuple expanded (i.e.', 'the enormous list with each tuple written out)', 'I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.'], ['not enough information")\n\nIf you need the full explicit list returned with every duplicate tuple expanded (i.e.', 'the enormous list with each tuple written out)', 'I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.'], ['not enough information")\n\nIf you need the full explicit list returned with every duplicate tuple expanded (i.e.', 'the enormous list with each tuple written out)', 'I can produce that as well; I withheld repeating thousands of identical updates here to keep the response compact.']]
-> Missing an abstract for reference with index 32 (Ref. ID = Min et al 2022); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = Montanari et al 2019); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = Neopane 2018); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = Nigam et al 2000); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = Oymak and Gulcu 2021); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = Qu et al 2025); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = Ratsaby and Venkatesh 1995); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = Shen et al 2024); Skipping LLM check...
-> Missing an abstract for reference with index 40 (Ref. ID = Snell et al 2024); Skipping LLM check...
-> Missing an abstract for reference with index 41 (Ref. ID = Thrampoulidis et al 2020); Skipping LLM check...
-> WARNING: Reference with index 42 (Ref. ID = Oswald et al 2023) has no associated sentence!
-> WARNING: Reference with index 43 (Ref. ID = Wang and Thrampoulidis 2022) has no associated sentence!
-> Missing an abstract for reference with index 44 (Ref. ID = Wang et al 2024); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 48 (Ref. ID = Xu et al 2021); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = Yang et al 2024); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = Ye et al 2025); Skipping LLM check...
-> Missing an abstract for reference with index 51 (Ref. ID = Zhang et al 2023); Skipping LLM check...
-> WARNING: Reference with index 52 (Ref. ID = Zhang et al 2024) has no associated sentence!
-> Missing an abstract for reference with index 53 (Ref. ID = Zhou et al 2024); Skipping LLM check...
-> Missing an abstract for reference with index 54 (Ref. ID = A 0); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 56 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 112 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 446 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 385 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 162 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 11833 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 9
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 10
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 11
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 12
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 13
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\14 When and How Unlabeled Data Provably Improve\PAU_results.md
```