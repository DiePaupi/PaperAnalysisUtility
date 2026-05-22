
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\29 Robust Reinforcement Learning\Robust Reinforcement Learning in Finance Modeling.pdf"
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
- Found following heading '2 - Preliminaries: Robust Reinforcement Learning' on page 3
- Found following heading '3 - Modeling Market Impact with Elliptic Uncertainty Sets' on page 4
- Found following heading '4 - Experiments' on page 8
- Found following heading '5 - Conclusion & Broader Impact' on page 10
=> Found references/literature section on page 10
- Found first appendix 'A - Backgrounds' on page 15
- Found following appendix 'B - Worst-Case Uncertainty under ℓp-Ellipse Uncertainty Sets' on page 17
- Found following appendix 'C - Experiment Details' on page 28
- Found following appendix 'D - Limitations' on page 31
- Found following appendix 'E - Additional Supplementary Materials' on page 31
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 15
All found references: 93
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ... link  valid
0       1           Ben Hambly, Renyuan Xu, and Huining Yang  ...        None
1       2  Nikolaos Pippas, Cagatay Turkay, and Elliot A ...  ...        None
2       3  Sebastian Jaimungal, Silvana M Pesenti, Ye She...  ...        None
3       4  Pengqian Yu, Joon Sern Lee, Ilya Kulyatin, Zek...  ...        None
4       5              Xiaochuan Shi, Yihua Zhou, and Lei Wu  ...        None
..    ...                                                ...  ...  ...    ...
88     89  John Schulman, Filip Wolski, Prafulla Dhariwal...  ...        None
89     90             Shaocong Ma, Yi Zhou, and Shaofeng Zou  ...        None
90     91  Shaocong Ma, Ziyi Chen, Yi Zhou, and Shaofeng Zou  ...        None
91     92                        Yi Zhou, Shaocong Ma, et al  ...        None
92     93  Shengbo Wang, Nian Si, Jose Blanchet, and Zhen...  ...        None

[93 rows x 10 columns]
- Checking reference 1/93:
  -> INFO: Now checking 10 results for matching title: 'Recent advances in reinforcement learning in finance'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/93:
  -> INFO: Now checking 1 results for matching title: 'The evolution of reinforcement learning in quantitative finance'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'The evolution of reinforcement learning in quantitative finance'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+evolution+of+reinforcement+learning+in+quantitative+finance manually and check the results.
        -> Author(s): Nikolaos Pippas, Cagatay Turkay, and Elliot A Ludvig
        -> Title:     The evolution of reinforcement learning in quantitative finance
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 3/93:
  -> INFO: Now checking 10 results for matching title: 'Robust risk-aware reinforcement learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/93:
  -> INFO: Now checking 10 results for matching title: 'Model-based deep reinforcement learning for dynamic portfolio optimization'
       -> INFO: All authors matched!
- Checking reference 5/93:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Robust reinforcement learning for portfolio management via competition and cooperation strategies, 2023
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 289 results for matching title: 'Robust reinforcement learning for portfolio management via competition and cooperation strategies, 2023'
  -> WARNING: None of the 289 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Robust+reinforcement+learning+for+portfolio+management+via+competition+and+cooperation+strategies%2C+2023 manually and check the results.
        -> Author(s): Xiaochuan Shi, Yihua Zhou, and Lei Wu
        -> Title:     Robust reinforcement learning for portfolio management via competition and cooperation strategies, 2023
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 6/93:
  -> INFO: Now checking 2 results for matching title: 'Advancing investment frontiers: Industry-grade deep reinforcement learning for portfolio optimization'
       -> INFO: All authors matched!
- Checking reference 7/93:
  -> INFO: Now checking 1 results for matching title: 'Deep reinforcement learning for portfolio management of markets with a dynamic number of assets'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Baca'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/93:
  -> INFO: Now checking 1 results for matching title: 'Continuous control with stacked deep dynamic recurrent reinforcement learning for portfolio optimization'
       -> INFO: All authors matched!
- Checking reference 9/93:
  -> INFO: Now checking 10 results for matching title: 'Portfolio dynamic trading strategies using deep reinforcement learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/93:
  -> INFO: Now checking 10 results for matching title: 'Deep reinforcement learning for optimizing finance portfolio management'
       -> INFO: All authors matched!
- Checking reference 11/93:
  -> INFO: Now checking 10 results for matching title: 'Reinforcement learning for portfolio management'
       -> INFO: All authors matched!
- Checking reference 12/93:
  -> INFO: Now checking 10 results for matching title: 'Dynamic Portfolio Management with Deep Reinforcement Learning'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['NUIPIAN', 'MEESAD', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dynamic+Portfolio+Management+with+Deep+Reinforcement+Learning manually and check the results.
        -> Author(s): WARAMETH NUIPIAN, PHAYUNG MEESAD, et al
        -> Title:     Dynamic Portfolio Management with Deep Reinforcement Learning
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 13/93:
  -> INFO: Now checking 1 results for matching title: 'Financial portfolio optimization with online deep reinforcement learning and restricted stacked autoencoder—deepbreath'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Financial portfolio optimization with online deep reinforcement learning and restricted stacked autoencoder—deepbreath'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Financial+portfolio+optimization+with+online+deep+reinforcement+learning+and+restricted+stacked+autoencoder—deepbreath manually and check the results.
        -> Author(s): Farzan Soleymani and Eric Paquet
        -> Title:     Financial portfolio optimization with online deep reinforcement learning and restricted stacked autoencoder—deepbreath
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 14/93:
  -> INFO: Now checking 10 results for matching title: 'Trading strategies using reinforcement learning'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = '조현민, 경영공학과'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 15/93:
  -> INFO: Now checking 10 results for matching title: 'Learning to trade via direct reinforcement'
       -> INFO: All authors matched!
- Checking reference 16/93:
  -> INFO: Now checking 10 results for matching title: 'Deep robust reinforcement learning for practical algorithmic trading'
       -> INFO: All authors matched!
- Checking reference 17/93:
  -> INFO: Now checking 1 results for matching title: 'Deep reinforcement learning robots for algorithmic trading: Considering stock market conditions and us interest rates'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 8 results for matching title: 'Deep reinforcement learning robots for algorithmic trading: Considering stock market conditions and us interest rates'
  -> WARNING: None of the 8 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+reinforcement+learning+robots+for+algorithmic+trading:+Considering+stock+market+conditions+and+us+interest+rates manually and check the results.
        -> Author(s): Ji-Heon Park, Jae-Hwan Kim, and Jun-Ho Huh
        -> Title:     Deep reinforcement learning robots for algorithmic trading: Considering stock market conditions and us interest rates
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 18/93:
  -> INFO: Now checking 10 results for matching title: 'A deep reinforcement learning-based decision support system for automated stock market trading'
       -> INFO: All authors matched!
- Checking reference 19/93:
  -> INFO: Now checking 10 results for matching title: 'Adaptive stock trading strategies with deep reinforcement learning methods'
       -> INFO: All authors matched!
- Checking reference 20/93:
  -> INFO: Now checking 2 results for matching title: 'Dealing with the inventory risk: a solution to the market making problem'
       -> INFO: All authors matched!
       -> WARNING: Year (2011) does not match expected year (2013)!
       -> INFO: All authors matched!
       -> WARNING: Year (2012) does not match expected year (2013)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 21/93:
  -> INFO: Now checking 5 results for matching title: 'Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading'
       -> INFO: All authors matched!
- Checking reference 22/93:
  -> INFO: Now checking 10 results for matching title: 'Deep reinforcement learning for trading'
       -> INFO: All authors matched!
- Checking reference 23/93:
  -> INFO: Now checking 10 results for matching title: 'Deep reinforcement learning for limit order book-based market making'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Deep reinforcement learning for limit order book-based market making'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+reinforcement+learning+for+limit+order+book-based+market+making manually and check the results.
        -> Author(s): Kyung Hyun Park, Hyeong Jin Kim, and Woo Chang Kim
        -> Title:     Deep reinforcement learning for limit order book-based market making
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 24/93:
  -> INFO: Now checking 4 results for matching title: 'Learning to trade with continuous action spaces: Application to market making'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Casgrain', 'Kulkarni', 'Watters', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Learning+to+trade+with+continuous+action+spaces:+Application+to+market+making manually and check the results.
        -> Author(s): Pierre Casgrain, Anirudh Kulkarni, and Nicholas Watters
        -> Title:     Learning to trade with continuous action spaces: Application to market making
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 25/93:
  -> INFO: Now checking 10 results for matching title: 'Reinforcement learning for optimal hedging'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kolm', 'Krügel', 'Zadorozhnyi', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Reinforcement+learning+for+optimal+hedging manually and check the results.
        -> Author(s): Petter N Kolm, Sebastian Krügel, and Sergiy V Zadorozhnyi
        -> Title:     Reinforcement learning for optimal hedging
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 26/93:
  -> INFO: Now checking 10 results for matching title: 'Deep hedging'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Buehler', 'Gonon', 'Teichmann', 'Wood', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+hedging manually and check the results.
        -> Author(s): Hans Buehler, Lukas Gonon, Josef Teichmann, and Ben Wood
        -> Title:     Deep hedging
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 27/93:
  -> INFO: Now checking 10 results for matching title: 'Risk-averse reinforcement learning for optimal option hedging'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Cao', 'Wang', 'Zhang', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Risk-averse+reinforcement+learning+for+optimal+option+hedging manually and check the results.
        -> Author(s): H Cao, Y Wang, and Y Zhang
        -> Title:     Risk-averse reinforcement learning for optimal option hedging
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 28/93:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Can machine learning improve delta hedging? Journal of Derivatives, 9(1):39–56.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chan', 'Shelton', '2001']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Can+machine+learning+improve+delta+hedging?+Journal+of+Derivatives%2C+9(1):39–56. manually and check the results.
        -> Author(s): W L Chan and R O Shelton
        -> Title:     Can machine learning improve delta hedging? Journal of Derivatives, 9(1):39–56.
        -> Year:      2001
     -> Manual search was skipped by the user.
- Checking reference 29/93:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Q-learning for option pricing and hedging with transaction costs
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ning', 'Kwok', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Q-learning+for+option+pricing+and+hedging+with+transaction+costs manually and check the results.
        -> Author(s): Z Ning and Y K Kwok
        -> Title:     Q-learning for option pricing and hedging with transaction costs
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 30/93:
  -> INFO: Now checking 10 results for matching title: 'Robust risk-aware option hedging'
       -> INFO: All authors matched!
- Checking reference 31/93:
  -> INFO: Now checking 10 results for matching title: 'Optimal execution of portfolio transactions'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Almgren', 'Chriss', '2001']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Optimal+execution+of+portfolio+transactions manually and check the results.
        -> Author(s): Robert Almgren and Neil Chriss
        -> Title:     Optimal execution of portfolio transactions
        -> Year:      2001
     -> Manual search was skipped by the user.
- Checking reference 32/93:
  -> INFO: Now checking 10 results for matching title: 'Optimal trading strategy and supply/demand dynamics'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Obizhaeva', 'Wang', '2013']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Optimal+trading+strategy+and+supply/demand+dynamics manually and check the results.
        -> Author(s): Anna A Obizhaeva and Jiang Wang
        -> Title:     Optimal trading strategy and supply/demand dynamics
        -> Year:      2013
     -> Manual search was skipped by the user.
- Checking reference 33/93:
  -> INFO: Now checking 2 results for matching title: 'The square-root impace law also holds for option markets'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tóth', 'Eisler', 'Bouchaud', '2016']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+square-root+impace+law+also+holds+for+option+markets manually and check the results.
        -> Author(s): Bence Tóth, Zoltán Eisler, and J-P Bouchaud
        -> Title:     The square-root impace law also holds for option markets
        -> Year:      2016
     -> Manual search was skipped by the user.
- Checking reference 34/93:
  -> INFO: Now checking 10 results for matching title: 'First-order policy optimization for robust markov decision process'
       -> INFO: All authors matched!
- Checking reference 35/93:
  -> INFO: Now checking 10 results for matching title: 'Robust reinforcement learning via progressive task sequence'
       -> INFO: All authors matched!
- Checking reference 36/93:
  -> INFO: Now checking 10 results for matching title: 'Efficient action robust reinforcement learning with probabilistic policy execution uncertainty'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 37/93:
  -> INFO: Now checking 10 results for matching title: 'Online robust reinforcement learning with model uncertainty'
       -> INFO: All authors matched!
- Checking reference 38/93:
  -> INFO: Now checking 1 results for matching title: 'Robust gymnasium: A unified modular benchmark for robust reinforcement learning'
       -> INFO: All authors matched!
- Checking reference 39/93:
  -> INFO: Now checking 10 results for matching title: 'Robust adversarial reinforcement learning'
       -> INFO: All authors matched!
- Checking reference 40/93:
  -> INFO: Now checking 10 results for matching title: 'Robust reinforcement learning using offline data'
       -> INFO: All authors matched!
- Checking reference 41/93:
  -> INFO: Now checking 10 results for matching title: 'Provably robust federated reinforcement learning'
       -> INFO: All authors matched!
- Checking reference 42/93:
  -> INFO: Now checking 6 results for matching title: 'Robust rlhf with noisy rewards'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Shen', 'Zhang', 'Yao', 'Zheng', 'Guo', 'Liu', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Robust+rlhf+with+noisy+rewards manually and check the results.
        -> Author(s): Wei Shen, Xiaoying Zhang, Yuanshun Yao, Rui Zheng, Hongyi Guo, and Yang Liu
        -> Title:     Robust rlhf with noisy rewards
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 43/93:
  -> INFO: Now checking 5 results for matching title: 'Decentralized robust v-learning for solving markov games with model uncertainty'
       -> INFO: All authors matched!
- Checking reference 44/93:
  -> INFO: Now checking 2 results for matching title: 'Nearoptimal distributionally robust reinforcement learning with general l_p norms'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Clavier', 'Shi', 'Pennec', 'Mazumdar', 'Wierman', 'Geist', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Nearoptimal+distributionally+robust+reinforcement+learning+with+general+l_p+norms manually and check the results.
        -> Author(s): Pierre Clavier, Laixi Shi, Erwan Le Pennec, Eric Mazumdar, Adam Wierman, and Matthieu Geist
        -> Title:     Nearoptimal distributionally robust reinforcement learning with general l_p norms
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 45/93:
  -> INFO: Now checking 5 results for matching title: 'An efficient solution to s-rectangular robust markov decision processes'
       -> INFO: All authors matched!
- Checking reference 46/93:
  -> INFO: Now checking 10 results for matching title: 'Policy gradient for rectangular robust markov decision processes'
       -> INFO: All authors matched!
- Checking reference 47/93:
  -> INFO: Now checking 2 results for matching title: 'Soft robust MDPs and risk-sensitive MDPs: Equivalence, policy gradient, and sample complexity'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/93:
  -> INFO: Now checking 4 results for matching title: 'Plan to predict: Learning an uncertainty-foreseeing model for model-based reinforcement learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 49/93:
  -> INFO: Now checking 5 results for matching title: 'Natural actor-critic for robust reinforcement learning with function approximation'
       -> INFO: All authors matched!
- Checking reference 50/93:
  -> INFO: Now checking 4 results for matching title: 'Policy gradient in robust mdps with global convergence guarantee'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 51/93:
  -> INFO: Now checking 10 results for matching title: 'Policy optimization for robust average reward mdps'
       -> INFO: All authors matched!
- Checking reference 52/93:
  -> INFO: Now checking 4 results for matching title: 'Rectified robust policy optimization for modeluncertain constrained reinforcement learning without strong duality'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ma', 'Chen', 'Zhou', 'Huang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Rectified+robust+policy+optimization+for+modeluncertain+constrained+reinforcement+learning+without+strong+duality manually and check the results.
        -> Author(s): Shaocong Ma, Ziyi Chen, Yi Zhou, and Heng Huang
        -> Title:     Rectified robust policy optimization for modeluncertain constrained reinforcement learning without strong duality
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 53/93:
  -> INFO: Now checking 10 results for matching title: 'Lobster: Limit order book reconstruction system'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Huang', 'Polak', '2011']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Lobster:+Limit+order+book+reconstruction+system manually and check the results.
        -> Author(s): Ruihong Huang and Tomas Polak
        -> Title:     Lobster: Limit order book reconstruction system
        -> Year:      2011
     -> Manual search was skipped by the user.
- Checking reference 54/93:
  -> INFO: Now checking 7 results for matching title: 'The price impact of order book events: Market orders, limit orders and cancellations'
       -> INFO: All authors matched!
- Checking reference 55/93:
  -> INFO: Now checking 10 results for matching title: 'Transient linear price impact and fredholm integral equations'
       -> INFO: All authors matched!
- Checking reference 56/93:
  -> INFO: Now checking 10 results for matching title: 'Trades: Generating realistic market simulations with diffusion models'
       -> INFO: All authors matched!
- Checking reference 57/93:
  -> INFO: Now checking 10 results for matching title: 'Direct estimation of equity market impact'
       -> INFO: All authors matched!
- Checking reference 58/93:
  -> INFO: Now checking 5 results for matching title: 'Empirical study of market impact conditional on order-flow imbalance'
       -> INFO: All authors matched!
- Checking reference 59/93:
  -> INFO: Now checking 10 results for matching title: 'Multi-agent reinforcement learning in a realistic limit order book market simulation'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['He', 'Lu', 'Xu', 'Bian', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Multi-agent+reinforcement+learning+in+a+realistic+limit+order+book+market+simulation manually and check the results.
        -> Author(s): Tianlang He, Keyan Lu, Chang Xu, and Jiang Bian
        -> Title:     Multi-agent reinforcement learning in a realistic limit order book market simulation
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 60/93:
  -> INFO: Now checking 2 results for matching title: 'Agent-based financial markets: A review of the methodology and domain'
       -> INFO: All authors matched!
- Checking reference 61/93:
  -> INFO: Now checking 10 results for matching title: 'Simulating financial market via large language model based agents'
       -> INFO: All authors matched!
- Checking reference 62/93:
  -> INFO: Now checking 1 results for matching title: 'Mars: a financial market simulation engine powered by generative foundation model'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 63/93:
  -> INFO: Now checking 10 results for matching title: 'Limit order books'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gould', 'Porter', 'Williams', 'McDonald', 'Fenn', 'Howison', '2013']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Limit+order+books manually and check the results.
        -> Author(s): Martin D  Gould, Mason A  Porter, Stacy Williams, Mark McDonald, Daniel J  Fenn, and Sam D  Howison
        -> Title:     Limit order books
        -> Year:      2013
     -> Manual search was skipped by the user.
- Checking reference 64/93:
  -> INFO: Now checking 10 results for matching title: 'Forecasting stock prices from limit order book using convolutional neural networks'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tsantekidis', 'Passalis', 'Tefas', 'Kanniainen', 'Gabbouj', 'Iosifidis', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Forecasting+stock+prices+from+limit+order+book+using+convolutional+neural+networks manually and check the results.
        -> Author(s): Avraam Tsantekidis, Nikolaos Passalis, Anastasios Tefas, Juho Kanniainen, Moncef Gabbouj, and Alexandros Iosifidis
        -> Title:     Forecasting stock prices from limit order book using convolutional neural networks
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 65/93:
  -> Checking if provided link is pingable: https://theses.hal.science/tel-04913317v1.
  -> INFO: Now checking 10 results for matching title: 'Reinforcement Learning for Systematic Market Making Strategies'
       -> INFO: All authors matched!
       -> WARNING: Year (0) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 66/93:
  -> INFO: Now checking 1 results for matching title: 'Developing a multi-agent and self-adaptive framework with deep reinforcement learning for dynamic portfolio risk management'
       -> INFO: All authors matched!
- Checking reference 67/93:
  -> INFO: Now checking 10 results for matching title: 'Wasserstein robust reinforcement learning'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 6)
                   Unmatched authors = 'Bou-Ammar'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 68/93:
  -> INFO: Now checking 8 results for matching title: 'Learning robust policy against disturbance in transition dynamics via state-conservative policy optimization'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 69/93:
  -> INFO: Now checking 10 results for matching title: 'Learning models with uniform performance via distributionally robust optimization'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 70/93:
  -> INFO: Now checking 10 results for matching title: 'Reinforcement learning'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sutton', 'Barto', '1999']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Reinforcement+learning manually and check the results.
        -> Author(s): Richard S Sutton, Andrew G Barto, et al
        -> Title:     Reinforcement learning
        -> Year:      1999
     -> Manual search was skipped by the user.
- Checking reference 71/93:
  -> INFO: Now checking 1 results for matching title: 'Policy gradient and actor-critic learning in continuous time and space: Theory and algorithms'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 72/93:
  -> INFO: Now checking 10 results for matching title: 'Deterministic policy gradient: Convergence analysis'
       -> INFO: All authors matched!
- Checking reference 73/93:
  -> INFO: Now checking 10 results for matching title: 'Networked multi-agent reinforcement learning in continuous spaces'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Başar'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 74/93:
  -> INFO: Now checking 10 results for matching title: 'Toward a theoretical foundation of policy optimization for learning control policies'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 5)
                   Unmatched authors = 'Başar'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 75/93:
  -> INFO: Now checking 10 results for matching title: 'Distributionally robust reinforcement learning'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Smirnova', 'Dohmatob', 'Mary', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Distributionally+robust+reinforcement+learning manually and check the results.
        -> Author(s): Elena Smirnova, Elvis Dohmatob, and Jérémie Mary
        -> Title:     Distributionally robust reinforcement learning
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 76/93:
  -> INFO: Now checking 1 results for matching title: 'Double pessimism is provably efficient for distributionally robust offline reinforcement learning: Generic algorithm and robust partial coverage'
       -> INFO: All authors matched!
- Checking reference 77/93:
  -> INFO: Now checking 3 results for matching title: 'Sample complexity of distributionally robust offdynamics reinforcement learning with online interaction'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['He', 'Liu', 'Wang', 'Xu', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Sample+complexity+of+distributionally+robust+offdynamics+reinforcement+learning+with+online+interaction manually and check the results.
        -> Author(s): Yiting He, Zhishuai Liu, Weixin Wang, and Pan Xu
        -> Title:     Sample complexity of distributionally robust offdynamics reinforcement learning with online interaction
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 78/93:
  -> INFO: Now checking 3 results for matching title: 'Rectangularity and duality of distributionally robust markov decision processes'
       -> INFO: All authors matched!
- Checking reference 79/93:
  -> INFO: Now checking 7 results for matching title: 'Distributionally robust off-dynamics reinforcement learning: Provable efficiency with linear function approximation'
       -> INFO: All authors matched!
- Checking reference 80/93:
  -> INFO: Now checking 2 results for matching title: 'Distributionally robust reinforcement learning with interactive data collection: Fundamental hardness and near-optimal algorithms'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lu', 'Zhong', 'Zhang', 'Blanchet', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Distributionally+robust+reinforcement+learning+with+interactive+data+collection:+Fundamental+hardness+and+near-optimal+algorithms manually and check the results.
        -> Author(s): Miao Lu, Han Zhong, Tong Zhang, and Jose Blanchet
        -> Title:     Distributionally robust reinforcement learning with interactive data collection: Fundamental hardness and near-optimal algorithms
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 81/93:
  -> INFO: Now checking 10 results for matching title: 'Robust markov decision processes'
       -> INFO: All authors matched!
- Checking reference 82/93:
  -> INFO: Now checking 1 results for matching title: 'Beat the market: An effective intraday momentum strategy for s&p500 etf (spy)'
       -> INFO: All authors matched!
- Checking reference 83/93:
  -> INFO: Now checking 10 results for matching title: 'Openai gym'
       -> INFO: All authors matched!
- Checking reference 84/93:
  -> INFO: Now checking 10 results for matching title: 'Gymnasium: A standard interface for reinforcement learning environments'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 85/93:
  -> INFO: Now checking 10 results for matching title: 'Convex Optimization'
       -> INFO: All authors matched!
       -> WARNING: Year (2010) does not match expected year (2004)!
       -> INFO: All authors matched!
- Checking reference 86/93:
  -> INFO: Now checking 10 results for matching title: 'Advanced Linear Algebra'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Roman', '2008']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Advanced+Linear+Algebra manually and check the results.
        -> Author(s): Stephen Roman
        -> Title:     Advanced Linear Algebra
        -> Year:      2008
     -> Manual search was skipped by the user.
- Checking reference 87/93:
  -> INFO: Now checking 10 results for matching title: 'Proximal algorithms'
       -> INFO: All authors matched!
       -> WARNING: Year (2013) does not match expected year (2014)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 88/93:
  -> INFO: Now checking 10 results for matching title: 'Convex Analysis and Nonlinear Optimization: Theory and Examples'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Borwein', 'Lewis', '2006']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Convex+Analysis+and+Nonlinear+Optimization:+Theory+and+Examples manually and check the results.
        -> Author(s): Jonathan M  Borwein and Adrian S  Lewis
        -> Title:     Convex Analysis and Nonlinear Optimization: Theory and Examples
        -> Year:      2006
     -> Manual search was skipped by the user.
- Checking reference 89/93:
  -> INFO: Now checking 10 results for matching title: 'Proximal policy optimization algorithms'
       -> INFO: All authors matched!
- Checking reference 90/93:
  -> INFO: Now checking 10 results for matching title: 'Variance-reduced off-policy tdc learning: Non-asymptotic convergence analysis'
       -> INFO: All authors matched!
- Checking reference 91/93:
  -> INFO: Now checking 1 results for matching title: 'Greedy-gq with variance reduction: Finite-time analysis and improved complexity'
       -> INFO: All authors matched!
- Checking reference 92/93:
  -> INFO: Now checking 10 results for matching title: 'Stochastic optimization methods for policy evaluation in reinforcement learning'
       -> INFO: All authors matched!
- Checking reference 93/93:
  -> INFO: Now checking 10 results for matching title: 'Sample complexity of variance-reduced distributionally robust q-learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
-> Starting the sorting of mismatching entries!
-> WARNING: No two years recognized in check-message!
##########################################################
# Starting Unicode Check
##########################################################
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 296 sentences on 10 pages -> Avg. of 33.888888888888886 sentences per page
-> Warning: Reference '85' never used in the document's text.
-> Warning: Reference '86' never used in the document's text.
-> Warning: Reference '87' never used in the document's text.
-> Warning: Reference '88' never used in the document's text.
-> Warning: Reference '89' never used in the document's text.
-> Warning: Reference '90' never used in the document's text.
-> Warning: Reference '91' never used in the document's text.
-> Warning: Reference '92' never used in the document's text.
-> Warning: Reference '93' never used in the document's text.
---
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
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
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
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
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
-> Missing an abstract for reference with index 57 (Ref. ID = 58); Skipping LLM check...
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 65 (Ref. ID = 66); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 69 (Ref. ID = 70); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 71 (Ref. ID = 72); Skipping LLM check...
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
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
-> Missing an abstract for reference with index 86 (Ref. ID = 87); Skipping LLM check...
-> Missing an abstract for reference with index 87 (Ref. ID = 88); Skipping LLM check...
-> Missing an abstract for reference with index 88 (Ref. ID = 89); Skipping LLM check...
-> Missing an abstract for reference with index 89 (Ref. ID = 90); Skipping LLM check...
-> Missing an abstract for reference with index 90 (Ref. ID = 91); Skipping LLM check...
-> Missing an abstract for reference with index 91 (Ref. ID = 92); Skipping LLM check...
-> WARNING: Reference with index 92 (Ref. ID = 93) has no associated sentence!
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
  -> Found 3 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 6 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 4 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 147 matches in this ranking!
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
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺  98% 0:00:01
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\29 Robust Reinforcement Learning\PAU_results.md
```