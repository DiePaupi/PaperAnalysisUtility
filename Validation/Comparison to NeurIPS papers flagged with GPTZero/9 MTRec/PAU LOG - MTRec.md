
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\9 MTRec\MTRec Learning to Align with User Preferences via.pdf"
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
 - 'numeric'           = A number placed inside square brackets (e.g., [28])
                      -> Multiple references are separated by a comma (e.g., [28,29])
 - 'authoryear_round'  = Authors' names and the year places insince round brackets (e.g., (Speckmann et al., 2025))
                      -> Multiple references are separated by a semicolon (e.g., (Speckmann et al. 2025; Janiesch et al. 2021))
                      -> Please note that the author and year are *not* separated
 - 'authoryear_square' = Authors' names and the year places insince square brackets (e.g., [Speckmann et al., 2025])
                      -> Multiple references are separated by a comma (e.g., [Speckmann et al., 2025, Janiesch et al., 2021])
                      -> Please note that the author and year are also separated by a comma
Enter a supported referencing template (['numeric', 'authoryear_round', 'authoryear_square']): authoryear_square
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Related Works' on page 2
- Found following heading '3 - Preliminaries' on page 3
- Found following heading '4 - Method' on page 4
- Found following heading '5 - Experiments' on page 7
- Found following heading '6 - Conclusions' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Technical Appendices and Supplementary Material' on page 19
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 19
All found references: 40
-> Warning: Could not parse year in reference 'NeurIPS Paper Checklist 1. Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: Our main contribution is the MTRec framework with the QR-IQL algorithm, which is described in Section 4 and justified in Section 5. Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper. • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers. • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper. 2. Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes] Justification: The limitation is discussed in Appendix A.5. Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate "Limitations" section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. • The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. • The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations. 3. Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: [Yes] Justification: The derivations details are provided in Appendix A. Guidelines: • The answer NA means that the paper does not include theoretical results. • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced. • All assumptions should be clearly stated or referenced in the statement of any theorems. • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. • Theorems and Lemmas that the proof relies upon should be properly referenced. 4. Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: [Yes] Justification: The implementation details are provided in Appendix A.3. Guidelines: • The answer NA means that the paper does not include experiments. • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. • Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results. 5. Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? Answer: [No] Justification: We provide implementation details in Appendix A.3 and will release the code upon acceptance of this paper. Guidelines: • The answer NA means that paper does not include experiments requiring code. • Please see the NeurIPS code and data submission guidelines ('!
 -> Found dublicated ref_ids:
                                       full_reference            ref_id  ... link valid
3   Xiaocong Chen, Lina Yao, Aixin Sun, Xianzhi Wa...  Chen et al, 2021  ...       None
19  Langming Liu, Liu Cai, Chi Zhang, Xiangyu Zhao...   Liu et al, 2023  ...       None

[2 rows x 11 columns]
-----------
 -> Parsed references DataFrame:
                            ref_id  ... valid
0                Brian et al, 2008  ...  None
1                Chen et al, 2021a  ...  None
2                 Chen et al, 2019  ...  None
3                Chen et al, 2021b  ...  None
4                Cheng et al, 2016  ...  None
5            Covington et al, 2016  ...  None
6                  Dai et al, 2021  ...  None
7            Deepak and Amir, 2007  ...  None
8                 Dong et al, 2023  ...  None
9                    Fawcett, 2006  ...  None
10                Garg et al, 2021  ...  None
11             Gilotte et al, 2018  ...  None
12                 Guo et al, 2017  ...  None
13            Haarnoja et al, 2018  ...  None
14           Jaedeug and Kim, 2012  ...  None
15              Jiawei et al, 2023  ...  None
16        Jonathan and Ermon, 2016  ...  None
17             Kingma and Ba, 2015  ...  None
18                Liu et al, 2023a  ...  None
19                Liu et al, 2023b  ...  None
20                 Liu et al, 2024  ...  None
21             McAuley et al, 2015  ...  None
22              Ouyang et al, 2022  ...  None
23                  Qu et al, 2016  ...  None
24         Saurabh and Doshi, 2021  ...  None
25            Schulman et al, 2017  ...  None
26                 Shi et al, 2019  ...  None
27  Swaminathan and Joachims, 2015  ...  None
28                Wang et al, 2017  ...  None
29                Wang et al, 2021  ...  None
30    Wang-Cheng and McAuley, 2018  ...  None
31                Will et al, 2018  ...  None
32                 Lee et al, 2021  ...  None
33                Yang et al, 2021  ...  None
34                  Yi et al, 2023  ...  None
35                Yu and Qin, 2020  ...  None
36               Zheng et al, 2018  ...  None
37                Zhou et al, 2018  ...  None
38                Zhou et al, 2019  ...  None
39                            1, 0  ...  None

[40 rows x 10 columns]
- Checking reference 1/40:
  -> INFO: Now checking 10 results for matching title: 'Maximum entropy inverse reinforcement learning'
       -> INFO: All authors matched!
- Checking reference 2/40:
  -> INFO: Now checking 1 results for matching title: 'Curriculum disentangled recommendation with noisy multi-feedback'
       -> INFO: All authors matched!
- Checking reference 3/40:
  -> INFO: Now checking 1 results for matching title: 'Top-k off-policy correction for a REINFORCE recommender system'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/40:
  -> INFO: Now checking 10 results for matching title: 'Generative inverse deep reinforcement learning for online recommendation'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 5/40:
  -> INFO: Now checking 10 results for matching title: 'Wide & deep learning for recommender systems'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 6/40:
  -> INFO: Now checking 10 results for matching title: 'Deep neural networks for youtube recommendations'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 3)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/40:
  -> INFO: Now checking 1 results for matching title: 'An adversarial imitation click model for information retrieval'
       -> INFO: All authors matched!
- Checking reference 8/40:
  -> INFO: Now checking 10 results for matching title: 'Bayesian inverse reinforcement learning'
       -> INFO: All authors matched!
- Checking reference 9/40:
  -> INFO: Now checking 1 results for matching title: 'Raft: Reward ranked finetuning for generative foundation model alignment.'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Raft: Reward ranked finetuning for generative foundation model alignment.'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 6)
                   Unmatched authors = '0015, Chow, 0002, 0001'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 5)
                   Unmatched authors = '0015, 0002, 0001'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/40:
  -> INFO: Now checking 10 results for matching title: 'An introduction to roc analysis'
       -> INFO: All authors matched!
- Checking reference 11/40:
  -> INFO: Now checking 10 results for matching title: 'Iq-learn: Inverse soft-q learning for imitation'
       -> INFO: All authors matched!
- Checking reference 12/40:
  -> INFO: Now checking 10 results for matching title: 'Offline a/b testing for recommender systems'
       -> INFO: All authors matched!
- Checking reference 13/40:
  -> INFO: Now checking 1 results for matching title: 'Deepfm: a factorizationmachine based neural network for ctr prediction'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 4 results for matching title: 'Deepfm: a factorizationmachine based neural network for ctr prediction'
  -> WARNING: None of the 4 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepfm:+a+factorizationmachine+based+neural+network+for+ctr+prediction manually and check the results.
        -> Author(s): Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, and Xiuqiang He
        -> Title:     Deepfm: a factorizationmachine based neural network for ctr prediction
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 14/40:
  -> INFO: Now checking 10 results for matching title: 'Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor'
       -> INFO: All authors matched!
- Checking reference 15/40:
  -> INFO: Now checking 10 results for matching title: 'Nonparametric bayesian inverse reinforcement learning for multiple reward functions'
       -> INFO: All authors matched!
- Checking reference 16/40:
  -> INFO: Now checking 1 results for matching title: 'Bias and debias in recommender system: A survey and future directions'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/40:
  -> INFO: Now checking 10 results for matching title: 'Generative adversarial imitation learning'
       -> INFO: All authors matched!
- Checking reference 18/40:
  -> INFO: Now checking 10 results for matching title: 'Deepfm: a factorization-machine based neural network for ctr prediction'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Deepfm: a factorization-machine based neural network for ctr prediction'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepfm:+a+factorization-machine+based+neural+network+for+ctr+prediction manually and check the results.
        -> Author(s): Diederik P  Kingma and Jimmy Ba
        -> Title:     Deepfm: a factorization-machine based neural network for ctr prediction
        -> Year:      2015
     -> Manual search was skipped by the user.
- Checking reference 19/40:
  -> INFO: Now checking 2 results for matching title: 'Adversarial batch inverse reinforcement learning: Learn to reward from imperfect demonstration for interactive recommendation'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 4)
                   Unmatched authors = ''
       -> INFO: All authors matched!
- Checking reference 20/40:
  -> INFO: Now checking 7 results for matching title: 'Linrec: Linear attention mechanism for long-term sequential recommender systems'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 12)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 21/40:
  -> INFO: Now checking 10 results for matching title: 'Bidirectional gated mamba for sequential recommendation'
       -> INFO: All authors matched!
- Checking reference 22/40:
  -> INFO: Now checking 7 results for matching title: 'Image-based recommendations on styles and substitutes'
       -> INFO: All authors matched!
- Checking reference 23/40:
  -> INFO: Now checking 10 results for matching title: 'Training language models to follow instructions with human feedback'
       -> INFO: All authors matched!
- Checking reference 24/40:
  -> INFO: Now checking 10 results for matching title: 'Product-based neural networks for user response prediction'
       -> INFO: All authors matched!
- Checking reference 25/40:
  -> INFO: Now checking 3 results for matching title: 'A survey of inverse reinforcement learning: Challenges, methods and progress'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/40:
  -> INFO: Now checking 10 results for matching title: 'Proximal policy optimization algorithms'
       -> INFO: All authors matched!
- Checking reference 27/40:
  -> INFO: Now checking 10 results for matching title: 'Virtual-taobao: Virtualizing real-world online retail environment for reinforcement learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 28/40:
  -> INFO: Now checking 4 results for matching title: 'The self-normalized estimator for counterfactual learning'
       -> INFO: All authors matched!
- Checking reference 29/40:
  -> INFO: Now checking 10 results for matching title: 'Deep & cross network for ad click predictions'
       -> INFO: All authors matched!
- Checking reference 30/40:
  -> INFO: Now checking 10 results for matching title: 'Denoising implicit feedback for recommendation'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/40:
  -> INFO: Now checking 10 results for matching title: 'Self-attentive sequential recommendation'
       -> INFO: All authors matched!
- Checking reference 32/40:
  -> INFO: Now checking 10 results for matching title: 'Distributional reinforcement learning with quantile regression'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/40:
  -> INFO: Now checking 10 results for matching title: 'Dual unbiased recommender learning for implicit feedback'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 3)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/40:
  -> INFO: Now checking 9 results for matching title: 'Capturing delayed feedback in conversion rate prediction via elapsed-time sampling'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 35/40:
  -> INFO: Now checking 4 results for matching title: 'Unbiased pairwise learning from implicit feedback for recommender systems without biased variance control'
       -> INFO: All authors matched!
- Checking reference 36/40:
  -> INFO: Now checking 2 results for matching title: 'Sampler design for implicit feedback data by noisy-label robust learning'
       -> INFO: All authors matched!
- Checking reference 37/40:
  -> INFO: Now checking 1 results for matching title: 'DRN: A deep reinforcement learning framework for news recommendation'
       -> INFO: All authors matched!
- Checking reference 38/40:
  -> INFO: Now checking 10 results for matching title: 'Deep interest network for click-through rate prediction'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 9)
                   Unmatched authors = 'Dai'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 39/40:
  -> INFO: Now checking 10 results for matching title: 'Deep interest evolution network for click-through rate prediction'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 40/40:
  -> Checking if provided link is pingable: https://nips.cc/public/guides/CodeSubmissionPolicy)
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: Our main contribution is the MTRec framework with the QR-IQL algorithm, which is described in Section 4 and justified in Section 5
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 998 results for matching title: 'Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: Our main contribution is the MTRec framework with the QR-IQL algorithm, which is described in Section 4 and justified in Section 5'
  -> WARNING: None of the 998 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Claims+Question:+Do+the+main+claims+made+in+the+abstract+and+introduction+accurately+reflect+the+paper’s+contributions+and+scope?+Answer:+[Yes]+Justification:+Our+main+contribution+is+the+MTRec+framework+with+the+QR-IQL+algorithm%2C+which+is+described+in+Section+4+and+justified+in+Section+5 manually and check the results.
        -> Author(s): NeurIPS Paper Checklist 1
        -> Title:     Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: Our main contribution is the MTRec framework with the QR-IQL algorithm, which is described in Section 4 and justified in Section 5
        -> Year:      0
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: i∈I pϕ(ˆa|i, ht−1),
-> Invalid unicode use found on p. 2: π∈Π EπE[r(s, a)] −Eπ[r(s, a)] −H(π),
-> Invalid unicode use found on p. 2: where H(π) ≜Eπ[−log π(a|s)] denotes the entropy of policy π. Intuitively, this formulation learns
-> Invalid unicode use found on p. 2: π∈Π EρE[r(s, a)] −Eρ[r(s, a)] −H(π) −ϕ(r),
-> Invalid unicode use found on p. 2: If we define the regularizer as ψ(x) = x −ϕ(x), then EρE[r(s, a)] −ϕ(r) can be compactly represented by
-> Invalid unicode use found on p. 3: r(s, a) = Q(s, a) −γEs′∼P (s,a)V (s′), where V (s) = Ea∼π(·|s)[Q(s, a) −log π(a|s)]. Also the
-> Invalid unicode use found on p. 3: Q∈ΩEs,a∼ρE[ψ(Q(s, a) −γEs′∼P (s,a)V ∗(s′))] −(1 −γ)Es0∼ρ0[V ∗(s0)],
-> Invalid unicode use found on p. 3: r(s, a) = Q(s, a) −γEρE[log
-> Invalid unicode use found on p. 5: D= Q(s, a) −γEρE[log
-> Invalid unicode use found on p. 5: in Problem 4 (i.e., (1 −γ)Es0∼ρ0[V (s0)]) can be replaced by E(s,a)∼ρE[V (s) −γV (s′)]. In other
-> Invalid unicode use found on p. 5: Garg et al. [2021], we choose the regularizer as ψ(x) = x −
-> Invalid unicode use found on p. 5: Qλ EρE[Qλ(s, a) −log
-> Invalid unicode use found on p. 5: exp Qλ(s, a)] −1
-> Invalid unicode use found on p. 5: 4αEρE[(Qλ(s, a) −log
-> Invalid unicode use found on p. 5: λ(s, a) −γEρE[log
-> Invalid unicode use found on p. 6: LCE(ζ) = −EDE[aP log(Fζ(i|h)) + aN log(1 −Fζ(i|h))],
-> Invalid unicode use found on p. 6: LAlign(ζ) = −EDE[r∗(s, aP ) · Fζ(i|h) + r∗(s, aN) · (1 −Fζ(i|h))],
-> Invalid unicode use found on p. 6: LRL(ζ) = −Eit∼Fζ[
-> Invalid unicode use found on p. 6: ˆr(ht−1, it, at)]
-> Invalid unicode use found on p. 6: LF inal(ζ) = −Eit∼Fζ[
-> Invalid unicode use found on p. 6: ˆr(ht−1, it, at) + κ · r∗(ht−1, it, at)]
-> Invalid unicode use found on p. 18: Q∈ΩEs,a∼ρE[ψ(Q(s, a) −γEs′∼P (s,a)V ∗(s′))] −(1 −γ)Es0∼ρ0[V ∗(s0)],
-> Invalid unicode use found on p. 18: (1 −γ)Es0∼ρ0[V ∗(s0)] = (1 −γ)
-> Invalid unicode use found on p. 18: EDE[V ∗(st)] −(1 −γ)
-> Invalid unicode use found on p. 18: = EρE[V ∗(s) −γV ∗(s′)],
-> Invalid unicode use found on p. 18: Then, on substituting ψ(x) = x −
-> Invalid unicode use found on p. 18: Q EρE[Q(s, a) −log
-> Invalid unicode use found on p. 18: exp Q(s, a)] −1
-> Invalid unicode use found on p. 18: 4αEρE[(Q(s, a) −log
-> Invalid unicode use found on p. 19: (λ −1) · u,
-> Invalid unicode use found on p. 19: λi(s, a) = λi(s, a) −log
-> Invalid unicode use found on p. 19: 4α(λi(s, a) −log
-> Invalid unicode use found on p. 20: λ(s, a) −γV ∗(s′), ∀s, a ∼DE;
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> INFO: Found possible citet reference but couldn't really match it: '[2016]'
      -> Sentence: ', click, video watching) to train recommendation models Covington et al [2016], Zhou et al [2018], Dai et al [2021], 
Yang et al [2021]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[2018]'
      -> Sentence: ', Zhou et al [2018], Dai et al [2021], Yang et al [2021]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[2020]'
      -> Sentence: ' [2020], Wang et al [2021]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[2021]'
      -> Sentence: ' Another line of works address various types of biases in user feedback, including position bias, selection bias, 
popularity bias and exposure bias woong Lee et al [2021], Yi et al [2023]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[2023]'
      -> Sentence: ' In some sense, such errors can be regarded as a certain type of inductive bias Jiawei et al [2023], because implicit 
feedback is wrongly assumed to reflect users’ real preferences'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[2019]'
      -> Sentence: ' Prior works have explored using reinforcement learning (RL) to optimize recommendation policy, where the recommender 
system is modeled as an agent and the users are treated as key components of environment Chen et al [2019], Zheng et al [2018]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[2021b]'
      -> Sentence: ' Some works apply IRL to infer the reward function for the recommender system, assuming expert recommendation policies
are available Chen et al [2021b], Liu et al [2023a]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'r(s'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a)'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  max r∈R min π∈Π EπE[r(s, a)] −Eπ[r(s, a)] −H(π), (2) where H(π) ≜Eπ[−log π(a|s)] denotes the entropy of policy π
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'r(s'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a)'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  max r∈R min π∈Π EπE[r(s, a)] −Eπ[r(s, a)] −H(π), (2) where H(π) ≜Eπ[−log π(a|s)] denotes the entropy of policy π
-> WARNING: Mismatch in intext-reference-parsing! Skipping '−log π(a|s)'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  max r∈R min π∈Π EπE[r(s, a)] −Eπ[r(s, a)] −H(π), (2) where H(π) ≜Eπ[−log π(a|s)] denotes the entropy of policy π
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'r(s'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a)'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  Then, Problem 2 can rewritten as: max r∈R min π∈Π EρE[r(s, a)] −Eρ[r(s, a)] −H(π) −ϕ(r), (3) where ϕ is a convex regularizer on r 
Jonathan and Ermon [2016]
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'r(s'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a)'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  Then, Problem 2 can rewritten as: max r∈R min π∈Π EρE[r(s, a)] −Eρ[r(s, a)] −H(π) −ϕ(r), (3) where ϕ is a convex regularizer on r 
Jonathan and Ermon [2016]
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'r(s'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a)'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  If we define the regularizer as ψ(x) = x −ϕ(x), then EρE[r(s, a)] −ϕ(r) can be compactly represented by EρE[ψ(r(s, a))]
-> INFO: Found possible citet reference but couldn't really match it: '[ψ(r(s]'
      -> Sentence: ' −ϕ(r) can be compactly represented by EρE[ψ(r(s, a))]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a) −log π(a|s)'...
-> INFO: Found possible citet reference but couldn't really match it: '[2008]'
      -> Sentence: ' Then, the inner problem becomes trivial so that Problem 3 can be reformulated as follows Brian et al [2008], Haarnoja
et al [2018]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[ψ(Q(s]'
      -> Sentence: ' max Q∈ΩEs,a∼ρE[ψ(Q(s, a) −γEs′∼P (s,a)V ∗(s′))] −(1 −γ)Es0∼ρ0[V ∗(s0)], (4) where V ∗(s) = log P a exp Q(s, a)'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> Warning: Bracket content ['V ∗(s0),'] on p. 4 could not be matched to a reference.
   -> Sentence:  max Q∈ΩEs,a∼ρE[ψ(Q(s, a) −γEs′∼P (s,a)V ∗(s′))] −(1 −γ)Es0∼ρ0[V ∗(s0)], (4) where V ∗(s) = log P a exp Q(s, a)
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'log X a exp Q(s′'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a)'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  Solving Problem 4 with the expert data DE results in the optimal Q-function, and the deterministic rewards can be recovered by: 
r(s, a) = Q(s, a) −γEρE[log X a exp Q(s′, a)], (5) The misalignment problem in recommendation
-> INFO: Found possible citet reference but couldn't really match it: '[2017]'
      -> Sentence: ' Therefore, most existing works focus on optimizing some surrogate objectives such as click-through rate and 
conversion rate Wang et al [2017], Zhou et al [2019]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[2018]'
      -> Sentence: ' Existing works usually model the recommender system as agent, who recommends items and receives user feedback as 
reward Zheng et al [2018], Chen et al [2019]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[2018]'
      -> Sentence: ' Following existing works on sequential recommendation Zhou et al [2018, 2019], Wang-Cheng and McAuley [2018], after 
an user takes an action, a new state st+1 = st ∪{ht+1, it+1} will be generated'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[2018]'
      -> Sentence: ', Wang-Cheng and McAuley [2018], after an user takes an action, a new state st+1 = st ∪{ht+1, it+1} will be generated'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[2007]'
      -> Sentence: 'functions and focus on estimating their posterior distribution using Bayes’ rule Deepak and Amir [2007], Jaedeug and 
Kim [2012]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'log X a exp Q(s′'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a)'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  Since we model the user’s mental reward r as a random variable, Equation 5 can be rephrased using a distributional operator as T 
πr(s, a) : D= Q(s, a) −γEρE[log X a exp Q(s′, a)], where X : D= U denotes equality of probability laws, that is, the random variable X is 
distributed according to the same law as U
-> INFO: Found possible citet reference but couldn't really match it: '[2018]'
      -> Sentence: ' Following the QR-DQN Will et al [2018], the distribution of Q can be characterized by a quantile distribution'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a)'...
-> Warning: Bracket content ['V (s0),'] on p. 6 could not be matched to a reference.
   -> Sentence: , (1 −γ)Es0∼ρ0[V (s0)]) can be replaced by E(s,a)∼ρE[V (s) −γV (s′)]
-> Warning: Bracket content ['V (s0),'] on p. 6 could not be matched to a reference.
   -> Sentence:  In other words, Es0∼ρ0[V (s0)] is irrelevant with the initial state distribution ρ0
-> INFO: Found possible citet reference but couldn't really match it: '[2021]'
      -> Sentence: ' Second, as is suggested in Garg et al [2021], we choose the regularizer as ψ(x) = x − 1 4αx2 for the ease of 
optimization while bounding the rewards'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a) −log X a exp Qλ(s'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a)'...
-> INFO: Found possible citet reference but couldn't really match it: '[(Qλ(s]'
      -> Sentence: ' −1 4αEρE[(Qλ(s, a) −log X a exp Qλ(s′, a))2], (6) We apply the Pinball loss to get the optimal quantile distribution 
supports {λi(s, a)}N i=1 and the optimal Q∗ λ, which we can use to calculate the mental rewards as: r∗(s, a) = Q∗ λ(s, a) −γEρE[log X a 
exp Q∗ λ(s′, a)]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'log X a exp Q∗ λ(s′'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'a)'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  max Qλ EρE[Qλ(s, a) −log X a exp Qλ(s, a)] −1 4αEρE[(Qλ(s, a) −log X a exp Qλ(s′, a))2], (6) We apply the Pinball loss to get the 
optimal quantile distribution supports {λi(s, a)}N i=1 and the optimal Q∗ λ, which we can use to calculate the mental rewards as: r∗(s, a)
= Q∗ λ(s, a) −γEρE[log X a exp Q∗ λ(s′, a)]
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'aP log(Fζ(i|h)) + aN log(1 −Fζ(i|h))'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  Many sequential recommendation tasks are formulated as binary classification problems with the following Cross Entropy loss: LCE(ζ)
= −EDE[aP log(Fζ(i|h)) + aN log(1 −Fζ(i|h))], (8) where aP = 1 and aN = 0 indicate user’s positive and negative responses, and Fζ(i|h) 
represents the estimated probability of clicking on item i based on history h
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'r∗(s'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'aP ) · Fζ(i|h) + r∗(s'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'aN) · (1 −Fζ(i|h))'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  We want the recommendation models to also maximize the expectation of user’s mental rewards, leading to the following alignment 
loss: LAlign(ζ) = −EDE[r∗(s, aP ) · Fζ(i|h) + r∗(s, aN) · (1 −Fζ(i|h))], (9) Then, the final loss for training the recommendation model 
can be written as a weighted combination of the two losses: LF inal(ζ) = LCE(ζ) + κ · LAlign(ζ)
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'it'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'at)'...
-> Warning: Bracket content ['X t ˆr(ht−1,'] on p. 7 could not be matched to a reference.
   -> Sentence:  In this context, Fζ(i|h) represents the RL-based recommendation policy, whose goal is to maximize the expectation of 
accumulated rewards ˆr: LRL(ζ) = −Eit∼Fζ[ X t ˆr(ht−1, it, at)] (11) Since we want the recommendation model to also maximize the mental 
rewards of the user
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'it'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'at) + κ · r∗(ht−1'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'it'...
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'at)'...
-> Warning: Bracket content ['X t ˆr(ht−1,'] on p. 7 could not be matched to a reference.
   -> Sentence:  LF inal(ζ) = −Eit∼Fζ[ X t ˆr(ht−1, it, at) + κ · r∗(ht−1, it, at)] (12) See Appendix A
-> Warning: Bracket content ['Wide&Deep Cheng et al, 2016'] on p. 7 could not be matched to a reference.
   -> Sentence:  Wide&Deep Cheng et al [2016] is a hybrid recommendation model combining a wide linear model and deep neural network for 
collaborative filtering
-> Warning: Bracket content ['PNN Qu et al, 2016'] on p. 7 could not be matched to a reference.
   -> Sentence:  PNN Qu et al [2016] is a neural network architecture designed for CTR prediction in recommender systems
-> Warning: Bracket content ['DeepFM Guo et al, 2017'] on p. 7 could not be matched to a reference.
   -> Sentence:  DeepFM Guo et al [2017] is a hybrid recommendation model combining factorization machines and deep neural networks
-> Warning: Bracket content ['SASRec Wang-Cheng and McAuley, 2018'] on p. 7 could not be matched to a reference.
   -> Sentence:  SASRec Wang-Cheng and McAuley [2018] uses the self-attention mechanism to model sequential patterns for recommendation 
systems
-> Warning: Bracket content ['DIN Zhou et al, 2018'] on p. 7 could not be matched to a reference.
   -> Sentence:  DIN Zhou et al [2018] is an attention-based neural model for sequential recommendation, where the attention mechanism 
aims to distinguish the interest of a user’s historical behaviors
-> Warning: Bracket content ['DIEN Zhou et al, 2019'] on p. 7 could not be matched to a reference.
   -> Sentence:  DIEN Zhou et al [2019] designs a sequential architecture to model interest evolution for recommendation, 7 
-> Warning: Bracket content ['LinRec Liu et al, 2023b'] on p. 8 could not be matched to a reference.
   -> Sentence:  LinRec Liu et al [2023b] is a lightweight linear recommendation model designed for efficient computation and scalability 
with large datasets
-> Warning: Bracket content ['SIGMA Liu et al, 2024'] on p. 8 could not be matched to a reference.
   -> Sentence:  SIGMA Liu et al [2024] is a sequential recommendation model that uses a selective gating mechanism to focus on the most 
relevant user behaviors for improved performance
-> INFO: Found possible citet reference but couldn't really match it: '[2021]'
      -> Sentence: ' The suffix “IRL" indicates that the mental reward model is learned by a nondistributional IRL algorithm IQ-Learn Garg
et al [2021], while the suffix “MTRec" indicates that the mental reward model is learned by our algorithm QR-IQL'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> Warning: Bracket content ['Virtual Taobao Shi et al, 2019'] on p. 8 could not be matched to a reference.
   -> Sentence:  Both training and testing of the algorithms are conducted in simulated interactive recommendation environments on Virtual
Taobao Shi et al [2019]
-> INFO: Found possible citet reference but couldn't really match it: '[2017]'
      -> Sentence: ' The baseline model is a Deep Cross Network (DCN) Wang et al [2017], which is trained using binary labels indicating 
whether the users click on videos'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 471 sentences on 11 pages -> Avg. of 48.1 sentences per page
-> Warning: Reference 'Chen et al, 2021b' never used in the document's text.
-> Warning: Reference 'Cheng et al, 2016' never used in the document's text.
-> Warning: Reference 'Covington et al, 2016' never used in the document's text.
-> Warning: Reference 'Dai et al, 2021' never used in the document's text.
-> Warning: Reference 'Deepak and Amir, 2007' never used in the document's text.
-> Warning: Reference 'Garg et al, 2021' never used in the document's text.
-> Warning: Reference 'Guo et al, 2017' never used in the document's text.
-> Warning: Reference 'Jiawei et al, 2023' never used in the document's text.
-> Warning: Reference 'Kingma and Ba, 2015' never used in the document's text.
-> Warning: Reference 'Liu et al, 2023b' never used in the document's text.
-> Warning: Reference 'Liu et al, 2024' never used in the document's text.
-> Warning: Reference 'Qu et al, 2016' never used in the document's text.
-> Warning: Reference 'Shi et al, 2019' never used in the document's text.
-> Warning: Reference 'Wang et al, 2017' never used in the document's text.
-> Warning: Reference 'Wang-Cheng and McAuley, 2018' never used in the document's text.
-> Warning: Reference 'Will et al, 2018' never used in the document's text.
-> Warning: Reference 'Lee et al, 2021' never used in the document's text.
-> Warning: Reference 'Yu and Qin, 2020' never used in the document's text.
-> Warning: Reference 'Zhou et al, 2018' never used in the document's text.
-> Warning: Reference '1, 0' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = Brian et al, 2008); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = Chen et al, 2021a); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> WARNING: Reference with index 3 (Ref. ID = Chen et al, 2021b) has no associated sentence!
-> Missing an abstract for reference with index 4 (Ref. ID = Cheng et al, 2016); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = Covington et al, 2016); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = Dai et al, 2021); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = Deepak and Amir, 2007); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = Dong et al, 2023); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = Fawcett, 2006); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = Garg et al, 2021); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = Gilotte et al, 2018); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = Guo et al, 2017); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = Haarnoja et al, 2018); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = Jaedeug and Kim, 2012); Skipping LLM check...
-> WARNING: Reference with index 15 (Ref. ID = Jiawei et al, 2023) has no associated sentence!
-> Missing an abstract for reference with index 16 (Ref. ID = Jonathan and Ermon, 2016); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = Kingma and Ba, 2015); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = Liu et al, 2023a); Skipping LLM check...
-> WARNING: Reference with index 19 (Ref. ID = Liu et al, 2023b) has no associated sentence!
-> Missing an abstract for reference with index 20 (Ref. ID = Liu et al, 2024); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = McAuley et al, 2015); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = Ouyang et al, 2022); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = Qu et al, 2016); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 25 (Ref. ID = Schulman et al, 2017); Skipping LLM check...
-> WARNING: Reference with index 26 (Ref. ID = Shi et al, 2019) has no associated sentence!
-> Missing an abstract for reference with index 27 (Ref. ID = Swaminathan and Joachims, 2015); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = Wang et al, 2017); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 30 (Ref. ID = Wang-Cheng and McAuley, 2018); Skipping LLM check...
-> WARNING: Reference with index 31 (Ref. ID = Will et al, 2018) has no associated sentence!
-> WARNING: Reference with index 32 (Ref. ID = Lee et al, 2021) has no associated sentence!
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 34 (Ref. ID = Yi et al, 2023); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = Yu and Qin, 2020); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = Zheng et al, 2018); Skipping LLM check...
-> WARNING: Reference with index 37 (Ref. ID = Zhou et al, 2018) has no associated sentence!
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 39 (Ref. ID = 1, 0); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
...
```