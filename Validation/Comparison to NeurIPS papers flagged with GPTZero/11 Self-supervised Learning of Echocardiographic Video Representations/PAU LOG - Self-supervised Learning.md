
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\11 Self-supervised Learning of Echocardiographic Video Representations\Self-supervised Learning of Echocardiographic Video Representations via.pdf"
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
- Found following heading '2 - Related Work' on page 3
- Found following heading '3 - Methodology' on page 4
- Found following heading '4 - Experiments and Results' on page 6
- Found following heading '5 - Ablation Study' on page 8
- Found following heading '6 - Conclusion' on page 9
=> Found references/literature section on page 10
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 12
All found references: 38
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ... link  valid
0       1  Anas Al-Lahham, Nurbek Tastan, Muhammad Zaigha...  ...        None
1       2  Sagie Benaim, Ariel Ephrat, Oran Lang, Inbar M...  ...        None
2       3  Mathilde Caron, Hugo Touvron, Ishan Misra, Her...  ...        None
3       4  Ting Chen, Simon Kornblith, Mohammad Norouzi, ...  ...        None
4       5  Yutong Chen, Hongzuo Xu, Guansong Pang, Hezhe ...  ...        None
5       6                                   Cleveland Clinic  ...        None
6       7  Fenglin Ding, Debesh Jha, Maria Härgestam, Pål...  ...        None
7       8  Grant Duffy, Paul P Cheng, Neal Yuan, Bryan He...  ...        None
8       9  David Fan, Jue Wang, Shuai Liao, Yi Zhu, Vimal...  ...        None
9      10  Christoph Feichtenhofer, Yanghao Li, Kaiming H...  ...        None
10     11  Spyros Gidaris, Praveer Singh, and Nikos Komod...  ...        None
11     12  Dong Gong, Lingqiao Liu, Vuong Le, Budhaditya ...  ...        None
12     13  Kaiming He, Haoqi Fan, Yuxin Wu, Saining Xie, ...  ...        None
13     14  Bingkun Huang, Zhiyu Zhao, Guozhen Zhang, Yu Q...  ...        None
14     15  Jianbo Jiao, Richard Droste, Lior Drukker, Ari...  ...        None
15     16  Zheng Jiao, Haoran Dai, Daniel Rueckert, and W...  ...        None
16     17          Dahun Kim, Donghyeon Cho, and In So Kweon  ...        None
17     18               RM Lang, LP Badano, V Mor-Avi, et al  ...        None
18     19  Sarah Leclerc, Erik Smistad, Joao Pedrosa, And...  ...        None
19     20  Bálint Magyar, Márton Tokodi, András Soós, Mát...  ...        None
20     21  Divyanshu Mishra, He Zhao, Pramit Saha, Aris T...  ...        None
21     22  Ishan Misra, C Lawrence Zitnick, and Martial H...  ...        None
22     23                     Mehdi Noroozi and Paolo Favaro  ...        None
23     24    Aaron van den Oord, Yazhe Li, and Oriol Vinyals  ...        None
24     25  David Ouyang, Bryan He, Amirata Ghorbani, Neal...  ...        None
25     26        Hyunjong Park, Jongyoun Noh, and Bumsub Ham  ...        None
26     27  Fernando Pérez-García, Harshita Sharma, Sam Bo...  ...        None
27     28  Hadrien Reynaud, Alberto Gomez, Paul Leeson, Q...  ...        None
28     29  Pramit Saha, Divyanshu Mishra, Netzahualcoyotl...  ...        None
29     30  Mohammadreza Salehi, Michael Dorkenwald, Fida ...  ...        None
30     31   Zhan Tong, Yibing Song, Jue Wang, and Limin Wang  ...        None
31     32        Jiangliu Wang, Jianbo Jiao, and Yun-Hui Liu  ...        None
32     33  Rui Wang, Dongdong Chen, Zuxuan Wu, Yinpeng Ch...  ...        None
33     34  Jhih-Ciang Wu, He-Yen Hsieh, Ding-Jie Chen, Ch...  ...        None
34     35  Zhirong Wu, Yuanjun Xiong, Stella X Yu, and Da...  ...        None
35     36  Dejing Xu, Jun Xiao, Zhou Zhao, Jian Shao, Di ...  ...        None
36     37   Richard Zhang, Phillip Isola, and Alexei A Efros  ...        None
37     38  Xinyu Zhuang, Wangmeng Zuo, Dongwei Lin, Cheng...  ...        None

[38 rows x 10 columns]
- Checking reference 1/38:
  -> INFO: Now checking 2 results for matching title: 'A coarse-to-fine pseudo-labeling (c2fpl) framework for unsupervised video anomaly detection'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/38:
  -> INFO: Now checking 2 results for matching title: 'Speednet: Learning the speediness in videos'
       -> INFO: All authors matched!
- Checking reference 3/38:
  -> INFO: Now checking 10 results for matching title: 'Emerging properties in self-supervised vision transformers'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 6)
                   Unmatched authors = 'J'egou'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/38:
  -> INFO: Now checking 5 results for matching title: 'A simple framework for contrastive learning of visual representations'
       -> INFO: All authors matched!
- Checking reference 5/38:
  -> INFO: Now checking 10 results for matching title: 'Self-supervised spatial-temporal normality learning for time series anomaly detection'
       -> INFO: All authors matched!
- Checking reference 6/38:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Ejection fraction: What it is, types and normal range, 2023
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 997 results for matching title: 'Ejection fraction: What it is, types and normal range, 2023'
  -> WARNING: None of the 997 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Ejection+fraction:+What+it+is%2C+types+and+normal+range%2C+2023 manually and check the results.
        -> Author(s): Cleveland Clinic
        -> Title:     Ejection fraction: What it is, types and normal range, 2023
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 7/38:
  -> INFO: Now checking 1 results for matching title: 'Vits: Vision transformer for video self-supervised pretraining of surgical phase recognition'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Ding', 'Jha', 'Härgestam', 'Halvorsen', 'Riegler', 'Johansen', 'Hänsch', 'Stensland', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vits:+Vision+transformer+for+video+self-supervised+pretraining+of+surgical+phase+recognition manually and check the results.
        -> Author(s): Fenglin Ding, Debesh Jha, Maria Härgestam, Pål Halvorsen, Michael A Riegler, Dag Johansen, Ronny Hänsch, and Håvard Stensland
        -> Title:     Vits: Vision transformer for video self-supervised pretraining of surgical phase recognition
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 8/38:
  -> INFO: Now checking 1 results for matching title: 'High-throughput precision phenotyping of left ventricular hypertrophy with cardiovascular deep learning'
       -> WARNING: Not all 18 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Liang, Schnittger, Ashley, Zou, Patel, Witteles, Ouyang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/38:
  -> INFO: Now checking 10 results for matching title: 'Motion-guided masking for spatiotemporal representation learning'
       -> INFO: All authors matched!
- Checking reference 10/38:
  -> INFO: Now checking 4 results for matching title: 'Masked autoencoders as spatiotemporal learners'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 11/38:
  -> INFO: Now checking 10 results for matching title: 'Unsupervised representation learning by predicting image rotations'
       -> INFO: All authors matched!
- Checking reference 12/38:
  -> INFO: Now checking 3 results for matching title: 'Memorizing normality to detect anomaly: Memoryaugmented deep autoencoder for unsupervised anomaly detection'
  -> WARNING: None of the 3 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Memorizing normality to detect anomaly: Memoryaugmented deep autoencoder for unsupervised anomaly detection'
  -> WARNING: None of the 2 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Memorizing+normality+to+detect+anomaly:+Memoryaugmented+deep+autoencoder+for+unsupervised+anomaly+detection manually and check the results.
        -> Author(s): Dong Gong, Lingqiao Liu, Vuong Le, Budhaditya Saha, Moussa Reda Mansour, Svetha Venkatesh, and Anton van den Hengel
        -> Title:     Memorizing normality to detect anomaly: Memoryaugmented deep autoencoder for unsupervised anomaly detection
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 13/38:
  -> INFO: Now checking 10 results for matching title: 'Momentum contrast for unsupervised visual representation learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 14/38:
  -> INFO: Now checking 2 results for matching title: 'Mgmae: Motion guided masking for video masked autoencoding'
       -> INFO: All authors matched!
- Checking reference 15/38:
  -> INFO: Now checking 10 results for matching title: 'Selfsupervised representation learning for ultrasound video'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jiao', 'Droste', 'Drukker', 'Papageorghiou', 'Noble', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Selfsupervised+representation+learning+for+ultrasound+video manually and check the results.
        -> Author(s): Jianbo Jiao, Richard Droste, Lior Drukker, Aris T Papageorghiou, and J Alison Noble
        -> Title:     Selfsupervised representation learning for ultrasound video
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 16/38:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Self-supervised cross-modal learning for ultrasound video-speech representation'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jiao', 'Dai', 'Rueckert', 'Bai', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Self-supervised+cross-modal+learning+for+ultrasound+video-speech+representation manually and check the results.
        -> Author(s): Zheng Jiao, Haoran Dai, Daniel Rueckert, and Wenjia Bai
        -> Title:     Self-supervised cross-modal learning for ultrasound video-speech representation
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 17/38:
  -> INFO: Now checking 3 results for matching title: 'Self-supervised video representation learning with space-time cubic puzzles'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/38:
  -> INFO: Now checking 3 results for matching title: 'Recommendations for cardiac chamber quantification by echocardiography in adults: an update from the american society of echocardiography and the european association of cardiovascular imaging'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lang', 'Badano', 'Mor-Avi', '2015']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Recommendations+for+cardiac+chamber+quantification+by+echocardiography+in+adults:+an+update+from+the+american+society+of+echocardiography+and+the+european+association+of+cardiovascular+imaging manually and check the results.
        -> Author(s): RM Lang, LP Badano, V Mor-Avi, et al
        -> Title:     Recommendations for cardiac chamber quantification by echocardiography in adults: an update from the american society of echocardiography and the european association of cardiovascular imaging
        -> Year:      2015
     -> Manual search was skipped by the user.
- Checking reference 19/38:
  -> INFO: Now checking 2 results for matching title: 'Deep learning for segmentation using an open large-scale dataset in 2d echocardiography'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 20/38:
  -> INFO: Now checking 1 results for matching title: 'Rvenet: a large echocardiographic dataset for the deep learning-based assessment of right ventricular function'
       -> INFO: All authors matched!
- Checking reference 21/38:
  -> INFO: Now checking 1 results for matching title: 'Dual conditioned diffusion models for out-of-distribution detection: Application to fetal ultrasound videos'
       -> INFO: All authors matched!
- Checking reference 22/38:
  -> INFO: Now checking 7 results for matching title: 'Shuffle and learn: unsupervised learning using temporal order verification'
       -> INFO: All authors matched!
- Checking reference 23/38:
  -> INFO: Now checking 2 results for matching title: 'Unsupervised learning of visual representations by solving jigsaw puzzles'
       -> INFO: All authors matched!
- Checking reference 24/38:
  -> INFO: Now checking 10 results for matching title: 'Representation learning with contrastive predictive coding'
       -> INFO: All authors matched!
- Checking reference 25/38:
  -> INFO: Now checking 2 results for matching title: 'Video-based ai for beat-to-beat assessment of cardiac function'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 26/38:
  -> INFO: Now checking 10 results for matching title: 'Learning memory-guided normality for anomaly detection'
       -> INFO: All authors matched!
- Checking reference 27/38:
  -> INFO: Now checking 3 results for matching title: 'Rad-dino: Exploring scalable medical image encoders beyond text supervision'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Pérez-García', 'Sharma', 'Bond-Taylor', 'Bouzid', 'Salvatelli', 'Ilse', 'Bannur', 'Castro', 'Schwaighofer', 'Lungren', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Rad-dino:+Exploring+scalable+medical+image+encoders+beyond+text+supervision manually and check the results.
        -> Author(s): Fernando Pérez-García, Harshita Sharma, Sam Bond-Taylor, Kenza Bouzid, Valentina Salvatelli, Maximilian Ilse, Shruthi Bannur, Daniel C Castro, Anton Schwaighofer, Matthew P Lungren, et al
        -> Title:     Rad-dino: Exploring scalable medical image encoders beyond text supervision
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 28/38:
  -> INFO: Now checking 1 results for matching title: 'Echoflow: A foundation model for cardiac ultrasound image and video generation'
       -> INFO: All authors matched!
- Checking reference 29/38:
  -> INFO: Now checking 1 results for matching title: 'Self-supervised normality learning and divergence vector-guided model merging for zero-shot congenital heart disease detection in fetal ultrasound videos'
       -> INFO: All authors matched!
- Checking reference 30/38:
  -> INFO: Now checking 10 results for matching title: 'Sigma: Sinkhorn-guided masked video modeling'
       -> INFO: All authors matched!
- Checking reference 31/38:
  -> INFO: Now checking 3 results for matching title: 'Videomae: Masked autoencoders are data-efficient learners for self-supervised video pre-training'
       -> INFO: All authors matched!
- Checking reference 32/38:
  -> INFO: Now checking 10 results for matching title: 'Self-supervised video representation learning by pace prediction'
       -> INFO: All authors matched!
- Checking reference 33/38:
  -> INFO: Now checking 5 results for matching title: 'Masked video distillation: Rethinking masked feature modeling for selfsupervised video representation learning'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Chen', 'Wu', 'Chen', 'Dai', 'Liu', 'Yuan', 'Jiang', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Masked+video+distillation:+Rethinking+masked+feature+modeling+for+selfsupervised+video+representation+learning manually and check the results.
        -> Author(s): Rui Wang, Dongdong Chen, Zuxuan Wu, Yinpeng Chen, Xiyang Dai, Mengchen Liu, Lu Yuan, and Yu-Gang Jiang
        -> Title:     Masked video distillation: Rethinking masked feature modeling for selfsupervised video representation learning
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 34/38:
  -> INFO: Now checking 10 results for matching title: 'Selfsupervised sparse representation for video anomaly detection'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'Hsieh', 'Chen', 'Fuh', 'Liu', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Selfsupervised+sparse+representation+for+video+anomaly+detection manually and check the results.
        -> Author(s): Jhih-Ciang Wu, He-Yen Hsieh, Ding-Jie Chen, Chiou-Shann Fuh, and Tyng-Luh Liu
        -> Title:     Selfsupervised sparse representation for video anomaly detection
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 35/38:
  -> INFO: Now checking 10 results for matching title: 'Unsupervised feature learning via non-parametric instance discrimination'
       -> INFO: All authors matched!
- Checking reference 36/38:
  -> INFO: Now checking 10 results for matching title: 'Self-supervised spatiotemporal learning via video clip order prediction'
       -> INFO: All authors matched!
- Checking reference 37/38:
  -> INFO: Now checking 10 results for matching title: 'Colorful image colorization'
       -> INFO: All authors matched!
- Checking reference 38/38:
  -> INFO: Now checking 10 results for matching title: 'Self-supervised learning via conditional motion propagation'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Pan, Liu, Loy'
  -> INFO: No perfect match found; taking the next best!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 3: θt ←λθt + (1 −λ)θs,
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Bracket content ['0'] on p. 4 could not be matched to a reference.
   -> Sentence:  Both encoders output a global video representation via the CLS token: zt = Eθt(v)[0], z(m) s = Eθs(vMm)[0]
-> Warning: Bracket content ['0'] on p. 4 could not be matched to a reference.
   -> Sentence:  Both encoders output a global video representation via the CLS token: zt = Eθt(v)[0], z(m) s = Eθs(vMm)[0]
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 530 sentences on 10 pages -> Avg. of 59.888888888888886 sentences per page
---
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
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
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 4 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 5 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 121 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 7
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 8
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 9
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 10
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 11
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
###############################
# Starting Author Check
###############################
-> Saved chapter_fig on try 1
-> Saved lit_fig on try 1
-> Saved rank_fig on try 1
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\11 Self-supervised Learning of Echocardiographic Video Representations\PAU_results.md
```