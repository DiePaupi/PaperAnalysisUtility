
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\32 Towards Multiscale Graph-based Protein Learning\Towards Multiscale Graph-based Protein Learning.pdf"
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
- Found following heading '2 - Background' on page 3
- Found following heading '3 - Hierarchical Graph Representations for Proteins' on page 4
- Found following heading '4 - A Two-Stage GNN Architecture for Multiscale Protein Modeling' on page 6
- Found following heading '5 - Numerical Experiments' on page 7
- Found following heading '6 - Concluding Remarks' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Missing proofs' on page 21
- Found following appendix 'B - Construction of Local Frames' on page 23
- Found following appendix 'C - SCHull Graphs' on page 23
- Found following appendix 'D - DSSP Algorithm' on page 24
- Found following appendix 'E - Additional Experiments Details' on page 24
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 21
All found references: 48
-> Warning: Could not parse year in reference 'AI21 Labs. Jamba: Open source hybrid ssm + transformer llm.'!
-> Warning: Could not parse year in reference 'Perrakis Group. Dssp: Define secondary structure of proteins.'!
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                               link  valid
0       1                                  Luciano A Abriata  ...                                                      None
1       2  Justin Baker, Shih-Hsin Wang, Tommaso de Ferne...  ...                                                      None
2       3  C  Bradford Barber, David P  Dobkin, and Hannu...  ...                                                      None
3       4  Helen M Berman, John Westbrook, Zukang Feng, G...  ...                                                      None
4       5  Byron Caughey, Heidi G Standke, Efrosini Artik...  ...                                                      None
5       6  Jose M Dana, Aleksandras Gutmanas, Nidhi Tyagi...  ...                                                      None
6       7  Tri Dao, Shizhe Ma, Wenxuan Sun, Albert Gu, Sa...  ...                                                      None
7       8  Weitao Du, He Zhang, Yuanqi Du, Qi Meng, Wei C...  ...                                                      None
8       9  Yuanqi Du, Limei Wang, Dieqiao Feng, Guifeng W...  ...                                                      None
9      10                    Matthias Fey and Jan E  Lenssen  ...                                                      None
10     11  Johannes Gasteiger, Florian Becker, and Stepha...  ...                                                      None
11     12  Vladimir Gligorijevi´c, P Douglas Renfrew, Tom...  ...                                                      None
12     13                              Albert Gu and Tri Dao  ...                                                      None
13     14  Pedro Hermosilla, Marco Schäfer, Matˇej Lang, ...  ...                                                      None
14     15         Jie Hou, Badri Adhikari, and Jianlin Cheng  ...                                                      None
15     16  Bozhen Hu, Cheng Tan, Yongjie Xu, Zhangyang Ga...  ...                                                      None
16     17  Bowen Jing, Stephan Eismann, Pratham N Soni, a...  ...                                                      None
17     18  Bowen Jing, Stephan Eismann, Patricia Suriana,...  ...                                                      None
18     19  Chaitanya K Joshi, Cristian Bodnar, Simon V Ma...  ...                                                      None
19     20  John Jumper, Richard Evans, Alexander Pritzel,...  ...                                                      None
20     21               Wolfgang Kabsch and Christian Sander  ...                                                      None
21     22                     Thomas N  Kipf and Max Welling  ...                                                      None
22     23  Allison Kraus, Forrest Hoyt, Cindi L Schwartz,...  ...                                                      None
23     24  Allison Kraus, Forrest Hoyt, Cindi L Schwartz,...  ...                                                      None
24     25                                          AI21 Labs  ...       https://www.ai21.com/blog/introducing-jamba,   None
25     26                                          Jiahan Li  ...                                                      None
26     27  Zhihai Liu, Yan Li, Li Han, Jie Li, Jie Liu, Z...  ...                                                      None
27     28  Christopher Morris, Martin Ritzert, Matthias F...  ...                                                      None
28     29  Marina V Omelchenko, Michael Y Galperin, Yuri ...  ...                                                      None
29     30                                     Perrakis Group  ...                    https://pdb-redo.eu/dssp/about.   None
30     31  Ruijie Quan, Wenguan Wang, Fan Ma, Hehe Fan, a...  ...                                                      None
31     32  Roshan Rao, Nicholas Bhattacharya, Neil Thomas...  ...                                                      None
32     33  Vignesh Ram Somnath, Charlotte Bunne, and Andr...  ...                                                      None
33     34  Wenxuan Sun, Tri Dao, Hongyu Zhuang, Zihang Da...  ...                                                      None
34     35  Wouter G Touw, Coos Baakman, Jon Black, Tim AH...  ...                                                      None
35     36      Chao Wang, Hehe Fan, Ruijie Quan, and Yi Yang  ...                                                      None
36     37  Limei Wang, Haoran Liu, Yi Liu, Jerry Kurtin, ...  ...                                                      None
37     38  Limei Wang, Yi Liu, Yuchao Lin, Haoran Liu, an...  ...                                                      None
38     39  Renxiao Wang, Xueliang Fang, Yipin Lu, and Sha...  ...                                                      None
39     40  Shih-Hsin Wang, Yung-Chang Hsu, Justin Baker, ...  ...                                                      None
40     41  Shih-Hsin Wang, Yuhao Huang, Justin M Baker, Y...  ...                                                      None
41     42  Joseph L Watson, David Juergens, Nathaniel R B...  ...                                                      None
42     43             Fang Wu, Dragomir Radev, and Stan Z Li  ...                                                      None
43     44  Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefa...  ...                                                      None
44     45  Minghao Xu, Xinyu Yuan, Santiago Miret, and Ji...  ...                                                      None
45     46                       Zhaoning Yu and Hongyang Gao  ...                                                      None
46     47  Zuobai Zhang, Pascal Notin, Yining Huang, Auré...  ...                                                      None
47     48  Zuobai Zhang, Minghao Xu, Arian Jamasb, Vijil ...  ...  https://nips.cc/public/guides/CodeSubmissionPo...   None

[48 rows x 10 columns]
- Checking reference 1/48:
  -> INFO: Now checking 1 results for matching title: 'The Nobel Prize in chemistry: past, present, and future of AI in biology'
       -> INFO: All authors matched!
- Checking reference 2/48:
  -> INFO: Now checking 2 results for matching title: 'An explicit frame construction for normalizing 3D point clouds'
       -> INFO: All authors matched!
- Checking reference 3/48:
  -> INFO: Now checking 10 results for matching title: 'The quickhull algorithm for convex hulls'
       -> INFO: All authors matched!
- Checking reference 4/48:
  -> INFO: Now checking 10 results for matching title: 'The protein data bank'
       -> INFO: All authors matched!
- Checking reference 5/48:
  -> INFO: Now checking 10 results for matching title: 'Pathogenic prion structures at high resolution'
       -> INFO: All authors matched!
- Checking reference 6/48:
  -> INFO: Now checking 1 results for matching title: 'Sifts: updated structure integration with function, taxonomy and sequences resource allows 40-fold increase in coverage of structure-based annotations for proteins'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/48:
  -> INFO: Now checking 10 results for matching title: 'An empirical study of state space models for large language modeling'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Dao', 'Ma', 'Sun', 'Gu', 'Smith', 'Kyrola', 'Manning', 'Re', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=An+empirical+study+of+state+space+models+for+large+language+modeling manually and check the results.
        -> Author(s): Tri Dao, Shizhe Ma, Wenxuan Sun, Albert Gu, Sam Smith, Aapo Kyrola, Christopher D Manning, and Christopher Re
        -> Title:     An empirical study of state space models for large language modeling
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 8/48:
  -> INFO: Now checking 4 results for matching title: 'Se (3) equivariant graph neural networks with complete local frames'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 7)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/48:
  -> INFO: Now checking 1 results for matching title: 'A new perspective on building efficient and expressive 3d equivariant graph neural networks'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 8)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/48:
  -> INFO: Now checking 10 results for matching title: 'Fast graph representation learning with PyTorch Geometric'
       -> INFO: All authors matched!
- Checking reference 11/48:
  -> INFO: Now checking 2 results for matching title: 'Gemnet: Universal directional graph neural networks for molecules'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Klicpera, Gunnemann'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/48:
  -> INFO: Now checking 10 results for matching title: 'Structure-based protein function prediction using graph convolutional networks'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 9)
                   Unmatched authors = 'Gligorijević, Xavier, Knight, Cho, Bonneau'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/48:
  -> INFO: Now checking 10 results for matching title: 'Mamba: Linear-time sequence modeling with selective state spaces'
       -> INFO: All authors matched!
- Checking reference 14/48:
  -> INFO: Now checking 2 results for matching title: 'Intrinsic-extrinsic convolution and pooling for learning on 3d protein structures'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 15/48:
  -> INFO: Now checking 6 results for matching title: 'Deepsf: deep convolutional neural network for mapping protein sequences to folds'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/48:
  -> INFO: Now checking 7 results for matching title: 'Protgo: Function-guided protein modeling for unified representation learning'
       -> INFO: All authors matched!
- Checking reference 17/48:
  -> INFO: Now checking 10 results for matching title: 'Equivariant graph neural networks for 3d macromolecular structure'
       -> INFO: All authors matched!
- Checking reference 18/48:
  -> INFO: Now checking 10 results for matching title: 'Learning from protein structure with geometric vector perceptrons'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 19/48:
  -> INFO: Now checking 1 results for matching title: 'On the expressive power of geometric graph neural networks'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/48:
  -> INFO: Now checking 10 results for matching title: 'Highly accurate protein structure prediction with AlphaFold'
       -> WARNING: Not all 34 authors from the found ref. were matched (only 33)
                   Unmatched authors = 'Romera-Paredes'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 21/48:
  -> INFO: Now checking 1 results for matching title: 'Dictionary of protein secondary structure: Pattern recognition of hydrogen-bonded and geometrical features'
       -> INFO: All authors matched!
- Checking reference 22/48:
  -> INFO: Now checking 10 results for matching title: 'Semi-supervised classification with graph convolutional networks'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 23/48:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Highresolution structure and strain comparison of infectious mammalian prions
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Kraus', 'Hoyt', 'Schwartz', 'Hansen', 'Artikis', 'Hughson', 'Raymond', 'Race', 'Baron', 'Caughey', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Highresolution+structure+and+strain+comparison+of+infectious+mammalian+prions manually and check the results.
        -> Author(s): Allison Kraus, Forrest Hoyt, Cindi L Schwartz, Bryan Hansen, Efrosini Artikis, Andrew G Hughson, Gregory J Raymond, Brent Race, Gerald S Baron, and Byron Caughey
        -> Title:     Highresolution structure and strain comparison of infectious mammalian prions
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 24/48:
  -> INFO: Now checking 10 results for matching title: 'Structure of an infectious mammalian prion'
       -> INFO: All authors matched!
- Checking reference 25/48:
  -> Checking if provided link is pingable: https://www.ai21.com/blog/introducing-jamba,
  -> INFO: Now checking 10 results for matching title: 'Jamba: Open source hybrid ssm + transformer llm'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 324 results for matching title: 'Jamba: Open source hybrid ssm + transformer llm'
  -> WARNING: None of the 324 results matched the expected title!
     -> You could also open https://www.ai21.com/blog/introducing-jamba, manually and check the results.
        -> Author(s): AI21 Labs
        -> Title:     Jamba: Open source hybrid ssm + transformer llm
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 26/48:
  -> INFO: Now checking 10 results for matching title: 'Directed weight neural networks for protein structure representation learning'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Directed weight neural networks for protein structure representation learning'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Directed+weight+neural+networks+for+protein+structure+representation+learning manually and check the results.
        -> Author(s): Jiahan Li
        -> Title:     Directed weight neural networks for protein structure representation learning
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 27/48:
  -> INFO: Now checking 1 results for matching title: 'Pdb-wide collection of binding data: current status of the pdbbind database'
       -> INFO: All authors matched!
- Checking reference 28/48:
  -> INFO: Now checking 10 results for matching title: 'Weisfeiler and leman go neural: Higher-order graph neural networks'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/48:
  -> INFO: Now checking 2 results for matching title: 'Nonhomologous isofunctional enzymes: a systematic analysis of alternative solutions in enzyme evolution'
  -> WARNING: None of the 2 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Omelchenko', 'Galperin', 'Wolf', 'Koonin', '2010']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Nonhomologous+isofunctional+enzymes:+a+systematic+analysis+of+alternative+solutions+in+enzyme+evolution manually and check the results.
        -> Author(s): Marina V Omelchenko, Michael Y Galperin, Yuri I Wolf, and Eugene V Koonin
        -> Title:     Nonhomologous isofunctional enzymes: a systematic analysis of alternative solutions in enzyme evolution
        -> Year:      2010
     -> Manual search was skipped by the user.
- Checking reference 30/48:
  -> Checking if provided link is pingable: https://pdb-redo.eu/dssp/about.
  -> INFO: Now checking 10 results for matching title: 'Dssp: Define secondary structure of proteins'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Group', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dssp:+Define+secondary+structure+of+proteins manually and check the results.
        -> Author(s): Perrakis Group
        -> Title:     Dssp: Define secondary structure of proteins
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 31/48:
  -> INFO: Now checking 10 results for matching title: 'Clustering for protein representation learning'
       -> INFO: All authors matched!
- Checking reference 32/48:
  -> INFO: Now checking 10 results for matching title: 'Evaluating protein transfer learning with tape.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Rao', 'Bhattacharya', 'Thomas', 'Duan', 'Chen', 'Canny', 'Abbeel', 'Song', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Evaluating+protein+transfer+learning+with+tape. manually and check the results.
        -> Author(s): Roshan Rao, Nicholas Bhattacharya, Neil Thomas, Yan Duan, Xi Chen, John Canny, Pieter Abbeel, and Yun S  Song
        -> Title:     Evaluating protein transfer learning with tape.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 33/48:
  -> INFO: Now checking 10 results for matching title: 'Multi-scale representation learning on proteins'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/48:
  -> INFO: Now checking 6 results for matching title: 'Llamba: Efficient llms with mamba-based distillation'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sun', 'Dao', 'Zhuang', 'Dai', 'Gu', 'Manning', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Llamba:+Efficient+llms+with+mamba-based+distillation manually and check the results.
        -> Author(s): Wenxuan Sun, Tri Dao, Hongyu Zhuang, Zihang Dai, Albert Gu, and Christopher D Manning
        -> Title:     Llamba: Efficient llms with mamba-based distillation
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 35/48:
  -> INFO: Now checking 1 results for matching title: 'A series of pdb-related databanks for everyday needs'
       -> INFO: All authors matched!
       -> WARNING: Year (2014) does not match expected year (2015)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 36/48:
  -> INFO: Now checking 10 results for matching title: 'Protchatgpt: Towards understanding proteins with large language models'
       -> INFO: All authors matched!
- Checking reference 37/48:
  -> INFO: Now checking 10 results for matching title: 'Learning hierarchical protein representations via complete 3d graph networks'
       -> INFO: All authors matched!
- Checking reference 38/48:
  -> INFO: Now checking 2 results for matching title: 'Comenet: Towards complete and efficient message passing for 3d molecular graphs'
       -> INFO: All authors matched!
- Checking reference 39/48:
  -> INFO: Now checking 1 results for matching title: 'The pdbbind database: Collection of binding affinities for protein- ligand complexes with known three-dimensional structures'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Fang', 'Lu', 'Wang', '2004']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+pdbbind+database:+Collection+of+binding+affinities+for+protein-+ligand+complexes+with+known+three-dimensional+structures manually and check the results.
        -> Author(s): Renxiao Wang, Xueliang Fang, Yipin Lu, and Shaomeng Wang
        -> Title:     The pdbbind database: Collection of binding affinities for protein- ligand complexes with known three-dimensional structures
        -> Year:      2004
     -> Manual search was skipped by the user.
- Checking reference 40/48:
  -> INFO: Now checking 1 results for matching title: 'Rethinking the benefits of steerable features in 3d equivariant graph neural networks'
       -> INFO: All authors matched!
- Checking reference 41/48:
  -> INFO: Now checking 1 results for matching title: 'A theoretically-principled sparse, connected, and rigid graph representation of molecules'
       -> INFO: All authors matched!
- Checking reference 42/48:
  -> INFO: Now checking 1 results for matching title: 'De novo design of protein structure and function with rfdiffusion'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 43/48:
  -> INFO: Now checking 2 results for matching title: 'Molformer: Motif-based transformer on 3d heterogeneous molecular graphs'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zhang, Cui, Zhang, Xing, Zhang, Chen'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 44/48:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: How powerful are graph neural networks? In International Conference on Learning Representations.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Xu', 'Hu', 'Leskovec', 'Jegelka', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=How+powerful+are+graph+neural+networks?+In+International+Conference+on+Learning+Representations. manually and check the results.
        -> Author(s): Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka
        -> Title:     How powerful are graph neural networks? In International Conference on Learning Representations.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 45/48:
  -> INFO: Now checking 2 results for matching title: 'Protst: Multi-modality learning of protein sequences and biomedical texts'
       -> INFO: All authors matched!
- Checking reference 46/48:
  -> INFO: Now checking 10 results for matching title: 'Molecular representation learning via heterogeneous motif graph neural networks'
       -> INFO: All authors matched!
- Checking reference 47/48:
  -> INFO: Now checking 10 results for matching title: 'Multi-scale representation learning for protein fitness prediction'
       -> INFO: All authors matched!
- Checking reference 48/48:
  -> Checking if provided link is pingable: https://nips.cc/public/guides/CodeSubmissionPolicy)
  -> INFO: Now checking 10 results for matching title: 'Protein representation learning by geometric structure pretraining'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 6: for t = 0, 1, . . . , T1 −1,
-> Invalid unicode use found on p. 6: for t = 0, 1, . . . , T2 −1,
-> Invalid unicode use found on p. 20: constructs a geometric graph with at most 3m −6 edges [41]. For the remaining cases, when m = 1,
-> Invalid unicode use found on p. 20: 3|Si| −6
-> Invalid unicode use found on p. 20: 3|Si| −6
-> Invalid unicode use found on p. 20: N −|J1| −2|J2|
-> Invalid unicode use found on p. 20: −6|J≥3|
-> Invalid unicode use found on p. 20: N −|J1| −|J2| −|J≥3|
-> Invalid unicode use found on p. 20: ≤3(N −I).
-> Invalid unicode use found on p. 20: |E| ≤3I −6.
-> Invalid unicode use found on p. 20: |Ei| ≤(3I −6) + 3(N −I) = 3N −6 < 3N.
-> Invalid unicode use found on p. 22: x −x
-> Invalid unicode use found on p. 22: ∥x −x∥,
-> Invalid unicode use found on p. 23: the edge attributes of (i, j) : (∥xi −xj∥, τij) for any (i, j) ∈E, and
-> Invalid unicode use found on p. 23: the node attributes : ∥xi −x∥for any i ∈V.
-> Invalid unicode use found on p. 23: connected with edges that satisfy |E| ≤3N −6 when N = |V| ≥3 (cf. [41, Proposition 3.1]). (2)
-> Invalid unicode use found on p. 23: r(CH) −
-> Invalid unicode use found on p. 23: r(OH) −
-> Invalid unicode use found on p. 23: is considered to exist at residue i if Hbond(i, i + n) is present. A bridge may exist between two nonoverlapping stretches of three residues each. A parallel bridge is said to be present if Hbond(i −1, j)
-> Invalid unicode use found on p. 23: and Hbond(j, i + 1) or if Hbond(j −1, i) and Hbond(i, j + 1). An antiparallel bridge is said to be
-> Invalid unicode use found on p. 23: present if Hbond(i, j) and Hbond(j, i) or if Hbond(i −1, j + 1) and Hbond(j −1, i + 1).
-> Invalid unicode use found on p. 23: i −Cα
-> Invalid unicode use found on p. 23: i−2 and Cα
-> Invalid unicode use found on p. 23: i+2 −Cα
-> Invalid unicode use found on p. 24: binding affinity pK = −log10(K) in molar units.
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 459 sentences on 11 pages -> Avg. of 46.9 sentences per page
-> Warning: Reference '2' never used in the document's text.
-> Warning: Reference '3' never used in the document's text.
-> Warning: Reference '4' never used in the document's text.
-> Warning: Reference '6' never used in the document's text.
-> Warning: Reference '7' never used in the document's text.
-> Warning: Reference '25' never used in the document's text.
-> Warning: Reference '30' never used in the document's text.
-> Warning: Reference '34' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> WARNING: Reference with index 5 (Ref. ID = 6) has no associated sentence!
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
-> Missing an abstract for reference with index 40 (Ref. ID = 41); Skipping LLM check...
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
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
  -> Found 6 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 5 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 160 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 14
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 15
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 16
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 17
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 18
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\32 Towards Multiscale Graph-based Protein Learning\PAU_results.md
```