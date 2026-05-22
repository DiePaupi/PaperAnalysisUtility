
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\12 PANTHER\PANTHER Generative Pretraining Beyond Language.pdf"
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
- Found following heading '3 - PANTHER' on page 3
- Found following heading '4 - Experiments' on page 6
- Found following heading '5 - Conclusions' on page 10
=> Found references/literature section on page 10
- Found first appendix 'A - Notation Table' on page 13
- Found following appendix 'B - Implementation Details' on page 14
- Found following appendix 'C - Transferability of PANTHER' on page 15
- Found following appendix 'D - Ablation Experiments' on page 15
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 13
All found references: 29
-> Warning: Malformed author string: 'GroupLens'
-> Warning: Malformed author string: 'Yelp'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                               link  valid
0       1                              Enterprise Apps Today  ...  https://www.enterpriseappstoday.com/stats/onli...   None
1       2                                       Jacob Devlin  ...                                                      None
2       3  Yu Sun, Shuohuan Wang, Yukun Li, Shikun Feng, ...  ...                                                      None
3       4  Mark Chen, Alec Radford, Rewon Child, Jeffrey ...  ...                                                      None
4       5  Kaiming He, Xinlei Chen, Saining Xie, Yanghao ...  ...                                                      None
5       6  Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang,...  ...                                                      None
6       7  Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo...  ...                                                      None
7       8    Ruoxi Wang, Bin Fu, Gang Fu, and Mingliang Wang  ...                                                      None
8       9  Bin Liu, Chenxu Zhu, Guilin Li, Weinan Zhang, ...  ...                                                      None
9      10  Guorui Zhou, Na Mou, Ying Fan, Qi Pi, Weijie C...  ...                                                      None
10     11         Paul Covington, Jay Adams, and Emre Sargin  ...                                                      None
11     12  Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang,...  ...                                                      None
12     13  Balazs Hidasi, Alexandros Karatzoglou, Linas B...  ...                  https://arxiv.org/abs/1511.06939.   None
13     14                             Jiaxi Tang and Ke Wang  ...                                                      None
14     15                 Wang-Cheng Kang and Julian McAuley  ...                                                      None
15     16                      Fei Sun, Jun Liu, and Jian Wu  ...                                                      None
16     17         Shubham Rajput, Mingxuan Chen, and Fei Sun  ...                                                      None
17     18    Majid Zolghadr, Mohsen Jamali, and Jiawei Zhang  ...                                                      None
18     19  Junyi Chen, Lu Chi, Bingyue Peng, and Zehuan Yuan  ...                                                      None
19     20                  Richard J Bolton and David J Hand  ...                                                      None
20     21  Humberto Acevedo-Viloria, Juan Martinez, and M...  ...                                                      None
21     22                   Hao Wang, Wei Zhang, and Fei Sun  ...                                                      None
22     23                                           Yoon Kim  ...                                                      None
23     24                                          A Vaswani  ...                                                      None
24     25                                  Eric Altman et al  ...  https://www.kaggle.com/datasets/ealtman2019/cr...   None
25     26                                       AI Lab et al  ...   https://huggingface.co/datasets/ai-lab/MBD-mini.   None
26     27                                    GroupLens et al  ...      https://grouplens.org/datasets/movielens/1m/.   None
27     28                                               Yelp  ...  https://business.yelp.com/data/resources/open-...   None
28     29  Inkit Padhi, Yair Schiff, Igor Melnyk, Mattia ...  ...                                                      None

[29 rows x 10 columns]
- Checking reference 1/29:
  -> Checking if provided link is pingable: https://www.enterpriseappstoday.com/stats/online-payment-statistics.html,
  -> INFO: Now checking 10 results for matching title: 'Global digital payment platforms user statistics (.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 43 results for matching title: 'Global digital payment platforms user statistics (.'
  -> WARNING: None of the 43 results matched the expected title!
     -> You could also open https://www.enterpriseappstoday.com/stats/online-payment-statistics.html, manually and check the results.
        -> Author(s): Enterprise Apps Today
        -> Title:     Global digital payment platforms user statistics (.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 2/29:
  -> INFO: Now checking 10 results for matching title: 'Bert: Pre-training of deep bidirectional transformers for language understanding'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Chang, Lee, Toutanova'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/29:
  -> INFO: Now checking 10 results for matching title: 'Ernie 2'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Ernie 2'
  -> WARNING: None of the 2 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Ernie+2 manually and check the results.
        -> Author(s): Yu Sun, Shuohuan Wang, Yukun Li, Shikun Feng, Hao Tian, Hua Wu, and Haifeng Wang
        -> Title:     Ernie 2
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 4/29:
  -> INFO: Now checking 10 results for matching title: 'Generative pretraining from pixels'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 6)
                   Unmatched authors = 'Dhariwal'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 5/29:
  -> INFO: Now checking 10 results for matching title: 'Masked autoencoders are scalable vision learners'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 5)
                   Unmatched authors = 'Doll'ar'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 6/29:
  -> INFO: Now checking 1 results for matching title: 'Actions speak louder than words: Trillion-parameter sequential transducers for generative recommendations'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Shi'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/29:
  -> INFO: Now checking 10 results for matching title: 'Deepfm: A factorization-machine based neural network for ctr prediction'
       -> INFO: All authors matched!
- Checking reference 8/29:
  -> INFO: Now checking 10 results for matching title: 'Deep & cross network for ad click predictions'
       -> INFO: All authors matched!
- Checking reference 9/29:
  -> INFO: Now checking 2 results for matching title: 'Autofis: Automatic feature interaction selection in factorization models for click-through rate prediction'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Yu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/29:
  -> INFO: Now checking 10 results for matching title: 'Deep interest evolution network for click-through rate prediction'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 7)
                   Unmatched authors = 'Bian'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/29:
  -> INFO: Now checking 10 results for matching title: 'Deep neural networks for youtube recommendations'
       -> INFO: All authors matched!
- Checking reference 12/29:
  -> INFO: Now checking 1 results for matching title: 'Actions speak louder than words: Trillion-parameter sequential transducers for generative recommendations'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Shi'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/29:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1511.06939.
  -> INFO: Now checking 10 results for matching title: 'Session-based recommendations with recurrent neural networks'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Session-based recommendations with recurrent neural networks'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Session-based+recommendations+with+recurrent+neural+networks manually and check the results.
        -> Author(s): Balazs Hidasi, Alexandros Karatzoglou, Linas Baltrunas, and Domonkos Tikk
        -> Title:     Session-based recommendations with recurrent neural networks
        -> Year:      2016
     -> Manual search was skipped by the user.
- Checking reference 14/29:
  -> INFO: Now checking 10 results for matching title: 'Personalized top-n sequential recommendation via convolutional sequence embedding'
       -> INFO: All authors matched!
- Checking reference 15/29:
  -> INFO: Now checking 10 results for matching title: 'Self-attentive sequential recommendation'
       -> INFO: All authors matched!
- Checking reference 16/29:
  -> INFO: Now checking 10 results for matching title: 'Bert4rec: Sequential recommendation with bidirectional encoder representations from transformers'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 133 results for matching title: 'Bert4rec: Sequential recommendation with bidirectional encoder representations from transformers'
  -> WARNING: None of the 133 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Bert4rec:+Sequential+recommendation+with+bidirectional+encoder+representations+from+transformers manually and check the results.
        -> Author(s): Fei Sun, Jun Liu, and Jian Wu
        -> Title:     Bert4rec: Sequential recommendation with bidirectional encoder representations from transformers
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 17/29:
  -> INFO: Now checking 5 results for matching title: 'Tiger: Token-based generative retrieval for sequential recommendation'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Rajput', 'Chen', 'Sun', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Tiger:+Token-based+generative+retrieval+for+sequential+recommendation manually and check the results.
        -> Author(s): Shubham Rajput, Mingxuan Chen, and Fei Sun
        -> Title:     Tiger: Token-based generative retrieval for sequential recommendation
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 18/29:
  -> INFO: Now checking 10 results for matching title: 'Diffurecsys: Diffusion-based generative modeling for sequential recommendation'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zolghadr', 'Jamali', 'Zhang', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Diffurecsys:+Diffusion-based+generative+modeling+for+sequential+recommendation manually and check the results.
        -> Author(s): Majid Zolghadr, Mohsen Jamali, and Jiawei Zhang
        -> Title:     Diffurecsys: Diffusion-based generative modeling for sequential recommendation
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 19/29:
  -> INFO: Now checking 3 results for matching title: 'Hllm: Enhancing sequential recommendations via hierarchical large language models for item and user modeling'
       -> INFO: All authors matched!
- Checking reference 20/29:
  -> INFO: Now checking 10 results for matching title: 'Statistical fraud detection: A review'
       -> INFO: All authors matched!
- Checking reference 21/29:
  -> INFO: Now checking 10 results for matching title: 'Relational graph convolutional networks for financial fraud detection'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Acevedo-Viloria', 'Martinez', 'Garcia', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Relational+graph+convolutional+networks+for+financial+fraud+detection manually and check the results.
        -> Author(s): Humberto Acevedo-Viloria, Juan Martinez, and Maria Garcia
        -> Title:     Relational graph convolutional networks for financial fraud detection
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 22/29:
  -> INFO: Now checking 10 results for matching title: 'Heterogeneous graph neural networks for user behavior prediction'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Zhang', 'Sun', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Heterogeneous+graph+neural+networks+for+user+behavior+prediction manually and check the results.
        -> Author(s): Hao Wang, Wei Zhang, and Fei Sun
        -> Title:     Heterogeneous graph neural networks for user behavior prediction
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 23/29:
  -> INFO: Now checking 10 results for matching title: 'Convolutional neural networks for sentence classification'
       -> INFO: All authors matched!
- Checking reference 24/29:
  -> INFO: Now checking 10 results for matching title: 'Attention is all you need'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 25/29:
  -> Checking if provided link is pingable: https://www.kaggle.com/datasets/ealtman2019/credit-card-transactions.
  -> INFO: Now checking 10 results for matching title: 'Credit card transactions (cct) dataset.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Altman', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Credit+card+transactions+(cct)+dataset. manually and check the results.
        -> Author(s): Eric Altman et al
        -> Title:     Credit card transactions (cct) dataset.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 26/29:
  -> Checking if provided link is pingable: https://huggingface.co/datasets/ai-lab/MBD-mini.
  -> INFO: Now checking 10 results for matching title: 'Mbd-mini dataset.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lab', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://huggingface.co/datasets/ai-lab/MBD-mini. manually and check the results.
        -> Author(s): AI Lab et al
        -> Title:     Mbd-mini dataset.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 27/29:
  -> Checking if provided link is pingable: https://grouplens.org/datasets/movielens/1m/.
  -> INFO: Now checking 10 results for matching title: 'Movielens-1m dataset.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['GroupLens', '2000']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://grouplens.org/datasets/movielens/1m/. manually and check the results.
        -> Author(s): GroupLens et al
        -> Title:     Movielens-1m dataset.
        -> Year:      2000
     -> Manual search was skipped by the user.
- Checking reference 28/29:
  -> Checking if provided link is pingable: https://business.yelp.com/data/resources/open-dataset/.
  -> INFO: Now checking 10 results for matching title: 'Yelp dataset.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yelp', '2014']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://business.yelp.com/data/resources/open-dataset/. manually and check the results.
        -> Author(s): Yelp
        -> Title:     Yelp dataset.
        -> Year:      2014
     -> Manual search was skipped by the user.
- Checking reference 29/29:
  -> INFO: Now checking 10 results for matching title: 'Tabular transformers for modeling multivariate time series'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 3: −log Prθ(xt | x<t, xprofile)
-> Invalid unicode use found on p. 5: LCL = −
-> Invalid unicode use found on p. 5: exp(−∥ei −ej∥2/τ)
-> Invalid unicode use found on p. 5: k∈U\{i} exp(−∥ei −ek∥2/τ),
-> Invalid unicode use found on p. 5: L = (1 −λ)Lgen
-> Invalid unicode use found on p. 6: positives for users with naturally varied transaction patterns: ∆u,m = Pu(m)−µu
 -> WARNING: Found a non-breaking space that seems invalid.
 -> WARNING: Found a non-breaking space that seems invalid.
 -> WARNING: Found a non-breaking space that seems invalid.
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Numeric reference range couldn't be parsed as Integers: ['L-100:L']
-> Warning: Bracket content ['L-100:L'] on p. 4 could not be matched to a reference.
   -> Sentence:  For live transactions, we compute risk scores through feature fusion: Pr(y = 1|·) = gϕ  ψ(cnew) | {z } context ,
fenc(X[L-100:L] u ) | {z } recent patterns , eu |{z} long-term profile , ∆(ˆxL+1, xnew) | {z } behavior deviation  , (3) where the
function gϕ represents a general downstream discriminative model, which can take various flexible forms depending on specific 
tasks or use cases, ψ(·) embeds transaction context features, fenc encodes the last 100 transactions via TextCNN [23], and 
∆measures the distance between predicted and observed behaviors
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 463 sentences on 10 pages -> Avg. of 52.44444444444444 sentences per page
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
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
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
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
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
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
Resorting to unclean kill browser.
-> Saved chapter_fig on try 1
-> Saved lit_fig on try 1
-> Saved rank_fig on try 1
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\12 PANTHER\PAU_results.md
```