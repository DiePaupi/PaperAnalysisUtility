
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\42 Tri-Modal\A Tri-Modal Multi-Agent Responsive Framework for Comprehensive 3D Object Annotation.pdf"
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
- Found following heading '2 - Related Works' on page 3
- Found following heading '3 - Methodology' on page 4
- Found following heading '4 - Experiments' on page 7
- Found following heading '5 - Conclusion' on page 9
=> Found references/literature section on page 10
- Found heading after References '6 - Analysis of GPU Memory Usage and Computing Efficiency' on page 14
- Found heading after References '7 - Isolating the Benefits of Multi-Agent Collaboration' on page 15
- Found heading after References '8 - Justification for MAB-based Aggregation in Tri-MARF' on page 16
- Found heading after References '9 - Exploring Tri-MARF for 3D Scene Annotation' on page 18
- Found heading after References '10 - Cost Calculation and Analysis' on page 20
- Found heading after References '11 - Detailed Ablation Studies' on page 20
- Found heading after References '12 - Details of Human Evaluation' on page 30
- Found heading after References '13 - Robustness Evaluation Under Occlusion' on page 32
- Found heading after References '14 - Additional Details of all the experiments' on page 32
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 14
All found references: 80
-> Warning: Malformed author string: 'OpenAI'
-> Warning: Malformed author string: 'Qwen'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ... link  valid
0       1  Erfan Aghasian, Shai Avidan, Piotr Dollar, and...  ...        None
1       2  Peter Auer, Nicolò Cesa-Bianchi, and Paul Fischer  ...        None
2       3  Shaofeng Cai, Yao Shu, Wei Wang, and Beng Chin...  ...        None
3       4  Marwa Chafii, Salmane Naoumi, Reda Alami, Ebte...  ...        None
4       5  Angel X Chang, Thomas Funkhouser, Leonidas Gui...  ...        None
..    ...                                                ...  ...  ...    ...
75     76  Renrui Zhang, Ziyu Guo, Wei Zhang, Kunchang Li...  ...        None
76     77  Changgang Zheng, Shufan Yang, Juan Marcelo Par...  ...        None
77     78  Huasong Zhong, Jingyuan Chen, Chen Shen, Hanwa...  ...        None
78     79  Junsheng Zhou, Jinsheng Wang, Baorui Ma, Yu-Sh...  ...        None
79     80       Luowei Zhou, Chenliang Xu, and Jason J Corso  ...        None

[80 rows x 10 columns]
- Checking reference 1/80:
  -> INFO: Now checking 10 results for matching title: 'Hierarchical protocols for multi-agent 3d scene understanding'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Aghasian', 'Avidan', 'Dollar', 'Johnson', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Hierarchical+protocols+for+multi-agent+3d+scene+understanding manually and check the results.
        -> Author(s): Erfan Aghasian, Shai Avidan, Piotr Dollar, and Justin Johnson
        -> Title:     Hierarchical protocols for multi-agent 3d scene understanding
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 2/80:
  -> INFO: Now checking 10 results for matching title: 'Finite-time analysis of the multiarmed bandit problem'
       -> INFO: All authors matched!
- Checking reference 3/80:
  -> INFO: Now checking 10 results for matching title: 'Dynamic routing networks.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Cai', 'Shu', 'Wang', 'Ooi', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dynamic+routing+networks. manually and check the results.
        -> Author(s): Shaofeng Cai, Yao Shu, Wei Wang, and Beng Chin Ooi
        -> Title:     Dynamic routing networks.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 4/80:
  -> INFO: Now checking 10 results for matching title: 'Emergent communication in multi-agent reinforcement learning for future wireless networks.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 3 results for matching title: 'Emergent communication in multi-agent reinforcement learning for future wireless networks.'
       -> INFO: All authors matched!
- Checking reference 5/80:
  -> INFO: Now checking 10 results for matching title: 'Shapenet: An information-rich 3d model repository.'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chang', 'Funkhouser', 'Guibas', 'Hanrahan', 'Huang', 'Li', 'Savarese', 'Savva', 'Song', 'Su', 'Xiao', 'Yi', 'Yu', '2015']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Shapenet:+An+information-rich+3d+model+repository. manually and check the results.
        -> Author(s): Angel X Chang, Thomas Funkhouser, Leonidas Guibas, Pat Hanrahan, Qixing Huang, Zimo Li, Silvio Savarese, Manolis Savva, Shuran Song, Hao Su, Jianxiong Xiao, Li Yi, and Fisher Yu
        -> Title:     Shapenet: An information-rich 3d model repository.
        -> Year:      2015
     -> Manual search was skipped by the user.
- Checking reference 6/80:
  -> INFO: Now checking 10 results for matching title: 'Shapenet: An information-rich 3d model repository.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chang', 'Funkhouser', 'Guibas', 'Hanrahan', 'Huang', 'Li', 'Savarese', 'Savva', 'Song', 'Su', 'Xiao', 'Yi', 'Yu', '2015']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Shapenet:+An+information-rich+3d+model+repository. manually and check the results.
        -> Author(s): Angel X Chang, Thomas Funkhouser, Leonidas Guibas, Pat Hanrahan, Qixing Huang, Zimo Li, Silvio Savarese, Manolis Savva, Shuran Song, Hao Su, Jianxiong Xiao, Li Yi, and Fisher Yu
        -> Title:     Shapenet: An information-rich 3d model repository.
        -> Year:      2015
     -> Manual search was skipped by the user.
- Checking reference 7/80:
  -> INFO: Now checking 10 results for matching title: 'Shapenet: An information-rich 3d model repository.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chang', 'Funkhouser', 'Guibas', 'Hanrahan', 'Huang3', 'Li', 'Savarese', 'Savva', 'Song', 'Su', 'Xiao', 'Yi', 'Yu', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Shapenet:+An+information-rich+3d+model+repository. manually and check the results.
        -> Author(s): Angel X Chang, Thomas Funkhouser, Leonidas Guibas, Pat Hanrahan, Qixing Huang3, Zimo Li, Silvio Savarese, Manolis Savva, Shuran Song, Hao Su, Jianxiong Xiao, Li Yi, and Fisher Yu
        -> Title:     Shapenet: An information-rich 3d model repository.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 8/80:
  -> INFO: Now checking 10 results for matching title: 'Iterative visual reasoning beyond convolutions'
       -> INFO: All authors matched!
- Checking reference 9/80:
  -> INFO: Now checking 2 results for matching title: 'Abo: Dataset and benchmarks for real-world 3d object understanding.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Collins', 'Goel', 'Deng', 'Luthra', 'Xu', 'Gundogdu', 'Zhang', 'Vicente', 'Dideriksen', 'Arora', 'Guillaumin', 'Malik', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Abo:+Dataset+and+benchmarks+for+real-world+3d+object+understanding. manually and check the results.
        -> Author(s): Jasmine Collins, Shubham Goel, Kenan Deng, Achleshwar Luthra, Leon Xu, Erhan Gundogdu, Xi Zhang, Tomas F Yago Vicente, Thomas Dideriksen, Himanshu Arora, Matthieu Guillaumin, and Jitendra Malik
        -> Title:     Abo: Dataset and benchmarks for real-world 3d object understanding.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 10/80:
  -> INFO: Now checking 6 results for matching title: 'Scannet: Richly-annotated 3d reconstructions of indoor scenes.'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Dai', 'Chang', 'Savva', 'Halber', 'Funkhouser', 'Nießner', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Scannet:+Richly-annotated+3d+reconstructions+of+indoor+scenes. manually and check the results.
        -> Author(s): Angela Dai, Angel X Chang, Manolis Savva, Maciej Halber, Thomas Funkhouser, and Matthias Nießner
        -> Title:     Scannet: Richly-annotated 3d reconstructions of indoor scenes.
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 11/80:
  -> INFO: Now checking 1 results for matching title: 'Objaverse-XL: A universe of 10m+ 3d objects'
       -> INFO: All authors matched!
- Checking reference 12/80:
  -> INFO: Now checking 3 results for matching title: 'Objaverse: A universe of annotated 3d objects'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/80:
  -> INFO: Now checking 10 results for matching title: 'Mlod: A multi-view 3d object detection based on robust feature fusion method'
       -> INFO: All authors matched!
- Checking reference 14/80:
  -> WARNING: Skipping search (due to not enough info) for reference titled '.'
           -> Author(s): Yasutaka Furukawa and Carlos Hernández
           -> Year: 2015
- Checking reference 15/80:
  -> INFO: Now checking 1 results for matching title: 'Dynamic fusion with intra- and inter-modality attention flow for visual question answering'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/80:
  -> INFO: Now checking 10 results for matching title: 'Algorithms and theory for multiple-source adaptation.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hoffman', 'Mohri', 'Zhang', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Algorithms+and+theory+for+multiple-source+adaptation. manually and check the results.
        -> Author(s): Judy Hoffman, Mehryar Mohri, and Ningshan Zhang
        -> Title:     Algorithms and theory for multiple-source adaptation.
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 17/80:
  -> INFO: Now checking 5 results for matching title: '3d-llm: Injecting the 3d world into large language models.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hong', 'Zhen', 'Chen', 'Zheng', 'Du', 'Chen', 'Gan', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=3d-llm:+Injecting+the+3d+world+into+large+language+models. manually and check the results.
        -> Author(s): Yining Hong, Haoyu Zhen, Peihao Chen, Shuhong Zheng, Yilun Du, Zhenfang Chen, and Chuang Gan
        -> Title:     3d-llm: Injecting the 3d world into large language models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 18/80:
  -> INFO: Now checking 10 results for matching title: 'Multi-objective optimization for sparse deep multi-task learning.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hotegni', 'Berkemeier', 'Peitz', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Multi-objective+optimization+for+sparse+deep+multi-task+learning. manually and check the results.
        -> Author(s): S S Hotegni, M Berkemeier, and S Peitz
        -> Title:     Multi-objective optimization for sparse deep multi-task learning.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 19/80:
  -> INFO: Now checking 1 results for matching title: 'DenseCap: Fully convolutional localization networks for dense captioning'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/80:
  -> INFO: Now checking 10 results for matching title: 'Leveraging vlm-based pipelines to annotate 3d objects.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kabra', 'Matthey', 'Lerchner', 'Mitra', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Leveraging+vlm-based+pipelines+to+annotate+3d+objects. manually and check the results.
        -> Author(s): Rishabh Kabra, Loic Matthey, Alexander Lerchner, and Niloy J Mitra
        -> Title:     Leveraging vlm-based pipelines to annotate 3d objects.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 21/80:
  -> INFO: Now checking 1 results for matching title: 'Vilt: Vision-and-language transformer without convolution or region supervision.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kim', 'Son', 'Kim', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Vilt:+Vision-and-language+transformer+without+convolution+or+region+supervision. manually and check the results.
        -> Author(s): Wonjae Kim, Bokyung Son, and Ildoo Kim
        -> Title:     Vilt: Vision-and-language transformer without convolution or region supervision.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 22/80:
  -> INFO: Now checking 10 results for matching title: 'Darts: Differentiable architecture search.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', 'Simonyan', 'Yang', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Darts:+Differentiable+architecture+search. manually and check the results.
        -> Author(s): Hanxiao Liu, Karen Simonyan, and Yiming Yang
        -> Title:     Darts: Differentiable architecture search.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 23/80:
  -> INFO: Now checking 10 results for matching title: 'Roberta: A robustly optimized bert pretraining approach.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', 'Ott', 'Goyal', 'Du', 'Joshi', 'Chen', 'Levy', 'Lewis', 'Zettlemoyer', 'Stoyanov', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Roberta:+A+robustly+optimized+bert+pretraining+approach. manually and check the results.
        -> Author(s): Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov
        -> Title:     Roberta: A robustly optimized bert pretraining approach.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 24/80:
  -> INFO: Now checking 10 results for matching title: 'Scalable 3d captioning with pretrained models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Luo', 'Rockwell', 'Lee', 'Johnson', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Scalable+3d+captioning+with+pretrained+models. manually and check the results.
        -> Author(s): Tiange Luo, Chris Rockwell, Honglak Lee, and Justin Johnson
        -> Title:     Scalable 3d captioning with pretrained models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 25/80:
  -> INFO: Now checking 10 results for matching title: 'Scalable 3d captioning with pretrained models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Luo', 'Rockwell', 'Lee', 'Johnson', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Scalable+3d+captioning+with+pretrained+models. manually and check the results.
        -> Author(s): Tiange Luo, Chris Rockwell, Honglak Lee, and Justin Johnson
        -> Title:     Scalable 3d captioning with pretrained models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 26/80:
  -> INFO: Now checking 10 results for matching title: 'Scalable 3d captioning with pretrained models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Luo', 'Rockwell', 'Lee', 'Johnson', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Scalable+3d+captioning+with+pretrained+models. manually and check the results.
        -> Author(s): Tiange Luo, Chris Rockwell, Honglak Lee, and Justin Johnson
        -> Title:     Scalable 3d captioning with pretrained models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 27/80:
  -> INFO: Now checking 10 results for matching title: 'Agents that reduce work and information overload'
       -> INFO: All authors matched!
- Checking reference 28/80:
  -> INFO: Now checking 2 results for matching title: 'Partnet: A large-scale benchmark for fine-grained and hierarchical part-level 3d object understanding.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Mo', 'Zhu', 'Chang', 'Yi', 'Tripathi', 'Guibas', 'Su', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Partnet:+A+large-scale+benchmark+for+fine-grained+and+hierarchical+part-level+3d+object+understanding. manually and check the results.
        -> Author(s): Kaichun Mo, Shilin Zhu, Angel X Chang, Li Yi, Subarna Tripathi, Leonidas J Guibas, and Hao Su
        -> Title:     Partnet: A large-scale benchmark for fine-grained and hierarchical part-level 3d object understanding.
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 29/80:
  -> INFO: Now checking 2 results for matching title: 'Partnet: A large-scale benchmark for fine-grained and hierarchical part-level 3d object understanding'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/80:
  -> INFO: Now checking 10 results for matching title: 'Visual representations for semantic target driven navigation'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 5)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/80:
  -> INFO: Now checking 1 results for matching title: 'Issues and challenges of forensics analysis of agents’ behavior in multi-agent systems: A critical review'
       -> INFO: All authors matched!
- Checking reference 32/80:
  -> INFO: Now checking 1 results for matching title: 'Panopticfusion: Online volumetric semantic mapping at the level of stuff and things.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Narita', 'Seno', 'Ishikawa', 'Kaji', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Panopticfusion:+Online+volumetric+semantic+mapping+at+the+level+of+stuff+and+things. manually and check the results.
        -> Author(s): Gaku Narita, Takashi Seno, Tomoya Ishikawa, and Yohsuke Kaji
        -> Title:     Panopticfusion: Online volumetric semantic mapping at the level of stuff and things.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 33/80:
  -> INFO: Now checking 10 results for matching title: 'Gpt-4 technical report.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['OpenAI', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gpt-4+technical+report. manually and check the results.
        -> Author(s): OpenAI
        -> Title:     Gpt-4 technical report.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 34/80:
  -> INFO: Now checking 10 results for matching title: 'Bleu: a method for automatic evaluation of machine translation'
       -> INFO: All authors matched!
- Checking reference 35/80:
  -> INFO: Now checking 10 results for matching title: 'An overview of reinforcement learning techniques'
       -> INFO: All authors matched!
- Checking reference 36/80:
  -> INFO: Now checking 10 results for matching title: 'An overview of reinforcement learning techniques'
       -> INFO: All authors matched!
- Checking reference 37/80:
  -> INFO: Now checking 2 results for matching title: 'Gpt4point: A unified framework for point-language understanding and generation.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Qi', 'Fang', 'Sun', 'Wu', 'Wu', 'Wang', 'Lin', 'Zhao', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gpt4point:+A+unified+framework+for+point-language+understanding+and+generation. manually and check the results.
        -> Author(s): Zhangyang Qi, Ye Fang, Zeyi Sun, Xiaoyang Wu, Tong Wu, Jiaqi Wang, Dahua Lin, and Hengshuang Zhao
        -> Title:     Gpt4point: A unified framework for point-language understanding and generation.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 38/80:
  -> INFO: Now checking 1 results for matching title: 'Shrec’22 track: Sketch-based 3d shape retrieval in the wild.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Qin', 'Yuan', 'Chen', 'Amor', 'Fang', 'Hoang-Xuan', 'Chu', 'Nguyen-Ngoc', 'Cao', 'Ngo', 'Huynh', 'Nguyen', 'Tran', 'Luo', 'Wang', 'Zhang', 'Xin', 'Wang', 'Wang', 'Tang', 'Chen', 'Wang', 'Zhou', 'Zhang', 'Wang', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Shrec’22+track:+Sketch-based+3d+shape+retrieval+in+the+wild. manually and check the results.
        -> Author(s): Jie Qin, Shuaihang Yuan, Jiaxin Chen, Boulbaba Ben Amor, Yi Fang, Nhat Hoang-Xuan, Chi-Bien Chu, Khoi-Nguyen Nguyen-Ngoc, Thien-Tri Cao, Nhat-Khang Ngo, Tuan-Luc Huynh, Hai-Dang Nguyen, Minh-Triet Tran, Haoyang Luo, Jianning Wang, Zheng Zhang, Zihao Xin, Yang Wang, Feng Wang, Ying Tang, Haiqin Chen, Yan Wang, Qunying Zhou, Ji Zhang, and Hongyuan Wang
        -> Title:     Shrec’22 track: Sketch-based 3d shape retrieval in the wild.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 39/80:
  -> INFO: Now checking 10 results for matching title: 'Qwen2.5 technical report.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Qwen', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Qwen2.5+technical+report. manually and check the results.
        -> Author(s): Qwen
        -> Title:     Qwen2.5 technical report.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 40/80:
  -> INFO: Now checking 10 results for matching title: 'Learning transferable visual models from natural language supervision.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Radford', 'Kim', 'Hallacy', 'Ramesh', 'Goh', 'Agarwal', 'Sastry', 'Askell', 'Mishkin', 'Clark', 'Krueger', 'Sutskever', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Learning+transferable+visual+models+from+natural+language+supervision. manually and check the results.
        -> Author(s): Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever
        -> Title:     Learning transferable visual models from natural language supervision.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 41/80:
  -> INFO: Now checking 10 results for matching title: 'High-dimensional ising model selection using l1-regularized logistic regression'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ravikumar', 'Wainwright', 'Lafferty', '2010']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=High-dimensional+ising+model+selection+using+l1-regularized+logistic+regression manually and check the results.
        -> Author(s): Pradeep Ravikumar, Martin J Wainwright, and John D Lafferty
        -> Title:     High-dimensional ising model selection using l1-regularized logistic regression
        -> Year:      2010
     -> Manual search was skipped by the user.
- Checking reference 42/80:
  -> INFO: Now checking 1 results for matching title: 'Learning multi-view aggregation in the wild for large-scale 3d semantic segmentation'
       -> INFO: All authors matched!
- Checking reference 43/80:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Improve Convergence Speed of Multi-Agent Q-Learning for Cooperative Task Planning, pages 111–166
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sadhu', 'Konar', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Improve+Convergence+Speed+of+Multi-Agent+Q-Learning+for+Cooperative+Task+Planning%2C+pages+111–166 manually and check the results.
        -> Author(s): Arup Kumar Sadhu and Amit Konar
        -> Title:     Improve Convergence Speed of Multi-Agent Q-Learning for Cooperative Task Planning, pages 111–166
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 44/80:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Consensus Q-Learning for Multi-agent Cooperative Planning, pages 167–182
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sadhu', 'Konar', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Consensus+Q-Learning+for+Multi-agent+Cooperative+Planning%2C+pages+167–182 manually and check the results.
        -> Author(s): Arup Kumar Sadhu and Amit Konar
        -> Title:     Consensus Q-Learning for Multi-agent Cooperative Planning, pages 167–182
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 45/80:
  -> INFO: Now checking 10 results for matching title: 'Crossover: 3d scene cross-modal alignment.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sarkar', 'Miksik', 'Pollefeys', 'Barath', 'Armeni', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Crossover:+3d+scene+cross-modal+alignment. manually and check the results.
        -> Author(s): Sayan Deb Sarkar, Ondrej Miksik, Marc Pollefeys, Daniel Barath, and Iro Armeni
        -> Title:     Crossover: 3d scene cross-modal alignment.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 46/80:
  -> INFO: Now checking 5 results for matching title: 'Multi-objective optimization of performance and interpretability of tabular supervised machine learning models.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Schneider', 'Bischl', 'Thomas', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Multi-objective+optimization+of+performance+and+interpretability+of+tabular+supervised+machine+learning+models. manually and check the results.
        -> Author(s): Lennart Schneider, Bernd Bischl, and Janek Thomas
        -> Title:     Multi-objective optimization of performance and interpretability of tabular supervised machine learning models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 47/80:
  -> INFO: Now checking 10 results for matching title: 'Deterministic policy gradient algorithms'
       -> INFO: All authors matched!
- Checking reference 48/80:
  -> WARNING: Skipping search (due to not enough info) for reference titled '.'
           -> Author(s): Aleksandrs Slivkins
           -> Year: 2019
- Checking reference 49/80:
  -> INFO: Now checking 10 results for matching title: 'Multi-agent systems'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Talukdar', '2004']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Multi-agent+systems manually and check the results.
        -> Author(s): S Talukdar
        -> Title:     Multi-agent systems
        -> Year:      2004
     -> Manual search was skipped by the user.
- Checking reference 50/80:
  -> INFO: Now checking 9 results for matching title: 'Cooperative behavior by multi-agent reinforcement learning with abstractive communication'
       -> INFO: All authors matched!
- Checking reference 51/80:
  -> INFO: Now checking 2 results for matching title: '3d-grounded visionlanguage framework for robotic task planning: Automated prompt synthesis and supervised reasoning.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tang', 'Jia', 'Huang', 'Chen', 'Ji', 'Yao', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=3d-grounded+visionlanguage+framework+for+robotic+task+planning:+Automated+prompt+synthesis+and+supervised+reasoning. manually and check the results.
        -> Author(s): Guoqin Tang, Qingxuan Jia, Zeyuan Huang, Gang Chen, Ning Ji, and Zhipeng Yao
        -> Title:     3d-grounded visionlanguage framework for robotic task planning: Automated prompt synthesis and supervised reasoning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 52/80:
  -> INFO: Now checking 2 results for matching title: 'Hiva: Self-organized hierarchical variable agent via goal-driven semantic-topological evolution.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tang', 'Zhang', 'Lv', 'Liu', 'Yang', 'Tang', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Hiva:+Self-organized+hierarchical+variable+agent+via+goal-driven+semantic-topological+evolution. manually and check the results.
        -> Author(s): Jinzhou Tang, Jusheng Zhang, Qinhan Lv, Sidi Liu, Jing Yang, Chengpei Tang, and Keze Wang
        -> Title:     Hiva: Self-organized hierarchical variable agent via goal-driven semantic-topological evolution.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 53/80:
  -> INFO: Now checking 10 results for matching title: 'Attention is all you need'
       -> INFO: All authors matched!
- Checking reference 54/80:
  -> INFO: Now checking 10 results for matching title: '3d scene graph generation from point clouds'
       -> INFO: All authors matched!
- Checking reference 55/80:
  -> INFO: Now checking 10 results for matching title: 'Intelligent agents: theory and practice'
       -> INFO: All authors matched!
- Checking reference 56/80:
  -> INFO: Now checking 10 results for matching title: '3d shapenets: A deep representation for volumetric shapes.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'Song', 'Khosla', 'Yu', 'Zhang', 'Tang', 'Xiao', '2015']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=3d+shapenets:+A+deep+representation+for+volumetric+shapes. manually and check the results.
        -> Author(s): Zhirong Wu, Shuran Song, Aditya Khosla, Fisher Yu, Linguang Zhang, Xiaoou Tang, and Jianxiong Xiao
        -> Title:     3d shapenets: A deep representation for volumetric shapes.
        -> Year:      2015
     -> Manual search was skipped by the user.
- Checking reference 57/80:
  -> INFO: Now checking 10 results for matching title: 'Multi-agent reinforcement learning with distributed targeted multi-agent communication'
       -> INFO: All authors matched!
- Checking reference 58/80:
  -> INFO: Now checking 2 results for matching title: 'Ulip: Learning a unified representation of language, images, and point clouds for 3d understanding'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Mart'in-Mart'in'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/80:
  -> INFO: Now checking 1 results for matching title: 'Ulip-2: Towards scalable multimodal pre-training for 3d understanding.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Xue', 'Yu', 'Zhang', 'Panagopoulou', 'Li', 'Martín-Martín', 'Wu', 'Xiong', 'Xu', 'Niebles', 'Savarese', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Ulip-2:+Towards+scalable+multimodal+pre-training+for+3d+understanding. manually and check the results.
        -> Author(s): Le Xue, Ning Yu, Shu Zhang, Artemis Panagopoulou, Junnan Li, Roberto Martín-Martín, Jiajun Wu, Caiming Xiong, Ran Xu, Juan Carlos Niebles, and Silvio Savarese
        -> Title:     Ulip-2: Towards scalable multimodal pre-training for 3d understanding.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 60/80:
  -> INFO: Now checking 2 results for matching title: 'Depthssc: Monocular 3d semantic scene completion via depth-spatial alignment and voxel adaptation.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yao', 'Zhang', 'Pan', 'Wu', 'Xiao', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Depthssc:+Monocular+3d+semantic+scene+completion+via+depth-spatial+alignment+and+voxel+adaptation. manually and check the results.
        -> Author(s): Jiawei Yao, Jusheng Zhang, Xiaochao Pan, Tong Wu, and Canran Xiao
        -> Title:     Depthssc: Monocular 3d semantic scene completion via depth-spatial alignment and voxel adaptation.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 61/80:
  -> INFO: Now checking 2 results for matching title: 'Depthssc: Monocular 3d semantic scene completion via depth-spatial alignment and voxel adaptation.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yao', 'Zhang', 'Pan', 'Wu', 'Xiao', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Depthssc:+Monocular+3d+semantic+scene+completion+via+depth-spatial+alignment+and+voxel+adaptation. manually and check the results.
        -> Author(s): Jiawei Yao, Jusheng Zhang, Xiaochao Pan, Tong Wu, and Canran Xiao
        -> Title:     Depthssc: Monocular 3d semantic scene completion via depth-spatial alignment and voxel adaptation.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 62/80:
  -> INFO: Now checking 6 results for matching title: 'Efficient transformer-based 3d object detection with dynamic token halting.'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ye', 'Meyer', 'Chai', 'Liu', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Efficient+transformer-based+3d+object+detection+with+dynamic+token+halting. manually and check the results.
        -> Author(s): Mao Ye, Gregory P Meyer, Yuning Chai, and Qiang Liu
        -> Title:     Efficient transformer-based 3d object detection with dynamic token halting.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 63/80:
  -> INFO: Now checking 2 results for matching title: 'A scalable active framework for region annotation in 3D shape collections'
       -> INFO: All authors matched!
- Checking reference 64/80:
  -> INFO: Now checking 10 results for matching title: 'Deep reinforcement learning for visual object tracking'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Han', 'Zhao', 'Meng', 'Yang', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+reinforcement+learning+for+visual+object+tracking manually and check the results.
        -> Author(s): Da Zhang, Junwei Han, Long Zhao, Deyu Meng, and Yi Yang
        -> Title:     Deep reinforcement learning for visual object tracking
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 65/80:
  -> INFO: Now checking 1 results for matching title: 'Multi-agent systems for distributed problem solving: A framework for task decomposition and coordination'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Li', '2015']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Multi-agent+systems+for+distributed+problem+solving:+A+framework+for+task+decomposition+and+coordination manually and check the results.
        -> Author(s): J Zhang and X Li
        -> Title:     Multi-agent systems for distributed problem solving: A framework for task decomposition and coordination
        -> Year:      2015
     -> Manual search was skipped by the user.
- Checking reference 66/80:
  -> INFO: Now checking 1 results for matching title: 'Neural slam: Learning to explore with external memory.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Tai', 'Liu', 'Boedecker', 'Burgard', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Neural+slam:+Learning+to+explore+with+external+memory. manually and check the results.
        -> Author(s): Jingwei Zhang, Lei Tai, Ming Liu, Joschka Boedecker, and Wolfram Burgard
        -> Title:     Neural slam: Learning to explore with external memory.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 67/80:
  -> INFO: Now checking 10 results for matching title: 'Mat-agent: Adaptive multi-agent training optimization.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Cai', 'Fan', 'Liu', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Mat-agent:+Adaptive+multi-agent+training+optimization. manually and check the results.
        -> Author(s): Jusheng Zhang, Kaitong Cai, Yijia Fan, Ningyuan Liu, and Keze Wang
        -> Title:     Mat-agent: Adaptive multi-agent training optimization.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 68/80:
  -> INFO: Now checking 10 results for matching title: 'Cf-vlm:counterfactual vision-language fine-tuning.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Cai', 'Fan', 'Wang', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Cf-vlm:counterfactual+vision-language+fine-tuning. manually and check the results.
        -> Author(s): Jusheng Zhang, Kaitong Cai, Yijia Fan, Jian Wang, and Keze Wang
        -> Title:     Cf-vlm:counterfactual vision-language fine-tuning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 69/80:
  -> INFO: Now checking 6 results for matching title: 'Learning dynamics of vlm finetuning.'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Cai', 'Yang', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Learning+dynamics+of+vlm+finetuning. manually and check the results.
        -> Author(s): Jusheng Zhang, Kaitong Cai, Jing Yang, and Keze Wang
        -> Title:     Learning dynamics of vlm finetuning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 70/80:
  -> INFO: Now checking 10 results for matching title: 'Failure-driven workflow refinement.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Cai', 'Zeng', 'Liu', 'Fan', 'Chen', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Failure-driven+workflow+refinement. manually and check the results.
        -> Author(s): Jusheng Zhang, Kaitong Cai, Qinglin Zeng, Ningyuan Liu, Stephen Fan, Ziliang Chen, and Keze Wang
        -> Title:     Failure-driven workflow refinement.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 71/80:
  -> INFO: Now checking 1 results for matching title: 'Drdiff: Dynamic routing diffusion with hierarchical attention for breaking the efficiency-quality trade-off.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Fan', 'Cai', 'Huang', 'Sun', 'Wang', 'Tang', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Drdiff:+Dynamic+routing+diffusion+with+hierarchical+attention+for+breaking+the+efficiency-quality+trade-off. manually and check the results.
        -> Author(s): Jusheng Zhang, Yijia Fan, Kaitong Cai, Zimeng Huang, Xiaofei Sun, Jian Wang, Chengpei Tang, and Keze Wang
        -> Title:     Drdiff: Dynamic routing diffusion with hierarchical attention for breaking the efficiency-quality trade-off.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 72/80:
  -> INFO: Now checking 6 results for matching title: 'Osc: Cognitive orchestration through dynamic knowledge alignment in multi-agent llm collaboration.'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Fan', 'Cai', 'Sun', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Osc:+Cognitive+orchestration+through+dynamic+knowledge+alignment+in+multi-agent+llm+collaboration. manually and check the results.
        -> Author(s): Jusheng Zhang, Yijia Fan, Kaitong Cai, Xiaofei Sun, and Keze Wang
        -> Title:     Osc: Cognitive orchestration through dynamic knowledge alignment in multi-agent llm collaboration.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 73/80:
  -> INFO: Now checking 10 results for matching title: 'Kolmogorov-arnold fourier networks.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Fan', 'Cai', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Kolmogorov-arnold+fourier+networks. manually and check the results.
        -> Author(s): Jusheng Zhang, Yijia Fan, Kaitong Cai, and Keze Wang
        -> Title:     Kolmogorov-arnold fourier networks.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 74/80:
  -> INFO: Now checking 1 results for matching title: 'Gam-agent: Game-theoretic and uncertainty-aware collaboration for complex visual reasoning.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Fan', 'Lin', 'Chen', 'Jiang', 'Chai', 'Wang', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gam-agent:+Game-theoretic+and+uncertainty-aware+collaboration+for+complex+visual+reasoning. manually and check the results.
        -> Author(s): Jusheng Zhang, Yijia Fan, Wenjun Lin, Ruiqi Chen, Haoyi Jiang, Wenhao Chai, Jian Wang, and Keze Wang
        -> Title:     Gam-agent: Game-theoretic and uncertainty-aware collaboration for complex visual reasoning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 75/80:
  -> INFO: Now checking 1 results for matching title: 'Kabb: Knowledge-aware bayesian bandits for dynamic expert coordination in multi-agent systems.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Huang', 'Fan', 'Liu', 'Li', 'Yang', 'Yao', 'Wang', 'Wang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Kabb:+Knowledge-aware+bayesian+bandits+for+dynamic+expert+coordination+in+multi-agent+systems. manually and check the results.
        -> Author(s): Jusheng Zhang, Zimeng Huang, Yijia Fan, Ningyuan Liu, Mingyan Li, Zhuojie Yang, Jiawei Yao, Jian Wang, and Keze Wang
        -> Title:     Kabb: Knowledge-aware bayesian bandits for dynamic expert coordination in multi-agent systems.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 76/80:
  -> INFO: Now checking 10 results for matching title: 'Pointclip: Point cloud understanding by clip.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Guo', 'Zhang', 'Li', 'Miao', 'Cui', 'Qiao', 'Gao', 'Li', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Pointclip:+Point+cloud+understanding+by+clip. manually and check the results.
        -> Author(s): Renrui Zhang, Ziyu Guo, Wei Zhang, Kunchang Li, Xupeng Miao, Bin Cui, Yu Qiao, Peng Gao, and Hongsheng Li
        -> Title:     Pointclip: Point cloud understanding by clip.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 77/80:
  -> INFO: Now checking 10 results for matching title: 'Reward-reinforced generative adversarial networks for multi-agent systems'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 78/80:
  -> INFO: Now checking 10 results for matching title: 'Self-adaptive neural module transformer for visual question answering'
       -> INFO: All authors matched!
- Checking reference 79/80:
  -> INFO: Now checking 10 results for matching title: 'Uni3d: Exploring unified 3d representation at scale.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhou', 'Wang', 'Ma', 'Liu', 'Huang', 'Wang', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Uni3d:+Exploring+unified+3d+representation+at+scale. manually and check the results.
        -> Author(s): Junsheng Zhou, Jinsheng Wang, Baorui Ma, Yu-Shen Liu, Tiejun Huang, and Xinlong Wang
        -> Title:     Uni3d: Exploring unified 3d representation at scale.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 80/80:
  -> INFO: Now checking 10 results for matching title: 'Towards automatic learning of procedures from web instructional videos.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhou', 'Xu', 'Corso', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Towards+automatic+learning+of+procedures+from+web+instructional+videos. manually and check the results.
        -> Author(s): Luowei Zhou, Chenliang Xu, and Jason J Corso
        -> Title:     Towards automatic learning of procedures from web instructional videos.
        -> Year:      2017
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 5: si := (1 −α) · Sconf,i + α · wi, where α ∈[0, 1] controls the balance between text similarity and
-> Invalid unicode use found on p. 5: (na−1),ˆra+ra
-> Invalid unicode use found on p. 16: view based on the highest composite score si = (1 −α) · Sconf,i + α · wi (detailed in
-> Invalid unicode use found on p. 25: −(α−µ1)2
-> Invalid unicode use found on p. 25: −(α−µ2)2
-> Invalid unicode use found on p. 25: −(α −µ1)2
-> Invalid unicode use found on p. 25: −(α −µ2)2
-> Invalid unicode use found on p. 25: (α −µ2)2
-> Invalid unicode use found on p. 25: −(α −µ1)2
-> Invalid unicode use found on p. 25: −1
-> Invalid unicode use found on p. 25: −µ2
-> Invalid unicode use found on p. 25: −µ2
-> Invalid unicode use found on p. 25: −2 ln
-> Invalid unicode use found on p. 25: 0.152 −
-> Invalid unicode use found on p. 25: 0.12 = 44.44 −100 = −55.56,
-> Invalid unicode use found on p. 25: 0.12 −0.35
-> Invalid unicode use found on p. 25: = 2(65 −15.56) = 98.89,
-> Invalid unicode use found on p. 25: 0.152 −0.652
-> Invalid unicode use found on p. 25: 0.12 −2 ln
-> Invalid unicode use found on p. 25: = 5.4444 −42.25 −2(0.4055) = −37.6166.
-> Invalid unicode use found on p. 26: α = −B ±
-> Invalid unicode use found on p. 26: B2 −4AC
-> Invalid unicode use found on p. 26: ∆= 98.892 −4(−55.56)(−37.6166) = 1425.4625,
-> Invalid unicode use found on p. 28: Theoretically, α = 0.557 balances partially overlapping distributions (µ1 −µ2 = 0.3 <
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 626 sentences on 10 pages -> Avg. of 70.55555555555556 sentences per page
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
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
  // LLM calling counter = 3
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
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 5
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
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
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
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 77 (Ref. ID = 78); Skipping LLM check...
-> Missing an abstract for reference with index 78 (Ref. ID = 79); Skipping LLM check...
-> Missing an abstract for reference with index 79 (Ref. ID = 80); Skipping LLM check...
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
  -> Found 1 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 19 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 8
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 9
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 10
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 11
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 12
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\42 Tri-Modal\PAU_results.md
```