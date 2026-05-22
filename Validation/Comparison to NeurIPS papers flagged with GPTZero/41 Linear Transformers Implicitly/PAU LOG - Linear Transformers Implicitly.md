
Note: This paper uses a new referencing style => Same as "When and How"
- "(Schulz, 1933; Ben-Israel, 1965; Higham, 2008; Fu et al., 2024)"
BUT it uses a different bib layout than the other NeurIPS papers:
- LFYTO but comma separated authors!!

---

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\41 Linear Transformers Implicitly\Linear Transformers Implicitly Discover Unified Numerical Algorithms.pdf"
---
INFO:
 - 'springer' = Has two headerlines to skip (1st = Shortitle/Author; 2nd = page number)
 - 'acm'      = Has no headerlines to skip
Enter a supported formatting template (['springer', 'acm']): acm
---
INFO:
 - 'LFTOY' = Lastname, Firstname, Title, Outlet, Year
            -> This is, for example, used by Springer Nature
 - 'LFYTO' = Lastname, Firstname, Year, Title, Outlet
            -> This is, for example, used by the AAAI/ACM Conference
 - 'FLYTO' = Firstname, Lastname, Year, Title, Outlet
            -> This is, for example, used by ACM
 - 'FLTOY' = Firstname, Lastname, Title, Outlet, Year
            -> This is, for example, used by most papers of the NeurIPS Conference
Enter a supported bibliography layout (['LFTOY', 'LFYTO', 'FLYTO', 'FLTOY']): LFflYTO
ERROR: Biblography layout 'LFflYTO' not supported yet!
 -> The programm will exit now. :)
PS C:\Users\pauli\OneDrive - tu-dortmund.de\Dokumente\Git_Projekte\LitChecker> 
PS C:\Users\pauli\OneDrive - tu-dortmund.de\Dokumente\Git_Projekte\LitChecker> & C:\Users\pauli\AppData\Local\Microsoft\WindowsApps\python3.10.exe "c:/Users/pauli/OneDrive - tu-dortmund.de/Dokumente/Git_Projekte/LitChecker/PAU.py"
Enter the path to the PDF file: "C:\Users\pauli\Sciebo\Paupis_Privatstuff\PhD_Notes\Paper-Projekte\PQC\PAU - All  GPTZero NeurIPS Paper with H\41 Linear Transformers Implicitly\Linear Transformers Implicitly Discover Unified Numerical Algorithms.pdf"
---
INFO:
 - 'springer' = Has two headerlines to skip (1st = Shortitle/Author; 2nd = page number)
 - 'acm'      = Has no headerlines to skip
Enter a supported formatting template (['springer', 'acm']): acm
---
INFO:
 - 'LFTOY' = Lastname, Firstname, Title, Outlet, Year
            -> This is, for example, used by Springer Nature
 - 'LFYTO' = Lastname, Firstname, Year, Title, Outlet
            -> This is, for example, used by the AAAI/ACM Conference
 - 'FLYTO' = Firstname, Lastname, Year, Title, Outlet
            -> This is, for example, used by ACM
 - 'FLTOY' = Firstname, Lastname, Title, Outlet, Year
            -> This is, for example, used by most papers of the NeurIPS Conference
Enter a supported bibliography layout (['LFTOY', 'LFYTO', 'FLYTO', 'FLTOY']): LFYTO
# PLEASE NOTE:
 -> The chosen bib layout uses ';' to separate multiple authors.
 => If that is correct, please press enter or type 'y', otherwise enter another author-separator to use: ,
... ',' as author separator accepted!
---
INFO:
 - 'natbib'           = No numbering; reference in 'References' section starts with the authors' names
 - 'numbered_squares' = Reference in 'References' section starts with, e.g., '[1]'
 - 'number_with_dot'  = Reference in 'References' section starts with, e.g., '1.'
Enter a supported bibliography numbering (['natbib', 'numbered_squares', 'number_with_dot']): natbib
---
INFO:
 - 'numeric'     = A number placed inside square brackets (e.g., [28])
                -> Multiple references are separated by a comma (e.g., [28,29])
 - 'authoryear'  = Authors' names and the year places insince brackets with or withou a comma in between (e.g., (Dignum et al., 2025))
                -> Multiple references are separated by a semicolon or comma (e.g., (Dignum et al. 2025; Caliskan et al. 2017))
Enter a supported referencing template (['numeric', 'authoryear']): authoryear
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Related Work' on page 2
- Found following heading '3 - Method' on page 3
- Found following heading '4 - Emergent Algorithm' on page 5
- Found following heading '5 - Evaluation of EAGLE' on page 8
- Found following heading '6 - Conclusions' on page 10
=> Found references/literature section on page 12
- Found first appendix 'A - Methodological Details' on page 15
- Found following appendix 'B - D' on page 15
- Found following appendix 'C - B' on page 15
- Found following appendix 'D - Further Details on Evaluation of EAGLE' on page 22
- Found following appendix 'E - Theoretical Analyses' on page 26
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 12 -- 15
All found references: 35
-> Warning: Malformed author string: ['Mechanics/Zeitschrift für Angewandte Mathematik und Mechanik', '13(1):57-59. 7 Siegelmann', 'H. T.', 'Sontag', 'E. D']
-----------
 -> Parsed references DataFrame:
                               ref_id                                            authors  ...                                link  valid
0                      Ahn et al 2023    Ahn, K., Cheng, X., Daneshmand, H., and Sra, S.  ...                                       None
1                  Akyürek et al 2022  Akyürek, E., Schuurmans, D., Andreas, J., Ma, ...  ...                                       None
2                      Bai et al 2023  Bai, Y., Chen, F., Wang, H., Xiong, C., and Me...  ...                                       None
3                     Ben-Israel 1965                                     Ben-Israel, A.  ...                                       None
4                    Brown et al 2020  Brown, T., Mann, B., Ryder, N., Subbiah, M., K...  ...                                       None
5               Candès and Recht 2009                        Candès, E. J. and Recht, B.  ...                                       None
6                 Candès and Tao 2010                          Candès, E. J. and Tao, T.  ...                                       None
7                   Transactions 2053          Transactions on Information Theory, 56(5)  ...                                       None
8                     Chen et al 2020            Chen, Y., Fan, J., Ma, C., and Wang, K.  ...                                       None
9          Clarkson and Woodruff 2017                Clarkson, K. L. and Woodruff, D. P.  ...                                       None
10                    Daneshmand 2024                                     Daneshmand, H.  ...                                       None
11         Davenport and Romberg 2016                   Davenport, M. A. and Romberg, J.  ...                                       None
12                  Demmel et al 2013  Demmel, J., Grigori, L., Hoemmen, M., and Lang...  ...                                       None
13                      Fu et al 2024       Fu, D., Chen, T.-q., Jia, R., and Sharan, V.  ...                                       None
14                 Giannou et al 2023  Giannou, A., Rajput, S., Sohn, J.-y., Lee, K.,...  ...                                       None
15           Gittens and Mahoney 2016                     Gittens, A. and Mahoney, M. W.  ...                                       None
16                   Halko et al 2011        Halko, N., Martinsson, P., and Tropp, J. A.  ...                                       None
17          Hestenes and Stiefel 1952                    Hestenes, M. R. and Stiefel, E.  ...                                       None
18                        Higham 1997                                      Higham, N. J.  ...                                       None
19                        Higham 2008                                      Higham, N. J.  ...                                       None
20                 Hoefler et al 2019  Hoefler, T., Huber, M., Luitjens, J., and Lums...  ...                                       None
21                   Ma and Chen 2020                                Ma, C. and Chen, Y.  ...                                       None
22                     Min et al 2021  Min, S., Lewis, M., Zettlemoyer, L., and Hajis...  ...                                       None
23                         Nanda 2023                                          Nanda, N.  ...                                       None
24                    Olah et al 2022  Olah, C., Elhage, N., Nanda, N., Schiefer, N.,...  ...  https://distill.pub/2022/circuits/   None
25                 Radford et al 2019  Radford, A., Wu, J., Child, R., Luan, D., Amod...  ...                                       None
26                        Schulz 1933                                         Schulz, G.  ...                                       None
27  Mechanics/Zeitschrift and H. 1992  Mechanics/Zeitschrift für Angewandte Mathemati...  ...                                       None
28             Tong and Pehlevan 2024                       Tong, W. L. and Pehlevan, C.  ...                                       None
29                 Vaswani et al 2017  Vaswani, A., Shazeer, N., Parmar, N., Uszkorei...  ...                                       None
30              Vladymyrov et al 2024  Vladymyrov, M., Von Oswald, J., Sandler, M., a...  ...                                       None
31                     Von et al 2023  Von Oswald, J., Niklasson, E., Randazzo, E., S...  ...                                       None
32                       Willems 1991                                     Willems, J. C.  ...                                       None
33           Williams and Seeger 2001                  Williams, C. K. I. and Seeger, M.  ...                                       None
34                      Woodruff 2014                                    Woodruff, D. P.  ...                                       None

[35 rows x 10 columns]
- Checking reference 1/35:
  -> INFO: Now checking 2 results for matching title: 'Transformers learn to implement preconditioned gradient descent for in-context learning'
       -> INFO: All authors matched!
- Checking reference 2/35:
  -> INFO: Now checking 10 results for matching title: 'What learning algorithm is in-context learning? investigations with linear models'
       -> INFO: All authors matched!
- Checking reference 3/35:
  -> INFO: Now checking 1 results for matching title: 'Transformers as statisticians: Provable incontext learning with in-context algorithm selection'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 5 results for matching title: 'Transformers as statisticians: Provable incontext learning with in-context algorithm selection'
  -> WARNING: None of the 5 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Transformers+as+statisticians:+Provable+incontext+learning+with+in-context+algorithm+selection manually and check the results.
        -> Author(s): Bai, Y., Chen, F., Wang, H., Xiong, C., and Mei, S.
        -> Title:     Transformers as statisticians: Provable incontext learning with in-context algorithm selection
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 4/35:
  -> INFO: Now checking 1 results for matching title: 'An iterative method for computing the generalized inverse of an arbitrary matrix'
       -> INFO: All authors matched!
- Checking reference 5/35:
  -> INFO: Now checking 10 results for matching title: 'Language models are few-shot learners'
       -> INFO: All authors matched!
- Checking reference 6/35:
  -> INFO: Now checking 10 results for matching title: 'Exact matrix completion via convex optimization'
       -> INFO: All authors matched!
       -> WARNING: Year (2008) does not match expected year (2009)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/35:
  -> INFO: Now checking 1 results for matching title: 'The power of convex relaxation: Near-optimal matrix completion'
       -> INFO: All authors matched!
       -> WARNING: Year (2009) does not match expected year (2010)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/35:
  -> INFO: Now checking 10 results for matching title: '–2080'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Transactions', '2053']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=–2080 manually and check the results.
        -> Author(s): Transactions on Information Theory, 56(5)
        -> Title:     –2080
        -> Year:      2053
     -> Manual search was skipped by the user.
- Checking reference 9/35:
  -> INFO: Now checking 10 results for matching title: 'Communication-efficient distributed statistical inference'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 83 results for matching title: 'Communication-efficient distributed statistical inference'
  -> WARNING: None of the 83 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Communication-efficient+distributed+statistical+inference manually and check the results.
        -> Author(s): Chen, Y., Fan, J., Ma, C., and Wang, K.
        -> Title:     Communication-efficient distributed statistical inference
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 10/35:
  -> INFO: Now checking 10 results for matching title: 'Low-rank approximation and regression in input sparsity time'
       -> INFO: All authors matched!
       -> WARNING: Year (2012) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/35:
  -> INFO: Now checking 1 results for matching title: 'Provable in-context optimal transport with transformers'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 13 results for matching title: 'Provable in-context optimal transport with transformers'
  -> WARNING: None of the 13 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Provable+in-context+optimal+transport+with+transformers manually and check the results.
        -> Author(s): Daneshmand, H.
        -> Title:     Provable in-context optimal transport with transformers
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 12/35:
  -> INFO: Now checking 2 results for matching title: 'An overview of low-rank matrix recovery from incomplete observations'
       -> INFO: All authors matched!
- Checking reference 13/35:
  -> INFO: Now checking 10 results for matching title: 'Communication-optimal parallel and sequential krylov subspace methods'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Demmel', 'Grigori', 'Hoemmen', 'Langou', '2013']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Communication-optimal+parallel+and+sequential+krylov+subspace+methods manually and check the results.
        -> Author(s): Demmel, J., Grigori, L., Hoemmen, M., and Langou, J.
        -> Title:     Communication-optimal parallel and sequential krylov subspace methods
        -> Year:      2013
     -> Manual search was skipped by the user.
- Checking reference 14/35:
  -> INFO: Now checking 1 results for matching title: 'Transformers learn to achieve second-order convergence rates for in-context linear regression'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 15/35:
  -> INFO: Now checking 10 results for matching title: 'Looped transformers as programmable computers'
       -> INFO: All authors matched!
- Checking reference 16/35:
  -> INFO: Now checking 3 results for matching title: 'Revisiting the nyström method for improved large-scale machine learning'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gittens', 'Mahoney', '2016']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Revisiting+the+nyström+method+for+improved+large-scale+machine+learning manually and check the results.
        -> Author(s): Gittens, A. and Mahoney, M. W.
        -> Title:     Revisiting the nyström method for improved large-scale machine learning
        -> Year:      2016
     -> Manual search was skipped by the user.
- Checking reference 17/35:
  -> INFO: Now checking 10 results for matching title: 'Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions'
       -> INFO: All authors matched!
       -> WARNING: Year (2009) does not match expected year (2011)!
       -> INFO: All authors matched!
       -> WARNING: Year (2009) does not match expected year (2011)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/35:
  -> INFO: Now checking 10 results for matching title: 'Methods of conjugate gradients for solving linear systems'
       -> INFO: All authors matched!
- Checking reference 19/35:
  -> INFO: Now checking 10 results for matching title: 'Stable iterations for the matrix sign function'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Higham', '1997']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Stable+iterations+for+the+matrix+sign+function manually and check the results.
        -> Author(s): Higham, N. J.
        -> Title:     Stable iterations for the matrix sign function
        -> Year:      1997
     -> Manual search was skipped by the user.
- Checking reference 20/35:
  -> INFO: Now checking 10 results for matching title: 'Functions of matrices: theory and computation'
       -> INFO: All authors matched!
- Checking reference 21/35:
  -> INFO: Now checking 10 results for matching title: 'Sparsity-aware communication schemes for distributed krylov solvers'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hoefler', 'Huber', 'Luitjens', 'Lumsdaine', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Sparsity-aware+communication+schemes+for+distributed+krylov+solvers manually and check the results.
        -> Author(s): Hoefler, T., Huber, M., Luitjens, J., and Lumsdaine, A.
        -> Title:     Sparsity-aware communication schemes for distributed krylov solvers
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 22/35:
  -> INFO: Now checking 10 results for matching title: 'Communication-efficient distributed statistical estimation with optimal convergence rate'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ma', 'Chen', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Communication-efficient+distributed+statistical+estimation+with+optimal+convergence+rate manually and check the results.
        -> Author(s): Ma, C. and Chen, Y.
        -> Title:     Communication-efficient distributed statistical estimation with optimal convergence rate
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 23/35:
  -> INFO: Now checking 10 results for matching title: 'Metaicl: Learning to learn in-context'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Min', 'Lewis', 'Zettlemoyer', 'Hajishirzi', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Metaicl:+Learning+to+learn+in-context manually and check the results.
        -> Author(s): Min, S., Lewis, M., Zettlemoyer, L., and Hajishirzi, H.
        -> Title:     Metaicl: Learning to learn in-context
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 24/35:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Progress in mechanistic interpretability: Reverse-engineering induction heads in GPT-2
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Nanda', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Progress+in+mechanistic+interpretability:+Reverse-engineering+induction+heads+in+GPT-2 manually and check the results.
        -> Author(s): Nanda, N.
        -> Title:     Progress in mechanistic interpretability: Reverse-engineering induction heads in GPT-2
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 25/35:
  -> Checking if provided link is pingable: https://distill.pub/2022/circuits/
  -> INFO: Now checking 10 results for matching title: 'Transformer circuits'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Olah', 'Elhage', 'Nanda', 'Schiefer', 'Jones', 'Henighan', 'DasSarma', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Transformer+circuits manually and check the results.
        -> Author(s): Olah, C., Elhage, N., Nanda, N., Schiefer, N., Jones, A., Henighan, T., and DasSarma, N.
        -> Title:     Transformer circuits
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 26/35:
  -> INFO: Now checking 10 results for matching title: 'Language models are unsupervised multitask learners'
       -> INFO: All authors matched!
- Checking reference 27/35:
  -> INFO: Now checking 4 results for matching title: 'Iterative berechung der reziproken matrix'
       -> INFO: All authors matched!
- Checking reference 28/35:
  -> INFO: Now checking 10 results for matching title: 'On the computational power of neural nets'
       -> INFO: All authors matched!
- Checking reference 29/35:
  -> INFO: Now checking 1 results for matching title: 'Mlps learn in-context on regression and classification tasks'
       -> INFO: All authors matched!
- Checking reference 30/35:
  -> INFO: Now checking 10 results for matching title: 'Attention is all you need'
       -> INFO: All authors matched!
- Checking reference 31/35:
  -> INFO: Now checking 1 results for matching title: 'Linear transformers are versatile in-context learners'
       -> INFO: All authors matched!
- Checking reference 32/35:
  -> INFO: Now checking 10 results for matching title: 'Transformers learn in-context by gradient descent'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/35:
  -> INFO: Now checking 2 results for matching title: 'Paradigms and puzzles in the theory of dynamical systems'
       -> INFO: All authors matched!
- Checking reference 34/35:
  -> INFO: Now checking 10 results for matching title: 'Using the nyström method to speed up kernel machines'
       -> INFO: All authors matched!
       -> WARNING: Year (2000) does not match expected year (2001)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 35/35:
  -> INFO: Now checking 5 results for matching title: 'Sketching as a tool for numerical linear algebra'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: find significantly smaller communication (and iteration) complexity when α−1 is much smaller that this joint
-> Invalid unicode use found on p. 5: η∥Aℓ∥−2
-> Invalid unicode use found on p. 5: ℓ≈γ∥Aℓ∥−2
-> Invalid unicode use found on p. 5: the scale of these weights is determined by ∥Aℓ∥−2, which is used in a fixed way by the method. Figure 5
-> Invalid unicode use found on p. 5: • Understanding the method. Note that the transformation A 7→(I −ρηAA⊤)A contracts large singular
-> Invalid unicode use found on p. 6: blocks, leading to Cℓ+1 = M −1P
-> Invalid unicode use found on p. 6: µ C′µ, Dℓ+1 = M −1P
-> Invalid unicode use found on p. 7: where α1, α2 are constants depending on ∥A∥−2. In other words, the update first computes the sketches
-> Invalid unicode use found on p. 7: • What the sketch buys. The contraction still needs ρℓ= ∥˜Aℓ∥−2
-> Invalid unicode use found on p. 7: log κ + log log(ε−1√
-> Invalid unicode use found on p. 7: such that ∀ℓ≥L, ∥DL −ˆD⋆∥F ≤ε, where W∗= BA(AA⊤)† is the Nyström parameter (§A.1).
-> Invalid unicode use found on p. 7: factor, and that once κℓ≤2, then κℓ−1 decyas supergeometrically. Error is controlled by developing a
-> Invalid unicode use found on p. 8: telescoping series with terms decaying with (κℓ−1). The log log(ε−1) dependence in L, i.e., the quadratic
-> Invalid unicode use found on p. 8: rate, is related to the quadratic decay in κℓ−1, which in turn arises since the EAGLE iterations for Aℓbear
-> Invalid unicode use found on p. 8: ∥Dℓ−Dℓ−1∥F <τ stopping rule suffices in practice.
-> Invalid unicode use found on p. 8: ∥v∥=1 M −1
-> Invalid unicode use found on p. 8: L = O(log(κmax + α−1 log(
-> Invalid unicode use found on p. 8: d′∥C∥F ∥W∗∥F /ε) such that ℓ≥L =⇒∥DL −D∥F ≤ε.
-> Invalid unicode use found on p. 8: controlled by the condition number of the average energy matrix ¯Eℓ= M −1 P
-> Invalid unicode use found on p. 8: , which tends to α−1.
-> Invalid unicode use found on p. 8: Second-order convergence re-emerges when α = 1. Let us note that α−1 is always smaller than κ( ¯E0) and,
-> Invalid unicode use found on p. 8: κ( ¯E0), which is always > α−1, and may be much larger. As a result, EAGLE has a strong advantage in
-> Invalid unicode use found on p. 9: (α ≈1), and its iteration count grows exactly linearly with α−1 as
-> Invalid unicode use found on p. 19: 2(3I −¯Aℓ¯A⊤
-> Invalid unicode use found on p. 20: rank-2 bias term whose first n −1 rows are identical by design.
-> Invalid unicode use found on p. 21: Aℓ+1 = A −ηρℓAℓA⊤
-> Invalid unicode use found on p. 21: Bℓ+1 = B −ηρℓBℓA⊤
-> Invalid unicode use found on p. 21: Wℓ+1 = Wℓ−γρℓ(WℓAℓ−Bℓ)A⊤
-> Invalid unicode use found on p. 21: linear system minX ∥XA −B∥2
-> Invalid unicode use found on p. 21: ∥XA −B∥2
-> Invalid unicode use found on p. 21: k −˜Bi
-> Invalid unicode use found on p. 21: Xk+1 = Xℓ−ηk
-> Invalid unicode use found on p. 22: i=1 ∥XA −B∥2
-> Invalid unicode use found on p. 22: Rk = B −XkG,
-> Invalid unicode use found on p. 22: Rk+1 = Rk −αkPkG,
-> Invalid unicode use found on p. 22: the condition number of the global matrix A is lower bounded by α−1, even if the data on each individual
-> Invalid unicode use found on p. 22: we evaluate the criterion minµ ∥I −Aµ,⊤
-> Invalid unicode use found on p. 22: SVD construction. Sample Aij, Bij orthogonal and set Z = AΣB⊤/√r with Σ diagonal with entries loguniform in [1e −2, 1]. This is the reference distribution in the simulation part.
-> Invalid unicode use found on p. 25: Correlated Gaussian factors. Draw each column of A and B from N(0, Σ) with Σij = ρ|i−j| (ρ = 0.8). Strong
-> Invalid unicode use found on p. 25: simplicity, let us set ηℓ= η∥Aℓ∥−2
-> Invalid unicode use found on p. 25: 2 , and γℓ= γ∥Aℓ∥−2
-> Invalid unicode use found on p. 25: Aℓ+1 = Aℓ(I −ηℓA⊤
-> Invalid unicode use found on p. 25: Bℓ+1 = Bℓ(I −ηℓA⊤
-> Invalid unicode use found on p. 25: Cℓ+1 = (I −γℓAℓA⊤
-> Invalid unicode use found on p. 26: Eℓ+1 = Eℓ(I −ηℓEℓ)2
-> Invalid unicode use found on p. 26: Vℓ+1 = Vℓ(I −ηℓEℓ)2
-> Invalid unicode use found on p. 26: Cℓ+1 = (I −γℓEℓ)Cℓ
-> Invalid unicode use found on p. 26: ℓ+1 = Bℓ(I −ηℓA⊤
-> Invalid unicode use found on p. 26: ℓAℓ)(I −ηℓA⊤
-> Invalid unicode use found on p. 26: = Bℓ(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: ℓ−ηℓA⊤
-> Invalid unicode use found on p. 26: = Bℓ(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: ℓ(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: ℓ(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: ℓ)(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: = Vℓ(I −ηℓEℓ)2,
-> Invalid unicode use found on p. 26: ℓ+1 = Aℓ(I −ηℓA⊤
-> Invalid unicode use found on p. 26: ℓAℓ)(I −ηℓA⊤
-> Invalid unicode use found on p. 26: ℓ(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: = Eℓ(I −ηℓEℓ)2,
-> Invalid unicode use found on p. 26: l<ℓ(I −ηlEl)2 and N ⊤
-> Invalid unicode use found on p. 26: l<ℓ(I −γlEl), where we use the convention that
-> Invalid unicode use found on p. 26: Ul = U1U2 · · · Uℓ−1,
-> Invalid unicode use found on p. 27: Dℓ= W∗(I −Nℓ)C0.
-> Invalid unicode use found on p. 27: l (I −γlEl) ⇐⇒Nl+1 = Nl −γlElNl ⇐⇒γlElNl = Nl −Nl+1.
-> Invalid unicode use found on p. 27: (Nl −Nl+1)
-> Invalid unicode use found on p. 27: C0 = W∗(I −Nℓ)C0.
-> Invalid unicode use found on p. 27: Recall that ˆD∗= W∗C0, meaning that the error Dℓ−ˆD∗is W∗NℓC0. Thus, this lemma captures a basic
-> Invalid unicode use found on p. 27: dynamics (see below), meaning that I −Nℓmay even asymptotically have a large eigenvalue corresponding to
-> Invalid unicode use found on p. 27: matrix ˜Nℓ:= (I −P0)Nℓ, where P0 projects onto the kernel of E0. Instead of this notational complication,
-> Invalid unicode use found on p. 28: −1
-> Invalid unicode use found on p. 28: λℓ+1 = (1 −ηℓλℓ)2λℓ
-> Invalid unicode use found on p. 28: λℓ+1 = (1 −ηℓλℓ)2λℓ.
-> Invalid unicode use found on p. 28: µℓ+1u1 = Eℓ+1u1 = Eℓ(I −ηℓEℓ)2u1 = (1 −ηℓµℓ)2µℓ,
-> Invalid unicode use found on p. 28: µℓ+1 −νℓ+1 = (1 −ηℓµℓ)2µℓ−(1 −ηℓνℓ)2νℓ
-> Invalid unicode use found on p. 28: = (µℓ−νℓ) −2η(µ2
-> Invalid unicode use found on p. 28: ℓ−ν2
-> Invalid unicode use found on p. 28: ℓ−ν3
-> Invalid unicode use found on p. 28: = (µℓ−νℓ)
-> Invalid unicode use found on p. 28: 1 −2ηℓ(µℓ+ νℓ) + η2
-> Invalid unicode use found on p. 28: Now, if the term multiplying (µℓ−νℓ) is nonnegative, then the claim follows. To see when this occurs, let us
-> Invalid unicode use found on p. 28: −1
-> Invalid unicode use found on p. 28: −1 within the brackets. We are left with an expression of the form
-> Invalid unicode use found on p. 28: (1 −2η(x + y) + η2(x2 + y2 + xy)),
-> Invalid unicode use found on p. 28: 1 −4η + 3η2.
-> Invalid unicode use found on p. 28: Lemma 7. Define κℓ= λℓ/λℓ, and θℓ= κℓ−1. If ηℓ≤λ
-> Invalid unicode use found on p. 28: −1/3, then θℓ+1 ≤θℓexp(−5ηℓλℓ/3). Further, if
-> Invalid unicode use found on p. 29: 1 −ηλ
-> Invalid unicode use found on p. 29: 1 −ηλ
-> Invalid unicode use found on p. 29: 1 −ηλ
-> Invalid unicode use found on p. 29: 1 −ηλ = 1 + η λ −λ
-> Invalid unicode use found on p. 29: 1 −ηλ = 1 −η λ(1 −1/(θ + 1))
-> Invalid unicode use found on p. 29: 1 −ηλ/(θ + 1) = 1 −
-> Invalid unicode use found on p. 29: θ + 1 −ηλ.
-> Invalid unicode use found on p. 29: 1 −2
-> Invalid unicode use found on p. 29: (θ + 1 −ηλ) +
-> Invalid unicode use found on p. 29: (θ + 1 −ηλ)2
-> Invalid unicode use found on p. 29: = θ + 1 −θ
-> Invalid unicode use found on p. 29: 1 −ηλ
-> Invalid unicode use found on p. 29: 2 −
-> Invalid unicode use found on p. 29: (θ + 1 −ηλ)
-> Invalid unicode use found on p. 29: 2 −
-> Invalid unicode use found on p. 29: θ + 1 −ηλ ≥2 −
-> Invalid unicode use found on p. 29: 3θ + 3 −1 = 5θ + 4
-> Invalid unicode use found on p. 29: θℓ+1 ≤θℓ−θℓ· 5/3ηℓλℓ
-> Invalid unicode use found on p. 29: 1 −ηℓλℓ
-> Invalid unicode use found on p. 29: −5ηℓλℓ/3
-> Invalid unicode use found on p. 29: 1 −ηℓλℓ
-> Invalid unicode use found on p. 29: ≤θℓexp(−ηℓλℓ).
-> Invalid unicode use found on p. 29: 1 −ηλ
-> Invalid unicode use found on p. 29: 1 −ηλ =
-> Invalid unicode use found on p. 29: 1 −L
-> Invalid unicode use found on p. 29: (θ + 1 −L)/(θ + 1),
-> Invalid unicode use found on p. 29: (θ+ + 1) = (θ + 1)3(1 −L)2
-> Invalid unicode use found on p. 29: (θ + 1 −L)2
-> Invalid unicode use found on p. 29: ⇐⇒θ+ = θ(1 −4L + 3L2) + θ2(2 −6L + 3L2) + θ3(1 −L)2
-> Invalid unicode use found on p. 29: (θ + 1 −L)2
-> Invalid unicode use found on p. 29: The statement of this Lemma has shown two decay modes of θℓ= (κℓ−1). Firstly, as long as ηℓ≤λ
-> Invalid unicode use found on p. 29: −1
-> Invalid unicode use found on p. 29: −1
-> Invalid unicode use found on p. 29: Lemma 8. Let κℓ:= λℓ/λℓ. If for all ℓ, ηℓλ = 1/3, then κℓ−1 ≤ε for all
-> Invalid unicode use found on p. 30: Proof. First using the geometric decay in Lemma 7, we know that θℓ≤(κ0 −1) exp(−5(ℓ−1)/3). Set
-> Invalid unicode use found on p. 30: ℓ0 = 2 + 3/5 log(κ0 −1). Then for ℓ≥ℓ0, we have θℓ0 ≤1/e. Further, for iterations beyond this ℓ0, the
-> Invalid unicode use found on p. 30: Tℓ≤2ℓ−ℓ0Tℓ0 ≤−2ℓ−ℓ0 =⇒θℓ≤4/3 exp(−2ℓ−ℓ0).
-> Invalid unicode use found on p. 30: We note that if E0 is not full rank, the statement holds for ˜Nℓ= (I −P0)Nℓ, where P0 projects onto the
-> Invalid unicode use found on p. 30: Lemma 9. For all ℓ, ∥Nℓ∥2 ≤exp(−P
-> Invalid unicode use found on p. 30: −1/3 and γℓ= λ
-> Invalid unicode use found on p. 30: −1, then ∥Nℓ∥2 ≤ε
-> Invalid unicode use found on p. 30: Proof. Since Nl+1 = (I −γlEl)Nl, we immediately have
-> Invalid unicode use found on p. 30: ∥I −γlEl∥2.
-> Invalid unicode use found on p. 30: But note that ∥I −γlEl∥2 = (1 −γlλl). Thus, we immediately have ∥Nℓ∥≤Q(1 −γlλl) ≤exp(P
-> Invalid unicode use found on p. 30: −1/3 for all ℓ, then λℓ≥λℓ/(1 + ε) for all ℓ≥L. But then, if
-> Invalid unicode use found on p. 30: −1, we have
-> Invalid unicode use found on p. 30: 1 −ηℓλ ≤1 −λ/λ ≤ε/(1 + ε) ≤ε,
-> Invalid unicode use found on p. 30: Proof of Theorem 1. By Lemma 4, we have Dℓ−ˆD∗= W∗NℓC0, and consequently,
-> Invalid unicode use found on p. 30: ∥Dℓ−ˆD∗∥F ≤∥W∗Nℓ∥F ∥C0∥F ≤
-> Invalid unicode use found on p. 30: −1
-> Invalid unicode use found on p. 30: ∥Aℓ∥−2
-> Invalid unicode use found on p. 30: λℓ+1 = λℓ(1 −1/3)2 = 4λℓ/9.
-> Invalid unicode use found on p. 31: ℓ(I −ηµ
-> Invalid unicode use found on p. 31: ℓ(I −ηµ
-> Invalid unicode use found on p. 31: Cℓ+1 = Cℓ−1
-> Invalid unicode use found on p. 31: ℓ∥−2
-> Invalid unicode use found on p. 31: ℓ∥−2
-> Invalid unicode use found on p. 32: ℓ(I −ηµ
-> Invalid unicode use found on p. 32: ℓ(I −ηµ
-> Invalid unicode use found on p. 32: Cℓ+1 = (I −γℓEℓ)Cℓ
-> Invalid unicode use found on p. 32: I −γℓ· 1
-> Invalid unicode use found on p. 32: Cℓ= (I −γℓEℓ)Cℓ
-> Invalid unicode use found on p. 32: (I −ηµ
-> Invalid unicode use found on p. 32: (I −γℓEℓ),
-> Invalid unicode use found on p. 32: Dℓ= W∗(I −Nℓ)C0.
-> Invalid unicode use found on p. 33: Nl+1 = (I −γlEl)Nl ⇐⇒γlElNl = Nl −Nl+1,
-> Invalid unicode use found on p. 33: and so the term in the brackets telescopes to N0 −Nℓ= I −Nℓ.
-> Invalid unicode use found on p. 33: ℓ)−1/3, and define κµ
-> Invalid unicode use found on p. 33: ℓ)−1/3. Define
-> Invalid unicode use found on p. 33: ℓ)−1/3. Thus, each of these λ
-> Invalid unicode use found on p. 34: At a high level, α−1 is the limiting condition number of the Eℓs, where deviation from perfect conditioning
-> Invalid unicode use found on p. 34: Proof of Theorem 2. Recall that D −ˆDℓ= W∗NℓC0. We again assume that λ
-> Invalid unicode use found on p. 34: ℓ)−1/3. We set γℓ= (λ
-> Invalid unicode use found on p. 34: ℓ)−1 ≤λ(Eℓ)−1. Then, as before, we have (restricted to the appropriate
-> Invalid unicode use found on p. 34: ∥I −ηℓEℓ∥2 ≤(1 −1/κℓ) ≤exp(−1/κℓ).
-> Invalid unicode use found on p. 34: ∥Nℓ∥≤exp(−
-> Invalid unicode use found on p. 34: 1/κℓ) ≤exp(−α(ℓ−L(1))/2),
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Couldn't parse in-text references '(['full visibility', ' rank-limited updates', ' and distributed computation'])' in bracket on p. 1!
-> Skipping possible_ref_id '0 Σ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'ZW h K ℓ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'Cℓ Dℓ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'n d' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'd′ n′' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '18 18' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '2 2' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Warning: Bracket content 'd′ =n′ =1' on p. 8 could not be matched to a reference.
   -> Sentence:  Von Oswald et al (2023) dubbed the same update “GD++” in the scalar case (d′ =n′ =1) and interpreted it as pre-conditioned gradient descent
-> Skipping possible_ref_id 'α1 ℓIn α2 ℓIn′' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'α1 ℓ α2 ℓ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '0n α2 ℓIn′' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'Cℓ Dℓ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'Aℓ Bℓ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'randomness clustered eigenvalues' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'min n2d d2n' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text references '(['CG', ' Hestenes and Stiefel', ' 1952'])' in bracket on p. 9!
-> Skipping possible_ref_id 'n2d d2n' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'min(nd3 dn2)' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text references '(['d = n = 1000', ' κmax = 103', ' α ≈1'])' in bracket on p. 10!
-> Skipping possible_ref_id 'EAGLE until A stabilizes then GD' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 468 sentences on 12 pages -> Avg. of 43.54545454545455 sentences per page
-> Warning: Reference 'Transactions 2053' never used in the document's text.
-> Warning: Reference 'Hestenes and Stiefel 1952' never used in the document's text.
-> Warning: Reference 'Mechanics/Zeitschrift and H. 1992' never used in the document's text.
-> Warning: Reference 'Von et al 2023' never used in the document's text.
-> Warning: Reference 'Willems 1991' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = Ahn et al 2023); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = Akyürek et al 2022); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = Bai et al 2023); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = Ben-Israel 1965); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = Brown et al 2020); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 7 (Ref. ID = Transactions 2053); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = Chen et al 2020); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = Clarkson and Woodruff 2017); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = Daneshmand 2024); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = Davenport and Romberg 2016); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = Demmel et al 2013); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 14 (Ref. ID = Giannou et al 2023); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = Gittens and Mahoney 2016); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 17 (Ref. ID = Hestenes and Stiefel 1952); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = Higham 1997); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = Higham 2008); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = Hoefler et al 2019); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = Ma and Chen 2020); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = Min et al 2021); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = Nanda 2023); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = Olah et al 2022); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = Radford et al 2019); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = Schulz 1933); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = Mechanics/Zeitschrift and H. 1992); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = Tong and Pehlevan 2024); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = Vaswani et al 2017); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = Vladymyrov et al 2024); Skipping LLM check...
-> WARNING: Reference with index 31 (Ref. ID = Von et al 2023) has no associated sentence!
-> Missing an abstract for reference with index 32 (Ref. ID = Willems 1991); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = Williams and Seeger 2001); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = Woodruff 2014); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 19 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 9 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 261 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 230 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 85 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 453 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 5
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
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
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 9
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\41 Linear Transformers Implicitly\PAU_results.md
```

---

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\41 Linear Transformers Implicitly\Linear Transformers Implicitly Discover Unified Numerical Algorithms.pdf"
---
---
INFO:
 - 'springer' = Has two headerlines to skip (1st = Shortitle/Author; 2nd = page number)
 - 'acm'      = Has no headerlines to skip
Enter a supported formatting template (['springer', 'acm']): acm       
---
INFO:
 - 'LFTOY' = Lastname, Firstname, Title, Outlet, Year
            -> This is, for example, used by Springer Nature
 - 'LFYTO' = Lastname, Firstname, Year, Title, Outlet
            -> This is, for example, used by the AAAI/ACM Conference
 - 'FLYTO' = Firstname, Lastname, Year, Title, Outlet
            -> This is, for example, used by ACM
 - 'FLTOY' = Firstname, Lastname, Title, Outlet, Year
            -> This is, for example, used by most papers of the NeurIPS Conference
Enter a supported bibliography layout (['LFTOY', 'LFYTO', 'FLYTO', 'FLTOY']): LFYTO  
# PLEASE NOTE:
 -> The chosen bib layout uses ';' to separate multiple authors.
 => If that is correct, please press enter or type 'y', otherwise enter another author-separator to use: ,
... ',' as author separator accepted!
---
INFO:
 - 'natbib'           = No numbering; reference in 'References' section starts with the authors' names
 - 'numbered_squares' = Reference in 'References' section starts with, e.g., '[1]'
 - 'number_with_dot'  = Reference in 'References' section starts with, e.g., '1.'
Enter a supported bibliography numbering (['natbib', 'numbered_squares', 'number_with_dot']): natbib    
---
INFO:
 - 'numeric'     = A number placed inside square brackets (e.g., [28])
                -> Multiple references are separated by a comma (e.g., [28,29])
 - 'authoryear'  = Authors' names and the year places insince brackets with or withou a comma in between (e.g., (Dignum et al., 2025))
                -> Multiple references are separated by a semicolon or comma (e.g., (Dignum et al. 2025; Caliskan et al. 2017))
Enter a supported referencing template (['numeric', 'authoryear']): authoryear
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Related Work' on page 2
- Found following heading '3 - Method' on page 3
- Found following heading '4 - Emergent Algorithm' on page 5
- Found following heading '5 - Evaluation of EAGLE' on page 8
- Found following heading '6 - Conclusions' on page 10
=> Found references/literature section on page 12
- Found first appendix 'A - Methodological Details' on page 15
- Found following appendix 'B - D' on page 15
- Found following appendix 'C - B' on page 15
- Found following appendix 'D - Further Details on Evaluation of EAGLE' on page 22
- Found following appendix 'E - Theoretical Analyses' on page 26
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 12 -- 15
All found references: 40
-> Warning: Could not parse year (and authors) in reference 'Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D., Wu, J., Winter, C., Hesse, C., Chen, M., Sigler, E., Litwin, M., Gray, S., Chess, B., Clark,'!
-> Warning: Malformed author string: ['J.', 'Berner', 'C.', 'McCandlish', 'S.', 'Radford', 'A.', 'Sutskever', 'I.', 'Amodei', 'D']
-> Warning: Could not parse year (and authors) in reference 'Mechanics/Zeitschrift für Angewandte Mathematik und Mechanik, 13(1):57–59. 7'!
-> Warning: Could not parse year (and authors) in reference 'Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., and Polosukhin, I.'!
-> WARNING: The normalized authors' list contains no entries!
-> Warning: Could not parse year (and authors) in reference 'Von Oswald, J., Niklasson, E., Randazzo, E., Sacramento, J., Mordvintsev, A., Zhmoginov, A., and'!
-> Warning: Could not parse year (and authors) in reference 'Machine Learning, pages 35151–35174. PMLR. 2, 4, 7, 20'!
 -> Found dublicated ref_ids:
                                       full_reference      ref_id     authors normalized_authors contains_et_al       title        year abstract      outlet link valid
28  Mechanics/Zeitschrift für Angewandte Mathemati...  NOT PARSED  NOT PARSED                NaN            NaN  NOT PARSED  NOT PARSED     None  NOT PARSED       None
31  Vaswani, A., Shazeer, N., Parmar, N., Uszkorei...  NOT PARSED  NOT PARSED                NaN            NaN  NOT PARSED  NOT PARSED     None  NOT PARSED       None
34  Von Oswald, J., Niklasson, E., Randazzo, E., S...  NOT PARSED  NOT PARSED                NaN            NaN  NOT PARSED  NOT PARSED     None  NOT PARSED       None
36  Machine Learning, pages 35151–35174. PMLR. 2, ...  NOT PARSED  NOT PARSED                NaN            NaN  NOT PARSED  NOT PARSED     None  NOT PARSED       None
-----------
 -> Parsed references DataFrame:
                        ref_id                                            authors  ...                                link valid
0               Ahn et al 2023    Ahn, K., Cheng, X., Daneshmand, H., and Sra, S.  ...                                      None
1           Akyürek et al 2022  Akyürek, E., Schuurmans, D., Andreas, J., Ma, ...  ...                                      None
2               Bai et al 2023  Bai, Y., Chen, F., Wang, H., Xiong, C., and Me...  ...                                      None
3              Ben-Israel 1965                                     Ben-Israel, A.  ...                                      None
4                  NOT PARSEDd                                         NOT PARSED  ...                                      None
5                J. et al 2020  J., Berner, C., McCandlish, S., Radford, A., S...  ...                                      None
6        Candès and Recht 2009                        Candès, E. J. and Recht, B.  ...                                      None
7          Candès and Tao 2010                          Candès, E. J. and Tao, T.  ...                                      None
8            Transactions 2053          Transactions on Information Theory, 56(5)  ...                                      None
9              Chen et al 2020            Chen, Y., Fan, J., Ma, C., and Wang, K.  ...                                      None
10  Clarkson and Woodruff 2017                Clarkson, K. L. and Woodruff, D. P.  ...                                      None
11             Daneshmand 2024                                     Daneshmand, H.  ...                                      None
12  Davenport and Romberg 2016                   Davenport, M. A. and Romberg, J.  ...                                      None
13           Demmel et al 2013  Demmel, J., Grigori, L., Hoemmen, M., and Lang...  ...                                      None
14               Fu et al 2024       Fu, D., Chen, T.-q., Jia, R., and Sharan, V.  ...                                      None
15          Giannou et al 2023  Giannou, A., Rajput, S., Sohn, J.-y., Lee, K.,...  ...                                      None
16    Gittens and Mahoney 2016                     Gittens, A. and Mahoney, M. W.  ...                                      None
17            Halko et al 2011        Halko, N., Martinsson, P., and Tropp, J. A.  ...                                      None
18   Hestenes and Stiefel 1952                    Hestenes, M. R. and Stiefel, E.  ...                                      None
19                 Higham 1997                                      Higham, N. J.  ...                                      None
20                 Higham 2008                                      Higham, N. J.  ...                                      None
21          Hoefler et al 2019  Hoefler, T., Huber, M., Luitjens, J., and Lums...  ...                                      None
22            Ma and Chen 2020                                Ma, C. and Chen, Y.  ...                                      None
23              Min et al 2021  Min, S., Lewis, M., Zettlemoyer, L., and Hajis...  ...                                      None
24                  Nanda 2023                                          Nanda, N.  ...                                      None
25             Olah et al 2022  Olah, C., Elhage, N., Nanda, N., Schiefer, N.,...  ...  https://distill.pub/2022/circuits/  None
26          Radford et al 2019  Radford, A., Wu, J., Child, R., Luan, D., Amod...  ...                                      None
27                 Schulz 1933                                         Schulz, G.  ...                                      None
28                 NOT PARSEDe                                         NOT PARSED  ...                                      None
29  Siegelmann and Sontag 1992                Siegelmann, H. T. and Sontag, E. D.  ...                                      None
30      Tong and Pehlevan 2024                       Tong, W. L. and Pehlevan, C.  ...                                      None
31                 NOT PARSEDf                                         NOT PARSED  ...                                      None
32                                                                                 ...                                      None
33       Vladymyrov et al 2024  Vladymyrov, M., Von Oswald, J., Sandler, M., a...  ...                                      None
34                 NOT PARSEDg                                         NOT PARSED  ...                                      None
35             Vladymyrov 2023                                     Vladymyrov, M.  ...                                      None
36                 NOT PARSEDh                                         NOT PARSED  ...                                      None
37                Willems 1991                                     Willems, J. C.  ...                                      None
38    Williams and Seeger 2001                  Williams, C. K. I. and Seeger, M.  ...                                      None
39               Woodruff 2014                                    Woodruff, D. P.  ...                                      None

[40 rows x 10 columns]
- Checking reference 1/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Ahn, K., Cheng, X., Daneshmand, H., and Sra, S.
           -> Year: 2023
- Checking reference 2/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Akyürek, E., Schuurmans, D., Andreas, J., Ma, T., and Zhou, D.
           -> Year: 2022
- Checking reference 3/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Bai, Y., Chen, F., Wang, H., Xiong, C., and Mei, S.
           -> Year: 2023
- Checking reference 4/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Ben-Israel, A.
           -> Year: 1965
- Checking reference 5/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled 'NOT PARSED'
           -> Author(s): NOT PARSED
           -> Year: NOT PARSED
- Checking reference 6/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): J., Berner, C., McCandlish, S., Radford, A., Sutskever, I., and Amodei, D.
           -> Year: 2020
- Checking reference 7/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Candès, E. J. and Recht, B.
           -> Year: 2009
- Checking reference 8/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Candès, E. J. and Tao, T.
           -> Year: 2010
- Checking reference 9/40:
  -> INFO: Now checking 10 results for matching title: '–2080'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Transactions', '2053']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=–2080 manually and check the results.
        -> Author(s): Transactions on Information Theory, 56(5)
        -> Title:     –2080
        -> Year:      2053
     -> Manual search was skipped by the user.
- Checking reference 10/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Chen, Y., Fan, J., Ma, C., and Wang, K.
           -> Year: 2020
- Checking reference 11/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Clarkson, K. L. and Woodruff, D. P.
           -> Year: 2017
- Checking reference 12/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Daneshmand, H.
           -> Year: 2024
- Checking reference 13/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Davenport, M. A. and Romberg, J.
           -> Year: 2016
- Checking reference 14/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Demmel, J., Grigori, L., Hoemmen, M., and Langou, J.
           -> Year: 2013
- Checking reference 15/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Fu, D., Chen, T.-q., Jia, R., and Sharan, V.
           -> Year: 2024
- Checking reference 16/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Giannou, A., Rajput, S., Sohn, J.-y., Lee, K., Lee, J. D., and Papailiopoulos, D.
           -> Year: 2023
- Checking reference 17/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Gittens, A. and Mahoney, M. W.
           -> Year: 2016
- Checking reference 18/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Halko, N., Martinsson, P., and Tropp, J. A.
           -> Year: 2011
- Checking reference 19/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Hestenes, M. R. and Stiefel, E.
           -> Year: 1952
- Checking reference 20/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Higham, N. J.
           -> Year: 1997
- Checking reference 21/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Higham, N. J.
           -> Year: 2008
- Checking reference 22/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Hoefler, T., Huber, M., Luitjens, J., and Lumsdaine, A.
           -> Year: 2019
- Checking reference 23/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Ma, C. and Chen, Y.
           -> Year: 2020
- Checking reference 24/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Min, S., Lewis, M., Zettlemoyer, L., and Hajishirzi, H.
           -> Year: 2021
- Checking reference 25/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Nanda, N.
           -> Year: 2023
- Checking reference 26/40:
  -> Checking if provided link is pingable: https://distill.pub/2022/circuits/
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Olah, C., Elhage, N., Nanda, N., Schiefer, N., Jones, A., Henighan, T., and DasSarma, N.
           -> Year: 2022
- Checking reference 27/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., et al.
           -> Year: 2019
- Checking reference 28/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Schulz, G.
           -> Year: 1933
- Checking reference 29/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled 'NOT PARSED'
           -> Author(s): NOT PARSED
           -> Year: NOT PARSED
- Checking reference 30/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Siegelmann, H. T. and Sontag, E. D.
           -> Year: 1992
- Checking reference 31/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Tong, W. L. and Pehlevan, C.
           -> Year: 2024
- Checking reference 32/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled 'NOT PARSED'
           -> Author(s): NOT PARSED
           -> Year: NOT PARSED
- Checking reference 33/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): 
           -> Year: 2017
- Checking reference 34/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Vladymyrov, M., Von Oswald, J., Sandler, M., and Ge, R.
           -> Year: 2024
- Checking reference 35/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled 'NOT PARSED'
           -> Author(s): NOT PARSED
           -> Year: NOT PARSED
- Checking reference 36/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Vladymyrov, M.
           -> Year: 2023
- Checking reference 37/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled 'NOT PARSED'
           -> Author(s): NOT PARSED
           -> Year: NOT PARSED
- Checking reference 38/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Willems, J. C.
           -> Year: 1991
- Checking reference 39/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Williams, C. K. I. and Seeger, M.
           -> Year: 2001
- Checking reference 40/40:
  -> WARNING: Skipping search (due to not enough info) for reference titled ')'
           -> Author(s): Woodruff, D. P.
           -> Year: 2014
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: find significantly smaller communication (and iteration) complexity when α−1 is much smaller that this joint
-> Invalid unicode use found on p. 5: η∥Aℓ∥−2
-> Invalid unicode use found on p. 5: ℓ≈γ∥Aℓ∥−2
-> Invalid unicode use found on p. 5: the scale of these weights is determined by ∥Aℓ∥−2, which is used in a fixed way by the method. Figure 5
-> Invalid unicode use found on p. 5: • Understanding the method. Note that the transformation A 7→(I −ρηAA⊤)A contracts large singular
-> Invalid unicode use found on p. 6: blocks, leading to Cℓ+1 = M −1P
-> Invalid unicode use found on p. 6: µ C′µ, Dℓ+1 = M −1P
-> Invalid unicode use found on p. 7: where α1, α2 are constants depending on ∥A∥−2. In other words, the update first computes the sketches
-> Invalid unicode use found on p. 7: • What the sketch buys. The contraction still needs ρℓ= ∥˜Aℓ∥−2
-> Invalid unicode use found on p. 7: log κ + log log(ε−1√
-> Invalid unicode use found on p. 7: such that ∀ℓ≥L, ∥DL −ˆD⋆∥F ≤ε, where W∗= BA(AA⊤)† is the Nyström parameter (§A.1).
-> Invalid unicode use found on p. 7: factor, and that once κℓ≤2, then κℓ−1 decyas supergeometrically. Error is controlled by developing a
-> Invalid unicode use found on p. 8: telescoping series with terms decaying with (κℓ−1). The log log(ε−1) dependence in L, i.e., the quadratic
-> Invalid unicode use found on p. 8: rate, is related to the quadratic decay in κℓ−1, which in turn arises since the EAGLE iterations for Aℓbear
-> Invalid unicode use found on p. 8: ∥Dℓ−Dℓ−1∥F <τ stopping rule suffices in practice.
-> Invalid unicode use found on p. 8: ∥v∥=1 M −1
-> Invalid unicode use found on p. 8: L = O(log(κmax + α−1 log(
-> Invalid unicode use found on p. 8: d′∥C∥F ∥W∗∥F /ε) such that ℓ≥L =⇒∥DL −D∥F ≤ε.
-> Invalid unicode use found on p. 8: controlled by the condition number of the average energy matrix ¯Eℓ= M −1 P
-> Invalid unicode use found on p. 8: , which tends to α−1.
-> Invalid unicode use found on p. 8: Second-order convergence re-emerges when α = 1. Let us note that α−1 is always smaller than κ( ¯E0) and,
-> Invalid unicode use found on p. 8: κ( ¯E0), which is always > α−1, and may be much larger. As a result, EAGLE has a strong advantage in
-> Invalid unicode use found on p. 9: (α ≈1), and its iteration count grows exactly linearly with α−1 as
-> Invalid unicode use found on p. 19: 2(3I −¯Aℓ¯A⊤
-> Invalid unicode use found on p. 20: rank-2 bias term whose first n −1 rows are identical by design.
-> Invalid unicode use found on p. 21: Aℓ+1 = A −ηρℓAℓA⊤
-> Invalid unicode use found on p. 21: Bℓ+1 = B −ηρℓBℓA⊤
-> Invalid unicode use found on p. 21: Wℓ+1 = Wℓ−γρℓ(WℓAℓ−Bℓ)A⊤
-> Invalid unicode use found on p. 21: linear system minX ∥XA −B∥2
-> Invalid unicode use found on p. 21: ∥XA −B∥2
-> Invalid unicode use found on p. 21: k −˜Bi
-> Invalid unicode use found on p. 21: Xk+1 = Xℓ−ηk
-> Invalid unicode use found on p. 22: i=1 ∥XA −B∥2
-> Invalid unicode use found on p. 22: Rk = B −XkG,
-> Invalid unicode use found on p. 22: Rk+1 = Rk −αkPkG,
-> Invalid unicode use found on p. 22: the condition number of the global matrix A is lower bounded by α−1, even if the data on each individual
-> Invalid unicode use found on p. 22: we evaluate the criterion minµ ∥I −Aµ,⊤
-> Invalid unicode use found on p. 22: SVD construction. Sample Aij, Bij orthogonal and set Z = AΣB⊤/√r with Σ diagonal with entries loguniform in [1e −2, 1]. This is the reference distribution in the simulation part.
-> Invalid unicode use found on p. 25: Correlated Gaussian factors. Draw each column of A and B from N(0, Σ) with Σij = ρ|i−j| (ρ = 0.8). Strong
-> Invalid unicode use found on p. 25: simplicity, let us set ηℓ= η∥Aℓ∥−2
-> Invalid unicode use found on p. 25: 2 , and γℓ= γ∥Aℓ∥−2
-> Invalid unicode use found on p. 25: Aℓ+1 = Aℓ(I −ηℓA⊤
-> Invalid unicode use found on p. 25: Bℓ+1 = Bℓ(I −ηℓA⊤
-> Invalid unicode use found on p. 25: Cℓ+1 = (I −γℓAℓA⊤
-> Invalid unicode use found on p. 26: Eℓ+1 = Eℓ(I −ηℓEℓ)2
-> Invalid unicode use found on p. 26: Vℓ+1 = Vℓ(I −ηℓEℓ)2
-> Invalid unicode use found on p. 26: Cℓ+1 = (I −γℓEℓ)Cℓ
-> Invalid unicode use found on p. 26: ℓ+1 = Bℓ(I −ηℓA⊤
-> Invalid unicode use found on p. 26: ℓAℓ)(I −ηℓA⊤
-> Invalid unicode use found on p. 26: = Bℓ(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: ℓ−ηℓA⊤
-> Invalid unicode use found on p. 26: = Bℓ(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: ℓ(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: ℓ(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: ℓ)(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: = Vℓ(I −ηℓEℓ)2,
-> Invalid unicode use found on p. 26: ℓ+1 = Aℓ(I −ηℓA⊤
-> Invalid unicode use found on p. 26: ℓAℓ)(I −ηℓA⊤
-> Invalid unicode use found on p. 26: ℓ(I −ηℓAℓA⊤
-> Invalid unicode use found on p. 26: = Eℓ(I −ηℓEℓ)2,
-> Invalid unicode use found on p. 26: l<ℓ(I −ηlEl)2 and N ⊤
-> Invalid unicode use found on p. 26: l<ℓ(I −γlEl), where we use the convention that
-> Invalid unicode use found on p. 26: Ul = U1U2 · · · Uℓ−1,
-> Invalid unicode use found on p. 27: Dℓ= W∗(I −Nℓ)C0.
-> Invalid unicode use found on p. 27: l (I −γlEl) ⇐⇒Nl+1 = Nl −γlElNl ⇐⇒γlElNl = Nl −Nl+1.
-> Invalid unicode use found on p. 27: (Nl −Nl+1)
-> Invalid unicode use found on p. 27: C0 = W∗(I −Nℓ)C0.
-> Invalid unicode use found on p. 27: Recall that ˆD∗= W∗C0, meaning that the error Dℓ−ˆD∗is W∗NℓC0. Thus, this lemma captures a basic
-> Invalid unicode use found on p. 27: dynamics (see below), meaning that I −Nℓmay even asymptotically have a large eigenvalue corresponding to
-> Invalid unicode use found on p. 27: matrix ˜Nℓ:= (I −P0)Nℓ, where P0 projects onto the kernel of E0. Instead of this notational complication,
-> Invalid unicode use found on p. 28: −1
-> Invalid unicode use found on p. 28: λℓ+1 = (1 −ηℓλℓ)2λℓ
-> Invalid unicode use found on p. 28: λℓ+1 = (1 −ηℓλℓ)2λℓ.
-> Invalid unicode use found on p. 28: µℓ+1u1 = Eℓ+1u1 = Eℓ(I −ηℓEℓ)2u1 = (1 −ηℓµℓ)2µℓ,
-> Invalid unicode use found on p. 28: µℓ+1 −νℓ+1 = (1 −ηℓµℓ)2µℓ−(1 −ηℓνℓ)2νℓ
-> Invalid unicode use found on p. 28: = (µℓ−νℓ) −2η(µ2
-> Invalid unicode use found on p. 28: ℓ−ν2
-> Invalid unicode use found on p. 28: ℓ−ν3
-> Invalid unicode use found on p. 28: = (µℓ−νℓ)
-> Invalid unicode use found on p. 28: 1 −2ηℓ(µℓ+ νℓ) + η2
-> Invalid unicode use found on p. 28: Now, if the term multiplying (µℓ−νℓ) is nonnegative, then the claim follows. To see when this occurs, let us
-> Invalid unicode use found on p. 28: −1
-> Invalid unicode use found on p. 28: −1 within the brackets. We are left with an expression of the form
-> Invalid unicode use found on p. 28: (1 −2η(x + y) + η2(x2 + y2 + xy)),
-> Invalid unicode use found on p. 28: 1 −4η + 3η2.
-> Invalid unicode use found on p. 28: Lemma 7. Define κℓ= λℓ/λℓ, and θℓ= κℓ−1. If ηℓ≤λ
-> Invalid unicode use found on p. 28: −1/3, then θℓ+1 ≤θℓexp(−5ηℓλℓ/3). Further, if
-> Invalid unicode use found on p. 29: 1 −ηλ
-> Invalid unicode use found on p. 29: 1 −ηλ
-> Invalid unicode use found on p. 29: 1 −ηλ
-> Invalid unicode use found on p. 29: 1 −ηλ = 1 + η λ −λ
-> Invalid unicode use found on p. 29: 1 −ηλ = 1 −η λ(1 −1/(θ + 1))
-> Invalid unicode use found on p. 29: 1 −ηλ/(θ + 1) = 1 −
-> Invalid unicode use found on p. 29: θ + 1 −ηλ.
-> Invalid unicode use found on p. 29: 1 −2
-> Invalid unicode use found on p. 29: (θ + 1 −ηλ) +
-> Invalid unicode use found on p. 29: (θ + 1 −ηλ)2
-> Invalid unicode use found on p. 29: = θ + 1 −θ
-> Invalid unicode use found on p. 29: 1 −ηλ
-> Invalid unicode use found on p. 29: 2 −
-> Invalid unicode use found on p. 29: (θ + 1 −ηλ)
-> Invalid unicode use found on p. 29: 2 −
-> Invalid unicode use found on p. 29: θ + 1 −ηλ ≥2 −
-> Invalid unicode use found on p. 29: 3θ + 3 −1 = 5θ + 4
-> Invalid unicode use found on p. 29: θℓ+1 ≤θℓ−θℓ· 5/3ηℓλℓ
-> Invalid unicode use found on p. 29: 1 −ηℓλℓ
-> Invalid unicode use found on p. 29: −5ηℓλℓ/3
-> Invalid unicode use found on p. 29: 1 −ηℓλℓ
-> Invalid unicode use found on p. 29: ≤θℓexp(−ηℓλℓ).
-> Invalid unicode use found on p. 29: 1 −ηλ
-> Invalid unicode use found on p. 29: 1 −ηλ =
-> Invalid unicode use found on p. 29: 1 −L
-> Invalid unicode use found on p. 29: (θ + 1 −L)/(θ + 1),
-> Invalid unicode use found on p. 29: (θ+ + 1) = (θ + 1)3(1 −L)2
-> Invalid unicode use found on p. 29: (θ + 1 −L)2
-> Invalid unicode use found on p. 29: ⇐⇒θ+ = θ(1 −4L + 3L2) + θ2(2 −6L + 3L2) + θ3(1 −L)2
-> Invalid unicode use found on p. 29: (θ + 1 −L)2
-> Invalid unicode use found on p. 29: The statement of this Lemma has shown two decay modes of θℓ= (κℓ−1). Firstly, as long as ηℓ≤λ
-> Invalid unicode use found on p. 29: −1
-> Invalid unicode use found on p. 29: −1
-> Invalid unicode use found on p. 29: Lemma 8. Let κℓ:= λℓ/λℓ. If for all ℓ, ηℓλ = 1/3, then κℓ−1 ≤ε for all
-> Invalid unicode use found on p. 30: Proof. First using the geometric decay in Lemma 7, we know that θℓ≤(κ0 −1) exp(−5(ℓ−1)/3). Set
-> Invalid unicode use found on p. 30: ℓ0 = 2 + 3/5 log(κ0 −1). Then for ℓ≥ℓ0, we have θℓ0 ≤1/e. Further, for iterations beyond this ℓ0, the
-> Invalid unicode use found on p. 30: Tℓ≤2ℓ−ℓ0Tℓ0 ≤−2ℓ−ℓ0 =⇒θℓ≤4/3 exp(−2ℓ−ℓ0).
-> Invalid unicode use found on p. 30: We note that if E0 is not full rank, the statement holds for ˜Nℓ= (I −P0)Nℓ, where P0 projects onto the
-> Invalid unicode use found on p. 30: Lemma 9. For all ℓ, ∥Nℓ∥2 ≤exp(−P
-> Invalid unicode use found on p. 30: −1/3 and γℓ= λ
-> Invalid unicode use found on p. 30: −1, then ∥Nℓ∥2 ≤ε
-> Invalid unicode use found on p. 30: Proof. Since Nl+1 = (I −γlEl)Nl, we immediately have
-> Invalid unicode use found on p. 30: ∥I −γlEl∥2.
-> Invalid unicode use found on p. 30: But note that ∥I −γlEl∥2 = (1 −γlλl). Thus, we immediately have ∥Nℓ∥≤Q(1 −γlλl) ≤exp(P
-> Invalid unicode use found on p. 30: −1/3 for all ℓ, then λℓ≥λℓ/(1 + ε) for all ℓ≥L. But then, if
-> Invalid unicode use found on p. 30: −1, we have
-> Invalid unicode use found on p. 30: 1 −ηℓλ ≤1 −λ/λ ≤ε/(1 + ε) ≤ε,
-> Invalid unicode use found on p. 30: Proof of Theorem 1. By Lemma 4, we have Dℓ−ˆD∗= W∗NℓC0, and consequently,
-> Invalid unicode use found on p. 30: ∥Dℓ−ˆD∗∥F ≤∥W∗Nℓ∥F ∥C0∥F ≤
-> Invalid unicode use found on p. 30: −1
-> Invalid unicode use found on p. 30: ∥Aℓ∥−2
-> Invalid unicode use found on p. 30: λℓ+1 = λℓ(1 −1/3)2 = 4λℓ/9.
-> Invalid unicode use found on p. 31: ℓ(I −ηµ
-> Invalid unicode use found on p. 31: ℓ(I −ηµ
-> Invalid unicode use found on p. 31: Cℓ+1 = Cℓ−1
-> Invalid unicode use found on p. 31: ℓ∥−2
-> Invalid unicode use found on p. 31: ℓ∥−2
-> Invalid unicode use found on p. 32: ℓ(I −ηµ
-> Invalid unicode use found on p. 32: ℓ(I −ηµ
-> Invalid unicode use found on p. 32: Cℓ+1 = (I −γℓEℓ)Cℓ
-> Invalid unicode use found on p. 32: I −γℓ· 1
-> Invalid unicode use found on p. 32: Cℓ= (I −γℓEℓ)Cℓ
-> Invalid unicode use found on p. 32: (I −ηµ
-> Invalid unicode use found on p. 32: (I −γℓEℓ),
-> Invalid unicode use found on p. 32: Dℓ= W∗(I −Nℓ)C0.
-> Invalid unicode use found on p. 33: Nl+1 = (I −γlEl)Nl ⇐⇒γlElNl = Nl −Nl+1,
-> Invalid unicode use found on p. 33: and so the term in the brackets telescopes to N0 −Nℓ= I −Nℓ.
-> Invalid unicode use found on p. 33: ℓ)−1/3, and define κµ
-> Invalid unicode use found on p. 33: ℓ)−1/3. Define
-> Invalid unicode use found on p. 33: ℓ)−1/3. Thus, each of these λ
-> Invalid unicode use found on p. 34: At a high level, α−1 is the limiting condition number of the Eℓs, where deviation from perfect conditioning
-> Invalid unicode use found on p. 34: Proof of Theorem 2. Recall that D −ˆDℓ= W∗NℓC0. We again assume that λ
-> Invalid unicode use found on p. 34: ℓ)−1/3. We set γℓ= (λ
-> Invalid unicode use found on p. 34: ℓ)−1 ≤λ(Eℓ)−1. Then, as before, we have (restricted to the appropriate
-> Invalid unicode use found on p. 34: ∥I −ηℓEℓ∥2 ≤(1 −1/κℓ) ≤exp(−1/κℓ).
-> Invalid unicode use found on p. 34: ∥Nℓ∥≤exp(−
-> Invalid unicode use found on p. 34: 1/κℓ) ≤exp(−α(ℓ−L(1))/2),
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Couldn't parse in-text references '(['full visibility', ' rank-limited updates', ' and distributed computation'])' in bracket on p. 1!
-> Warning: Bracket content '2021' on p. 2 could not be matched to a reference.
   -> Sentence:  This raises a natural question: how do transformers implicitly handle such computational constraints to perform multitask learning? Can a neural network invent a numerical algorithm 
simply by learning to fill in missing data? Transformers excel at in-context learning (ICL), adapting to new tasks from a short prompt of examples Brown et al (2020); Xie et al (2021), and ICL serves as 
a simple subdomain to investigate the representational and learning properties of transformers
-> Skipping possible_ref_id '0 Σ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'ZW h K ℓ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'Cℓ Dℓ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'n d' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'd′ n′' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '18 18' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '2 2' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Warning: Bracket content 'd′ =n′ =1' on p. 8 could not be matched to a reference.
   -> Sentence:  Von Oswald et al (2023) dubbed the same update “GD++” in the scalar case (d′ =n′ =1) and interpreted it as pre-conditioned gradient descent
-> Skipping possible_ref_id 'α1 ℓIn α2 ℓIn′' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'α1 ℓ α2 ℓ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '0n α2 ℓIn′' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'Cℓ Dℓ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'Aℓ Bℓ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'randomness clustered eigenvalues' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Warning: Bracket content '2017' on p. 9 could not be matched to a reference.
   -> Sentence:  This aligns with the original motivation in Vaswani et al (2017), where low-rank constraints on WQ,ℓ, WK,ℓ, WV,ℓ, and WP,ℓwere explicitly introduced for computational efficiency
-> Skipping possible_ref_id 'min n2d d2n' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text references '(['CG', ' Hestenes and Stiefel', ' 1952'])' in bracket on p. 9!
-> Skipping possible_ref_id 'n2d d2n' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'min(nd3 dn2)' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text references '(['d = n = 1000', ' κmax = 103', ' α ≈1'])' in bracket on p. 10!
-> Skipping possible_ref_id 'EAGLE until A stabilizes then GD' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 468 sentences on 12 pages -> Avg. of 43.54545454545455 sentences per page
-> Warning: Reference 'NOT PARSEDd' never used in the document's text.
-> Warning: Reference 'J. et al 2020' never used in the document's text.
-> Warning: Reference 'Transactions 2053' never used in the document's text.
-> Warning: Reference 'Hestenes and Stiefel 1952' never used in the document's text.
-> Warning: Reference 'NOT PARSEDe' never used in the document's text.
-> Warning: Reference 'NOT PARSEDf' never used in the document's text.
-> Warning: Reference '' never used in the document's text.
-> Warning: Reference 'NOT PARSEDg' never used in the document's text.
-> Warning: Reference 'Vladymyrov 2023' never used in the document's text.
-> Warning: Reference 'NOT PARSEDh' never used in the document's text.
-> Warning: Reference 'Willems 1991' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = Ahn et al 2023); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = Akyürek et al 2022); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = Bai et al 2023); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = Ben-Israel 1965); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = NOT PARSEDd); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = J. et al 2020); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = Candès and Recht 2009); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = Candès and Tao 2010); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = Transactions 2053); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = Chen et al 2020); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = Clarkson and Woodruff 2017); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = Daneshmand 2024); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = Davenport and Romberg 2016); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = Demmel et al 2013); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = Fu et al 2024); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = Giannou et al 2023); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = Gittens and Mahoney 2016); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = Halko et al 2011); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = Hestenes and Stiefel 1952); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = Higham 1997); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = Higham 2008); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = Hoefler et al 2019); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = Ma and Chen 2020); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = Min et al 2021); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = Nanda 2023); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = Olah et al 2022); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = Radford et al 2019); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = Schulz 1933); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = NOT PARSEDe); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = Siegelmann and Sontag 1992); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = Tong and Pehlevan 2024); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = NOT PARSEDf); Skipping LLM check...
-> Missing an abstract for reference with index 32 (Ref. ID = ); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = Vladymyrov et al 2024); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = NOT PARSEDg); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = Vladymyrov 2023); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = NOT PARSEDh); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = Willems 1991); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = Williams and Seeger 2001); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = Woodruff 2014); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 7 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 7 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 13 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 1
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 2
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 3
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 4
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 5
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\41 Linear Transformers Implicitly\PAU_results.md
```