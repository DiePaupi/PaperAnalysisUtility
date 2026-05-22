
```
Enter the path to the PDF file: "C:\Users\pauli\Sciebo\Paupis_Privatstuff\PhD_Notes\Paper-Projekte\PQC\PAU - All  GPTZero NeurIPS Paper with H\48 Learning the Wrong Lessons Syntactic-Domain Spurious Correlations\Learning the Wrong Lessons Syntactic-Domain Spurious Correlations in.pdf"
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
- Found following heading '2 - Syntactic-Domain Spurious Correlations' on page 2
- Found following heading '3 - Synthetic Dataset: Entity-Pair Syntactic Domains' on page 4
- Found following heading '4 - Measuring Reliance on Syntactic–Domain Spurious Correlation' on page 6
- Found following heading '5 - Syntactic-Domain Reliance in Open and Closed-Source LLMs' on page 7
- Found following heading '6 - Case Study: Bypassing Answer Refusals' on page 8
- Found following heading '7 - Related Work' on page 10
- Found following heading '8 - Discussion & Limitations' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Part-of-Speech Tag Legend' on page 20
- Found following appendix 'B - Unintended Instruction Taxonomy' on page 20
- Found following appendix 'C - Example Instantiations' on page 20
- Found following appendix 'D - Finetuning Details' on page 20
- Found following appendix 'E - Additional Results' on page 22
- Found following appendix 'F - Bypassing Answer Refusals (Continued)' on page 25
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 20
All found references: 42
-> Warning: Malformed author string: 'OpenAI'
-> Warning: Malformed author string: ':'
-> Warning: Malformed author string: 'Shuaiqi'
-> Warning: Malformed author string: 'Xia'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                               link  valid
0       1                            E Akyurek and J Andreas  ...                                                      None
1       2  M Arjovsky, L Bottou, I Gulrajani, and D Lopez...  ...                                                      None
2       3       H Bahng, S Chun, Y Yoo, J Choo, and S J H Oh  ...                                                      None
3       4            B Cao, D Cai, Z Zhang, Y Zou, and W Lam  ...                                                      None
4       5                                 H Chen and P Singh  ...                                                      None
5       6                         L Chen, J Wang, and M Zhao  ...                                                      None
6       7                                          N Chomsky  ...                                                      None
7       8                                          N Chomsky  ...                                                      None
8       9  H Elsahar, P Vougiouklis, A Remaci, C Gravier,...  ...                                                      None
9      10  L Fang, X Yu, J Cai, Y Chen, S Wu, Z Liu, Z Ya...  ...                                                      None
10     11                            M Garcia and A Thompson  ...                                                      None
11     12           R Geirhos, P Rubisch, C Michaelis, et al  ...                                                      None
12     13                                       A E Goldberg  ...                                                      None
13     14  S Gururangan, A Marasovi´c, S Swayamdipta, K L...  ...                                                      None
14     15         S Gururangan, S Swayamdipta, O Levy, et al  ...                                                      None
15     16               D Hendrycks, K Zhao, S Basart, et al  ...                                                      None
16     17  P Izmailov, P Kirichenko, N Gruver, and A G Wi...  ...                                                      None
17     18                                   B Jha and U Puri  ...                                                      None
18     19  L Jiang, K Rao, S Han, A Ettinger, F Brahman, ...  ...                                                      None
19     20                       D Ju, H Blix, and A Williams  ...                                                      None
20     21  N Lambert, J Morrison, V Pyatkin, S Huang, H I...  ...                                                      None
21     22  N Lambert, J Morrison, V Pyatkin, S Huang, H I...  ...                                                      None
22     23  S Longpre, L Hou, T Vu, A Webson, H W Chung, Y...  ...                                                      None
23     24                 R T McCoy, E Pavlick, and T Linzen  ...                                                      None
24     25                 R T McCoy, E Pavlick, and T Linzen  ...                                                      None
25     26      V Moskvoretskii, A Panchenko, and I Nikishina  ...                                                      None
26     27           K Nikoli´c, L Sun, J Zhang, and F Tramèr  ...                                                      None
27     28  T OLMo, P Walsh, L Soldaini, D Groeneveld, K L...  ...                                                      None
28     29  OpenAI, :, A Hurst, A Lerer, A P Goucher, A Pe...  ...                                                      None
29     30  A Poliak, J Naradowsky, A Haldar, R Rudinger, ...  ...                                                      None
30     31  X Qi, A Panda, K Lyu, X Ma, S Roy, A Beirami, ...  ...                                                      None
31     32        S Sagawa, P W Koh, T Hashimoto, and P Liang  ...                                                      None
32     33      S Sagawa, A Raghunathan, P W Koh, and P Liang  ...                                                      None
33     34         C Shaib, Y Elazar, J J Li, and B C Wallace  ...                                                      None
34     35                               S Singla and S Feizi  ...                                                      None
35     36                                J Smith and A Patel  ...                                                      None
36     37  L Soldaini, R Kinney, A Bhagia, D Schwenk, D A...  ...                                                      None
37     38                    J Sun, C Shaib, and B C Wallace  ...                                                      None
38     39          M Sun, Y Yin, Z Xu, J Z Kolter, and Z Liu  ...                                                      None
39     40         S Wadhwa, C Shaib, S Amir, and B C Wallace  ...                                                      None
40     41                             A Webson and E Pavlick  ...                                                      None
41     42                         W Zhang, M Liu, and L Chen  ...  https://nips.cc/public/guides/CodeSubmissionPo...   None

[42 rows x 10 columns]
- Checking reference 1/42:
  -> INFO: Now checking 1 results for matching title: 'LexSym: Compositionality as lexical symmetry'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Akyürek'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/42:
  -> INFO: Now checking 10 results for matching title: 'Invariant risk minimization'
       -> INFO: All authors matched!
- Checking reference 3/42:
  -> INFO: Now checking 10 results for matching title: 'Learning de-biased representations with biased representations'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Yun'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/42:
  -> INFO: Now checking 5 results for matching title: 'On the worst prompt performance of large language models'
       -> INFO: All authors matched!
- Checking reference 5/42:
  -> INFO: Now checking 10 results for matching title: 'Accelerating scientific discoveries using llms'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 136 results for matching title: 'Accelerating scientific discoveries using llms'
  -> WARNING: None of the 136 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Accelerating+scientific+discoveries+using+llms manually and check the results.
        -> Author(s): H Chen and P Singh
        -> Title:     Accelerating scientific discoveries using llms
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 6/42:
  -> INFO: Now checking 4 results for matching title: 'Domain specialization as the key to make large language models effective'
  -> WARNING: None of the 4 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Domain specialization as the key to make large language models effective'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Domain+specialization+as+the+key+to+make+large+language+models+effective manually and check the results.
        -> Author(s): L Chen, J Wang, and M Zhao
        -> Title:     Domain specialization as the key to make large language models effective
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 7/42:
  -> INFO: Now checking 10 results for matching title: 'Syntactic structures'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Syntactic structures'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Syntactic+structures manually and check the results.
        -> Author(s): N Chomsky
        -> Title:     Syntactic structures
        -> Year:      2002
     -> Manual search was skipped by the user.
- Checking reference 8/42:
  -> INFO: Now checking 10 results for matching title: 'Aspects of the Theory of Syntax'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chomsky', '2014']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Aspects+of+the+Theory+of+Syntax manually and check the results.
        -> Author(s): N Chomsky
        -> Title:     Aspects of the Theory of Syntax
        -> Year:      2014
     -> Manual search was skipped by the user.
- Checking reference 9/42:
  -> INFO: Now checking 1 results for matching title: 'T-rex: A large scale alignment of natural language with knowledge base triples'
       -> INFO: All authors matched!
- Checking reference 10/42:
  -> INFO: Now checking 2 results for matching title: 'Knowledge distillation and dataset distillation of large language models: Emerging trends, challenges, and future directions'
       -> WARNING: Not all 24 authors from the found ref. were matched (only 12)
                   Unmatched authors = 'Ma, Ruan, Abbasi, Zhang, Wang, Latif, Zhang, Kolouri, Zhai, Zhu, Zhong, Ma'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/42:
  -> INFO: Now checking 10 results for matching title: 'Applications of llms in legal document analysis'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Garcia', 'Thompson', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Applications+of+llms+in+legal+document+analysis manually and check the results.
        -> Author(s): M Garcia and A Thompson
        -> Title:     Applications of llms in legal document analysis
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 12/42:
  -> INFO: Now checking 5 results for matching title: 'Imagenet-trained cnns are biased towards texture; increasing shape bias improves accuracy and robustness'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/42:
  -> INFO: Now checking 10 results for matching title: 'Usage-based constructionist approaches and large language models'
       -> INFO: All authors matched!
- Checking reference 14/42:
  -> INFO: Now checking 1 results for matching title: 'Don’t stop pretraining: Adapt language models to domains and tasks'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 6)
                   Unmatched authors = 'Marasović'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 15/42:
  -> INFO: Now checking 10 results for matching title: 'Annotation artifacts in natural language inference data'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 16/42:
  -> INFO: Now checking 1 results for matching title: 'Many faces of robustness: A critical analysis of out-of-distribution generalization'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hendrycks', 'Zhao', 'Basart', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Many+faces+of+robustness:+A+critical+analysis+of+out-of-distribution+generalization manually and check the results.
        -> Author(s): D Hendrycks, K Zhao, S Basart, et al
        -> Title:     Many faces of robustness: A critical analysis of out-of-distribution generalization
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 17/42:
  -> INFO: Now checking 2 results for matching title: 'On feature learning in the presence of spurious correlations'
       -> INFO: All authors matched!
- Checking reference 18/42:
  -> INFO: Now checking 1 results for matching title: 'The rosetta paradox: Domain-specific performance inversions in large language models'
       -> INFO: All authors matched!
- Checking reference 19/42:
  -> INFO: Now checking 2 results for matching title: 'Wildteaming at scale: From in-the-wild jailbreaks to (adversarially) safer language models.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jiang', 'Rao', 'Han', 'Ettinger', 'Brahman', 'Kumar', 'Mireshghallah', 'Lu', 'Sap', 'Choi', 'Dziri', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Wildteaming+at+scale:+From+in-the-wild+jailbreaks+to+(adversarially)+safer+language+models. manually and check the results.
        -> Author(s): L Jiang, K Rao, S Han, A Ettinger, F Brahman, S Kumar, N Mireshghallah, X Lu, M Sap, Y Choi, and N Dziri
        -> Title:     Wildteaming at scale: From in-the-wild jailbreaks to (adversarially) safer language models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 20/42:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Domain regeneration: How well do llms match syntactic properties of text domains? arXiv preprint arXiv:2505.07784.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ju', 'Blix', 'Williams', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Domain+regeneration:+How+well+do+llms+match+syntactic+properties+of+text+domains?+arXiv+preprint+arXiv:2505.07784. manually and check the results.
        -> Author(s): D Ju, H Blix, and A Williams
        -> Title:     Domain regeneration: How well do llms match syntactic properties of text domains? arXiv preprint arXiv:2505.07784.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 21/42:
  -> INFO: Now checking 4 results for matching title: 'T\" ulu 3: Pushing frontiers in open language model post-training'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lambert', 'Morrison', 'Pyatkin', 'Huang', 'Ivison', 'Brahman', 'Miranda', 'Liu', 'Dziri', 'Lyu', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=T\"+ulu+3:+Pushing+frontiers+in+open+language+model+post-training manually and check the results.
        -> Author(s): N Lambert, J Morrison, V Pyatkin, S Huang, H Ivison, F Brahman, L J V Miranda, A Liu, N Dziri, S Lyu, et al
        -> Title:     T\" ulu 3: Pushing frontiers in open language model post-training
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 22/42:
  -> INFO: Now checking 2 results for matching title: 'Tulu 3: Pushing frontiers in open language model post-training.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lambert', 'Morrison', 'Pyatkin', 'Huang', 'Ivison', 'Brahman', 'Miranda', 'Liu', 'Dziri', 'Lyu', 'Gu', 'Malik', 'Graf', 'Hwang', 'Yang', 'Bras', 'Tafjord', 'Wilhelm', 'Soldaini', 'Smith', 'Wang', 'Dasigi', 'Hajishirzi', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Tulu+3:+Pushing+frontiers+in+open+language+model+post-training. manually and check the results.
        -> Author(s): N Lambert, J Morrison, V Pyatkin, S Huang, H Ivison, F Brahman, L J V Miranda, A Liu, N Dziri, S Lyu, Y Gu, S Malik, V Graf, J D Hwang, J Yang, R L Bras, O Tafjord, C Wilhelm, L Soldaini, N A Smith, Y Wang, P Dasigi, and H Hajishirzi
        -> Title:     Tulu 3: Pushing frontiers in open language model post-training.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 23/42:
  -> INFO: Now checking 1 results for matching title: 'The flan collection: Designing data and methods for effective instruction tuning'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 24/42:
  -> INFO: Now checking 1 results for matching title: 'Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference'
       -> INFO: All authors matched!
- Checking reference 25/42:
  -> INFO: Now checking 1 results for matching title: 'Right for the wrong reasons: Diagnosing syntactic heuristics in nli models'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['McCoy', 'Pavlick', 'Linzen', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Right+for+the+wrong+reasons:+Diagnosing+syntactic+heuristics+in+nli+models manually and check the results.
        -> Author(s): R T McCoy, E Pavlick, and T Linzen
        -> Title:     Right for the wrong reasons: Diagnosing syntactic heuristics in nli models
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 26/42:
  -> INFO: Now checking 1 results for matching title: 'Are large language models good at lexical semantics? a case of taxonomy learning'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Skoltech'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 27/42:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: The jailbreak tax: How useful are your jailbreak outputs? arXiv preprint arXiv:2504.10694.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Nikoli´c', 'Sun', 'Zhang', 'Tramèr', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+jailbreak+tax:+How+useful+are+your+jailbreak+outputs?+arXiv+preprint+arXiv:2504.10694. manually and check the results.
        -> Author(s): K Nikoli´c, L Sun, J Zhang, and F Tramèr
        -> Title:     The jailbreak tax: How useful are your jailbreak outputs? arXiv preprint arXiv:2504.10694.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 28/42:
  -> INFO: Now checking 10 results for matching title: '2 olmo 2 furious'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 29/42:
  -> INFO: Now checking 10 results for matching title: 'Gpt-4o system card.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['OpenAI', ':', 'Hurst', 'Lerer', 'Goucher', 'Perelman', 'Ramesh', 'Clark', 'Ostrow', 'Welihinda', 'Hayes', 'Radford', '˛adry', 'Baker-Whitcomb', 'Beutel', 'Borzunov', 'Carney', 'Chow', 'Kirillov', 'Nichol', 'Paino', 'Renzin', 'Passos', 'Kirillov', 'Christakis', 'Conneau', 'Kamali', 'Jabri', 'Moyer', 'Tam', 'Crookes', 'Tootoochian', 'Tootoonchian', 'Kumar', 'Vallone', 'Karpathy', 'Braunstein', 'Cann', 'Codispoti', 'Galu', 'Kondrich', 'Tulloch', 'Mishchenko', 'Baek', 'Jiang', 'Pelisse', 'Woodford', 'Gosalia', 'Dhar', 'Pantuliano', 'Nayak', 'Oliver', 'Zoph', 'Ghorbani', 'Leimberger', 'Rossen', 'Sokolowsky', 'Wang', 'Zweig', 'Hoover', 'Samic', 'McGrew', 'Spero', 'Giertler', 'Cheng', 'Lightcap', 'Walkin', 'Quinn', 'Guarraci', 'Hsu', 'Kellogg', 'Eastman', 'Lugaresi', 'Wainwright', 'Bassin', 'Hudson', 'Chu', 'Nelson', 'Li', 'Shern', 'Conger', 'Barette', 'Voss', 'Ding', 'Lu', 'Zhang', 'Beaumont', 'Hallacy', 'Koch', 'Gibson', 'Kim', 'Choi', 'McLeavey', 'Hesse', 'Fischer', 'Winter', 'Czarnecki', 'Jarvis', 'Wei', 'Koumouzelis', 'Sherburn', 'Kappler', 'Levin', 'Levy', 'Carr', 'Farhi', 'Mely', 'Robinson', 'Sasaki', 'Jin', 'Valladares', 'Tsipras', 'Li', 'Nguyen', 'Findlay', 'Oiwoh', 'Wong', 'Asdar', 'Proehl', 'Yang', 'Antonow', 'Kramer', 'Peterson', 'Sigler', 'Wallace', 'Brevdo', 'Mays', 'Khorasani', 'Such', 'Raso', 'Zhang', 'Lohmann', 'Sulit', 'Goh', 'Oden', 'Salmon', 'Starace', 'Brockman', 'Salman', 'Bao', 'Hu', 'Wong', 'Wang', 'Schmidt', 'Whitney', 'Jun', 'Kirchner', 'Pinto', 'Ren', 'Chang', 'Chung', 'Kivlichan', "O'Connell", "O'Connell", 'Osband', 'Silber', 'Sohl', 'Okuyucu', 'Lan', 'Kostrikov', 'Sutskever', 'Kanitscheider', 'Gulrajani', 'Coxon', 'Menick', 'Pachocki', 'Aung', 'Betker', 'Crooks', 'Lennon', 'Kiros', 'Leike', 'Park', 'Kwon', 'Phang', 'Teplitz', 'Wei', 'Wolfe', 'Chen', 'Harris', 'Varavva', 'Lee', 'Shieh', 'Lin', 'Yu', 'Weng', 'Tang', 'Yu', 'Jang', 'Candela', 'Beutler', 'Landers', 'Parish', 'Heidecke', 'Schulman', 'Lachman', 'McKay', 'Uesato', 'Ward', 'Kim', 'Huizinga', 'Sitkin', 'Kraaijeveld', 'Gross', 'Kaplan', 'Snyder', 'Achiam', 'Jiao', 'Lee', 'Zhuang', 'Harriman', 'Fricke', 'Hayashi', 'Singhal', 'Shi', 'Karthik', 'Wood', 'Rimbach', 'Hsu', 'Nguyen', 'Gu-Lemberg', 'Button', 'Liu', 'Howe', 'Muthukumar', 'Luther', 'Ahmad', 'Kai', 'Itow', 'Workman', 'Pathak', 'Chen', 'Jing', 'Guy', 'Fedus', 'Zhou', 'Mamitsuka', 'Weng', 'McCallum', 'Held', 'Ouyang', 'Feuvrier', 'Zhang', 'Kondraciuk', 'Kaiser', 'Hewitt', 'Metz', 'Doshi', 'Aflak', 'Simens', 'Boyd', 'Thompson', 'Dukhan', 'Chen', 'Gray', 'Hudnall', 'Zhang', 'Aljubeh', 'Litwin', 'Zeng', 'Johnson', 'Shetty', 'Gupta', 'Shah', 'Yatbaz', 'Yang', 'Zhong', 'Glaese', 'Chen', 'Janner', 'Lampe', 'Petrov', 'Wu', 'Wang', 'Fradin', 'Pokrass', 'Castro', 'Castro', 'Pavlov', 'Brundage', 'Wang', 'Khan', 'Murati', 'Bavarian', 'Lin', 'Yesildal', 'Soto', 'Gimelshein', 'Cone', 'Staudacher', 'Summers', 'LaFontaine', 'Chowdhury', 'Ryder', 'Stathas', 'Turley', 'Tezak', 'Felix', 'Kudige', 'Keskar', 'Deutsch', 'Bundick', 'Puckett', 'Nachum', 'Okelola', 'Boiko', 'Murk', 'Jaffe', 'Watkins', 'Godement', 'Campbell-Moore', 'Chao', 'McMillan', 'Belov', 'Su', 'Bak', 'Bakkum', 'Deng', 'Dolan', 'Hoeschele', 'Welinder', 'Tillet', 'Pronin', 'Tillet', 'Dhariwal', 'Yuan', 'Dias', 'Lim', 'Arora', 'Troll', 'Lin', 'Lopes', 'Puri', 'Miyara', 'Leike', 'Gaubert', 'Zamani', 'Wang', 'Donnelly', 'Honsby', 'Smith', 'Sahai', 'Ramchandani', 'Huet', 'Carmichael', 'Zellers', 'Chen', 'Chen', 'Nigmatullin', 'Cheu', 'Jain', 'Altman', 'Schoenholz', 'Toizer', 'Miserendino', 'Agarwal', 'Culver', 'Ethersmith', 'Gray', 'Grove', 'Metzger', 'Hermani', 'Jain', 'Zhao', 'Wu', 'Jomoto', 'Wu', 'Shuaiqi', 'Xia', 'Phene', 'Papay', 'Narayanan', 'Coffey', 'Lee', 'Hall', 'Balaji', 'Broda', 'Stramer', 'Xu', 'Gogineni', 'Christianson', 'Sanders', 'Patwardhan', 'Cunninghman', 'Degry', 'Dimson', 'Raoux', 'Shadwell', 'Zheng', 'Underwood', 'Markov', 'Sherbakov', 'Rubin', 'Stasi', 'Kaftan', 'Heywood', 'Peterson', 'Walters', 'Eloundou', 'Qi', 'Moeller', 'Monaco', 'Kuo', 'Fomenko', 'Chang', 'Zheng', 'Zhou', 'Manassra', 'Sheu', 'Zaremba', 'Patil', 'Qian', 'Kim', 'Cheng', 'Zhang', 'He', 'Zhang', 'Jin', 'Dai', 'Malkov', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gpt-4o+system+card. manually and check the results.
        -> Author(s): OpenAI, :, A Hurst, A Lerer, A P Goucher, A Perelman, A Ramesh, A Clark, A Ostrow, A Welihinda, A Hayes, A Radford, A M ˛adry, A Baker-Whitcomb, A Beutel, A Borzunov, A Carney, A Chow, A Kirillov, A Nichol, A Paino, A Renzin, A T Passos, A Kirillov, A Christakis, A Conneau, A Kamali, A Jabri, A Moyer, A Tam, A Crookes, A Tootoochian, A Tootoonchian, A Kumar, A Vallone, A Karpathy, A Braunstein, A Cann, A Codispoti, A Galu, A Kondrich, A Tulloch, A Mishchenko, A Baek, A Jiang, A Pelisse, A Woodford, A Gosalia, A Dhar, A Pantuliano, A Nayak, A Oliver, B Zoph, B Ghorbani, B Leimberger, B Rossen, B Sokolowsky, B Wang, B Zweig, B Hoover, B Samic, B McGrew, B Spero, B Giertler, B Cheng, B Lightcap, B Walkin, B Quinn, B Guarraci, B Hsu, B Kellogg, B Eastman, C Lugaresi, C Wainwright, C Bassin, C Hudson, C Chu, C Nelson, C Li, C J Shern, C Conger, C Barette, C Voss, C Ding, C Lu, C Zhang, C Beaumont, C Hallacy, C Koch, C Gibson, C Kim, C Choi, C McLeavey, C Hesse, C Fischer, C Winter, C Czarnecki, C Jarvis, C Wei, C Koumouzelis, D Sherburn, D Kappler, D Levin, D Levy, D Carr, D Farhi, D Mely, D Robinson, D Sasaki, D Jin, D Valladares, D Tsipras, D Li, D P Nguyen, D Findlay, E Oiwoh, E Wong, E Asdar, E Proehl, E Yang, E Antonow, E Kramer, E Peterson, E Sigler, E Wallace, E Brevdo, E Mays, F Khorasani, F P Such, F Raso, F Zhang, F von Lohmann, F Sulit, G Goh, G Oden, G Salmon, G Starace, G Brockman, H Salman, H Bao, H Hu, H Wong, H Wang, H Schmidt, H Whitney, H Jun, H Kirchner, H P de Oliveira Pinto, H Ren, H Chang, H W Chung, I Kivlichan, I O'Connell, I O'Connell, I Osband, I Silber, I Sohl, I Okuyucu, I Lan, I Kostrikov, I Sutskever, I Kanitscheider, I Gulrajani, J Coxon, J Menick, J Pachocki, J Aung, J Betker, J Crooks, J Lennon, J Kiros, J Leike, J Park, J Kwon, J Phang, J Teplitz, J Wei, J Wolfe, J Chen, J Harris, J Varavva, J G Lee, J Shieh, J Lin, J Yu, J Weng, J Tang, J Yu, J Jang, J Q Candela, J Beutler, J Landers, J Parish, J Heidecke, J Schulman, J Lachman, J McKay, J Uesato, J Ward, J W Kim, J Huizinga, J Sitkin, J Kraaijeveld, J Gross, J Kaplan, J Snyder, J Achiam, J Jiao, J Lee, J Zhuang, J Harriman, K Fricke, K Hayashi, K Singhal, K Shi, K Karthik, K Wood, K Rimbach, K Hsu, K Nguyen, K Gu-Lemberg, K Button, K Liu, K Howe, K Muthukumar, K Luther, L Ahmad, L Kai, L Itow, L Workman, L Pathak, L Chen, L Jing, L Guy, L Fedus, L Zhou, L Mamitsuka, L Weng, L McCallum, L Held, L Ouyang, L Feuvrier, L Zhang, L Kondraciuk, L Kaiser, L Hewitt, L Metz, L Doshi, M Aflak, M Simens, M Boyd, M Thompson, M Dukhan, M Chen, M Gray, M Hudnall, M Zhang, M Aljubeh, M Litwin, M Zeng, M Johnson, M Shetty, M Gupta, M Shah, M Yatbaz, M J Yang, M Zhong, M Glaese, M Chen, M Janner, M Lampe, M Petrov, M Wu, M Wang, M Fradin, M Pokrass, M Castro, M O T de Castro, M Pavlov, M Brundage, M Wang, M Khan, M Murati, M Bavarian, M Lin, M Yesildal, N Soto, N Gimelshein, N Cone, N Staudacher, N Summers, N LaFontaine, N Chowdhury, N Ryder, N Stathas, N Turley, N Tezak, N Felix, N Kudige, N Keskar, N Deutsch, N Bundick, N Puckett, O Nachum, O Okelola, O Boiko, O Murk, O Jaffe, O Watkins, O Godement, O Campbell-Moore, P Chao, P McMillan, P Belov, P Su, P Bak, P Bakkum, P Deng, P Dolan, P Hoeschele, P Welinder, P Tillet, P Pronin, P Tillet, P Dhariwal, Q Yuan, R Dias, R Lim, R Arora, R Troll, R Lin, R G Lopes, R Puri, R Miyara, R Leike, R Gaubert, R Zamani, R Wang, R Donnelly, R Honsby, R Smith, R Sahai, R Ramchandani, R Huet, R Carmichael, R Zellers, R Chen, R Chen, R Nigmatullin, R Cheu, S Jain, S Altman, S Schoenholz, S Toizer, S Miserendino, S Agarwal, S Culver, S Ethersmith, S Gray, S Grove, S Metzger, S Hermani, S Jain, S Zhao, S Wu, S Jomoto, S Wu, Shuaiqi, Xia, S Phene, S Papay, S Narayanan, S Coffey, S Lee, S Hall, S Balaji, T Broda, T Stramer, T Xu, T Gogineni, T Christianson, T Sanders, T Patwardhan, T Cunninghman, T Degry, T Dimson, T Raoux, T Shadwell, T Zheng, T Underwood, T Markov, T Sherbakov, T Rubin, T Stasi, T Kaftan, T Heywood, T Peterson, T Walters, T Eloundou, V Qi, V Moeller, V Monaco, V Kuo, V Fomenko, W Chang, W Zheng, W Zhou, W Manassra, W Sheu, W Zaremba, Y Patil, Y Qian, Y Kim, Y Cheng, Y Zhang, Y He, Y Zhang, Y Jin, Y Dai, and Y Malkov
        -> Title:     Gpt-4o system card.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 30/42:
  -> INFO: Now checking 10 results for matching title: 'Hypothesis only baselines in natural language inference'
       -> INFO: All authors matched!
- Checking reference 31/42:
  -> INFO: Now checking 5 results for matching title: 'Safety alignment should be made more than just a few tokens deep'
       -> INFO: All authors matched!
- Checking reference 32/42:
  -> INFO: Now checking 1 results for matching title: 'Distributionally robust neural networks for group shifts: On the importance of regularization for worst-case generalization'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/42:
  -> INFO: Now checking 10 results for matching title: 'Environment inference for invariant learning'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sagawa', 'Raghunathan', 'Koh', 'Liang', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Environment+inference+for+invariant+learning manually and check the results.
        -> Author(s): S Sagawa, A Raghunathan, P W Koh, and P Liang
        -> Title:     Environment inference for invariant learning
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 34/42:
  -> INFO: Now checking 1 results for matching title: 'Detection and measurement of syntactic templates in generated text'
       -> INFO: All authors matched!
- Checking reference 35/42:
  -> INFO: Now checking 10 results for matching title: 'Understanding attention and generalization in vision transformers'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Singla', 'Feizi', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Understanding+attention+and+generalization+in+vision+transformers manually and check the results.
        -> Author(s): S Singla and S Feizi
        -> Title:     Understanding attention and generalization in vision transformers
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 36/42:
  -> INFO: Now checking 10 results for matching title: 'Leveraging large language models for financial forecasting'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Smith', 'Patel', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Leveraging+large+language+models+for+financial+forecasting manually and check the results.
        -> Author(s): J Smith and A Patel
        -> Title:     Leveraging large language models for financial forecasting
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 37/42:
  -> INFO: Now checking 1 results for matching title: 'Dolma: An open corpus of three trillion tokens for language model pretraining research'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 38/42:
  -> INFO: Now checking 10 results for matching title: 'Evaluating the zero-shot robustness of instruction-tuned language models'
       -> INFO: All authors matched!
- Checking reference 39/42:
  -> INFO: Now checking 10 results for matching title: 'Idiosyncrasies in large language models'
       -> INFO: All authors matched!
- Checking reference 40/42:
  -> INFO: Now checking 1 results for matching title: 'Who taught you that? tracing teachers in model distillation.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wadhwa', 'Shaib', 'Amir', 'Wallace', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Who+taught+you+that?+tracing+teachers+in+model+distillation. manually and check the results.
        -> Author(s): S Wadhwa, C Shaib, S Amir, and B C Wallace
        -> Title:     Who taught you that? tracing teachers in model distillation.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 41/42:
  -> INFO: Now checking 1 results for matching title: 'Do prompt-based models really understand the meaning of their prompts? In ACL.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Webson', 'Pavlick', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Do+prompt-based+models+really+understand+the+meaning+of+their+prompts?+In+ACL. manually and check the results.
        -> Author(s): A Webson and E Pavlick
        -> Title:     Do prompt-based models really understand the meaning of their prompts? In ACL.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 42/42:
  -> Checking if provided link is pingable: https://nips.cc/public/guides/CodeSubmissionPolicy)
  -> INFO: Now checking 7 results for matching title: 'Application of large language models in healthcare: A bibliometric analysis'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Zhao, Song, Wang'
  -> INFO: No perfect match found; taking the next best!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: Ep−∼PSemantic BreakingM(e | p−) + Ep+∼PSemantic PreservingM(e | p+)
-> Invalid unicode use found on p. 2: enumerate semantic-breaking perturbations of each prompt (Ep−∼PSemantic Breaking)
-> Invalid unicode use found on p. 7: 0.36 (∆= −0.33). The ANTONYM and DISFLUENT settings show more modest degradations (e.g.
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 541 sentences on 11 pages -> Avg. of 55.1 sentences per page
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
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
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
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
  // LLM calling counter = 7
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
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
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
  -> Found 2 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 4 matches in this ranking!
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\48 Learning the Wrong Lessons Syntactic-Domain Spurious Correlations\PAU_results.md
```