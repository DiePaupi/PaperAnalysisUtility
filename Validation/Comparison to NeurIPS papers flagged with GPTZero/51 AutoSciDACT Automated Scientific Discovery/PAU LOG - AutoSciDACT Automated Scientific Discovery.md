
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\51 AutoSciDACT Automated Scientific Discovery\AutoSciDACT Automated Scientific Discovery through Contrastive Embedding.pdf"
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
- Found following heading '3 - The AutoSciDACT Pipeline' on page 3
- Found following heading '4 - Datasets' on page 6
- Found following heading '5 - Experiments' on page 7
- Found following heading '6 - Discussion' on page 9
- Found following heading '7 - Acknowledgments' on page 10
=> Found references/literature section on page 10
- Found first appendix 'A - Dataset, Training, and Evaluation Details' on page 18
- Found following appendix 'B - Additional Experiments' on page 22
- Found following appendix 'C - Comparison to previous results from histology' on page 25
- Found following appendix 'D - Discriminating CIFAR-10.1 and CIFAR-5m' on page 28
- Found following appendix 'E - Searching for the Higgs boson in LHC Data' on page 28
- Found following appendix 'F - Embedding Space Visualizations' on page 31
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 18
All found references: 124
-> Warning: Could not parse year in reference 'Cms open data. range (%)synthetic10,0002,0000.5 - 10astronomy20,0004,0000.5 - 10particle physics50,00010,0000.1 - 2histology6,2965002.5 - 20images (cifar-10)9,0001,8001 - 10genomics1,7641005 - 20table 1: the reference dataset size, observed dataset size, and range of injected anomaly fractions(relative to the background component in d) for each dataset considered in our study. theseparameters are used when running nplm pseudo-experiments across a range of signal fractions toproduce the results shown in fig. 3.a'!
-----------
 -> Parsed references DataFrame:
    ref_id                                            authors  ...                                       link  valid
0        1  Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob ...  ...                                              None
1        2  Yutaro Yamada, Robert Tjarko Lange, Cong Lu, S...  ...                                              None
2        3  Juraj Gottweis, Wei-Hung Weng, Alexander Daryi...  ...                                              None
3        4  Marco Letizia, Gianvito Losapio, Marco Rando, ...  ...                                              None
4        5  Ting Chen, Simon Kornblith, Mohammad Norouzi, ...  ...                                              None
..     ...                                                ...  ...                                        ...    ...
119    120  Benjamin Recht, Rebecca Roelofs, Ludwig Schmid...  ...                                              None
120    121  Feng Liu, Wenkai Xu, Jie Lu, Guangquan Zhang, ...  ...                                              None
121    122                           Serguei Chatrchyan et al  ...                                              None
122    123                                  Georges Aad et al  ...                                              None
123    124                                      Cms open data  ...  https://opendata.cern.ch/.Dataset|R||D|fS   None

[124 rows x 10 columns]
- Checking reference 1/124:
  -> INFO: Now checking 10 results for matching title: 'The ai scientist: Towards fully automated open-ended scientific discovery'
       -> INFO: All authors matched!
- Checking reference 2/124:
  -> INFO: Now checking 1 results for matching title: 'The ai scientist-v2: Workshop-level automated scientific discovery via agentic tree search'
       -> INFO: All authors matched!
- Checking reference 3/124:
  -> INFO: Now checking 10 results for matching title: 'Towards an ai co-scientist'
       -> WARNING: Not all 34 authors from the found ref. were matched (only 10)
                   Unmatched authors = 'Saab, Popovici, Blum, Zhang, Chou, Hassidim, Gokturk, Vahdat, Kohli, Matias, Carroll, Kulkarni, Tomašev, Guan, Dhillon, Vaishnav, Lee, Costa, Penad'es, Peltz, Xu, Pawlosky, Karthikesalingam, Natarajan'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/124:
  -> INFO: Now checking 10 results for matching title: 'Learning new physics efficiently with nonparametric methods'
       -> INFO: All authors matched!
- Checking reference 5/124:
  -> INFO: Now checking 5 results for matching title: 'A simple framework for contrastive learning of visual representations'
       -> INFO: All authors matched!
- Checking reference 6/124:
  -> INFO: Now checking 10 results for matching title: 'Momentum contrast for unsupervised visual representation learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/124:
  -> INFO: Now checking 10 results for matching title: 'Vicreg: Variance-invariance-covariance regularization for self-supervised learning'
       -> INFO: All authors matched!
- Checking reference 8/124:
  -> INFO: Now checking 10 results for matching title: 'Barlow twins: Selfsupervised learning via redundancy reduction'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Barlow twins: Selfsupervised learning via redundancy reduction'
  -> WARNING: None of the 2 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Barlow+twins:+Selfsupervised+learning+via+redundancy+reduction manually and check the results.
        -> Author(s): Jure Zbontar, Li Jing, Ishan Misra, Yann LeCun, and Stéphane Deny
        -> Title:     Barlow twins: Selfsupervised learning via redundancy reduction
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 9/124:
  -> INFO: Now checking 10 results for matching title: 'Supervised contrastive learning'
       -> INFO: All authors matched!
- Checking reference 10/124:
  -> INFO: Now checking 10 results for matching title: 'Supervised contrastive learning for pre-trained language model fine-tuning'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/124:
  -> INFO: Now checking 10 results for matching title: 'Learning transferable visual models from natural language supervision'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 12/124:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Mineclip: Multimodal neural exploration of clip latents for automatic video annotation
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Azabou', 'Weber', 'Ma', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Mineclip:+Multimodal+neural+exploration+of+clip+latents+for+automatic+video+annotation manually and check the results.
        -> Author(s): Mehdi Azabou, Micah Weber, Wenlin Ma, et al
        -> Title:     Mineclip: Multimodal neural exploration of clip latents for automatic video annotation
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 13/124:
  -> INFO: Now checking 2 results for matching title: 'Cadet: Fully self-supervised out-of-distribution detection with contrastive learning'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'López'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 14/124:
  -> INFO: Now checking 10 results for matching title: 'Contrastive predictive coding for anomaly detection'
       -> INFO: All authors matched!
- Checking reference 15/124:
  -> INFO: Now checking 10 results for matching title: 'Deep anomaly detection using geometric transformations'
       -> INFO: All authors matched!
- Checking reference 16/124:
  -> INFO: Now checking 2 results for matching title: 'Csi: Novelty detection via contrastive learning on distributionally shifted instances'
       -> INFO: All authors matched!
- Checking reference 17/124:
  -> INFO: Now checking 10 results for matching title: 'Hybrid discriminative-generative training via contrastive learning'
       -> INFO: All authors matched!
- Checking reference 18/124:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Rodd: A selfsupervised approach for robust out-of-distribution detection
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 4 results for matching title: 'Rodd: A selfsupervised approach for robust out-of-distribution detection'
  -> WARNING: None of the 4 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Rodd:+A+selfsupervised+approach+for+robust+out-of-distribution+detection manually and check the results.
        -> Author(s): Umar Khalid, Ashkan Esmaeili, Nazmul Karim, and Nazanin Rahnavard
        -> Title:     Rodd: A selfsupervised approach for robust out-of-distribution detection
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 19/124:
  -> INFO: Now checking 10 results for matching title: 'Contrastive training for improved out-of-distribution detection'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 20/124:
  -> Checking if provided link is pingable: https://ojs.aaai.org/index.php/AAAI/article/view/5966
  -> INFO: Now checking 10 results for matching title: 'Self-supervised learning for generalizable out-of-distribution detection'
       -> INFO: All authors matched!
- Checking reference 21/124:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Ssd: A unified framework for selfsupervised outlier detection
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 4 results for matching title: 'Ssd: A unified framework for selfsupervised outlier detection'
  -> WARNING: None of the 4 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Ssd:+A+unified+framework+for+selfsupervised+outlier+detection manually and check the results.
        -> Author(s): Vikash Sehwag, Mung Chiang, and Prateek Mittal
        -> Title:     Ssd: A unified framework for selfsupervised outlier detection
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 22/124:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2503.19111
  -> INFO: Now checking 10 results for matching title: 'Classification of radio sources through self-supervised learning.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Perez', 'Brüggen', 'Kasieczka', 'Lucie-Smith', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://arxiv.org/abs/2503.19111 manually and check the results.
        -> Author(s): Nicolas Baron Perez, Marcus Brüggen, Gregor Kasieczka, and Luisa Lucie-Smith
        -> Title:     Classification of radio sources through self-supervised learning.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 23/124:
  -> Checking if provided link is pingable: https://doi.org/10.1093/mnras/staa2395
  -> INFO: Now checking 3 results for matching title: 'Unsupervised machine learning for transient discovery in deeper, wider, faster light curves'
       -> INFO: All authors matched!
- Checking reference 24/124:
  -> Checking if provided link is pingable: https://doi.org/10.1016/j.jpi.2023.100305
  -> INFO: Now checking 1 results for matching title: 'Investigation of semi- and self-supervised learning methods in the histopathological domain'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Voigt', 'Fischer', 'Schilling', 'Krumnow', 'Herta', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.1016/j.jpi.2023.100305 manually and check the results.
        -> Author(s): Benjamin Voigt, Oliver Fischer, Bruno Schilling, Christian Krumnow, and Christian Herta
        -> Title:     Investigation of semi- and self-supervised learning methods in the histopathological domain
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 25/124:
  -> Checking if provided link is pingable: https://doi.org/10.1016/j.media.2023.103067
  -> INFO: Now checking 1 results for matching title: 'Learning image representations for anomaly detection: Application to discovery of histological alterations in drug development'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/124:
  -> Checking if provided link is pingable: https://link.aps.org/doi/10.1103/PhysRevD.106.056005
  -> INFO: Now checking 10 results for matching title: 'Self-supervised anomaly detection for new physics'
       -> INFO: All authors matched!
- Checking reference 27/124:
  -> INFO: Now checking 1 results for matching title: 'Anomaly preserving contrastive neural embeddings for end-to-end modelindependent searches at the LHC'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Metzger', 'Xu', 'Sodini', 'Arrestad', 'Govorkova', 'Grosso', 'Harris', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Anomaly+preserving+contrastive+neural+embeddings+for+end-to-end+modelindependent+searches+at+the+LHC manually and check the results.
        -> Author(s): Kyle Metzger, Lana Xu, Mia Sodini, Thea K Arrestad, Katya Govorkova, Gaia Grosso, and Philip Harris
        -> Title:     Anomaly preserving contrastive neural embeddings for end-to-end modelindependent searches at the LHC
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 28/124:
  -> INFO: Now checking 1 results for matching title: 'A simple unified framework for detecting out-of-distribution samples and adversarial attacks'
       -> INFO: All authors matched!
- Checking reference 29/124:
  -> INFO: Now checking 10 results for matching title: 'A kernel two-sample test'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Scholkopf'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/124:
  -> INFO: Now checking 1 results for matching title: 'Mmd-fuse: learning and combining kernels for two-sample testing without data splitting'
       -> INFO: All authors matched!
- Checking reference 31/124:
  -> INFO: Now checking 10 results for matching title: 'Mmd aggregated two-sample test'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 32/124:
  -> INFO: Now checking 10 results for matching title: 'Revisiting classifier two-sample tests'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/124:
  -> INFO: Now checking 10 results for matching title: 'Density ratio estimation in machine learning'
       -> INFO: All authors matched!
- Checking reference 34/124:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Do deep generative models know what they don’t know? In International Conference on Learning Representations (ICLR).
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 3 results for matching title: 'Do deep generative models know what they don’t know? In International Conference on Learning Representations (ICLR).'
  -> WARNING: None of the 3 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Do+deep+generative+models+know+what+they+don’t+know?+In+International+Conference+on+Learning+Representations+(ICLR). manually and check the results.
        -> Author(s): Eric Nalisnick, Akihiro Matsukawa, Yee Whye Teh, Dilan Gorur, and Balaji Lakshminarayanan
        -> Title:     Do deep generative models know what they don’t know? In International Conference on Learning Representations (ICLR).
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 35/124:
  -> INFO: Now checking 2 results for matching title: 'Variational Autoencoders for New Physics Mining at the Large Hadron Collider'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 36/124:
  -> Checking if provided link is pingable: https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2022.803685
  -> INFO: Now checking 1 results for matching title: 'Improving variational autoencoders for new physics detection at the lhc with normalizing flows'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 37/124:
  -> INFO: Now checking 2 results for matching title: 'Autoencoders on field-programmable gate arrays for real-time, unsupervised new physics detection at 40 MHz at the Large Hadron Collider'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 38/124:
  -> INFO: Now checking 10 results for matching title: 'Autoencoders for unsupervised anomaly detection in high energy physics'
       -> INFO: All authors matched!
- Checking reference 39/124:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Realtime Anomaly Detection at the L1 Trigger of CMS Experiment
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 5 results for matching title: 'Realtime Anomaly Detection at the L1 Trigger of CMS Experiment'
  -> WARNING: None of the 5 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Realtime+Anomaly+Detection+at+the+L1+Trigger+of+CMS+Experiment manually and check the results.
        -> Author(s): Abhijith Gandrakota
        -> Title:     Realtime Anomaly Detection at the L1 Trigger of CMS Experiment
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 40/124:
  -> Checking if provided link is pingable: https://doi.org/10.1016/j.revip.2024.100091.URL
  -> INFO: Now checking 10 results for matching title: 'Machine learning for anomaly detection in particle physics'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 41/124:
  -> INFO: Now checking 3 results for matching title: 'Autoencoder-Based Anomaly Detection System for Online Data Quality Monitoring of the CMS Electromagnetic Calorimeter'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 42/124:
  -> INFO: Now checking 1 results for matching title: 'Adversarially Learned Anomaly Detection on CMS Open Data: re-discovering the top quark'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 43/124:
  -> INFO: Now checking 1 results for matching title: 'Quasi Anomalous Knowledge: Searching for new physics with embedded knowledge'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 44/124:
  -> Checking if provided link is pingable: https://dx.doi.org/10.1088/2632-2153/abf3d0
  -> INFO: Now checking 10 results for matching title: 'Anomaly detection in gravitational waves data using convolutional autoencoders'
       -> INFO: All authors matched!
- Checking reference 45/124:
  -> INFO: Now checking 2 results for matching title: 'Source-agnostic gravitational-wave detection with recurrent autoencoders'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 46/124:
  -> INFO: Now checking 1 results for matching title: 'GWAK: gravitational-wave anomalous knowledge with recurrent autoencoders'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 47/124:
  -> INFO: Now checking 10 results for matching title: 'Classification without labels: Learning from mixed samples in high energy physics'
       -> INFO: All authors matched!
- Checking reference 48/124:
  -> INFO: Now checking 10 results for matching title: 'Learning New Physics from a Machine'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 49/124:
  -> INFO: Now checking 10 results for matching title: 'Learning multivariate new physics'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2021)!
       -> INFO: All authors matched!
- Checking reference 50/124:
  -> INFO: Now checking 10 results for matching title: 'Goodness of fit by NeymanPearson testing'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Grosso', 'Letizia', 'Pierini', 'Wulzer', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Goodness+of+fit+by+NeymanPearson+testing manually and check the results.
        -> Author(s): Gaia Grosso, Marco Letizia, Maurizio Pierini, and Andrea Wulzer
        -> Title:     Goodness of fit by NeymanPearson testing
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 51/124:
  -> INFO: Now checking 10 results for matching title: 'Learning new physics from an imperfect machine'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 52/124:
  -> Checking if provided link is pingable: https://royalsocietypublishing.org/doi/abs/10.1098/rsta.1933.0009
  -> WARNING: Skipping search (due to not enough info) for reference titled 'Ix'
           -> Author(s): Jerzy Neyman, Egon Sharpe Pearson, and Karl Pearson
           -> Year: 1933
- Checking reference 53/124:
  -> INFO: Now checking 2 results for matching title: 'Multiple testing for signal-agnostic searches for new physics with machine learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/124:
  -> INFO: Now checking 10 results for matching title: 'Advanced LIGO'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 11 results for matching title: 'Advanced LIGO'
  -> WARNING: None of the 11 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Advanced+LIGO manually and check the results.
        -> Author(s): J Aasi et al
        -> Title:     Advanced LIGO
        -> Year:      2015
     -> Manual search was skipped by the user.
- Checking reference 55/124:
  -> INFO: Now checking 1 results for matching title: 'GWTC-3: Compact Binary Coalescences Observed by LIGO and Virgo during the Second Part of the Third Observing Run'
       -> WARNING: Not all 500 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Collaboration, Collaboration, Acernese, Ackley, Adams, Adhikari, Adhikari, Adya, Affeldt, Agarwal, Agathos, Agatsuma, Aggarwal, Aguiar, Aiello, Ain, Ajith, Akçay, Akutsu, Albanesi, Allocca, Altin, Amato, Anand, Anand, Ananyeva, Anderson, Anderson, Ando, Andrade, Andrés, Andri'c, Angelova, Ansoldi, Antelis, Antier, Appert, Arai, Arai, Arai, Araki, Araya, Araya, Areeda, Arène, Aritomi, Arnaud, Arogeti, Aronson, Arun, Asada, Asali, Ashton, Aso, Assiduo, Aston, Astone, Aubin, Austin, Babak, Badaracco, Bader, Badger, Bae, Bae, Baer, Bagnasco, Bai, Baiotti, Baird, Bajpai, Ball, Ballardin, Ballmer, Balsamo, Baltus, Banagiri, Bankar, Barayoga, Barbieri, Barish, Barker, Barneo, Barone, Barr, Barsotti, Barsuglia, Barta, Bartlett, Barton, Bartos, Bassiri, Basti, Bawaj, Bayley, Baylor, Bazzan, B'ecsy, Bedakihale, Bejger, Belahcene, Benedetto, Beniwal, Bennett, Bentley, BenYaala, Bergamin, Berger, Bernuzzi, Berry, Bersanetti, Bertolini, Betzwieser, Beveridge, Bhandare, Bhardwaj, Bhattacharjee, Bhaumik, Bilenko, Billingsley, Bini, Birney, Birnholtz, Biscans, Bischi, Biscoveanu, Bisht, Biswas, Bitossi, Bizouard, Blackburn, Blair, Blair, Blair, Bobba, Bode, Boer, Bogaert, Boldrini, Bonavena, Bondu, Bonilla, Bonnand, Booker, Boom, Bork, Boschi, Bose, Bose, Bossilkov, Boudart, Bouffanais, Bozzi, Bradaschia, Brady, Bramley, Branch, Branchesi, Brandt, Brau, Breschi, Briant, Briggs, Brillet, Brinkmann, Brockill, Brooks, Brooks, Brown, Brunett, Bruno, Bruntz, Bryant, Bulik, Bulten, Buonanno, Buscicchio, Buskulic, Buy, Byer, Davies, Cadonati, Cagnoli, Cahillane, Bustillo, Callaghan, Callister, Calloni, Cameron, Camp, Canepa, Canevarolo, Cannavacciuolo, Cannon, Cao, Cao, Capocasa, Capote, Carapella, Carbognani, Carlin, Carney, Carpinelli, Carrillo, Carullo, Carver, Diaz, Casentini, Castaldi, Caudill, Cavaglià, Cavalier, Cavalieri, Ceasar, Cella, Cerd'a-Dur'an, Cesarini, Chaibi, Chakravarti, Subrahmanya, Champion, Chan, Chan, Chan, Chan, Chan, Chandra, Chanial, Chao, Chapman-Bird, Charlton, Chase, Chassande-Mottin, Chatterjee, Chatterjee, Chatterjee, Chaturvedi, Chaty, Chatziioannou, Chen, Chen, Chen, Chen, Chen, Chen, Chen, Chen, Cheng, Cheong, Cheung, Chia, Chiadini, Chiang, Chiarini, Chierici, Chincarini, Chiofalo, Chiummo, Cho, Cho, Choudhary, Choudhary, Christensen, Chu, Chu, Chu, Chua, Chung, Ciani, Ciecieląg, Cie'slar, Cifaldi, Ciobanu, Ciolfi, Cipriano, Cirone, Clara, Clark, Clark, Clarke, Clearwater, Clesse, Cleva, Coccia, Codazzo, Cohadon, Cohen, Cohen, Colleoni, Collette, Colombo, Colpi, Compton, Constancio, Conti, Cooper, Corban, Corbitt, Cordero-Carri'on, Corezzi, Corley, Cornish, Corre, Corsi, Cortese, Costa, Cotesta, Coughlin, Coulon, Countryman, Cousins, Couvares, Coward, Cowart, Coyne, Coyne, Creighton, Creighton, Criswell, Croquette, Crowder, Cudell, Cullen, Cumming, Cummings, Cunningham, Cuoco, Curyło, Dabadie, Canton, Dall'Osso, D'alya, Dana, DaneshgaranBajastani, D'Angelo, Danila, Danilishin, D'Antonio, Danzmann, Darsow-Fromm, Dasgupta, Datrier, Datta, Dattilo, Dave, Davier, Davis, Davis, Daw, Alarc'on, Dean, DeBra, Deenadayalan, Degallaix, Laurentis, Del'eglise, Favero, Lillo, Lillo, Pozzo, Demarchi, Matteis, d'Emilio, Demos, Dent, Depasse, Pietri, Rosa, Rossi, DeSalvo, Simone, Dhurandhar, Díaz, Diaz-Ortiz, Didio, Dietrich, Fiore, Fronzo, Giorgio, Giovanni, Giovanni, Girolamo, Lieto, Ding, Pace, Palma, Renzo, Divakarla, Dmitriev, Doctor, D'Onofrio, Donovan, Dooley, Doravari, Dorrington, Drago, Driggers, Drori, Ducoin, Dupej, Durante, D'Urso, Duverne, Dwyer, Eassa, Easter, Ebersold, Eckhardt, Eddolls, Edelman, Edo, Edy, Effler, Eguchi, Eichholz, Eikenberry, Eisenmann, Eisenstein, Ejlli, Engelby, Enomoto, Errico, Essick, Estell'es, Estevez, Etienne, Etzel, Evans, Evans, Ewing, Fafone, Fair, Fairhurst, Farah, Farinon, Farr, Farr, Farrow, Fauchon-Jones, Favaro, Favata, Fays, Fazio, Feicht, Fejer, Fenyvesi, Ferguson, Fernández-Galiana, Ferrante, Ferreira, Fidecaro, Figura, Fiori, Fishbach, Fisher, Fittipaldi, Fiumara, Flaminio, Floden, Fong, Font, Fornal, Forsyth, Franke, Frasca, Frasconi, Frederick, Freed, Frei, Freise, Frey, Fritschel, Frolov, Fronz'e, Fujii, Fujikawa, Fukunaga, Fukushima, Fulda, Fyffe, Gabbard, Gadre, Gair, Gais, Galaudage, Gamba, Ganapathy, Ganguly, Gao, Gaonkar, Garaventa, Garc'ia, Garc'ia-N'unez, Garc'ia-Quir'os, Garufi, Gateley, Gaudio, Gayathri'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 56/124:
  -> Checking if provided link is pingable: https://doi.org/10.7935/nfnt-hm34
  -> INFO: Now checking 10 results for matching title: 'The O3a Data Release, April.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 996 results for matching title: 'The O3a Data Release, April.'
  -> WARNING: None of the 996 results matched the expected title!
     -> You could also open https://doi.org/10.7935/nfnt-hm34 manually and check the results.
        -> Author(s): LIGO Scientific
        -> Title:     The O3a Data Release, April.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 57/124:
  -> Checking if provided link is pingable: https://doi.org/10.7935/pr1e-j706
  -> INFO: Now checking 10 results for matching title: 'The O3b Data Release, November.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 996 results for matching title: 'The O3b Data Release, November.'
  -> WARNING: None of the 996 results matched the expected title!
     -> You could also open https://doi.org/10.7935/pr1e-j706 manually and check the results.
        -> Author(s): LIGO Scientific
        -> Title:     The O3b Data Release, November.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 58/124:
  -> INFO: Now checking 6 results for matching title: 'Machine-learning pipeline for real-time detection of gravitational waves from compact binary coalescences'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 59/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.6619768
  -> INFO: Now checking 4 results for matching title: 'Jetclass: A large-scale dataset for deep learning in jet physics, June.'
  -> WARNING: None of the 4 results matched the expected title!
  -> INFO: Now checking 146 results for matching title: 'Jetclass: A large-scale dataset for deep learning in jet physics, June.'
  -> WARNING: None of the 146 results matched the expected title!
     -> You could also open https://doi.org/10.5281/zenodo.6619768 manually and check the results.
        -> Author(s): Huilin Qu, Congqiao Li, and Sitian Qian
        -> Title:     Jetclass: A large-scale dataset for deep learning in jet physics, June.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 60/124:
  -> INFO: Now checking 10 results for matching title: 'Particle Transformer for Jet Tagging'
       -> INFO: All authors matched!
- Checking reference 61/124:
  -> INFO: Now checking 2 results for matching title: 'A portrait of the Higgs boson by the CMS experiment ten years after the discovery'
       -> WARNING: Not all 500 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Dama, Adam, Andrejkovic, Bergauer, Chatterjee, Damanakis, Dragicevic, Valle, Hussain, Jeitler, Krammer, Lechner, Liko, Mikulec, Paulitsch, Pitters, Schieck, Schöfbeck, Schwarz, Templ, Waltenberger, Wulz, Darwish, Janssen, Kello, Sfar, Mechelen, Bols, D'Hondt, Moor, Delcourt, Faham, Lowette, Moortgat, Morton, Müller, Sahasransu, Tavernier, Doninck, Vannerom, Clerbaux, Lentdecker, Favart, Jaramillo, Lee, Mahdavikhorrami, Makarenko, Malara, Paredes, Pétré, Postiau, Starling, Thomas, Bemden, Velde, Vanlaer, Dobur, Knolle, Lambrecht, Mestdach, Niedziela, Rendón, Roskas, Samalan, Skovpen, Tytgat, Bossche, Vermassen, Wezenbeek, Benecke, Bruno, Bury, Caputo, David, Delaere, Donertas, Giammanco, Jaffel, Jain, Lemaitre, Mondal, Prisciandaro, Taliercio, Tran, Vischia, Wertz, Alves, Coelho, Hensel, Moraes, Teles, Júnior, Pereira, Filho, Malbouisson, Carvalho, Chinellato, Costa, Silveira, Damiao, Sousa, Souza, Martins, Herrera, Amarilo, Mundim, Nogima, Santoro, Amaral, Sznajder, Thiel, Araujo, Pereira, Bernardes, Calligaris, Gregores, Mercadante, Novaes, Padula, Tomei, Aleksandrov, Antchev, Hadjiiska, Iaydjiev, Misheva, Rodozov, Shopova, Sultanov, Dimitrov, Ivanov, Litov, Pavlov, Petkov, Petrov, Shumka, Cheng, Javaid, Mittal, Yuan, Ahmad, Bauer, Hu, Lezki, Yi, Chen, Chen, Chen, Iemmi, Jiang, Kapoor, Liao, Liu, Milosevic, Monti, Sharma, Tao, Thomas-Wilsker, Wang, Zhang, Zhao, Agapitos, Ban, Chen, Levin, Li, Li, Lyu, Mao, Qian, Sun, Wang, Xiao, Yang, Li, Lu, You, Gao, Leggat, Okawa, Zhang, Lin, Lu, Xiao, Avila, Trujillo, Cabrera, Florez, Fraga, Guisao, Ramirez, Rodriguez, Alvarez, Giljanovic, Godinovic, Lelas, Puljak, Antunović, Kovač, Šćulac, Brigljevic, Chitroda, Ferencek, Majumder, Roguljic, Starodumov, Susa, Attikis, Christoforou, Kole, Kolosova, Konstantinou, Mousa, Nicolaou, Ptochos, Razis, Rykaczewski, Saka, Finger, Finger, Kveton, Ayala, Jarrin, Abdelalim, Salama, Mahmoud, Mohammed, Bhowmik, Dewanjee, Ehataht, Kadastik, Nandan, Nielsen, Pata, Raidal, Tani, Veelken, Eerola, Kirschenmann, Osterberg, Voutilainen, Bharthuar, Brücken, Garcia, Havukainen, Kim, Kinnunen, Lampén, Lassila-Perini, Lehti, Lindén, Lotti, Martikainen, Myllymäki, Ott, Rantanen, Siikonen, Tuominen, Tuominiemi, Luukka, Petrow, Tuuva, Amendola, Besançon, Couderc, Dejardin, Denegri, Faure, Ferri, Ganjour, Gras, Monchenault, Jarry, Lohezic, Malcles, Rander, Rosowsky, Sahin, Savoy-Navarro, Simkina, Titov, Barrera, Beaudette, Perraguin, Busson, Cappati, Charlot, Davignon, Diab, Falmagne, Alves, Ghosh, Cassagnac, Hakimi, Harikrishnan, Motta, Nguyen, Ochando, Portalès, Rembser, Salerno, Sarkar, Sauvan, Sirois, Tarabini, Vernazza, Zabi, Zghiche, Agram, Andrea, Apparu, Bloch, Bourgatte, Brom, Chabert, Collard, Darej, Goerlach, Grimault, Bihan, Hove, Beauceron, Bernet, Boudoul, Camen, Carle, Chanon, Choi, Contardo, Depasse, Dozen, Mamouni, Fay, Gascon, Gouzevitch, Grenier, Ille, Laktineh, Lethuillier, Mirabito, Perriès, Shchablo, Sordini, Torterotot, Donckt, Verdier, Viret, Lomidze, Toriashvili, Tsamalaidze, Botta, Feld, Klein, Lipinski, Meuser, Pauls, Röwert, Teroerde, Diekmann, Dodonova, Eich, Eliseev, Erdmann, Fackeldey, Fischer, Hebbeker, Hoepfner, Ivone, Lee, Mastrolorenzo, Merschmeyer, Meyer, Mondal, Mukherjee, Noll, Novák, Nowotny, Pozdnyakov, Rath, Redjeb, Reithler, Schmidt, Schuler, Sharma, Vigilante, Wiedenbeck, Zaleski, Dziwok, Flügge, Ahmad, Hlushchenko, Kress, Nowack, Pooth, Stahl, Ziemons, Zotz, Petersen, Martin, Asmuss, Baxter, Bayatmakou, Behnke, Martínez, Bhattacharya, Anuar, Blekman, Borras, Brunner, Campbell, Cardini, Cheng, Colombina, Rodríguez, Silva, Silva, Didukh, Eckerlin, Eckstein, Banos, Filatov, Gallo, Geiser, Giraldi, Greau, Grohsjean, Guglielmi, Guthoff, Jafari, Jomhari, Kaech, Kasemann, Kaveh, Kleinwort, Kogler, Komm, Krücker, Lange, Pernia, Lipka, Lohmann, Mankel, Melzer-Pellmann, Morentin, Metwally, Meyer, Milella, Kasem, Mormile, Mussgiller, Nürnberg, Otarid, Adán, Raspereza, Lopes, Rübenach, Saggio, Saibel, Savitskyi, Scham, Scheurer, Schnake, Schütze, Schwanenberger, Shchedrolosiev, Ricardo, Stafford, Tonon, Klundert, Vazzoler, Barroso, Walsh, Walter, Wang, Wen, Wichmann, Wiens, Wissing, Wuchterl, Yang, Santos, Aggleton, Albrecht, Albrecht, Antonello, Bein, Benato, Bonanomi, Connor, Leo, Eich, Morabit, Feindt, Fröhlich, Garbers, Garutti, Hajheidari, Haller, Hinzmann'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 62/124:
  -> INFO: Now checking 10 results for matching title: 'Attention is all you need'
       -> INFO: All authors matched!
- Checking reference 63/124:
  -> Checking if provided link is pingable: https://osf.io/gqutd/
  -> WARNING: Skipping search (due to not enough info) for reference titled ''
           -> Author(s): Stierstofer B Heinemann F Zingman, I Nafld pathology and healthy tissue samples
           -> Year: 2022
- Checking reference 64/124:
  -> INFO: Now checking 10 results for matching title: 'Efficientnet: Rethinking model scaling for convolutional neural networks'
       -> INFO: All authors matched!
- Checking reference 65/124:
  -> INFO: Now checking 10 results for matching title: 'Learning multiple layers of features from tiny images'
       -> INFO: All authors matched!
- Checking reference 66/124:
  -> INFO: Now checking 2 results for matching title: 'The deep bootstrap framework: Good online learners are good offline generalizers'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 67/124:
  -> INFO: Now checking 10 results for matching title: 'Deep residual learning for image recognition'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 68/124:
  -> INFO: Now checking 10 results for matching title: 'On the distribution of the likelihood ratio'
       -> INFO: All authors matched!
- Checking reference 69/124:
  -> INFO: Now checking 1 results for matching title: 'The LHC Olympics 2020 a community challenge for anomaly detection in high energy physics'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 70/124:
  -> INFO: Now checking 2 results for matching title: 'A Neural Network-Based Search for Unmodeled Transients in LIGOVirgo-KAGRA’s Third Observing Run'
  -> WARNING: None of the 2 results matched the expected title!
  -> INFO: Now checking 4 results for matching title: 'A Neural Network-Based Search for Unmodeled Transients in LIGOVirgo-KAGRA’s Third Observing Run'
  -> WARNING: None of the 4 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+Neural+Network-Based+Search+for+Unmodeled+Transients+in+LIGOVirgo-KAGRA’s+Third+Observing+Run manually and check the results.
        -> Author(s): Ryan Raikman et al
        -> Title:     A Neural Network-Based Search for Unmodeled Transients in LIGOVirgo-KAGRA’s Third Observing Run
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 71/124:
  -> INFO: Now checking 10 results for matching title: 'Toward real-time detection of unmodeled gravitational wave transients using convolutional neural networks'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 72/124:
  -> INFO: Now checking 1 results for matching title: 'Weakly supervised anomaly detection for resonant new physics in the dijet final state using proton-proton collisions at √s = 13 TeV with the ATLAS detector'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 290 results for matching title: 'Weakly supervised anomaly detection for resonant new physics in the dijet final state using proton-proton collisions at √s = 13 TeV with the ATLAS detector'
  -> WARNING: None of the 290 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Weakly+supervised+anomaly+detection+for+resonant+new+physics+in+the+dijet+final+state+using+proton-proton+collisions+at+√s+=+13+TeV+with+the+ATLAS+detector manually and check the results.
        -> Author(s): Georges Aad et al
        -> Title:     Weakly supervised anomaly detection for resonant new physics in the dijet final state using proton-proton collisions at √s = 13 TeV with the ATLAS detector
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 73/124:
  -> INFO: Now checking 2 results for matching title: 'Dijet resonance search with weak supervision using √s = 13 TeV pp collisions in the ATLAS detector'
  -> WARNING: None of the 2 results matched the expected title!
  -> INFO: Now checking 166 results for matching title: 'Dijet resonance search with weak supervision using √s = 13 TeV pp collisions in the ATLAS detector'
  -> WARNING: None of the 166 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dijet+resonance+search+with+weak+supervision+using+√s+=+13+TeV+pp+collisions+in+the+ATLAS+detector manually and check the results.
        -> Author(s): Georges Aad et al
        -> Title:     Dijet resonance search with weak supervision using √s = 13 TeV pp collisions in the ATLAS detector
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 74/124:
  -> INFO: Now checking 1 results for matching title: 'Model-agnostic search for dijet resonances with anomalous jet substructure in proton-proton collisions at √s = 13 TeV'
  -> WARNING: None of the 1 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chekhovsky', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Model-agnostic+search+for+dijet+resonances+with+anomalous+jet+substructure+in+proton-proton+collisions+at+√s+=+13+TeV manually and check the results.
        -> Author(s): Vladimir Chekhovsky et al
        -> Title:     Model-agnostic search for dijet resonances with anomalous jet substructure in proton-proton collisions at √s = 13 TeV
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 75/124:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2203.02261
  -> INFO: Now checking 10 results for matching title: 'Class-aware contrastive semi-supervised learning.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yang', 'Wu', 'Zhang', 'Jiang', 'Liu', 'Zheng', 'Zhang', 'Wang', 'Zeng', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://arxiv.org/abs/2203.02261 manually and check the results.
        -> Author(s): Fan Yang, Kai Wu, Shuyi Zhang, Guannan Jiang, Yong Liu, Feng Zheng, Wei Zhang, Chengjie Wang, and Long Zeng
        -> Title:     Class-aware contrastive semi-supervised learning.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 76/124:
  -> INFO: Now checking 10 results for matching title: 'Resimulation-based self-supervised learning for pretraining physics foundation models'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 77/124:
  -> INFO: Now checking 10 results for matching title: 'Efficient hyperparameter tuning for large scale kernel ridge regression'
       -> INFO: All authors matched!
- Checking reference 78/124:
  -> INFO: Now checking 1 results for matching title: 'Kernel methods through the roof: handling billions of points efficiently'
       -> INFO: All authors matched!
- Checking reference 79/124:
  -> Checking if provided link is pingable: https://link.aps.org/doi/10.1103/PhysRevD.93.044006
  -> INFO: Now checking 10 results for matching title: 'Frequency-domain gravitational waves from nonprecessing black-hole binaries'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Husa', 'Khan', 'Hannam', 'Pürrer', 'Ohme', 'Forteza', 'Bohé', '2016']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://link.aps.org/doi/10.1103/PhysRevD.93.044006 manually and check the results.
        -> Author(s): Sascha Husa, Sebastian Khan, Mark Hannam, Michael Pürrer, Frank Ohme, Xisco Jiménez Forteza, and Alejandro Bohé
        -> Title:     Frequency-domain gravitational waves from nonprecessing black-hole binaries
        -> Year:      2016
     -> Manual search was skipped by the user.
- Checking reference 80/124:
  -> Checking if provided link is pingable: https://link.aps.org/doi/10.1103/PhysRevD.93.044007
  -> INFO: Now checking 10 results for matching title: 'Frequency-domain gravitational waves from nonprecessing black-hole binaries'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Khan', 'Husa', 'Hannam', 'Ohme', 'Pürrer', 'Forteza', 'Bohé', '2016']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://link.aps.org/doi/10.1103/PhysRevD.93.044007 manually and check the results.
        -> Author(s): Sebastian Khan, Sascha Husa, Mark Hannam, Frank Ohme, Michael Pürrer, Xisco Jiménez Forteza, and Alejandro Bohé
        -> Title:     Frequency-domain gravitational waves from nonprecessing black-hole binaries
        -> Year:      2016
     -> Manual search was skipped by the user.
- Checking reference 81/124:
  -> INFO: Now checking 2 results for matching title: 'LVK Algorithm Library - LALSuite'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Collaboration', 'Collaboration', 'Collaboration', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=LVK+Algorithm+Library+-+LALSuite manually and check the results.
        -> Author(s): LIGO Scientific Collaboration, Virgo Collaboration, and KAGRA Collaboration
        -> Title:     LVK Algorithm Library - LALSuite
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 82/124:
  -> INFO: Now checking 10 results for matching title: 'Gravitational wave bursts from cosmic strings'
       -> INFO: All authors matched!
- Checking reference 83/124:
  -> INFO: Now checking 10 results for matching title: 'Gravitational wave bursts from cusps and kinks on cosmic strings'
       -> INFO: All authors matched!
- Checking reference 84/124:
  -> INFO: Now checking 10 results for matching title: 'Gravitational wave background from kink-kink collisions on infinite cosmic strings'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Matsui', 'Kuroyanagi', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gravitational+wave+background+from+kink-kink+collisions+on+infinite+cosmic+strings manually and check the results.
        -> Author(s): Yuka Matsui and Sachiko Kuroyanagi
        -> Title:     Gravitational wave background from kink-kink collisions on infinite cosmic strings
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 85/124:
  -> INFO: Now checking 10 results for matching title: 'Search for gravitational-wave bursts in LIGO data from the fourth science run'
       -> WARNING: Not all 447 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Adhikari, Agresti, Ajith, Allen, Amin, Anderson, Anderson, Arain, Araya, Armandula, Ashley, Aston, Aufmuth, Aulbert, Babak, Ballmer, Bantilan, Barish, Barker, Barker, Barr, Barriga, Barton, Bayer, Belczynski, Betzwieser, Beyersdorf, Bhawal, Bilenko, Billingsley, Biswas, Black, Blackburn, Blackburn, Blair, Bland, Bogenstahl, Bogue, Bork, Boschi, Bose, Brady, Braginsky, Brau, Brinkmann, Brooks, Brown, Bullington, Bunkowski, Buonanno, Burmeister, Busby, Byer, Cadonati, Cagnoli, Camp, Cannizzo, Cannon, Cantley, Cao, Cárdenas, Casey, Castaldi, Cepeda, Chalkey, Charlton, Chatterji, Chelkowski, Chen, Chiadini, Chin, Chin, Chow, Christensen, Clark, Cochrane, Cokelaer, Colacino, Coldwell, Conte, Cook, Corbitt, Coward, Coyne, Creighton, Creighton, Croce, Crooks, Cruise, Cumming, Dalrymple, D'ambrosio, Danzmann, Davies, DeBra, Degallaix, Degree, Demma, Dergachev, Desai, DeSalvo, Dhurandhar, Díaz, Dickson, Credico, Diederichs, Dietz, Doomes, Drever, Dumas, Dupuis, Dwyer, Ehrens, Espinoza, Etzel, Evans, Evans, Fairhurst, Fan, Fazi, Fejer, Finn, Fiumara, Fotopoulos, Franzen, Franzén, Freise, Frey, Fricke, Fritschel, Frolov, Fyffe, Galdi, Garofoli, Gholami, Giaime, Giampanis, Giardina, Goda, Goetz, Goggin, González, Gossler, Grant, Gras, Gray, Gray, Greenhalgh, Gretarsson, Grosso, Grote, Grunewald, Guenther, Gustafson, Hage, Hammer, Hanna, Hanson, Harms, Harry, Harstad, Hayler, Heefner, Heng, Heptonstall, Heurs, Hewitson, Hild, Hirose, Hoak, Hosken, Hough, Howell, Hoyland, Huttner, Ingram, Innerhofer, Ito, Itoh, Ivanov, Jackrel, Johnson, Johnson, Jones, Jones, Jones, Ju, Kalmus, Kalogera, Kasprzyk, Katsavounidis, Kawabe, Kawamura, Kawazoe, Kells, Keppel, Khalili, Kim, King, Kissel, Klimenko, Kokeyama, Kondrashov, Kopparapu, Kozak, Krishnan, Kwee, Lam, Landry, Lantz, Lazzarini, Lee, Lei, Leiner, Leonhardt, Leonor, Libbrecht, Lindquist, Lockerbie, Longo, Lormand, Lubinski, Lück, Machenschalk, Macinnis, Mageswaran, Mailand, Malec, Mandic, Maranò, Márka, Markowitz, Maros, Martin, Marx, Mason, Matone, Matta, Mavalvala, McCarthy, McClelland, Mcguire, McHugh, McKenzie, Mcnabb, McWilliams, Meier, Melissinos, Mendell, Mercer, Meshkov, Messaritaki, Messenger, Meyers, Mikhailov, Mitra, Mitrofanov, Mitselmakher, Mittleman, Miyakawa, Mohanty, Moreno, Mossavi, Mow-Lowry, Moylan, Mudge, Mueller, Mukherjee, Müller-Ebhardt, Munch, Murray, Myers, Myers, Nash, Newton, Nishizawa, Numata, O'Reilly, O'Shaughnessy, Ottaway, Overmier, Owen, Pan, Papa, Parameshwaraiah, Patel, Pedraza, Pelc, Penn, Pierro, Pinto, Pitkin, Pletsch, Plissi, Postiglione, Prix, Quetschke, Raab, Rabeling, Radkins, Rahkola, Rainer, Rakhmanov, Ramsunder, Rawlins, Ray-Majumder, Re, Rehbein, Reid, Reitze, Ribichini, Riesen, Riles, Rivera, Robertson, Robinson, Robinson, Roddy, Rodriguez, Rogan, Rollins, Romano, Romie, Route, Rowan, Rüdiger, Ruet, Russell, Ryan, Sakata, Samidi, Jordana, Sandberg, Sannibale, Saraf, Sarin, Sathyaprakash, Sato, Saulson, Savage, Savov, Schediwy, Schilling, Schnabel, Schofield, Schutz, Schwinberg, Scott, Searle, Sears, Seifert, Sellers, Sengupta, Shawhan, Shoemaker, Sibley, Sidles, Siemens, Sigg, Sinha, Sintes, Slagmolen, Slutsky, Smith, Smith, Somiya, Strain, Strom, Stuver, Summerscales, Sun, Sung, Sutton, Takahashi, Tanner, Tarallo, Taylor, Thacker, Thorne, Thorne, Thüring, Tinto, Tokmakov, Torres, Torrie, Traylor, Trias, Tyler, Ugolini, Ungarelli, Urbanek, Vahlbruch, Vallisneri, Broeck, Varvella, Vass, Vecchio, Veitch, Veitch, Villar, Vorvick, Vyachanin, Waldman, Wallace, Ward, Ward, Watts, Webber, Weidner, Weinert, Weinstein, Weiss, Wen, Wette, Whelan, Whitbeck, Whitcomb, Whiting, Wilkinson, Willems, Williams, Willke, Wilmut, Winkler, Wipf, Wise, Wiseman, Woan, Woods, Wooley, Worden, Wu, Yakushin, Yamamoto, Yan, Yoshida, Yunes, Zanolin, Zhang, Zhang, Zhao, Zotov, Zucker, Mühlen, Zweizig'
       -> INFO: All authors matched!
- Checking reference 86/124:
  -> INFO: Now checking 1 results for matching title: 'Omicron: a tool to characterize transient noise in gravitational-wave detectors'
       -> INFO: All authors matched!
- Checking reference 87/124:
  -> Checking if provided link is pingable: https://openreview.net/forum?id=Bkg6RiCqY7
  -> INFO: Now checking 10 results for matching title: 'Decoupled weight decay regularization'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 88/124:
  -> INFO: Now checking 10 results for matching title: 'Decoupled weight decay regularization'
       -> INFO: All authors matched!
- Checking reference 89/124:
  -> INFO: Now checking 10 results for matching title: 'Imagenet: A largescale hierarchical image database'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Deng', 'Dong', 'Socher', 'Li', 'Li', 'Fei-Fei', '2009']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Imagenet:+A+largescale+hierarchical+image+database manually and check the results.
        -> Author(s): Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei
        -> Title:     Imagenet: A largescale hierarchical image database
        -> Year:      2009
     -> Manual search was skipped by the user.
- Checking reference 90/124:
  -> INFO: Now checking 10 results for matching title: 'Denoising diffusion probabilistic models'
       -> INFO: All authors matched!
- Checking reference 91/124:
  -> INFO: Now checking 10 results for matching title: 'Big transfer (bit): General visual representation learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 92/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2555086
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: University of Helsinki butterfly collection Anniina Mattila bred specimens, February.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Mattila', 'Jiggins', 'Warren', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2555086 manually and check the results.
        -> Author(s): Anniina Mattila, Chris Jiggins, and Ian Warren
        -> Title:     University of Helsinki butterfly collection Anniina Mattila bred specimens, February.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 93/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2735056
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Camilo Salazar and Cambridge butterfly wing collection batch 1, May.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Salazar', 'Montejo-Kovacevich', 'Jiggins', 'Warren', 'Gavins', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2735056 manually and check the results.
        -> Author(s): Camilo Salazar, Gabriela Montejo-Kovacevich, Chris Jiggins, Ian Warren, and Imogen Gavins
        -> Title:     Camilo Salazar and Cambridge butterfly wing collection batch 1, May.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 94/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2553501
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Miscellaneous Heliconius wing photographs (2001-2019) Part 2, February.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Warren', 'Jiggins', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2553501 manually and check the results.
        -> Author(s): Ian Warren and Chris Jiggins
        -> Title:     Miscellaneous Heliconius wing photographs (2001-2019) Part 2, February.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 95/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.5526257
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Heliconius erato cyrbia, Cook Islands (New Zealand) 2016, 2019, 2021, September.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Montejo-Kovacevich', 'Paynter', 'Ghane', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.5526257 manually and check the results.
        -> Author(s): Gabriela Montejo-Kovacevich, Quentin Paynter, and Amin Ghane
        -> Title:     Heliconius erato cyrbia, Cook Islands (New Zealand) 2016, 2019, 2021, September.
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 96/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.4291095
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Cambridge butterfly collection - GMK Broods Ikiam 2018, November.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Montejo-Kovacevich', 'Heijden', 'Jiggins', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.4291095 manually and check the results.
        -> Author(s): Gabriela Montejo-Kovacevich, Eva van der Heijden, and Chris Jiggins
        -> Title:     Cambridge butterfly collection - GMK Broods Ikiam 2018, November.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 97/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2714333
  -> INFO: Now checking 10 results for matching title: 'Cambridge butterfly wing collection batch 9, May.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Montejo-Kovacevich', 'Jiggins', 'Warren', 'Wiltshire', 'Gavins', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2714333 manually and check the results.
        -> Author(s): Gabriela Montejo-Kovacevich, Chris Jiggins, Ian Warren, Eva Wiltshire, and Imogen Gavins
        -> Title:     Cambridge butterfly wing collection batch 9, May.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 98/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2707828
  -> INFO: Now checking 10 results for matching title: 'Cambridge butterfly wing collection batch 8, May.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Montejo-Kovacevich', 'Jiggins', 'Warren', 'Wiltshire', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2707828 manually and check the results.
        -> Author(s): Gabriela Montejo-Kovacevich, Chris Jiggins, Ian Warren, and Eva Wiltshire
        -> Title:     Cambridge butterfly wing collection batch 8, May.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 99/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.5561246
  -> INFO: Now checking 5 results for matching title: 'Brazilian Butterflies Collected December 2020 to January 2021, February.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Castro', 'Jiggins', 'Silva-Brand˘00e3o', 'Freitas', 'Cardoso', 'Heijden', 'Meier', 'Warren', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.5561246 manually and check the results.
        -> Author(s): Erika Pinheiro de Castro, Christopher Jiggins, Karina Lucas da Silva-Brand˘00e3o, Andre Victor Lucci Freitas, Marcio Zikan Cardoso, Eva Van Der Heijden, Joana Meier, and Ian Warren
        -> Title:     Brazilian Butterflies Collected December 2020 to January 2021, February.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 100/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2548678
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Cambridge butterfly wing collection - Patricio Salazar PhD wild and bred specimens batch 2, January.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Salazar', 'Montejo-Kovacevich', 'Warren', 'Jiggins', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2548678 manually and check the results.
        -> Author(s): Patricio Salazar, Gabriela Montejo-Kovacevich, Ian Warren, and Chris Jiggins
        -> Title:     Cambridge butterfly wing collection - Patricio Salazar PhD wild and bred specimens batch 2, January.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 101/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2702457
  -> INFO: Now checking 10 results for matching title: 'Cambridge butterfly wing collection batch 7, May.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Montejo-Kovacevich', 'Jiggins', 'Warren', 'Wiltshire', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2702457 manually and check the results.
        -> Author(s): Gabriela Montejo-Kovacevich, Chris Jiggins, Ian Warren, and Eva Wiltshire
        -> Title:     Cambridge butterfly wing collection batch 7, May.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 102/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.1748277
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Cambridge butterfly wing collection - Patricio Salazar PhD wild and bred specimens batch 1, December.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Salazar', 'Montejo-Kovacevich', 'Warren', 'Jiggins', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.1748277 manually and check the results.
        -> Author(s): Patricio Salazar, Gabriela Montejo-Kovacevich, Ian Warren, and Chris Jiggins
        -> Title:     Cambridge butterfly wing collection - Patricio Salazar PhD wild and bred specimens batch 1, December.
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 103/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2813153
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Cambridge and collaborators butterfly wing collection batch 10, May.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Montejo-Kovacevich', 'Jiggins', 'Warren', 'Salazar', 'Elias', 'Gavins', 'Wiltshire', 'Montgomery', 'McMillan', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2813153 manually and check the results.
        -> Author(s): Gabriela Montejo-Kovacevich, Chris Jiggins, Ian Warren, Camilo Salazar, Marianne Elias, Imogen Gavins, Eva Wiltshire, Stephen Montgomery, and Owen McMillan
        -> Title:     Cambridge and collaborators butterfly wing collection batch 10, May.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 104/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.3082688
  -> INFO: Now checking 3 results for matching title: 'Cambridge butterfly wing collection batch 1- version 2, May.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Montejo-Kovacevich', 'Jiggins', 'Warren', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.3082688 manually and check the results.
        -> Author(s): Gabriela Montejo-Kovacevich, Chris Jiggins, and Ian Warren
        -> Title:     Cambridge butterfly wing collection batch 1- version 2, May.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 105/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.4153502
  -> INFO: Now checking 1 results for matching title: 'Cambridge butterfly wing collection - Patricio Salazar PhD wild specimens batch 3, October.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Meier', 'Salazar', 'Montejo-Kovacevich', 'Warren', 'Jggins', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.4153502 manually and check the results.
        -> Author(s): Joana I Meier, Patricio Salazar, Gabriela Montejo-Kovacevich, Ian Warren, and Chris Jggins
        -> Title:     Cambridge butterfly wing collection - Patricio Salazar PhD wild specimens batch 3, October.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 106/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2550097
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Cambridge butterfly wing collection - Chris Jiggins 2001/2 broods batch 2, January.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jiggins', 'Warren', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2550097 manually and check the results.
        -> Author(s): Chris Jiggins and Ian Warren
        -> Title:     Cambridge butterfly wing collection - Chris Jiggins 2001/2 broods batch 2, January.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 107/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2549524
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Cambridge butterfly wing collection - Chris Jiggins 2001/2 broods batch 1, January.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jiggins', 'Warren', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2549524 manually and check the results.
        -> Author(s): Chris Jiggins and Ian Warren
        -> Title:     Cambridge butterfly wing collection - Chris Jiggins 2001/2 broods batch 1, January.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 108/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2686762
  -> INFO: Now checking 10 results for matching title: 'Cambridge butterfly wing collection batch 6, May.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Montejo-Kovacevich', 'Jiggins', 'Warren', 'Wiltshire', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2686762 manually and check the results.
        -> Author(s): Gabriela Montejo-Kovacevich, Chris Jiggins, Ian Warren, and Eva Wiltshire
        -> Title:     Cambridge butterfly wing collection batch 6, May.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 109/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2553977
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Miscellaneous Heliconius wing photographs (2001-2019) Part 3, February.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Warren', 'Jiggins', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2553977 manually and check the results.
        -> Author(s): Ian Warren and Chris Jiggins
        -> Title:     Miscellaneous Heliconius wing photographs (2001-2019) Part 3, February.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 110/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2552371
  -> INFO: Now checking 1 results for matching title: 'Miscellaneous Heliconius wing photographs (2001-2019) Part 1, February.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Warren', 'Jiggins', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2552371 manually and check the results.
        -> Author(s): Ian Warren and Chris Jiggins
        -> Title:     Miscellaneous Heliconius wing photographs (2001-2019) Part 1, February.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 111/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2684906
  -> INFO: Now checking 10 results for matching title: 'Cambridge butterfly wing collection batch 5, May.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Montejo-Kovacevich', 'Jiggins', 'Warren', 'Wiltshire', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2684906 manually and check the results.
        -> Author(s): Gabriela Montejo-Kovacevich, Chris Jiggins, Ian Warren, and Eva Wiltshire
        -> Title:     Cambridge butterfly wing collection batch 5, May.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 112/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2682458
  -> INFO: Now checking 10 results for matching title: 'Cambridge butterfly wing collection batch 3, May.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jiggins', 'Montejo-Kovacevich', 'Warren', 'Wiltshire', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2682458 manually and check the results.
        -> Author(s): Chris Jiggins, Gabriela Montejo-Kovacevich, Ian Warren, and Eva Wiltshire
        -> Title:     Cambridge butterfly wing collection batch 3, May.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 113/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.2677821
  -> INFO: Now checking 10 results for matching title: 'Cambridge butterfly wing collection batch 2, May.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Montejo-Kovacevich', 'Jiggins', 'Warren', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.2677821 manually and check the results.
        -> Author(s): Gabriela Montejo-Kovacevich, Chris Jiggins, and Ian Warren
        -> Title:     Cambridge butterfly wing collection batch 2, May.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 114/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.4288311
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Sheffield butterfly wing collection - Patricio Salazar, Nicola Nadeau, Ikiam broods batch 1 and 2, November.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Salazar', 'Nadeau', 'Montejo-Kovacevich', 'Jiggins', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.4288311 manually and check the results.
        -> Author(s): Patricio A Salazar, Nicola Nadeau, Gabriela Montejo-Kovacevich, and Chris Jiggins
        -> Title:     Sheffield butterfly wing collection - Patricio Salazar, Nicola Nadeau, Ikiam broods batch 1 and 2, November.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 115/124:
  -> Checking if provided link is pingable: https://doi.org/10.5281/zenodo.4289223
  -> INFO: Now checking 6 results for matching title: 'Cambridge butterfly wing collection batch 10, November.'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Montejo-Kovacevich', 'Heijden', 'Nadeau', 'Jiggins', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.5281/zenodo.4289223 manually and check the results.
        -> Author(s): Gabriela Montejo-Kovacevich, Eva van der Heijden, Nicola Nadeau, and Chris Jiggins
        -> Title:     Cambridge butterfly wing collection batch 10, November.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 116/124:
  -> INFO: Now checking 2 results for matching title: 'BioCLIP: A Vision Foundation Model for the Tree of Life'
       -> INFO: All authors matched!
- Checking reference 117/124:
  -> INFO: Now checking 10 results for matching title: 'The fréchet distance between multivariate normal distributions'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Dowson', 'Landau', '1982']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+fréchet+distance+between+multivariate+normal+distributions manually and check the results.
        -> Author(s): DC Dowson and BV666017 Landau
        -> Title:     The fréchet distance between multivariate normal distributions
        -> Year:      1982
     -> Manual search was skipped by the user.
- Checking reference 118/124:
  -> INFO: Now checking 3 results for matching title: 'Gans trained by a two time-scale update rule converge to a local nash equilibrium'
       -> INFO: All authors matched!
- Checking reference 119/124:
  -> INFO: Now checking 10 results for matching title: 'An efficient permutation-based kernel two-sample test'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chatalic', 'Letizia', 'Schreuder', 'Rosasco', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=An+efficient+permutation-based+kernel+two-sample+test manually and check the results.
        -> Author(s): Antoine Chatalic, Marco Letizia, Nicolas Schreuder, and Lorenzo Rosasco
        -> Title:     An efficient permutation-based kernel two-sample test
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 120/124:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Do imagenet classifiers generalize to imagenet? In International conference on machine learning, pages 5389–5400
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Recht', 'Roelofs', 'Schmidt', 'Shankar', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Do+imagenet+classifiers+generalize+to+imagenet?+In+International+conference+on+machine+learning%2C+pages+5389–5400 manually and check the results.
        -> Author(s): Benjamin Recht, Rebecca Roelofs, Ludwig Schmidt, and Vaishaal Shankar
        -> Title:     Do imagenet classifiers generalize to imagenet? In International conference on machine learning, pages 5389–5400
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 121/124:
  -> INFO: Now checking 10 results for matching title: 'Learning deep kernels for non-parametric two-sample tests'
       -> INFO: All authors matched!
- Checking reference 122/124:
  -> INFO: Now checking 5 results for matching title: 'Observation of a New Boson at a Mass of 125 GeV with the CMS Experiment at the LHC'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 123/124:
  -> INFO: Now checking 5 results for matching title: 'Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 124/124:
  -> Checking if provided link is pingable: https://opendata.cern.ch/.Dataset|R||D|fS
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: range (%)synthetic10,0002,0000.5 - 10astronomy20,0004,0000.5 - 10particle physics50,00010,0000.1 - 2histology6,2965002.5 - 20images (cifar-10)9,0001,8001 - 10genomics1,7641005 - 20table 1: the reference dataset size, observed dataset size, and range of injected anomaly fractions(relative to the background component in d) for each dataset considered in our study
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['data', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=range+(%)synthetic10%2C0002%2C0000.5+-+10astronomy20%2C0004%2C0000.5+-+10particle+physics50%2C00010%2C0000.1+-+2histology6%2C2965002.5+-+20images+(cifar-10)9%2C0001%2C8001+-+10genomics1%2C7641005+-+20table+1:+the+reference+dataset+size%2C+observed+dataset+size%2C+and+range+of+injected+anomaly+fractions(relative+to+the+background+component+in+d)+for+each+dataset+considered+in+our+study manually and check the results.
        -> Author(s): Cms open data
        -> Title:     range (%)synthetic10,0002,0000.5 - 10astronomy20,0004,0000.5 - 10particle physics50,00010,0000.1 - 2histology6,2965002.5 - 20images (cifar-10)9,0001,8001 - 10genomics1,7641005 - 20table 1: the reference dataset size, observed dataset size, and range of injected anomaly fractions(relative to the background component in d) for each dataset considered in our study
        -> Year:      0
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 3: LSimCLR = −
-> Invalid unicode use found on p. 3: LSupCon = −
-> Invalid unicode use found on p. 4: wR(1 −y) log
-> Invalid unicode use found on p. 4: 1 + e−fw
-> Invalid unicode use found on p. 4: tNP(D) = −2
-> Invalid unicode use found on p. 4: wR(1 −y)
-> Invalid unicode use found on p. 4: w(x) −1
-> Invalid unicode use found on p. 4: −yf ˆ
-> Invalid unicode use found on p. 5: obscure the discriminating variables. The contrastive embedding is trained on N −1 clusters with
-> Invalid unicode use found on p. 7: H0 −χ2
-> Invalid unicode use found on p. 7: mini(x −µi)T Σ−1
-> Invalid unicode use found on p. 7: i (x −µi), and we define the test statistic as tMaha(D) = P
-> Invalid unicode use found on p. 27: two electrons and two muons (pp →H →e+e−e+e−, µ+µ−µ+µ−, or µ+µ−e+e−). The Higgs
-> Invalid unicode use found on p. 28: one opposite-sign pair of electrons or muons with invariant mass (mℓ+ℓ−) greater than 12 GeV. In the
-> Invalid unicode use found on p. 29: delta log-likelihood test statistic obtained from the two fits: ∆log L = log LS+B −log LB.
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 295 sentences on 10 pages -> Avg. of 33.77777777777778 sentences per page
-> Warning: Reference '77' never used in the document's text.
-> Warning: Reference '78' never used in the document's text.
-> Warning: Reference '79' never used in the document's text.
-> Warning: Reference '80' never used in the document's text.
-> Warning: Reference '81' never used in the document's text.
-> Warning: Reference '82' never used in the document's text.
-> Warning: Reference '83' never used in the document's text.
-> Warning: Reference '84' never used in the document's text.
-> Warning: Reference '85' never used in the document's text.
-> Warning: Reference '86' never used in the document's text.
-> Warning: Reference '87' never used in the document's text.
-> Warning: Reference '88' never used in the document's text.
-> Warning: Reference '89' never used in the document's text.
-> Warning: Reference '90' never used in the document's text.
-> Warning: Reference '91' never used in the document's text.
-> Warning: Reference '92' never used in the document's text.
-> Warning: Reference '93' never used in the document's text.
-> Warning: Reference '94' never used in the document's text.
-> Warning: Reference '95' never used in the document's text.
-> Warning: Reference '96' never used in the document's text.
-> Warning: Reference '97' never used in the document's text.
-> Warning: Reference '98' never used in the document's text.
-> Warning: Reference '99' never used in the document's text.
-> Warning: Reference '100' never used in the document's text.
-> Warning: Reference '101' never used in the document's text.
-> Warning: Reference '102' never used in the document's text.
-> Warning: Reference '103' never used in the document's text.
-> Warning: Reference '104' never used in the document's text.
-> Warning: Reference '105' never used in the document's text.
-> Warning: Reference '106' never used in the document's text.
-> Warning: Reference '107' never used in the document's text.
-> Warning: Reference '108' never used in the document's text.
-> Warning: Reference '109' never used in the document's text.
-> Warning: Reference '110' never used in the document's text.
-> Warning: Reference '111' never used in the document's text.
-> Warning: Reference '112' never used in the document's text.
-> Warning: Reference '113' never used in the document's text.
-> Warning: Reference '114' never used in the document's text.
-> Warning: Reference '115' never used in the document's text.
-> Warning: Reference '116' never used in the document's text.
-> Warning: Reference '117' never used in the document's text.
-> Warning: Reference '118' never used in the document's text.
-> Warning: Reference '119' never used in the document's text.
-> Warning: Reference '120' never used in the document's text.
-> Warning: Reference '121' never used in the document's text.
-> Warning: Reference '122' never used in the document's text.
-> Warning: Reference '123' never used in the document's text.
-> Warning: Reference '124' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
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
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
  // LLM calling counter = 17
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
  // LLM calling counter = 18
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
  // LLM calling counter = 19
  => WARNING: A Syntax Error occured during parsing: invalid syntax. Perhaps you forgot a comma? (<string>, line 1)
     Structurally parsing response as string: [(" To mitigate this feature and make the model more robust, we adopt an extended version of the algorithm introduced in [53], where multiple widths are considered and combined to obtain a final p-value", True, "supports"), (" The authors of [53] explore several options for combining the tests based on "local" p-values, but in this work we choose the average of p-values as a rule", True, "not enough information")]
  -> LLM list extracted as follows:
[['but in this work we choose the average of p-values as a rule', 'True', 'not enough information")'], ['but in this work we choose the average of p-values as a rule', 'True', 'not enough information")'], ['but in this work we choose the average of p-values as a rule', 'True', 'not enough information")']]
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
  // LLM calling counter = 20
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
-> Missing an abstract for reference with index 57 (Ref. ID = 58); Skipping LLM check...
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
  // LLM calling counter = 21
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 61 (Ref. ID = 62); Skipping LLM check...
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
-> Missing an abstract for reference with index 65 (Ref. ID = 66); Skipping LLM check...
  // LLM calling counter = 22
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 67 (Ref. ID = 68); Skipping LLM check...
-> Missing an abstract for reference with index 68 (Ref. ID = 69); Skipping LLM check...
-> Missing an abstract for reference with index 69 (Ref. ID = 70); Skipping LLM check...
  // LLM calling counter = 23
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 71 (Ref. ID = 72); Skipping LLM check...
-> Missing an abstract for reference with index 72 (Ref. ID = 73); Skipping LLM check...
-> Missing an abstract for reference with index 73 (Ref. ID = 74); Skipping LLM check...
-> Missing an abstract for reference with index 74 (Ref. ID = 75); Skipping LLM check...
  // LLM calling counter = 24
  -> Automatic parsing of LLM list worked!
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
-> WARNING: Reference with index 90 (Ref. ID = 91) has no associated sentence!
-> Missing an abstract for reference with index 91 (Ref. ID = 92); Skipping LLM check...
-> Missing an abstract for reference with index 92 (Ref. ID = 93); Skipping LLM check...
-> Missing an abstract for reference with index 93 (Ref. ID = 94); Skipping LLM check...
-> Missing an abstract for reference with index 94 (Ref. ID = 95); Skipping LLM check...
-> Missing an abstract for reference with index 95 (Ref. ID = 96); Skipping LLM check...
-> Missing an abstract for reference with index 96 (Ref. ID = 97); Skipping LLM check...
-> Missing an abstract for reference with index 97 (Ref. ID = 98); Skipping LLM check...
-> Missing an abstract for reference with index 98 (Ref. ID = 99); Skipping LLM check...
-> Missing an abstract for reference with index 99 (Ref. ID = 100); Skipping LLM check...
-> Missing an abstract for reference with index 100 (Ref. ID = 101); Skipping LLM check...
-> Missing an abstract for reference with index 101 (Ref. ID = 102); Skipping LLM check...
-> Missing an abstract for reference with index 102 (Ref. ID = 103); Skipping LLM check...
-> Missing an abstract for reference with index 103 (Ref. ID = 104); Skipping LLM check...
-> Missing an abstract for reference with index 104 (Ref. ID = 105); Skipping LLM check...
-> Missing an abstract for reference with index 105 (Ref. ID = 106); Skipping LLM check...
-> Missing an abstract for reference with index 106 (Ref. ID = 107); Skipping LLM check...
-> Missing an abstract for reference with index 107 (Ref. ID = 108); Skipping LLM check...
-> Missing an abstract for reference with index 108 (Ref. ID = 109); Skipping LLM check...
-> Missing an abstract for reference with index 109 (Ref. ID = 110); Skipping LLM check...
-> Missing an abstract for reference with index 110 (Ref. ID = 111); Skipping LLM check...
-> Missing an abstract for reference with index 111 (Ref. ID = 112); Skipping LLM check...
-> Missing an abstract for reference with index 112 (Ref. ID = 113); Skipping LLM check...
-> Missing an abstract for reference with index 113 (Ref. ID = 114); Skipping LLM check...
-> Missing an abstract for reference with index 114 (Ref. ID = 115); Skipping LLM check...
-> Missing an abstract for reference with index 115 (Ref. ID = 116); Skipping LLM check...
-> Missing an abstract for reference with index 116 (Ref. ID = 117); Skipping LLM check...
-> Missing an abstract for reference with index 117 (Ref. ID = 118); Skipping LLM check...
-> Missing an abstract for reference with index 118 (Ref. ID = 119); Skipping LLM check...
-> Missing an abstract for reference with index 119 (Ref. ID = 120); Skipping LLM check...
-> Missing an abstract for reference with index 120 (Ref. ID = 121); Skipping LLM check...
-> Missing an abstract for reference with index 121 (Ref. ID = 122); Skipping LLM check...
-> Missing an abstract for reference with index 122 (Ref. ID = 123); Skipping LLM check...
-> Missing an abstract for reference with index 123 (Ref. ID = 124); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 6 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 99 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 84 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 30 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 179 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 25
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   6% 0:00:01
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 26
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━  94% 0:00:01
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 27
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 28
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━━━━━━━━  67% 0:00:01
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 29
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━━━━  83% 0:00:01
###############################
# Starting Author Check
###############################
-> Saved chapter_fig on try 1
-> Saved lit_fig on try 1
-> Saved rank_fig on try 1
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\51 AutoSciDACT Automated Scientific Discovery\PAU_results.md
```