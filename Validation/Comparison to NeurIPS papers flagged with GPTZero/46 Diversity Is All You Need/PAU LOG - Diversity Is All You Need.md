
NOTE: Same referencing template as "When and How"

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\46 Diversity Is All You Need\Diversity Is All You Need for Contrastive Learning Spectral Bounds on Gra.pdf"
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
Enter a supported bibliography layout (['LFTOY', 'LFYTO', 'FLYTO', 'FLTOY']): FLTOY
# PLEASE NOTE:
 -> The chosen bib layout uses ',' to separate multiple authors.
 => If that is correct, please press enter or type 'y', otherwise enter another author-separator to use: 
... Using default :)
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
- Found following heading '2 - Experiments' on page 3
- Found following heading '3 - N −τ 4' on page 6
=> Found references/literature section on page 10
- Found first appendix 'A - Appendix / Supplemental Material' on page 16
- Found following appendix 'B - ImageNet–1k: Effective Rank vs. Accuracy' on page 27
- Found following appendix 'C - Related Work' on page 30
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 16
All found references: 32
-> Warning: Could not parse year in reference 'NeurIPS Paper Checklist 1. Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: The abstract and introduction clearly state the goal of bounding InfoNCE gradient norms via a spectral framework, which is then carried out in the theoretical analysis and validated empirically in Sections 2–4. 2. Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes] Justification: Section A.5 discusses the assumption of batch-level isotropy and explicitly evaluates the degradation of spectral bounds under increasing anisotropy, showing that the method is robust to mild violations but degrades in extreme cases. 3. Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: [Yes] Justification: Assumptions (A1)–(A3) are clearly stated, and the full derivation of the bounds appears in Appendix A.1. A proof sketch is also provided in the main paper for clarity. 4. Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: [Yes] Justification: Sections 4.1–4.6 provide sufficient details on experimental setups, such as datasets, architectures (ResNet-18, ResNet-50), batch sizes, and hyperparameters (e.g., temperature values), to allow replication of all key results. 5. Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? Answer: [No] Justification: While the experiments use standard datasets (ImageNet, CIFAR-10), the code was not released at submission time to preserve anonymity. Code will be released upon acceptance. 6. Experimental setting/details Question: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand the results? Answer: [Yes] Justification: The experimental sections describe data splits, architectures, optimizers, hyperparameters (e.g., learning rates, temperature), and compute budgets, either in the main text or in Appendix A. 7. Experiment statistical significance Question: Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments? Answer: [Yes] Justification: All empirical plots include shaded error bands representing ±1 standard error over multiple seeds (typically 3 or 5), and statistical variations are reported in tables. 8. Experiments compute resources Question: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments? Answer: [Yes] Justification: Sections 4.4 and 4.5 specify compute types (V100, A100 GPUs), training time (e.g., 200 epochs), and approximate runtime overheads (e.g., 18.6 9. Code of ethics Question: Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics [yes]justification: the research involves theoretical analysis and standard benchmark datasets,with no ethical risks identified.10. broader impactsquestion: does the paper discuss both potential positive societal impacts and negativesocietal impacts of the work performed?answer: [yes]justification: while the work is primarily theoretical and does not involve direct deploymentor sensitive data, its findings may influence how contrastive learning is used in large-scaletraining pipelines. a discussion of potential downstream impacts—such as efficiencyimprovements in resource-intensive models or unintended consequences of aggressive batchselection—would strengthen the paper’s ethical reflection. we recommend including a briefbroader impact section in future revisions.11. safeguardsquestion: does the paper describe safeguards that have been put in place for responsiblerelease of data or models that have a high risk for misuse (e.g., pretrained language models,image generators, or scraped datasets)?answer: [na]justification: no high-risk assets are released; the work focuses on contrastive learningtheory and batch selection.12. licenses for existing assetsquestion: are the creators or original owners of assets (e.g., code, data, models), used inthe paper, properly credited and are the license and terms of use explicitly mentioned andproperly respected?answer: [yes]justification: all datasets (imagenet, cifar-10) and methods (simclr, moco) used arecited in the references with proper attribution.13. new assetsquestion: are new assets introduced in the paper well documented and is the documentationprovided alongside the assets?answer: [na]justification: no new datasets or pretrained models are introduced.14. crowdsourcing and research with human subjectsquestion: for crowdsourcing experiments and research with human subjects, does the paperinclude the full text of instructions given to participants and screenshots, if applicable, aswell as details about compensation (if any)?answer: [na]justification: no human subjects or crowdsourcing were involved.15. institutional review board (irb) approvals or equivalent for research with humansubjectsquestion: does the paper describe potential risks incurred by study participants, whethersuch risks were disclosed to the subjects, and whether institutional review board (irb)approvals (or an equivalent approval/review based on the requirements of your country orinstitution) were obtained?answer: [na]justification: the study did not involve human subjects.16. declaration of llm usagequestion: does the paper describe the usage of llms if it is an important, original, ornon-standard component of the core methods in this research?answer: [na]justification: llms were not used in the development or evaluation of the proposed methods.'!
 -> Found dublicated ref_ids:
                                       full_reference           ref_id  ... link valid
3   Xinlei Chen, Haoqi Fan, Ross Girshick, and Kai...  Chen et al 2020  ...       None
11  Kaiming He, Haoqi Fan, Yuxin Wu, Saining Xie, ...    He et al 2020  ...       None

[2 rows x 11 columns]
-----------
 -> Parsed references DataFrame:
                           ref_id  ... valid
0                  Cai et al 2021  ...  None
1                Chen et al 2020a  ...  None
2                Chen and He 2021  ...  None
3                Chen et al 2020b  ...  None
4               Chuang et al 2020  ...  None
5                   Du et al 2021  ...  None
6              Ermolov et al 2021  ...  None
7              Garrido et al 2023  ...  None
8                Grill et al 2020  ...  None
9              Harwood et al 2017  ...  None
10                 He et al 2020a  ...  None
11                 He et al 2020b  ...  None
12                 Hua et al 2021  ...  None
13               Huang et al 2022  ...  None
14                Jing et al 2022  ...  None
15          Kalantidis et al 2020  ...  None
16              Khosla et al 2020  ...  None
17  Koltchinskii and Lounici 2017  ...  None
18         10.3150/15-BEJ730 2017  ...  None
19        10.1214/16-AOS1437 2018  ...  None
20            Robinson et al 2020  ...  None
21            Robinson et al 2021  ...  None
22          Roy and Vetterli 2007  ...  None
23                     Tropp 2015  ...  None
24                 Vershynin 9781  ...  None
25                 Vershynin 2018  ...  None
26            Wang and Isola 2020  ...  None
27                 Wen et al 2021  ...  None
28                  Wu et al 2017  ...  None
29                Zhao et al 2020  ...  None
30     Zimmermann and Geiger 2021  ...  None
31                            1 0  ...  None

[32 rows x 10 columns]
- Checking reference 1/32:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=xYGNO86OWDH
  -> INFO: Now checking 1 results for matching title: 'Isotropy in the contextual embedding space: Clusters and manifolds'
       -> INFO: All authors matched!
- Checking reference 2/32:
  -> INFO: Now checking 5 results for matching title: 'A simple framework for contrastive learning of visual representations'
       -> INFO: All authors matched!
- Checking reference 3/32:
  -> INFO: Now checking 10 results for matching title: 'Exploring simple siamese representation learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/32:
  -> INFO: Now checking 10 results for matching title: 'Improved baselines with momentum contrastive learning'
       -> INFO: All authors matched!
- Checking reference 5/32:
  -> INFO: Now checking 10 results for matching title: 'Debiased contrastive learning'
       -> INFO: All authors matched!
- Checking reference 6/32:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Agree to disagree: Adaptive learning with gradient disagreement
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Du', 'Sener', 'Savarese', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Agree+to+disagree:+Adaptive+learning+with+gradient+disagreement manually and check the results.
        -> Author(s): Qiyang Du, Ozan Sener, and Silvio Savarese
        -> Title:     Agree to disagree: Adaptive learning with gradient disagreement
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 7/32:
  -> Checking if provided link is pingable: https://proceedings.mlr.press/v139/ermolov21a.html
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Whitening for selfsupervised representation learning
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 1 results for matching title: 'Whitening for selfsupervised representation learning'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://proceedings.mlr.press/v139/ermolov21a.html manually and check the results.
        -> Author(s): Aleksandr Ermolov, Aliaksandr Siarohin, Enver Sangineto, and Nicu Sebe
        -> Title:     Whitening for selfsupervised representation learning
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 8/32:
  -> INFO: Now checking 1 results for matching title: 'Rankme: Assessing the downstream performance of pretrained self-supervised representations by their rank'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Balestriero, Najman'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/32:
  -> INFO: Now checking 10 results for matching title: 'Bootstrap your own latent: A new approach to self-supervised learning'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Altch'e'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/32:
  -> INFO: Now checking 10 results for matching title: 'Smart mining for deep metric learning'
       -> INFO: All authors matched!
- Checking reference 11/32:
  -> INFO: Now checking 10 results for matching title: 'Momentum contrast for unsupervised visual representation learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/32:
  -> INFO: Now checking 10 results for matching title: 'Momentum contrast for unsupervised visual representation learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/32:
  -> INFO: Now checking 10 results for matching title: 'On feature decorrelation in self-supervised learning'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Xue, Ren, Zhao'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 14/32:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: The role of supervised learning in the era of foundation models: Boundary and information theoretic perspectives
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 3 results for matching title: 'The role of supervised learning in the era of foundation models: Boundary and information theoretic perspectives'
  -> WARNING: None of the 3 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+role+of+supervised+learning+in+the+era+of+foundation+models:+Boundary+and+information+theoretic+perspectives manually and check the results.
        -> Author(s): Kaizhao Huang, Binghui Li, Zhirong Wu, Mike Wu, Bo Zhao, Jun Zhu, and Saining Xie
        -> Title:     The role of supervised learning in the era of foundation models: Boundary and information theoretic perspectives
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 15/32:
  -> INFO: Now checking 1 results for matching title: 'Understanding contrastive representation learning through alignment and uniformity on the hypersphere'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Jing', 'Tian', 'Pei', 'Shen', 'Feng', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Understanding+contrastive+representation+learning+through+alignment+and+uniformity+on+the+hypersphere manually and check the results.
        -> Author(s): Longxuan Jing, Yu Tian, Yujun Pei, Yibing Shen, and Jiashi Feng
        -> Title:     Understanding contrastive representation learning through alignment and uniformity on the hypersphere
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 16/32:
  -> INFO: Now checking 10 results for matching title: 'Hard negative mixing for contrastive learning'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Sariyildiz, Larlus'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/32:
  -> INFO: Now checking 10 results for matching title: 'Supervised contrastive learning'
       -> INFO: All authors matched!
- Checking reference 18/32:
  -> Checking if provided link is pingable: https://projecteuclid.org/journals/bernoulli/volume-23/issue-1/
  -> INFO: Now checking 2 results for matching title: 'Concentration inequalities and moment bounds for sample covariance operators'
       -> INFO: All authors matched!
       -> WARNING: Year (2014) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 19/32:
  -> Checking if provided link is pingable: https://projecteuclid.org/journals/annals-of-statistics/volume-45/issue-1/
  -> INFO: Now checking 10 results for matching title: 'full'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['10.3150/15-BEJ730', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://projecteuclid.org/journals/annals-of-statistics/volume-45/issue-1/ manually and check the results.
        -> Author(s): Concentration-inequalities-and-moment-bounds-for-sample-covariance-operators/ 10.3150/15-BEJ730
        -> Title:     full
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 20/32:
  -> INFO: Now checking 10 results for matching title: 'full'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['10.1214/16-AOS1437', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=full manually and check the results.
        -> Author(s): Normal-approximation-and-concentration-of-spectral-projectors-of-sample-covariance/ 10.1214/16-AOS1437
        -> Title:     full
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 21/32:
  -> INFO: Now checking 1 results for matching title: 'Learning with curriculum-based sample mining for deep metric learning'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Robinson', 'Chuang', 'Santhanam', 'Jegelka', 'Sra', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Learning+with+curriculum-based+sample+mining+for+deep+metric+learning manually and check the results.
        -> Author(s): Joshua Robinson, Ching-Yao Chuang, Ganesh Santhanam, Stefanie Jegelka, and Suvrit Sra
        -> Title:     Learning with curriculum-based sample mining for deep metric learning
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 22/32:
  -> INFO: Now checking 10 results for matching title: 'Contrastive learning with hard negative samples'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 23/32:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'The effective rank: A measure of effective dimensionality'
       -> INFO: All authors matched!
- Checking reference 24/32:
  -> INFO: Now checking 10 results for matching title: 'An introduction to matrix concentration inequalities'
       -> INFO: All authors matched!
- Checking reference 25/32:
  -> INFO: Now checking 2 results for matching title: 'High-Dimensional Probability: An Introduction with Applications in Data Science'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Vershynin', '9781']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=High-Dimensional+Probability:+An+Introduction+with+Applications+in+Data+Science manually and check the results.
        -> Author(s): Roman Vershynin
        -> Title:     High-Dimensional Probability: An Introduction with Applications in Data Science
        -> Year:      9781
     -> Manual search was skipped by the user.
- Checking reference 26/32:
  -> INFO: Now checking 2 results for matching title: 'High-Dimensional Probability: An Introduction with Applications in Data Science'
  -> WARNING: None of the 2 results matched the expected title!
  -> INFO: Now checking 4 results for matching title: 'High-Dimensional Probability: An Introduction with Applications in Data Science'
  -> WARNING: None of the 4 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=High-Dimensional+Probability:+An+Introduction+with+Applications+in+Data+Science manually and check the results.
        -> Author(s): Roman Vershynin
        -> Title:     High-Dimensional Probability: An Introduction with Applications in Data Science
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 27/32:
  -> INFO: Now checking 1 results for matching title: 'Understanding contrastive representation learning through alignment and uniformity on the hypersphere'
       -> INFO: All authors matched!
- Checking reference 28/32:
  -> INFO: Now checking 5 results for matching title: 'Towards understanding the regularization of contrastive loss'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Wen', 'Vicol', 'Ba', 'Grosse', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Towards+understanding+the+regularization+of+contrastive+loss manually and check the results.
        -> Author(s): Hao Wen, Paul Vicol, Jimmy Ba, and Roger Grosse
        -> Title:     Towards understanding the regularization of contrastive loss
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 29/32:
  -> INFO: Now checking 10 results for matching title: 'Sampling matters in deep embedding learning'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Krähenbühl'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/32:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Maintaining discriminative features in batch normalization for deep face recognition
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 5 results for matching title: 'Maintaining discriminative features in batch normalization for deep face recognition'
  -> WARNING: None of the 5 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Maintaining+discriminative+features+in+batch+normalization+for+deep+face+recognition manually and check the results.
        -> Author(s): Lei Zhao, Shengcai Xie, Yu Gao, and Jinhui Tang
        -> Title:     Maintaining discriminative features in batch normalization for deep face recognition
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 31/32:
  -> INFO: Now checking 10 results for matching title: 'Contrastive learning inverts the data generating process'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Sharma, Schneider, Bethge, Brendel'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 32/32:
  -> Checking if provided link is pingable: https://neurips.cc/public/EthicsGuidelines?Answer:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: The abstract and introduction clearly state the goal of bounding InfoNCE gradient norms via a spectral framework, which is then carried out in the theoretical analysis and validated empirically in Sections 2–4
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 998 results for matching title: 'Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: The abstract and introduction clearly state the goal of bounding InfoNCE gradient norms via a spectral framework, which is then carried out in the theoretical analysis and validated empirically in Sections 2–4'
  -> WARNING: None of the 998 results matched the expected title!
     -> You could also open https://neurips.cc/public/EthicsGuidelines?Answer: manually and check the results.
        -> Author(s): NeurIPS Paper Checklist 1
        -> Title:     Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: The abstract and introduction clearly state the goal of bounding InfoNCE gradient norms via a spectral framework, which is then carried out in the theoretical analysis and validated empirically in Sections 2–4
        -> Year:      0
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 1: Let batch size n > 2 and embedding dimension d. Each embedding zi ∈Sd−1 ⊂Rd has a designated
-> Invalid unicode use found on p. 1: |Si| = n −1, and the negatives
-> Invalid unicode use found on p. 1: as N −
-> Invalid unicode use found on p. 1: |N −
-> Invalid unicode use found on p. 1: i | = n−2. Let Z = [ z1; . . . ; zn ] ∈Rn×d collect rows z⊤
-> Invalid unicode use found on p. 1: i zj ∈[−1, 1] with softmax temperature τ > 0.
-> Invalid unicode use found on p. 1: n−1
-> Invalid unicode use found on p. 1: ˜Σ−
-> Invalid unicode use found on p. 1: n−2
-> Invalid unicode use found on p. 1: j∈N −
-> Invalid unicode use found on p. 1: unit norms, tr(ˆΣ) = tr(˜Σi) = tr(˜Σ−
-> Invalid unicode use found on p. 1: n−1
-> Invalid unicode use found on p. 1: ˆΣ −1
-> Invalid unicode use found on p. 1: ˜Σ−
-> Invalid unicode use found on p. 1: n−2
-> Invalid unicode use found on p. 1: ˆΣ −1
-> Invalid unicode use found on p. 1: n −1 λmax(ˆΣ),
-> Invalid unicode use found on p. 1: λmax(˜Σ−
-> Invalid unicode use found on p. 1: n −2 λmax(ˆΣ).
-> Invalid unicode use found on p. 1: := λmax(˜Σ−
-> Invalid unicode use found on p. 1: Let N −=n−2, ˜Σ−
-> Invalid unicode use found on p. 1: N −
-> Invalid unicode use found on p. 1: j∈N −
-> Invalid unicode use found on p. 1: := λmax(˜Σ−
-> Invalid unicode use found on p. 1: unit norms and the Löwner order, ˜Σ−
-> Invalid unicode use found on p. 1: N−
-> Invalid unicode use found on p. 1: nˆΣ−ziz⊤
-> Invalid unicode use found on p. 1: i −zi+z⊤
-> Invalid unicode use found on p. 1: n−2 ˆΣ ⇒σ(i)
-> Invalid unicode use found on p. 1: n−2 ˆσ, where
-> Invalid unicode use found on p. 1: i and ˆσ = λmax(ˆΣ). InfoNCE: Li = −log pii+ with pij ∝esij/τ, sij = z⊤
-> Invalid unicode use found on p. 1: ϵi := 1 −pii+, and Mi = P
-> Invalid unicode use found on p. 1: k pikzk so ∇ziLi = τ −1(Mi −zi+). Expectations are over the
-> Invalid unicode use found on p. 1: i ] + E[(1−pii+)2]
-> Invalid unicode use found on p. 1: N−
-> Invalid unicode use found on p. 1: + 3 E[(1 −pii+)2] σ∗
-> Invalid unicode use found on p. 1: + 3c E[(1 −pii+)2] σ2
-> Invalid unicode use found on p. 1: ≥(1 −ρ)2
-> Invalid unicode use found on p. 1: Decompose δi := Mi −zi+ = Ai + Bi + Ci with Ai = −ϵizi+, Bi = (1 −pii+)¯z−
-> Invalid unicode use found on p. 1: ¯z−
-> Invalid unicode use found on p. 1: N −
-> Invalid unicode use found on p. 1: j∈N −
-> Invalid unicode use found on p. 1: i zj, and Ci = (1 −pii+) P
-> Invalid unicode use found on p. 1: j(qij −
-> Invalid unicode use found on p. 1: N −)zj where qij = pij/(1 −pii+). Then
-> Invalid unicode use found on p. 1: i ], E∥Bi∥2 = E[(1 −pii+)2]/N −by (A2),
-> Invalid unicode use found on p. 1: ∥2 ≤τ −2E[(1 −pii+)2]σ∗and E∥C(2)
-> Invalid unicode use found on p. 1: ∥2 ≤c τ −4E[(1 −pii+)2]σ2
-> Invalid unicode use found on p. 1: ∥Mi∥≤1 implies ∥Mi −zi+∥2 ≥(1 −⟨Mi, zi+⟩)2; apply Jensen. Full details in App. A.1.
-> Invalid unicode use found on p. 1: n−2 ˆσ gives
-> Invalid unicode use found on p. 1: n−2λmax(ˆΣ);
-> Invalid unicode use found on p. 1: Softmax error ϵi and the sampling term 1/N −set a baseline that decays with batch
-> Invalid unicode use found on p. 1: size. Anisotropy enters via σ∗at orders τ −4 and τ −6; pushing toward isotropy (e.g., larger Reff,
-> Invalid unicode use found on p. 1: whitening) tightens the ceiling. Higher alignment ρ shrinks the floor (1 −ρ)2/τ 2 without implying
-> Invalid unicode use found on p. 2: = λmax(˜Σ−
-> Invalid unicode use found on p. 2: with ˜Σ−
-> Invalid unicode use found on p. 2: N−
-> Invalid unicode use found on p. 2: j∈N −
-> Invalid unicode use found on p. 2: j , N −= n −2. Computing σ(i)
-> Invalid unicode use found on p. 2: ˜Σ−
-> Invalid unicode use found on p. 2: N −
-> Invalid unicode use found on p. 2: nˆΣ −ziz⊤
-> Invalid unicode use found on p. 2: i −zi+z⊤
-> Invalid unicode use found on p. 2: n−2 ˆΣ ⇒σ(i)
-> Invalid unicode use found on p. 2: n−2 ˆσ,
-> Invalid unicode use found on p. 2: −1 (eigs λk of ˆΣ). Since P
-> Invalid unicode use found on p. 2: (higher variance risk); P3 (balanced) picks arg minm |R(m) −R⋆| with R⋆set by running 10th/90th
-> Invalid unicode use found on p. 2: B∪{z})−tB = 2b (qB(z) −tB) + (1 −tB)
-> Invalid unicode use found on p. 2: maximizing the Frobenius diversity ∆F (z | B) = ∥ΣB −zz⊤∥2
-> Invalid unicode use found on p. 2: F = tB −2qB(z) + 1.
-> Invalid unicode use found on p. 3: 1 −ρ 2gen u⊥, where u⊥is a random unit
-> Invalid unicode use found on p. 3: i zj, softmax weights pij over {i+} ∪N −
-> Invalid unicode use found on p. 3: j pijzj, and gi = τ −1(Mi −zi+).
-> Invalid unicode use found on p. 3: ˜Σ−
-> Invalid unicode use found on p. 3: N−
-> Invalid unicode use found on p. 3: j∈N −
-> Invalid unicode use found on p. 3: N −=n−2,
-> Invalid unicode use found on p. 3: := λmax(˜Σ−
-> Invalid unicode use found on p. 3: i ] + E[(1 −pii+)2]
-> Invalid unicode use found on p. 3: N −
-> Invalid unicode use found on p. 3: + O(τ −4) + O(τ −6),
-> Invalid unicode use found on p. 3: where the prefactor depends on the softmax weights p through ϵi = 1 −pii+. When relative logit
-> Invalid unicode use found on p. 4: 1 −c2 u⊥with u⊥⊥zi. We sweep
-> Invalid unicode use found on p. 4: τ 2 ∥Mi −z+
-> Invalid unicode use found on p. 4: per τ. Orange line: fitted slope; green dashed: 1/τ 2 prediction. Higher–order O(τ −4) and O(τ −6)
-> Invalid unicode use found on p. 4: i(1 −pii+)2.
-> Invalid unicode use found on p. 4: From the per-sample lower bound ∥gi,t∥2 ≥(1 −ρi,t)2/τ 2 we obtain, by
-> Invalid unicode use found on p. 4: (1−ρi,t)2
-> Invalid unicode use found on p. 4: (1−¯ρt)2
-> Invalid unicode use found on p. 4: n −2 ˆσt,
-> Invalid unicode use found on p. 5: (cf. §1.3). This yields a conservative ceiling UBt that includes the τ −4 and τ −6 terms from the
-> Invalid unicode use found on p. 5: with α=0.10; log scale), lower bound LBt = (1 −¯ρt)2/τ 2 (black, dashed), and upper bound UBt
-> Invalid unicode use found on p. 5: from Thm. 1.1 (red). The upper bound uses the negatives-only form with N −=n−2 and the batchlevel spectrum proxy σ(i)
-> Invalid unicode use found on p. 5: n−2 ˆσt, where ˆσt = λmax(ˆΣt) and ˆΣt = 1
-> Invalid unicode use found on p. 5: only the orange curve is EMA-smoothed. We set csm = 0.5 in the τ −6 term (results are qualitatively
-> Invalid unicode use found on p. 5: for the sampling term 1/N −. With correlated negatives, this term inflates and UBt becomes more
-> Invalid unicode use found on p. 5: conservative; spectral contributions via ˆσt are unaffected. As a robustness check, replacing 1/N −by
-> Invalid unicode use found on p. 5: N −; 1
-> Invalid unicode use found on p. 5: ¯z−
-> Invalid unicode use found on p. 5: ¯z−
-> Invalid unicode use found on p. 5: N −
-> Invalid unicode use found on p. 5: j∈N −
-> Invalid unicode use found on p. 5: N −τ 4
-> Invalid unicode use found on p. 5: 1 −
-> Invalid unicode use found on p. 5: N −
-> Invalid unicode use found on p. 5: A(N −,τ)
-> Invalid unicode use found on p. 5: N −:= n −2,
-> Invalid unicode use found on p. 5: where ˜Σ−
-> Invalid unicode use found on p. 5: N−
-> Invalid unicode use found on p. 5: j∈N −
-> Invalid unicode use found on p. 5: j and σ∗:= E[λmax(˜Σ−
-> Invalid unicode use found on p. 5: N −E[ϵ2
-> Invalid unicode use found on p. 5: ϵi := 1 −pii+.
-> Invalid unicode use found on p. 5: 2Derivation in App. A.7. Independence is only used to identify the 1/N −sampling term; see also App. A.4.
-> Invalid unicode use found on p. 6: λmax(˜Σ−
-> Invalid unicode use found on p. 6: n −2 ˆσt,
-> Invalid unicode use found on p. 6: the leading term A(N −, τ) σ∗in (V) shrinks by roughly a factor d (the factor n/(n−2) ≈1 for large
-> Invalid unicode use found on p. 6: For n=4096 (N −=4094) and τ=0.1,
-> Invalid unicode use found on p. 6: A(N −, τ) =
-> Invalid unicode use found on p. 6: 1 −
-> Invalid unicode use found on p. 6: ˆzi = Σ−1/2
-> Invalid unicode use found on p. 6: 1 + (n−1) ¯ργ
-> Invalid unicode use found on p. 6: 1. Independence. Negatives-only independence is invoked only for the 1/N −factors in A(N −, τ)
-> Invalid unicode use found on p. 6: N−
-> Invalid unicode use found on p. 6: by the empirical ∥¯z−
-> Invalid unicode use found on p. 6: 2. Softmax dependence on τ. Both A and Bτ depend on τ via ϵi = 1 −pii+. In our toggles pii+ is
-> Invalid unicode use found on p. 15: Let zi ∈Sd−1 ⊂Rd be the anchor and zi+ its positive. Define the set
-> Invalid unicode use found on p. 15: of others Si := {1, . . . , n} \ {i} and the negatives-only set N −
-> Invalid unicode use found on p. 15: := Si \ {i+} with size N −:= n −2.
-> Invalid unicode use found on p. 15: Li = −log
-> Invalid unicode use found on p. 15: k∈{i+}∪N −
-> Invalid unicode use found on p. 15: i zj ∈[−1, 1], τ > 0,
-> Invalid unicode use found on p. 15: k∈{i+}∪N −
-> Invalid unicode use found on p. 15: i exp(sik/τ) and positive-miss ϵi := 1 −pii+.
-> Invalid unicode use found on p. 15: ˜Σ−
-> Invalid unicode use found on p. 15: N−
-> Invalid unicode use found on p. 15: j∈N −
-> Invalid unicode use found on p. 15: := λmax(˜Σ−
-> Invalid unicode use found on p. 15: Under unit norms, tr ˆΣ = tr ˜Σ−
-> Invalid unicode use found on p. 15: (A2) Zero mean & negatives-only independence: E[z] = 0; for j ∈N −
-> Invalid unicode use found on p. 15: ˜Σ−
-> Invalid unicode use found on p. 15: N −
-> Invalid unicode use found on p. 15: nˆΣ−ziz⊤
-> Invalid unicode use found on p. 15: i −zi+z⊤
-> Invalid unicode use found on p. 15: n −2
-> Invalid unicode use found on p. 15: n −2 ˆσ, ˆσ := λmax(ˆΣ). (4)
-> Invalid unicode use found on p. 15: k∈{i+}∪N −
-> Invalid unicode use found on p. 15: pikzk −zi+
-> Invalid unicode use found on p. 15: τ (Mi −zi+) ≡1
-> Invalid unicode use found on p. 15: so ∥∇ziLi∥2 = τ −2∥δi∥2.
-> Invalid unicode use found on p. 15: 1−pii+ for j ∈N −
-> Invalid unicode use found on p. 15: j∈N −
-> Invalid unicode use found on p. 15: i qij = 1) and ¯z−
-> Invalid unicode use found on p. 15: N−
-> Invalid unicode use found on p. 15: j∈N −
-> Invalid unicode use found on p. 15: δi = (pii+ −1)zi+ + (1 −pii+)
-> Invalid unicode use found on p. 15: j∈N −
-> Invalid unicode use found on p. 15: Ai := −ϵizi+,
-> Invalid unicode use found on p. 15: Bi := (1 −pii+) ¯z−
-> Invalid unicode use found on p. 15: Ci := (1 −pii+)
-> Invalid unicode use found on p. 15: j∈N −
-> Invalid unicode use found on p. 15: qij −
-> Invalid unicode use found on p. 15: N −
-> Invalid unicode use found on p. 15: (B) Sampling noise. By (A2), E∥¯z−
-> Invalid unicode use found on p. 15: N−, hence
-> Invalid unicode use found on p. 15: N −E[(1 −pii+)2].
-> Invalid unicode use found on p. 16: E∥¯z−
-> Invalid unicode use found on p. 16: N −+ N −−1
-> Invalid unicode use found on p. 16: N −
-> Invalid unicode use found on p. 16: (C) Adaptive fluctuations. Linearizing the negatives-only softmax around uniform logits on N −
-> Invalid unicode use found on p. 16: qij −
-> Invalid unicode use found on p. 16: N −= sij−¯s−
-> Invalid unicode use found on p. 16: N−τ
-> Invalid unicode use found on p. 16: ¯s−
-> Invalid unicode use found on p. 16: N −
-> Invalid unicode use found on p. 16: j∈N −
-> Invalid unicode use found on p. 16: (1 −pii+)2 σ(i)
-> Invalid unicode use found on p. 16: (1 −pii+)2 (σ(i)
-> Invalid unicode use found on p. 16: i ] + E[(1 −pii+)2]
-> Invalid unicode use found on p. 16: N −
-> Invalid unicode use found on p. 16: (1 −pii+)2 σ(i)
-> Invalid unicode use found on p. 16: (1 −pii+)2 (σ(i)
-> Invalid unicode use found on p. 16: i ] + E[(1 −pii+)2]
-> Invalid unicode use found on p. 16: N −
-> Invalid unicode use found on p. 16: + 3 E[(1 −pii+)2] (n/(n −2)) ˆσ
-> Invalid unicode use found on p. 16: + 3csm E[(1 −pii+)2] (n/(n −2))2ˆσ2
-> Invalid unicode use found on p. 16: ∥Mi −zi+∥2 = ∥Mi∥2 + 1 −2⟨Mi, zi+⟩≥(1 −⟨Mi, zi+⟩)2.
-> Invalid unicode use found on p. 16: 2 ≥(1 −ρ)2
-> Invalid unicode use found on p. 16: positive-miss (ϵi), finite-sample noise (1/N −), batch anisotropy (via σ(i)
-> Invalid unicode use found on p. 16: (i) Independence vs. correlation. Assumption (A2) is used only to obtain E∥¯z−
-> Invalid unicode use found on p. 16: 1/N −for the sampling term; with correlated negatives this term inflates as in the remark in Step 5(B),
-> Invalid unicode use found on p. 17: There exists a universal constant C > 0 such that, with probability at least 1 −δ,
-> Invalid unicode use found on p. 17: ∥ˆΣ −Σ∥2 ≤C κ2
-> Invalid unicode use found on p. 17: tr ˆΣ −1
-> Invalid unicode use found on p. 17: with probability at least 1 −δ,
-> Invalid unicode use found on p. 17: w.p. ≥1 −δ,
-> Invalid unicode use found on p. 17: ∥ˆΣ −Σ∥2 ≲κ2
-> Invalid unicode use found on p. 17: over N −
-> Invalid unicode use found on p. 17: i with logits ℓij := sij/τ and ¯ℓ−
-> Invalid unicode use found on p. 17: N−
-> Invalid unicode use found on p. 17: j∈N −
-> Invalid unicode use found on p. 17: i ℓij. Then, for each anchor i and j ∈N −
-> Invalid unicode use found on p. 17: qij −
-> Invalid unicode use found on p. 17: N−=
-> Invalid unicode use found on p. 17: ℓij−¯ℓ−
-> Invalid unicode use found on p. 17: N−
-> Invalid unicode use found on p. 17: 8 (ℓij −¯ℓ−
-> Invalid unicode use found on p. 17: Equivalently, in vector form, with Π := I −
-> Invalid unicode use found on p. 17: N−11⊤,
-> Invalid unicode use found on p. 17: qi −
-> Invalid unicode use found on p. 17: N−1 =
-> Invalid unicode use found on p. 17: N−Π ℓi + eRi,
-> Invalid unicode use found on p. 17: := 1−pii+
-> Invalid unicode use found on p. 17: N−τ
-> Invalid unicode use found on p. 17: j∈N −
-> Invalid unicode use found on p. 17: i (sij −¯s−
-> Invalid unicode use found on p. 17: (1 −pii+) P
-> Invalid unicode use found on p. 17: j∈N −
-> Invalid unicode use found on p. 17: (1 −pii+)2 σ(i)
-> Invalid unicode use found on p. 17: (1 −pii+)2 (σ(i)
-> Invalid unicode use found on p. 17: = λmax(˜Σ−
-> Invalid unicode use found on p. 17: and Varj∈N −
-> Invalid unicode use found on p. 17: i ˜Σ−
-> Invalid unicode use found on p. 17: j(ℓij −¯ℓ−
-> Invalid unicode use found on p. 17: τ 2 N −σ(i)
-> Invalid unicode use found on p. 18: E∥¯z−
-> Invalid unicode use found on p. 18: Let N −
-> Invalid unicode use found on p. 18: i be the negatives for anchor i, N −:= |N −
-> Invalid unicode use found on p. 18: i |, and ¯z−
-> Invalid unicode use found on p. 18: N −
-> Invalid unicode use found on p. 18: j∈N −
-> Invalid unicode use found on p. 18: N −(N −−1)
-> Invalid unicode use found on p. 18: j,k∈N −
-> Invalid unicode use found on p. 18: E∥¯z−
-> Invalid unicode use found on p. 18: N −+ N −−1
-> Invalid unicode use found on p. 18: N −
-> Invalid unicode use found on p. 18: E∥Bi∥2 = E[(1 −pii+)2]
-> Invalid unicode use found on p. 18: N −+ N −−1
-> Invalid unicode use found on p. 18: N −
-> Invalid unicode use found on p. 18: Relative to the independent case, the sampling term is inflated by a factor 1 + (N −−1)µcorr.
-> Invalid unicode use found on p. 18: Proof. Expand ∥¯z−
-> Invalid unicode use found on p. 18: (N −)2
-> Invalid unicode use found on p. 18: N −(N −−1)
-> Invalid unicode use found on p. 18: E∥¯z−
-> Invalid unicode use found on p. 18: N −+ N −−1
-> Invalid unicode use found on p. 18: N −
-> Invalid unicode use found on p. 18: model: zj ∝√α u + √1 −α ξj with u ∼Unif(Sd−1), ξj
-> Invalid unicode use found on p. 18: norm. This yields µcorr ≈α in high dimension. We sweep α ∈[0, 0.1], N −∈{62, 254, 1022},
-> Invalid unicode use found on p. 18: d = 256, τ = 0.1 and, for each batch, check coverage of ∥gi∥2 between the lower bound (1−ρi)2
-> Invalid unicode use found on p. 18: over all negative pairs in N −
-> Invalid unicode use found on p. 18: 1 + (N −−1)¯µcorr remains close to 1 for N −≤1024. Our coverage checks in §A.11 match this
-> Invalid unicode use found on p. 19: if |R −R⋆| < ∆⋆then
-> Invalid unicode use found on p. 19: ∆⋆←|R −R⋆|,
-> Invalid unicode use found on p. 19: −tB = 2b (qB(z) −tB) + (1 −tB)
-> Invalid unicode use found on p. 20: qB(z) −tB
-> Invalid unicode use found on p. 20: + O(b−2).
-> Invalid unicode use found on p. 20: −tB = 2b (qB(z) −tB) + (1 −tB)
-> Invalid unicode use found on p. 20: qB(z) < tB −1 −tB
-> Invalid unicode use found on p. 20: Define ∆F (z | B) := ∥ΣB −zz⊤∥2
-> Invalid unicode use found on p. 20: B) −2 z⊤ΣBz +
-> Invalid unicode use found on p. 20: The score ∆(z | B) := 1 −⟨z, ¯zB⟩with ¯zB = 1
-> Invalid unicode use found on p. 21: We bound Var(γi) with γi := ∥∇ziLi∥2. Recall ∇ziLi = τ −1δi, δi := Mi−zi+, and the decomposition δi = Ai+Bi+Ci with Ai = −ϵizi+, Bi = (1−pii+) ¯z−
-> Invalid unicode use found on p. 21: i , Ci = (1−pii+) P
-> Invalid unicode use found on p. 21: j∈N −
-> Invalid unicode use found on p. 21: i (qij−
-> Invalid unicode use found on p. 21: N −)zj
-> Invalid unicode use found on p. 21: γi = τ −2∥δi∥2 ≤
-> Invalid unicode use found on p. 21: (B) Sampling term. Under negatives-only independence (A2), ¯z−
-> Invalid unicode use found on p. 21: N −
-> Invalid unicode use found on p. 21: j∈N −
-> Invalid unicode use found on p. 21: i zj has E∥¯z−
-> Invalid unicode use found on p. 21: 1/N −and Var(∥¯z−
-> Invalid unicode use found on p. 21: N−
-> Invalid unicode use found on p. 21: 1 −
-> Invalid unicode use found on p. 21: N−
-> Invalid unicode use found on p. 21: Var(∥Bi∥2) ≤E[(1 −pii+)4] Var(∥¯z−
-> Invalid unicode use found on p. 21: 1 −
-> Invalid unicode use found on p. 21: N −
-> Invalid unicode use found on p. 21: N −E[(1 −pii+)2].
-> Invalid unicode use found on p. 21: τ 2 E[(1 −pii+)2 σ(i)
-> Invalid unicode use found on p. 21: τ 4 E[(1 −pii+)2 (σ(i)
-> Invalid unicode use found on p. 21: Combining (A)–(C) and the τ −2 prefactor yields
-> Invalid unicode use found on p. 21: N −τ 4
-> Invalid unicode use found on p. 21: 1 −
-> Invalid unicode use found on p. 21: N −
-> Invalid unicode use found on p. 21: A(N −,τ)
-> Invalid unicode use found on p. 21: with σ∗:= E[λmax(˜Σ−
-> Invalid unicode use found on p. 21: N−E[ϵ2
-> Invalid unicode use found on p. 21: τ −2E[(1 −pii+)2σ∗]
-> Invalid unicode use found on p. 21: τ −4E[(1 −pii+)2σ2
-> Invalid unicode use found on p. 21: . A deterministic proxy follows from λmax(˜Σ−
-> Invalid unicode use found on p. 21: n−2 ˆσ (cf. §1.3).
-> Invalid unicode use found on p. 21: ϵi := 1 −pii+,
-> Invalid unicode use found on p. 21: N −:= n −2.
-> Invalid unicode use found on p. 21: N−
-> Invalid unicode use found on p. 21: j∈N −
-> Invalid unicode use found on p. 21: N −
-> Invalid unicode use found on p. 21: where c > 0 is a softmax smoothness constant controlling the τ −6 remainder.
-> Invalid unicode use found on p. 21: n −2 ˆσ
-> Invalid unicode use found on p. 21: N −
-> Invalid unicode use found on p. 21: n −2 ˆσ + 3c ϵ2
-> Invalid unicode use found on p. 21: n −2
-> Invalid unicode use found on p. 22: δt = 100 · ∥Σt −1
-> Invalid unicode use found on p. 22: Σt −1
-> Invalid unicode use found on p. 22: dI∥F = d−1/2.
-> Invalid unicode use found on p. 22: N −
-> Invalid unicode use found on p. 22: N −= n −2.
-> Invalid unicode use found on p. 22: n −2 ˆσ.
-> Invalid unicode use found on p. 23:  (1−ρi)2
-> Invalid unicode use found on p. 23: d ∥Σ−1
-> Invalid unicode use found on p. 23: n−2 ˆσ
-> Invalid unicode use found on p. 23: (notably the τ −6σ2
-> Invalid unicode use found on p. 24: with probability ≥1 −δ,
-> Invalid unicode use found on p. 24: bΣQ −Σ⋆
-> Invalid unicode use found on p. 24: = λmax(˜Σ−
-> Invalid unicode use found on p. 25: Augmentation strength scales the color-jitter and blur coefficients by −50%, 0% (default), or +50%;
-> Invalid unicode use found on p. 25: Random−Greedy
-> Invalid unicode use found on p. 25: Weak (−50%)
-> Invalid unicode use found on p. 25: ∥∇ziLi∥2 ≥(1 −ρi)2
-> Invalid unicode use found on p. 25: ∥∇ziLi∥≥1 −ρi
-> Invalid unicode use found on p. 26: approximately linearly in 1 −˜ρ; beyond ˜ρ ≳0.8 they are effectively vanishing, consistent with the
-> Invalid unicode use found on p. 26: gradient magnitudes roughly in proportion to 1−ρ, hindering optimisation. Inequality (11) quantifies
-> Invalid unicode use found on p. 27: Lemma B.2. Let the mini-batch satisfy (A1)–(A3) and use the negatives-only set N −
-> Invalid unicode use found on p. 27: of size N −=n−2. With the notation of Step 7, the softmax Taylor remainder satisfies
-> Invalid unicode use found on p. 27: ≤(sij −¯s−
-> Invalid unicode use found on p. 27: 2N −τ 2
-> Invalid unicode use found on p. 27: ¯s−
-> Invalid unicode use found on p. 27: N−
-> Invalid unicode use found on p. 27: j∈N −
-> Invalid unicode use found on p. 27: := (1 −pii+)
-> Invalid unicode use found on p. 27: j∈N −
-> Invalid unicode use found on p. 27: (sij −¯s−
-> Invalid unicode use found on p. 27: N −τ 4 E
-> Invalid unicode use found on p. 27: (1 −pii+)2
-> Invalid unicode use found on p. 28: 2 ≤N −P
-> Invalid unicode use found on p. 28: j with aj := (1 −
-> Invalid unicode use found on p. 28: ∥2 ≤N −E
-> Invalid unicode use found on p. 28: j = N −E
-> Invalid unicode use found on p. 28: (1 −pii+)2 X
-> Invalid unicode use found on p. 28: Using | eRij| ≤(sij −¯s−
-> Invalid unicode use found on p. 28: i )2/(2N −τ 2),
-> Invalid unicode use found on p. 28: 4(N −)2τ 4
-> Invalid unicode use found on p. 28: (sij −¯s−
-> Invalid unicode use found on p. 28: j(sij −¯s−
-> Invalid unicode use found on p. 28: i )4 ≤N −C4 σ2
-> Invalid unicode use found on p. 28: ∥2 ≤N −· E[(1 −pii+)2] ·
-> Invalid unicode use found on p. 28: 4(N −)2τ 4 · N −C4 σ2
-> Invalid unicode use found on p. 28: E[(1 −pii+)2] σ2
-> Invalid unicode use found on p. 28: N −τ 4
-> Invalid unicode use found on p. 28: ∥2 ≤E[(1 −pii+)2]σ∗/τ 2, Lemma B.2 justifies the ˜O
-> Invalid unicode use found on p. 28: E[(1 −
-> Invalid unicode use found on p. 28: ∗/(N −τ 4)
-> Invalid unicode use found on p. 28: −11%
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Couldn't parse in-text (sub) reference '(high anisotropy)' in bracket 'high anisotropy; low effective rank' on
p. 1!
-> Couldn't parse in-text (sub) reference '( low effective rank)' in bracket 'high anisotropy; low effective 
rank' on p. 1!
-> Warning: Bracket content 'NeurIPS 2025' on p. 2 could not be matched to a reference.
   -> Sentence:  ∗Accepted as a Poster at the 39th Conference on Neural Information Processing Systems (NeurIPS 
2025) 39th Conference on Neural Information Processing Systems (NeurIPS 2025)
-> Skipping possible_ref_id '1/d 1' since it's shorter than 6 chars and/or the last four chars are not all digits
(missing year).
-> Skipping possible_ref_id '1 −⟨Mi zi+⟩' since it's shorter than 6 chars and/or the last four chars are not all 
digits (missing year).
-> Skipping possible_ref_id 'Σ2 B∪{z}) = b2tB + 2b qB(z) + 1 (b + 1)2 ⇒ ∆t := tr(Σ2 B∪{z})−tB = 2b (qB(z' since 
it's shorter than 6 chars and/or the last four chars are not all digits (missing year).
-> Couldn't parse in-text references '(['initial seeds', ' Gram maintenance', ' streaming'])' in bracket on p. 3!
-> Skipping possible_ref_id '0 Id' since it's shorter than 6 chars and/or the last four chars are not all digits 
(missing year).
-> Warning: Bracket content 'batch size n=256, dimension d=1024' on p. 5 could not be matched to a reference.
   -> Sentence:  For each setting we generate 10,000 batches (batch size n=256, dimension d=1024)
-> Skipping possible_ref_id 'per-anchor no expectation' since it's shorter than 6 chars and/or the last four 
chars are not all digits (missing year).
-> Skipping possible_ref_id 'all cosines including a fixed anchor–positive cosine' since it's shorter than 6 
chars and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'embeddings are ℓ2normalized so tr ˆΣt = 1' since it's shorter than 6 chars and/or 
the last four chars are not all digits (missing year).
-> Skipping possible_ref_id '1 −ρi t' since it's shorter than 6 chars and/or the last four chars are not all 
digits (missing year).
-> Skipping possible_ref_id '1−ρi t' since it's shorter than 6 chars and/or the last four chars are not all 
digits (missing year).
-> Skipping possible_ref_id 'LBt UBt' since it's shorter than 6 chars and/or the last four chars are not all 
digits (missing year).
-> Skipping possible_ref_id 'results are qualitatively insensitive for csm ∈[0 1' since it's shorter than 6 chars
and/or the last four chars are not all digits (missing year).
-> Skipping possible_ref_id 'LBt UBt' since it's shorter than 6 chars and/or the last four chars are not all 
digits (missing year).
-> Skipping possible_ref_id 'N − τ' since it's shorter than 6 chars and/or the last four chars are not all digits
(missing year).
-> Skipping possible_ref_id 'N − τ' since it's shorter than 6 chars and/or the last four chars are not all digits
(missing year).
-> Skipping possible_ref_id 'N − τ' since it's shorter than 6 chars and/or the last four chars are not all digits
(missing year).
-> Skipping possible_ref_id 'N − τ' since it's shorter than 6 chars and/or the last four chars are not all digits
(missing year).
-> Skipping possible_ref_id 'N − τ' since it's shorter than 6 chars and/or the last four chars are not all digits
(missing year).
-> Couldn't parse in-text (sub) reference '(lower is better)' in bracket 'lower is better; computed over all 200 
epochs' on p. 8!
-> Couldn't parse in-text (sub) reference '( computed over all 200 epochs)' in bracket 'lower is better; computed
over all 200 epochs' on p. 8!
-> Couldn't parse in-text (sub) reference '(thick = seed mean)' in bracket 'thick = seed mean; faint = individual
seeds' on p. 8!
-> Couldn't parse in-text (sub) reference '( faint = individual seeds)' in bracket 'thick = seed mean; faint = 
individual seeds' on p. 8!
-> Skipping possible_ref_id 'equivalently minimize tr(Σ2 B)' since it's shorter than 6 chars and/or the last four
chars are not all digits (missing year).
-> Couldn't parse in-text references '(['captured by ˆσ', ' σ(i) ∗', ' with Reff as a practical proxy'])' in 
bracket on p. 10!
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 441 sentences on 10 pages -> Avg. of 50.0 sentences per page
-> Warning: Reference 'Cai et al 2021' never used in the document's text.
-> Warning: Reference 'Chen and He 2021' never used in the document's text.
-> Warning: Reference 'Chen et al 2020b' never used in the document's text.
-> Warning: Reference 'Chuang et al 2020' never used in the document's text.
-> Warning: Reference 'Du et al 2021' never used in the document's text.
-> Warning: Reference 'Ermolov et al 2021' never used in the document's text.
-> Warning: Reference 'Garrido et al 2023' never used in the document's text.
-> Warning: Reference 'Grill et al 2020' never used in the document's text.
-> Warning: Reference 'Harwood et al 2017' never used in the document's text.
-> Warning: Reference 'He et al 2020a' never used in the document's text.
-> Warning: Reference 'Hua et al 2021' never used in the document's text.
-> Warning: Reference 'Huang et al 2022' never used in the document's text.
-> Warning: Reference 'Jing et al 2022' never used in the document's text.
-> Warning: Reference 'Kalantidis et al 2020' never used in the document's text.
-> Warning: Reference 'Khosla et al 2020' never used in the document's text.
-> Warning: Reference 'Koltchinskii and Lounici 2017' never used in the document's text.
-> Warning: Reference '10.3150/15-BEJ730 2017' never used in the document's text.
-> Warning: Reference '10.1214/16-AOS1437 2018' never used in the document's text.
-> Warning: Reference 'Robinson et al 2020' never used in the document's text.
-> Warning: Reference 'Robinson et al 2021' never used in the document's text.
-> Warning: Reference 'Roy and Vetterli 2007' never used in the document's text.
-> Warning: Reference 'Tropp 2015' never used in the document's text.
-> Warning: Reference 'Vershynin 9781' never used in the document's text.
-> Warning: Reference 'Vershynin 2018' never used in the document's text.
-> Warning: Reference 'Wang and Isola 2020' never used in the document's text.
-> Warning: Reference 'Wen et al 2021' never used in the document's text.
-> Warning: Reference 'Wu et al 2017' never used in the document's text.
-> Warning: Reference 'Zhao et al 2020' never used in the document's text.
-> Warning: Reference 'Zimmermann and Geiger 2021' never used in the document's text.
-> Warning: Reference '1 0' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = Cai et al 2021); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = Chen et al 2020a); Skipping LLM check...
-> WARNING: Reference with index 2 (Ref. ID = Chen and He 2021) has no associated sentence!
-> Missing an abstract for reference with index 3 (Ref. ID = Chen et al 2020b); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = Chuang et al 2020); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = Du et al 2021); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = Ermolov et al 2021); Skipping LLM check...
-> WARNING: Reference with index 7 (Ref. ID = Garrido et al 2023) has no associated sentence!
-> WARNING: Reference with index 8 (Ref. ID = Grill et al 2020) has no associated sentence!
-> Missing an abstract for reference with index 9 (Ref. ID = Harwood et al 2017); Skipping LLM check...
-> WARNING: Reference with index 10 (Ref. ID = He et al 2020a) has no associated sentence!
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> WARNING: Reference with index 12 (Ref. ID = Hua et al 2021) has no associated sentence!
-> Missing an abstract for reference with index 13 (Ref. ID = Huang et al 2022); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = Jing et al 2022); Skipping LLM check...
-> WARNING: Reference with index 15 (Ref. ID = Kalantidis et al 2020) has no associated sentence!
-> Missing an abstract for reference with index 16 (Ref. ID = Khosla et al 2020); Skipping LLM check...
-> WARNING: Reference with index 17 (Ref. ID = Koltchinskii and Lounici 2017) has no associated sentence!
-> Missing an abstract for reference with index 18 (Ref. ID = 10.3150/15-BEJ730 2017); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 10.1214/16-AOS1437 2018); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = Robinson et al 2020); Skipping LLM check...
-> WARNING: Reference with index 21 (Ref. ID = Robinson et al 2021) has no associated sentence!
-> Missing an abstract for reference with index 22 (Ref. ID = Roy and Vetterli 2007); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = Tropp 2015); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = Vershynin 9781); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = Vershynin 2018); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = Wang and Isola 2020); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = Wen et al 2021); Skipping LLM check...
-> WARNING: Reference with index 28 (Ref. ID = Wu et al 2017) has no associated sentence!
-> Missing an abstract for reference with index 29 (Ref. ID = Zhao et al 2020); Skipping LLM check...
-> WARNING: Reference with index 30 (Ref. ID = Zimmermann and Geiger 2021) has no associated sentence!
-> Missing an abstract for reference with index 31 (Ref. ID = 1 0); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 5 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 2
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 3
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 4
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 5
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━  90% 0:00:03
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 6
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━  90% 0:00:03
###############################
# Starting Author Check
###############################
-> Saved chapter_fig on try 1
-> Saved lit_fig on try 1
-> Saved rank_fig on try 1
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\46 Diversity Is All You Need\PAU_results.md
```