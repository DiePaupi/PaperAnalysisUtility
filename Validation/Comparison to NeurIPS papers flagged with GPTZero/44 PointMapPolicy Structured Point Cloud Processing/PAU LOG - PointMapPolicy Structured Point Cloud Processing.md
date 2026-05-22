
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\44 PointMapPolicy Structured Point Cloud Processing\PointMapPolicy Structured Point Cloud Processing for Multi-Modal Imitati.pdf"
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
- Found following heading '2 - Related Work' on page 2
- Found following heading '3 - Method' on page 3
- Found following heading '4 - Simulation Experiments' on page 5
- Found following heading '5 - ABC→D' on page 7
- Found following heading '6 - Limitation and Future Work' on page 9
- Found following heading '7 - Conclusion' on page 9
=> Found references/literature section on page 10
- Found first appendix 'A - Simulation Experiment Details' on page 15
- Found following appendix 'B - Real World Experiment Details' on page 17
- Found following appendix 'C - Hyper Parameters' on page 18
- Found following appendix 'D - Activation Map Analysis' on page 18
- Found following appendix 'E - Compute Resources' on page 22
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 15
All found references: 60
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                               link  valid
0       1  Lingdong Chi, Aravind Rajeswaran Gupta, Silvio...  ...                                                      None
1       2  Kevin Black, Noah Brown, Danny Driess, Adnan E...  ...                                      https://arxiv   None
2       3  Xiaogang Jia, Denis Blessing, Xinkai Jiang, Mo...  ...                                                      None
3       4  Haoyi Zhu, Yating Wang, Di Huang, Weicai Ye, W...  ...         https://openreview.net/forum?id=zgSnSZ0Re6   None
4       5  Skand Peri, Iain Lee, Chanho Kim, Li Fuxin, Tu...  ...                   https://arxiv.org/abs/2404.18926   None
5       6  Balazs Gyenes, Nikolai Franke, Philipp Becker,...  ...         https://openreview.net/forum?id=3jNEz3kUSl   None
6       7  Yanjie Ze, Gu Zhang, Kangning Zhang, Chenyuan ...  ...                                                      None
7       8  Eugenio Chisari, Nick Heppert, Max Argus, Tim ...  ...         https://openreview.net/forum?id=vtEn8NJWlz   None
8       9  Zhou Xian, Nikolaos Gkanatsios, Theophile Gerv...  ...        https://openreview.net/forum?id=W0zgY2mBTA8   None
9      10  Shuzhe Wang, Vincent Leroy, Yohann Cabon, Bori...  ...                                                      None
10     11     Vincent Leroy, Yohann Cabon, and Jerome Revaud  ...                                                      None
11     12  Kaiming He, Xiangyu Zhang, Shaoqing Ren, and J...  ...  https://openaccess.thecvf.com/content_cvpr_201...   None
12     13  Alexey Dosovitskiy, Lucas Beyer, Alexander Kol...  ...         https://openreview.net/forum?id=YicbFdNTTy   None
13     14  Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, Christoph...  ...                                                      None
14     15  Charles Ruizhongtai Qi, Li Yi, Hao Su, and Leo...  ...                                                      None
15     16  Yatian Pang, Wenxiao Wang, Francis E H Tay, We...  ...                                                      None
16     17  Guangyan Chen, Meiling Wang, Yi Yang, Kai Yu, ...  ...                    http://arxiv.org/abs/2305.11487   None
17     18  Tero Karras, Miika Aittala, Timo Aila, and Sam...  ...        https://openreview.net/forum?id=k7FuTOWMOc7   None
18     19  Soroush Nasiriany, Abhiram Maddukuri, Lance Zh...  ...                                                      None
19     20  Oier Mees, Daniel Merk, Yannik Bukschat, Harsh...  ...                                                      None
20     21  Songming Liu, Lingxuan Wu, Bangguo Li, Hengkai...  ...         https://openreview.net/forum?id=yAzN4tz7oI   None
21     22  Moo Jin Kim, Karl Pertsch, Siddharth Karamchet...  ...         https://openreview.net/forum?id=ZMnD6QZAE6   None
22     23  Moritz Reuss, Jyothish Pari, Pulkit Agrawal, a...  ...         https://openreview.net/forum?id=nDmwloEl3N   None
23     24  Octo Model Team, Dibya Ghosh, Homer Walke, Kar...  ...                                                      None
24     25  Stephen James, Kentaro Wada, Tristan Laidlow, ...  ...  https://doi.ieeecomputersociety.org/10.1109/CV...   None
25     26     Mohit Shridhar, Lucas Manuelli, and Dieter Fox  ...        https://openreview.net/forum?id=PS_eCS_WCvD   None
26     27  Tsung-Wei Ke, Nikolaos Gkanatsios, and Katerin...  ...                                                      None
27     28  Atalay Donat, Xiaogang Jia, Xi Huang, Aleksand...  ...         https://openreview.net/forum?id=5cG7ilWX1V   None
28     29  Ankit Goyal, Jie Xu, Yijie Guo, Valts Blukis, ...  ...         https://openreview.net/forum?id=0hPkttoGAf   None
29     30  Ankit Goyal, Valts Blukis, Jie Xu, Yijie Guo, ...  ...         https://openreview.net/forum?id=T6c4qoc6PG   None
30     31     Mohit Shridhar, Lucas Manuelli, and Dieter Fox  ...                                                      None
31     32  Ajay Mandlekar, Danfei Xu, Josiah Wong, Sorous...  ...        https://openreview.net/forum?id=JrsfBJtDFdI   None
32     33  Nur Muhammad Mahi Shafiullah, Zichen Jeff Cui,...  ...         https://openreview.net/forum?id=agTr-vRQsa   None
33     34  Moritz Reuss, Maximilian Li, Xiaogang Jia, and...  ...          https://doi.org/10.15607/RSS.2023.XIX.028   None
34     35  Homanga Bharadhwaj, Jay Vakil, Mohit Sharma, A...  ...         https://openreview.net/forum?id=Pt5N3OG5wP   None
35     36  Xiaogang Jia, Qian Wang, Atalay Donat, Bowen X...  ...                   https://arxiv.org/abs/2406.08234   None
36     37  Xiaogang Jia, Atalay Donat, Xi Huang, Xuan Zha...  ...         https://openreview.net/forum?id=8w0OJsTaFz   None
37     38                              Albert Gu and Tri Dao  ...         https://openreview.net/forum?id=AL1fq05o7H   None
38     39  Maximilian Beck, Korbinian Pöppel, Markus Span...  ...         https://openreview.net/forum?id=ARAxPPIAhq   None
39     40  Tony Z Zhao, Vikash Kumar, Sergey Levine, and ...  ...                                                      None
40     41  Moritz Reuss, Maximilian Li, Xiaogang Jia, and...  ...                                                      None
41     42                                     Pascal Vincent  ...                                                      None
42     43      Jiaming Song, Chenlin Meng, and Stefano Ermon  ...                                                      None
43     44  Alec Radford, Jong Wook Kim, Chris Hallacy, Ad...  ...                                                      None
44     45  Ethan Perez, Florian Strub, Harm De Vries, Vin...  ...                                                      None
45     46  Johan Bjorck, Fernando Castañeda, Nikita Chern...  ...                                                      None
46     47  Xinyang Bu, Fan Yang, Vikash Kumar, Stephan Ma...  ...                                                      None
47     48  Moritz Reuss, Ömer Erdinç Ya˘gmurlu, Fabian We...  ...                                                      None
48     49  Yilun Zhou, Yufei Wu, De-An Huang, Yilun Zhang...  ...                                                      None
49     50  Xinghang Li, Minghuan Liu, Hanbo Zhang, Cunjun...  ...                                                      None
50     51                                 Andrew Black et al  ...                                                      None
51     52  Hongtao Wu, Ya Jing, Chilam Cheang, Guangzeng ...  ...                                                      None
52     53  Qingwen Bu, Hongyang Li, Li Chen, Jisong Cai, ...  ...                                                      None
53     54  Aditya Chattopadhay, Anirban Sarkar, Prantik H...  ...                                                      None
54     55  Oier Mees, Harsh Lodhi, Daniel Merk, Yannik Bu...  ...                                                      None
55     56  Shuang Zhang, Ilija Radosavovic, Kaiming He, A...  ...                                                      None
56     57  Duy Ha, Ajay Mandlekar, Andy Zeng, Yunzhu Chai...  ...                                                      None
57     58  Zichen Liu, Rakibul Hoque, Kevin Zakka, Shuran...  ...                                                      None
58     59  Yufei Wu, Kiran Alwala, Vivek Ganapathi, Sudee...  ...                                                      None
59     60  Yilun Zhou, Yen-Chen Lin, De-An Huang, Yao Lu,...  ...                                                      None

[60 rows x 10 columns]
- Checking reference 1/60:
  -> INFO: Now checking 10 results for matching title: 'Diffusion policy: Visuomotor policy learning via action diffusion'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Feng, Du, Xu, Cousineau, Burchfiel, Song'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/60:
  -> Checking if provided link is pingable: https://arxiv
  -> INFO: Now checking 10 results for matching title: 'π0: A vision-language-action flow model for general robot control.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'π0: A vision-language-action flow model for general robot control.'
       -> WARNING: Not all 24 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Jakubczak, Jones, Levine, Li-Bell, Mothukuri, 0003, Pertsch, Shi, Tanner, Vuong, Walling, Wang, Zhilinsky'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/60:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'Towards diverse behaviors: A benchmark for imitation learning with human demonstrations'
       -> INFO: All authors matched!
- Checking reference 4/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=zgSnSZ0Re6
  -> INFO: Now checking 1 results for matching title: 'Point cloud matters: Rethinking the impact of different observation spaces on robot learning'
       -> INFO: All authors matched!
- Checking reference 5/60:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2404.18926
  -> INFO: Now checking 10 results for matching title: 'Point cloud models improve visual robustness in robotic learners.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Point cloud models improve visual robustness in robotic learners.'
       -> INFO: All authors matched!
- Checking reference 6/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=3jNEz3kUSl
  -> INFO: Now checking 1 results for matching title: 'PointpatchRL - masked reconstruction improves reinforcement learning on point clouds'
       -> INFO: All authors matched!
- Checking reference 7/60:
  -> INFO: Now checking 10 results for matching title: '3d diffusion policy: Generalizable visuomotor policy learning via simple 3d representations'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 185 results for matching title: '3d diffusion policy: Generalizable visuomotor policy learning via simple 3d representations'
  -> WARNING: None of the 185 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=3d+diffusion+policy:+Generalizable+visuomotor+policy+learning+via+simple+3d+representations manually and check the results.
        -> Author(s): Yanjie Ze, Gu Zhang, Kangning Zhang, Chenyuan Hu, Muhan Wang, and Huazhe Xu
        -> Title:     3d diffusion policy: Generalizable visuomotor policy learning via simple 3d representations
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 8/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=vtEn8NJWlz
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Learning robotic manipulation policies from point clouds with conditional flow matching'
       -> INFO: All authors matched!
- Checking reference 9/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=W0zgY2mBTA8
  -> INFO: Now checking 1 results for matching title: 'Chaineddiffuser: Unifying trajectory diffusion and keypose prediction for robotic manipulation'
       -> INFO: All authors matched!
- Checking reference 10/60:
  -> INFO: Now checking 10 results for matching title: 'Dust3r: Geometric 3d vision made easy'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/60:
  -> INFO: Now checking 1 results for matching title: 'Grounding image matching in 3d with mast3r.'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 4 results for matching title: 'Grounding image matching in 3d with mast3r.'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0003'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0003'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/60:
  -> Checking if provided link is pingable: https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Deep Residual Learning for Image Recognition'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=YicbFdNTTy
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'An image is worth 16x16 words: Transformers for image recognition at scale'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 14/60:
  -> INFO: Now checking 3 results for matching title: 'A convnet for the 2020s'
       -> INFO: All authors matched!
- Checking reference 15/60:
  -> INFO: Now checking 3 results for matching title: 'Pointnet++: Deep hierarchical feature learning on point sets in a metric space'
       -> INFO: All authors matched!
- Checking reference 16/60:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Masked Autoencoders for Point Cloud Self-supervised Learning'
       -> INFO: All authors matched!
- Checking reference 17/60:
  -> Checking if provided link is pingable: http://arxiv.org/abs/2305.11487
  -> INFO: Now checking 6 results for matching title: 'PointGPT: Autoregressively Generative Pre-training from Point Clouds, May.'
  -> WARNING: None of the 6 results matched the expected title!
  -> INFO: Now checking 255 results for matching title: 'PointGPT: Autoregressively Generative Pre-training from Point Clouds, May.'
  -> WARNING: None of the 255 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=http://arxiv.org/abs/2305.11487 manually and check the results.
        -> Author(s): Guangyan Chen, Meiling Wang, Yi Yang, Kai Yu, Li Yuan, and Yufeng Yue
        -> Title:     PointGPT: Autoregressively Generative Pre-training from Point Clouds, May.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 18/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=k7FuTOWMOc7
  -> INFO: Now checking 6 results for matching title: 'Elucidating the design space of diffusion-based generative models'
       -> INFO: All authors matched!
- Checking reference 19/60:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 3 results for matching title: 'Robocasa: Large-scale simulation of everyday tasks for generalist robots'
       -> INFO: All authors matched!
- Checking reference 20/60:
  -> INFO: Now checking 7 results for matching title: 'Calvin: A benchmark for language-conditioned policy learning for long-horizon robot manipulation tasks'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Hermann, Rosete-Beas'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 21/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=yAzN4tz7oI
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'RDT-1b: a diffusion foundation model for bimanual manipulation'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 22/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=ZMnD6QZAE6
  -> INFO: Now checking 10 results for matching title: 'OpenVLA: An open-source vision-language-action model'
       -> WARNING: Not all 18 authors from the found ref. were matched (only 17)
                   Unmatched authors = 'Lam'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 23/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=nDmwloEl3N
  -> INFO: Now checking 2 results for matching title: 'Efficient diffusion transformer policies with mixture of expert denoisers for multitask learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 24/60:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Octo: An open-source generalist robot policy'
       -> INFO: All authors matched!
- Checking reference 25/60:
  -> Checking if provided link is pingable: https://doi.ieeecomputersociety.org/10.1109/CVPR52688.2022.01337
  -> INFO: Now checking 1 results for matching title: 'Coarse-toFine Q-attention: Efficient Learning for Visual Robotic Manipulation via Discretisation'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Coarse-toFine Q-attention: Efficient Learning for Visual Robotic Manipulation via Discretisation'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://doi.ieeecomputersociety.org/10.1109/CVPR52688.2022.01337 manually and check the results.
        -> Author(s): Stephen James, Kentaro Wada, Tristan Laidlow, and Andrew J Davison
        -> Title:     Coarse-toFine Q-attention: Efficient Learning for Visual Robotic Manipulation via Discretisation
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 26/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=PS_eCS_WCvD
  -> INFO: Now checking 2 results for matching title: 'Perceiver-actor: A multi-task transformer for robotic manipulation'
       -> INFO: All authors matched!
- Checking reference 27/60:
  -> INFO: Now checking 3 results for matching title: '3d diffuser actor: Policy diffusion with 3d scene representations'
       -> INFO: All authors matched!
- Checking reference 28/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=5cG7ilWX1V
  -> INFO: Now checking 1 results for matching title: 'Towards fusing point cloud and visual representations for imitation learning'
       -> INFO: All authors matched!
- Checking reference 29/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=0hPkttoGAf
  -> INFO: Now checking 10 results for matching title: 'RVT: Robotic view transformer for 3d object manipulation'
       -> INFO: All authors matched!
- Checking reference 30/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=T6c4qoc6PG
  -> INFO: Now checking 10 results for matching title: 'RVT-2: Learning precise manipulation from few demonstrations'
       -> INFO: All authors matched!
- Checking reference 31/60:
  -> INFO: Now checking 2 results for matching title: 'Perceiver-actor: A multi-task transformer for robotic manipulation'
       -> INFO: All authors matched!
- Checking reference 32/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=JrsfBJtDFdI
  -> INFO: Now checking 5 results for matching title: 'What matters in learning from offline human demonstrations for robot manipulation'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 9)
                   Unmatched authors = 'Mart'in-Mart'in'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=agTr-vRQsa
  -> INFO: Now checking 3 results for matching title: 'Behavior transformers: Cloning $k$ modes with one stone'
  -> WARNING: None of the 3 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Behavior transformers: Cloning $k$ modes with one stone'
  -> WARNING: None of the 2 results matched the expected title!
     -> You could also open https://openreview.net/forum?id=agTr-vRQsa manually and check the results.
        -> Author(s): Nur Muhammad Mahi Shafiullah, Zichen Jeff Cui, Ariuntuya Altanzaya, and Lerrel Pinto
        -> Title:     Behavior transformers: Cloning $k$ modes with one stone
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 34/60:
  -> Checking if provided link is pingable: https://doi.org/10.15607/RSS.2023.XIX.028
  -> INFO: Now checking 10 results for matching title: 'Goal-conditioned imitation learning using score-based diffusion policies'
       -> INFO: All authors matched!
- Checking reference 35/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=Pt5N3OG5wP
  -> INFO: Now checking 1 results for matching title: 'Roboagent: Generalization and efficiency in robot manipulation via semantic augmentations and action chunking'
       -> INFO: All authors matched!
- Checking reference 36/60:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2406.08234
  -> INFO: Now checking 10 results for matching title: 'Mail: Improving imitation learning with mamba.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Mail: Improving imitation learning with mamba.'
       -> INFO: All authors matched!
- Checking reference 37/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=8w0OJsTaFz
  -> INFO: Now checking 1 results for matching title: 'X-IL: Exploring the design space of imitation learning policies'
       -> INFO: All authors matched!
- Checking reference 38/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=AL1fq05o7H
  -> INFO: Now checking 10 results for matching title: 'Mamba: Linear-time sequence modeling with selective state spaces.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 158 results for matching title: 'Mamba: Linear-time sequence modeling with selective state spaces.'
  -> WARNING: None of the 158 results matched the expected title!
     -> You could also open https://openreview.net/forum?id=AL1fq05o7H manually and check the results.
        -> Author(s): Albert Gu and Tri Dao
        -> Title:     Mamba: Linear-time sequence modeling with selective state spaces.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 39/60:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=ARAxPPIAhq
  -> INFO: Now checking 10 results for matching title: 'xLSTM: Extended long short-term memory'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Poppel'
       -> INFO: All authors matched!
- Checking reference 40/60:
  -> INFO: Now checking 4 results for matching title: 'Learning fine-grained bimanual manipulation with low-cost hardware'
       -> INFO: All authors matched!
- Checking reference 41/60:
  -> INFO: Now checking 10 results for matching title: 'Goal conditioned imitation learning using score-based diffusion policies'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 4 results for matching title: 'Goal conditioned imitation learning using score-based diffusion policies'
  -> WARNING: None of the 4 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Goal+conditioned+imitation+learning+using+score-based+diffusion+policies manually and check the results.
        -> Author(s): Moritz Reuss, Maximilian Li, Xiaogang Jia, and Rudolf Lioutikov
        -> Title:     Goal conditioned imitation learning using score-based diffusion policies
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 42/60:
  -> INFO: Now checking 5 results for matching title: 'A connection between score matching and denoising autoencoders'
       -> INFO: All authors matched!
- Checking reference 43/60:
  -> INFO: Now checking 10 results for matching title: 'Denoising diffusion implicit models'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 44/60:
  -> INFO: Now checking 10 results for matching title: 'Learning transferable visual models from natural language supervision'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 45/60:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 3 results for matching title: 'Film: Visual reasoning with a general conditioning layer'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 46/60:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'Gr00t n1: An open foundation model for generalist humanoid robots'
       -> WARNING: Not all 42 authors from the found ref. were matched (only 15)
                   Unmatched authors = 'Nvidia, LinxiJimFan, Jang, Jiang, Kautz, Kundalia, Lao, Liu, Llontop, Magne, Mandlekar, Narayan, Nasiriany, Reed, Wang, Wang, Wang, Wang, Xiang, Xie, Xu, Xu, Zhang, Zhang, Zhao, Zheng, Zhu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 47/60:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Clover: Closedloop visual planning for long-horizon manipulation with diffusion policies
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Bu', 'Yang', 'Kumar', 'Mandt', 'Fox', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Clover:+Closedloop+visual+planning+for+long-horizon+manipulation+with+diffusion+policies manually and check the results.
        -> Author(s): Xinyang Bu, Fan Yang, Vikash Kumar, Stephan Mandt, and Dieter Fox
        -> Title:     Clover: Closedloop visual planning for long-horizon manipulation with diffusion policies
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 48/60:
  -> INFO: Now checking 10 results for matching title: 'Multimodal diffusion transformer: Learning versatile behavior from multimodal goals'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Yagmurlu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 49/60:
  -> INFO: Now checking 10 results for matching title: 'Seer: Pretraining vision-language-action models on robot play'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Zhou', 'Wu', 'Huang', 'Zhang', 'Ganapathi', 'Lu', 'Tenenbaum', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Seer:+Pretraining+vision-language-action+models+on+robot+play manually and check the results.
        -> Author(s): Yilun Zhou, Yufei Wu, De-An Huang, Yilun Zhang, Vivek Ganapathi, Yao Lu, and Josh Tenenbaum
        -> Title:     Seer: Pretraining vision-language-action models on robot play
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 50/60:
  -> INFO: Now checking 10 results for matching title: 'Vision-language foundation models as effective robot imitators'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Kong'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 51/60:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 3 results for matching title: 'Zero-shot skill composition with semantic feature fusion'
  -> WARNING: None of the 3 results matched the expected title!
  -> INFO: Now checking 999 results for matching title: 'Zero-shot skill composition with semantic feature fusion'
  -> WARNING: None of the 999 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Zero-shot+skill+composition+with+semantic+feature+fusion manually and check the results.
        -> Author(s): Andrew Black et al
        -> Title:     Zero-shot skill composition with semantic feature fusion
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 52/60:
  -> INFO: Now checking 10 results for matching title: 'Unleashing large-scale video generative pre-training for visual robot manipulation'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 53/60:
  -> INFO: Now checking 1 results for matching title: 'Towards synergistic, generalized, and efficient dual-system for robotic manipulation'
       -> INFO: All authors matched!
- Checking reference 54/60:
  -> INFO: Now checking 10 results for matching title: 'Grad-cam++: Generalized gradient-based visual explanations for deep convolutional networks'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Chattopadhyay'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 55/60:
  -> INFO: Now checking 10 results for matching title: 'What matters in language conditioned robotic imitation learning over long horizons'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Mees', 'Lodhi', 'Merk', 'Bukschat', 'Burgard', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=What+matters+in+language+conditioned+robotic+imitation+learning+over+long+horizons manually and check the results.
        -> Author(s): Oier Mees, Harsh Lodhi, Daniel Merk, Yannik Bukschat, and Wolfram Burgard
        -> Title:     What matters in language conditioned robotic imitation learning over long horizons
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 56/60:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Lad: Language as an abstraction for diffusion policy
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Zhang', 'Radosavovic', 'He', 'Yao', 'Misra', 'Pathak', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Lad:+Language+as+an+abstraction+for+diffusion+policy manually and check the results.
        -> Author(s): Shuang Zhang, Ilija Radosavovic, Kaiming He, Angel Yao, Dinesh Misra, and Deepak Pathak
        -> Title:     Lad: Language as an abstraction for diffusion policy
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 57/60:
  -> INFO: Now checking 10 results for matching title: 'Scaling vision-language models for robot learning with imitation transformers'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Ha', 'Mandlekar', 'Zeng', 'Chai', 'Liang', 'Li', 'Wang', 'Tian', 'Zeng', 'Xiao', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Scaling+vision-language+models+for+robot+learning+with+imitation+transformers manually and check the results.
        -> Author(s): Duy Ha, Ajay Mandlekar, Andy Zeng, Yunzhu Chai, Jacky Liang, Yao Li, Kelvin Wang, Yuan Tian, Xinyang Zeng, Tianhao Xiao, et al
        -> Title:     Scaling vision-language models for robot learning with imitation transformers
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 58/60:
  -> INFO: Now checking 1 results for matching title: 'Libero: Benchmarking knowledge transfer for language-instructed robotic manipulation'
  -> WARNING: None of the 1 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', 'Hoque', 'Zakka', 'Song', 'Florence', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Libero:+Benchmarking+knowledge+transfer+for+language-instructed+robotic+manipulation manually and check the results.
        -> Author(s): Zichen Liu, Rakibul Hoque, Kevin Zakka, Shuran Song, and Pete Florence
        -> Title:     Libero: Benchmarking knowledge transfer for language-instructed robotic manipulation
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 59/60:
  -> INFO: Now checking 1 results for matching title: 'Susie: Scaling up instruction-following policies for robot manipulation'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'Alwala', 'Ganapathi', 'Sharma', 'Chang', 'Zhang', 'Zhou', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Susie:+Scaling+up+instruction-following+policies+for+robot+manipulation manually and check the results.
        -> Author(s): Yufei Wu, Kiran Alwala, Vivek Ganapathi, Sudeep Sharma, Yilun Chang, Yicheng Zhang, Yilun Zhou, et al
        -> Title:     Susie: Scaling up instruction-following policies for robot manipulation
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 60/60:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Mode: Mixture of diffusion experts for long-horizon manipulation
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhou', 'Lin', 'Huang', 'Lu', 'Tenenbaum', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Mode:+Mixture+of+diffusion+experts+for+long-horizon+manipulation manually and check the results.
        -> Author(s): Yilun Zhou, Yen-Chen Lin, De-An Huang, Yao Lu, and Josh Tenenbaum
        -> Title:     Mode: Mixture of diffusion experts for long-horizon manipulation
        -> Year:      2024
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 3: βtσt −˙σt
-> Invalid unicode use found on p. 3: α(σt)|Dθ(¯a + ϵ, s, σt) −¯a|2
-> Invalid unicode use found on p. 3: Mt = ϕ(D, K−1
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 666 sentences on 10 pages -> Avg. of 75.0 sentences per page
-> Warning: Reference '55' never used in the document's text.
-> Warning: Reference '56' never used in the document's text.
-> Warning: Reference '57' never used in the document's text.
-> Warning: Reference '58' never used in the document's text.
-> Warning: Reference '59' never used in the document's text.
-> Warning: Reference '60' never used in the document's text.
---
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
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
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
-> Missing an abstract for reference with index 57 (Ref. ID = 58); Skipping LLM check...
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 17
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━  96% 0:00:01
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 18
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 19
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 20
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 21
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\44 PointMapPolicy Structured Point Cloud Processing\PAU_results.md
```