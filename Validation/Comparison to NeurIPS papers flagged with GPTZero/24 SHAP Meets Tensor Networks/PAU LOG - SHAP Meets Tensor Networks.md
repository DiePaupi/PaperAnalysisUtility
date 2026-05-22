
```
Enter the path to the PDF file: "C:\Users\pauli\Sciebo\Paupis_Privatstuff\PhD_Notes\Paper-Projekte\PQC\PAU - All  GPTZero NeurIPS Paper with H\24 SHAP Meets Tensor Networks\SHAP Meets Tensor Networks.pdf"
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
- Found following heading '2 - Preliminaries' on page 3
- Found following heading '3 - Tensors, Tensor Networks and Binarized Neural Networks' on page 4
- Found following heading '4 - Provably Exact SHAP Explanations for TNs: A General Framework' on page 5
- Found following heading '5 - Provably Exact and Tractable SHAP for TTs, and Other ML Models' on page 6
- Found following heading '6 - A Fine-Grained Analysis of SHAP Computation for BNNs' on page 8
- Found following heading '7 - Limitations and Future Work' on page 10
- Found following heading '8 - Conclusion' on page 10
=> Found references/literature section on page 10
- Found first appendix 'A - Extended Related Work' on page 25
- Found following appendix 'B - Background' on page 26
- Found following appendix 'C - Computing Marginal SHAP for General TNs' on page 31
- Found following appendix 'D - Computing Marginal SHAP for Tensor Trains' on page 36
- Found following appendix 'E - Tightening Complexity Results for Other ML Models' on page 38
- Found following appendix 'F - Computing Marginal SHAP for BNNs' on page 41
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 25
All found references: 117
-> Warning: Could not parse year in reference 'Matthieu Courbariaux, Itay Hubara, Daniel Soudry, Ran El-Yaniv, and Yoshua Bengio. Binarized Neural Networks: Training Deep Neural Networks with Weights and Activations Constrained to +1 or -1. Technical Report.'!
-----------
 -> Parsed references DataFrame:
    ref_id                                            authors  ...                                               link  valid
0        1  Omer Abramovich, Daniel Deutch, Nave Frost, Ah...  ...                                                      None
1        2   Federico Adolfi, Martina Vilas, and Todd Wareham  ...                                                      None
2        3      Borja Aizpurua, Samuel Palmer, and Román Orús  ...                                                      None
3        4                         Mazen Ali and Anthony Nouy  ...                  https://arxiv.org/abs/2101.11932.   None
4        5              Guy Amir, Shahaf Bassan, and Guy Katz  ...                                                      None
..     ...                                                ...  ...                                                ...    ...
112    113  Jilei Yang, Rui Zhang, Cong Li, Meng Zhang, Ch...  ...                  https://arxiv.org/abs/2109.09847.   None
113    114  Jinqiang Yu, Graham Farr, Alexey Ignatiev, and...  ...                                                      None
114    115     Peng Yu, Chao Xu, Albert Bifet, and Jesse Read  ...                                                      None
115    116  Artjom Zern, Klaus Broelemann, and Gjergji Kas...  ...                                                      None
116    117                  Erik Štrumbelj and Igor Kononenko  ...  https://nips.cc/public/guides/CodeSubmissionPo...   None

[117 rows x 10 columns]
- Checking reference 1/117:
  -> INFO: Now checking 3 results for matching title: 'Banzhaf Values for Facts in Query Answering'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/117:
  -> INFO: Now checking 2 results for matching title: 'The Computational Complexity of Circuit Discovery for Inner Interpretability'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
       -> INFO: All authors matched!
- Checking reference 3/117:
  -> INFO: Now checking 1 results for matching title: 'Tensor Networks for Explainable Machine Learning in Cybersecurity'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/117:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2101.11932.
  -> INFO: Now checking 5 results for matching title: 'Approximation Theory of Tree Tensor Networks: Tensorized Multivariate Functions.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Ali', 'Nouy', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Approximation+Theory+of+Tree+Tensor+Networks:+Tensorized+Multivariate+Functions. manually and check the results.
        -> Author(s): Mazen Ali and Anthony Nouy
        -> Title:     Approximation Theory of Tree Tensor Networks: Tensorized Multivariate Functions.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 5/117:
  -> INFO: Now checking 1 results for matching title: 'Hard to Explain: On the Computational Hardness of In-Distribution Model Interpretation'
       -> INFO: All authors matched!
- Checking reference 6/117:
  -> INFO: Now checking 1 results for matching title: 'On the Complexity of SHAP-Score-Based Explanations: Tractability via Knowledge Compilation and NonApproximability Results'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'On the Complexity of SHAP-Score-Based Explanations: Tractability via Knowledge Compilation and NonApproximability Results'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=On+the+Complexity+of+SHAP-Score-Based+Explanations:+Tractability+via+Knowledge+Compilation+and+NonApproximability+Results manually and check the results.
        -> Author(s): Marcelo Arenas, Pablo Barcelo, Leopoldo Bertossi, and Mikael Monet
        -> Title:     On the Complexity of SHAP-Score-Based Explanations: Tractability via Knowledge Compilation and NonApproximability Results
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 7/117:
  -> INFO: Now checking 10 results for matching title: 'Computational Complexity: A Modern Approach'
       -> INFO: All authors matched!
- Checking reference 8/117:
  -> INFO: Now checking 1 results for matching title: 'On Preferred Abductive Explanations for Decision Trees and Random Forests'
       -> INFO: All authors matched!
- Checking reference 9/117:
  -> INFO: Now checking 2 results for matching title: 'Trading Complexity for Sparsity in Random Forest Explanations'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/117:
  -> Checking if provided link is pingable: https://arXiv:2501.02356.
  -> INFO: Now checking 1 results for matching title: 'When is the Computation of a Feature Attribution Method Tractable?.'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'When is the Computation of a Feature Attribution Method Tractable?.'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=When+is+the+Computation+of+a+Feature+Attribution+Method+Tractable?. manually and check the results.
        -> Author(s): P Barceló, R Cominetti, and M Morgado
        -> Title:     When is the Computation of a Feature Attribution Method Tractable?.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 11/117:
  -> INFO: Now checking 10 results for matching title: 'Model Interpretability Through the Lens of Computational Complexity'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Barcel'o, P'erez'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/117:
  -> INFO: Now checking 4 results for matching title: 'Explaining k-Nearest Neighbors: Abductive and Counterfactual Explanations'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Barcel'o'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/117:
  -> INFO: Now checking 10 results for matching title: 'Satisfiability Modulo Theories'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Barrett', 'Tinelli', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Satisfiability+Modulo+Theories manually and check the results.
        -> Author(s): Clark Barrett and Cesare Tinelli
        -> Title:     Satisfiability Modulo Theories
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 14/117:
  -> INFO: Now checking 4 results for matching title: 'Towards Formal XAI: Formally Approximate Minimal Explanations of Neural Networks'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 15/117:
  -> INFO: Now checking 10 results for matching title: 'Formally Explaining Neural Networks within Reactive Systems'
       -> INFO: All authors matched!
- Checking reference 16/117:
  -> INFO: Now checking 10 results for matching title: 'Local vs'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Bassan', 'Amir', 'Katz', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Local+vs manually and check the results.
        -> Author(s): Shahaf Bassan, Guy Amir, and Guy Katz
        -> Title:     Local vs
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 17/117:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: What makes an Ensemble (Un) Interpretable? In Proc
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Bassan', 'Amir', 'Zehavi', 'Katz', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=What+makes+an+Ensemble+(Un)+Interpretable?+In+Proc manually and check the results.
        -> Author(s): Shahaf Bassan, Guy Amir, Meirav Zehavi, and Guy Katz
        -> Title:     What makes an Ensemble (Un) Interpretable? In Proc
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 18/117:
  -> INFO: Now checking 1 results for matching title: 'Explaining, Fast and Slow: Abstraction and Refinement of Provable Explanations'
       -> INFO: All authors matched!
- Checking reference 19/117:
  -> INFO: Now checking 3 results for matching title: 'Explain Yourself, Briefly! Self-Explaining Neural Networks with Concise Sufficient Reasons'
       -> INFO: All authors matched!
- Checking reference 20/117:
  -> Checking if provided link is pingable: https://arXiv:2503.18067.
  -> INFO: Now checking 10 results for matching title: 'Self-Explaining Neural Networks for Business Process Monitoring'
       -> INFO: All authors matched!
- Checking reference 21/117:
  -> INFO: Now checking 10 results for matching title: 'Additive Models Explained: A Computational Complexity Approach'
       -> INFO: All authors matched!
- Checking reference 22/117:
  -> INFO: Now checking 10 results for matching title: 'Causality-based Explanation of Classification Outcomes'
       -> INFO: All authors matched!
- Checking reference 23/117:
  -> INFO: Now checking 10 results for matching title: 'The Shapley Value in Database Management'
       -> INFO: All authors matched!
- Checking reference 24/117:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1912.10049.
  -> INFO: Now checking 10 results for matching title: 'Lectures on Quantum Tensor Networks'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 25/117:
  -> INFO: Now checking 3 results for matching title: 'Axiomatic Aggregations of Abductive Explanations'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/117:
  -> INFO: Now checking 10 results for matching title: 'Provably Efficient, Succinct, and Precise Explanations'
       -> INFO: All authors matched!
- Checking reference 27/117:
  -> INFO: Now checking 2 results for matching title: 'From Shapley values to Generalized Additive Models and Back'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 28/117:
  -> INFO: Now checking 10 results for matching title: 'Fast Parallel Matrix and GCD Computations'
       -> INFO: All authors matched!
- Checking reference 29/117:
  -> INFO: Now checking 10 results for matching title: 'Approximating Probabilistic Explanations via Supermodular Minimization'
       -> INFO: All authors matched!
- Checking reference 30/117:
  -> Checking if provided link is pingable: https://arXivpreprintarXiv:2501.06766.
  -> INFO: Now checking 1 results for matching title: 'On the Complexity of Global Necessary Reasons to Explain Classification'
       -> INFO: All authors matched!
- Checking reference 31/117:
  -> INFO: Now checking 2 results for matching title: 'Polynomial Calculation of the Shapley Value Based on Sampling'
       -> INFO: All authors matched!
- Checking reference 32/117:
  -> INFO: Now checking 10 results for matching title: 'RKHS-SHAP: Shapley Values for Kernel Methods'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 3)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/117:
  -> INFO: Now checking 1 results for matching title: 'Explaining the Uncertain: Stochastic Shapley Values for Gaussian Process Models'
       -> INFO: All authors matched!
- Checking reference 34/117:
  -> INFO: Now checking 10 results for matching title: 'Chapter 8 - Tensor Network Algorithms for Image Classification'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chen', 'Batselier', 'Wong', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Chapter+8+-+Tensor+Network+Algorithms+for+Image+Classification manually and check the results.
        -> Author(s): Cong Chen, Kim Batselier, and Ngai Wong
        -> Title:     Chapter 8 - Tensor Network Algorithms for Image Classification
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 35/117:
  -> INFO: Now checking 1 results for matching title: 'Machine learning with tree tensor networks, cp rank constraints, and tensor dropout'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 36/117:
  -> INFO: Now checking 1 results for matching title: 'Machine Learning With Tree Tensor Networks, CP Rank Constraints, and Tensor Dropout'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 37/117:
  -> INFO: Now checking 2 results for matching title: 'Explaining Models by Propagating Shapley Values of Local Components'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 38/117:
  -> INFO: Now checking 1 results for matching title: 'HarsanyiNet: Computing Accurate Shapley Values in a Single Forward Propagation'
       -> INFO: All authors matched!
- Checking reference 39/117:
  -> INFO: Now checking 10 results for matching title: 'Towards a Complexity Theory of Synchronous Parallel Computation'
       -> INFO: All authors matched!
- Checking reference 40/117:
  -> INFO: Now checking 10 results for matching title: 'Tractability of Explaining Classifier Decisions'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 41/117:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1602.02830.
  -> INFO: Now checking 4 results for matching title: 'Binarized Neural Networks: Training Deep Neural Networks with Weights and Activations Constrained to +1 or -1'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Courbariaux', 'Hubara', 'Soudry', 'El-Yaniv', 'Bengio', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Binarized+Neural+Networks:+Training+Deep+Neural+Networks+with+Weights+and+Activations+Constrained+to++1+or+-1 manually and check the results.
        -> Author(s): Matthieu Courbariaux, Itay Hubara, Daniel Soudry, Ran El-Yaniv, and Yoshua Bengio
        -> Title:     Binarized Neural Networks: Training Deep Neural Networks with Weights and Activations Constrained to +1 or -1
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 42/117:
  -> INFO: Now checking 10 results for matching title: 'Improving KernelSHAP: Practical Shapley Value Estimation via Linear Regression'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 43/117:
  -> INFO: Now checking 10 results for matching title: 'On the Reasons Behind Decisions'
       -> INFO: All authors matched!
- Checking reference 44/117:
  -> INFO: Now checking 2 results for matching title: 'On the Computation of Necessary and Sufficient Explanations'
       -> INFO: All authors matched!
- Checking reference 45/117:
  -> INFO: Now checking 1 results for matching title: 'Computing the Shapley Value of Facts in Query Answering'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 46/117:
  -> INFO: Now checking 10 results for matching title: 'Parameterized complexity'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Downey', 'Fellows', '2012']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Parameterized+complexity manually and check the results.
        -> Author(s): Rodney G Downey and Michael Ralph Fellows
        -> Title:     Parameterized complexity
        -> Year:      2012
     -> Manual search was skipped by the user.
- Checking reference 47/117:
  -> INFO: Now checking 10 results for matching title: 'InstaSHAP: Interpretable Additive Models Explain Shapley Values Instantly'
       -> INFO: All authors matched!
- Checking reference 48/117:
  -> INFO: Now checking 10 results for matching title: 'Parameterized Complexity Theory'
       -> INFO: All authors matched!
- Checking reference 49/117:
  -> INFO: Now checking 1 results for matching title: 'Shapley Values for Feature Selection: The Good, the Bad, and the Axioms'
       -> INFO: All authors matched!
- Checking reference 50/117:
  -> INFO: Now checking 2 results for matching title: 'SHAP-IQ: Unified Approximation of Any-Order Shapley Interactions'
       -> INFO: All authors matched!
- Checking reference 51/117:
  -> INFO: Now checking 1 results for matching title: 'KernelSHAP-IQ: Weighted Least Square Optimization for Shapley Interactions'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Fumagalli', 'Muschalik', 'Kolpaczki', 'Hüllermeier', 'Hammer', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=KernelSHAP-IQ:+Weighted+Least+Square+Optimization+for+Shapley+Interactions manually and check the results.
        -> Author(s): Fabian Fumagalli, Maximilian Muschalik, Patrick Kolpaczki, Eyke Hüllermeier, and Barbara Hammer
        -> Title:     KernelSHAP-IQ: Weighted Least Square Optimization for Shapley Interactions
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 52/117:
  -> INFO: Now checking 1 results for matching title: 'Expressive Power of Tensor-Network Factorizations for Probabilistic Modeling'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Glasser', 'Sweke', 'Pancotti', 'Eisert', 'Cirac', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Expressive+Power+of+Tensor-Network+Factorizations+for+Probabilistic+Modeling manually and check the results.
        -> Author(s): Ivan Glasser, Ryan Sweke, Nicola Pancotti, Jens Eisert, and Ignacio Cirac
        -> Title:     Expressive Power of Tensor-Network Factorizations for Probabilistic Modeling
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 53/117:
  -> INFO: Now checking 10 results for matching title: 'Sequence Processing with Quantum-Inspired Tensor Networks'
       -> INFO: All authors matched!
- Checking reference 54/117:
  -> INFO: Now checking 10 results for matching title: 'Exploring Unexplored Tensor Network Decompositions for Convolutional Neural Networks'
       -> INFO: All authors matched!
- Checking reference 55/117:
  -> INFO: Now checking 3 results for matching title: 'Causal Shapley Values: Exploiting Causal Knowledge to Explain Individual Predictions of Complex Models'
       -> INFO: All authors matched!
- Checking reference 56/117:
  -> INFO: Now checking 10 results for matching title: 'Introduction to Automata Theory, Languages, and Computation'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hopcroft', 'Motwani', 'Ullman', '2006']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Introduction+to+Automata+Theory%2C+Languages%2C+and+Computation manually and check the results.
        -> Author(s): John E  Hopcroft, Rajeev Motwani, and Jeffrey D  Ullman
        -> Title:     Introduction to Automata Theory, Languages, and Computation
        -> Year:      2006
     -> Manual search was skipped by the user.
- Checking reference 57/117:
  -> INFO: Now checking 1 results for matching title: 'On the Failings of Shapley Values for Explainability'
       -> INFO: All authors matched!
- Checking reference 58/117:
  -> INFO: Now checking 10 results for matching title: 'Updates on the Complexity of SHAP Scores'
       -> INFO: All authors matched!
- Checking reference 59/117:
  -> INFO: Now checking 10 results for matching title: 'Towards Trustable Explainable AI'
       -> INFO: All authors matched!
- Checking reference 60/117:
  -> INFO: Now checking 10 results for matching title: 'Abduction-based Explanations for Machine Learning Models'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 61/117:
  -> INFO: Now checking 10 results for matching title: 'Distance-Restricted Explanations: Theoretical Underpinnings & Efficient implementation'
       -> INFO: All authors matched!
- Checking reference 62/117:
  -> INFO: Now checking 2 results for matching title: 'Feature Relevance Quantification in Explainable AI: A causal Problem'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Janzing', 'Minorics', 'Blöbaum', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Feature+Relevance+Quantification+in+Explainable+AI:+A+causal+Problem manually and check the results.
        -> Author(s): Dominik Janzing, Lenon Minorics, and Patrick Blöbaum
        -> Title:     Feature Relevance Quantification in Explainable AI: A causal Problem
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 63/117:
  -> INFO: Now checking 10 results for matching title: 'FastSHAP: Real-time Shapley Value Estimation'
       -> INFO: All authors matched!
- Checking reference 64/117:
  -> INFO: Now checking 10 results for matching title: 'Efficient Exact Verification of Binarized Neural Networks'
       -> INFO: All authors matched!
- Checking reference 65/117:
  -> Checking if provided link is pingable: https://arXiv:2504.13787.
  -> INFO: Now checking 10 results for matching title: 'Probabilistic Stability Guarantees for Feature Attributions'
       -> INFO: All authors matched!
- Checking reference 66/117:
  -> INFO: Now checking 8 results for matching title: 'From Shapley Value to Model Counting and Back'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 67/117:
  -> INFO: Now checking 8 results for matching title: 'From Shapley Value to Model Counting and Back'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 68/117:
  -> INFO: Now checking 1 results for matching title: 'Expected Shapleylike Scores of Boolean Functions: Complexity and Applications to Probabilistic Databases'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Karmakar', 'Monet', 'Senellart', 'Bressan', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Expected+Shapleylike+Scores+of+Boolean+Functions:+Complexity+and+Applications+to+Probabilistic+Databases manually and check the results.
        -> Author(s): Pratik Karmakar, Mikaël Monet, Pierre Senellart, and Stéphane Bressan
        -> Title:     Expected Shapleylike Scores of Boolean Functions: Complexity and Applications to Probabilistic Databases
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 69/117:
  -> INFO: Now checking 3 results for matching title: 'Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks'
       -> INFO: All authors matched!
- Checking reference 70/117:
  -> INFO: Now checking 10 results for matching title: 'Challenging the Performance-Interpretability Trade-Off: An Evaluation of Interpretable Machine Learning Models'
       -> INFO: All authors matched!
- Checking reference 71/117:
  -> INFO: Now checking 7 results for matching title: 'Problems with Shapley-Value-based Explanations as Feature Importance Measures'
       -> INFO: All authors matched!
- Checking reference 72/117:
  -> INFO: Now checking 10 results for matching title: 'Towards Trustable SHAP Scores'
       -> INFO: All authors matched!
- Checking reference 73/117:
  -> INFO: Now checking 10 results for matching title: 'Boltzmann Machines as Two-Dimensional Tensor Networks'
       -> INFO: All authors matched!
- Checking reference 74/117:
  -> INFO: Now checking 10 results for matching title: 'Entanglement-Based Feature Extraction by Tensor Network Machine Learning'
       -> INFO: All authors matched!
- Checking reference 75/117:
  -> INFO: Now checking 1 results for matching title: 'The Shapley Value of Tuples in Query Answering'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 76/117:
  -> INFO: Now checking 10 results for matching title: 'A Unified Approach to Interpreting Model Predictions'
       -> INFO: All authors matched!
- Checking reference 77/117:
  -> INFO: Now checking 9 results for matching title: 'From Local Explanations to Global Understanding with Explainable AI for Trees'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Erion-Barner, DeGrave, Prutkin, Nair, Katz, Himmelfarb, Bansal'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 78/117:
  -> INFO: Now checking 6 results for matching title: 'Cost-Efficient Gaussian Tensor Network Embeddings for Tensor-Structured Inputs'
       -> INFO: All authors matched!
- Checking reference 79/117:
  -> INFO: Now checking 10 results for matching title: 'Logic-based Explainability in Machine Learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 80/117:
  -> INFO: Now checking 10 results for matching title: 'Explainability is NOT a Game'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 81/117:
  -> INFO: Now checking 10 results for matching title: 'Parallelizing Linear Recurrent Neural Nets Over Sequence Length'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 82/117:
  -> INFO: Now checking 1 results for matching title: 'On the Tractability of SHAP Explanations under Markovian Distributions'
       -> INFO: All authors matched!
- Checking reference 83/117:
  -> INFO: Now checking 2 results for matching title: 'On the Computational Tractability of the (Many) Shapley Values'
       -> INFO: All authors matched!
- Checking reference 84/117:
  -> INFO: Now checking 10 results for matching title: 'Tensor Networks for Probabilistic Sequence Modeling'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 85/117:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2010.13972.
  -> INFO: Now checking 1 results for matching title: 'GPUTreeShap: Massively Parallel Exact Calculation of SHAP Scores for Tree Ensembles'
       -> INFO: All authors matched!
- Checking reference 86/117:
  -> INFO: Now checking 10 results for matching title: 'Sampling Permutations for Shapley Value Estimation'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 87/117:
  -> INFO: Now checking 2 results for matching title: 'Beyond TreeSHAP: Efficient Computation of Any-Order Shapley Interactions for Tree Ensembles'
       -> INFO: All authors matched!
- Checking reference 88/117:
  -> INFO: Now checking 1 results for matching title: 'Exact Computation of AnyOrder Shapley Interactions for Graph Neural Networks'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Muschalik', 'Fumagalli', 'Frazzetto', 'Strotherm', 'Hermes', 'Sperduti', 'Hüllermeier', 'Hammer', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Exact+Computation+of+AnyOrder+Shapley+Interactions+for+Graph+Neural+Networks manually and check the results.
        -> Author(s): Maximilian Muschalik, Fabian Fumagalli, Paolo Frazzetto, Janine Strotherm, Luca Hermes, Alessandro Sperduti, Eyke Hüllermeier, and Barbara Hammer
        -> Title:     Exact Computation of AnyOrder Shapley Interactions for Graph Neural Networks
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 89/117:
  -> INFO: Now checking 8 results for matching title: 'Provably Accurate Shapley Value Estimation via Leverage Score Sampling'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 90/117:
  -> INFO: Now checking 10 results for matching title: 'Tensorizing Neural Networks'
       -> INFO: All authors matched!
- Checking reference 91/117:
  -> INFO: Now checking 10 results for matching title: 'Tensor-Train Density Estimation'
       -> INFO: All authors matched!
- Checking reference 92/117:
  -> INFO: Now checking 1 results for matching title: 'The Parameterized Complexity of Finding Concise Local Explanations'
       -> INFO: All authors matched!
- Checking reference 93/117:
  -> INFO: Now checking 5 results for matching title: 'SIAM Journal on Scientific Computing, 33(5): 2295–2317.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Oseledets', 'Decomposition', '2011']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=SIAM+Journal+on+Scientific+Computing%2C+33(5):+2295–2317. manually and check the results.
        -> Author(s): V  Oseledets, I ˙Tensor-Train Decomposition
        -> Title:     SIAM Journal on Scientific Computing, 33(5): 2295–2317.
        -> Year:      2011
     -> Manual search was skipped by the user.
- Checking reference 94/117:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1710.10248.
  -> INFO: Now checking 10 results for matching title: 'Tensor Network Language Model.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Pestun', 'Vlassopoulos', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Tensor+Network+Language+Model. manually and check the results.
        -> Author(s): Vasily Pestun and Yiannis Vlassopoulos
        -> Title:     Tensor Network Language Model.
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 95/117:
  -> INFO: Now checking 4 results for matching title: 'Connecting Weighted Automata and Recurrent Neural Networks through Spectral Learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 96/117:
  -> INFO: Now checking 3 results for matching title: 'Tensor Networks for Interpretable and Efficient Quantum-Inspired Machine Learning'
       -> INFO: All authors matched!
- Checking reference 97/117:
  -> INFO: Now checking 1 results for matching title: 'Probabilistic Inference in the Era of Tensor Networks and Differential Programming'
       -> INFO: All authors matched!
- Checking reference 98/117:
  -> INFO: Now checking 10 results for matching title: 'Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 99/117:
  -> INFO: Now checking 10 results for matching title: 'Tensor Networks for Medical Image Classification'
       -> INFO: All authors matched!
- Checking reference 100/117:
  -> INFO: Now checking 10 results for matching title: 'Fooling LIME and SHAP: Adversarial Attacks on Post Hoc Explanation Methods'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 101/117:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: NP-Hardness of Optimal TensorNetwork Contraction and Polynomial-Time Algorithms for Tree Tensor Networks
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Stoian', 'Milbradt', 'Mendl', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=NP-Hardness+of+Optimal+TensorNetwork+Contraction+and+Polynomial-Time+Algorithms+for+Tree+Tensor+Networks manually and check the results.
        -> Author(s): Mihail Stoian, Richard Milbradt, and Christian Mendl
        -> Title:     NP-Hardness of Optimal TensorNetwork Contraction and Polynomial-Time Algorithms for Tree Tensor Networks
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 102/117:
  -> INFO: Now checking 10 results for matching title: 'Supervised Learning with Tensor Networks'
       -> INFO: All authors matched!
- Checking reference 103/117:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2405.04590.
  -> INFO: Now checking 10 results for matching title: 'Language Modeling Using Tensor Trains.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Su', 'Zhou', 'Mo', 'Simonsen', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Language+Modeling+Using+Tensor+Trains. manually and check the results.
        -> Author(s): Zhan Su, Yuqin Zhou, Fengran Mo, and Jakob Grue Simonsen
        -> Title:     Language Modeling Using Tensor Trains.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 104/117:
  -> INFO: Now checking 10 results for matching title: 'The Many Shapley Values for Model Explanation'
       -> INFO: All authors matched!
- Checking reference 105/117:
  -> INFO: Now checking 10 results for matching title: 'The Shapley Taylor Interaction Index'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 106/117:
  -> INFO: Now checking 10 results for matching title: 'Manifold Restricted Interventional Shapley Values'
       -> INFO: All authors matched!
- Checking reference 107/117:
  -> INFO: Now checking 10 results for matching title: 'On the Tractability of SHAP Explanations'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 108/117:
  -> INFO: Now checking 10 results for matching title: 'The Computational Complexity of Understanding Binary Classifier Decisions'
       -> INFO: All authors matched!
- Checking reference 109/117:
  -> INFO: Now checking 2 results for matching title: 'Beta-Crown: Efficient Bound Propagation with Per-Neuron Split Constraints for Neural Network Robustness Verification'
       -> INFO: All authors matched!
- Checking reference 110/117:
  -> INFO: Now checking 10 results for matching title: 'Marabou 2'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'Isac', 'Zelji´c', 'Tagomori', 'Daggitt', 'Kokke', 'Refaeli', 'Amir', 'Julian', 'Bassan', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Marabou+2 manually and check the results.
        -> Author(s): Haoze Wu, Omri Isac, Aleksandar Zelji´c, Teruhiro Tagomori, Matthew Daggitt, Wen Kokke, Idan Refaeli, Guy Amir, Kyle Julian, Shahaf Bassan, et al
        -> Title:     Marabou 2
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 111/117:
  -> INFO: Now checking 10 results for matching title: 'Complexity of Optimal Tensor Network Contraction Sequences'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Xu', 'Li', 'Zhao', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Complexity+of+Optimal+Tensor+Network+Contraction+Sequences manually and check the results.
        -> Author(s): Jianyu Xu, Wei Li, and Ming Zhao
        -> Title:     Complexity of Optimal Tensor Network Contraction Sequences
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 112/117:
  -> INFO: Now checking 1 results for matching title: 'Stability Guarantees for Feature Attributions with Multiplicative Smoothing'
       -> INFO: All authors matched!
- Checking reference 113/117:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2109.09847.
  -> INFO: Now checking 2 results for matching title: 'Fast TreeSHAP: Accelerating SHAP Value Computation for Trees'
       -> WARNING: Not all 1 authors from the found ref. were matched (only 1)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 114/117:
  -> INFO: Now checking 8 results for matching title: 'Anytime Approximate Formal Feature Attribution'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 115/117:
  -> INFO: Now checking 10 results for matching title: 'Linear TreeSHAP'
       -> INFO: All authors matched!
- Checking reference 116/117:
  -> INFO: Now checking 4 results for matching title: 'Interventional SHAP Values and Interaction Values for Piecewise Linear Regression Trees'
       -> INFO: All authors matched!
- Checking reference 117/117:
  -> Checking if provided link is pingable: https://nips.cc/public/guides/CodeSubmissionPolicy)
  -> INFO: Now checking 10 results for matching title: 'Explaining Prediction Models and Individual Predictions with Feature Contributions'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: VM(x, S ∪{i}; P) −VM(x, S; P)
-> Invalid unicode use found on p. 2: def= |S|!(nin−|S|−1)!
-> Invalid unicode use found on p. 3: Ti1,...,ij−1,:,ij+1,...,in is a vector in Rdj whose k-th entry is equal to Ti1,...,ij−1,k,ij+1,...,in for k ∈[dj].
-> Invalid unicode use found on p. 3: Rd1×...di−1×di+1×...×dn×d′
-> Invalid unicode use found on p. 3: j−1×d′
-> Invalid unicode use found on p. 3: a1,...,ai−1,ai+1,...,an,b1,...,bj−1,bj+1,...,bm
-> Invalid unicode use found on p. 3: a1,...,ai−1,k,ai+1,...,am · T (2)
-> Invalid unicode use found on p. 3: b1,...,bj−1,k,bj+1,...,bn
-> Invalid unicode use found on p. 3: core T (i) ∈Rdi−1×Ni×di. The TT T corresponds to a tensor in Rd0×N1×...×Nn×dn obtained by
-> Invalid unicode use found on p. 4: are constrained to binary values, typically {−1, +1}. In a BNN, each layer performs a sequence of
-> Invalid unicode use found on p. 4: an input vector x ∈{−1, +1}n, the output y ∈{−1, +1}m of a layer is computed as follows [41]:
-> Invalid unicode use found on p. 4: z′ = γ · z −µ
-> Invalid unicode use found on p. 4: W ∈{−1, +1}m×n, b ∈Rm, and γ, β, µ, σ ∈Rm are the batch normalization parameters. The
-> Invalid unicode use found on p. 4: sign function is applied element-wise, mapping positive inputs to +1 and non-positive inputs to −1.
-> Invalid unicode use found on p. 4: a constraint: for binary inputs xj and weights wij ∈{−1, +1}, define lij = xj if wij = +1, and
-> Invalid unicode use found on p. 4: def= −W(s −1nin) if si = 1, and
-> Invalid unicode use found on p. 4: def= W(s −1nin) otherwise. Moreover, define the marginal value tensor V(M,P ) ∈
-> Invalid unicode use found on p. 5: i for any i ∈[2, nin −1], and
-> Invalid unicode use found on p. 5: def= {(5 −k) · i, i) : i ∈
-> Invalid unicode use found on p. 25: t−1.
-> Invalid unicode use found on p. 26: ht = T ×(1,1) ht−1 ×(2,1) eN
-> Invalid unicode use found on p. 26: xt + Uht−1 + b
-> Invalid unicode use found on p. 26: Where ht−1 is the hidden state vector of the RNN after reading the prefix x1:y of the input sequence,
-> Invalid unicode use found on p. 26: Rd1×...di−1×di+1×...×dn×d′
-> Invalid unicode use found on p. 26: j−1×d′
-> Invalid unicode use found on p. 26: a1,...,ai−1,ai+1,...,an,b1,...,bj−1,bj+1,...,bm
-> Invalid unicode use found on p. 26: a1,...,ai−1,k,ai+1,...,am · T (2)
-> Invalid unicode use found on p. 26: b1,...,bj−1,k,bj+1,...,bn
-> Invalid unicode use found on p. 27: Pi−1
-> Invalid unicode use found on p. 27: (ij −1) Qq(i)
-> Invalid unicode use found on p. 27: G(k) ∈Rrk−1 × d × rk,
-> Invalid unicode use found on p. 27: rk = d (1 ≤k ≤n −1)
-> Invalid unicode use found on p. 27: αk−1, ik, αk := Jαk−1 = ikK · Jαk = ikK
-> Invalid unicode use found on p. 27: α1,...,αn−1=1
-> Invalid unicode use found on p. 27: αn−1,in,1.
-> Invalid unicode use found on p. 27: Since each core enforces αk−1 = ik = αk, the only nonzero term in the sum occurs when i1 = · · · =
-> Invalid unicode use found on p. 28: l+1 = δ(sl−1
-> Invalid unicode use found on p. 29: layer l ∈[L −1], the TT whose parameterization is given in equation (11) simulates exactly the
-> Invalid unicode use found on p. 30: def= −W(s −1nin) if si = 1, and
-> Invalid unicode use found on p. 30: def= W(s −1nin) otherwise. Moreover, define the marginal value tensor V(M,P ) ∈
-> Invalid unicode use found on p. 31: VM(x, swap(s, i); P) −VM(x, s; P)
-> Invalid unicode use found on p. 31: W(s) · VM(x, s; P) −
-> Invalid unicode use found on p. 31: −W(s)
-> Invalid unicode use found on p. 31: i for any i ∈[2, nin −1], and
-> Invalid unicode use found on p. 31: −W(˜s −1nin)
-> Invalid unicode use found on p. 31: W(˜s −1nin)
-> Invalid unicode use found on p. 31: ˜s ∈[2]n and an integer i ∈N, and outputs 1 if [(˜si = 1) ∨(n ≤i −1)], −1 otherwise. The function
-> Invalid unicode use found on p. 31: −∆(˜s, i)
-> Invalid unicode use found on p. 31: if |˜s| = i −1 ∧σ = 1
-> Invalid unicode use found on p. 32: (−1)Ji=1K · (nin −1)!
-> Invalid unicode use found on p. 32: (nin −2)!
-> Invalid unicode use found on p. 32: (−1)Jj=iK
-> Invalid unicode use found on p. 32: j·(nin−k−1)
-> Invalid unicode use found on p. 33: (−1)∆(˜s1:j,i) · |˜s1:j|!(nin−|˜s1:j|−1)!
-> Invalid unicode use found on p. 33: General Case. Assume Equation (17) holds for j ∈[nin −1], we need to show that it’s also valid for
-> Invalid unicode use found on p. 33: = (−1)∆(˜s1:j,i) · |˜si:j|! · (nin −|˜s1:j| −1)!
-> Invalid unicode use found on p. 33: i,s1,...,sj+1,i,|s1:j+1| = (−1)∆(s1:j,i) · |si:j|! · (nin −|s1:j| −1)!
-> Invalid unicode use found on p. 33: · (−1)[i=j+1]
-> Invalid unicode use found on p. 33: = (−1)∆(s1:j+1,i) · |si:j+1|! · (nin −|s1:j+1| −1)!
-> Invalid unicode use found on p. 33: i,s1,...,sj+1,i,|s1:j+1| = (−1)∆(s1:j+1,i) · |s1:j|! · (nin −|s1:j+1|)!
-> Invalid unicode use found on p. 33: (j + 1) · (nin −|s1:j+1|)
-> Invalid unicode use found on p. 33: = (−1)∆(s1:j+1,i) · |s1:j+1|! · (nin −|s1:j+1| −1)!
-> Invalid unicode use found on p. 34: of the factorial terms (nin −1)! and (nin −2)!. This operation can be performed using a parallel
-> Invalid unicode use found on p. 34: def= {(5 −k) · i, i) :
-> Invalid unicode use found on p. 36: = H2·(i−1)
-> Invalid unicode use found on p. 36: j−1
-> Invalid unicode use found on p. 36: j−1
-> Invalid unicode use found on p. 36: def= {(7 −k, k) : k ∈[3]}.
-> Invalid unicode use found on p. 37: ht−1
-> Invalid unicode use found on p. 38: (nin−2)times
-> Invalid unicode use found on p. 39: I(1) ×(1,1) 1L, , I(2), . . . , I(nin−1), I(nin) ×(3,1) 1L
-> Invalid unicode use found on p. 40: negatively, the weight is −1. Each hidden neuron is assigned a bias of 3
-> Invalid unicode use found on p. 40: output neuron with a bias of −(m −1
-> Invalid unicode use found on p. 41: if the remaining two inputs contribute −1 each, the total input is 5
-> Invalid unicode use found on p. 41: 2 −2 = 1
-> Invalid unicode use found on p. 41: neuron has a bias of −(m −1
-> Invalid unicode use found on p. 41: Let w = (w1, . . . wn) ∈{−1, 1}n be the weight parameters of a BNN with a single output neuron
-> Invalid unicode use found on p. 41: • Transition function: For a layer l ∈[n −1],
-> Invalid unicode use found on p. 41: if (r ̸= R) ∧[(wl = 1 ∧σ = 1) ∨(wl = −1 ∧σ = 0)]
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Bracket content ['N1'] on p. 3 could not be matched to a reference.
   -> Sentence:  Fix a discrete input space D = [N1] × [N2] × · · · × [Nnin], a model M : D →Rnout, and a probability distribution
P over D
-> Warning: Bracket content ['N2'] on p. 3 could not be matched to a reference.
   -> Sentence:  Fix a discrete input space D = [N1] × [N2] × · · · × [Nnin], a model M : D →Rnout, and a probability distribution
P over D
-> Warning: Bracket content ['nin + 1'] on p. 5 could not be matched to a reference.
   -> Sentence:  ◦e Nnin xnin i (3) where S def= n (k, k) : k ∈[nin + 1] o 
-> Warning: Numeric reference range couldn't be parsed as Integers: ['2', ' nin −1']
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 371 sentences on 10 pages -> Avg. of 42.22222222222222 sentences per page
-> Warning: Reference '1' never used in the document's text.
-> Warning: Reference '5' never used in the document's text.
-> Warning: Reference '8' never used in the document's text.
-> Warning: Reference '9' never used in the document's text.
-> Warning: Reference '11' never used in the document's text.
-> Warning: Reference '12' never used in the document's text.
-> Warning: Reference '13' never used in the document's text.
-> Warning: Reference '14' never used in the document's text.
-> Warning: Reference '15' never used in the document's text.
-> Warning: Reference '16' never used in the document's text.
-> Warning: Reference '17' never used in the document's text.
-> Warning: Reference '18' never used in the document's text.
-> Warning: Reference '19' never used in the document's text.
-> Warning: Reference '20' never used in the document's text.
-> Warning: Reference '21' never used in the document's text.
-> Warning: Reference '23' never used in the document's text.
-> Warning: Reference '26' never used in the document's text.
-> Warning: Reference '27' never used in the document's text.
-> Warning: Reference '29' never used in the document's text.
-> Warning: Reference '30' never used in the document's text.
-> Warning: Reference '33' never used in the document's text.
-> Warning: Reference '38' never used in the document's text.
-> Warning: Reference '40' never used in the document's text.
-> Warning: Reference '43' never used in the document's text.
-> Warning: Reference '44' never used in the document's text.
-> Warning: Reference '45' never used in the document's text.
-> Warning: Reference '47' never used in the document's text.
-> Warning: Reference '55' never used in the document's text.
-> Warning: Reference '56' never used in the document's text.
-> Warning: Reference '59' never used in the document's text.
-> Warning: Reference '60' never used in the document's text.
-> Warning: Reference '61' never used in the document's text.
-> Warning: Reference '65' never used in the document's text.
-> Warning: Reference '66' never used in the document's text.
-> Warning: Reference '68' never used in the document's text.
-> Warning: Reference '69' never used in the document's text.
-> Warning: Reference '75' never used in the document's text.
-> Warning: Reference '79' never used in the document's text.
-> Warning: Reference '80' never used in the document's text.
-> Warning: Reference '88' never used in the document's text.
-> Warning: Reference '92' never used in the document's text.
-> Warning: Reference '105' never used in the document's text.
-> Warning: Reference '106' never used in the document's text.
-> Warning: Reference '108' never used in the document's text.
-> Warning: Reference '109' never used in the document's text.
-> Warning: Reference '110' never used in the document's text.
-> Warning: Reference '112' never used in the document's text.
---
-> WARNING: Reference with index 0 (Ref. ID = 1) has no associated sentence!
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> WARNING: Reference with index 8 (Ref. ID = 9) has no associated sentence!
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> WARNING: Reference with index 10 (Ref. ID = 11) has no associated sentence!
-> WARNING: Reference with index 11 (Ref. ID = 12) has no associated sentence!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> WARNING: Reference with index 13 (Ref. ID = 14) has no associated sentence!
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> WARNING: Reference with index 26 (Ref. ID = 27) has no associated sentence!
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
-> Missing an abstract for reference with index 40 (Ref. ID = 41); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> WARNING: Reference with index 44 (Ref. ID = 45) has no associated sentence!
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
-> Missing an abstract for reference with index 57 (Ref. ID = 58); Skipping LLM check...
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> WARNING: Reference with index 59 (Ref. ID = 60) has no associated sentence!
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
-> Missing an abstract for reference with index 61 (Ref. ID = 62); Skipping LLM check...
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
-> WARNING: Reference with index 65 (Ref. ID = 66) has no associated sentence!
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 67 (Ref. ID = 68); Skipping LLM check...
-> Missing an abstract for reference with index 68 (Ref. ID = 69); Skipping LLM check...
-> Missing an abstract for reference with index 69 (Ref. ID = 70); Skipping LLM check...
-> Missing an abstract for reference with index 70 (Ref. ID = 71); Skipping LLM check...
-> Missing an abstract for reference with index 71 (Ref. ID = 72); Skipping LLM check...
-> Missing an abstract for reference with index 72 (Ref. ID = 73); Skipping LLM check...
-> Missing an abstract for reference with index 73 (Ref. ID = 74); Skipping LLM check...
-> WARNING: Reference with index 74 (Ref. ID = 75) has no associated sentence!
-> Missing an abstract for reference with index 75 (Ref. ID = 76); Skipping LLM check...
-> Missing an abstract for reference with index 76 (Ref. ID = 77); Skipping LLM check...
-> Missing an abstract for reference with index 77 (Ref. ID = 78); Skipping LLM check...
-> WARNING: Reference with index 78 (Ref. ID = 79) has no associated sentence!
-> WARNING: Reference with index 79 (Ref. ID = 80) has no associated sentence!
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 81 (Ref. ID = 82); Skipping LLM check...
-> Missing an abstract for reference with index 82 (Ref. ID = 83); Skipping LLM check...
-> Missing an abstract for reference with index 83 (Ref. ID = 84); Skipping LLM check...
-> Missing an abstract for reference with index 84 (Ref. ID = 85); Skipping LLM check...
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 86 (Ref. ID = 87); Skipping LLM check...
-> Missing an abstract for reference with index 87 (Ref. ID = 88); Skipping LLM check...
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 89 (Ref. ID = 90); Skipping LLM check...
-> Missing an abstract for reference with index 90 (Ref. ID = 91); Skipping LLM check...
-> Missing an abstract for reference with index 91 (Ref. ID = 92); Skipping LLM check...
-> Missing an abstract for reference with index 92 (Ref. ID = 93); Skipping LLM check...
-> Missing an abstract for reference with index 93 (Ref. ID = 94); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 95 (Ref. ID = 96); Skipping LLM check...
-> Missing an abstract for reference with index 96 (Ref. ID = 97); Skipping LLM check...
-> Missing an abstract for reference with index 97 (Ref. ID = 98); Skipping LLM check...
-> Missing an abstract for reference with index 98 (Ref. ID = 99); Skipping LLM check...
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 100 (Ref. ID = 101); Skipping LLM check...
-> Missing an abstract for reference with index 101 (Ref. ID = 102); Skipping LLM check...
-> Missing an abstract for reference with index 102 (Ref. ID = 103); Skipping LLM check...
-> Missing an abstract for reference with index 103 (Ref. ID = 104); Skipping LLM check...
-> WARNING: Reference with index 104 (Ref. ID = 105) has no associated sentence!
-> Missing an abstract for reference with index 105 (Ref. ID = 106); Skipping LLM check...
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 107 (Ref. ID = 108); Skipping LLM check...
-> Missing an abstract for reference with index 108 (Ref. ID = 109); Skipping LLM check...
-> Missing an abstract for reference with index 109 (Ref. ID = 110); Skipping LLM check...
-> Missing an abstract for reference with index 110 (Ref. ID = 111); Skipping LLM check...
-> Missing an abstract for reference with index 111 (Ref. ID = 112); Skipping LLM check...
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 17
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 114 (Ref. ID = 115); Skipping LLM check...
-> Missing an abstract for reference with index 115 (Ref. ID = 116); Skipping LLM check...
-> Missing an abstract for reference with index 116 (Ref. ID = 117); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 5 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 11 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 51 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 42 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 42 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 293 matches in this ranking!
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
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 22
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\24 SHAP Meets Tensor Networks\PAU_results.md
```