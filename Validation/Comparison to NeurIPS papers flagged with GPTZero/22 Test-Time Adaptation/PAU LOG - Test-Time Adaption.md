
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\22 Test-Time Adaptation\Test-Time Adaptation of Vision-Language Models for Open-Vocabulary S.pdf"
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
- Found Introduction on page 1
- Found following heading '2 - Related Work' on page 3
- Found following heading '3 - Methodology' on page 3
- Found following heading '4 - Experimental Settings' on page 6
- Found following heading '5 - Results' on page 7
- Found following heading '6 - Conclusion' on page 9
=> Found references/literature section on page 10
- Found first appendix 'A - Proof of Proposition 1' on page 13
- Found following appendix 'B - Implementation Details' on page 13
- Found following appendix 'C - Template Details' on page 14
- Found following appendix 'D - Dataset Details' on page 14
- Found following appendix 'E - Computational Complexity' on page 15
- Found following appendix 'F - Performance with a Single Test Sample' on page 15
- Found following appendix 'G - Generalization Across Model Variants' on page 16
- Found following appendix 'H - Visualization of Layer-Wise Confidence Weights' on page 18
- Found following appendix 'I - Visualization of Segmentation Maps' on page 19
- Found following appendix 'J - Detailed Results of the Main Paper' on page 19
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 13
All found references: 39
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ... link  valid
0       1  Alec Radford, Jong Wook Kim, Chris Hallacy, Ad...  ...        None
1       2  Ziyi Lin, Shijie Geng, Renrui Zhang, Peng Gao,...  ...        None
2       3  Andrey Guzhov, Federico Raue, Jörn Hees, and A...  ...        None
3       4  Jie Liu, Yixiao Zhang, Jie-Neng Chen, Junfei X...  ...        None
4       5  David Osowiechi, Mehrdad Noori, Gustavo Vargas...  ...        None
5       6  Manli Shu, Weili Nie, De-An Huang, Zhiding Yu,...  ...        None
6       7  Zachary Nado, Shreyas Padhy, D  Sculley, Alexa...  ...        None
7       8  Dequan Wang, Evan Shelhamer, Shaoteng Liu, Bru...  ...        None
8       9      Marvin Zhang, Sergey Levine, and Chelsea Finn  ...        None
9      10  Malik Boudiaf, Romain Mueller, Ismail Ben Ayed...  ...        None
10     11  Shuaicheng Niu, Jiaxiang Wu, Yifan Zhang, Zhiq...  ...        None
11     12  Hong Liu, Guoliang Kang, Shan You, Jiancheng B...  ...        None
12     13  Jiacheng He, Zhilu Zhang, Zhen Wang, and Yan H...  ...        None
13     14  Charanpal D Mummadi, Matthias Arens, and Thoma...  ...        None
14     15  Gabriele Valvano, Andrea Leo, Kuniaki Saito, a...  ...        None
15     16         Zhi Wang, Yue Zhang, Kun Yu, and Hao Zhang  ...        None
16     17  Davide Barsellotti, Roberto Amoroso, and Barba...  ...        None
17     18  Golnaz Ghiasi, Yin Cui, Aravind Srinivas, Rui ...  ...        None
18     19  Feng Liang, Bichen Wu, Xiaoliang Dai, Kunpeng ...  ...        None
19     20  Kaixin Cai, Pengzhen Ren, Yi Zhu, Hang Xu, Jia...  ...        None
20     21        Junbum Cha, Jonghwan Mun, and Byungseok Roh  ...        None
21     22  Yuxin Chen, Yujie Li, Zhaoxiang Zhang, and Yun...  ...        None
22     23  Jiarui Xu, Shalini De Mello, Sifei Liu, and Xi...  ...        None
23     24  Davide Barsellotti, Roberto Amoroso, and Barba...  ...        None
24     25  Andrea Corradini, Federico Bianchi, Debora Noz...  ...        None
25     26  Lukas Karazija, Wafaa Bousselham, Andrei Bursu...  ...        None
26     27              Feng Wang, Jieru Mei, and Alan Yuille  ...        None
27     28            Chong Zhou, Chen Change Loy, and Bo Dai  ...        None
28     29  Wafaa Bousselham, Andrei Bursuc, Thiemo Alldie...  ...        None
29     30      Sina Hajimiri, Ismail Ben Ayed, and Jose Dolz  ...        None
30     31  Gustavo Adolfo Vargas Hakim, David Osowiechi, ...  ...        None
31     32  Olaf Ronneberger, Philipp Fischer, and Thomas ...  ...        None
32     33                Dan Hendrycks and Thomas Dietterich  ...        None
33     34  Mark Everingham, Luc Van Gool, Christopher K  ...  ...        None
34     35  Roozbeh Mottaghi, Xianjie Chen, Xiaobai Liu, N...  ...        None
35     36  Marius Cordts, Mohamed Omran, Sebastian Ramos,...  ...        None
36     37  Holger Caesar, Jasper R  R  Uijlings, and Vitt...  ...        None
37     38  Tsung-Yi Lin, Michael Maire, Serge J  Belongie...  ...        None
38     39  Michael Tschannen, Alexey Gritsenko, Xiao Wang...  ...        None

[39 rows x 10 columns]
- Checking reference 1/39:
  -> INFO: Now checking 10 results for matching title: 'Learning transferable visual models from natural language supervision'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 2/39:
  -> INFO: Now checking 10 results for matching title: 'Frozen clip models are efficient video learners'
       -> INFO: All authors matched!
- Checking reference 3/39:
  -> INFO: Now checking 1 results for matching title: 'Audioclip: Extending clip to image, text and audio'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/39:
  -> INFO: Now checking 2 results for matching title: 'Clip-driven universal model for organ segmentation and tumor detection'
       -> INFO: All authors matched!
- Checking reference 5/39:
  -> INFO: Now checking 9 results for matching title: 'Watt: Weight average test time adaptation of clip'
       -> INFO: All authors matched!
- Checking reference 6/39:
  -> INFO: Now checking 10 results for matching title: 'Test-time prompt tuning for zero-shot generalization in vision-language models'
       -> INFO: All authors matched!
- Checking reference 7/39:
  -> INFO: Now checking 6 results for matching title: 'Evaluating prediction-time batch normalization for robustness under covariate shift'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2006)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/39:
  -> INFO: Now checking 10 results for matching title: 'Tent: Fully test-time adaptation by entropy minimization'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/39:
  -> INFO: Now checking 10 results for matching title: 'Memo: Test time robustness via adaptation and augmentation'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/39:
  -> INFO: Now checking 10 results for matching title: 'Parameter-free online test-time adaptation'
       -> INFO: All authors matched!
- Checking reference 11/39:
  -> INFO: Now checking 10 results for matching title: 'Towards stable test-time adaptation in dynamic wild world.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Towards stable test-time adaptation in dynamic wild world.'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 5)
                   Unmatched authors = '0001, 0004'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 5)
                   Unmatched authors = '0001, 0004'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/39:
  -> INFO: Now checking 10 results for matching title: 'Source-free domain adaptation for semantic segmentation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/39:
  -> INFO: Now checking 10 results for matching title: 'Autoencoder based test-time adaptation for semantic segmentation'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 116 results for matching title: 'Autoencoder based test-time adaptation for semantic segmentation'
  -> WARNING: None of the 116 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Autoencoder+based+test-time+adaptation+for+semantic+segmentation manually and check the results.
        -> Author(s): Jiacheng He, Zhilu Zhang, Zhen Wang, and Yan Huang
        -> Title:     Autoencoder based test-time adaptation for semantic segmentation
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 14/39:
  -> INFO: Now checking 10 results for matching title: 'Test-time adaptation for continual semantic segmentation'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Mummadi', 'Arens', 'Brox', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Test-time+adaptation+for+continual+semantic+segmentation manually and check the results.
        -> Author(s): Charanpal D Mummadi, Matthias Arens, and Thomas Brox
        -> Title:     Test-time adaptation for continual semantic segmentation
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 15/39:
  -> INFO: Now checking 10 results for matching title: 'Learning multi-modal self-supervision for test-time adaptation'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Valvano', 'Leo', 'Saito', 'Tommasi', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Learning+multi-modal+self-supervision+for+test-time+adaptation manually and check the results.
        -> Author(s): Gabriele Valvano, Andrea Leo, Kuniaki Saito, and Tatiana Tommasi
        -> Title:     Learning multi-modal self-supervision for test-time adaptation
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 16/39:
  -> INFO: Now checking 10 results for matching title: 'Active test-time adaptation for semantic segmentation'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Zhang', 'Yu', 'Zhang', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Active+test-time+adaptation+for+semantic+segmentation manually and check the results.
        -> Author(s): Zhi Wang, Yue Zhang, Kun Yu, and Hao Zhang
        -> Title:     Active test-time adaptation for semantic segmentation
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 17/39:
  -> INFO: Now checking 10 results for matching title: 'Enhancing open-vocabulary semantic segmentation with prototype retrieval'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Baraldi, Cucchiara'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/39:
  -> INFO: Now checking 10 results for matching title: 'Scaling open-vocabulary image segmentation with image-level labels'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Gu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 19/39:
  -> INFO: Now checking 10 results for matching title: 'Open-vocabulary semantic segmentation with mask-adapted clip'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/39:
  -> INFO: Now checking 1 results for matching title: 'Mixreorg: Cross-modal mixed patch reorganization is a good mask learner for open-world semantic segmentation'
       -> INFO: All authors matched!
- Checking reference 21/39:
  -> INFO: Now checking 6 results for matching title: 'Learning to generate text-grounded mask for open-world semantic segmentation from only image-text pairs'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 22/39:
  -> INFO: Now checking 10 results for matching title: 'Exploring open-vocabulary semantic segmentation from clip vision encoder distillation only'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zhu, Qian, Ghanem, Yan, Zhu, Xiao, Culatana, Elhoseiny'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 23/39:
  -> INFO: Now checking 10 results for matching title: 'Groupvit: Semantic segmentation emerges from text supervision'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Byeon, Breuel, Kautz'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 24/39:
  -> INFO: Now checking 2 results for matching title: 'Fossil: Free open-vocabulary semantic segmentation through synthetic references retrieval'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Baraldi, Cucchiara'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 25/39:
  -> INFO: Now checking 1 results for matching title: 'Freeseg-diff: Training-free open-vocabulary segmentation with diffusion models'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Shukor, Couairon, Couairon, Scarselli, Cord'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/39:
  -> INFO: Now checking 10 results for matching title: 'Diffusion models for zero-shot open-vocabulary segmentation'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Karazija', 'Bousselham', 'Bursuc', 'Alldieck', 'Pérez', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Diffusion+models+for+zero-shot+open-vocabulary+segmentation manually and check the results.
        -> Author(s): Lukas Karazija, Wafaa Bousselham, Andrei Bursuc, Thiemo Alldieck, and Patrick Pérez
        -> Title:     Diffusion models for zero-shot open-vocabulary segmentation
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 27/39:
  -> INFO: Now checking 1 results for matching title: 'SCLIP: Rethinking self-attention for dense visionlanguage inference'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Mei', 'Yuille', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=SCLIP:+Rethinking+self-attention+for+dense+visionlanguage+inference manually and check the results.
        -> Author(s): Feng Wang, Jieru Mei, and Alan Yuille
        -> Title:     SCLIP: Rethinking self-attention for dense visionlanguage inference
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 28/39:
  -> INFO: Now checking 10 results for matching title: 'Extract free dense labels from clip'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/39:
  -> INFO: Now checking 1 results for matching title: 'Grounding everything: Emerging localization properties in vision-language transformers'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Petersen, Ferrari, Kuehne'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/39:
  -> INFO: Now checking 1 results for matching title: 'Pay attention to your neighbours: Training-free open-vocabulary semantic segmentation'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/39:
  -> INFO: Now checking 2 results for matching title: 'Clipartt: Light-weight adaptation of clip to new domains at test time'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hakim', 'Osowiechi', 'Noori', 'Cheraghalikhani', 'Bahri', 'Yazdanpanah', 'Ayed', 'Desrosiers', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Clipartt:+Light-weight+adaptation+of+clip+to+new+domains+at+test+time manually and check the results.
        -> Author(s): Gustavo Adolfo Vargas Hakim, David Osowiechi, Mehrdad Noori, Milad Cheraghalikhani, Ali Bahri, Moslem Yazdanpanah, Ismail Ben Ayed, and Christian Desrosiers
        -> Title:     Clipartt: Light-weight adaptation of clip to new domains at test time
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 32/39:
  -> INFO: Now checking 10 results for matching title: 'U-net: Convolutional networks for biomedical image segmentation'
       -> INFO: All authors matched!
- Checking reference 33/39:
  -> INFO: Now checking 10 results for matching title: 'Benchmarking neural network robustness to common corruptions and perturbations'
       -> INFO: All authors matched!
- Checking reference 34/39:
  -> INFO: Now checking 10 results for matching title: 'The pascal visual object classes (voc) challenge'
       -> INFO: All authors matched!
- Checking reference 35/39:
  -> INFO: Now checking 1 results for matching title: 'The role of context for object detection and semantic segmentation in the wild'
       -> INFO: All authors matched!
- Checking reference 36/39:
  -> INFO: Now checking 10 results for matching title: 'The cityscapes dataset for semantic urban scene understanding'
       -> INFO: All authors matched!
- Checking reference 37/39:
  -> INFO: Now checking 6 results for matching title: 'Coco-stuff: Thing and stuff classes in context'
       -> INFO: All authors matched!
- Checking reference 38/39:
  -> INFO: Now checking 10 results for matching title: 'Microsoft COCO: common objects in context'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 8)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 39/39:
  -> INFO: Now checking 1 results for matching title: 'Siglip 2: Multilingual vision-language encoders with improved semantic understanding, localization, and dense features'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 4: H(P) = −
-> Invalid unicode use found on p. 4: exp(−β·hℓ)
-> Invalid unicode use found on p. 4: ℓ′=1 exp(−β·hℓ′)
-> Invalid unicode use found on p. 4: LILE(T) = −1
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 778 sentences on 10 pages -> Avg. of 87.44444444444444 sentences per page
-> Warning: Reference '39' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 4 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
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
  -> Found 26 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 16
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 17
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 18
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 19
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 20
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\22 Test-Time Adaptation\PAU_results.md
```