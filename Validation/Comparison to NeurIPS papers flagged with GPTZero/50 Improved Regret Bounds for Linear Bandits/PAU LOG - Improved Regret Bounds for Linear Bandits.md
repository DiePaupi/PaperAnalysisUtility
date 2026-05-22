
NOTE:
- `[Lugosi and Mendelson (2019a); Catoni (2012)]`
- `[Chowdhury and Gopalan (2019)]`
- `Camilleri et al. (2021)`

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\50 Improved Regret Bounds for Linear Bandits\Improved Regret Bounds for Linear Bandits with Heavy-Tailed Rewards.pdf"
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
- Found following heading '2 - Lower Bounds' on page 4
- Found following heading '3 - Proposed Algorithm and Upper Bounds' on page 8
- Found following heading '4 - Conclusion' on page 12
=> Found references/literature section on page 12
- Found first appendix 'A - Upper Bound Proofs' on page 16
- Found following appendix 'B - Unit Ball Lower Bound' on page 18
- Found following appendix 'C - Extension to Kernel Bandits' on page 20
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 12 -- 16
All found references: 35
Backend tkagg is interactive backend. Turning interactive mode on.
 -> Found dublicated ref_ids:
                                       full_reference                     ref_id                                   authors  ...                                             outlet  link valid
21  Lugosi, G. and Mendelson, S. (2019b). Sub-Gaus...  Lugosi and Mendelson 2019              Lugosi, G. and Mendelson, S.  ...                           The Annals of Statistics        None
29  Vakili, S., Khezeli, K., and Picheny, V. (2021...          Vakili et al 2021  Vakili, S., Khezeli, K., and Picheny, V.  ...  International Conference on Artificial Intelli...        None

[2 rows x 11 columns]
-----------
 -> Parsed references DataFrame:
                           ref_id                                            authors  ... link  valid
0        Audibert and Catoni 2011                     Audibert, J.-Y. and Catoni, O.  ...        None
1             Baccelli et al 2002         Baccelli, F., Taché, G. H., and Altman, E.  ...        None
2            Brownlees et al 2015            Brownlees, C., Joly, E., and Lugosi, G.  ...        None
3            Camilleri et al 2021  Camilleri, R., Jamieson, K., and Katz-Samuels, J.  ...        None
4                     Catoni 2012                                         Catoni, O.  ...        None
5                 Chen et al 2025        Chen, Y., Huang, J., Dai, Y., and Huang, L.  ...        None
6                 Choi et al 2020        Choi, Y., van der Laan, E., and Ghattas, O.  ...        None
7      Chowdhury and Gopalan 2019                   Chowdhury, S. R. and Gopalan, A.  ...        None
8                       Cont 2001                                           Cont, R.  ...        None
9          Cont and Bouchaud 2000                          Cont, R. and Bouchaud, J.  ...        None
10             Devroye et al 2016  Devroye, L., Lerasle, M., Lugosi, G., and Oliv...  ...        None
11           Han and Wellner 2019                         Han, Q. and Wellner, J. A.  ...        None
12            Hsu and Sabato 2014                             Hsu, D. and Sabato, S.  ...        None
13               Huang et al 2022                  Huang, J., Dai, Y., and Huang, L.  ...        None
14               Huang et al 2023       Huang, J., Zhong, H., Wang, L., and Yang, L.  ...        None
15      Jebarajakirthy et al 2021     Jebarajakirthy, S., Shukla, P., and Palvia, P.  ...        None
16              Kang and Kim 2023                            Kang, M. and Kim, G.-S.  ...        None
17  Lattimore and Szepesvári 2020                   Lattimore, T. and Szepesvári, C.  ...        None
18                Li and Sun 2024                                 Li, X. and Sun, Q.  ...        None
19                  Lu et al 2019            Lu, S., Wang, G., Hu, Y., and Zhang, L.  ...        None
20     Lugosi and Mendelson 2019a                       Lugosi, G. and Mendelson, S.  ...        None
21     Lugosi and Mendelson 2019b                       Lugosi, G. and Mendelson, S.  ...        None
22           Medina and Yang 2016                         Medina, A. M. and Yang, S.  ...        None
23             Roberts et al 2015  Roberts, J. A., Varnai, L. A. E., Houghton, B....  ...        None
24                     Sason 2015                                          Sason, I.  ...        None
25            Scarlett et al 2017        Scarlett, J., Bogunovic, I., and Cevher, V.  ...        None
26                Shao et al 2018         Shao, H., Yu, X., King, I., and Lyu, M. R.  ...        None
27                 Sun et al 2020                  Sun, Q., Zhou, W.-X., and Fan, J.  ...        None
28             Vakili et al 2021a  Vakili, S., Bouziani, N., Jalali, S., Bernacch...  ...        None
29             Vakili et al 2021b           Vakili, S., Khezeli, K., and Picheny, V.  ...        None
30                Wang et al 2025        Wang, J., Zhang, Y., Zhao, P., and Zhou, Z.  ...        None
31        Wei and Srivastava 2021                         Wei, L. and Srivastava, V.  ...        None
32                 Xue et al 2020         Xue, B., Wang, G., Wang, Y., and Zhang, L.  ...        None
33                 Xue et al 2023  Xue, B., Wang, Y., Wan, Y., Yi, J., and Zhang, L.  ...        None
34                  Yu et al 2018    Yu, X., Nevmyvaka, Y., King, I., and Lyu, M. R.  ...        None

[35 rows x 10 columns]
- Checking reference 1/35:
  -> INFO: Now checking 10 results for matching title: 'Robust linear least squares regression'
       -> INFO: All authors matched!
       -> WARNING: Year (2010) does not match expected year (2011)!
       -> INFO: All authors matched!
       -> WARNING: Year (2010) does not match expected year (2011)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/35:
  -> INFO: Now checking 2 results for matching title: 'Flow complexity and heavy-tailed delays in packet networks'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Baccelli', 'Taché', 'Altman', '2002']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Flow+complexity+and+heavy-tailed+delays+in+packet+networks manually and check the results.
        -> Author(s): Baccelli, F., Taché, G. H., and Altman, E.
        -> Title:     Flow complexity and heavy-tailed delays in packet networks
        -> Year:      2002
     -> Manual search was skipped by the user.
- Checking reference 3/35:
  -> INFO: Now checking 10 results for matching title: 'Empirical risk minimization for heavy-tailed losses'
       -> INFO: All authors matched!
       -> WARNING: Year (2014) does not match expected year (2015)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/35:
  -> INFO: Now checking 10 results for matching title: 'High-dimensional experimental design and kernel bandits'
       -> INFO: All authors matched!
- Checking reference 5/35:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Challenging the Empirical Mean and Empirical Variance: A Deviation Study, volume 1906 of Lecture Notes in Mathematics
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Catoni', '2012']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Challenging+the+Empirical+Mean+and+Empirical+Variance:+A+Deviation+Study%2C+volume+1906+of+Lecture+Notes+in+Mathematics manually and check the results.
        -> Author(s): Catoni, O.
        -> Title:     Challenging the Empirical Mean and Empirical Variance: A Deviation Study, volume 1906 of Lecture Notes in Mathematics
        -> Year:      2012
     -> Manual search was skipped by the user.
- Checking reference 6/35:
  -> INFO: Now checking 1 results for matching title: 'uniINF: Best-of-both-worlds algorithm for parameter-free heavy-tailed MABs'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/35:
  -> INFO: Now checking 4 results for matching title: 'Modeling heavy-tailed conversion values in real-time bidding'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Choi', 'van', 'Ghattas', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Modeling+heavy-tailed+conversion+values+in+real-time+bidding manually and check the results.
        -> Author(s): Choi, Y., van der Laan, E., and Ghattas, O.
        -> Title:     Modeling heavy-tailed conversion values in real-time bidding
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 8/35:
  -> INFO: Now checking 10 results for matching title: 'Bayesian optimization under heavy-tailed payoffs'
       -> INFO: All authors matched!
- Checking reference 9/35:
  -> INFO: Now checking 5 results for matching title: 'Empirical properties of asset returns: Stylized facts and statistical issues'
       -> INFO: All authors matched!
- Checking reference 10/35:
  -> INFO: Now checking 8 results for matching title: 'Herd behavior and aggregate fluctuations in financial markets'
       -> INFO: All authors matched!
       -> WARNING: Year (1997) does not match expected year (2000)!
       -> INFO: All authors matched!
       -> WARNING: Year (1998) does not match expected year (2000)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/35:
  -> INFO: Now checking 10 results for matching title: 'Sub-Gaussian mean estimators'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/35:
  -> INFO: Now checking 10 results for matching title: 'Convergence rates of least squares regression estimators with heavy-tailed errors'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/35:
  -> INFO: Now checking 1 results for matching title: 'Heavy-tailed regression with a generalized median-of-means'
       -> INFO: All authors matched!
- Checking reference 14/35:
  -> INFO: Now checking 7 results for matching title: 'Adaptive best-of-both-worlds algorithm for heavy-tailed multi-armed bandits'
       -> INFO: All authors matched!
- Checking reference 15/35:
  -> INFO: Now checking 1 results for matching title: 'Tackling heavy-tailed rewards in reinforcement learning with function approximation: Minimax optimal and instance-dependent regret bounds'
       -> INFO: All authors matched!
- Checking reference 16/35:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Heavy-tailed distributions in online ad response: A marketing analytics perspective
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Jebarajakirthy', 'Shukla', 'Palvia', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Heavy-tailed+distributions+in+online+ad+response:+A+marketing+analytics+perspective manually and check the results.
        -> Author(s): Jebarajakirthy, S., Shukla, P., and Palvia, P.
        -> Title:     Heavy-tailed distributions in online ad response: A marketing analytics perspective
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 17/35:
  -> INFO: Now checking 10 results for matching title: 'Heavy-tailed linear bandit with Huber regression'
       -> INFO: All authors matched!
- Checking reference 18/35:
  -> INFO: Now checking 10 results for matching title: 'Bandit Algorithms'
       -> INFO: All authors matched!
- Checking reference 19/35:
  -> INFO: Now checking 3 results for matching title: 'Variance-aware decision making with linear function approximation under heavy-tailed rewards'
       -> INFO: All authors matched!
- Checking reference 20/35:
  -> INFO: Now checking 3 results for matching title: 'Optimal algorithms for Lipschitz bandits with heavy-tailed rewards'
       -> INFO: All authors matched!
- Checking reference 21/35:
  -> INFO: Now checking 8 results for matching title: 'Mean estimation and regression under heavy-tailed distributions: A survey'
       -> INFO: All authors matched!
- Checking reference 22/35:
  -> INFO: Now checking 1 results for matching title: 'Sub-Gaussian estimators of the mean of a random vector'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 23/35:
  -> INFO: Now checking 10 results for matching title: 'No-regret algorithms for heavy-tailed linear bandits'
       -> INFO: All authors matched!
- Checking reference 24/35:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Heavy-tailed distributions in the amplitude of neural oscillations
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Roberts', 'Varnai', 'Houghton', 'Hughes', '2015']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Heavy-tailed+distributions+in+the+amplitude+of+neural+oscillations manually and check the results.
        -> Author(s): Roberts, J. A., Varnai, L. A. E., Houghton, B. H., and Hughes, D.
        -> Title:     Heavy-tailed distributions in the amplitude of neural oscillations
        -> Year:      2015
     -> Manual search was skipped by the user.
- Checking reference 25/35:
  -> INFO: Now checking 1 results for matching title: 'An improved reverse pinsker inequality for probability distributions on a finite set'
       -> INFO: All authors matched!
- Checking reference 26/35:
  -> INFO: Now checking 4 results for matching title: 'Lower bounds on regret for noisy Gaussian process bandit optimization'
       -> INFO: All authors matched!
- Checking reference 27/35:
  -> INFO: Now checking 3 results for matching title: 'Almost optimal algorithms for linear stochastic bandits with heavy-tailed payoffs'
       -> INFO: All authors matched!
- Checking reference 28/35:
  -> INFO: Now checking 10 results for matching title: 'Adaptive Huber regression'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/35:
  -> INFO: Now checking 10 results for matching title: 'Optimal order simple regret for Gaussian process bandits'
       -> INFO: All authors matched!
- Checking reference 30/35:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 2 results for matching title: 'On information gain and regret bounds in Gaussian process bandits'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/35:
  -> INFO: Now checking 1 results for matching title: 'Heavy-tailed linear bandits: Huber regression with one-pass update'
       -> INFO: All authors matched!
- Checking reference 32/35:
  -> INFO: Now checking 10 results for matching title: 'Minimax policy for heavy-tailed bandits'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/35:
  -> INFO: Now checking 5 results for matching title: 'Nearly optimal regret for stochastic linear bandits with heavy-tailed payoffs'
       -> INFO: All authors matched!
- Checking reference 34/35:
  -> INFO: Now checking 1 results for matching title: 'Efficient algorithms for generalized linear bandits with heavy-tailed rewards'
       -> INFO: All authors matched!
- Checking reference 35/35:
  -> INFO: Now checking 1 results for matching title: 'Pure exploration of multi-armed bandits with heavy-tailed payoffs'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Shao'
  -> INFO: No perfect match found; taking the next best!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 1: ⟨x⋆, θ⋆⟩−⟨xt, θ⋆⟩
-> Invalid unicode use found on p. 2: 1−ϵ
-> Invalid unicode use found on p. 3: w.p. 1 −∆
-> Invalid unicode use found on p. 3: 12T −
-> Invalid unicode use found on p. 3: (1 + ϵ)-absolute moment of ∆−1(θ⊤x) ≥d for all actions. Recall that in our problem statement we
-> Invalid unicode use found on p. 3: 4 −3
-> Invalid unicode use found on p. 3: d−1∆
-> Invalid unicode use found on p. 4: Theorem 1. Fix the action set A = {x ∈[0, 1]2d : x2i−1 + x2i = 1
-> Invalid unicode use found on p. 4: w.p. 1 −γ
-> Invalid unicode use found on p. 4: θ ∈{∆, 2∆}2d : θ2i−1 + θ2i = 3∆
-> Invalid unicode use found on p. 4: are nonnegative) for each action is bounded by E[|y(x)|1+ϵ|x] = γ−(1+ϵ)/ϵγ1/ϵθ⊤x = γ−1θ⊤x ≤1,
-> Invalid unicode use found on p. 4: arg maxb∈{0,1}(θ2i−1+b) for θ ∈Θ, and write xt = (xt,1, . . . , xt,d). We have
-> Invalid unicode use found on p. 4: ∆−∆xt,2i−1+indi(θ)
-> Invalid unicode use found on p. 4: 2 −1
-> Invalid unicode use found on p. 4: 2(−1)indi(θ)(xt,2i−1 −xt,2i)
-> Invalid unicode use found on p. 4: I{(−1)indi(θ)(xt,2i−1 −xt,2i) ≤0}
-> Invalid unicode use found on p. 4: I{(−1)indi(θ)(xt,2i−1 −xt,2i) ≤0} ≥T
-> Invalid unicode use found on p. 4: where the second equality follows by using xt,2i−1 + xt,2i = 1 and checking the cases indi(θ) = 0 and
-> Invalid unicode use found on p. 4: 3∆−θj
-> Invalid unicode use found on p. 4: 2i −1 ≤j ≤2i
-> Invalid unicode use found on p. 4: t=1 I{(−1)indi(θ)(xt,2i−1 −xt,2i) ≤0} ≥T
-> Invalid unicode use found on p. 4: 2 exp(−KL(Pθ∥Pθ′))
-> Invalid unicode use found on p. 4: −Eθ
-> Invalid unicode use found on p. 5: ϵ−1
-> Invalid unicode use found on p. 5: −ϵ
-> Invalid unicode use found on p. 5: 1−ϵ
-> Invalid unicode use found on p. 5: = 4T −1,
-> Invalid unicode use found on p. 5: where in the first inequality we used KL(Ber(p)∥Ber(q)) ≤(p−q)2
-> Invalid unicode use found on p. 5: q(1−q); we get |p−q| ≤2γ
-> Invalid unicode use found on p. 5: construction, and 1 −q ≥1 −γ
-> Invalid unicode use found on p. 5: 2 exp(−4), and averaging over all
-> Invalid unicode use found on p. 5: 4d exp(−4). Hence, there
-> Invalid unicode use found on p. 5: 4d exp(−4), and substituting into our earlier lower bound on
-> Invalid unicode use found on p. 5: 16 exp(−4)∆dT = 1
-> Invalid unicode use found on p. 5: 32 exp(−4)d
-> Invalid unicode use found on p. 5: with d′ = d −(d mod m) and pad the action vectors with zeros. Letting di := (i −1)m, we define
-> Invalid unicode use found on p. 6: w.p. 1 −γ
-> Invalid unicode use found on p. 6: ∆−∆I{indi(θ) = indi(xt)}
-> Invalid unicode use found on p. 6: T −Eθ
-> Invalid unicode use found on p. 6: 1 −Pθ[xtU,di+indi(θ) = 1]
-> Invalid unicode use found on p. 6: Similarly to the proof of Theorem 1, applying KL(Ber(p)∥Ber(q)) ≤(p−q)2
-> Invalid unicode use found on p. 6: q(1−q) along with ∆d/m ≤
-> Invalid unicode use found on p. 6: θ⊤x ≤2∆d/m and |(θ(0) −θ(b))⊤x| ≤∆gives
-> Invalid unicode use found on p. 6: ϵ (θ(0) −θ(b))⊤xt)2
-> Invalid unicode use found on p. 6:  1−ϵ
-> Invalid unicode use found on p. 7:  ϵ−1
-> Invalid unicode use found on p. 7:  −ϵ
-> Invalid unicode use found on p. 7: ϵ−1
-> Invalid unicode use found on p. 7: 1+ϵ T −
-> Invalid unicode use found on p. 7: ϵ−1
-> Invalid unicode use found on p. 7: 1+ϵ d−1. Dividing both sides by m gives ∆
-> Invalid unicode use found on p. 7: 32d−
-> Invalid unicode use found on p. 7:  1−ϵ
-> Invalid unicode use found on p. 7:  1−ϵ
-> Invalid unicode use found on p. 7: 1 −Pθ[xt,di+indi(θ) = 1]
-> Invalid unicode use found on p. 7: 1 −1
-> Invalid unicode use found on p. 7: m −1
-> Invalid unicode use found on p. 7: 1 −Pθ∗[xt,di+indi(θ∗) = 1]
-> Invalid unicode use found on p. 7: m −1
-> Invalid unicode use found on p. 7: log(m −1) > m −1
-> Invalid unicode use found on p. 7: log m ≥m −1
-> Invalid unicode use found on p. 7: 1 −1
-> Invalid unicode use found on p. 8: h

                                       a⊤A(γ)(λ)−1x
-> Invalid unicode use found on p. 8: A(γ)(λ)−1
-> Invalid unicode use found on p. 8: εℓ←2−ℓ, τℓ←32
-> Invalid unicode use found on p. 8: −1+ϵ
-> Invalid unicode use found on p. 8: ℓ)−1xs ys}τℓ
-> Invalid unicode use found on p. 8: a∈Aℓ|θ⊤a −W (a)|
-> Invalid unicode use found on p. 8: ℓa′ −4εℓ
-> Invalid unicode use found on p. 8: we find an experimental design that minimizes the (1 + ϵ)-absolute moment of a⊤A(γ)(λ)−1x, with
-> Invalid unicode use found on p. 8: θ⊤a −bµ
-> Invalid unicode use found on p. 8: {a⊤A(γ)(λ)−1xi yi}n
-> Invalid unicode use found on p. 8: log(δ−1)
-> Invalid unicode use found on p. 9: ity at least 1 −δ:
-> Invalid unicode use found on p. 9: a∈A |⟨bθ −θ∗, a⟩| ≤
-> Invalid unicode use found on p. 9: 2γ1/2∥θ∗∥2β−1 + 32(1 + υ)
-> Invalid unicode use found on p. 9: 

                                      a⊤A(γ)(λ)−1x
-> Invalid unicode use found on p. 9: A(γ)(λ)−1.
-> Invalid unicode use found on p. 9: moment of our samples a⊤A(γ)(λ)−1x y for x ∼λ. Using the boundedness of the expected rewards
-> Invalid unicode use found on p. 9: ⟨θ∗, a⟩−E[W (a)]
-> Invalid unicode use found on p. 9: ≤√γβ−1∥θ∗∥2M1+ϵ(λ; A, γ, β)
-> Invalid unicode use found on p. 9: mean estimator (Lemma 1) and γ = T −2ϵ
-> Invalid unicode use found on p. 9: C0β−1b + C1(1 + υ)
-> Invalid unicode use found on p. 9: −2ϵ
-> Invalid unicode use found on p. 9: Proof Sketch. Using Lemma 1, with probability at least 1 −(2ℓ2T)−1, we have
-> Invalid unicode use found on p. 9: a∈Aℓ|a⊤θ∗−a⊤bθℓ| ≤ϵℓ+ 2γ1/2bβ−1M∗
-> Invalid unicode use found on p. 9: Therefore, in the phases where ϵℓis large compared to γ1/2β−1M∗
-> Invalid unicode use found on p. 9: O(γ1/2β−1M∗
-> Invalid unicode use found on p. 9: −2ϵ
-> Invalid unicode use found on p. 9: expected reward of each arm can be approximated by one of the covered elements with T −1 error, and
-> Invalid unicode use found on p. 9: C0β−1b + C′
-> Invalid unicode use found on p. 9: −2ϵ
-> Invalid unicode use found on p. 10: −2ϵ
-> Invalid unicode use found on p. 10: 1+ϵ(A, T −2ϵ
-> Invalid unicode use found on p. 10: −2ϵ
-> Invalid unicode use found on p. 10: h

                                        a⊤A(γ)(λ)−1x
-> Invalid unicode use found on p. 10: h

                                        a⊤A(γ)(λ)−1x
-> Invalid unicode use found on p. 10: a⊤A(γ)(λ)−1xx⊤A(γ)(λ)−1a
-> Invalid unicode use found on p. 10: A(γ)(λ)−1.
-> Invalid unicode use found on p. 10: Hence, the minimization of M1+ϵ is upper bounded in terms of a minimization of maxa ∥a∥A(λ)−1.
-> Invalid unicode use found on p. 10: maxa ∥a∥A(λ)−1 = O(
-> Invalid unicode use found on p. 10: Ex∼λ[|a⊤A−1x|1+ϵ] = Ex∼λ[|da⊤x|1+ϵ] = d1+ϵ
-> Invalid unicode use found on p. 10: d−1|a⊤ei|1+ϵ = dϵ
-> Invalid unicode use found on p. 10: −2ϵ
-> Invalid unicode use found on p. 10: ϵ−1
-> Invalid unicode use found on p. 10: Ex∼λ[|a⊤A−1x|1+ϵ] = Ex∼λ
-> Invalid unicode use found on p. 10: −2ϵ
-> Invalid unicode use found on p. 10: ϵ−1
-> Invalid unicode use found on p. 11: space, as long as the design and the estimator a⊤A(γ)(λ)−1x can be computed efficiently.
-> Invalid unicode use found on p. 11: O(T 1−
-> Invalid unicode use found on p. 15: log(δ−1)
-> Invalid unicode use found on p. 15: satisfies with probability at least 1 −δ that
-> Invalid unicode use found on p. 15: i=1, δ) −µ| ≤4u
-> Invalid unicode use found on p. 15: log(δ−1)
-> Invalid unicode use found on p. 15: {a⊤A(γ)(λ)−1xi yi}n
-> Invalid unicode use found on p. 15: a∈A |a⊤bθ(γ) −a⊤θ∗| = max
-> Invalid unicode use found on p. 15: a∈A |a⊤bθ(γ) −W (a) + W (a) −a⊤θ∗|
-> Invalid unicode use found on p. 15: a∈A |a⊤bθ(γ) −W (a)| + max
-> Invalid unicode use found on p. 15: a∈A |W (a) −a⊤θ∗|
-> Invalid unicode use found on p. 15: a∈A |aT θ −W (a)| + max
-> Invalid unicode use found on p. 15: a∈A |W (a) −a⊤θ∗|
-> Invalid unicode use found on p. 15: a∈A |W (a) −a⊤θ∗|.
-> Invalid unicode use found on p. 15: For fixed a, we bound the (1 + ϵ)-moment of a⊤A(γ)(λ)−1xy, where x ∼λ and y = x⊤θ∗+ η, as
-> Invalid unicode use found on p. 15: h

                                        a⊤A(γ)(λ)−1xy
-> Invalid unicode use found on p. 15: h

                                        a⊤A(γ)(λ)−1x(x⊤θ∗+ η)
-> Invalid unicode use found on p. 15: h

                                        a⊤A(γ)(λ)−1x(x⊤θ∗)
-> Invalid unicode use found on p. 15: h

                                        a⊤A(γ)(λ)−1x
-> Invalid unicode use found on p. 15: h

                                        a⊤A(γ)(λ)−1x
-> Invalid unicode use found on p. 15: h

                                        a⊤A(γ)(λ)−1x
-> Invalid unicode use found on p. 15: Using this moment bound and Lemma 3, for any a, we have with probability at least 1 −
-> Invalid unicode use found on p. 15: |W (a) −E[W (a)]| ≤16(1 + υ)
-> Invalid unicode use found on p. 15: log(δ−1|A|)
-> Invalid unicode use found on p. 15: |a⊤θ∗−E[W (a)]| = |⟨θ∗, a⟩−E[a⊤A(γ)(λ)−1xx⊤θ∗]|
-> Invalid unicode use found on p. 15: = |⟨θ∗, a⟩−a⊤A(γ)(λ)−1A(λ)θ∗|
-> Invalid unicode use found on p. 15: = |⟨θ∗, a⟩−a⊤A(γ)(λ)−1A(γ)(λ) −γI
-> Invalid unicode use found on p. 15: (A(λ) = A(γ)(λ) −γI)
-> Invalid unicode use found on p. 15: = γ|a⊤A(γ)(λ)−1θ∗|
-> Invalid unicode use found on p. 15: = γ|a⊤(A(λ) + γI)−1/2(A(λ) + γI)−1/2θ∗|
-> Invalid unicode use found on p. 15: ≤γ∥a∥A(γ)(λ)−1γ−1/2∥θ∗∥(I+γ−1A(λ))−1
-> Invalid unicode use found on p. 16: ≤γ1/2∥a∥A(γ)(λ)−1∥θ∗∥2
-> Invalid unicode use found on p. 16: (I + γ−1A(λ) ⪰I)
-> Invalid unicode use found on p. 16: ≤γ1/2β−1∥θ∗∥2M1+ϵ(λ; A, γ, β)
-> Invalid unicode use found on p. 16: Using Lemma 1 for action set Aℓ, we have with probability of at least 1 −
-> Invalid unicode use found on p. 16: a∈Aℓ|a⊤θ∗−a⊤bθℓ| ≤
-> Invalid unicode use found on p. 16: 2γ1/2∥θ∗∥2β−1 + 32(1 + υ)
-> Invalid unicode use found on p. 16: ≤2γ1/2bβ−1M1+ϵ(λ∗
-> Invalid unicode use found on p. 16: ≤2γ1/2bβ−1M∗
-> Invalid unicode use found on p. 16: |x⊤bθℓ(V) −x⊤θ∗| ≤ϵℓ+ 2bγ1/2β−1M∗
-> Invalid unicode use found on p. 16: As E[RT 1Ec] = E[RT |Ec]P[Ec] ≤(supx,x′ x′⊤θ∗−x⊤θ∗)T 1
-> Invalid unicode use found on p. 16: Let x∗= argmaxx∈A x⊤θ∗; then, for every ℓsuch that 2ϵℓ≥4bγ1/2β−1M1+ϵ(A, γ, β)
-> Invalid unicode use found on p. 16: x⊤bθℓ−x∗⊤bθℓ= (x⊤bθℓ−x⊤θ∗) + (x⊤θ∗−x∗⊤θ∗) + (x∗⊤θ∗−x∗⊤bθℓ)
-> Invalid unicode use found on p. 16: ≤2ϵℓ+ 4bγ1/2β−1M∗
-> Invalid unicode use found on p. 16: x′⊤bθℓ−x⊤bθℓ
-> Invalid unicode use found on p. 16: ≥x∗⊤bθℓ−x⊤bθℓ
-> Invalid unicode use found on p. 16: ≥x∗⊤θ∗−x⊤θ∗−2ϵℓ−4bγ1/2β−1M∗
-> Invalid unicode use found on p. 17: ≥x∗⊤θ∗−x⊤θ∗−4ϵℓ
-> Invalid unicode use found on p. 17: In summary, the above arguments show that when 2ϵℓ≥4bγ1/2β−1M∗
-> Invalid unicode use found on p. 17: increases beyond such a point, we still incur regret at most 32bγ1/2β−1M∗
-> Invalid unicode use found on p. 17: x∗T θ∗−xT θ∗
-> Invalid unicode use found on p. 17: τℓmax{16ϵℓ, 32bγ1/2β−1M∗
-> Invalid unicode use found on p. 17: (ζ := 32bγ1/2β−1M1+ϵ(A, γ, β)
-> Invalid unicode use found on p. 17: −1+ϵ
-> Invalid unicode use found on p. 17: −1
-> Invalid unicode use found on p. 17: −ϵ
-> Invalid unicode use found on p. 17: C0β−1b + C1(1 + υ)
-> Invalid unicode use found on p. 17: −2ϵ
-> Invalid unicode use found on p. 17: −2ϵ
-> Invalid unicode use found on p. 17: −1
-> Invalid unicode use found on p. 17: possible term ω−1
-> Invalid unicode use found on p. 17: However, we can overcome this by shifting all probabilities and adding −1 to the support of the
-> Invalid unicode use found on p. 18: w.p. 1 −γ
-> Invalid unicode use found on p. 18: d∆) −3
-> Invalid unicode use found on p. 18: −1
-> Invalid unicode use found on p. 18: E[|y(x) −θ⊤x|1+ϵ | x]
-> Invalid unicode use found on p. 18: ≤|γ−1
-> Invalid unicode use found on p. 18: ϵ −θ⊤x|1+ϵ(θ⊤x + 2
-> Invalid unicode use found on p. 18: d∆) + |θ⊤x|1+ϵ + | −1 −θ⊤x|1+ϵ2
-> Invalid unicode use found on p. 18: ≤21+ϵγ−13
-> Invalid unicode use found on p. 18: d∆≤1 and γ−1
-> Invalid unicode use found on p. 18: −xt,isign(θi)
-> Invalid unicode use found on p. 18: −xt,isign(θi)
-> Invalid unicode use found on p. 18: −xt,isign(θi)
-> Invalid unicode use found on p. 18: d −xt,ib
-> Invalid unicode use found on p. 18: Eθ[Ui(1)] ≥Eθ′[Ui(1)] −
-> Invalid unicode use found on p. 18: ≥Eθ′[Ui(1)] −
-> Invalid unicode use found on p. 18: ≥Eθ′[Ui(1)] −
-> Invalid unicode use found on p. 18: 1−ϵ
-> Invalid unicode use found on p. 18: ≥Eθ′[Ui(1)] −24
-> Invalid unicode use found on p. 18: 1−ϵ
-> Invalid unicode use found on p. 19: ≥Eθ′[Ui(1)] −24
-> Invalid unicode use found on p. 19: 1−ϵ
-> Invalid unicode use found on p. 19: mina∈{γ−1
-> Invalid unicode use found on p. 19: ϵ ,0,−1} P[yθ′(xt) = a] sup
-> Invalid unicode use found on p. 19: a |P[yθ(xt) = a] −P[yθ′(xt) = a]|2
-> Invalid unicode use found on p. 19: ϵ −1∆
-> Invalid unicode use found on p. 19: −1
-> Invalid unicode use found on p. 19: 3ϵ−1
-> Invalid unicode use found on p. 19: −ϵ
-> Invalid unicode use found on p. 19: Eθ[Ui(1)] + Eθ′[Ui(−1)] ≥Eθ′[Ui(1) + Ui(−1)] −24
-> Invalid unicode use found on p. 19: 1−ϵ
-> Invalid unicode use found on p. 19: −24
-> Invalid unicode use found on p. 19: 1−ϵ
-> Invalid unicode use found on p. 19: d −T
-> Invalid unicode use found on p. 19: θ∈{−∆,∆}d
-> Invalid unicode use found on p. 19: θi∈{−∆,∆}
-> Invalid unicode use found on p. 19: {θj}j̸=i 1 = 2d−1)
-> Invalid unicode use found on p. 19: (Eθ[Ui(1)] + Eθ′[Ui(−1)] ≥T
-> Invalid unicode use found on p. 20: f(x∗) −f(xt)
-> Invalid unicode use found on p. 20: Kν,l(x, x′) := 21−ν
-> Invalid unicode use found on p. 20: ∥x −x′∥2
-> Invalid unicode use found on p. 20: ∥x −x′∥2
-> Invalid unicode use found on p. 20: −2ϵ
-> Invalid unicode use found on p. 20: T 1−
-> Invalid unicode use found on p. 20: ψ⊤A(γ)(λ)−1ρ = γ−1ψ⊤ρ −γ−1kλ(ψ)(Kλ + I|A|)−1kλ(ρ).
-> Invalid unicode use found on p. 20: Then the gradient for the experimental design problem infλ∈∆V maxv∈V ∥ϕ(v)∥A(γ)(λ)−1 (which is an
-> Invalid unicode use found on p. 21: the well-known polynomial eigenvalue decay of the Matérn kernel. Specifically, the j-th eigenvalue φj satisfies φj ≤O(j−κ) with κ =
-> Invalid unicode use found on p. 21: A(γ)(λ)−1
-> Invalid unicode use found on p. 21: D) + γI)−1
-> Invalid unicode use found on p. 21: D + γI)−1
-> Invalid unicode use found on p. 21: cj−κ
-> Invalid unicode use found on p. 21: cj−κ + γ
-> Invalid unicode use found on p. 21: j≤γ−1
-> Invalid unicode use found on p. 21: j−κ
-> Invalid unicode use found on p. 21: j−κ + γ + 4c
-> Invalid unicode use found on p. 21: j>γ−1
-> Invalid unicode use found on p. 21: j−κ
-> Invalid unicode use found on p. 21: j−κ + γ
-> Invalid unicode use found on p. 21: ≤4cγ−1/κ + 4c
-> Invalid unicode use found on p. 21: j>γ−1
-> Invalid unicode use found on p. 21: j−κ
-> Invalid unicode use found on p. 21: ≤4cγ−1
-> Invalid unicode use found on p. 21: κ + 4c(γ−1
-> Invalid unicode use found on p. 21: κ )1−κ
-> Invalid unicode use found on p. 21: (κ −1)γ
-> Invalid unicode use found on p. 21: = 4cγ−1
-> Invalid unicode use found on p. 21: κ −1
-> Invalid unicode use found on p. 21: −2ϵ
-> Invalid unicode use found on p. 21: O(T 1−
-> Invalid unicode use found on p. 21: O(T 1−
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Skipping possible_ref_id '0 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
Backend tkagg is interactive backend. Turning interactive mode on.
-> Skipping possible_ref_id '0 1]' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Warning: Bracket content '2013' on p. 3 could not be matched to a reference.
   -> Sentence:  Robustness to heavy tails was first introduced into sequential decision-making by Bubeck et al (2013) in the context of multi-armed bandits
-> Couldn't parse in-text references '(['A', ' ϵ', ' υ'])' in bracket on p. 2!
-> Skipping possible_ref_id 'who studied the finite-variance setting ϵ = 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '0 1]' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'd log |A|' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Warning: Bracket content '1+ϵ' on p. 4 could not be matched to a reference.
   -> Sentence: 3 Related Work The first systematic study of heavy-tailed noise in bandits is due to Bubeck et al (2013), who replaced the empirical mean in UCB with robust mean estimators, and
obtained a regret bound of eO n ϵ 1+ϵ T 1/(1+ϵ) with n arms, along with a matching lower bound
-> Warning: Bracket content '2021' on p. 4 could not be matched to a reference.
   -> Sentence:  Zhong et al (2021) suggested median based estimators for symmetric error distributions without any bounded moments (e
-> Skipping possible_ref_id '0 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'and therefore the central moment since the rewards are nonnegative' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'A θ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'A θ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text references '(['xt', '2i−1 −xt', '2i'])' in bracket on p. 5!
-> Couldn't parse in-text references '(['xt', '2i−1 −xt', '2i'])' in bracket on p. 5!
-> Couldn't parse in-text references '(['xt', '2i−1 −xt', '2i'])' in bracket on p. 5!
-> Couldn't parse in-text references '(['xt', '2i−1 −xt', '2i'])' in bracket on p. 5!
-> Skipping possible_ref_id '0 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '∆ 2∆' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '2∆ ∆' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'θ θ′' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'A θ∗' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'd 2⌊d 4 ⌋' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'd 2⌊d 4 ⌋' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '4 d' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'm 4d 1 4 √ d' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'xtU di+b = 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'Ti b' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'A θ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'xtU di+indi(θ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '∆+ ∆I{j = di + b} j ∈[di + 1 di+1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '∆ j ∈[di + 1 di+1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'xt di+b = 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'xt di+b = 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'xt di+b = 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'm 4d 1 4 √ d' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'xt di+b = 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'Ti b' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'Ti b' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text references '(['Jensen', ' P b Ti', 'b = T & choice of ∆'])' in bracket on p. 8!
-> Skipping possible_ref_id 'xt di+indi(θ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'xt di+indi(θ∗' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'A θ∗' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '4 d' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'S δ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text (sub) reference '(λ)' in bracket 'λ; Aℓ, γ, β' on p. 9!
-> Couldn't parse in-text (sub) reference '( Aℓ, γ, β)' in bracket 'λ; Aℓ, γ, β' on p. 9!
-> Skipping possible_ref_id 'xi yi' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '{Xi}n i=1 δ' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text (sub) reference '(λ)' in bracket 'λ; A, γ, β' on p. 10!
-> Couldn't parse in-text (sub) reference '( A, γ, β)' in bracket 'λ; A, γ, β' on p. 10!
-> Couldn't parse in-text (sub) reference '(λ)' in bracket 'λ; A, γ, β' on p. 10!
-> Couldn't parse in-text (sub) reference '( A, γ, β)' in bracket 'λ; A, γ, β' on p. 10!
-> Couldn't parse in-text (sub) reference '(λ)' in bracket 'λ; A, γ, β' on p. 10!
-> Couldn't parse in-text (sub) reference '( A, γ, β)' in bracket 'λ; A, γ, β' on p. 10!
-> Couldn't parse in-text (sub) reference '(λ)' in bracket 'λ; A, γ, β' on p. 10!
-> Couldn't parse in-text (sub) reference '( A, γ, β)' in bracket 'λ; A, γ, β' on p. 10!
-> Couldn't parse in-text references '(['A', ' γ', ' β'])' in bracket on p. 10!
-> Couldn't parse in-text (sub) reference '(λ)' in bracket 'λ; V, γ, β' on p. 10!
-> Couldn't parse in-text (sub) reference '( V, γ, β)' in bracket 'λ; V, γ, β' on p. 10!
-> Couldn't parse in-text references '(['A', ' T −2ϵ 1+ϵ ', ' β'])' in bracket on p. 10!
-> Couldn't parse in-text references '(['A', ' γ', ' β'])' in bracket on p. 10!
-> Couldn't parse in-text references '(['A', ' γ', ' β'])' in bracket on p. 10!
-> Couldn't parse in-text references '(['γ1/2β−1M∗ 1+ϵ(A', ' γ', ' β) 1 1+ϵ '])' in bracket on p. 10!
-> Couldn't parse in-text references '(['A', ' T −2ϵ 1+ϵ ', ' β'])' in bracket on p. 10!
-> Couldn't parse in-text references '(['A', ' T −2ϵ 1+ϵ ', ' 1'])' in bracket on p. 11!
-> Couldn't parse in-text (sub) reference '(λ)' in bracket 'λ; A, T −2ϵ 1+ϵ , 1' on p. 11!
-> Couldn't parse in-text (sub) reference '( A, T −2ϵ 1+ϵ , 1)' in bracket 'λ; A, T −2ϵ 1+ϵ , 1' on p. 11!
-> Couldn't parse in-text references '(['Lattimore and Szepesvári', ' 2020', ' Chapter 21'])' in bracket on p. 11!
-> Skipping possible_ref_id '∥· ∥p r' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'x y' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'stated informally here with the formal version deferred to Appendix C' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '0 1' since it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text references '(['ϵ', ' d', ' ν'])' in bracket on p. 12!
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━━━━━━━━  73% 0:00:07
-> Processed 238 sentences on 12 pages -> Avg. of 22.636363636363637 sentences per page
-> Warning: Reference 'Lugosi and Mendelson 2019a' never used in the document's text.
-> Warning: Reference 'Lugosi and Mendelson 2019b' never used in the document's text.
-> Warning: Reference 'Sason 2015' never used in the document's text.
-> Warning: Reference 'Scarlett et al 2017' never used in the document's text.
-> Warning: Reference 'Vakili et al 2021a' never used in the document's text.
-> Warning: Reference 'Vakili et al 2021b' never used in the document's text.
-> Warning: Reference 'Xue et al 2023' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = Audibert and Catoni 2011); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = Baccelli et al 2002); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 3 (Ref. ID = Camilleri et al 2021); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = Catoni 2012); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 6 (Ref. ID = Choi et al 2020); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = Chowdhury and Gopalan 2019); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = Cont 2001); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = Cont and Bouchaud 2000); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = Hsu and Sabato 2014); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = Huang et al 2022); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = Huang et al 2023); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = Jebarajakirthy et al 2021); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = Kang and Kim 2023); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = Lattimore and Szepesvári 2020); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = Li and Sun 2024); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = Lu et al 2019); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = Lugosi and Mendelson 2019a); Skipping LLM check...
-> WARNING: Reference with index 21 (Ref. ID = Lugosi and Mendelson 2019b) has no associated sentence!
-> Missing an abstract for reference with index 22 (Ref. ID = Medina and Yang 2016); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = Roberts et al 2015); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = Sason 2015); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = Scarlett et al 2017); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = Shao et al 2018); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 28 (Ref. ID = Vakili et al 2021a); Skipping LLM check...
-> WARNING: Reference with index 29 (Ref. ID = Vakili et al 2021b) has no associated sentence!
-> Missing an abstract for reference with index 30 (Ref. ID = Wang et al 2025); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 32 (Ref. ID = Xue et al 2020); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = Xue et al 2023); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = Yu et al 2018); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 47 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 7
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 8
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 9
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 10
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 11
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\50 Improved Regret Bounds for Linear Bandits\PAU_results.md
```