
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\27 A Unified Stability Analysis\A Unified Stability Analysis of SAM vs SGD.pdf"
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
 - 'authoryear_round'  = Authors' names and the year places insince round brackets (e.g., (Dignum et al., 2025))
                      -> Multiple references are separated by a semicolon (e.g., (Dignum et al. 2025; Caliskan et al. 2017))
                      -> Please note that the author and year are *not* separated
 - 'authoryear_square' = Authors' names and the year places insince square brackets (e.g., [Dignum et al., 2025])
                      -> Multiple references are separated by a comma (e.g., [Dignum et al., 2025, Caliskan et al., 2017])
                      -> Please note that the author and year are also separated by a comma
Enter a supported referencing template (['numeric', 'authoryear_round', 'authoryear_square']): authoryear_square
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Background' on page 3
- Found following heading '3 - Main Results' on page 4
- Found following heading '4 - Experiments' on page 8
=> Found references/literature section on page 10
- Found first appendix 'A - More discussion on limitation and practical implication' on page 19
- Found following appendix 'B - Related Work' on page 20
- Found following appendix 'C - Appendix – Experiments and Proofs' on page 22
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 19
All found references: 40
-> Warning: Could not parse year in reference 'NeurIPS Paper Checklist The checklist is designed to encourage best practices for responsible machine learning research, addressing issues of reproducibility, transparency, research ethics, and societal impact. Do not remove the checklist: The papers not including the checklist will be desk rejected. The checklist should follow the references and follow the (optional) supplemental material. The checklist does NOT count towards the page limit. Please read the checklist guidelines carefully for information on how to answer these questions. For each question in the checklist: • You should answer [Yes] , [No] , or [NA] . • [NA] means either that the question is Not Applicable for that particular paper or the relevant information is Not Available. • Please provide a short (1–2 sentence) justification right after your answer (even for NA). The checklist answers are an integral part of your paper submission. They are visible to the reviewers, area chairs, senior area chairs, and ethics reviewers. You will be asked to also include it (after eventual revisions) with the final version of your paper, and its final version will be published with the paper. The reviewers of your paper will be asked to use the checklist as one of the factors in their evaluation. While ”[Yes] ” is generally preferable to ”[No] ”, it is perfectly acceptable to answer ”[No] ” provided a proper justification is given (e.g., ”error bars are not reported because it would be too computationally expensive” or ”we were unable to find the license for the dataset we used”). In general, answering ”[No] ” or ”[NA] ” is not grounds for rejection. While the questions are phrased in a binary way, we acknowledge that the true answer is often more nuanced, so please just use your best judgment and write a justification to elaborate. All supporting evidence can appear either in the main paper or the supplemental material, provided in appendix. If you answer [Yes] to a question, in the justification please point to the section(s) where related material for the question can be found. IMPORTANT, please: • Delete this instruction block, but keep the section heading “NeurIPS Paper Checklist”, • Keep the checklist subsection headings, questions/answers and guidelines below. • Do not modify the questions and only use the provided macros for your answers. 1. Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: see main context and abstract Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper. • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers. • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper. 2. Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes] Justification: See the limitation of the paper at the end Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate ”Limitations” section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. • The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. • The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations. 3. Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: [Yes] Justification: See proof in appendix C.9, C.11, C.13, C.7 and theory section Guidelines: • The answer NA means that the paper does not include theoretical results. • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced. • All assumptions should be clearly stated or referenced in the statement of any theorems. • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. • Theorems and Lemmas that the proof relies upon should be properly referenced. 4. Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: [Yes] Justification: See experiment section in main context and details in section C.5, C.3, C.4 Guidelines: • The answer NA means that the paper does not include experiments. • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. • Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results. 5. Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? Answer: [No] Justification: Will provide code in camera ready version once accpeted Guidelines: • The answer NA means that paper does not include experiments requiring code. • Please see the NeurIPS code and data submission guidelines ('!
-> Warning: Malformed author string: 'transparency'
 -> Found dublicated ref_ids:
                                       full_reference            ref_id  ...                                         link valid
9   Z. Chen, J. Zhang, Y. Kou, X. Chen, C.-J. Hsie...  Chen et al, 2023  ...  https://openreview.net/forum?id=3WAnGWLpSQ.  None
33  K. Wen, T. Ma, and Z. Li. How does sharpness-a...   Wen et al, 2023  ...            https://arxiv.org/abs/2211.05729.  None

[2 rows x 11 columns]
-----------
 -> Parsed references DataFrame:
                                 ref_id  ... valid
0                    Achour et al, 2024  ...  None
1   Andriushchenko and Flammarion, 2022  ...  None
2            Andriushchenko et al, 2023  ...  None
3                     Arpit et al, 2017  ...  None
4                          Bhatia, 2013  ...  None
5                     Bisla et al, 2022  ...  None
6                      Chatterjee, 2020  ...  None
7             Chen and Flammarion, 2022  ...  None
8                     Chen et al, 2023a  ...  None
9                     Chen et al, 2023b  ...  None
10                   Dexter et al, 2024  ...  None
11                     Dinh et al, 2017  ...  None
12                       Du et al, 2022  ...  None
13                    Foret et al, 2021  ...  None
14                Gunasekar et al, 2018  ...  None
15                    Hardt et al, 2016  ...  None
16     Hochreiter and Schmidhuber, 1997  ...  None
17                    Jiang et al, 2020  ...  None
18                Kalimeris et al, 2019  ...  None
19                   Keskar et al, 2017  ...  None
20                   Khanna et al, 2018  ...  None
21                     Kwon et al, 2021  ...  None
22                       Li et al, 2018  ...  None
23                     Lyu and Li, 2019  ...  None
24                    Ma and Ying, 2021  ...  None
25                  Morwani et al, 2023  ...  None
26                   Papyan et al, 2020  ...  None
27             Sankararaman et al, 2020  ...  None
28                     Shah et al, 2020  ...  None
29                   Soudry et al, 2018  ...  None
30                 Springer et al, 2024  ...  None
31              Valle-Pérez et al, 2019  ...  None
32                     Wen et al, 2023a  ...  None
33                     Wen et al, 2023b  ...  None
34                      Wu and Su, 2023  ...  None
35                      Wu and Ma, 2018  ...  None
36                       Wu et al, 2022  ...  None
37                    Zhang et al, 2024  ...  None
38                     Zhou et al, 2025  ...  None
39                    research et al, 0  ...  None

[40 rows x 10 columns]
- Checking reference 1/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2107.13289.
  -> INFO: Now checking 4 results for matching title: 'The loss landscape of deep linear neural networks: a second-order analysis.'
  -> WARNING: None of the 4 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'The loss landscape of deep linear neural networks: a second-order analysis.'
       -> INFO: All authors matched!
- Checking reference 2/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2206.06232.
  -> INFO: Now checking 10 results for matching title: 'Towards understanding sharpness-aware minimization.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 7 results for matching title: 'Towards understanding sharpness-aware minimization.'
       -> INFO: All authors matched!
- Checking reference 3/40:
  -> INFO: Now checking 3 results for matching title: 'Sharpness-aware minimization leads to low-rank features'
       -> INFO: All authors matched!
- Checking reference 4/40:
  -> INFO: Now checking 1 results for matching title: 'A closer look at memorization in deep networks'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 5/40:
  -> INFO: Now checking 10 results for matching title: 'Matrix analysis, volume 169'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 69 results for matching title: 'Matrix analysis, volume 169'
  -> WARNING: None of the 69 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Matrix+analysis%2C+volume+169 manually and check the results.
        -> Author(s): R  Bhatia
        -> Title:     Matrix analysis, volume 169
        -> Year:      2013
     -> Manual search was skipped by the user.
- Checking reference 6/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2201.08025.
  -> INFO: Now checking 1 results for matching title: 'Low-pass filtering sgd for recovering flat optima in the deep learning optimization landscape.'
  -> WARNING: None of the 1 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Bisla', 'Wang', 'Choromanska', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Low-pass+filtering+sgd+for+recovering+flat+optima+in+the+deep+learning+optimization+landscape. manually and check the results.
        -> Author(s): D  Bisla, J  Wang, and A  Choromanska
        -> Title:     Low-pass filtering sgd for recovering flat optima in the deep learning optimization landscape.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 7/40:
  -> INFO: Now checking 1 results for matching title: 'Coherent gradients: An approach to understanding generalization in gradient descentbased optimization'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chatterjee', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Coherent+gradients:+An+approach+to+understanding+generalization+in+gradient+descentbased+optimization manually and check the results.
        -> Author(s): S  Chatterjee
        -> Title:     Coherent gradients: An approach to understanding generalization in gradient descentbased optimization
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 8/40:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: When and why sam generalizes better: An optimization perspective
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chen', 'Flammarion', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=When+and+why+sam+generalizes+better:+An+optimization+perspective manually and check the results.
        -> Author(s): Z  Chen and N  Flammarion
        -> Title:     When and why sam generalizes better: An optimization perspective
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 9/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2310.07269.
  -> INFO: Now checking 10 results for matching title: 'Hsieh, and Q  Gu'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chen', 'Zhang', 'Kou', 'Chen', '-J', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Hsieh%2C+and+Q++Gu manually and check the results.
        -> Author(s): Z  Chen, J  Zhang, Y  Kou, X  Chen, C -J
        -> Title:     Hsieh, and Q  Gu
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 10/40:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=3WAnGWLpSQ.
  -> INFO: Now checking 10 results for matching title: 'Hsieh, and Q  Gu'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chen', 'Zhang', 'Kou', 'Chen', '-J', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://openreview.net/forum?id=3WAnGWLpSQ. manually and check the results.
        -> Author(s): Z  Chen, J  Zhang, Y  Kou, X  Chen, C -J
        -> Title:     Hsieh, and Q  Gu
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 11/40:
  -> INFO: Now checking 1 results for matching title: 'A precise characterization of sgd stability using loss surface geometry'
       -> INFO: All authors matched!
- Checking reference 12/40:
  -> INFO: Now checking 10 results for matching title: 'Sharp minima can generalize for deep nets'
       -> INFO: All authors matched!
- Checking reference 13/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2110.03141.
  -> INFO: Now checking 10 results for matching title: 'Efficient sharpness-aware minimization for improved training of neural networks.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Du', 'Yan', 'Feng', 'Zhou', 'Zhen', 'Goh', 'Tan', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Efficient+sharpness-aware+minimization+for+improved+training+of+neural+networks. manually and check the results.
        -> Author(s): J  Du, H  Yan, J  Feng, J  T  Zhou, L  Zhen, R  S  M  Goh, and V  Y  F  Tan
        -> Title:     Efficient sharpness-aware minimization for improved training of neural networks.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 14/40:
  -> INFO: Now checking 10 results for matching title: 'Sharpness-aware minimization for efficiently improving generalization'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 15/40:
  -> INFO: Now checking 10 results for matching title: 'Implicit regularization in matrix factorization'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/40:
  -> INFO: Now checking 10 results for matching title: 'Train faster, generalize better: Stability of stochastic gradient descent'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/40:
  -> INFO: Now checking 10 results for matching title: 'Flat minima'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hochreiter', 'Schmidhuber', '1997']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Flat+minima manually and check the results.
        -> Author(s): S  Hochreiter and J  Schmidhuber
        -> Title:     Flat minima
        -> Year:      1997
     -> Manual search was skipped by the user.
- Checking reference 18/40:
  -> INFO: Now checking 2 results for matching title: 'Fantastic generalization measures and where to find them'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 19/40:
  -> INFO: Now checking 3 results for matching title: 'Sgd on neural networks learns functions of increasing complexity'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Nakkiran, Kaplun, Yang, Edelman, Zhang, Barak'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/40:
  -> INFO: Now checking 4 results for matching title: 'On large-batch training for deep learning: Generalization gap and sharp minima'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 5)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 21/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1810.10118.
  -> INFO: Now checking 10 results for matching title: 'Interpreting black box predictions using fisher kernels.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Interpreting black box predictions using fisher kernels.'
       -> INFO: All authors matched!
- Checking reference 22/40:
  -> INFO: Now checking 1 results for matching title: 'Asam: Adaptive sharpness-aware minimization for scale-invariant learning of deep neural networks'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Park, Choi'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 23/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/1712.09913.
  -> INFO: Now checking 1 results for matching title: 'Visualizing the loss landscape of neural nets.'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Visualizing the loss landscape of neural nets.'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 3)
                   Unmatched authors = '0022, 0002'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 24/40:
  -> INFO: Now checking 4 results for matching title: 'Gradient descent maximizes the margin of homogeneous neural networks'
       -> INFO: All authors matched!
- Checking reference 25/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2105.13462.
  -> INFO: Now checking 1 results for matching title: 'On linear stability of sgd and input-smoothness of neural networks.'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 793 results for matching title: 'On linear stability of sgd and input-smoothness of neural networks.'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0012'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/40:
  -> INFO: Now checking 10 results for matching title: 'Simplicity bias in 1-hidden layer neural networks'
       -> INFO: All authors matched!
- Checking reference 27/40:
  -> INFO: Now checking 1 results for matching title: 'Prevalence of neural collapse during the terminal phase of deep learning training'
       -> INFO: All authors matched!
- Checking reference 28/40:
  -> INFO: Now checking 3 results for matching title: 'The impact of neural network overparameterization on gradient confusion and stochastic gradient descent'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Xu, Huang, Goldstein'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/40:
  -> INFO: Now checking 3 results for matching title: 'The pitfalls of simplicity bias in neural networks'
       -> INFO: All authors matched!
- Checking reference 30/40:
  -> INFO: Now checking 3 results for matching title: 'The implicit bias of gradient descent on separable data'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 4)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/40:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=3xDaj4pRna.
  -> INFO: Now checking 10 results for matching title: 'Sharpness-aware minimization enhances feature quality via balanced learning'
       -> INFO: All authors matched!
- Checking reference 32/40:
  -> INFO: Now checking 1 results for matching title: 'Deep learning generalizes because the parameterfunction map is biased towards simple functions'
  -> WARNING: None of the 1 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Valle-Pérez', 'Camargo', 'Louis', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+learning+generalizes+because+the+parameterfunction+map+is+biased+towards+simple+functions manually and check the results.
        -> Author(s): G  Valle-Pérez, C  Q  Camargo, and A  A  Louis
        -> Title:     Deep learning generalizes because the parameterfunction map is biased towards simple functions
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 33/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2307.11007.
  -> INFO: Now checking 10 results for matching title: 'Sharpness minimization algorithms do not only minimize sharpness to achieve better generalization.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wen', 'Li', 'Ma', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Sharpness+minimization+algorithms+do+not+only+minimize+sharpness+to+achieve+better+generalization. manually and check the results.
        -> Author(s): K  Wen, Z  Li, and T  Ma
        -> Title:     Sharpness minimization algorithms do not only minimize sharpness to achieve better generalization.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 34/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2211.05729.
  -> INFO: Now checking 10 results for matching title: 'How does sharpness-aware minimization minimize sharpness?.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wen', 'Ma', 'Li', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=How+does+sharpness-aware+minimization+minimize+sharpness?. manually and check the results.
        -> Author(s): K  Wen, T  Ma, and Z  Li
        -> Title:     How does sharpness-aware minimization minimize sharpness?.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 35/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2305.17490.
  -> INFO: Now checking 1 results for matching title: 'The implicit regularization of dynamical stability in stochastic gradient descent.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'Su', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+implicit+regularization+of+dynamical+stability+in+stochastic+gradient+descent. manually and check the results.
        -> Author(s): L  Wu and W  J  Su
        -> Title:     The implicit regularization of dynamical stability in stochastic gradient descent.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 36/40:
  -> INFO: Now checking 4 results for matching title: 'How sgd selects the global minima in over-parameterized learning: A dynamical stability perspective'
       -> WARNING: Not all 1 authors from the found ref. were matched (only 1)
                   Unmatched authors = ''
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 37/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2207.02628.
  -> INFO: Now checking 1 results for matching title: 'The alignment property of sgd noise and how it helps select flat minima: A stability analysis.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', 'Wang', 'Su', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+alignment+property+of+sgd+noise+and+how+it+helps+select+flat+minima:+A+stability+analysis. manually and check the results.
        -> Author(s): L  Wu, M  Wang, and W  Su
        -> Title:     The alignment property of sgd noise and how it helps select flat minima: A stability analysis.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 38/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2402.15152.
  -> INFO: Now checking 1 results for matching title: 'On the duality between sharpness-aware minimization and adversarial training.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'He', 'Zhu', 'Chen', 'Wang', 'Wei', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=On+the+duality+between+sharpness-aware+minimization+and+adversarial+training. manually and check the results.
        -> Author(s): Y  Zhang, H  He, J  Zhu, H  Chen, Y  Wang, and Z  Wei
        -> Title:     On the duality between sharpness-aware minimization and adversarial training.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 39/40:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2410.10373.
  -> INFO: Now checking 1 results for matching title: 'Sharpness-aware minimization efficiently selects flatter minima late in training.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhou', 'Wang', 'Mao', 'Li', 'Yan', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Sharpness-aware+minimization+efficiently+selects+flatter+minima+late+in+training. manually and check the results.
        -> Author(s): Z  Zhou, M  Wang, Y  Mao, B  Li, and J  Yan
        -> Title:     Sharpness-aware minimization efficiently selects flatter minima late in training.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 40/40:
  -> Checking if provided link is pingable: https://nips.cc/public/guides/CodeSubmissionPolicy)
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Do not remove the checklist: The papers not including the checklist will be desk rejected
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['research', 'reproducibility', 'transparency', 'ethics', 'impact', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Do+not+remove+the+checklist:+The+papers+not+including+the+checklist+will+be+desk+rejected manually and check the results.
        -> Author(s): NeurIPS Paper Checklist The checklist is designed to encourage best practices for responsible machine learning research, addressing issues of reproducibility, transparency, research ethics, and societal impact
        -> Title:     Do not remove the checklist: The papers not including the checklist will be desk rejected
        -> Year:      0
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: model parameters w ∈Rd, and suppose w⋆is a local minimum. Let δt = wt−w⋆be the perturbation
-> Invalid unicode use found on p. 2: since ∇L(w⋆) = 0. For a generic optimization algorithm with update rule wt+1 = wt −ηgt, the
-> Invalid unicode use found on p. 2: δt+1 = (I −ηHt)δt,
-> Invalid unicode use found on p. 2: wt+1 = wt −ηHtwt = (I −ηHt)wt = ˆJtwt,
-> Invalid unicode use found on p. 3: wt+1 = wt −η∇Sl(w + δt)
-> Invalid unicode use found on p. 3: = wt −ηHtwt −ηHtδt
-> Invalid unicode use found on p. 3: b −1)−1
-> Invalid unicode use found on p. 4: wt+1 = wt −η∇Sl(wt + ρ ∇l(wt)
-> Invalid unicode use found on p. 4: = (I −ηHt(I +
-> Invalid unicode use found on p. 4: I −ηHt
-> Invalid unicode use found on p. 4: B −1
-> Invalid unicode use found on p. 4: −1/2 
-> Invalid unicode use found on p. 4: −1
-> Invalid unicode use found on p. 4: i ≤2 −ϵ
-> Invalid unicode use found on p. 5: B −1)−1,
-> Invalid unicode use found on p. 5: x ∈{−1, 1}d are drawn i.i.d. and labels are generated y = x[0]x[1], ensuring that both simple and
-> Invalid unicode use found on p. 6: W1,j = r · [(−1)a1, (−1)a2, . . . , (−1)aC, 0, . . . , 0],
-> Invalid unicode use found on p. 6: with j indexing a binary encoding of the ai’s i.e. j = 1 + P 2i−1ai. We set W2[j] = 1
-> Invalid unicode use found on p. 6: r(−1)a1+a2
-> Invalid unicode use found on p. 6: probability at least 1−δ, for a randomly drawn dataset of size n, the top eigenvalue of the coherence
-> Invalid unicode use found on p. 7: 2c −1
-> Invalid unicode use found on p. 21: jth row of W1 be W1,j = r[(−1)a1, (−1)a2, ...(−1)aC, 0, 0, ...0], with j = 1+P 2i−1ai. Similarly,
-> Invalid unicode use found on p. 21: let b[j] = −r(C −1). We set W2[j] = 1
-> Invalid unicode use found on p. 21: r(−1)a1+a2. For k > C, W1,k = 0, W2[k] = 0, b[k] = 0.
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 21: −1
-> Invalid unicode use found on p. 22: −1
-> Invalid unicode use found on p. 22: −1
-> Invalid unicode use found on p. 22: −1
-> Invalid unicode use found on p. 22: −1
-> Invalid unicode use found on p. 23: 1 for all i ∈[σ] and Hi = mei−σ+1eT
-> Invalid unicode use found on p. 23: i−σ+1 otherwise. We use m = 2n
-> Invalid unicode use found on p. 25: n −1
-> Invalid unicode use found on p. 25: k −1
-> Invalid unicode use found on p. 25: n −1
-> Invalid unicode use found on p. 25: b −1)−1
-> Invalid unicode use found on p. 25: wk = ˆJk... ˆJ1w0 −η
-> Invalid unicode use found on p. 25: k wk] = E[( ˆJk... ˆJ1w0 −η
-> Invalid unicode use found on p. 25: Jt′)Htδt)T ( ˆJk... ˆJ1w0 −η
-> Invalid unicode use found on p. 26: Bn −1
-> Invalid unicode use found on p. 26: b −1)tλmax(H)2t)
-> Invalid unicode use found on p. 26: b −1)λmax(H)2 to be larger than 1. i.e.,
-> Invalid unicode use found on p. 26: b −1)−1
-> Invalid unicode use found on p. 26: b −1)tλ2t
-> Invalid unicode use found on p. 26: b −1)(( η
-> Invalid unicode use found on p. 26: b −1)k −1)
-> Invalid unicode use found on p. 26: b −1) −1
-> Invalid unicode use found on p. 26: C0αt = C0α(αk −1)
-> Invalid unicode use found on p. 26: α −1
-> Invalid unicode use found on p. 26: b −1) to be r and the overall lower bound
-> Invalid unicode use found on p. 26: min(C0α(αk −1)
-> Invalid unicode use found on p. 26: α −1
-> Invalid unicode use found on p. 26: r(rk −1)
-> Invalid unicode use found on p. 26: r −1
-> Invalid unicode use found on p. 27: α −1
-> Invalid unicode use found on p. 27: r −1
-> Invalid unicode use found on p. 27: 1... ˆJk] ≤C((1 −ϵ)2 + ϵ)k. Here, we temporarily denote ((1 −ϵ)2 + ϵ) to be r. We apply
-> Invalid unicode use found on p. 27: r(1 −rk)
-> Invalid unicode use found on p. 27: 1 −r
-> Invalid unicode use found on p. 27: 1 −r
-> Invalid unicode use found on p. 28: Wt+1 = (I −ηHt(I + ρ
-> Invalid unicode use found on p. 28: Define ˆJt = (I −ηHt(I + ρ
-> Invalid unicode use found on p. 28: Bn −1
-> Invalid unicode use found on p. 28: Bn −1
-> Invalid unicode use found on p. 28: B −1)k(1 + ρ
-> Invalid unicode use found on p. 28: B −1)−1
-> Invalid unicode use found on p. 28: αλmin(H))−1
-> Invalid unicode use found on p. 28: T ˆJ1] = E[(I −ηHt(I + ρ
-> Invalid unicode use found on p. 28: α)H)T (I −ηHt(I + ρ
-> Invalid unicode use found on p. 28: = E[I −2ηHt −ηρ
-> Invalid unicode use found on p. 28: = I −2ηH −2ηρ
-> Invalid unicode use found on p. 28: Bn −1
-> Invalid unicode use found on p. 28: Bn −1
-> Invalid unicode use found on p. 29: T Mk−1 ˆJk]
-> Invalid unicode use found on p. 29: = E[(I −ηHk −ηρ
-> Invalid unicode use found on p. 29: α HkH)T Mk−1(I −ηHk −ηρ
-> Invalid unicode use found on p. 29: = E[Mk−1 −ηMk−1Hk −ηρ
-> Invalid unicode use found on p. 29: α Mk−1HkH −ηHkMk−1 + η2HkMk−1Hk + η2ρ
-> Invalid unicode use found on p. 29: α HkMk−1HkH−
-> Invalid unicode use found on p. 29: α HHkMk−1 + η2ρ
-> Invalid unicode use found on p. 29: α HHkMk−1Hk + η2ρ2
-> Invalid unicode use found on p. 29: α2 HHkMk−1HkH]
-> Invalid unicode use found on p. 29: = JMk−1J + η2( 1
-> Invalid unicode use found on p. 29: nB −1
-> Invalid unicode use found on p. 29: HiMk−1Hi)(I + ρ
-> Invalid unicode use found on p. 29: Now, we subsititude the expression of Mk−1 into the expression and we will have the follows:
-> Invalid unicode use found on p. 29: T ˆJ1... ˆJk] ⪰JMk−1J + η2( 1
-> Invalid unicode use found on p. 29: nB −1
-> Invalid unicode use found on p. 29: HiMk−1Hi)(I + ρ
-> Invalid unicode use found on p. 29: = J[J2(k−1) + η2(k−1)( 1
-> Invalid unicode use found on p. 29: Bn −1
-> Invalid unicode use found on p. 29: n2 )(k−1)
-> Invalid unicode use found on p. 29: αH)Hyk−1...(I + ρ
-> Invalid unicode use found on p. 29: αH)...Hyk−1(I + ρ
-> Invalid unicode use found on p. 29: nB −1
-> Invalid unicode use found on p. 29: Hi[J2(k−1)+
-> Invalid unicode use found on p. 29: η2(k−1)( 1
-> Invalid unicode use found on p. 29: Bn −1
-> Invalid unicode use found on p. 29: n2 )(k−1)
-> Invalid unicode use found on p. 29: αH)Hyk−1...(I + ρ
-> Invalid unicode use found on p. 29: αH)...Hyk−1(I + ρ
-> Invalid unicode use found on p. 29: Bn −1
-> Invalid unicode use found on p. 29: Bn −1
-> Invalid unicode use found on p. 29: αH)Hyk−1...(I + ρ
-> Invalid unicode use found on p. 29: αH)...Hyk−1(I + ρ
-> Invalid unicode use found on p. 29: αλmin(H))3 Tr[Hyk−1...(I + ρ
-> Invalid unicode use found on p. 29: αH)...Hyk−1(I + ρ
-> Invalid unicode use found on p. 29: αλmin(H))4 Tr[Hyk−1H2
-> Invalid unicode use found on p. 29: ykHyk−1(I + ρ
-> Invalid unicode use found on p. 30: Bn −1
-> Invalid unicode use found on p. 30: Bn −1
-> Invalid unicode use found on p. 30: Bn −1
-> Invalid unicode use found on p. 30: Bn −1
-> Invalid unicode use found on p. 30: Bn −1
-> Invalid unicode use found on p. 30: Bn −1
-> Invalid unicode use found on p. 30: Bn −1
-> Invalid unicode use found on p. 30: Bn −1
-> Invalid unicode use found on p. 30: Bn −1
-> Invalid unicode use found on p. 30: B −1)k(1 + ρ
-> Invalid unicode use found on p. 30: B −1)k(1 + ρ
-> Invalid unicode use found on p. 30: B −1)−1
-> Invalid unicode use found on p. 30: αλmin(H))−1
-> Invalid unicode use found on p. 31: Wt+1 = (I −ηHt(I + ρ
-> Invalid unicode use found on p. 31: (1 −ϵ)2(k−r)
-> Invalid unicode use found on p. 31: nB −1
-> Invalid unicode use found on p. 31: B −1
-> Invalid unicode use found on p. 31: i ≤2 −ϵ
-> Invalid unicode use found on p. 31: nB −1
-> Invalid unicode use found on p. 31: nB −1
-> Invalid unicode use found on p. 31: (1 −ϵ)2(k−r)
-> Invalid unicode use found on p. 31: 1 ˆJ1] = E[(I −η ˆH −ηρ
-> Invalid unicode use found on p. 31: ˆHH)T (I −η ˆH −ηρ
-> Invalid unicode use found on p. 31: nB −1
-> Invalid unicode use found on p. 31: ⪯(1 −ϵ)2N0 + N1
-> Invalid unicode use found on p. 31: The first condition (1 −ϵ)2I is achieved when the condition of the assumption is satisfied. We
-> Invalid unicode use found on p. 31: J = I −ηH(I + ρ
-> Invalid unicode use found on p. 32: −(1 −ϵ)2I ⪯J2 ⪯(1 −ϵ)2I
-> Invalid unicode use found on p. 32: J2 ⪯(1 −ϵ)2I
-> Invalid unicode use found on p. 32: (I −ηH(I + ρ
-> Invalid unicode use found on p. 32: αH))2 ⪯(1 −ϵ)2I
-> Invalid unicode use found on p. 32: (I −ηH(I + ρ
-> Invalid unicode use found on p. 32: αH)) ⪯(1 −ϵ)I
-> Invalid unicode use found on p. 32: i ≤2 −ϵ
-> Invalid unicode use found on p. 32: Compared to SGD, the ϵ can be larger as the term I −ηH is larger than I −ηH −η ρ
-> Invalid unicode use found on p. 32: k−1
-> Invalid unicode use found on p. 32: (1 −ϵ)2(k−1−r)
-> Invalid unicode use found on p. 32: k −1
-> Invalid unicode use found on p. 32: k−1
-> Invalid unicode use found on p. 32: (1 −ϵ)2(k−1−r)
-> Invalid unicode use found on p. 32: k −1
-> Invalid unicode use found on p. 32: nb −1
-> Invalid unicode use found on p. 32: k−1
-> Invalid unicode use found on p. 32: (1 −ϵ)2(k−1−r)
-> Invalid unicode use found on p. 32: k −1
-> Invalid unicode use found on p. 32: ⪯(1 −ϵ)2
-> Invalid unicode use found on p. 32: k−1
-> Invalid unicode use found on p. 32: (1 −ϵ)2(k−1−r)
-> Invalid unicode use found on p. 32: k −1
-> Invalid unicode use found on p. 32: nb −1
-> Invalid unicode use found on p. 32: k−1
-> Invalid unicode use found on p. 32: (1 −ϵ)2(k−1−r)
-> Invalid unicode use found on p. 32: k −1
-> Invalid unicode use found on p. 32: k−1
-> Invalid unicode use found on p. 32: (1 −ϵ)2(k−r)
-> Invalid unicode use found on p. 32: k −1
-> Invalid unicode use found on p. 32: nb −1
-> Invalid unicode use found on p. 32: k−1
-> Invalid unicode use found on p. 32: (1 −ϵ)2(k−1−r)
-> Invalid unicode use found on p. 32: k −1
-> Invalid unicode use found on p. 32: k−1
-> Invalid unicode use found on p. 32: (1 −ϵ)2(k−r)
-> Invalid unicode use found on p. 32: k −1
-> Invalid unicode use found on p. 32: k−1
-> Invalid unicode use found on p. 32: (1 −ϵ)2(k−1−r)
-> Invalid unicode use found on p. 32: k −1
-> Invalid unicode use found on p. 33: k−1
-> Invalid unicode use found on p. 33: (1 −ϵ)2(k−r)
-> Invalid unicode use found on p. 33: k −1
-> Invalid unicode use found on p. 33: (1 −ϵ)2(k−r)
-> Invalid unicode use found on p. 33: k −1
-> Invalid unicode use found on p. 33: r −1
-> Invalid unicode use found on p. 33: = (1 −ϵ)2kN0 +
-> Invalid unicode use found on p. 33: k−1
-> Invalid unicode use found on p. 33: ((1 −ϵ)2(k−r)
-> Invalid unicode use found on p. 33: k −1
-> Invalid unicode use found on p. 33: + (1 −ϵ)2(k−r)
-> Invalid unicode use found on p. 33: k −1
-> Invalid unicode use found on p. 33: r −1
-> Invalid unicode use found on p. 33: (1 −ϵ)2(k−r)
-> Invalid unicode use found on p. 33: (1 −ϵ)2(k−r)
-> Invalid unicode use found on p. 33: (1 −ϵ)2(k−r)ϵr
-> Invalid unicode use found on p. 33: = C((1 −ϵ)2 + ϵ)k
-> Invalid unicode use found on p. 34: nB −1
-> Invalid unicode use found on p. 34: nB −1
-> Invalid unicode use found on p. 34: nB −1
-> Invalid unicode use found on p. 34: B −1
-> Invalid unicode use found on p. 34: B −1
-> Invalid unicode use found on p. 34: B −1
-> Invalid unicode use found on p. 34: B −1
-> Invalid unicode use found on p. 35: Xj ≥u + ϵ) ≤exp(−2ϵn2) ≤exp(−(C + log 1
-> Invalid unicode use found on p. 35: δ )) = e−Cδ
-> Invalid unicode use found on p. 35: e−Cδ
-> Invalid unicode use found on p. 36: 2c −
-> Invalid unicode use found on p. 36: 2c −1
-> Invalid unicode use found on p. 36: 2c −1
-> Invalid unicode use found on p. 36: probability statement. With probability 1 −δ, the eigenvalue of the coherence matrix is upper
-> Invalid unicode use found on p. 36: 2c −
-> Invalid unicode use found on p. 37: where ˆJ = I −ηHt −ηρ
-> Invalid unicode use found on p. 37: JT ˆJ] = E[(I −ηHt −ηρ
-> Invalid unicode use found on p. 37: α HHt)(I −ηHt −ηρ
-> Invalid unicode use found on p. 37: = E[I −2ηHt −ηρ
-> Invalid unicode use found on p. 37: = I −2ηHt −2ηρ
-> Invalid unicode use found on p. 37: Bn −1
-> Invalid unicode use found on p. 37: JT ˆJ]e1 = 1 −2ηλ1 −2ηρ
-> Invalid unicode use found on p. 37: Bn −1
-> Invalid unicode use found on p. 37: 1 −2ηλ1 −2ηρ
-> Invalid unicode use found on p. 37: Bn −1
-> Invalid unicode use found on p. 37: −2ηλ1(1 + ρ
-> Invalid unicode use found on p. 37: B −1)(1 + ρ
-> Invalid unicode use found on p. 37: −2 + ηλ1(1 + ρ
-> Invalid unicode use found on p. 37: B −1)(1 + ρ
-> Invalid unicode use found on p. 37: B −1
-> Invalid unicode use found on p. 37: B −1 + σ) ≤2
-> Invalid unicode use found on p. 37: B −1 + σ)−1
-> Invalid unicode use found on p. 38: B −1)−1
-> Invalid unicode use found on p. 38: B −1)−1
-> Invalid unicode use found on p. 38: nB −η2
-> Invalid unicode use found on p. 38: η < λi(H) < 2 −ϵ
-> Invalid unicode use found on p. 38: nB −η2
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Bracket content ['Valle-P´erez et al, 2019'] on p. 1 could not be matched to a reference.
   -> Sentence:  This built-in Occam’s razor has been offered as an explanation for why DNNs do not overfit even when they could 
in principle memorize the training set [Valle-P´erez et al, 2019]
-> INFO: Found possible citet reference but couldn't really match it: '[∥wk∥2]'
      -> Sentence: ' To study the long-term behavior of the iterates, we analyze the expected squared norm of the weights: 
E[∥wk∥2] = E[w⊤ 0 ˆJ⊤ 1 · · · ˆJ⊤ k ˆJk · · · ˆJ1w0] = E[Tr( ˆJk · · · ˆJ1w0w⊤ 0 ˆJ⊤ 1 · · · ˆJ⊤ k )]'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'w⊤ 0 ˆJ⊤ 1 · · · ˆJ⊤ k ˆJk · · · ˆJ1w0'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  To study the long-term behavior of the iterates, we analyze the expected squared norm of the weights: E[∥wk∥2] = E[w⊤ 0 ˆJ⊤
1 · · · ˆJ⊤ k ˆJk · · · ˆJ1w0] = E[Tr( ˆJk · · · ˆJ1w0w⊤ 0 ˆJ⊤ 1 · · · ˆJ⊤ k )]
-> Warning: Bracket content ['Tr( ˆJk · · · ˆJ1w0w⊤ 0 ˆJ⊤ 1 · · · ˆJ⊤ k ),'] on p. 3 could not be matched to a reference.
   -> Sentence:  To study the long-term behavior of the iterates, we analyze the expected squared norm of the weights: E[∥wk∥2] = 
E[w⊤ 0 ˆJ⊤ 1 · · · ˆJ⊤ k ˆJk · · · ˆJ1w0] = E[Tr( ˆJk · · · ˆJ1w0w⊤ 0 ˆJ⊤ 1 · · · ˆJ⊤ k )]
-> Warning: Bracket content ['Tr( ˆJ⊤ k · · · ˆJ⊤ 1 ˆJ1 · · · ˆJk),'] on p. 3 could not be matched to a reference.
   -> Sentence:  Assuming w0 ∼N(0, I), we reduce to analyzing the quantity E[Tr( ˆJ⊤ k · · · ˆJ⊤ 1 ˆJ1 · · · ˆJk)], which captures
the contraction or expansion behavior of the iterates under the sequence of update matrices
-> INFO: Found possible citet reference but couldn't really match it: '[∥wk∥2]'
      -> Sentence: ' The system is said to be linearly stable at w⋆under a given optimization method if the expected squared norm 
E[∥wk∥2] remains bounded as k →∞'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'ˆJ⊤ t ˆJt'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  A sufficient condition for this is that the spectral norm of the average update matrix E[ ˆJ⊤ t ˆJt] is strictly less than 
1
-> Warning: Bracket content ['J2k,'] on p. 4 could not be matched to a reference.
   -> Sentence:  (Comparative Divergence Speed) Suppose Tr[J2k] ≤C0αk for some constants C0 and αk, then the divergence rate of 
the random perturbation method is asymptotically within a constant factor of that of standard SGD: lim k→∞ E[∥wk∥2]Random, lower 
bound E[∥wk∥2]SGD, lower bound = O(1) 3
-> INFO: Found possible citet reference but couldn't really match it: '[∥wk∥2]'
      -> Sentence: ' ≤C0αk for some constants C0 and αk, then the divergence rate of the random perturbation method is 
asymptotically within a constant factor of that of standard SGD: lim k→∞ E[∥wk∥2]Random, lower bound E[∥wk∥2]SGD, lower bound = 
O(1) 3'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[∥wk∥2]'
      -> Sentence: 'Random, lower bound E[∥wk∥2]SGD, lower bound = O(1) 3'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[2024]'
      -> Sentence: ', Dexter et al [2024])'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> WARNING: Mismatch in intext-reference-parsing! Skipping 'wT k wk'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  Then, under the random perturbation update (3), the expected squared norm of the iterates remains bounded as k →∞: lim 
k→∞E[wT k wk]upper bound = O(1) Discussion
-> Info: There is no bracket content?? Skipping this sentence:
   ->  If there exists ϵ ∈(0, 1) such that ϵ η ≤λi + ρ αλ2 i ≤2 −ϵ η , ∀i ∈[d], and the accumulated noise decays sufficiently fast
(see Appendix C
-> INFO: Found possible citet reference but couldn't really match it: '[∥wk∥2]'
      -> Sentence: '9), then the iterates converge in expectation: lim k→∞E[∥wk∥2] = 0'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> WARNING: Mismatch in intext-reference-parsing! Skipping '(I + ρ αH)Hi(I + ρ αH)Hj'...
-> Info: There is no bracket content?? Skipping this sentence:
   ->  However, if we map the SAM dyanamics to those of SGD as per Eq (1), we can extrapolate that SAM operates on a sharper 
surface where the effective Hessian and coherence matrix becomes HSAM =  I + ρ αH  H, SSAM,ij = r Tr[(I + ρ αH)Hi(I + ρ αH)Hj]
-> Info: There is no bracket content?? Skipping this sentence:
   ->  For every choice of λ1 > 0, n ∈N, B ∈[n], η > 0 and σ ∈[n], that satisfied λ1(1 + ρ αλ1) ≤2σ η (σ + n B −1)−1, (5) there 
exist a set of PSD matrices {Hi}i∈[n] such that λmax(H) = λ1 and limk→∞E|| ˆJk
-> Info: There is no bracket content?? Skipping this sentence:
   ->  For every choice of λ1 > 0, n ∈N, B ∈[n], η > 0 and σ ∈[n], that satisfied λ1(1 + ρ αλ1) ≤2σ η (σ + n B −1)−1, (5) there 
exist a set of PSD matrices {Hi}i∈[n] such that λmax(H) = λ1 and limk→∞E|| ˆJk
-> Info: There is no bracket content?? Skipping this sentence:
   ->  For every choice of λ1 > 0, n ∈N, B ∈[n], η > 0 and σ ∈[n], that satisfied λ1(1 + ρ αλ1) ≤2σ η (σ + n B −1)−1, (5) there 
exist a set of PSD matrices {Hi}i∈[n] such that λmax(H) = λ1 and limk→∞E|| ˆJk
-> INFO: Found possible citet reference but couldn't really match it: '[0]'
      -> Sentence: ' and labels are generated y = x[0]x[1], ensuring that both simple and complex solutions exist'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[1]'
      -> Sentence: 'x[1], ensuring that both simple and complex solutions exist'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> Info: There is no bracket content?? Skipping this sentence:
   ->  We set W2[j] = 1 r(−1)a1+a2 to match
-> Info: There is no bracket content?? Skipping this sentence:
   ->  For k > C, W1,k = 0, W2[k] = 0, b[k] = 0
-> Info: There is no bracket content?? Skipping this sentence:
   ->  For k > C, W1,k = 0, W2[k] = 0, b[k] = 0
-> INFO: Found possible citet reference but couldn't really match it: '[0]'
      -> Sentence: ' Given that y = x[0]x[1] (as described in Section 3'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> INFO: Found possible citet reference but couldn't really match it: '[1]'
      -> Sentence: 'x[1] (as described in Section 3'
-> Info: The bracket content [''] is empty?? Skipping this one.
-> Info: There is no bracket content?? Skipping this sentence:
   -> 3), the construction guarantees that each (C, r)-generalizing solution is also interpolating: f(xi) = yi for all i ∈[n]
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 310 sentences on 10 pages -> Avg. of 35.44444444444444 sentences per page
-> Warning: Reference 'Achour et al, 2024' never used in the document's text.
-> Warning: Reference 'Bhatia, 2013' never used in the document's text.
-> Warning: Reference 'Chatterjee, 2020' never used in the document's text.
-> Warning: Reference 'Chen and Flammarion, 2022' never used in the document's text.
-> Warning: Reference 'Chen et al, 2023a' never used in the document's text.
-> Warning: Reference 'Dinh et al, 2017' never used in the document's text.
-> Warning: Reference 'Gunasekar et al, 2018' never used in the document's text.
-> Warning: Reference 'Hardt et al, 2016' never used in the document's text.
-> Warning: Reference 'Jiang et al, 2020' never used in the document's text.
-> Warning: Reference 'Kalimeris et al, 2019' never used in the document's text.
-> Warning: Reference 'Khanna et al, 2018' never used in the document's text.
-> Warning: Reference 'Kwon et al, 2021' never used in the document's text.
-> Warning: Reference 'Li et al, 2018' never used in the document's text.
-> Warning: Reference 'Lyu and Li, 2019' never used in the document's text.
-> Warning: Reference 'Ma and Ying, 2021' never used in the document's text.
-> Warning: Reference 'Morwani et al, 2023' never used in the document's text.
-> Warning: Reference 'Papyan et al, 2020' never used in the document's text.
-> Warning: Reference 'Sankararaman et al, 2020' never used in the document's text.
-> Warning: Reference 'Soudry et al, 2018' never used in the document's text.
-> Warning: Reference 'Valle-Pérez et al, 2019' never used in the document's text.
-> Warning: Reference 'Wen et al, 2023b' never used in the document's text.
-> Warning: Reference 'Wu and Su, 2023' never used in the document's text.
-> Warning: Reference 'Wu and Ma, 2018' never used in the document's text.
-> Warning: Reference 'Wu et al, 2022' never used in the document's text.
-> Warning: Reference 'Zhang et al, 2024' never used in the document's text.
-> Warning: Reference 'research et al, 0' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = Achour et al, 2024); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = Andriushchenko and Flammarion, 2022); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = Andriushchenko et al, 2023); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = Arpit et al, 2017); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = Bhatia, 2013); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = Bisla et al, 2022); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = Chatterjee, 2020); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = Chen and Flammarion, 2022); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = Chen et al, 2023a); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = Chen et al, 2023b); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = Dexter et al, 2024); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = Dinh et al, 2017); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = Du et al, 2022); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> WARNING: Reference with index 14 (Ref. ID = Gunasekar et al, 2018) has no associated sentence!
-> WARNING: Reference with index 15 (Ref. ID = Hardt et al, 2016) has no associated sentence!
-> Missing an abstract for reference with index 16 (Ref. ID = Hochreiter and Schmidhuber, 1997); Skipping LLM check...
-> WARNING: Reference with index 17 (Ref. ID = Jiang et al, 2020) has no associated sentence!
-> WARNING: Reference with index 18 (Ref. ID = Kalimeris et al, 2019) has no associated sentence!
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 20 (Ref. ID = Khanna et al, 2018); Skipping LLM check...
-> WARNING: Reference with index 21 (Ref. ID = Kwon et al, 2021) has no associated sentence!
-> Missing an abstract for reference with index 22 (Ref. ID = Li et al, 2018); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = Lyu and Li, 2019); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = Ma and Ying, 2021); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = Morwani et al, 2023); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = Papyan et al, 2020); Skipping LLM check...
-> WARNING: Reference with index 27 (Ref. ID = Sankararaman et al, 2020) has no associated sentence!
-> Missing an abstract for reference with index 28 (Ref. ID = Shah et al, 2020); Skipping LLM check...
-> WARNING: Reference with index 29 (Ref. ID = Soudry et al, 2018) has no associated sentence!
-> Missing an abstract for reference with index 30 (Ref. ID = Springer et al, 2024); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = Valle-Pérez et al, 2019); Skipping LLM check...
-> Missing an abstract for reference with index 32 (Ref. ID = Wen et al, 2023a); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = Wen et al, 2023b); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = Wu and Su, 2023); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = Wu and Ma, 2018); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = Wu et al, 2022); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = Zhang et al, 2024); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = Zhou et al, 2025); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = research et al, 0); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 7 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 3
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 4
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 5
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 6
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 7
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\27 A Unified Stability Analysis\PAU_results.md
```