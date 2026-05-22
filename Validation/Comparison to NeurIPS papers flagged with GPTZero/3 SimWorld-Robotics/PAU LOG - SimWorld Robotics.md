
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\3 SimWorld-Robotics\SimWorld-Robotics Synthesizing Photorealistic and.pdf"
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
- Found following heading '3 - SimWorld-Robotics' on page 4
- Found following heading '4 - Multimodal Robot Navigation Benchmark' on page 6
- Found following heading '5 - Multi-Robot Search Benchmark' on page 9
- Found following heading '6 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - SimWorld-Robotics Details' on page 16
- Found following appendix 'B - Benchmark Comparison' on page 20
- Found following appendix 'C - SIMWORLD-MMNAV' on page 21
- Found following appendix 'D - SIMWORLD-MRS' on page 28
- Found following appendix 'E - Qualitative Examples' on page 31
- Found following appendix 'F - Code Availability Statement' on page 35
- Found following appendix 'G - LLM Usage Statement' on page 35
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 16
All found references: 63
-> Warning: Malformed author string: 'Others'
-> Warning: Malformed author string: 'Others'
-> Warning: Malformed author string: 'OpenAI'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                               link  valid
0       1  Peter Anderson, Angel Chang, Devendra Singh Ch...  ...  https://arxiv.org/abs/1807.06757.   None
1       2  Peter Anderson, Qi Wu, Damien Teney, Jake Bruc...  ...                                      None
2       3  Peter Anderson, Qi Wu, Damien Teney, Jake Bruc...  ...  https://arxiv.org/abs/1711.07280.   None
3       4  Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wan...  ...                                      None
4       5  Abhijat Biswas, Allan Wang, Gustavo Silvera, A...  ...  https://arxiv.org/abs/2103.00047.   None
..    ...                                                ...  ...                                ...    ...
58     59  Shengqiang Zhang, Philipp Wicke, LütﬁKerem ene...  ...  https://arxiv.org/abs/2310.12020.   None
59     60          Mandi Zhao, Shreeya Jain, and Shuran Song  ...                                      None
60     61  Fangwei Zhong, Kui Wu, Churan Wang, Hao Chen, ...  ...                                      None
61     62  Qinhong Zhou, Hongxin Zhang, Xiangye Lin, Zhey...  ...  https://arxiv.org/abs/2508.14893.   None
62     63  Yan Zhuang*, Jiawei Ren*, Xiaokang Ye*, Xuhong...  ...                                      None

[63 rows x 10 columns]
- Checking reference 1/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1807.06757.
  -> INFO: Now checking 10 results for matching title: 'On evaluation of embodied navigation agents.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'On evaluation of embodied navigation agents.'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 9)
                   Unmatched authors = '0001, 0001'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/63:
  -> INFO: Now checking 10 results for matching title: 'Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vision-and-language+navigation:+Interpreting+visuallygrounded+navigation+instructions+in+real+environments manually and check the results.
        -> Author(s): Peter Anderson, Qi Wu, Damien Teney, Jake Bruce, Mark Johnson, Niko Sünderhauf, Ian Reid, Stephen Gould, and Anton Van Den Hengel
        -> Title:     Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 3/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1711.07280.
  -> INFO: Now checking 10 results for matching title: 'Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments.'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vision-and-language+navigation:+Interpreting+visuallygrounded+navigation+instructions+in+real+environments. manually and check the results.
        -> Author(s): Peter Anderson, Qi Wu, Damien Teney, Jake Bruce, Mark Johnson, Niko Sünderhauf, Ian Reid, Stephen Gould, and Anton van den Hengel
        -> Title:     Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments.
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 4/63:
  -> INFO: Now checking 10 results for matching title: 'Qwen2'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Bai', 'Chen', 'Liu', 'Wang', 'Ge', 'Song', 'Dang', 'Wang', 'Wang', 'Tang', 'Zhong', 'Zhu', 'Yang', 'Li', 'Wan', 'Wang', 'Ding', 'Fu', 'Xu', 'Ye', 'Zhang', 'Xie', 'Cheng', 'Zhang', 'Yang', 'Xu', 'Lin', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Qwen2 manually and check the results.
        -> Author(s): Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang, Humen Zhong, Yuanzhi Zhu, Mingkun Yang, Zhaohai Li, Jianqiang Wan, Pengfei Wang, Wei Ding, Zheren Fu, Yiheng Xu, Jiabo Ye, Xi Zhang, Tianbao Xie, Zesen Cheng, Hang Zhang, Zhibo Yang, Haiyang Xu, and Junyang Lin
        -> Title:     Qwen2
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 5/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2103.00047.
  -> INFO: Now checking 1 results for matching title: 'Socnavbench: A grounded simulation testing framework for evaluating social navigation.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Biswas', 'Wang', 'Silvera', 'Steinfeld', 'Admoni', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Socnavbench:+A+grounded+simulation+testing+framework+for+evaluating+social+navigation. manually and check the results.
        -> Author(s): Abhijat Biswas, Allan Wang, Gustavo Silvera, Aaron Steinfeld, and Henny Admoni
        -> Title:     Socnavbench: A grounded simulation testing framework for evaluating social navigation.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 6/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1606.01540.
  -> INFO: Now checking 10 results for matching title: 'Openai gym.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Brockman', 'Cheung', 'Pettersson', 'Schneider', 'Schulman', 'Tang', 'Zaremba', '2016']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Openai+gym. manually and check the results.
        -> Author(s): Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schulman, Jie Tang, and Wojciech Zaremba
        -> Title:     Openai gym.
        -> Year:      2016
     -> Manual search was skipped by the user.
- Checking reference 7/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1709.06158.
  -> INFO: Now checking 10 results for matching title: 'Matterport3d: Learning from rgb-d data in indoor environments.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chang', 'Dai', 'Funkhouser', 'Halber', 'NieSSner', 'Savva', 'Song', 'Zeng', 'Zhang', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Matterport3d:+Learning+from+rgb-d+data+in+indoor+environments. manually and check the results.
        -> Author(s): Angel Chang, Angela Dai, Thomas Funkhouser, Maciej Halber, Matthias NieSSner, Manolis Savva, Shuran Song, Andy Zeng, and Yinda Zhang
        -> Title:     Matterport3d: Learning from rgb-d data in indoor environments.
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 8/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1811.12354.
  -> INFO: Now checking 5 results for matching title: 'Touchdown: Natural language navigation and spatial reasoning in visual street environments.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chen', 'Suhr', 'Misra', 'Snavely', 'Artzi', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Touchdown:+Natural+language+navigation+and+spatial+reasoning+in+visual+street+environments. manually and check the results.
        -> Author(s): Howard Chen, Alane Suhr, Dipendra Misra, Noah Snavely, and Yoav Artzi
        -> Title:     Touchdown: Natural language navigation and spatial reasoning in visual street environments.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 9/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2412.05271.
  -> INFO: Now checking 1 results for matching title: 'Expanding performance boundaries of opensource multimodal models with model, data, and test-time scaling.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chen', 'Wang', 'Cao', 'Liu', 'Gao', 'Cui', 'Zhu', 'Ye', 'Tian', 'Liu', 'Gu', 'Wang', 'Li', 'Ren', 'Chen', 'Luo', 'Wang', 'Jiang', 'Wang', 'He', 'Shi', 'Zhang', 'Lv', 'Wang', 'Shao', 'Chu', 'Tu', 'He', 'Wu', 'Deng', 'Ge', 'Chen', 'Zhang', 'Wang', 'Dou', 'Lu', 'Zhu', 'Lu', 'Lin', 'Qiao', 'Dai', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Expanding+performance+boundaries+of+opensource+multimodal+models+with+model%2C+data%2C+and+test-time+scaling. manually and check the results.
        -> Author(s): Zhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong Ye, Hao Tian, Zhaoyang Liu, Lixin Gu, Xuehui Wang, Qingyun Li, Yimin Ren, Zixuan Chen, Jiapeng Luo, Jiahao Wang, Tan Jiang, Bo Wang, Conghui He, Botian Shi, Xingcheng Zhang, Han Lv, Yi Wang, Wenqi Shao, Pei Chu, Zhongying Tu, Tong He, Zhiyong Wu, Huipeng Deng, Jiaye Ge, Kai Chen, Kaipeng Zhang, Limin Wang, Min Dou, Lewei Lu, Xizhou Zhu, Tong Lu, Dahua Lin, Yu Qiao, Jifeng Dai, and Wenhai Wang
        -> Title:     Expanding performance boundaries of opensource multimodal models with model, data, and test-time scaling.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 10/63:
  -> INFO: Now checking 10 results for matching title: 'Where are you? localization from embodied dialog'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Hahn, Krantz, Rehg, Anderson'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2004.06799.
  -> INFO: Now checking 1 results for matching title: 'Robothor: An open simulation-to-real embodied ai platform.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Deitke', 'Han', 'Herrasti', 'Kembhavi', 'Kolve', 'Mottaghi', 'Salvador', 'Schwenk', 'VanderBilt', 'Wallingford', 'Weihs', 'Yatskar', 'Farhadi', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Robothor:+An+open+simulation-to-real+embodied+ai+platform. manually and check the results.
        -> Author(s): Matt Deitke, Winson Han, Alvaro Herrasti, Aniruddha Kembhavi, Eric Kolve, Roozbeh Mottaghi, Jordi Salvador, Dustin Schwenk, Eli VanderBilt, Matthew Wallingford, Luca Weihs, Mark Yatskar, and Ali Farhadi
        -> Title:     Robothor: An open simulation-to-real embodied ai platform.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 12/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2305.14314.
  -> INFO: Now checking 10 results for matching title: 'Qlora: Efﬁcient ﬁnetuning of quantized llms.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Dettmers', 'Pagnoni', 'Holtzman', 'Zettlemoyer', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Qlora:+Efﬁcient+ﬁnetuning+of+quantized+llms. manually and check the results.
        -> Author(s): Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer
        -> Title:     Qlora: Efﬁcient ﬁnetuning of quantized llms.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 13/63:
  -> INFO: Now checking 10 results for matching title: 'CARLA: An open urban driving simulator'
       -> INFO: All authors matched!
- Checking reference 14/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2205.12219.
  -> INFO: Now checking 6 results for matching title: 'Aerial vision-and-dialog navigation.'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Fan', 'Chen', 'Jiang', 'Zhou', 'Zhang', 'Wang', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Aerial+vision-and-dialog+navigation. manually and check the results.
        -> Author(s): Yue Fan, Winson Chen, Tongzhou Jiang, Chun Zhou, Yi Zhang, and Xin Eric Wang
        -> Title:     Aerial vision-and-dialog navigation.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 15/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2007.04954.
  -> INFO: Now checking 2 results for matching title: 'Threedworld: A platform for interactive multi-modal physical simulation.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gan', 'Schwartz', 'Alter', 'Mrowca', 'Schrimpf', 'Traer', 'Freitas', 'Kubilius', 'Bhandwaldar', 'Haber', 'Sano', 'Kim', 'Wang', 'Lingelbach', 'Curtis', 'Feigelis', 'Bear', 'Gutfreund', 'Cox', 'Torralba', 'DiCarlo', 'Tenenbaum', 'McDermott', 'Yamins', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Threedworld:+A+platform+for+interactive+multi-modal+physical+simulation. manually and check the results.
        -> Author(s): Chuang Gan, Jeremy Schwartz, Seth Alter, Damian Mrowca, Martin Schrimpf, James Traer, Julian De Freitas, Jonas Kubilius, Abhishek Bhandwaldar, Nick Haber, Megumi Sano, Kuno Kim, Elias Wang, Michael Lingelbach, Aidan Curtis, Kevin Feigelis, Daniel M  Bear, Dan Gutfreund, David Cox, Antonio Torralba, James J  DiCarlo, Joshua B  Tenenbaum, Josh H  McDermott, and Daniel L  K  Yamins
        -> Title:     Threedworld: A platform for interactive multi-modal physical simulation.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 16/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2103.14025.
  -> INFO: Now checking 1 results for matching title: 'The threedworld transport challenge: A visually guided task-and-motion planning benchmark for physically realistic embodied ai.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gan', 'Zhou', 'Schwartz', 'Alter', 'Bhandwaldar', 'Gutfreund', 'Yamins', 'DiCarlo', 'McDermott', 'Torralba', 'Tenenbaum', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+threedworld+transport+challenge:+A+visually+guided+task-and-motion+planning+benchmark+for+physically+realistic+embodied+ai. manually and check the results.
        -> Author(s): Chuang Gan, Siyuan Zhou, Jeremy Schwartz, Seth Alter, Abhishek Bhandwaldar, Dan Gutfreund, Daniel L  K  Yamins, James J DiCarlo, Josh McDermott, Antonio Torralba, and Joshua B  Tenenbaum
        -> Title:     The threedworld transport challenge: A visually guided task-and-motion planning benchmark for physically realistic embodied ai.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 17/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2410.09604.
  -> INFO: Now checking 1 results for matching title: 'Embodiedcity: A benchmark platform for embodied agent in real-world city environment.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gao', 'Zhao', 'Zhang', 'Mao', 'Zhang', 'Zheng', 'Man', 'Fang', 'Zhou', 'Cui', 'Chen', 'Li', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Embodiedcity:+A+benchmark+platform+for+embodied+agent+in+real-world+city+environment. manually and check the results.
        -> Author(s): Chen Gao, Baining Zhao, Weichen Zhang, Jinzhu Mao, Jun Zhang, Zhiheng Zheng, Fanhang Man, Jianjie Fang, Zile Zhou, Jinqiang Cui, Xinlei Chen, and Yong Li
        -> Title:     Embodiedcity: A benchmark platform for embodied agent in real-world city environment.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 18/63:
  -> Checking if provided link is pingable: https://doi.org/10.1109/tssc.1968.300136.
  -> INFO: Now checking 3 results for matching title: 'A formal basis for the heuristic determination of minimum cost paths'
       -> INFO: All authors matched!
- Checking reference 19/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2111.09543.
  -> INFO: Now checking 1 results for matching title: 'Debertav3: Improving deberta using electrastyle pre-training with gradient-disentangled embedding sharing.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['He', 'Gao', 'Chen', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Debertav3:+Improving+deberta+using+electrastyle+pre-training+with+gradient-disentangled+embedding+sharing. manually and check the results.
        -> Author(s): Pengcheng He, Jianfeng Gao, and Weizhu Chen
        -> Title:     Debertav3: Improving deberta using electrastyle pre-training with gradient-disentangled embedding sharing.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 20/63:
  -> INFO: Now checking 1 results for matching title: 'A comprehensive survey of pid and pure pursuit control algorithms for autonomous vehicle navigation'
       -> INFO: All authors matched!
- Checking reference 21/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2210.03094.
  -> INFO: Now checking 10 results for matching title: 'Vima: General robot manipulation with multimodal prompts.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jiang', 'Gupta', 'Zhang', 'Wang', 'Dou', 'Chen', 'Fei-Fei', 'Anandkumar', 'Zhu', 'Fan', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vima:+General+robot+manipulation+with+multimodal+prompts. manually and check the results.
        -> Author(s): Yunfan Jiang, Agrim Gupta, Zichen Zhang, Guanzhi Wang, Yongqiang Dou, Yanjun Chen, Li Fei-Fei, Anima Anandkumar, Yuke Zhu, and Linxi Fan
        -> Title:     Vima: General robot manipulation with multimodal prompts.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 22/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1712.05474.
  -> INFO: Now checking 2 results for matching title: 'Ai2-thor: An interactive 3d environment for visual ai.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kolve', 'Mottaghi', 'Han', 'VanderBilt', 'Weihs', 'Herrasti', 'Deitke', 'Ehsani', 'Gordon', 'Zhu', 'Kembhavi', 'Gupta', 'Farhadi', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Ai2-thor:+An+interactive+3d+environment+for+visual+ai. manually and check the results.
        -> Author(s): Eric Kolve, Roozbeh Mottaghi, Winson Han, Eli VanderBilt, Luca Weihs, Alvaro Herrasti, Matt Deitke, Kiana Ehsani, Daniel Gordon, Yuke Zhu, Aniruddha Kembhavi, Abhinav Gupta, and Ali Farhadi
        -> Title:     Ai2-thor: An interactive 3d environment for visual ai.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 23/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2004.02857.
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Beyond the navgraph: Vision-and-language navigation in continuous environments.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Krantz', 'Wijmans', 'Majumdar', 'Batra', 'Lee', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Beyond+the+navgraph:+Vision-and-language+navigation+in+continuous+environments. manually and check the results.
        -> Author(s): Jacob Krantz, Erik Wijmans, Arjun Majumdar, Dhruv Batra, and Stefan Lee
        -> Title:     Beyond the navgraph: Vision-and-language navigation in continuous environments.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 24/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2406.00837.
  -> INFO: Now checking 10 results for matching title: 'Arena 3'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kästner', 'Shcherbyna', 'Zeng', 'Le', 'Schreff', 'Osmaev', 'Tran', 'Diaz', 'Golebiowski', 'Soh', 'Lambrecht', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Arena+3 manually and check the results.
        -> Author(s): Linh Kästner, Volodymyir Shcherbyna, Huajian Zeng, Tuan Anh Le, Maximilian Ho-Kyoung Schreff, Halid Osmaev, Nam Truong Tran, Diego Diaz, Jan Golebiowski, Harold Soh, and Jens Lambrecht
        -> Title:     Arena 3
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 25/63:
  -> INFO: Now checking 10 results for matching title: 'Drivlme: A large-scale multi-agent driving benchmark.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lastname', 'Others', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Drivlme:+A+large-scale+multi-agent+driving+benchmark. manually and check the results.
        -> Author(s): Firstname Lastname and Others
        -> Title:     Drivlme: A large-scale multi-agent driving benchmark.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 26/63:
  -> INFO: Now checking 4 results for matching title: 'Robotslang: Grounded natural language for multi-robot object search.'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lastname', 'Others', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Robotslang:+Grounded+natural+language+for+multi-robot+object+search. manually and check the results.
        -> Author(s): Firstname Lastname and Others
        -> Title:     Robotslang: Grounded natural language for multi-robot object search.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 27/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2108.03272.
  -> INFO: Now checking 10 results for matching title: 'igibson 2'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Li', 'Xia', 'Martín-Martín', 'Lingelbach', 'Srivastava', 'Shen', 'Vainio', 'Gokmen', 'Dharan', 'Jain', 'Kurenkov', 'Liu', 'Gweon', 'Wu', 'Fei-Fei', 'Savarese', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=igibson+2 manually and check the results.
        -> Author(s): Chengshu Li, Fei Xia, Roberto Martín-Martín, Michael Lingelbach, Sanjana Srivastava, Bokui Shen, Kent Vainio, Cem Gokmen, Gokul Dharan, Tanish Jain, Andrey Kurenkov, C  Karen Liu, Hyowon Gweon, Jiajun Wu, Li Fei-Fei, and Silvio Savarese
        -> Title:     igibson 2
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 28/63:
  -> Checking if provided link is pingable: https://proceedings.mlr.press/v205/li23a.html.
  -> INFO: Now checking 1 results for matching title: 'Behavior-1k: A benchmark for embodied ai with 1,000 everyday activities and realistic simulation'
       -> WARNING: Not all 28 authors from the found ref. were matched (only 27)
                   Unmatched authors = 'Martín-Martín'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/63:
  -> Checking if provided link is pingable: https://proceedings.neurips.cc/paper_files/paper/2024/file/d8087deaf34bb07ddd41c65f8a9fe9b5-Paper-Datasets_and_Benchmarks_Track.pdf.
  -> INFO: Now checking 2 results for matching title: 'Human-aware vision-andlanguage navigation: Bridging simulation to reality with dynamic human interactions'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Li', 'Li', 'Cheng', 'Dong', 'Zhou', 'He', 'Dai', 'Mitamura', 'Hauptmann', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Human-aware+vision-andlanguage+navigation:+Bridging+simulation+to+reality+with+dynamic+human+interactions manually and check the results.
        -> Author(s): Heng Li, Minghan Li, Zhi-Qi Cheng, Yifei Dong, Yuxuan Zhou, Jun-Yan He, Qi Dai, Teruko Mitamura, and Alexander G  Hauptmann
        -> Title:     Human-aware vision-andlanguage navigation: Bridging simulation to reality with dynamic human interactions
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 30/63:
  -> INFO: Now checking 1 results for matching title: 'Metadrive: Composing diverse driving scenarios for generalizable reinforcement learning'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 5)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2308.06735.
  -> INFO: Now checking 3 results for matching title: 'Aerialvln: Vision-and-language navigation for uavs.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', 'Zhang', 'Qi', 'Wang', 'Zhang', 'Wu', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Aerialvln:+Vision-and-language+navigation+for+uavs. manually and check the results.
        -> Author(s): Shubo Liu, Hongsheng Zhang, Yuankai Qi, Peng Wang, Yaning Zhang, and Qi Wu
        -> Title:     Aerialvln: Vision-and-language navigation for uavs.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 32/63:
  -> INFO: Now checking 10 results for matching title: 'Multi-agent actor-critic for mixed cooperative-competitive environments'
       -> INFO: All authors matched!
- Checking reference 33/63:
  -> INFO: Now checking 1 results for matching title: 'Dorothie: Spoken dialogue for handling unexpected situations in interactive autonomous driving agents.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ma', 'VanDerPloeg', 'Bara', 'Huang', 'Kim', 'Gervits', 'Marge', 'Chai', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dorothie:+Spoken+dialogue+for+handling+unexpected+situations+in+interactive+autonomous+driving+agents. manually and check the results.
        -> Author(s): Ziqiao Ma, Ben VanDerPloeg, Cristian-Paul Bara, Yidong Huang, Eui-In Kim, Felix Gervits, Matthew Marge, and Joyce Y  Chai
        -> Title:     Dorothie: Spoken dialogue for handling unexpected situations in interactive autonomous driving agents.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 34/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2112.03227.
  -> INFO: Now checking 7 results for matching title: 'Calvin: A benchmark for language-conditioned policy learning for long-horizon robot manipulation tasks.'
  -> WARNING: None of the 7 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Mees', 'Hermann', 'Rosete-Beas', 'Burgard', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Calvin:+A+benchmark+for+language-conditioned+policy+learning+for+long-horizon+robot+manipulation+tasks. manually and check the results.
        -> Author(s): Oier Mees, Lukas Hermann, Erick Rosete-Beas, and Wolfram Burgard
        -> Title:     Calvin: A benchmark for language-conditioned policy learning for long-horizon robot manipulation tasks.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 35/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2107.14483.
  -> INFO: Now checking 6 results for matching title: 'Maniskill: Generalizable manipulation skill benchmark with large-scale demonstrations.'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Mu', 'Ling', 'Xiang', 'Yang', 'Li', 'Tao', 'Huang', 'Jia', 'Su', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Maniskill:+Generalizable+manipulation+skill+benchmark+with+large-scale+demonstrations. manually and check the results.
        -> Author(s): Tongzhou Mu, Zhan Ling, Fanbo Xiang, Derek Yang, Xuanlin Li, Stone Tao, Zhiao Huang, Zhiwei Jia, and Hao Su
        -> Title:     Maniskill: Generalizable manipulation skill benchmark with large-scale demonstrations.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 36/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2410.21276.
  -> INFO: Now checking 10 results for matching title: 'Gpt-4o system card.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['OpenAI', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gpt-4o+system+card. manually and check the results.
        -> Author(s): OpenAI
        -> Title:     Gpt-4o system card.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 37/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2304.07193.
  -> INFO: Now checking 10 results for matching title: 'Dinov2: Learning robust visual features without supervision.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Oquab', 'Darcet', 'Moutakanni', 'Vo', 'Szafraniec', 'Khalidov', 'Fernandez', 'Haziza', 'Massa', 'El-Nouby', 'Assran', 'Ballas', 'Galuba', 'Howes', 'Huang', 'Li', 'Misra', 'Rabbat', 'Sharma', 'Synnaeve', 'Xu', 'Jegou', 'Mairal', 'Labatut', 'Joulin', 'Bojanowski', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dinov2:+Learning+robust+visual+features+without+supervision. manually and check the results.
        -> Author(s): Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, Mahmoud Assran, Nicolas Ballas, Wojciech Galuba, Russell Howes, Po-Yao Huang, Shang-Wen Li, Ishan Misra, Michael Rabbat, Vasu Sharma, Gabriel Synnaeve, Hu Xu, Hervé Jegou, Julien Mairal, Patrick Labatut, Armand Joulin, and Piotr Bojanowski
        -> Title:     Dinov2: Learning robust visual features without supervision.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 38/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1806.07011.
  -> INFO: Now checking 10 results for matching title: 'Virtualhome: Simulating household activities via programs.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Puig', 'Ra', 'Boben', 'Li', 'Wang', 'Fidler', 'Torralba', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Virtualhome:+Simulating+household+activities+via+programs. manually and check the results.
        -> Author(s): Xavier Puig, Kevin Ra, Marko Boben, Jiaman Li, Tingwu Wang, Sanja Fidler, and Antonio Torralba
        -> Title:     Virtualhome: Simulating household activities via programs.
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 39/63:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Watch-and-help: A challenge for social perception and humanai collaboration
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Puig', 'Shu', 'Li', 'Wang', 'Liao', 'Tenenbaum', 'Fidler', 'Torralba', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Watch-and-help:+A+challenge+for+social+perception+and+humanai+collaboration manually and check the results.
        -> Author(s): Xavier Puig, Tianmin Shu, Shuang Li, Zilin Wang, Yuan-Hong Liao, Joshua B Tenenbaum, Sanja Fidler, and Antonio Torralba
        -> Title:     Watch-and-help: A challenge for social perception and humanai collaboration
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 40/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2310.13724.
  -> INFO: Now checking 10 results for matching title: 'Habitat 3'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Puig', 'Undersander', 'Szot', 'Cote', 'Yang', 'Partsey', 'Desai', 'Clegg', 'Hlavac', 'Min', 'Vondru', 'Gervet', 'Berges', 'Turner', 'Maksymets', 'Kira', 'Kalakrishnan', 'Malik', 'Chaplot', 'Jain', 'Batra', 'Rai', 'Mottaghi', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Habitat+3 manually and check the results.
        -> Author(s): Xavier Puig, Eric Undersander, Andrew Szot, Mikael Dallaire Cote, Tsung-Yen Yang, Ruslan Partsey, Ruta Desai, Alexander William Clegg, Michal Hlavac, So Yeon Min, Vladimír Vondru, Theophile Gervet, Vincent-Pierre Berges, John M  Turner, Oleksandr Maksymets, Zsolt Kira, Mrinal Kalakrishnan, Jitendra Malik, Devendra Singh Chaplot, Unnat Jain, Dhruv Batra, Akshara Rai, and Roozbeh Mottaghi
        -> Title:     Habitat 3
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 41/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2010.08600.
  -> INFO: Now checking 10 results for matching title: 'Robot navigation in constrained pedestrian environments using reinforcement learning.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ["Pérez-D'Arpino", 'Liu', 'Goebel', 'Martín-Martín', 'Savarese', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Robot+navigation+in+constrained+pedestrian+environments+using+reinforcement+learning. manually and check the results.
        -> Author(s): Claudia Pérez-D'Arpino, Can Liu, Patrick Goebel, Roberto Martín-Martín, and Silvio Savarese
        -> Title:     Robot navigation in constrained pedestrian environments using reinforcement learning.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 42/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1904.10151.
  -> INFO: Now checking 7 results for matching title: 'Reverie: Remote embodied visual referring expression in real indoor environments.'
  -> WARNING: None of the 7 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Qi', 'Wu', 'Anderson', 'Wang', 'Wang', 'Shen', 'Hengel', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Reverie:+Remote+embodied+visual+referring+expression+in+real+indoor+environments. manually and check the results.
        -> Author(s): Yuankai Qi, Qi Wu, Peter Anderson, Xin Wang, William Yang Wang, Chunhua Shen, and Anton van den Hengel
        -> Title:     Reverie: Remote embodied visual referring expression in real indoor environments.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 43/63:
  -> Checking if provided link is pingable: https://doi.org/10.1145/3123266.3129396.
  -> INFO: Now checking 10 results for matching title: 'Unrealcv: Virtual worlds for computer vision'
       -> INFO: All authors matched!
- Checking reference 44/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1705.05065.
  -> INFO: Now checking 1 results for matching title: 'Airsim: High-ﬁdelity visual and physical simulation for autonomous vehicles.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Shah', 'Dey', 'Lovett', 'Kapoor', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Airsim:+High-ﬁdelity+visual+and+physical+simulation+for+autonomous+vehicles. manually and check the results.
        -> Author(s): Shital Shah, Debadeepta Dey, Chris Lovett, and Ashish Kapoor
        -> Title:     Airsim: High-ﬁdelity visual and physical simulation for autonomous vehicles.
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 45/63:
  -> INFO: Now checking 1 results for matching title: 'Alfred: A benchmark for interpreting grounded instructions for everyday tasks'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 46/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2108.03332.
  -> INFO: Now checking 2 results for matching title: 'Behavior: Benchmark for everyday household activities in virtual, interactive, and ecological environments.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Srivastava', 'Li', 'Lingelbach', 'Martín-Martín', 'Xia', 'Vainio', 'Lian', 'Gokmen', 'Buch', 'Liu', 'Savarese', 'Gweon', 'Wu', 'Fei-Fei', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Behavior:+Benchmark+for+everyday+household+activities+in+virtual%2C+interactive%2C+and+ecological+environments. manually and check the results.
        -> Author(s): Sanjana Srivastava, Chengshu Li, Michael Lingelbach, Roberto Martín-Martín, Fei Xia, Kent Vainio, Zheng Lian, Cem Gokmen, Shyamal Buch, C  Karen Liu, Silvio Savarese, Hyowon Gweon, Jiajun Wu, and Li Fei-Fei
        -> Title:     Behavior: Benchmark for everyday household activities in virtual, interactive, and ecological environments.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 47/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2106.14405.
  -> INFO: Now checking 10 results for matching title: 'Habitat 2'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Szot', 'Clegg', 'Undersander', 'Wijmans', 'Zhao', 'Turner', 'Maestre', 'Mukadam', 'Chaplot', 'Maksymets', 'Gokaslan', 'Vondrus', 'Dharur', 'Meier', 'Galuba', 'Chang', 'Kira', 'Koltun', 'Malik', 'Savva', 'Batra', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Habitat+2 manually and check the results.
        -> Author(s): Andrew Szot, Alex Clegg, Eric Undersander, Erik Wijmans, Yili Zhao, John Turner, Noah Maestre, Mustafa Mukadam, Devendra Chaplot, Oleksandr Maksymets, Aaron Gokaslan, Vladimir Vondrus, Sameer Dharur, Franziska Meier, Wojciech Galuba, Angel Chang, Zsolt Kira, Vladlen Koltun, Jitendra Malik, Manolis Savva, and Dhruv Batra
        -> Title:     Habitat 2
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 48/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2312.11805.
  -> INFO: Now checking 8 results for matching title: 'Gemini: A family of highly capable multimodal models.'
  -> WARNING: None of the 8 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gemini:+A+family+of+highly+capable+multimodal+models. manually and check the results.
        -> Author(s): Gemini Team
        -> Title:     Gemini: A family of highly capable multimodal models.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 49/63:
  -> Checking if provided link is pingable: https://goo.gle/Gemma3Report.
  -> INFO: Now checking 10 results for matching title: 'Gemma 3'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://goo.gle/Gemma3Report. manually and check the results.
        -> Author(s): Gemma Team
        -> Title:     Gemma 3
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 50/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1907.04957.
  -> INFO: Now checking 10 results for matching title: 'Vision-and-dialog navigation.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Thomason', 'Murray', 'Cakmak', 'Zettlemoyer', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vision-and-dialog+navigation. manually and check the results.
        -> Author(s): Jesse Thomason, Michael Murray, Maya Cakmak, and Luke Zettlemoyer
        -> Title:     Vision-and-dialog navigation.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 51/63:
  -> INFO: Now checking 10 results for matching title: 'Sean 2'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tsoi', 'Xiang', 'Yu', 'Sohn', 'Schwartz', 'Ramesh', 'Hussein', 'Gupta', 'Kapadia', 'Vázquez', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Sean+2 manually and check the results.
        -> Author(s): Nathan Tsoi, Alec Xiang, Peter Yu, Samuel S  Sohn, Greg Schwartz, Subashri Ramesh, Mohamed Hussein, Anjali W  Gupta, Mubbasir Kapadia, and Marynel Vázquez
        -> Title:     Sean 2
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 52/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2407.10943.
  -> INFO: Now checking 1 results for matching title: 'Grutopia: Dream general robots in a city at scale.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Chen', 'Huang', 'Ben', 'Wang', 'Mi', 'Huang', 'Zhao', 'Chen', 'Yang', 'Cao', 'Yu', 'Ye', 'Li', 'Long', 'Wang', 'Wang', 'Zhao', 'Tu', 'Qiao', 'Lin', 'Pang', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Grutopia:+Dream+general+robots+in+a+city+at+scale. manually and check the results.
        -> Author(s): Hanqing Wang, Jiahe Chen, Wensi Huang, Qingwei Ben, Tai Wang, Boyu Mi, Tao Huang, Siheng Zhao, Yilun Chen, Sizhe Yang, Peizhou Cao, Wenye Yu, Zichao Ye, Jialun Li, Junfeng Long, Zirui Wang, Huiling Wang, Ying Zhao, Zhongying Tu, Yu Qiao, Dahua Lin, and Jiangmiao Pang
        -> Title:     Grutopia: Dream general robots in a city at scale.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 53/63:
  -> INFO: Now checking 1 results for matching title: 'Qwen2-vl: Enhancing vision-language model’s perception of the world at any resolution'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Dang, Du, Ren, Men, Zhou, Zhou'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/63:
  -> Checking if provided link is pingable: http://www.jstor.org/stable/2276774.
  -> INFO: Now checking 1 results for matching title: 'Probable inference, the law of succession, and statistical inference'
       -> INFO: All authors matched!
- Checking reference 55/63:
  -> INFO: Now checking 1 results for matching title: 'Metaurban: An embodied ai simulation platform for urban micromobility.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'He', 'He', 'Wang', 'Duan', 'Liu', 'Li', 'Zhou', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Metaurban:+An+embodied+ai+simulation+platform+for+urban+micromobility. manually and check the results.
        -> Author(s): Wayne Wu, Honglin He, Jack He, Yiran Wang, Chenda Duan, Zhizheng Liu, Quanyi Li, and Bolei Zhou
        -> Title:     Metaurban: An embodied ai simulation platform for urban micromobility.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 56/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2407.08725.
  -> INFO: Now checking 1 results for matching title: 'Metaurban: An embodied ai simulation platform for urban micromobility.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'He', 'He', 'Wang', 'Duan', 'Liu', 'Li', 'Zhou', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Metaurban:+An+embodied+ai+simulation+platform+for+urban+micromobility. manually and check the results.
        -> Author(s): Wayne Wu, Honglin He, Jack He, Yiran Wang, Chenda Duan, Zhizheng Liu, Quanyi Li, and Bolei Zhou
        -> Title:     Metaurban: An embodied ai simulation platform for urban micromobility.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 57/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2210.03629.
  -> INFO: Now checking 3 results for matching title: 'React: Synergizing reasoning and acting in language models.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yao', 'Zhao', 'Yu', 'Du', 'Shafran', 'Narasimhan', 'Cao', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=React:+Synergizing+reasoning+and+acting+in+language+models. manually and check the results.
        -> Author(s): Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao
        -> Title:     React: Synergizing reasoning and acting in language models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 58/63:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=Kb4fDvJBlj.
  -> INFO: Now checking 2 results for matching title: 'Partinstruct: Part-level instruction following for ﬁne-grained robot manipulation'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yin', 'Han', 'Aarya', 'Xu', 'Wang', 'Peng', 'Wang', 'Yuille', 'Shu', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://openreview.net/forum?id=Kb4fDvJBlj. manually and check the results.
        -> Author(s): Yifan Yin, Zhengtao Han, Shivam Aarya, Shuhang Xu, Jianxin Wang, Jiawei Peng, Angtian Wang, Alan Yuille, and Tianmin Shu
        -> Title:     Partinstruct: Part-level instruction following for ﬁne-grained robot manipulation
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 59/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2310.12020.
  -> INFO: Now checking 1 results for matching title: 'Lohoravens: A long-horizon languageconditioned benchmark for robotic tabletop manipulation.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Wicke', 'enel', 'Figueredo', 'Naceri', 'Haddadin', 'Plank', 'Schütze', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Lohoravens:+A+long-horizon+languageconditioned+benchmark+for+robotic+tabletop+manipulation. manually and check the results.
        -> Author(s): Shengqiang Zhang, Philipp Wicke, LütﬁKerem enel, Luis Figueredo, Abdeldjallil Naceri, Sami Haddadin, Barbara Plank, and Hinrich Schütze
        -> Title:     Lohoravens: A long-horizon languageconditioned benchmark for robotic tabletop manipulation.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 60/63:
  -> INFO: Now checking 5 results for matching title: 'Roco: Dialectic multi-robot collaboration with large language models.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhao', 'Jain', 'Song', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Roco:+Dialectic+multi-robot+collaboration+with+large+language+models. manually and check the results.
        -> Author(s): Mandi Zhao, Shreeya Jain, and Shuran Song
        -> Title:     Roco: Dialectic multi-robot collaboration with large language models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 61/63:
  -> INFO: Now checking 2 results for matching title: 'Unrealzoo: Enriching photo-realistic virtual worlds for embodied ai'
       -> INFO: All authors matched!
- Checking reference 62/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2508.14893.
  -> INFO: Now checking 3 results for matching title: 'Virtual community: An open world for humans, robots, and society.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhou', 'Zhang', 'Lin', 'Zhang', 'Chen', 'Liu', 'Zhang', 'Chen', 'Fang', 'Lyu', 'Sun', 'Yang', 'Wang', 'Dang', 'Chen', 'Ladia', 'Liu', 'Gan', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Virtual+community:+An+open+world+for+humans%2C+robots%2C+and+society. manually and check the results.
        -> Author(s): Qinhong Zhou, Hongxin Zhang, Xiangye Lin, Zheyuan Zhang, Yutian Chen, Wenjun Liu, Zunzhe Zhang, Sunli Chen, Lixing Fang, Qiushi Lyu, Xinyu Sun, Jincheng Yang, Zeyuan Wang, Bao Chi Dang, Zhehuan Chen, Daksha Ladia, Jiageng Liu, and Chuang Gan
        -> Title:     Virtual community: An open world for humans, robots, and society.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 63/63:
  -> INFO: Now checking 1 results for matching title: 'Simworld: An open-ended realistic simulator for autonomous agents in physical and social worlds.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhuang*', 'Ren*', 'Ye*', 'He', 'Gao', 'Wu', 'Dogra', 'Zhang', 'Kim', 'Wolﬁnger', 'Ma', 'Shu†', 'Hu†', 'Qin†', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Simworld:+An+open-ended+realistic+simulator+for+autonomous+agents+in+physical+and+social+worlds. manually and check the results.
        -> Author(s): Yan Zhuang*, Jiawei Ren*, Xiaokang Ye*, Xuhong He, Zijun Gao, Ryan Wu, Mrinaal Dogra, Cassie Zhang, Kai Kim, Bertt Wolﬁnger, Ziqiao Ma, Tianmin Shu†, Zhiting Hu†, and Lianhui Qin†
        -> Title:     Simworld: An open-ended realistic simulator for autonomous agents in physical and social worlds.
        -> Year:      2025
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 20: forward, move backward, move left, move right, turn left (−90◦), turn right (+90◦), or stay still.
-> Invalid unicode use found on p. 21: (d0 −dT
-> Invalid unicode use found on p. 21: 5 for i ←2 to k −1 do
-> Invalid unicode use found on p. 21: if θi ̸= θi−1 then
-> Invalid unicode use found on p. 21: Vmove ←capture visual cue at ni−1 with orientation θi−1;
-> Invalid unicode use found on p. 21: Imove ←generate Move Along the Road instruction using a landmark near ni−1;
-> Invalid unicode use found on p. 21: θi−1 and θi;
-> Invalid unicode use found on p. 28: (D0 −DT
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 416 sentences on 11 pages -> Avg. of 42.6 sentences per page
Backend tkagg is interactive backend. Turning interactive mode on.
-> Warning: Reference '5' never used in the document's text.
-> Warning: Reference '6' never used in the document's text.
-> Warning: Reference '12' never used in the document's text.
-> Warning: Reference '24' never used in the document's text.
-> Warning: Reference '42' never used in the document's text.
-> Warning: Reference '43' never used in the document's text.
-> Warning: Reference '54' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
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
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
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
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
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
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 5
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━  89% 0:00:01
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 6
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 7
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 8
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━━━━━━━━  73% 0:00:01
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 9
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
###############################
# Starting Author Check
###############################
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\3 SimWorld-Robotics\PAU_results.md
```

---

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\3 SimWorld-Robotics\SimWorld-Robotics Synthesizing Photorealistic and.pdf"
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
- Found following heading '3 - SimWorld-Robotics' on page 4
- Found following heading '4 - Multimodal Robot Navigation Benchmark' on page 6
- Found following heading '5 - Multi-Robot Search Benchmark' on page 9
- Found following heading '6 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - SimWorld-Robotics Details' on page 16
- Found following appendix 'B - Benchmark Comparison' on page 20
- Found following appendix 'C - SIMWORLD-MMNAV' on page 21
- Found following appendix 'D - SIMWORLD-MRS' on page 28
- Found following appendix 'E - Qualitative Examples' on page 31
- Found following appendix 'F - Code Availability Statement' on page 35
- Found following appendix 'G - LLM Usage Statement' on page 35
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 16
All found references: 63
-> Warning: Malformed author string: 'Others'
-> Warning: Malformed author string: 'Others'
-> Warning: Malformed author string: 'OpenAI'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                               link  valid
0       1  Peter Anderson, Angel Chang, Devendra Singh Ch...  ...  https://arxiv.org/abs/1807.06757.   None
1       2  Peter Anderson, Qi Wu, Damien Teney, Jake Bruc...  ...                                      None
2       3  Peter Anderson, Qi Wu, Damien Teney, Jake Bruc...  ...  https://arxiv.org/abs/1711.07280.   None
3       4  Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wan...  ...                                      None
4       5  Abhijat Biswas, Allan Wang, Gustavo Silvera, A...  ...  https://arxiv.org/abs/2103.00047.   None
..    ...                                                ...  ...                                ...    ...
58     59  Shengqiang Zhang, Philipp Wicke, LütﬁKerem ene...  ...  https://arxiv.org/abs/2310.12020.   None
59     60          Mandi Zhao, Shreeya Jain, and Shuran Song  ...                                      None
60     61  Fangwei Zhong, Kui Wu, Churan Wang, Hao Chen, ...  ...                                      None
61     62  Qinhong Zhou, Hongxin Zhang, Xiangye Lin, Zhey...  ...  https://arxiv.org/abs/2508.14893.   None
62     63  Yan Zhuang*, Jiawei Ren*, Xiaokang Ye*, Xuhong...  ...                                      None

[63 rows x 10 columns]
- Checking reference 1/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1807.06757.
  -> INFO: Now checking 10 results for matching title: 'On evaluation of embodied navigation agents.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'On evaluation of embodied navigation agents.'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 9)
                   Unmatched authors = '0001, 0001'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/63:
  -> INFO: Now checking 10 results for matching title: 'Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vision-and-language+navigation:+Interpreting+visuallygrounded+navigation+instructions+in+real+environments manually and check the results.
        -> Author(s): Peter Anderson, Qi Wu, Damien Teney, Jake Bruce, Mark Johnson, Niko Sünderhauf, Ian Reid, Stephen Gould, and Anton Van Den Hengel
        -> Title:     Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 3/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1711.07280.
  -> INFO: Now checking 10 results for matching title: 'Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments.'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vision-and-language+navigation:+Interpreting+visuallygrounded+navigation+instructions+in+real+environments. manually and check the results.
        -> Author(s): Peter Anderson, Qi Wu, Damien Teney, Jake Bruce, Mark Johnson, Niko Sünderhauf, Ian Reid, Stephen Gould, and Anton van den Hengel
        -> Title:     Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments.
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 4/63:
  -> INFO: Now checking 10 results for matching title: 'Qwen2'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Bai', 'Chen', 'Liu', 'Wang', 'Ge', 'Song', 'Dang', 'Wang', 'Wang', 'Tang', 'Zhong', 'Zhu', 'Yang', 'Li', 'Wan', 'Wang', 'Ding', 'Fu', 'Xu', 'Ye', 'Zhang', 'Xie', 'Cheng', 'Zhang', 'Yang', 'Xu', 'Lin', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Qwen2 manually and check the results.
        -> Author(s): Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang, Humen Zhong, Yuanzhi Zhu, Mingkun Yang, Zhaohai Li, Jianqiang Wan, Pengfei Wang, Wei Ding, Zheren Fu, Yiheng Xu, Jiabo Ye, Xi Zhang, Tianbao Xie, Zesen Cheng, Hang Zhang, Zhibo Yang, Haiyang Xu, and Junyang Lin
        -> Title:     Qwen2
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 5/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2103.00047.
  -> INFO: Now checking 1 results for matching title: 'Socnavbench: A grounded simulation testing framework for evaluating social navigation.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Biswas', 'Wang', 'Silvera', 'Steinfeld', 'Admoni', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Socnavbench:+A+grounded+simulation+testing+framework+for+evaluating+social+navigation. manually and check the results.
        -> Author(s): Abhijat Biswas, Allan Wang, Gustavo Silvera, Aaron Steinfeld, and Henny Admoni
        -> Title:     Socnavbench: A grounded simulation testing framework for evaluating social navigation.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 6/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1606.01540.
  -> INFO: Now checking 10 results for matching title: 'Openai gym.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Brockman', 'Cheung', 'Pettersson', 'Schneider', 'Schulman', 'Tang', 'Zaremba', '2016']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Openai+gym. manually and check the results.
        -> Author(s): Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schulman, Jie Tang, and Wojciech Zaremba
        -> Title:     Openai gym.
        -> Year:      2016
     -> Manual search was skipped by the user.
- Checking reference 7/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1709.06158.
  -> INFO: Now checking 10 results for matching title: 'Matterport3d: Learning from rgb-d data in indoor environments.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chang', 'Dai', 'Funkhouser', 'Halber', 'NieSSner', 'Savva', 'Song', 'Zeng', 'Zhang', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Matterport3d:+Learning+from+rgb-d+data+in+indoor+environments. manually and check the results.
        -> Author(s): Angel Chang, Angela Dai, Thomas Funkhouser, Maciej Halber, Matthias NieSSner, Manolis Savva, Shuran Song, Andy Zeng, and Yinda Zhang
        -> Title:     Matterport3d: Learning from rgb-d data in indoor environments.
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 8/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1811.12354.
  -> INFO: Now checking 5 results for matching title: 'Touchdown: Natural language navigation and spatial reasoning in visual street environments.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chen', 'Suhr', 'Misra', 'Snavely', 'Artzi', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Touchdown:+Natural+language+navigation+and+spatial+reasoning+in+visual+street+environments. manually and check the results.
        -> Author(s): Howard Chen, Alane Suhr, Dipendra Misra, Noah Snavely, and Yoav Artzi
        -> Title:     Touchdown: Natural language navigation and spatial reasoning in visual street environments.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 9/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2412.05271.
  -> INFO: Now checking 1 results for matching title: 'Expanding performance boundaries of opensource multimodal models with model, data, and test-time scaling.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chen', 'Wang', 'Cao', 'Liu', 'Gao', 'Cui', 'Zhu', 'Ye', 'Tian', 'Liu', 'Gu', 'Wang', 'Li', 'Ren', 'Chen', 'Luo', 'Wang', 'Jiang', 'Wang', 'He', 'Shi', 'Zhang', 'Lv', 'Wang', 'Shao', 'Chu', 'Tu', 'He', 'Wu', 'Deng', 'Ge', 'Chen', 'Zhang', 'Wang', 'Dou', 'Lu', 'Zhu', 'Lu', 'Lin', 'Qiao', 'Dai', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Expanding+performance+boundaries+of+opensource+multimodal+models+with+model%2C+data%2C+and+test-time+scaling. manually and check the results.
        -> Author(s): Zhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong Ye, Hao Tian, Zhaoyang Liu, Lixin Gu, Xuehui Wang, Qingyun Li, Yimin Ren, Zixuan Chen, Jiapeng Luo, Jiahao Wang, Tan Jiang, Bo Wang, Conghui He, Botian Shi, Xingcheng Zhang, Han Lv, Yi Wang, Wenqi Shao, Pei Chu, Zhongying Tu, Tong He, Zhiyong Wu, Huipeng Deng, Jiaye Ge, Kai Chen, Kaipeng Zhang, Limin Wang, Min Dou, Lewei Lu, Xizhou Zhu, Tong Lu, Dahua Lin, Yu Qiao, Jifeng Dai, and Wenhai Wang
        -> Title:     Expanding performance boundaries of opensource multimodal models with model, data, and test-time scaling.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 10/63:
  -> INFO: Now checking 10 results for matching title: 'Where are you? localization from embodied dialog'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Hahn, Krantz, Rehg, Anderson'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2004.06799.
  -> INFO: Now checking 1 results for matching title: 'Robothor: An open simulation-to-real embodied ai platform.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Deitke', 'Han', 'Herrasti', 'Kembhavi', 'Kolve', 'Mottaghi', 'Salvador', 'Schwenk', 'VanderBilt', 'Wallingford', 'Weihs', 'Yatskar', 'Farhadi', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Robothor:+An+open+simulation-to-real+embodied+ai+platform. manually and check the results.
        -> Author(s): Matt Deitke, Winson Han, Alvaro Herrasti, Aniruddha Kembhavi, Eric Kolve, Roozbeh Mottaghi, Jordi Salvador, Dustin Schwenk, Eli VanderBilt, Matthew Wallingford, Luca Weihs, Mark Yatskar, and Ali Farhadi
        -> Title:     Robothor: An open simulation-to-real embodied ai platform.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 12/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2305.14314.
  -> INFO: Now checking 10 results for matching title: 'Qlora: Efﬁcient ﬁnetuning of quantized llms.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Dettmers', 'Pagnoni', 'Holtzman', 'Zettlemoyer', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Qlora:+Efﬁcient+ﬁnetuning+of+quantized+llms. manually and check the results.
        -> Author(s): Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer
        -> Title:     Qlora: Efﬁcient ﬁnetuning of quantized llms.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 13/63:
  -> INFO: Now checking 10 results for matching title: 'CARLA: An open urban driving simulator'
       -> INFO: All authors matched!
- Checking reference 14/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2205.12219.
  -> INFO: Now checking 6 results for matching title: 'Aerial vision-and-dialog navigation.'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Fan', 'Chen', 'Jiang', 'Zhou', 'Zhang', 'Wang', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Aerial+vision-and-dialog+navigation. manually and check the results.
        -> Author(s): Yue Fan, Winson Chen, Tongzhou Jiang, Chun Zhou, Yi Zhang, and Xin Eric Wang
        -> Title:     Aerial vision-and-dialog navigation.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 15/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2007.04954.
  -> INFO: Now checking 2 results for matching title: 'Threedworld: A platform for interactive multi-modal physical simulation.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gan', 'Schwartz', 'Alter', 'Mrowca', 'Schrimpf', 'Traer', 'Freitas', 'Kubilius', 'Bhandwaldar', 'Haber', 'Sano', 'Kim', 'Wang', 'Lingelbach', 'Curtis', 'Feigelis', 'Bear', 'Gutfreund', 'Cox', 'Torralba', 'DiCarlo', 'Tenenbaum', 'McDermott', 'Yamins', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Threedworld:+A+platform+for+interactive+multi-modal+physical+simulation. manually and check the results.
        -> Author(s): Chuang Gan, Jeremy Schwartz, Seth Alter, Damian Mrowca, Martin Schrimpf, James Traer, Julian De Freitas, Jonas Kubilius, Abhishek Bhandwaldar, Nick Haber, Megumi Sano, Kuno Kim, Elias Wang, Michael Lingelbach, Aidan Curtis, Kevin Feigelis, Daniel M  Bear, Dan Gutfreund, David Cox, Antonio Torralba, James J  DiCarlo, Joshua B  Tenenbaum, Josh H  McDermott, and Daniel L  K  Yamins
        -> Title:     Threedworld: A platform for interactive multi-modal physical simulation.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 16/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2103.14025.
  -> INFO: Now checking 1 results for matching title: 'The threedworld transport challenge: A visually guided task-and-motion planning benchmark for physically realistic embodied ai.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gan', 'Zhou', 'Schwartz', 'Alter', 'Bhandwaldar', 'Gutfreund', 'Yamins', 'DiCarlo', 'McDermott', 'Torralba', 'Tenenbaum', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+threedworld+transport+challenge:+A+visually+guided+task-and-motion+planning+benchmark+for+physically+realistic+embodied+ai. manually and check the results.
        -> Author(s): Chuang Gan, Siyuan Zhou, Jeremy Schwartz, Seth Alter, Abhishek Bhandwaldar, Dan Gutfreund, Daniel L  K  Yamins, James J DiCarlo, Josh McDermott, Antonio Torralba, and Joshua B  Tenenbaum
        -> Title:     The threedworld transport challenge: A visually guided task-and-motion planning benchmark for physically realistic embodied ai.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 17/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2410.09604.
  -> INFO: Now checking 1 results for matching title: 'Embodiedcity: A benchmark platform for embodied agent in real-world city environment.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gao', 'Zhao', 'Zhang', 'Mao', 'Zhang', 'Zheng', 'Man', 'Fang', 'Zhou', 'Cui', 'Chen', 'Li', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Embodiedcity:+A+benchmark+platform+for+embodied+agent+in+real-world+city+environment. manually and check the results.
        -> Author(s): Chen Gao, Baining Zhao, Weichen Zhang, Jinzhu Mao, Jun Zhang, Zhiheng Zheng, Fanhang Man, Jianjie Fang, Zile Zhou, Jinqiang Cui, Xinlei Chen, and Yong Li
        -> Title:     Embodiedcity: A benchmark platform for embodied agent in real-world city environment.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 18/63:
  -> Checking if provided link is pingable: https://doi.org/10.1109/tssc.1968.300136.
  -> INFO: Now checking 3 results for matching title: 'A formal basis for the heuristic determination of minimum cost paths'
       -> INFO: All authors matched!
- Checking reference 19/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2111.09543.
  -> INFO: Now checking 1 results for matching title: 'Debertav3: Improving deberta using electrastyle pre-training with gradient-disentangled embedding sharing.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['He', 'Gao', 'Chen', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Debertav3:+Improving+deberta+using+electrastyle+pre-training+with+gradient-disentangled+embedding+sharing. manually and check the results.
        -> Author(s): Pengcheng He, Jianfeng Gao, and Weizhu Chen
        -> Title:     Debertav3: Improving deberta using electrastyle pre-training with gradient-disentangled embedding sharing.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 20/63:
  -> INFO: Now checking 1 results for matching title: 'A comprehensive survey of pid and pure pursuit control algorithms for autonomous vehicle navigation'
       -> INFO: All authors matched!
- Checking reference 21/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2210.03094.
  -> INFO: Now checking 10 results for matching title: 'Vima: General robot manipulation with multimodal prompts.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jiang', 'Gupta', 'Zhang', 'Wang', 'Dou', 'Chen', 'Fei-Fei', 'Anandkumar', 'Zhu', 'Fan', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vima:+General+robot+manipulation+with+multimodal+prompts. manually and check the results.
        -> Author(s): Yunfan Jiang, Agrim Gupta, Zichen Zhang, Guanzhi Wang, Yongqiang Dou, Yanjun Chen, Li Fei-Fei, Anima Anandkumar, Yuke Zhu, and Linxi Fan
        -> Title:     Vima: General robot manipulation with multimodal prompts.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 22/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1712.05474.
  -> INFO: Now checking 2 results for matching title: 'Ai2-thor: An interactive 3d environment for visual ai.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kolve', 'Mottaghi', 'Han', 'VanderBilt', 'Weihs', 'Herrasti', 'Deitke', 'Ehsani', 'Gordon', 'Zhu', 'Kembhavi', 'Gupta', 'Farhadi', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Ai2-thor:+An+interactive+3d+environment+for+visual+ai. manually and check the results.
        -> Author(s): Eric Kolve, Roozbeh Mottaghi, Winson Han, Eli VanderBilt, Luca Weihs, Alvaro Herrasti, Matt Deitke, Kiana Ehsani, Daniel Gordon, Yuke Zhu, Aniruddha Kembhavi, Abhinav Gupta, and Ali Farhadi
        -> Title:     Ai2-thor: An interactive 3d environment for visual ai.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 23/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2004.02857.
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Beyond the navgraph: Vision-and-language navigation in continuous environments.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Krantz', 'Wijmans', 'Majumdar', 'Batra', 'Lee', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Beyond+the+navgraph:+Vision-and-language+navigation+in+continuous+environments. manually and check the results.
        -> Author(s): Jacob Krantz, Erik Wijmans, Arjun Majumdar, Dhruv Batra, and Stefan Lee
        -> Title:     Beyond the navgraph: Vision-and-language navigation in continuous environments.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 24/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2406.00837.
  -> INFO: Now checking 10 results for matching title: 'Arena 3'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kästner', 'Shcherbyna', 'Zeng', 'Le', 'Schreff', 'Osmaev', 'Tran', 'Diaz', 'Golebiowski', 'Soh', 'Lambrecht', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Arena+3 manually and check the results.
        -> Author(s): Linh Kästner, Volodymyir Shcherbyna, Huajian Zeng, Tuan Anh Le, Maximilian Ho-Kyoung Schreff, Halid Osmaev, Nam Truong Tran, Diego Diaz, Jan Golebiowski, Harold Soh, and Jens Lambrecht
        -> Title:     Arena 3
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 25/63:
  -> INFO: Now checking 10 results for matching title: 'Drivlme: A large-scale multi-agent driving benchmark.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lastname', 'Others', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Drivlme:+A+large-scale+multi-agent+driving+benchmark. manually and check the results.
        -> Author(s): Firstname Lastname and Others
        -> Title:     Drivlme: A large-scale multi-agent driving benchmark.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 26/63:
  -> INFO: Now checking 4 results for matching title: 'Robotslang: Grounded natural language for multi-robot object search.'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lastname', 'Others', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Robotslang:+Grounded+natural+language+for+multi-robot+object+search. manually and check the results.
        -> Author(s): Firstname Lastname and Others
        -> Title:     Robotslang: Grounded natural language for multi-robot object search.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 27/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2108.03272.
  -> INFO: Now checking 10 results for matching title: 'igibson 2'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Li', 'Xia', 'Martín-Martín', 'Lingelbach', 'Srivastava', 'Shen', 'Vainio', 'Gokmen', 'Dharan', 'Jain', 'Kurenkov', 'Liu', 'Gweon', 'Wu', 'Fei-Fei', 'Savarese', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=igibson+2 manually and check the results.
        -> Author(s): Chengshu Li, Fei Xia, Roberto Martín-Martín, Michael Lingelbach, Sanjana Srivastava, Bokui Shen, Kent Vainio, Cem Gokmen, Gokul Dharan, Tanish Jain, Andrey Kurenkov, C  Karen Liu, Hyowon Gweon, Jiajun Wu, Li Fei-Fei, and Silvio Savarese
        -> Title:     igibson 2
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 28/63:
  -> Checking if provided link is pingable: https://proceedings.mlr.press/v205/li23a.html.
  -> INFO: Now checking 1 results for matching title: 'Behavior-1k: A benchmark for embodied ai with 1,000 everyday activities and realistic simulation'
       -> WARNING: Not all 28 authors from the found ref. were matched (only 27)
                   Unmatched authors = 'Martín-Martín'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/63:
  -> Checking if provided link is pingable: https://proceedings.neurips.cc/paper_files/paper/2024/file/d8087deaf34bb07ddd41c65f8a9fe9b5-Paper-Datasets_and_Benchmarks_Track.pdf.
  -> INFO: Now checking 2 results for matching title: 'Human-aware vision-andlanguage navigation: Bridging simulation to reality with dynamic human interactions'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Li', 'Li', 'Cheng', 'Dong', 'Zhou', 'He', 'Dai', 'Mitamura', 'Hauptmann', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Human-aware+vision-andlanguage+navigation:+Bridging+simulation+to+reality+with+dynamic+human+interactions manually and check the results.
        -> Author(s): Heng Li, Minghan Li, Zhi-Qi Cheng, Yifei Dong, Yuxuan Zhou, Jun-Yan He, Qi Dai, Teruko Mitamura, and Alexander G  Hauptmann
        -> Title:     Human-aware vision-andlanguage navigation: Bridging simulation to reality with dynamic human interactions
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 30/63:
  -> INFO: Now checking 1 results for matching title: 'Metadrive: Composing diverse driving scenarios for generalizable reinforcement learning'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 5)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2308.06735.
  -> INFO: Now checking 3 results for matching title: 'Aerialvln: Vision-and-language navigation for uavs.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', 'Zhang', 'Qi', 'Wang', 'Zhang', 'Wu', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Aerialvln:+Vision-and-language+navigation+for+uavs. manually and check the results.
        -> Author(s): Shubo Liu, Hongsheng Zhang, Yuankai Qi, Peng Wang, Yaning Zhang, and Qi Wu
        -> Title:     Aerialvln: Vision-and-language navigation for uavs.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 32/63:
  -> INFO: Now checking 10 results for matching title: 'Multi-agent actor-critic for mixed cooperative-competitive environments'
       -> INFO: All authors matched!
- Checking reference 33/63:
  -> INFO: Now checking 1 results for matching title: 'Dorothie: Spoken dialogue for handling unexpected situations in interactive autonomous driving agents.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ma', 'VanDerPloeg', 'Bara', 'Huang', 'Kim', 'Gervits', 'Marge', 'Chai', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dorothie:+Spoken+dialogue+for+handling+unexpected+situations+in+interactive+autonomous+driving+agents. manually and check the results.
        -> Author(s): Ziqiao Ma, Ben VanDerPloeg, Cristian-Paul Bara, Yidong Huang, Eui-In Kim, Felix Gervits, Matthew Marge, and Joyce Y  Chai
        -> Title:     Dorothie: Spoken dialogue for handling unexpected situations in interactive autonomous driving agents.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 34/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2112.03227.
  -> INFO: Now checking 7 results for matching title: 'Calvin: A benchmark for language-conditioned policy learning for long-horizon robot manipulation tasks.'
  -> WARNING: None of the 7 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Mees', 'Hermann', 'Rosete-Beas', 'Burgard', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Calvin:+A+benchmark+for+language-conditioned+policy+learning+for+long-horizon+robot+manipulation+tasks. manually and check the results.
        -> Author(s): Oier Mees, Lukas Hermann, Erick Rosete-Beas, and Wolfram Burgard
        -> Title:     Calvin: A benchmark for language-conditioned policy learning for long-horizon robot manipulation tasks.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 35/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2107.14483.
  -> INFO: Now checking 6 results for matching title: 'Maniskill: Generalizable manipulation skill benchmark with large-scale demonstrations.'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Mu', 'Ling', 'Xiang', 'Yang', 'Li', 'Tao', 'Huang', 'Jia', 'Su', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Maniskill:+Generalizable+manipulation+skill+benchmark+with+large-scale+demonstrations. manually and check the results.
        -> Author(s): Tongzhou Mu, Zhan Ling, Fanbo Xiang, Derek Yang, Xuanlin Li, Stone Tao, Zhiao Huang, Zhiwei Jia, and Hao Su
        -> Title:     Maniskill: Generalizable manipulation skill benchmark with large-scale demonstrations.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 36/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2410.21276.
  -> INFO: Now checking 10 results for matching title: 'Gpt-4o system card.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['OpenAI', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gpt-4o+system+card. manually and check the results.
        -> Author(s): OpenAI
        -> Title:     Gpt-4o system card.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 37/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2304.07193.
  -> INFO: Now checking 10 results for matching title: 'Dinov2: Learning robust visual features without supervision.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Oquab', 'Darcet', 'Moutakanni', 'Vo', 'Szafraniec', 'Khalidov', 'Fernandez', 'Haziza', 'Massa', 'El-Nouby', 'Assran', 'Ballas', 'Galuba', 'Howes', 'Huang', 'Li', 'Misra', 'Rabbat', 'Sharma', 'Synnaeve', 'Xu', 'Jegou', 'Mairal', 'Labatut', 'Joulin', 'Bojanowski', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dinov2:+Learning+robust+visual+features+without+supervision. manually and check the results.
        -> Author(s): Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, Mahmoud Assran, Nicolas Ballas, Wojciech Galuba, Russell Howes, Po-Yao Huang, Shang-Wen Li, Ishan Misra, Michael Rabbat, Vasu Sharma, Gabriel Synnaeve, Hu Xu, Hervé Jegou, Julien Mairal, Patrick Labatut, Armand Joulin, and Piotr Bojanowski
        -> Title:     Dinov2: Learning robust visual features without supervision.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 38/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1806.07011.
  -> INFO: Now checking 10 results for matching title: 'Virtualhome: Simulating household activities via programs.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Puig', 'Ra', 'Boben', 'Li', 'Wang', 'Fidler', 'Torralba', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Virtualhome:+Simulating+household+activities+via+programs. manually and check the results.
        -> Author(s): Xavier Puig, Kevin Ra, Marko Boben, Jiaman Li, Tingwu Wang, Sanja Fidler, and Antonio Torralba
        -> Title:     Virtualhome: Simulating household activities via programs.
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 39/63:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Watch-and-help: A challenge for social perception and humanai collaboration
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Puig', 'Shu', 'Li', 'Wang', 'Liao', 'Tenenbaum', 'Fidler', 'Torralba', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Watch-and-help:+A+challenge+for+social+perception+and+humanai+collaboration manually and check the results.
        -> Author(s): Xavier Puig, Tianmin Shu, Shuang Li, Zilin Wang, Yuan-Hong Liao, Joshua B Tenenbaum, Sanja Fidler, and Antonio Torralba
        -> Title:     Watch-and-help: A challenge for social perception and humanai collaboration
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 40/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2310.13724.
  -> INFO: Now checking 10 results for matching title: 'Habitat 3'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Puig', 'Undersander', 'Szot', 'Cote', 'Yang', 'Partsey', 'Desai', 'Clegg', 'Hlavac', 'Min', 'Vondru', 'Gervet', 'Berges', 'Turner', 'Maksymets', 'Kira', 'Kalakrishnan', 'Malik', 'Chaplot', 'Jain', 'Batra', 'Rai', 'Mottaghi', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Habitat+3 manually and check the results.
        -> Author(s): Xavier Puig, Eric Undersander, Andrew Szot, Mikael Dallaire Cote, Tsung-Yen Yang, Ruslan Partsey, Ruta Desai, Alexander William Clegg, Michal Hlavac, So Yeon Min, Vladimír Vondru, Theophile Gervet, Vincent-Pierre Berges, John M  Turner, Oleksandr Maksymets, Zsolt Kira, Mrinal Kalakrishnan, Jitendra Malik, Devendra Singh Chaplot, Unnat Jain, Dhruv Batra, Akshara Rai, and Roozbeh Mottaghi
        -> Title:     Habitat 3
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 41/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2010.08600.
  -> INFO: Now checking 10 results for matching title: 'Robot navigation in constrained pedestrian environments using reinforcement learning.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ["Pérez-D'Arpino", 'Liu', 'Goebel', 'Martín-Martín', 'Savarese', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Robot+navigation+in+constrained+pedestrian+environments+using+reinforcement+learning. manually and check the results.
        -> Author(s): Claudia Pérez-D'Arpino, Can Liu, Patrick Goebel, Roberto Martín-Martín, and Silvio Savarese
        -> Title:     Robot navigation in constrained pedestrian environments using reinforcement learning.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 42/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1904.10151.
  -> INFO: Now checking 7 results for matching title: 'Reverie: Remote embodied visual referring expression in real indoor environments.'
  -> WARNING: None of the 7 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Qi', 'Wu', 'Anderson', 'Wang', 'Wang', 'Shen', 'Hengel', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Reverie:+Remote+embodied+visual+referring+expression+in+real+indoor+environments. manually and check the results.
        -> Author(s): Yuankai Qi, Qi Wu, Peter Anderson, Xin Wang, William Yang Wang, Chunhua Shen, and Anton van den Hengel
        -> Title:     Reverie: Remote embodied visual referring expression in real indoor environments.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 43/63:
  -> Checking if provided link is pingable: https://doi.org/10.1145/3123266.3129396.
  -> INFO: Now checking 10 results for matching title: 'Unrealcv: Virtual worlds for computer vision'
       -> INFO: All authors matched!
- Checking reference 44/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1705.05065.
  -> INFO: Now checking 1 results for matching title: 'Airsim: High-ﬁdelity visual and physical simulation for autonomous vehicles.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Shah', 'Dey', 'Lovett', 'Kapoor', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Airsim:+High-ﬁdelity+visual+and+physical+simulation+for+autonomous+vehicles. manually and check the results.
        -> Author(s): Shital Shah, Debadeepta Dey, Chris Lovett, and Ashish Kapoor
        -> Title:     Airsim: High-ﬁdelity visual and physical simulation for autonomous vehicles.
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 45/63:
  -> INFO: Now checking 1 results for matching title: 'Alfred: A benchmark for interpreting grounded instructions for everyday tasks'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 46/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2108.03332.
  -> INFO: Now checking 2 results for matching title: 'Behavior: Benchmark for everyday household activities in virtual, interactive, and ecological environments.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Srivastava', 'Li', 'Lingelbach', 'Martín-Martín', 'Xia', 'Vainio', 'Lian', 'Gokmen', 'Buch', 'Liu', 'Savarese', 'Gweon', 'Wu', 'Fei-Fei', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Behavior:+Benchmark+for+everyday+household+activities+in+virtual%2C+interactive%2C+and+ecological+environments. manually and check the results.
        -> Author(s): Sanjana Srivastava, Chengshu Li, Michael Lingelbach, Roberto Martín-Martín, Fei Xia, Kent Vainio, Zheng Lian, Cem Gokmen, Shyamal Buch, C  Karen Liu, Silvio Savarese, Hyowon Gweon, Jiajun Wu, and Li Fei-Fei
        -> Title:     Behavior: Benchmark for everyday household activities in virtual, interactive, and ecological environments.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 47/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2106.14405.
  -> INFO: Now checking 10 results for matching title: 'Habitat 2'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Szot', 'Clegg', 'Undersander', 'Wijmans', 'Zhao', 'Turner', 'Maestre', 'Mukadam', 'Chaplot', 'Maksymets', 'Gokaslan', 'Vondrus', 'Dharur', 'Meier', 'Galuba', 'Chang', 'Kira', 'Koltun', 'Malik', 'Savva', 'Batra', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Habitat+2 manually and check the results.
        -> Author(s): Andrew Szot, Alex Clegg, Eric Undersander, Erik Wijmans, Yili Zhao, John Turner, Noah Maestre, Mustafa Mukadam, Devendra Chaplot, Oleksandr Maksymets, Aaron Gokaslan, Vladimir Vondrus, Sameer Dharur, Franziska Meier, Wojciech Galuba, Angel Chang, Zsolt Kira, Vladlen Koltun, Jitendra Malik, Manolis Savva, and Dhruv Batra
        -> Title:     Habitat 2
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 48/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2312.11805.
  -> INFO: Now checking 8 results for matching title: 'Gemini: A family of highly capable multimodal models.'
  -> WARNING: None of the 8 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gemini:+A+family+of+highly+capable+multimodal+models. manually and check the results.
        -> Author(s): Gemini Team
        -> Title:     Gemini: A family of highly capable multimodal models.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 49/63:
  -> Checking if provided link is pingable: https://goo.gle/Gemma3Report.
  -> INFO: Now checking 10 results for matching title: 'Gemma 3'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://goo.gle/Gemma3Report. manually and check the results.
        -> Author(s): Gemma Team
        -> Title:     Gemma 3
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 50/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1907.04957.
  -> INFO: Now checking 10 results for matching title: 'Vision-and-dialog navigation.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Thomason', 'Murray', 'Cakmak', 'Zettlemoyer', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vision-and-dialog+navigation. manually and check the results.
        -> Author(s): Jesse Thomason, Michael Murray, Maya Cakmak, and Luke Zettlemoyer
        -> Title:     Vision-and-dialog navigation.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 51/63:
  -> INFO: Now checking 10 results for matching title: 'Sean 2'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tsoi', 'Xiang', 'Yu', 'Sohn', 'Schwartz', 'Ramesh', 'Hussein', 'Gupta', 'Kapadia', 'Vázquez', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Sean+2 manually and check the results.
        -> Author(s): Nathan Tsoi, Alec Xiang, Peter Yu, Samuel S  Sohn, Greg Schwartz, Subashri Ramesh, Mohamed Hussein, Anjali W  Gupta, Mubbasir Kapadia, and Marynel Vázquez
        -> Title:     Sean 2
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 52/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2407.10943.
  -> INFO: Now checking 1 results for matching title: 'Grutopia: Dream general robots in a city at scale.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Chen', 'Huang', 'Ben', 'Wang', 'Mi', 'Huang', 'Zhao', 'Chen', 'Yang', 'Cao', 'Yu', 'Ye', 'Li', 'Long', 'Wang', 'Wang', 'Zhao', 'Tu', 'Qiao', 'Lin', 'Pang', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Grutopia:+Dream+general+robots+in+a+city+at+scale. manually and check the results.
        -> Author(s): Hanqing Wang, Jiahe Chen, Wensi Huang, Qingwei Ben, Tai Wang, Boyu Mi, Tao Huang, Siheng Zhao, Yilun Chen, Sizhe Yang, Peizhou Cao, Wenye Yu, Zichao Ye, Jialun Li, Junfeng Long, Zirui Wang, Huiling Wang, Ying Zhao, Zhongying Tu, Yu Qiao, Dahua Lin, and Jiangmiao Pang
        -> Title:     Grutopia: Dream general robots in a city at scale.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 53/63:
  -> INFO: Now checking 1 results for matching title: 'Qwen2-vl: Enhancing vision-language model’s perception of the world at any resolution'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Dang, Du, Ren, Men, Zhou, Zhou'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/63:
  -> Checking if provided link is pingable: http://www.jstor.org/stable/2276774.
  -> INFO: Now checking 1 results for matching title: 'Probable inference, the law of succession, and statistical inference'
       -> INFO: All authors matched!
- Checking reference 55/63:
  -> INFO: Now checking 1 results for matching title: 'Metaurban: An embodied ai simulation platform for urban micromobility.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'He', 'He', 'Wang', 'Duan', 'Liu', 'Li', 'Zhou', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Metaurban:+An+embodied+ai+simulation+platform+for+urban+micromobility. manually and check the results.
        -> Author(s): Wayne Wu, Honglin He, Jack He, Yiran Wang, Chenda Duan, Zhizheng Liu, Quanyi Li, and Bolei Zhou
        -> Title:     Metaurban: An embodied ai simulation platform for urban micromobility.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 56/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2407.08725.
  -> INFO: Now checking 1 results for matching title: 'Metaurban: An embodied ai simulation platform for urban micromobility.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'He', 'He', 'Wang', 'Duan', 'Liu', 'Li', 'Zhou', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Metaurban:+An+embodied+ai+simulation+platform+for+urban+micromobility. manually and check the results.
        -> Author(s): Wayne Wu, Honglin He, Jack He, Yiran Wang, Chenda Duan, Zhizheng Liu, Quanyi Li, and Bolei Zhou
        -> Title:     Metaurban: An embodied ai simulation platform for urban micromobility.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 57/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2210.03629.
  -> INFO: Now checking 3 results for matching title: 'React: Synergizing reasoning and acting in language models.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yao', 'Zhao', 'Yu', 'Du', 'Shafran', 'Narasimhan', 'Cao', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=React:+Synergizing+reasoning+and+acting+in+language+models. manually and check the results.
        -> Author(s): Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao
        -> Title:     React: Synergizing reasoning and acting in language models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 58/63:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=Kb4fDvJBlj.
  -> INFO: Now checking 2 results for matching title: 'Partinstruct: Part-level instruction following for ﬁne-grained robot manipulation'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yin', 'Han', 'Aarya', 'Xu', 'Wang', 'Peng', 'Wang', 'Yuille', 'Shu', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://openreview.net/forum?id=Kb4fDvJBlj. manually and check the results.
        -> Author(s): Yifan Yin, Zhengtao Han, Shivam Aarya, Shuhang Xu, Jianxin Wang, Jiawei Peng, Angtian Wang, Alan Yuille, and Tianmin Shu
        -> Title:     Partinstruct: Part-level instruction following for ﬁne-grained robot manipulation
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 59/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2310.12020.
  -> INFO: Now checking 1 results for matching title: 'Lohoravens: A long-horizon languageconditioned benchmark for robotic tabletop manipulation.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Wicke', 'enel', 'Figueredo', 'Naceri', 'Haddadin', 'Plank', 'Schütze', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Lohoravens:+A+long-horizon+languageconditioned+benchmark+for+robotic+tabletop+manipulation. manually and check the results.
        -> Author(s): Shengqiang Zhang, Philipp Wicke, LütﬁKerem enel, Luis Figueredo, Abdeldjallil Naceri, Sami Haddadin, Barbara Plank, and Hinrich Schütze
        -> Title:     Lohoravens: A long-horizon languageconditioned benchmark for robotic tabletop manipulation.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 60/63:
  -> INFO: Now checking 5 results for matching title: 'Roco: Dialectic multi-robot collaboration with large language models.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhao', 'Jain', 'Song', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Roco:+Dialectic+multi-robot+collaboration+with+large+language+models. manually and check the results.
        -> Author(s): Mandi Zhao, Shreeya Jain, and Shuran Song
        -> Title:     Roco: Dialectic multi-robot collaboration with large language models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 61/63:
  -> INFO: Now checking 2 results for matching title: 'Unrealzoo: Enriching photo-realistic virtual worlds for embodied ai'
       -> INFO: All authors matched!
- Checking reference 62/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2508.14893.
  -> INFO: Now checking 3 results for matching title: 'Virtual community: An open world for humans, robots, and society.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhou', 'Zhang', 'Lin', 'Zhang', 'Chen', 'Liu', 'Zhang', 'Chen', 'Fang', 'Lyu', 'Sun', 'Yang', 'Wang', 'Dang', 'Chen', 'Ladia', 'Liu', 'Gan', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Virtual+community:+An+open+world+for+humans%2C+robots%2C+and+society. manually and check the results.
        -> Author(s): Qinhong Zhou, Hongxin Zhang, Xiangye Lin, Zheyuan Zhang, Yutian Chen, Wenjun Liu, Zunzhe Zhang, Sunli Chen, Lixing Fang, Qiushi Lyu, Xinyu Sun, Jincheng Yang, Zeyuan Wang, Bao Chi Dang, Zhehuan Chen, Daksha Ladia, Jiageng Liu, and Chuang Gan
        -> Title:     Virtual community: An open world for humans, robots, and society.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 63/63:
  -> INFO: Now checking 1 results for matching title: 'Simworld: An open-ended realistic simulator for autonomous agents in physical and social worlds.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhuang*', 'Ren*', 'Ye*', 'He', 'Gao', 'Wu', 'Dogra', 'Zhang', 'Kim', 'Wolﬁnger', 'Ma', 'Shu†', 'Hu†', 'Qin†', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Simworld:+An+open-ended+realistic+simulator+for+autonomous+agents+in+physical+and+social+worlds. manually and check the results.
        -> Author(s): Yan Zhuang*, Jiawei Ren*, Xiaokang Ye*, Xuhong He, Zijun Gao, Ryan Wu, Mrinaal Dogra, Cassie Zhang, Kai Kim, Bertt Wolﬁnger, Ziqiao Ma, Tianmin Shu†, Zhiting Hu†, and Lianhui Qin†
        -> Title:     Simworld: An open-ended realistic simulator for autonomous agents in physical and social worlds.
        -> Year:      2025
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 20: forward, move backward, move left, move right, turn left (−90◦), turn right (+90◦), or stay still.
-> Invalid unicode use found on p. 21: (d0 −dT
-> Invalid unicode use found on p. 21: 5 for i ←2 to k −1 do
-> Invalid unicode use found on p. 21: if θi ̸= θi−1 then
-> Invalid unicode use found on p. 21: Vmove ←capture visual cue at ni−1 with orientation θi−1;
-> Invalid unicode use found on p. 21: Imove ←generate Move Along the Road instruction using a landmark near ni−1;
-> Invalid unicode use found on p. 21: θi−1 and θi;
-> Invalid unicode use found on p. 28: (D0 −DT
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
```

---

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\3 SimWorld-Robotics\SimWorld-Robotics Synthesizing Photorealistic and.pdf"
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
- Found following heading '3 - SimWorld-Robotics' on page 4
- Found following heading '4 - Multimodal Robot Navigation Benchmark' on page 6
- Found following heading '5 - Multi-Robot Search Benchmark' on page 9
- Found following heading '6 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - SimWorld-Robotics Details' on page 16
- Found following appendix 'B - Benchmark Comparison' on page 20
- Found following appendix 'C - SIMWORLD-MMNAV' on page 21
- Found following appendix 'D - SIMWORLD-MRS' on page 28
- Found following appendix 'E - Qualitative Examples' on page 31
- Found following appendix 'F - Code Availability Statement' on page 35
- Found following appendix 'G - LLM Usage Statement' on page 35
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 16
All found references: 63
-> Warning: Malformed author string: 'Others'
-> Warning: Malformed author string: 'Others'
-> Warning: Malformed author string: 'OpenAI'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors                                 normalized_authors  contains_et_al  ... abstract                                             outlet                               link valid
0       1  Peter Anderson, Angel Chang, Devendra Singh Ch...  [Anderson P., Chang A., Chaplot D., Dosovitski...           False  ...     None                                                     https://arxiv.org/abs/1807.06757.  None
1       2  Peter Anderson, Qi Wu, Damien Teney, Jake Bruc...  [Anderson P., Wu Q., Teney D., Bruce J., Johns...           False  ...     None  Proceedings of the IEEE conference on computer...                                     None
2       3  Peter Anderson, Qi Wu, Damien Teney, Jake Bruc...  [Anderson P., Wu Q., Teney D., Bruce J., Johns...           False  ...     None                                                     https://arxiv.org/abs/1711.07280.  None
3       4  Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wan...  [Bai S., Chen K., Liu X., Wang J., Ge W., Song...           False  ...     None  5-vl technical report.  arXiv preprint arXiv:2...                                     None
4       5  Abhijat Biswas, Allan Wang, Gustavo Silvera, A...  [Biswas A., Wang A., Silvera G., Steinfeld A.,...           False  ...     None                                                     https://arxiv.org/abs/2103.00047.  None
..    ...                                                ...                                                ...             ...  ...      ...                                                ...                                ...   ...
58     59  Shengqiang Zhang, Philipp Wicke, LütﬁKerem ene...  [Zhang S., Wicke P., enel L., Figueredo L., Na...           False  ...     None                                                     https://arxiv.org/abs/2310.12020.  None
59     60          Mandi Zhao, Shreeya Jain, and Shuran Song                        [Zhao M., Jain S., Song S.]           False  ...     None                                                                                        None
60     61  Fangwei Zhong, Kui Wu, Churan Wang, Hao Chen, ...  [Zhong F., Wu K., Wang C., Chen H., Ci H., Li ...           False  ...     None                   arXiv preprint arXiv:2412. 20977                                     None
61     62  Qinhong Zhou, Hongxin Zhang, Xiangye Lin, Zhey...  [Zhou Q., Zhang H., Lin X., Zhang Z., Chen Y.,...           False  ...     None                                                     https://arxiv.org/abs/2508.14893.  None
62     63  Yan Zhuang*, Jiawei Ren*, Xiaokang Ye*, Xuhong...  [Zhuang* Y., Ren* J., Ye* X., He X., Gao Z., W...           False  ...     None                                                                                        None

[63 rows x 10 columns]
- Checking reference 1/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1807.06757.
  -> INFO: Now checking 10 results for matching title: 'On evaluation of embodied navigation agents.'
       -> INFO: All authors matched!
- Checking reference 2/63:
  -> INFO: Now checking 10 results for matching title: 'Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Dong, Chen, Yu, Feng, Li'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wang, Li, Hu, Yao, Liu, Chen'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yakolli, Gautam, Das, Shekhawat'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Shi, Li, Lyu, Xia, Dayoub, Qiao'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lin, Nie, Wei, Chen, Han, Xu, Chang, Liang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1711.07280.
  -> INFO: Now checking 10 results for matching title: 'Vision-and-language navigation: Interpreting visuallygrounded navigation instructions in real environments.'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Dong, Chen, Yu, Feng, Li'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wang, Li, Hu, Yao, Liu, Chen'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yakolli, Gautam, Das, Shekhawat'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Shi, Li, Lyu, Xia, Dayoub, Qiao'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lin, Nie, Wei, Chen, Han, Xu, Chang, Liang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/63:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Qwen2'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 14)
                   Unmatched authors = 'Fan, Fan, Du, Zhou, Zhou'
       -> WARNING: Not all 58 authors from the found ref. were matched (only 40)
                   Unmatched authors = 'Hui, Zheng, Zhou, Huang, Dong, Tu, Ma, Zhou, Lu, Ni, Gao, Deng, Zhou, Fan, Yao, Chu, Cui, Fan'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Guo, Fan, Chu'
       -> WARNING: Not all 16 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Hui, Gao, Tu, Zhou, Lu'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 6)
                   Unmatched authors = 'Chu, Guo, Leng, Lv, Zhou, Zhou'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Du, Noto'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 5)
                   Unmatched authors = ''
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Qu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 5/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2103.00047.
  -> INFO: Now checking 1 results for matching title: 'Socnavbench: A grounded simulation testing framework for evaluating social navigation.'
       -> INFO: All authors matched!
- Checking reference 6/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1606.01540.
  -> INFO: Now checking 10 results for matching title: 'Openai gym.'
       -> INFO: All authors matched!
- Checking reference 7/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1709.06158.
  -> INFO: Now checking 10 results for matching title: 'Matterport3d: Learning from rgb-d data in indoor environments.'
       -> INFO: All authors matched!
- Checking reference 8/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1811.12354.
  -> INFO: Now checking 5 results for matching title: 'Touchdown: Natural language navigation and spatial reasoning in visual street environments.'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2020)!
       -> WARNING: Not all 1 authors from the found ref. were matched (only 1)
                   Unmatched authors = ''
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Mei, Yang, Guo, Wang, Yu, Wu, Liu'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Mei, Yang, Guo, Wang, Yu, Wu, Liu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2412.05271.
  -> INFO: Now checking 1 results for matching title: 'Expanding performance boundaries of opensource multimodal models with model, data, and test-time scaling.'
       -> WARNING: Not all 40 authors from the found ref. were matched (only 40)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/63:
  -> INFO: Now checking 10 results for matching title: 'Where are you? localization from embodied dialog'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Hahn, Krantz, Rehg, Anderson'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Cartillier, Ren, Jain, Essa'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2004.06799.
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'Robothor: An open simulation-to-real embodied ai platform.'
       -> INFO: All authors matched!
- Checking reference 12/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2305.14314.
  -> INFO: Now checking 10 results for matching title: 'Qlora: Efﬁcient ﬁnetuning of quantized llms.'
       -> INFO: All authors matched!
- Checking reference 13/63:
  -> INFO: Now checking 10 results for matching title: 'CARLA: An open urban driving simulator'
       -> INFO: All authors matched!
- Checking reference 14/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2205.12219.
  -> INFO: Now checking 6 results for matching title: 'Aerial vision-and-dialog navigation.'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Qiao, Wu, Wu'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Su, Xu, Huang'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cui, Li, Liu, Jiao'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Su, Ning, Ling, Huang'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Xia, Tang, Zhu, Zhu, Yao'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 15/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2007.04954.
  -> INFO: Now checking 2 results for matching title: 'Threedworld: A platform for interactive multi-modal physical simulation.'
       -> WARNING: Not all 23 authors from the found ref. were matched (only 23)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2103.14025.
  -> INFO: Now checking 1 results for matching title: 'The threedworld transport challenge: A visually guided task-and-motion planning benchmark for physically realistic embodied ai.'
       -> INFO: All authors matched!
- Checking reference 17/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2410.09604.
  -> INFO: Now checking 1 results for matching title: 'Embodiedcity: A benchmark platform for embodied agent in real-world city environment.'
       -> INFO: All authors matched!
- Checking reference 18/63:
  -> Checking if provided link is pingable: https://doi.org/10.1109/tssc.1968.300136.
  -> INFO: Now checking 3 results for matching title: 'A formal basis for the heuristic determination of minimum cost paths'
       -> INFO: All authors matched!
- Checking reference 19/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2111.09543.
  -> INFO: Now checking 1 results for matching title: 'Debertav3: Improving deberta using electrastyle pre-training with gradient-disentangled embedding sharing.'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/63:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'A comprehensive survey of pid and pure pursuit control algorithms for autonomous vehicle navigation'
       -> INFO: All authors matched!
- Checking reference 21/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2210.03094.
  -> INFO: Now checking 10 results for matching title: 'Vima: General robot manipulation with multimodal prompts.'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
       -> INFO: All authors matched!
- Checking reference 22/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1712.05474.
  -> INFO: Now checking 2 results for matching title: 'Ai2-thor: An interactive 3d environment for visual ai.'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2022)!
       -> WARNING: Not all 8 authors from the found ref. were matched (only 8)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 23/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2004.02857.
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Beyond the navgraph: Vision-and-language navigation in continuous environments.
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 2 results for matching title: 'Beyond the navgraph: Vision-and-language navigation in continuous environments.'
       -> INFO: All authors matched!
- Checking reference 24/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2406.00837.
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Arena 3'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Arena 3'
       -> INFO: All authors matched!
- Checking reference 25/63:
  -> INFO: Now checking 10 results for matching title: 'Drivlme: A large-scale multi-agent driving benchmark.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Lastname', 'Others', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Drivlme:+A+large-scale+multi-agent+driving+benchmark. manually and check the results.
        -> Author(s): Firstname Lastname and Others
        -> Title:     Drivlme: A large-scale multi-agent driving benchmark.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 26/63:
  -> INFO: Now checking 4 results for matching title: 'Robotslang: Grounded natural language for multi-robot object search.'
  -> WARNING: None of the 4 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lastname', 'Others', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Robotslang:+Grounded+natural+language+for+multi-robot+object+search. manually and check the results.
        -> Author(s): Firstname Lastname and Others
        -> Title:     Robotslang: Grounded natural language for multi-robot object search.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 27/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2108.03272.
  -> INFO: Now checking 10 results for matching title: 'igibson 2'
       -> WARNING: Not all 16 authors from the found ref. were matched (only 15)
                   Unmatched authors = 'Mart'in-Mart'in'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 7)
                   Unmatched authors = 'Mart'in-Mart'in, Fan, Wang, Buch, D'Arpino, Tchapmi, Tchapmi'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Fan, Wang, Buch, D'Arpino, Tchapmi, Tchapmi'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Huang, Wang, Liang, Di'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zheng, O'Regan'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 28/63:
  -> Checking if provided link is pingable: https://proceedings.mlr.press/v205/li23a.html.
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'Behavior-1k: A benchmark for embodied ai with 1,000 everyday activities and realistic simulation'
       -> WARNING: Not all 28 authors from the found ref. were matched (only 27)
                   Unmatched authors = 'Martín-Martín'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/63:
  -> Checking if provided link is pingable: https://proceedings.neurips.cc/paper_files/paper/2024/file/d8087deaf34bb07ddd41c65f8a9fe9b5-Paper-Datasets_and_Benchmarks_Track.pdf.
  -> INFO: Now checking 2 results for matching title: 'Human-aware vision-andlanguage navigation: Bridging simulation to reality with dynamic human interactions'
       -> INFO: All authors matched!
- Checking reference 30/63:
  -> INFO: Now checking 1 results for matching title: 'Metadrive: Composing diverse driving scenarios for generalizable reinforcement learning'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 5)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2308.06735.
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 3 results for matching title: 'Aerialvln: Vision-and-language navigation for uavs.'
       -> INFO: All authors matched!
- Checking reference 32/63:
  -> INFO: Now checking 10 results for matching title: 'Multi-agent actor-critic for mixed cooperative-competitive environments'
       -> INFO: All authors matched!
- Checking reference 33/63:
  -> INFO: Now checking 1 results for matching title: 'Dorothie: Spoken dialogue for handling unexpected situations in interactive autonomous driving agents.'
       -> INFO: All authors matched!
- Checking reference 34/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2112.03227.
  -> INFO: Now checking 7 results for matching title: 'Calvin: A benchmark for language-conditioned policy learning for long-horizon robot manipulation tasks.'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
       -> WARNING: Not all 3 authors from the found ref. were matched (only 3)
                   Unmatched authors = ''
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Borja-Diaz'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 35/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2107.14483.
  -> INFO: Now checking 6 results for matching title: 'Maniskill: Generalizable manipulation skill benchmark with large-scale demonstrations.'
       -> INFO: All authors matched!
- Checking reference 36/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2410.21276.
  -> INFO: Now checking 10 results for matching title: 'Gpt-4o system card.'
       -> INFO: All authors matched!
- Checking reference 37/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2304.07193.
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Dinov2: Learning robust visual features without supervision.'
       -> WARNING: Not all 26 authors from the found ref. were matched (only 25)
                   Unmatched authors = 'Jégou'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang, Ze, Sun, Yuan'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Chen, Chen, Wang, Tao'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Caron, Goyal'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Tsai, Salakhutdinov'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Goyal, Duval, Seessel, Caron, Sagun'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 38/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1806.07011.
  -> INFO: Now checking 10 results for matching title: 'Virtualhome: Simulating household activities via programs.'
       -> INFO: All authors matched!
- Checking reference 39/63:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Watch-and-help: A challenge for social perception and humanai collaboration
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Puig', 'Shu', 'Li', 'Wang', 'Liao', 'Tenenbaum', 'Fidler', 'Torralba', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Watch-and-help:+A+challenge+for+social+perception+and+humanai+collaboration manually and check the results.
        -> Author(s): Xavier Puig, Tianmin Shu, Shuang Li, Zilin Wang, Yuan-Hong Liao, Joshua B Tenenbaum, Sanja Fidler, and Antonio Torralba
        -> Title:     Watch-and-help: A challenge for social perception and humanai collaboration
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 40/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2310.13724.
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Habitat 3'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Puig', 'Undersander', 'Szot', 'Cote', 'Yang', 'Partsey', 'Desai', 'Clegg', 'Hlavac', 'Min', 'Vondru', 'Gervet', 'Berges', 'Turner', 'Maksymets', 'Kira', 'Kalakrishnan', 'Malik', 'Chaplot', 'Jain', 'Batra', 'Rai', 'Mottaghi', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Habitat+3 manually and check the results.
        -> Author(s): Xavier Puig, Eric Undersander, Andrew Szot, Mikael Dallaire Cote, Tsung-Yen Yang, Ruslan Partsey, Ruta Desai, Alexander William Clegg, Michal Hlavac, So Yeon Min, Vladimír Vondru, Theophile Gervet, Vincent-Pierre Berges, John M  Turner, Oleksandr Maksymets, Zsolt Kira, Mrinal Kalakrishnan, Jitendra Malik, Devendra Singh Chaplot, Unnat Jain, Dhruv Batra, Akshara Rai, and Roozbeh Mottaghi
        -> Title:     Habitat 3
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 41/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2010.08600.
  -> INFO: Now checking 10 results for matching title: 'Robot navigation in constrained pedestrian environments using reinforcement learning.'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'P'erez-D'Arpino'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 42/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1904.10151.
  -> INFO: Now checking 7 results for matching title: 'Reverie: Remote embodied visual referring expression in real indoor environments.'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Guo, Liu, Sun'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lin'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 6)
                   Unmatched authors = ''
       -> WARNING: Not all 6 authors from the found ref. were matched (only 5)
                   Unmatched authors = 'Liu'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Qiao, Liu'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Mohammadi, Abbasnejad, Shi'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 43/63:
  -> Checking if provided link is pingable: https://doi.org/10.1145/3123266.3129396.
  -> INFO: Now checking 10 results for matching title: 'Unrealcv: Virtual worlds for computer vision'
       -> INFO: All authors matched!
- Checking reference 44/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1705.05065.
  -> INFO: Now checking 1 results for matching title: 'Airsim: High-ﬁdelity visual and physical simulation for autonomous vehicles.'
       -> INFO: All authors matched!
- Checking reference 45/63:
  -> INFO: Now checking 1 results for matching title: 'Alfred: A benchmark for interpreting grounded instructions for everyday tasks'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 46/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2108.03332.
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 2 results for matching title: 'Behavior: Benchmark for everyday household activities in virtual, interactive, and ecological environments.'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Mart'in-Mart'in'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Zhang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 47/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2106.14405.
  -> INFO: Now checking 10 results for matching title: 'Habitat 2'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Szot', 'Clegg', 'Undersander', 'Wijmans', 'Zhao', 'Turner', 'Maestre', 'Mukadam', 'Chaplot', 'Maksymets', 'Gokaslan', 'Vondrus', 'Dharur', 'Meier', 'Galuba', 'Chang', 'Kira', 'Koltun', 'Malik', 'Savva', 'Batra', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Habitat+2 manually and check the results.
        -> Author(s): Andrew Szot, Alex Clegg, Eric Undersander, Erik Wijmans, Yili Zhao, John Turner, Noah Maestre, Mustafa Mukadam, Devendra Chaplot, Oleksandr Maksymets, Aaron Gokaslan, Vladimir Vondrus, Sameer Dharur, Franziska Meier, Wojciech Galuba, Angel Chang, Zsolt Kira, Vladlen Koltun, Jitendra Malik, Manolis Savva, and Dhruv Batra
        -> Title:     Habitat 2
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 48/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2312.11805.
  -> INFO: Now checking 8 results for matching title: 'Gemini: A family of highly capable multimodal models.'
       -> WARNING: Not all 118 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Abeyruwan, Ainslie, Alayrac, Arenas, Armstrong, Balakrishna, Baruch, Bauzá, Blokzijl, Bohez, Bousmalis, Brohan, Buschmann, Byravan, Cabi, Caluwaerts, Casarini, Chang, Chen, Chen, Chiang, Choromanski, D'Ambrosio, Dasari, Davchev, Devin, Palo, Ding, Dostmohamed, Driess, Du, Dwibedi, Elabd, Fantacci, Fong, Frey, Fu, Giustina, Gopalakrishnan, Graesser, Hasenclever, Heess, Hernaez, Herzog, Hofer, Humplik, Iscen, Jacob, Jain, Julian, Kalashnikov, Karagozler, Karp, Kew, Kirkland, Kirmani, Kuang, Lampe, Laurens, Leal, Lee, Lee, Liang, Lin, Maddineni, Majumdar, Michaely, Moreno, Neunert, Nori, Parada, Parisotto, Pastor, Pooley, Rao, Reymann, Sadigh, Saliceti, Sanketi, Sermanet, Shah, Sharma, Shea, Shu, Sindhwani, Singh, Soricut, Springenberg, Sterneck, Surdulescu, Tan, Tompson, Vanhoucke, Varley, Vesom, Vezzani, Vinyals, Wahid, Welker, Wohlhart, Xia, Xiao, Xie, Xie, Xu, Xu, Xu, Xu, Yang, Yao, Yaroshenko, Yu, Yuan, Zhang, Zhang, Zhou, Zhou'
       -> WARNING: Not all 500 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Comanici, Bieber, Schaekermann, Pasupat, Sachdeva, Dhillon, Blistein, Ram, Zhang, Rosen, Marris, Petulla, Gaffney, Aharoni, Lintz, Pais, Jacobsson, Szpektor, Jiang, Haridasan, Omran, Saunshi, Bahri, Mishra, Chu, Boyd, Hekman, Parisi, Zhang, Kawintiranon, Bedrax-Weiss, Wang, Xu, Purkiss, Mendlovic, Deutel, Nguyen, Langley, Korn, Rossazza, Ram'e, Waghmare, Miller, Keshava, Jian, Zhang, Popa, Dhamdhere, Bratanivc, Kim, Koo, Alet, Chen, Nagrani, Muckenhirn, Zhang, Quick, Paveti'c, Nguyen, Carreira, Elabd, Qureshi, Mentzer, Yang, Eisenbud, Gulati, Talius, Ghalebikesabi, Yvinec, Saade, Ulrich, Blanco, Calian, Huang, Oord, Goyal, Chen, Rawlani, Schallhart, Lokhande, Luo, Shan, Montgomery, Krakovna, Piccinini, Barak, Cui, Jia, Dektiarev, Kolganov, Huang, Chen, Wang, Austin, Boursac, Sluzhaev, Ding, Li, Bhupatiraju, Agarwal, Kwasiborski, Sandhu, Siegler, Iscen, Ben-David, Butt, Allamanis, Benjamin, Busa-Fekete, Hernández-Campos, Goldshtein, Dibb, Zhang, Marsden, Radebaugh, Roller, Nayyar, Austin, Terzi, Shamanna, Shaw, Singh, Luisier, Mendoncca, Aggarwal, Markeeva, Fantacci, Brin, Choe, Wang, Adam, Dabush, Kiyono, Marcus, Cole, Weber, Lee, Huang, Muzio, Kieliger, Le, Biles, Le, Sharma, Yang, Lamp, Dopson, Hurley, Xu, Shan, Song, Tan, Senges, Zhang, You, Jun, Raposo, Ricco, Yang, Chen, Gupta, Szlam, Villela, Ferng, Kasenberg, Liang, Zhu, Narayanaswamy, Perot, Pucciarelli, Shekhawat, Stern, Ingale, Karp, Bahargam, Goedeckemeyer, Han, Li, Tacchetti, Yu, Chakladar, Zhang, Mahdy, Gao, Johnson, Phatale, Piergiovanni, Lim, Farabet, Lebsack, Guidroz, Blitzer, Duduta, Madras, Li, Dincklage, Li, Mahdieh, Tucker, Jawahar, Xiao, Tarlow, Geirhos, Velan, Vlasic, Bullard, Park, Gupta, Webster, Hitron, Mao, Eisenschlos, Prince, D'souza, Zheng, Nasso, Botea, Doersch, Unlu, Alberti, Svyatkovskiy, Goel, Choromanski, Jiang, Nguyen, Flynn, Ćurko, Chen, Roth, Milan, Habtegebriel, Narayan, Moffitt, Marcus, Anthony, McMahan, Cheon, Liu, Barnes, Lew, Santamaria-Fernandez, Upadhyay, Akula, Hrafnkelsson, Caceres, Bunner, Sokolik, Puttagunta, Moore, Isik, Hartford, Chan, Shenoy, Holtmann-Rice, Park, Viola, Salcianu, Rajayogam, Stewart-Binks, Wu, Everett, Xiong, Manzagol, Leung, Saroufim, Pang, Wegner, Papamakarios, Palomaki, Pankov, Lai, Tubone, Zhao, Strinopoulos, Neel, Wang, Kelley, Li, Xu, Vijayakumar, D'olimpio, Levy, Nicosia, Rozhdestvenskiy, Lao, Xie, Katariya, Simon, Kumar, Hartmann, Kilgore, Lee, Mahendru, Ring, Hennigan, Lang, Cherry, Steiner, Hwang, Smith, Wang, Chen, Yang, Kwei, Schlattner, Kim, Girirajan, Momchev, Agarwal, Zhou, Safarli, Garrett, Pierigiovanni, Jauhari, Rochman, Vashishth, Yuan, Angermueller, Blanton, Song, Gundavarapu, Avrahami, Deines, Roy, Gupta, Semturs, Vasudevan, Veerubhotla, Sharma, Jacob, Yang, Terzis, Karliner, Wright, Rojas-Esponda, Brown, Roy, Dogra, Kapishnikov, Young, Kan, Rajendran, Ivanova, Deshmukh, Ho, Kwong, Ginzburg, Louis, Sawhney, Petrov, Xie, Bai, Stoyanov, Fabrikant, Jayaram, Li, Heyward, Gilmer, Wang, Soricut, Liu, Duan, Hayes, O'Brien, Tomar, Eiger, Fatemi, Hui, Barros, Chukwuka, Butryna, Thakur, Huang, Pan, Tang, Cabi, Doshi, Bakker, Bagri, Ley-Wild, Lelkes, Lees, Kane, Greene, Wu, Bornschein, Surita, Hodkinson, Li, Hidey, Pereira, Ammirati, Lippe, Kraft, Han, Gerlach, Wang, Panait, Han, Farris, Bi, DeBalsi, Wang, Tyen, Cohan, Zhang, Barber, Chung, Kim, Kunesch, Pecht, Akazawa, Friesen, Lyon, Eslami, Wu, Tan, Song, Kumar, Welty, Akolzin, Gibson, Augenstein, Pillai, Yuen, Phan, Wang, Barr, Zen, Hua, Liu, Wang, Bhatia, Xu, Elyada, Kohli, Olvs'ak, Chen, Mirhoseini, Shazeer, Jakobovits, Tran, Ramsden, Bharti, Alcober, Li, Shetty, Chen, Kalashnikov, Nawhal, Arik, Chen, Blokzijl, Gupta, Rubin, Swavely, Bridgers, Gemp, Su, Suggala, Pluto, Cassin, Vaucher, Ji, Cai, Audibert, Sinha, Tian, Farkash, Hua, Chen, Tran, Loper, Brichtova, McConnaughey, Sandhu, Leland, DeCarlo, Over, Huang, Wu, Fan, Li, Lei, Sharma, Paduraru, Yu, Bovsnjak, Dao, Choi, Kudugunta, Adamek, Gu'ia, Khodaei, Feng, Zeng, Welling, Tata, Butterfield'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 49/63:
  -> Checking if provided link is pingable: https://goo.gle/Gemma3Report.
  -> INFO: Now checking 10 results for matching title: 'Gemma 3'
       -> WARNING: Not all 210 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Kamath, Ferret, Pathak, Vieillard, Merhej, Perrin, Matejovicova, Ram'e, Rivière, Rouillard, Mesnard, Cideron, Grill, Ramos, Yvinec, Casbon, Pot, Penchev, Liu, Visin, Kenealy, Beyer, Zhai, Tsitsulin, Busa-Fekete, Feng, Sachdeva, Coleman, Gao, Mustafa, Barr, Parisotto, Tian, Eyal, Cherry, Peter, Sinopalnikov, Bhupatiraju, Agarwal, Kazemi, Malkin, Kumar, Vilar, Brusilovsky, Luo, Steiner, Friesen, Sharma, Sharma, Gilady, Goedeckemeyer, Saade, Kolesnikov, Bendebury, Abdagic, Vadi, Gyorgy, Pinto, Das, Bapna, Miech, Yang, Paterson, Shenoy, Chakrabarti, Piot, Wu, Shahriari, Petrini, Chen, Lan, Choquette-Choo, Carey, Brick, Deutsch, Eisenbud, Cattle, Cheng, Paparas, Sreepathihalli, Reid, Tran, Zelle, Noland, Huizenga, Kharitonov, Liu, Amirkhanyan, Cameron, Hashemi, Klimczak-Pluci'nska, Singh, Mehta, Lehri, Hazimeh, Ballantyne, Szpektor, Nardini, Pouget-Abadie, Chan, Stanton, Wieting, Lai, Orbay, Fernandez, Newlan, Ji, Singh, Black, Yu, Hui, Vodrahalli, Greff, Qiu, Valentine, Coelho, Ritter, Hoffman, Watson, Chaturvedi, Moynihan, Babar, Noy, Byrd, Roy, Momchev, Chauhan, Bunyan, Botarda, Caron, Rubenstein, Culliton, Schmid, Sessa, Xu, Stańczyk, Tafti, Shivanna, Wu, Pan, Rokni, Willoughby, Vallu, Mullins, Jerome, Smoot, Girgin, Iqbal, Reddy, Sheth, Põder, Bhatnagar, Panyam, Eiger, Zhang, Liu, Yacovone, Liechty, Kalra, Evci, Misra, Roseberry, Feinberg, Kolesnikov, Han, Kwon, Chen, Chow, Zhu, Wei, Egyed, Cotruta, Giang, Kirk, Rao, Lo, Moreira, Martins, Sanseviero, Gonzalez, Gleicher, Warkentin, Mirrokni, Senter, Collins, Barral, Ghahramani, Hadsell, Matias, Sculley, Petrov, Fiedel, Shazeer, Vinyals, Dean, Hassabis, Kavukcuoglu, Farabet, Buchatskaya, Alayrac, Anil, Lepikhin, Borgeaud, Bachem, Joulin, Andreev, Hardin, Dadashi, Hussenot'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 50/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1907.04957.
  -> INFO: Now checking 10 results for matching title: 'Vision-and-dialog navigation.'
       -> INFO: All authors matched!
- Checking reference 51/63:
  -> INFO: Now checking 10 results for matching title: 'Sean 2'
       -> WARNING: Not all 500 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Castander, Fosalba, Stadel, Potter, Carretero, Tallada-Cresp'i, Pozzetti, Bolzonella, Mamon, Blot, Hoffmann, Huertas-Company, Monaco, Gonzalez, Lucia, Scarlata, Breton, Linke, Viglione, Zhai, Baghkhani, Pardede, Neissner, Teyssier, Crocce, Tutusaus, Miller, Congedo, Biviano, Hirschmann, Pezzotta, Aussel, Hoekstra, Kitching, Percival, Guzzo, Mellier, Oesch, Bowler, Bruton, Allevato, Gonzalez-Perez, Manera, Ávila, Kov'acs, Aghanim, Altieri, Amara, Amendola, Andreon, Auricchio, Baldi, Balestra, Bardelli, Bender, Bodendorf, Bonino, Branchini, Brescia, Brinchmann, Camera, Capobianco, Carbone, Casas, Castellano, Cavuoti, Cimatti, Conselice, Conversi, Copin, Corcione, Courbin, Courtois, Silva, Degaudenzi, Giorgio, Dinis, Douspis, Dubath, Duncan, Dupac, Dusini, Ealet, Farina, Farrens, Ferriol, Fotopoulou, Fourmanoit, Frailis, Franceschi, Franzetti, Galeotta, Gillard, Gillis, Giocoli, G'omez-Alvarez, Granett, Grazian, Grupp, Haugan, Holliman, Holmes, Hook, Hormuth, Hornstrup, Hudelot, Jahnke, Jhabvala, Joachimi, Keihanen, Kermiche, Kiessling, Kilbinger, Kohley, Kubik, Kummel, Kunz, Kurki-Suonio, Lahav, Laureijs, Mignant, Ligori, Lilje, Lindholm, Lloro, Maino, Maiorano, Mansutti, Marggraf, Markovič, Martinet, Marulli, Massey, Masters, Maurogordato, McCracken, Medinaceli, Mei, Melchior, Meneghetti, Merlin, Meylan, Mohr, Moresco, Moscardini, Munari, Nakajima, Nichol, Niemi, Padilla, Paech, Paltani, Pasian, Peacock, Pedersen, Pettorino, Pires, Polenta, Poncet, Popa, Raison, Rebolo, Renzi, Rhodes, Riccio, Romelli, Roncarelli, Rosset, Rossetti, Saglia, Sapone, Schirmer, Schneider, Schrabback, Scodeggio, Secroun, Seidel, Serrano, Sirignano, Sirri, Stanco, Starck, Taylor, Teplitz, Tereno, Toledo-Moreo, Torradeflot, Tsyganov, Valenziano, Vassallo, Veropalumbo, Wang, Weller, Zacchei, Zamorani, Zerbi, Zoubian, Zucca, Baccigalupi, Bernardeau, Boucaud, Bozzo, Burigana, Calabrese, Casenove, Castignani, Colodro-Conde, Ferdinando, Vigo, Fabbian, Finelli, Graciá-Carpio, Ili'c, Liebing, Marcin, Martinelli, Matthew, Mauri, Pontinen, Porciani, Sakr, Scottez, Sefusatti, Steinwagner, Tenti, Viel, Wiesmann, Akrami, Anselmi, Archidiacono, Atrio-Barandela, Aubourg, Balaguera-Antolínez, Ballardini, Bertacca, Béthermin, Blanchard, Bohringer, Borgani, Bouvard, Cabanac, Calabrò, Quevedo, Cañas-Herrera, Cappi, Caro, Carvalho, Castro, Chambers, Contarini, Contini, Cooray, Costanzi, Cucciati, Davini, Caro, Torre, Desprez, D'iaz-S'anchez, Diaz, Domizio, Dole, Escoffier, Ezziati, Ferrari, Ferreira, Ferrero, Finoguenov, Fontana, Fornari, Gabarra, Ganga, Garc'ia-Bellido, Gasparetto, Gaztañaga, Giacomini, Gianotti, Gonzalez, Gozaliasl, Hall, Hartley, Hildebrandt, Hjorth, Holland, Ilbert, Joudaki, Jullo, Kajava, Kansal, Karagiannis, Kirkpatrick, Graet, Legrand, Lesgourgues, Liaudat, Loureiro, Macías-Pérez, Magliocchetti, Mancini, Mannucci, Maoli, Martins, Maurin, Metcalf, Migliaccio, Miluzio, Mora, Moretti, Morgante, Nadathur, Nicastro, Walton, Oguri, Patrizii, Popa, Pourtsidou, Reimberg, Risso, Rocci, Rollins, Rusholme, Sahl'en, S'anchez, Schaye, Schewtschenko, Schneider, Schultheis, Sereno, Shankar, Shulevski, Silvestri, Simon, Mancini, Stanford, Tanidis, Tao, Tessore, Testera, Tewes, Toft, Tosi, Troja, Tucci, Valieri, Valiviita, Vergani, Vernizzi, Verza, Vielzeuf, Weaver, Zalesky, Dimauro, Duc, Fang, Ferguson, Gutiérrez, Kovavci'c, Kruk, Brun, Montoro, Murray, Pagano, Paoletti, Sarpa, Viitanen, Mart'in-Fleitas, Sciences, Uab, Magrans, Sn, Barcelona, Spain., Catalunya, Rdit, Upc, Castelldefels, Barcelona, Astrophysics, Zurich, 190, Zurich, Switzerland., Energ'eticas, Tecnol'ogicas, AvenidaComplutense, Madrid, Cient'ifica, Sn, Bellaterra, Bologna, 933, Bologna, Italy, Paris, 7095, Cnrs, Universit'e, Arago, Paris, France, Arago, 75014, Paris, Physics, Universe, Tokyo, Kashiwa, 277-8583, Japan., Th'eorie, Paris, Psl, Cit'e, Meudon, Canarias, sn, 38204, Laguna, Tenerife, Astrof'isica, Laguna, 38200, Laguna, Lerma, Paris-Cit'e, Mann, 75013, Astronomia, Trieste, ViaTiepolo, Trieste, Trieste, ViaG.B.Tiepolo, Trieste, Infn, Trieste, ViaValerio, 34127Trieste, Ifpu, Universe, viaBeirut, Trieste, Energies, Science, Technology, Experimental, 854, X5000BGR, C'ordoba, Argentina, Astrophysics, Minnesota, 116ChurchSt, Minneapolis, 55455, Usa, l'Espai, Vall'es, Innsbruck, Teilchenphysik, 258, Innsbruck, Austria, Observatory, University, Einsteinweg, Leiden, Netherlands., Astronomy, Physics, Astronomy, University, 200240, China, Physics, Cosmology, Astrophysics, Waterloo, Waterloo, 3G1, Canada, Physics, Parma, Parma, Sissa, Studies, 265, 34136Trieste, Physics, StradaCostiera, Sciences, Hall, University., Princeton, 08544, Plan'etologie, Toulouse, Ups, Cnes'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 52/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2407.10943.
  -> INFO: Now checking 1 results for matching title: 'Grutopia: Dream general robots in a city at scale.'
       -> INFO: All authors matched!
- Checking reference 53/63:
  -> INFO: Now checking 1 results for matching title: 'Qwen2-vl: Enhancing vision-language model’s perception of the world at any resolution'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Dang, Du, Ren, Men, Zhou, Zhou'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/63:
  -> Checking if provided link is pingable: http://www.jstor.org/stable/2276774.
  -> INFO: Now checking 1 results for matching title: 'Probable inference, the law of succession, and statistical inference'
       -> INFO: All authors matched!
- Checking reference 55/63:
  -> INFO: Now checking 1 results for matching title: 'Metaurban: An embodied ai simulation platform for urban micromobility.'
       -> INFO: All authors matched!
- Checking reference 56/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2407.08725.
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'Metaurban: An embodied ai simulation platform for urban micromobility.'
       -> INFO: All authors matched!
- Checking reference 57/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2210.03629.
  -> INFO: Now checking 3 results for matching title: 'React: Synergizing reasoning and acting in language models.'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Guo, Zhou, Deng, Zhu, Bao'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 58/63:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=Kb4fDvJBlj.
  -> INFO: Now checking 2 results for matching title: 'Partinstruct: Part-level instruction following for ﬁne-grained robot manipulation'
       -> INFO: All authors matched!
- Checking reference 59/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2310.12020.
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'Lohoravens: A long-horizon languageconditioned benchmark for robotic tabletop manipulation.'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 7)
                   Unmatched authors = 'Senel'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 60/63:
  -> INFO: Now checking 5 results for matching title: 'Roco: Dialectic multi-robot collaboration with large language models.'
       -> INFO: All authors matched!
- Checking reference 61/63:
  -> INFO: Now checking 2 results for matching title: 'Unrealzoo: Enriching photo-realistic virtual worlds for embodied ai'
       -> INFO: All authors matched!
- Checking reference 62/63:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2508.14893.
  -> INFO: Now checking 3 results for matching title: 'Virtual community: An open world for humans, robots, and society.'
       -> INFO: All authors matched!
- Checking reference 63/63:
  -> INFO: Now checking 1 results for matching title: 'Simworld: An open-ended realistic simulator for autonomous agents in physical and social worlds.'
       -> WARNING: Not all 23 authors from the found ref. were matched (only 12)
                   Unmatched authors = 'Mao, Shen, Liang, Yue, Yang, Liu, Benavente, Nagaraju, Faayez, Sharma, Zhong'
  -> INFO: No perfect match found; taking the next best!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 20: forward, move backward, move left, move right, turn left (−90◦), turn right (+90◦), or stay still.
-> Invalid unicode use found on p. 21: (d0 −dT
-> Invalid unicode use found on p. 21: 5 for i ←2 to k −1 do
-> Invalid unicode use found on p. 21: if θi ̸= θi−1 then
-> Invalid unicode use found on p. 21: Vmove ←capture visual cue at ni−1 with orientation θi−1;
-> Invalid unicode use found on p. 21: Imove ←generate Move Along the Road instruction using a landmark near ni−1;
-> Invalid unicode use found on p. 21: θi−1 and θi;
-> Invalid unicode use found on p. 28: (D0 −DT
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 416 sentences on 11 pages -> Avg. of 42.6 sentences per page
-> Warning: Reference '5' never used in the document's text.
-> Warning: Reference '6' never used in the document's text.
-> Warning: Reference '12' never used in the document's text.
-> Warning: Reference '14' never used in the document's text.
-> Warning: Reference '16' never used in the document's text.
-> Warning: Reference '21' never used in the document's text.
-> Warning: Reference '22' never used in the document's text.
-> Warning: Reference '24' never used in the document's text.
-> Warning: Reference '27' never used in the document's text.
-> Warning: Reference '29' never used in the document's text.
-> Warning: Reference '34' never used in the document's text.
-> Warning: Reference '39' never used in the document's text.
-> Warning: Reference '42' never used in the document's text.
-> Warning: Reference '43' never used in the document's text.
-> Warning: Reference '46' never used in the document's text.
-> Warning: Reference '51' never used in the document's text.
-> Warning: Reference '54' never used in the document's text.
-> Warning: Reference '58' never used in the document's text.
-> Warning: Reference '59' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> WARNING: Reference with index 13 (Ref. ID = 14) has no associated sentence!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> WARNING: Reference with index 21 (Ref. ID = 22) has no associated sentence!
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> WARNING: Reference with index 26 (Ref. ID = 27) has no associated sentence!
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> WARNING: Reference with index 33 (Ref. ID = 34) has no associated sentence!
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> WARNING: Reference with index 41 (Ref. ID = 42) has no associated sentence!
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> WARNING: Reference with index 45 (Ref. ID = 46) has no associated sentence!
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> WARNING: Reference with index 50 (Ref. ID = 51) has no associated sentence!
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 57 (Ref. ID = 58); Skipping LLM check...
-> WARNING: Reference with index 58 (Ref. ID = 59) has no associated sentence!
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
-> Missing an abstract for reference with index 61 (Ref. ID = 62); Skipping LLM check...
  // LLM calling counter = 17
  -> Automatic parsing of LLM list worked!
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
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
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━  84% 0:00:01
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 22
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
###############################
# Starting Author Check
###############################
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\3 SimWorld-Robotics\PAU_results.md
```