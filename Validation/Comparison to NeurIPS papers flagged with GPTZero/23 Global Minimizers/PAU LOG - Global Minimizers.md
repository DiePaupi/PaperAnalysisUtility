
Note: This paper uses a new referencing style
- "(Candes and Tao (2005); Chartrand (2007); Chartrand and Staneva (2008); Foucart and Lai (2009))"
- "(Parhi and Nowak (2021, 2022); Shenouda et al. (2024))"

---

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\23 Global Minimizers\Global Minimizers of ℓ.pdf"
---
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
- Found following heading '2 - Related work' on page 2
- Found following heading '3 - Univariate ℓp-regularized neural networks' on page 4
- Found following heading '4 - Multivariate ℓp-regularized neural networks' on page 8
- Found following heading '5 - Conclusion and Discussion' on page 10
=> Found references/literature section on page 10
- Found first appendix 'A - Proofs of main results' on page 13
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 13
All found references: 46
-----------
 -> Parsed references DataFrame:
                          ref_id                                            authors  ... link  valid
0     Aliprantis and Border 2006                      C D Aliprantis and K C Border  ...        None
1   Boursier and Flammarion 2023                        E Boursier and N Flammarion  ...        None
2              Bubeck et al 2020       S Bubeck, R Eldan, Y T Lee, and D Mikulincer  ...        None
3            Candes and Tao 2005                               E J Candes and T Tao  ...        None
4                 Chartrand 2007                                        R Chartrand  ...        None
5     Chartrand and Staneva 2008                          R Chartrand and V Staneva  ...        None
6             Debarre et al 2022      T Debarre, Q Denoyelle, M Unser, and J Fageot  ...        None
7       Dudley and Norvaiša 2006                          R M Dudley and R Norvaiša  ...        None
8         Ergen and Pilanci 2021                              T Ergen and M Pilanci  ...        None
9                Fan and Li 2001                                     J Fan and R Li  ...        None
10           Foucart and -J 2009                                 S Foucart and M -J  ...        None
11       Frank and Friedman 1993                         L E Frank and J H Friedman  ...        None
12       Frankle and Carbin 2018                             J Frankle and M Carbin  ...        None
13                  Goemans 2009                                        M X Goemans  ...        None
14               Gong et al 2022                   M Gong, F Yu, J Zhang, and D Tao  ...        None
15                Guo et al 2016                           Y Guo, A Yao, and Y Chen  ...        None
16                Guo et al 2018                Y Guo, C Zhang, C Zhang, and Y Chen  ...        None
17                Han et al 2015                 S Han, J Pool, J Tran, and W Dally  ...        None
18                    Hanin 2022                                            B Hanin  ...        None
19            Hassibi et al 1993                B Hassibi, D G Stork, and G J Wolff  ...        None
20          Hinton and Camp 1993                          G E Hinton and D Van Camp  ...        None
21                  Jameson 2006                                        G J Jameson  ...        None
22            Knight and Fu 2000                                  K Knight and W Fu  ...        None
23              LeCun et al 1989                     Y LeCun, J Denker, and S Solla  ...        None
24               Liao et al 2022   N Liao, S Wang, L Xiang, N Ye, S Shao, and P Chu  ...        None
25                Liu et al 2022                      S Liu, Z Zhu, Q Qu, and C You  ...        None
26            Louizos et al 2018               C Louizos, M Welling, and D P Kingma  ...        None
27          Molchanov et al 2017               D Molchanov, A Ashukha, and D Vetrov  ...        None
28      Mozer and Smolensky 1988                          M C Mozer and P Smolensky  ...        None
29          Neyshabur et al 2015               B Neyshabur, R Tomioka, and N Srebro  ...        None
30                       Ng 2004                                             A Y Ng  ...        None
31                     Ojha 2000                                           P C Ojha  ...        None
32     Outmezguine and Levi 2024                         N J Outmezguine and N Levi  ...        None
33          Parhi and Nowak 2021                              R Parhi and R D Nowak  ...        None
34          Parhi and Nowak 2022                              R Parhi and R D Nowak  ...        None
35               Peng et al 2015                            J Peng, S Yue, and H Li  ...        None
36        Pilanci and Ergen 2020                              M Pilanci and T Ergen  ...        None
37         Scardapane et al 2017  S Scardapane, D Comminiello, A Hussain, and A ...  ...        None
38           Shenouda et al 2024          J Shenouda, R Parhi, K Lee, and R D Nowak  ...        None
39        Srinivas and Babu 2017                            S Srinivas and R V Babu  ...        None
40                  Stanley 2007                                  R P Stanley et al  ...        None
41                Wen et al 2016              W Wen, C Wu, Y Wang, Y Chen, and H Li  ...        None
42                   Winder 1966                                         R O Winder  ...        None
43              Zhang et al 2016  C Zhang, S Bengio, M Hardt, B Recht, and O Vin...  ...        None
44              Zhang et al 2018                 T Zhang, S Ye, K Zhang, and J Tang  ...        None
45               Zhou et al 2019               H Zhou, J Lan, R Liu, and J Yosinski  ...        None

[46 rows x 10 columns]
- Checking reference 1/46:
  -> INFO: Now checking 10 results for matching title: 'Infinite dimensional analysis: a hitchhiker’s guide'
       -> INFO: All authors matched!
       -> WARNING: Year (1994) does not match expected year (2006)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/46:
  -> INFO: Now checking 1 results for matching title: 'Penalising the biases in norm regularisation enforces sparsity'
       -> INFO: All authors matched!
- Checking reference 3/46:
  -> INFO: Now checking 2 results for matching title: 'Network size and size of the weights in memorization with two-layers neural networks'
       -> INFO: All authors matched!
- Checking reference 4/46:
  -> INFO: Now checking 10 results for matching title: 'Decoding by linear programming'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Candès'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 5/46:
  -> INFO: Now checking 10 results for matching title: 'Exact reconstruction of sparse signals via nonconvex minimization'
       -> INFO: All authors matched!
- Checking reference 6/46:
  -> INFO: Now checking 10 results for matching title: 'Restricted isometry properties and nonconvex compressive sensing'
       -> INFO: All authors matched!
       -> WARNING: Year (2007) does not match expected year (2008)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/46:
  -> INFO: Now checking 10 results for matching title: 'Sparsest piecewise-linear regression of one-dimensional data'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/46:
  -> INFO: Now checking 10 results for matching title: 'Product integrals, young integrals and p-variation'
       -> INFO: All authors matched!
       -> WARNING: Year (1999) does not match expected year (2006)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/46:
  -> INFO: Now checking 1 results for matching title: 'Convex geometry and duality of over-parameterized neural networks'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/46:
  -> INFO: Now checking 10 results for matching title: 'Variable selection via nonconcave penalized likelihood and its oracle properties'
       -> INFO: All authors matched!
- Checking reference 11/46:
  -> INFO: Now checking 10 results for matching title: 'Lai'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Foucart', '-J', '2009']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Lai manually and check the results.
        -> Author(s): S Foucart and M -J
        -> Title:     Lai
        -> Year:      2009
     -> Manual search was skipped by the user.
- Checking reference 12/46:
  -> INFO: Now checking 10 results for matching title: 'A statistical view of some chemometrics regression tools'
       -> INFO: All authors matched!
- Checking reference 13/46:
  -> INFO: Now checking 10 results for matching title: 'The lottery ticket hypothesis: Finding sparse, trainable neural networks'
       -> INFO: All authors matched!
- Checking reference 14/46:
  -> WARNING: Skipping search (due to not enough info) for reference titled '3'
           -> Author(s): M X Goemans
           -> Year: 2009
- Checking reference 15/46:
  -> INFO: Now checking 10 results for matching title: 'Efficient ℓp norm regularization for learning sparsity in deep neural networks'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 9 results for matching title: 'Efficient ℓp norm regularization for learning sparsity in deep neural networks'
  -> WARNING: None of the 9 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Efficient+ℓp+norm+regularization+for+learning+sparsity+in+deep+neural+networks manually and check the results.
        -> Author(s): M Gong, F Yu, J Zhang, and D Tao
        -> Title:     Efficient ℓp norm regularization for learning sparsity in deep neural networks
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 16/46:
  -> INFO: Now checking 10 results for matching title: 'Dynamic network surgery for efficient dnns'
       -> INFO: All authors matched!
- Checking reference 17/46:
  -> INFO: Now checking 10 results for matching title: 'Sparse dnns with improved adversarial robustness'
       -> INFO: All authors matched!
- Checking reference 18/46:
  -> INFO: Now checking 10 results for matching title: 'Learning both weights and connections for efficient neural network'
       -> INFO: All authors matched!
- Checking reference 19/46:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: On the implicit bias of weight decay in shallow univariate ReLU networks
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 32 results for matching title: 'On the implicit bias of weight decay in shallow univariate ReLU networks'
  -> WARNING: None of the 32 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=On+the+implicit+bias+of+weight+decay+in+shallow+univariate+ReLU+networks manually and check the results.
        -> Author(s): B Hanin
        -> Title:     On the implicit bias of weight decay in shallow univariate ReLU networks
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 20/46:
  -> INFO: Now checking 10 results for matching title: 'Optimal brain surgeon and general network pruning'
       -> INFO: All authors matched!
- Checking reference 21/46:
  -> INFO: Now checking 1 results for matching title: 'Keeping the neural networks simple by minimizing the description length of the weights'
       -> INFO: All authors matched!
- Checking reference 22/46:
  -> INFO: Now checking 1 results for matching title: 'Counting zeros of generalised polynomials: Descartes’ rule of signs and Laguerre’s extensions'
       -> INFO: All authors matched!
- Checking reference 23/46:
  -> INFO: Now checking 10 results for matching title: 'Asymptotics for lasso-type estimators'
       -> INFO: All authors matched!
- Checking reference 24/46:
  -> INFO: Now checking 10 results for matching title: 'Optimal brain damage'
       -> INFO: All authors matched!
- Checking reference 25/46:
  -> INFO: Now checking 10 results for matching title: 'Achieving adversarial robustness via sparsity'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Zhang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/46:
  -> INFO: Now checking 10 results for matching title: 'Robust training under label noise by over-parameterization'
       -> INFO: All authors matched!
- Checking reference 27/46:
  -> INFO: Now checking 10 results for matching title: 'Learning sparse neural networks through l0 regularization'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 28/46:
  -> INFO: Now checking 10 results for matching title: 'Variational dropout sparsifies deep neural networks'
       -> INFO: All authors matched!
- Checking reference 29/46:
  -> INFO: Now checking 3 results for matching title: 'Skeletonization: A technique for trimming the fat from a network via relevance assessment'
       -> INFO: All authors matched!
- Checking reference 30/46:
  -> INFO: Now checking 10 results for matching title: 'Norm-based capacity control in neural networks'
       -> INFO: All authors matched!
- Checking reference 31/46:
  -> INFO: Now checking 10 results for matching title: 'Feature selection, l1 vs'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 916 results for matching title: 'Feature selection, l1 vs'
  -> WARNING: None of the 916 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Feature+selection%2C+l1+vs manually and check the results.
        -> Author(s): A Y Ng
        -> Title:     Feature selection, l1 vs
        -> Year:      2004
     -> Manual search was skipped by the user.
- Checking reference 32/46:
  -> INFO: Now checking 1 results for matching title: 'Enumeration of linear threshold functions from the lattice of hyperplane intersections'
       -> INFO: All authors matched!
- Checking reference 33/46:
  -> INFO: Now checking 10 results for matching title: 'Decoupled weight decay for any p norm'
       -> INFO: All authors matched!
- Checking reference 34/46:
  -> INFO: Now checking 2 results for matching title: 'Banach space representer theorems for neural networks and ridge splines'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 35/46:
  -> INFO: Now checking 6 results for matching title: 'What kinds of functions do deep neural networks learn? insights from variational spline theory'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 36/46:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: NP/CMP equivalence: A phenomenon hidden among sparsity models l0 minimization and lp minimization for information processing
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 412 results for matching title: 'NP/CMP equivalence: A phenomenon hidden among sparsity models l0 minimization and lp minimization for information processing'
  -> WARNING: None of the 412 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=NP/CMP+equivalence:+A+phenomenon+hidden+among+sparsity+models+l0+minimization+and+lp+minimization+for+information+processing manually and check the results.
        -> Author(s): J Peng, S Yue, and H Li
        -> Title:     NP/CMP equivalence: A phenomenon hidden among sparsity models l0 minimization and lp minimization for information processing
        -> Year:      2015
     -> Manual search was skipped by the user.
- Checking reference 37/46:
  -> INFO: Now checking 10 results for matching title: 'Neural networks are convex regularizers: Exact polynomial-time convex optimization formulations for two-layer networks'
       -> INFO: All authors matched!
- Checking reference 38/46:
  -> INFO: Now checking 10 results for matching title: 'Group sparse regularization for deep neural networks'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 39/46:
  -> INFO: Now checking 1 results for matching title: 'Variation spaces for multi-output neural networks: Insights on multi-task learning and network compression'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 40/46:
  -> INFO: Now checking 10 results for matching title: 'Training sparse neural networks'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Subramanya'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 41/46:
  -> INFO: Now checking 2 results for matching title: 'An introduction to hyperplane arrangements'
       -> INFO: All authors matched!
- Checking reference 42/46:
  -> INFO: Now checking 10 results for matching title: 'Learning structured sparsity in deep neural networks'
       -> INFO: All authors matched!
- Checking reference 43/46:
  -> INFO: Now checking 10 results for matching title: 'Partitions of n-space by hyperplanes'
       -> INFO: All authors matched!
- Checking reference 44/46:
  -> INFO: Now checking 10 results for matching title: 'Understanding deep learning requires rethinking generalization'
       -> INFO: All authors matched!
- Checking reference 45/46:
  -> INFO: Now checking 10 results for matching title: 'Systematic weight pruning using alternating direction method of multipliers'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 29 results for matching title: 'Systematic weight pruning using alternating direction method of multipliers'
  -> WARNING: None of the 29 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Systematic+weight+pruning+using+alternating+direction+method+of+multipliers manually and check the results.
        -> Author(s): T Zhang, S Ye, K Zhang, and J Tang
        -> Title:     Systematic weight pruning using alternating direction method of multipliers
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 46/46:
  -> INFO: Now checking 1 results for matching title: 'Deconstructing lottery tickets: Zeros, signs, and the supermask'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 1: N −2 active neurons. In contrast, ℓ1 path norm minimization alone is not guaranteed to implicitly
-> Invalid unicode use found on p. 4: PnP−1
-> Invalid unicode use found on p. 4: |Df(xi+1) −Df(xi)|p = supπ
-> Invalid unicode use found on p. 4: the slopes si := yi+1−yi
-> Invalid unicode use found on p. 4: xi+1−xi of the straight lines ℓi connecting (xi, yi) and (xi+1, yi+1). The discrete curvature
-> Invalid unicode use found on p. 4: at a data point xi refers to ϵi := sgn(si −si−1), which is positive if the slope of the straight lines between
-> Invalid unicode use found on p. 4: such region. Additionally, Theorem 3.1 says that solutions to (5) for 0 < p < 1 have at most N −2 knots.
-> Invalid unicode use found on p. 4: choice of network width K, as long as K ≥N −2.
-> Invalid unicode use found on p. 5: function in Fig. 2a on (−∞, x7] and [x10, ∞). The only possible ambiguity occurs between x7 and x10, where
-> Invalid unicode use found on p. 5: ϵi−1 ̸= ϵi = ϵi+1 = · · · = ϵi+m ̸= ϵi+m+1):
-> Invalid unicode use found on p. 5: (a) If m = 1, then f has a single knot between xi and xi+1, with incoming/outgoing slopes si−1 at xi
-> Invalid unicode use found on p. 5: (b) If m ≥2, then f has incoming slope si−1 at xi and outgoing slope si+m at xi+m. Between xi
-> Invalid unicode use found on p. 5: and xi+m, f takes on at most m −1 slopes u1, . . . , um−1 distinct from si−1 and si+m. Each uj is
-> Invalid unicode use found on p. 5: between si+j−1 and si+j, inclusive, and its corresponding segment passes through (xi+j, yi+j).
-> Invalid unicode use found on p. 5: path norm interpolant, and can be represented by a network with no more than N −2 neurons.
-> Invalid unicode use found on p. 6: k=1 |vkwk| = PN−2
-> Invalid unicode use found on p. 6: i=1 |si+1−
-> Invalid unicode use found on p. 6: si|, and Lipschitz constant L ≤maxi=1,...,N−1 |si|.
-> Invalid unicode use found on p. 6: Regarding the N −2 neuron bound in Corollary 3.1.1, we note that this bound applies to any minimum
-> Invalid unicode use found on p. 6: N −2 knots, but also solutions with arbitrarily many knots (Hanin (2022); Debarre et al. (2022)); see Fig. 1a.
-> Invalid unicode use found on p. 6: norm solution for small enough p—are known to have as many as N −2 active neurons and as few as O(N/2)
-> Invalid unicode use found on p. 7: concave function over the hypercube [0, 1]m−1. This reformulation is possible because, by Theorem 3.1,
-> Invalid unicode use found on p. 7: slopes u1, . . . , um−1 of any f ∈S on such an interval [xi, xi+m] can be expressed as convex combinations
-> Invalid unicode use found on p. 7: uj := (1 −αj)si+j−1 + αjsi+j, and any such solution f ∈S can be fully identified with its corresponding
-> Invalid unicode use found on p. 7: vector of the corresponding parameters [α1, . . . , αj−1]⊤∈[0, 1]m−1. Expressed in terms of these parameters
-> Invalid unicode use found on p. 7: [α1, . . . , αj−1]⊤∈[0, 1]m−1, the cost Vp is strictly concave. Therefore, by the Bauer Maximum Principle,
-> Invalid unicode use found on p. 7: [0, 1]m−1. Having restricted the set of possible candidate solutions to this finite set (which can be shown to
-> Invalid unicode use found on p. 8: DjX(νj −ωj) = y,
-> Invalid unicode use found on p. 8: (2Dj −I)Xνj ≥0, (2Dj −I)Xωj ≥0, ∥νj∥∞≤R, ∥ωj∥∞≤R, ∀j
-> Invalid unicode use found on p. 8: −βj, ω′
-> Invalid unicode use found on p. 12: of the form (1) can have its parameters rescaled as vk 7→|wk|vk, (wk, bk) 7→|wk|−1(wk, bk) without changing
-> Invalid unicode use found on p. 12: vk(wkx + bk)+ + vk′(wk′x + bk′)+ = (vk + vk′)(wkx + bk)+ −vk′(wkx + bk)
-> Invalid unicode use found on p. 12: if wk = −wk′. (The latter uses the identity x = (x)+ −(−x)+.) In either case, we see that the original two
-> Invalid unicode use found on p. 12: is located at −bk/wk, and the slope change of the function at knot k is vk. Conversely, any R →R CPWL
-> Invalid unicode use found on p. 12: f(x) = f(u0) + f ′(u0)(x −u0) +
-> Invalid unicode use found on p. 12: vk(x −uk)+
-> Invalid unicode use found on p. 12: p, 0 ≤p < 1, if the signs of si −sin(f, xi) and sout(f, xi+1) −si agree, then f
-> Invalid unicode use found on p. 13: Figure 3: Left: Illustration of the case sgn (si −sin(f, xi)) = sgn (sout(f, xi+1) −si) addressed in Lemma A.1.
-> Invalid unicode use found on p. 13: Right: illustration of the case sgn (si −sin(f, xi)) ̸= sgn (sout(f, xi+1) −si) addressed in Lemma A.2. In both
-> Invalid unicode use found on p. 13: sgn (si −sin(f, xi)) = sgn (sout(f, xi+1) −si) at consecutive data points xi, xi+1. If both signs are zero, then
-> Invalid unicode use found on p. 13: f is linear on the interval I := [xi −δ, xi+1 + δ] surrounding [xi, xi+1], for small δ > 0. Otherwise, f has a
-> Invalid unicode use found on p. 13: |sout(f, xi+1) −sin(f, xi)|p < |sout(f, xi+1) −uJ|p + |uJ −uJ−1|p + · · · + |u2 −u1|p + |u1 −sin(f, xi)|p
-> Invalid unicode use found on p. 13: Next, Lemma A.2 says that if the signs of si −sin(f, xi) and sout(f, xi+1) −si of an optimal f ∈S∗
-> Invalid unicode use found on p. 13: has sgn (si −sin(f, xi)) ̸= sgn (sout(f, xi+1) −si) at consecutive data points xi, xi+1. If 0 < p < 1, then f
-> Invalid unicode use found on p. 13: x−xi
-> Invalid unicode use found on p. 13: xi+1−xi and assume that sgn(a −b) ̸= sgn(b −c). The intermediate slopes u1 and
-> Invalid unicode use found on p. 13: u2 can be parameterized as u1 = b + δ and u2 = b −
-> Invalid unicode use found on p. 13: 1−τ δ for some δ ∈R. Consider the cost Vp(f
-> Invalid unicode use found on p. 13: the interval I := (xi −ϵ, xi+1 + ϵ) (for some arbitrary ϵ > 0) as a function C(δ) of the parameter δ. If p = 0,
-> Invalid unicode use found on p. 13: C(δ) := |δ + b −a|p +
-> Invalid unicode use found on p. 13: (1 −τ)p |δ|p +
-> Invalid unicode use found on p. 13: c −b +
-> Invalid unicode use found on p. 13: 1 −τ δ
-> Invalid unicode use found on p. 14: single knot at some x ∈(xi, xi+1) where sgn(a −b) ̸= sgn(b −c). Here τ :=
-> Invalid unicode use found on p. 14: x−xi
-> Invalid unicode use found on p. 14: xi+1−xi .
-> Invalid unicode use found on p. 14: undefined. The three points where C′ is undefined are δ1 = a −b, δ2 = 0, and δ3 = 1−τ
-> Invalid unicode use found on p. 14: τ (b −c). Assuming
-> Invalid unicode use found on p. 14: without loss of generality that δ1 < δ2 < δ3, note that C is concave on the intervals (−∞, δ1), (δ1, δ2), (δ2, δ3),
-> Invalid unicode use found on p. 14: (1 −τ)p |a −b|p +
-> Invalid unicode use found on p. 14: 1 −τ a −
-> Invalid unicode use found on p. 14: 1 −τ b
-> Invalid unicode use found on p. 14: C(δ2) = |b −a|p + |c −b|p
-> Invalid unicode use found on p. 14: τ b −1 −τ
-> Invalid unicode use found on p. 14: c −a
-> Invalid unicode use found on p. 14: τ p |b −c|p
-> Invalid unicode use found on p. 14: (1 −t)p |a −b|p +
-> Invalid unicode use found on p. 14: 1 −ta −
-> Invalid unicode use found on p. 14: 1 −tb
-> Invalid unicode use found on p. 14: (1 −t)p+1 |a −b|p + p
-> Invalid unicode use found on p. 14: 1 −ta −
-> Invalid unicode use found on p. 14: 1 −tb
-> Invalid unicode use found on p. 14: p−1sgn
-> Invalid unicode use found on p. 14: 1 −ta −
-> Invalid unicode use found on p. 14: 1 −tb
-> Invalid unicode use found on p. 14: a −b
-> Invalid unicode use found on p. 14: (1 −t)2
-> Invalid unicode use found on p. 14: (1 −t)p+1 |a −b|p + p
-> Invalid unicode use found on p. 14: 1 −ta −
-> Invalid unicode use found on p. 14: 1 −tb
-> Invalid unicode use found on p. 14: p−1sgn
-> Invalid unicode use found on p. 14: (1 −t)(c −b) + t(a −b)
-> Invalid unicode use found on p. 14: 1 −t
-> Invalid unicode use found on p. 14: a −b
-> Invalid unicode use found on p. 14: (1 −t)2
-> Invalid unicode use found on p. 14: Assuming that sgn(a −b) ̸= sgn(b −c) with a ̸= b (and thus δ1 ̸= δ2), we see that h′
-> Invalid unicode use found on p. 14: t b −1 −t
-> Invalid unicode use found on p. 14: c −a
-> Invalid unicode use found on p. 14: tp |b −c|p
-> Invalid unicode use found on p. 14: t b −1 −t
-> Invalid unicode use found on p. 14: c −a
-> Invalid unicode use found on p. 14: p−1 sgn
-> Invalid unicode use found on p. 14: t b −1 −t
-> Invalid unicode use found on p. 14: c −a
-> Invalid unicode use found on p. 14:  c −b
-> Invalid unicode use found on p. 14: −
-> Invalid unicode use found on p. 14: tp+1 |b −c|p
-> Invalid unicode use found on p. 14: t b −1 −t
-> Invalid unicode use found on p. 14: c −a
-> Invalid unicode use found on p. 14: p−1 sgn
-> Invalid unicode use found on p. 14: t(b −a) + (1 −t)(b −c)
-> Invalid unicode use found on p. 14:  c −b
-> Invalid unicode use found on p. 14: −
-> Invalid unicode use found on p. 14: tp+1 |b −c|p
-> Invalid unicode use found on p. 15: Assuming that sgn(a −b) ̸= sgn(b −c) with b ̸= c (and thus δ2 ̸= δ3), we see that h′
-> Invalid unicode use found on p. 15: with slopes u2, . . . , uJ−1 and connect the segments with u1 and uJ in a single knot inside (xi, xi+1); this
-> Invalid unicode use found on p. 15: Linearity before x2 and after xN−1.
-> Invalid unicode use found on p. 15: We will prove the statement for (−∞, x2]; the proof for [xN−1, ∞)
-> Invalid unicode use found on p. 15: that sgn(s1 −sin(f, x1)) = sgn(sout(f, x2) −s1), and by Lemma A.1, this knot is the only one inside (x1, x2),
-> Invalid unicode use found on p. 15: that sgn(s1 −sin(f, x1)) = sgn(sout(f, x2) −s1) = −1, we have sin(f, x1) > s1 > sout(f, x2), and therefore
-> Invalid unicode use found on p. 15: |sout(f, x2) −sin(f, x1)| > |sout(f, x2) −s1|. But this shows that Vp(f) > Vp(g), where g = ℓ1 on (−∞, x2]
-> Invalid unicode use found on p. 16: 0. As argued above, f has no knots on (−∞, x1]. If sgn(s1 −sin(f, x1)) ̸=
-> Invalid unicode use found on p. 16: sgn(sout(f, x2) −s1), then by Lemma A.2, either f = ℓ1 on [x1, x2] (hence it also must agree with ℓ1 on
-> Invalid unicode use found on p. 16: (−∞, x1]), or there is some g ∈S∗
-> Invalid unicode use found on p. 16: 0 which agrees with ℓ1 on [x1, x2] (hence also on (−∞, x1], since g must also
-> Invalid unicode use found on p. 16: not have any knots on (−∞, x1]). If sgn(s1 −sin(f, x1)) = sgn(sout(f, x2) −s1) = 0, then by Lemma A.1,
-> Invalid unicode use found on p. 16: f = ℓ1 on [x1, x2] and thus also on (−∞, x1]. If sgn(s1 −sin(f, x1)) = sgn(sout(f, x2) −s1) are both nonzero,
-> Invalid unicode use found on p. 16: as in Fig. 7a. Then function depicted in Fig. 7, which agrees with ℓ1 on (−∞, x2] and with f on [x2, ∞), has
-> Invalid unicode use found on p. 16: p does not agree with ℓi on an interval [xi, xi+1] where sgn(si −si−1) ̸= sgn(si+1 −si).
-> Invalid unicode use found on p. 16: By Lemmas A.1 and A.2, it must be the case that sgn(si −sin(f, xi)) = sgn(sout(f, xi+1) −si) are both
-> Invalid unicode use found on p. 16: (b) A function which agrees with ℓ1 on (−∞, x2].
-> Invalid unicode use found on p. 17: sgn(si −si−1) ̸= sgn(si −sin(f, xi)) and/or that sgn(si+1 −si) ̸= sgn(sout(f, xi+1) −si). Assume without loss
-> Invalid unicode use found on p. 17: of generality that sgn(si+1 −si) ̸= sgn(sout(f, xi+1) −si) = 1, so that si+1 ≤si < sout(f, xi+1) = sin(f, xi+1).
-> Invalid unicode use found on p. 17: Lemma A.1 and Lemma A.2, it must be the case that −1 = sgn(si+1 −sin(f, xi+1)) = sgn(sout(f, xi+2) −
-> Invalid unicode use found on p. 17: sgn(sout(f, xi+1) −si) = sgn(si −sin(f, xi)), we have sin(f, xi) < si < sout(xi+1). On I := [xi−1 −ϵ, xi+2 + ϵ]
-> Invalid unicode use found on p. 17: I) = |sout(f, xi+1) −sin(f, xi)|p + |sout(f, xi+2) −sout(f, xi+1)|p
-> Invalid unicode use found on p. 17: > |si −sin(f, xi)|p + |sout(f, xi+2) −si|p = Vp(g
-> Invalid unicode use found on p. 17: 0. If sgn(si −sin(f, xi)) ̸= sgn(sout(f, xi+1) −si), then by Lemma A.2,
-> Invalid unicode use found on p. 17: if sgn(si −sin(f, xi)) = sgn(sout(f, xi+1) −si) = 0, then f = ℓi on [xi, xi+1]. If sgn(si −sin(f, xi)) =
-> Invalid unicode use found on p. 17: sgn(sout(f, xi+1) −si) are both nonzero, then by Lemma A.1, sin(f, xi) = sout(f, xi) and sin(f, xi+1) =
-> Invalid unicode use found on p. 17: xi+1 meet. As before, it must be the case that sgn(si−si−1) ̸= sgn(si−sin(f, xi)) and/or that sgn(si+1−si) ̸=
-> Invalid unicode use found on p. 17: sgn(sout(f, xi+1) −si). Assume without loss of generality that sgn(si+1 −si) ̸= sgn(sout(f, xi+1) −si) = 1,
-> Invalid unicode use found on p. 17: so that si+1 ≤si < sout(f, xi+1) = sin(f, xi+1). Because 1 = sgn(sout(f, xi+1) −si) = sgn(si −sin(f, xi)),
-> Invalid unicode use found on p. 17: we also have sin(f, xi) < si < sout(f, xi+1). If sgn(sout(f, xi+2) −si+1) ̸= sgn(si+1 −sin(f, xi+1)) = −1,
-> Invalid unicode use found on p. 17: [xi+1, xi+2]. Then this g has sout(g, xi+1) = si and sin(g, xi) = sin(f, xi), so sgn(sout(xi+1) −si) ∈{−1, 0},
-> Invalid unicode use found on p. 17: and sgn(si−sin(g, xi)) = 1; hence by Lemma A.2, there is some h ∈S∗
-> Invalid unicode use found on p. 17: and agrees with ℓi on [xi, xi+1]. On the other hand, if sgn(sout(f, xi+2)−si+1) = sgn(si+1−sin(f, xi+1)) = −1,
-> Invalid unicode use found on p. 17: This function has two knots on I := [xi−1 −ϵ, xi+2 + ϵ] (for small ϵ > 0). The function g depicted in Fig. 8b,
-> Invalid unicode use found on p. 17: si+m−1 = sout(f, xi+m), then f must agree with ℓi = · · · = ℓi+m−1 on [xi, xi+m], since any other function
-> Invalid unicode use found on p. 17: I) on I := [xi −ϵ, xi+m + ϵ] for small ϵ > 0. If sgn(si −sin(f, xi)) ̸=
-> Invalid unicode use found on p. 18: sgn(sout(f, xi+m)−si), then the argument in the proof of Lemma A.2 shows that f must agree with ℓi = · · · =
-> Invalid unicode use found on p. 18: ℓi+m−1 on [xi, xi+m]. So we need only consider the case where sgn(si −sin(f, xi)) = sgn(sout(f, xi+m) −si)
-> Invalid unicode use found on p. 18: If f = ℓi on both [xi, xi+1] and [xi+m−1, xi+m], then it also must agree with ℓi on [xi+1, xi+m−1] (otherwise
-> Invalid unicode use found on p. 18: applies on the remaining intervals up to and including [xi+m−1, xi+m] (see Fig. 9). Note that if m is even, we
-> Invalid unicode use found on p. 18: will have sin(f, xi+m−1) = sout(f, xi+m−1) > si+m−1 = si > sin(f, xi+m) = sout(f, xi+m), contradicting the
-> Invalid unicode use found on p. 18: assumption that sgn(sout(f, xi+m) −si) = 1 (see Fig. 9a). If m is odd, as in Fig. 9b, we have
-> Invalid unicode use found on p. 18: I) = |sout(f, xi+1) −sin(f, xi)|p + |sout(f, xi+2) −sout(f, xi+1)|p
-> Invalid unicode use found on p. 18: + · · · + |sout(f, xi+m) −sout(f, xi+m−1)|p
-> Invalid unicode use found on p. 18: > |si −sin(f, xi)|p + |sout(f, xi+m) −si+m−1|p = Vp(g
-> Invalid unicode use found on p. 18: where g is the function which agrees with f outside of [xi, xi+m] and agrees with ℓi = · · · = ℓi+m−1 on
-> Invalid unicode use found on p. 18: 0. If sin(f, xi) = si = · · · = si+m−1 = sout(f, xi+m), then f must agree
-> Invalid unicode use found on p. 18: with ℓi = · · · = ℓi+m−1 on [xi, xi+m] and if sgn(si −sin(f, xi)) ̸= sgn(sout(f, xi+m) −si), then the proof of
-> Invalid unicode use found on p. 18: [xi, xi+m]. If sgn(si −sin(f, xi)) = sgn(sout(f, xi+m) −si) are both nonzero, then there must be at least one
-> Invalid unicode use found on p. 18: with exactly two knots on [xi −ϵ, xi+m + ϵ], and thus g ∈S∗
-> Invalid unicode use found on p. 18: then f = ℓ1 on (−∞, x2] by Theorem 3.1,1. If i > 2, then by assumption, sgn(si−1 −si−2) ̸= sgn(si −si−1),
-> Invalid unicode use found on p. 19: so by Theorem 3.1,1, f = ℓi−1 on [xi−1, xi]. In either case, we have sin(f, xi) = si−1. An analogous
-> Invalid unicode use found on p. 19: sin(g, xi) = si−1 and sout(g, xi+1) = si+1. In both cases, the conclusion then follows from Lemma A.2.
-> Invalid unicode use found on p. 19: As in the proof of Theorem 3.1,2a above, the assumptions guarantee that si−1 = sin(f, xi) and si+m =
-> Invalid unicode use found on p. 19: sgn(si −si−1) = sgn(si+1 −si) = · · · = sgn(si+m −si+m−1) = 1.
-> Invalid unicode use found on p. 19: In the base case m = 2, first suppose that sgn(si −sin(f, xi)) ̸= sgn(sout(f, xi+1) −si). Since sin(f, xi) =
-> Invalid unicode use found on p. 19: si−1 < si by assumption, it must be the case that sgn(sout(f, xi+1) −si) ∈{0, −1}. If sgn(sout(f, xi+1) −
-> Invalid unicode use found on p. 19: si) = −1, Lemma A.2 implies that f = ℓi on [xi, xi+1], and thus sin(f, xi+1) = si. But then we have
-> Invalid unicode use found on p. 19: sout(f, xi+1), contradicting sgn(sout(f, xi+1) −si) = −1 (see Fig. 11b).
-> Invalid unicode use found on p. 19: If sgn(sout(f, xi+1) −si) = 0,
-> Invalid unicode use found on p. 19: On the other hand, still for the base case m = 2, suppose that sgn(si −sin(f, xi)) = sgn(sout(f, xi+1) −si).
-> Invalid unicode use found on p. 19: Then by Lemma A.1, there is a single knot inside [xi, xi+1], with si−1 = sin(f, xi) = sout(f, xi) and
-> Invalid unicode use found on p. 19: we would have −1 = sgn(si+1 −sin(f, xi+1)) ̸= sgn(sout(f, xi+2) −si+1) = 1, and that would imply by
-> Invalid unicode use found on p. 19: 0 = sgn(si+1 −sin(f, xi+1) ̸= sgn(sout(f, xi+2) −si+1) = 1, so by Lemma A.2, f = ℓi+1 on [xi+1, xi+2]. The
-> Invalid unicode use found on p. 20: (a) si+m−2 < um−1 < si+m−1
-> Invalid unicode use found on p. 20: (b) um−2 = um−1 = si+m−2
-> Invalid unicode use found on p. 20: Assuming inductively that Theorem 3.1,2b holds for 2, . . . , m −1, both satisfy si+j−1 ≤uj ≤si+j for
-> Invalid unicode use found on p. 20: j = 1, . . . , m −1.
-> Invalid unicode use found on p. 20: integers 2, . . . , m −1. First suppose that sout(f, xi+m−1) > si+m−2. Then by the inductive hypothesis, f
-> Invalid unicode use found on p. 20: sin(f, xi) = si−1 and sout(f, xi+m−1)—on [xi, xi+m−1] satisfying si+j−1 ≤uj ≤si+j for all j = 1, . . . , m −2.
-> Invalid unicode use found on p. 20: It cannot be the case that sout(f, xi+m−1) > si+m−1, because if this were true, we would have −1 =
-> Invalid unicode use found on p. 20: sgn(si+m−1 −sin(f, xi+m−1)) ̸= sgn(sout(f, xi+m) −si+m−1) = 1, and thus Lemma A.2 would imply that
-> Invalid unicode use found on p. 20: f = ℓi+m−1 on [xi+m−1, xi+m], contradicting sout(f, xi+m−1) > si+m−1 (see Fig. 11b). Therefore, we must
-> Invalid unicode use found on p. 20: have sout(f, xi+m−1) ≤si+m−1. If sout(f, xi+m−1) < si+m−1, then by Lemma A.1, there is a single knot
-> Invalid unicode use found on p. 20: inside [xi+m−1, xi+m] and sin(f, xi+m−1) = sout(f, xi+m−1) and sin(f, xi+m) = sout(f, xi+m) = si+m. The
-> Invalid unicode use found on p. 20: conclusion then holds for m with um−1 := sout(f, xi+m−1) (see Fig. 12a). If sout(f, xi+m−1) = si+m−1, then by
-> Invalid unicode use found on p. 20: Lemmas A.1 and A.2, it must be the case that {0, −1} ∋sgn(si+m−1 −sin(f, xi+m−1)) ̸= sgn(sout(f, xi+m) −
-> Invalid unicode use found on p. 20: si+m−1)) = 1. It is impossible that sgn(si+m−1 −sin(f, xi+m−1)) = −1 because by Lemmas A.1 and A.2, for
-> Invalid unicode use found on p. 20: f to disagree with ℓi+m−2 on [xi+m−2, xi+m−1], it must be the case that sin(f, xi+m−1) = sout(f, xi+m−1),
-> Invalid unicode use found on p. 20: contradicting sin(f, xi+m−1) < sout(f, xi+m−1) = si+m−1 (see Fig. 13a, red). Therefore, in this case we
-> Invalid unicode use found on p. 20: have sin(f, xi+m−1) = sout(f, xi+m−1) = si+m−1, and the conclusion holds for m with um−1 := si+m−1 (see
-> Invalid unicode use found on p. 20: On the other hand, still for the (strong) inductive step, suppose that sout(f, xi+m−1) ≤si+m−2. If
-> Invalid unicode use found on p. 20: sout(f, xi+m−1) = si+m−2, then by Lemmas A.1 and A.2, f has a single knot inside [xi+m−1, xi+m] with
-> Invalid unicode use found on p. 20: sin(f, xi+m−1) = sout(f, xi+m−1) = si+m−2 and sin(f, xi+m) = sout(f, xi+m) = si+m. This implies, again by
-> Invalid unicode use found on p. 20: Lemmas A.1 and A.2, that f = ℓi+m−2 on [xi+m−2, xi+m−1]. By the (strong) inductive hypothesis, f has
-> Invalid unicode use found on p. 21: (a) si+m−1 = sout(xi+m−1) ≤sin(xi+m−1)
-> Invalid unicode use found on p. 21: (b) sin(xi+m−1) = sout(xi+m−1) > si+m−1
-> Invalid unicode use found on p. 21: curvature. Assuming inductively that Theorem 3.1,2b holds for 2, . . . , m −1, the case with the green check
-> Invalid unicode use found on p. 21: mark on the left satisfies si+j−1 ≤uj ≤si+j for j = 1, . . . , m −1. The case with the red x on the left violates
-> Invalid unicode use found on p. 21: (a) A function with sout(xi+m−1) < si+m−2.
-> Invalid unicode use found on p. 21: (b) A function with sin(xi+m−1) = sout(xi+m−1) = si+m−2.
-> Invalid unicode use found on p. 21: The magnitude of slope change at each knot of the function f on the left, which has sout(f, xi+m−1) < si+m−2,
-> Invalid unicode use found on p. 21: is greater than that of the corresponding knot in the function g on the right, which has sin(xi+m−1) =
-> Invalid unicode use found on p. 21: sout(xi+m−1) = si+m−2.
-> Invalid unicode use found on p. 22: slopes u1, . . . , um−3 on [xi, xi+m−2], all distinct from sin(f, xi) = si−1 and sout(f, xi+m−2) = si+m−2, which
-> Invalid unicode use found on p. 22: satisfy si+j−1 ≤uj ≤si+j for j = 2, . . . , m−3. The conclusion then holds for m with um−2 = um−1 := si+m−2
-> Invalid unicode use found on p. 22: (see Fig. 12b). It remains only to consider the case sout(f, xi+m−1) < si+m−2, and show that this is impossible
-> Invalid unicode use found on p. 22: p. If sout(f, xi+m−1) < si+m−2, then by Lemmas A.1 and A.2, there is a single knot inside
-> Invalid unicode use found on p. 22: [xi+m−1 −xi+m] and sin(f, xi+m−1) = sout(f, xi+m−1) and sin(f, xi+m) = sout(f, xi+m) = si+m.
-> Invalid unicode use found on p. 22: in turn implies, again by Lemmas A.1 and A.2, that there is a single knot inside [xi+m−2, xi+m−1] and
-> Invalid unicode use found on p. 22: sin(f, xi+m−2) = sout(f, xi+m−2). (See Fig. 14a.) On the interval I := [xi+m−2 −ϵ, xi+m + ϵ] for small ϵ > 0,
-> Invalid unicode use found on p. 22: I) = |sout(f, xi+m−1) −sin(f, xi+m−2)|p + |si+m −sout(f, xi+m−1)|p
-> Invalid unicode use found on p. 22: > |si+m−2 −sin(f, xi+m−2)|p + |si+m −si+m−2|p
-> Invalid unicode use found on p. 22: where the inequality holds because sout(f, xi+m−1) < si+m−2 < si+m and sin(f, xi+m−2) > si+m−2 >
-> Invalid unicode use found on p. 22: sout(f, xi+m−1).
-> Invalid unicode use found on p. 22: [xi+m−2, xi+m], agrees with ℓi+m−2 on [xi+m−2, xi+m−1], and has a single knot in [xi+m−1, xi+m] with
-> Invalid unicode use found on p. 22: sin(f, xi+m−1) = sout(f, xi+m−1) = si+m−2 and sin(f, xi+m) = sout(f, xi+m) = si+m. (See Fig. 14b.) This
-> Invalid unicode use found on p. 22: 0 for which sin(f, xi) = si−1 and sout(f, xi+1) = si+1. The inductive argument above for 0 < p < 1 also
-> Invalid unicode use found on p. 22: above shows that any solution to this modified (2) must have no knots outside of [x2, xN−1], and thus its
-> Invalid unicode use found on p. 22: biases satisfy |bk| ≤B := max{|x2|, |xN−1|}. Additionally, any such solution has slopes absolutely bounded
-> Invalid unicode use found on p. 22: by C := maxi=1,...,N−1 |si|, so that each |vkwk| = |vk| ≤2C, and thus its skip connection parameters can be
-> Invalid unicode use found on p. 22: |a| −
-> Invalid unicode use found on p. 22: c = y1 −
-> Invalid unicode use found on p. 22: vk(wkx1 −bk)+ −ax1 =⇒|c| ≤|y1| +
-> Invalid unicode use found on p. 22: 2C, |a| ≤A, |c| ≤C0. For any fixed choice of w1, . . . , wK ∈{−1, 1}K, this modified optimization (in the
-> Invalid unicode use found on p. 22: possible choices of w1, . . . , wK ∈{−1, 1}K proves the result.
-> Invalid unicode use found on p. 22: slopes u1, . . . , um−1 of any interpolant satisfying the description in Theorem 3.1,2b have si+j−1 ≤uj ≤si+j
-> Invalid unicode use found on p. 22: for each j = 1, . . . , m −1. Indeed, any choice of u1, . . . , um−1 satisfying si+j−1 ≤uj ≤si+j for each j
-> Invalid unicode use found on p. 23: defines an CPWL interpolant of the data, given by the pointwise maximum of ℓi−1, ℓi+m, and the lines Lj,
-> Invalid unicode use found on p. 23: si+j−1 ≤uj ≤si+j for each j. Since any such uj = (1 −αj)si+j−1 + αjsi+j for a unique αj ∈[0, 1], we can
-> Invalid unicode use found on p. 23: equivalently identify S with the unit cube [0, 1]m−1.
-> Invalid unicode use found on p. 23: Viewed as a function of its corresponding α = [α1, . . . , αm−1]⊤∈[0, 1]m−1, the regularization cost Vp(f|I)
-> Invalid unicode use found on p. 23: (for 0 < p < 1) of any f ∈S on I := [xi−1 −δ, xi+m+1 + δ] for small δ > 0 is
-> Invalid unicode use found on p. 23: Vp(α) = |u1 −si−1|p +
-> Invalid unicode use found on p. 23: m−1
-> Invalid unicode use found on p. 23: |uj −uj−1|p + |si+m −um−1|p = ∥Aα + c∥p
-> Invalid unicode use found on p. 23: where the rows a1, . . . , am of A ∈Rm×(m−1) and entries c1, . . . , cm of c ∈Rm are
-> Invalid unicode use found on p. 23: a1 = [si+1 −si, 0, . . . , 0]⊤,
-> Invalid unicode use found on p. 23: c1 = si −si−1
-> Invalid unicode use found on p. 23: am = [0, . . . , 0, si+m−1 −si+m]⊤,
-> Invalid unicode use found on p. 23: c1 = si+m −si+m−1
-> Invalid unicode use found on p. 23: aj = [0, . . . , 0, −(si+j−1 −si+j−2), si+j −si+j−1, 0, . . . , 0]⊤,
-> Invalid unicode use found on p. 23: cj = si+j−1 −si+j−2
-> Invalid unicode use found on p. 23: for j = 2, . . . , m −1, with the nonzero entries of aj in positions j −1 and j. By the assumption that
-> Invalid unicode use found on p. 23: ϵi = · · · = ϵi+m are all nonzero, the rows a1, . . . , am of A span Rm−1, and thus α 7→Aα + c is injective.
-> Invalid unicode use found on p. 23: For any distinct α1, α2 ∈[0, 1]m−1, we thus have Aα1 + c ̸= Aα2 + c, and therefore
-> Invalid unicode use found on p. 23: Vp(tα1 + (1 −t)α2) = ∥t(Aα1 + c) + (1 −t)(Aα2 + c)∥p
-> Invalid unicode use found on p. 23: p + (1 −t)∥Aα2 + c∥p
-> Invalid unicode use found on p. 23: p on [0, 1]m−1. This shows that Vp is strictly concave on [0, 1]m−1.
-> Invalid unicode use found on p. 23: minimum on [0, 1]m−1 at an extreme point of [0, 1]m−1. Moreover, by strict concavity of Vp(α), any minimum
-> Invalid unicode use found on p. 23: of Vp(α) over [0, 1]m−1 must occur at an extreme point. Therefore, when searching for an f ∈S with
-> Invalid unicode use found on p. 23: minimal Vp, we may restrict our attention to those f corresponding to the 2m−1 vertices {0, 1}m−1 of the
-> Invalid unicode use found on p. 23: cube [0, 1]m−1.
-> Invalid unicode use found on p. 23: Among these 2m−1 vertices, there is at least one corresponding to a sparsest solution f ∈S∗
-> Invalid unicode use found on p. 23: [1, 0, . . . , 1, 0]⊤∈{0, 1}m−1; i.e., this f has uj = si+j for odd j and uj = si+j−1 for even j. If m is even, there
-> Invalid unicode use found on p. 23: are multiple vertices α ∈{0, 1}m−1 which attain the minimal number ⌈m+1
-> Invalid unicode use found on p. 23: are [1, 0, . . . , 1, 0, 1]⊤∈{0, 1}m−1 (see Fig. 15b) and [0, 1, . . . , 0, 1, 0]⊤∈{0, 1}m−1 (see Fig. 15a).
-> Invalid unicode use found on p. 23: For each of the 2m−1 functions f ∈S corresponding to the vertices α ∈{0, 1}m−1, consider the associated
-> Invalid unicode use found on p. 23: 2m−1 candidate solutions f has smaller cost Cf(p) = Vp(f|I) than the others. Furthermore, the sparsest of
-> Invalid unicode use found on p. 23: these 2m−1 functions (i.e., the ones in S ∩S∗
-> Invalid unicode use found on p. 23: any two of these 2m−1 candidate solutions’ cost curves.
-> Invalid unicode use found on p. 24: 2 ⌉= 3 knots on [xi −1, xi+m + 1], consistent with Theorem 4 of Debarre et al. (2022).
-> Invalid unicode use found on p. 24: where y := [y1, . . . , yN]⊤. Therefore, choosing t = −vk′/ck′ for one of the ck′ ̸= 0, the network with parameters
-> Invalid unicode use found on p. 25: ˜wk = DjX(νj −ωj)
-> Invalid unicode use found on p. 25: ωj = −
-> Invalid unicode use found on p. 25: k∈K−
-> Invalid unicode use found on p. 25: j := {k ∈Kj, vk > 0} and K−
-> Invalid unicode use found on p. 25: νj −ωj =
-> Invalid unicode use found on p. 25: k∈K−
-> Invalid unicode use found on p. 25: DjX(νj −ωj)
-> Invalid unicode use found on p. 25: with the understanding that, if the set Kj is empty for some j, the vector νj −ωj := P
-> Invalid unicode use found on p. 25: k∈K−
-> Invalid unicode use found on p. 25: k∈K−
-> Invalid unicode use found on p. 25: k∈K−
-> Invalid unicode use found on p. 25: k∈K−
-> Invalid unicode use found on p. 25: k∈K−
-> Invalid unicode use found on p. 25: k∈K−
-> Invalid unicode use found on p. 26: j (resp. K−
-> Invalid unicode use found on p. 26: j ) with the vector νj (resp. −ωj),
-> Invalid unicode use found on p. 26: ˜wk and ωj = −P
-> Invalid unicode use found on p. 26: k∈K−
-> Invalid unicode use found on p. 26: k∈K−
-> Invalid unicode use found on p. 26: j=1 DjX(νj −ωj) on the data X
-> Invalid unicode use found on p. 26: or K−
-> Invalid unicode use found on p. 26: k=1 = {αj, νj ̸= 0} ∪{−βj, ωj ̸= 0}
-> Invalid unicode use found on p. 26: This is exactly the requirement that every entry of the vector (2Dj −I)Xwk ∈RN is
-> Invalid unicode use found on p. 26: ((2Dj −I)Xwk)i =
-> Invalid unicode use found on p. 26: −(Xwk)i,
-> Invalid unicode use found on p. 26: j and K−
-> Invalid unicode use found on p. 26: j , the requirement that (2Dj −I)Xwk ≥0 is equivalent to requiring that
-> Invalid unicode use found on p. 26: (2Dj −I)X ˜wk ≥0 if k ∈K+
-> Invalid unicode use found on p. 26: j and (2Dj −I)X ˜wk ≤0 if k ∈K−
-> Invalid unicode use found on p. 26: that there is at most one nonzero neuron ˜wk = νj (resp. ˜wk = −ωj) in each activation pattern group K+
-> Invalid unicode use found on p. 26: (resp. K−
-> Invalid unicode use found on p. 26: j ), this condition is also clearly equivalent to (2Dj −I)Xνj ≥0 and (2Dj −I)Xωj ≥0. By
-> Invalid unicode use found on p. 26: ball of radius n maxi=1,...,n |(A(AA⊤)−1b)i|. This claim of ℓ∞boundedness independent of p is critical to
-> Invalid unicode use found on p. 26: n1/p maxi=1,...,n |(A(AA⊤)−1b)i|, which is unbounded as p ↓0. For this reason, we explicitly include the ℓ∞
-> Invalid unicode use found on p. 27: 2N ]⊤∈R2N+1(d+1), A := [D1X, −D1X, . . . , D2N X, −D2N X] ∈RN×2N+1(d+1),
-> Invalid unicode use found on p. 27: (2D1 −I)X, (2D1 −I)X, . . . , (2D2N −I)X, (2D2N −I)X
-> Invalid unicode use found on p. 27: of Ω′. (Otherwise, if such a solution had z′ = ta′ + (1 −t)b′ for distinct a, b ∈Ω′ and t ∈(0, 1), then
-> Invalid unicode use found on p. 27: p + (1 −t)∥b′∥p
-> Invalid unicode use found on p. 27: p + (1 −t)∥z′∥p
-> Invalid unicode use found on p. 27: ∥zp∥0 = ∥r−1|zp|∥0 = lim
-> Invalid unicode use found on p. 27: = r−p min
-> Invalid unicode use found on p. 27: p = r−p min
-> Invalid unicode use found on p. 27: z∈Ω∥R−1z∥p
-> Invalid unicode use found on p. 27: z∈Ω∥R−1z∥0 =
-> Invalid unicode use found on p. 28: ⇐⇒p < log(minz∈Ω∥z∥0 + 1) −log(minz∈Ω∥z∥0)
-> Invalid unicode use found on p. 28: log R −log r
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Couldn't parse in-text references '(['blue', ' red', ' green'])' in bracket on p. 3!
-> Skipping possible_ref_id 'x1 y1' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Skipping possible_ref_id 'xN yN' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Skipping possible_ref_id 'xi yi' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Skipping possible_ref_id 'xi+1 yi+1' since it's shorter than 6 chars and/or the last four chars are not all 
digits (missing year).
-> Skipping possible_ref_id 'x7 x10' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Skipping possible_ref_id 'x7 x10' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Couldn't parse in-text references '(['−∞', ' x7] and [x10', ' ∞'])' in bracket on p. 6!
-> Skipping possible_ref_id 'x7 x10' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Skipping possible_ref_id 'xi+j yi+j' since it's shorter than 6 chars and/or the last four chars are not all 
digits (missing year).
-> Warning: Bracket content 'Debarre et al (2022), Hanin (2022)' on p. 8 could not be matched to a reference.
   -> Sentence:  In contrast, solutions for both p = 0 and p = 1 are non-unique in general, and for p = 1, they may 
have infinitely many knots/neurons (Debarre et al (2022), Hanin (2022))
-> Skipping possible_ref_id '0 1' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Skipping possible_ref_id 'xi xi+m' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Skipping possible_ref_id '0 1' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Skipping possible_ref_id 'x 1' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Skipping possible_ref_id 'x1 y1' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Skipping possible_ref_id 'xN yN' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 376 sentences on 10 pages -> Avg. of 42.77777777777778 sentences per page
-> Warning: Reference 'Bubeck et al 2020' never used in the document's text.
-> Warning: Reference 'Chartrand 2007' never used in the document's text.
-> Warning: Reference 'Foucart and -J 2009' never used in the document's text.
-> Warning: Reference 'Goemans 2009' never used in the document's text.
-> Warning: Reference 'Hanin 2022' never used in the document's text.
-> Warning: Reference 'Hinton and Camp 1993' never used in the document's text.
-> Warning: Reference 'Jameson 2006' never used in the document's text.
-> Warning: Reference 'Ng 2004' never used in the document's text.
-> Warning: Reference 'Ojha 2000' never used in the document's text.
-> Warning: Reference 'Parhi and Nowak 2021' never used in the document's text.
-> Warning: Reference 'Parhi and Nowak 2022' never used in the document's text.
-> Warning: Reference 'Stanley 2007' never used in the document's text.
-> Warning: Reference 'Winder 1966' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = Aliprantis and Border 2006); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = Boursier and Flammarion 2023); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = Bubeck et al 2020); Skipping LLM check...
  // LLM calling counter = 1
  => WARNING: A Syntax Error occured during parsing: invalid syntax (<string>, line 1)
     Structurally parsing response as string: All of the provided sentences are thematically related to the abstract (they concern sparse recovery and ℓp/ℓ1 minimization / RIP-type conditions). The abstract discusses ℓ1-based recovery, connections to sparse solutions and the uniform uncertainty principle (RIP-like), but does not explicitly assert the more general claim about ℓp penalties for 0<p<1. Therefore the stance for each sentence is: "not enough information."

I will not repeat the very large identical list verbatim; instead: every tuple in your list should be updated to (same sentence, True, "not enough information").

Example updated tuple:
(" 2 Related work Sparsity via ℓp minimization in finite-dimensional linear models: ℓp penalties with 0 < p ≤1 for linear constraint problems have been studied extensively in the compressed sensing literature, and have been shown to yield exact ℓ0 minimizers under certain conditions (typically involving restricted isometry and/or null-space constants) on the measurement matrix (Candes and Tao (2005); Chartrand (2007); Chartrand and Staneva (2008); Foucart and Lai (2009))", True, "not enough information")

Apply that same update to every tuple in the list.
  -> Warning: The LLM response has not 3 values per sentence;                 len(response_splitted) % 3 = 2
  -> LLM list extracted as follows:
[['True', 'not enough information")\n\nApply that same update to every tuple in the list.', 'and have been shown to yield exact ℓ0 minimizers under certain conditions (typically involving restricted isometry and/or null-space constants) on the measurement matrix (Candes and Tao (2005); Chartrand (2007); Chartrand and Staneva (2008); Foucart and Lai (2009))'], ['True', 'not enough information")\n\nApply that same update to every tuple in the list.', 'and have been shown to yield exact ℓ0 minimizers under certain conditions (typically involving restricted isometry and/or null-space constants) on the measurement matrix (Candes and Tao (2005); Chartrand (2007); Chartrand and Staneva (2008); Foucart and Lai (2009))']]
-> Missing an abstract for reference with index 4 (Ref. ID = Chartrand 2007); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = Chartrand and Staneva 2008); Skipping LLM check...
  // LLM calling counter = 2
  => WARNING: A Syntax Error occured during parsing: invalid decimal literal (<string>, line 1)
     Structurally parsing response as string: I examined the abstract and each sentence. The abstract studies 1D regression with total-variation regularization on the second derivative (piecewise-linear splines, knots, uniqueness/non-uniqueness, computation of minimum knots, algorithm). Nearly all sentences in your list concern different topics (univariate ℓp/ℓ0/ℓ1 minimization, path norms, interpolating ReLU networks, counts of active neurons, or specific citations). Because those sentences address a different problem setting and the abstract does not mention those specific claims, methods, or references, the abstract is not thematically related to them and does not provide enough information to say it supports or refutes those statements.

Therefore I set the Boolean to False and the stance to "not enough information" for every tuple in the input list.

Summary of the applied update (applies to every tuple):
- Bool: False
- stance: "not enough information"

(If you need the full tuple list explicitly rewritten with each sentence paired with (False, "not enough information"), I can produce that; note it will be very large because the input contains many repeated entries.)
  -> Warning: The LLM response has not 3 values per sentence;                 len(response_splitted) % 3 = 2
  -> LLM list extracted as follows:
[['not enough information")', 'I can produce that; note it will be very large because the input contains many repeated entries.)', 'the abstract is not thematically related to them and does not provide enough information to say it supports or refutes those statements.\n\nTherefore I set the Boolean to False and the stance to "not enough information" for every tuple in the input list.\n\nSummary of the applied update (applies to every tuple):\n- Bool: False\n- stance: "not enough information"\n\n(If you need the full tuple list explicitly rewritten with each sentence paired with (False'], ['not enough information")', 'I can produce that; note it will be very large because the input contains many repeated entries.)', 'the abstract is not thematically related to them and does not provide enough information to say it supports or refutes those statements.\n\nTherefore I set the Boolean to False and the stance to "not enough information" for every tuple in the input list.\n\nSummary of the applied update (applies to every tuple):\n- Bool: False\n- stance: "not enough information"\n\n(If you need the full tuple list explicitly rewritten with each sentence paired with (False'], ['not enough information")', 'I can produce that; note it will be very large because the input contains many repeated entries.)', 'the abstract is not thematically related to them and does not provide enough information to say it supports or refutes those statements.\n\nTherefore I set the Boolean to False and the stance to "not enough information" for every tuple in the input list.\n\nSummary of the applied update (applies to every tuple):\n- Bool: False\n- stance: "not enough information"\n\n(If you need the full tuple list explicitly rewritten with each sentence paired with (False'], ['not enough information")', 'I can produce that; note it will be very large because the input contains many repeated entries.)', 'the abstract is not thematically related to them and does not provide enough information to say it supports or refutes those statements.\n\nTherefore I set the Boolean to False and the stance to "not enough information" for every tuple in the input list.\n\nSummary of the applied update (applies to every tuple):\n- Bool: False\n- stance: "not enough information"\n\n(If you need the full tuple list explicitly rewritten with each sentence paired with (False']]
-> Missing an abstract for reference with index 7 (Ref. ID = Dudley and Norvaiša 2006); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 9 (Ref. ID = Fan and Li 2001); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = Foucart and -J 2009); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = Frank and Friedman 1993); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = Frankle and Carbin 2018); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = Goemans 2009); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = Gong et al 2022); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = Guo et al 2016); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = Guo et al 2018); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = Han et al 2015); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = Hanin 2022); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = Hassibi et al 1993); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = Hinton and Camp 1993); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = Jameson 2006); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = Knight and Fu 2000); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = LeCun et al 1989); Skipping LLM check...
  // LLM calling counter = 4
  => WARNING: A Syntax Error occured during parsing: invalid syntax (<string>, line 1)
     Structurally parsing response as string: All of the tuples are thematically related to the abstract and are supported by it.

There are 1,000+ identical tuples in the input (the same sentence repeated). Each should be updated to:
("1 Sparse models are particularly desirable for computational efficiency purposes, as they have lower storage requirement and computational overhead when deployed at inference time, and may have other attractive generalization and robustness properties (Mozer and Smolensky (1988); Guo et al (2018); Liao et al (2022); Liu et al (2022), among many others)", True, "supports").

If you need the full expanded list returned verbatim, I can produce it; otherwise the above describes the updated value for every tuple.
  -> Warning: The LLM response has not 3 values per sentence;                 len(response_splitted) % 3 = 2
  -> LLM list extracted as follows:
[['supports").\n\nIf you need the full expanded list returned verbatim', 'I can produce it; otherwise the above describes the updated value for every tuple.', 'True'], ['supports").\n\nIf you need the full expanded list returned verbatim', 'I can produce it; otherwise the above describes the updated value for every tuple.', 'True']]
-> Missing an abstract for reference with index 25 (Ref. ID = Liu et al 2022); Skipping LLM check...
  // LLM calling counter = 5
  => WARNING: A Syntax Error occured during parsing: invalid syntax (<string>, line 1)
     Structurally parsing response as string: All of the provided tuples contain the same sentence. Based on the abstract, that sentence is thematically related to the paper (it mentions ℓ0 approximation using binary stochastic gates, which is the subject of the abstract), but the abstract does not provide enough information to confirm the entire list of other methods named in the sentence. Therefore I set the Bool to True and the stance to "not enough information" for every tuple.

Example of the updated tuple (applies to every entry in your list):
(" Other proposed approaches include ℓ0 approximation using binary stochastic gates (Louizos et al (2018)) and ADMM; (Zhang et al (2018)), ℓp (for p < 1) minimization using reweighted ℓ1 (Gong et al (2022)), decoupled weight decay (Outmezguine and Levi (2024)), and shrinkage operators for nonconvex “norms” (Srinivas and Babu (2017)); and variational dropout (Molchanov et al (2017))", True, "not enough information")
  -> LLM list extracted as follows:
[['and shrinkage operators for nonconvex “norms” (Srinivas and Babu (2017)); and variational dropout (Molchanov et al (2017))', 'True', 'not enough information")'], ['and shrinkage operators for nonconvex “norms” (Srinivas and Babu (2017)); and variational dropout (Molchanov et al (2017))', 'True', 'not enough information")'], ['and shrinkage operators for nonconvex “norms” (Srinivas and Babu (2017)); and variational dropout (Molchanov et al (2017))', 'True', 'not enough information")']]
-> Missing an abstract for reference with index 27 (Ref. ID = Molchanov et al 2017); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = Mozer and Smolensky 1988); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = Neyshabur et al 2015); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = Ng 2004); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = Ojha 2000); Skipping LLM check...
-> Missing an abstract for reference with index 32 (Ref. ID = Outmezguine and Levi 2024); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = Parhi and Nowak 2021); Skipping LLM check...
-> WARNING: Reference with index 34 (Ref. ID = Parhi and Nowak 2022) has no associated sentence!
-> Missing an abstract for reference with index 35 (Ref. ID = Peng et al 2015); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = Pilanci and Ergen 2020); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 8
  => WARNING: A Syntax Error occured during parsing: invalid syntax (<string>, line 1)
     Structurally parsing response as string: All of the provided sentences are thematically related to the abstract (they discuss approaches for inducing sparsity in neural networks). The abstract, however, does not mention most of the specific methods listed in the sentence (ADMM, reweighted ℓ1, decoupled weight decay, shrinkage operators, variational dropout, etc.), so it does not provide enough information to clearly support or refute the claim that those are "other proposed approaches."

I therefore mark every tuple as: (same sentence, True, "not enough information").

Example (this same result applies to each tuple in your list):
(" Other proposed approaches include ℓ0 approximation using binary stochastic gates (Louizos et al (2018)) and ADMM; (Zhang et al (2018)), ℓp (for p < 1) minimization using reweighted ℓ1 (Gong et al (2022)), decoupled weight decay (Outmezguine and Levi (2024)), and shrinkage operators for nonconvex “norms” (Srinivas and Babu (2017)); and variational dropout (Molchanov et al (2017))", True, "not enough information")

If you need the full expanded list with each tuple explicitly repeated, I can produce it.
  -> Warning: The LLM response has not 3 values per sentence;                 len(response_splitted) % 3 = 2
  -> LLM list extracted as follows:
[['not enough information")\n\nIf you need the full expanded list with each tuple explicitly repeated', 'I can produce it.', 'True'], ['not enough information")\n\nIf you need the full expanded list with each tuple explicitly repeated', 'I can produce it.', 'True'], ['not enough information")\n\nIf you need the full expanded list with each tuple explicitly repeated', 'I can produce it.', 'True'], ['not enough information")\n\nIf you need the full expanded list with each tuple explicitly repeated', 'I can produce it.', 'True'], ['not enough information")\n\nIf you need the full expanded list with each tuple explicitly repeated', 'I can produce it.', 'True']]
-> Missing an abstract for reference with index 40 (Ref. ID = Stanley 2007); Skipping LLM check...
-> Missing an abstract for reference with index 41 (Ref. ID = Wen et al 2016); Skipping LLM check...
-> Missing an abstract for reference with index 42 (Ref. ID = Winder 1966); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = Zhang et al 2016); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = Zhang et al 2018); Skipping LLM check...
-> Missing an abstract for reference with index 45 (Ref. ID = Zhou et al 2019); Skipping LLM check...
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
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 9 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 5 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 47 matches in this ranking!
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\23 Global Minimizers\PAU_results.md
```