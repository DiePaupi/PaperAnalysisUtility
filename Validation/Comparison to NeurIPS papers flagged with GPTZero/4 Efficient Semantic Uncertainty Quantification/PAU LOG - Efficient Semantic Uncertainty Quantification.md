

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\4 Efficient Semantic Uncertainty Quantification\Efficient semantic uncertainty quantification in.pdf"
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
 - 'authoryear_round'  = Authors' names and the year places insince round brackets (e.g., (Speckmann et al., 2025))
                      -> Multiple references are separated by a semicolon (e.g., (Speckmann et al. 2025; Janiesch et al. 2021))
                      -> Please note that the author and year are *not* separated
 - 'authoryear_square' = Authors' names and the year places insince square brackets (e.g., [Speckmann et al., 2025])
                      -> Multiple references are separated by a comma (e.g., [Speckmann et al., 2025, Janiesch et al., 2021])
                      -> Please note that the author and year are also separated by a comma
Enter a supported referencing template (['numeric', 'authoryear_round', 'authoryear_square']): numeric
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Estimating the predictive uncertainty of free-form responses' on page 2
- Found following heading '3 - Methods' on page 3
- Found following heading '4 - Related Work' on page 7
- Found following heading '5 - Experiments' on page 8
- Found following heading '6 - Discussion and limitations' on page 9
- Found following heading '7 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Extension to masked diffusion models' on page 16
- Found following appendix 'B - Additional implementation details' on page 17
- Found following appendix 'C - Qualitative case studies' on page 19
- Found following appendix 'D - Mutual information results' on page 21
- Found following appendix 'E - Variance reduction with control variates' on page 21
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 16
All found references: 65
-> Warning: Malformed author string: 'AI@Meta'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                              link  valid
0       1     Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar  ...                                     None
1       2  Yasin Abbasi Yadkori, Ilja Kuzborskij, András ...  ...                                     None
2       3  Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes,...  ...                                     None
3       4        Franz Aichberger, Lily Chen, and John Smith  ...                                     None
4       5                             Jacob Austin and et al  ...                                     None
..    ...                                                ...  ...                               ...    ...
60     61                                     Augustine Kong  ...                                     None
61     62  Ilia Kulikov, Alexander Miller, Kyunghyun Cho,...  ...                                     None
62     63  John Schulman, Filip Wolski, Prafulla Dhariwal...  ...  http://arxiv.org/abs/1707.06347.   None
63     64  Daya Guo, Dejian Yang, Haowei Zhang, Junxiao S...  ...                                     None
64     65                   Ilya Loshchilov and Frank Hutter  ...                                     None

[65 rows x 10 columns]
- Checking reference 1/65:
  -> INFO: Now checking 4 results for matching title: 'Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation'
       -> INFO: All authors matched!
- Checking reference 2/65:
  -> INFO: Now checking 1 results for matching title: 'To believe or not to believe your llm'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Abbasi-Yadkori, Szepesv'ari'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/65:
  -> INFO: Now checking 3 results for matching title: 'The curious case of neural text degeneration'
       -> INFO: All authors matched!
- Checking reference 4/65:
  -> INFO: Now checking 10 results for matching title: 'Semantically diverse language generation'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Aichberger', 'Chen', 'Smith', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Semantically+diverse+language+generation manually and check the results.
        -> Author(s): Franz Aichberger, Lily Chen, and John Smith
        -> Title:     Semantically diverse language generation
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 5/65:
  -> INFO: Now checking 6 results for matching title: 'Diffuseq: Sequence to sequence text generation with diffusion models'
  -> WARNING: None of the 6 results matched the expected title!
  -> INFO: Now checking 335 results for matching title: 'Diffuseq: Sequence to sequence text generation with diffusion models'
  -> WARNING: None of the 335 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Diffuseq:+Sequence+to+sequence+text+generation+with+diffusion+models manually and check the results.
        -> Author(s): Jacob Austin and et al
        -> Title:     Diffuseq: Sequence to sequence text generation with diffusion models
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 6/65:
  -> INFO: Now checking 2 results for matching title: 'Dsp: Diffusion-based span prediction for masked text modeling'
  -> WARNING: None of the 2 results matched the expected title!
  -> INFO: Now checking 998 results for matching title: 'Dsp: Diffusion-based span prediction for masked text modeling'
  -> WARNING: None of the 998 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dsp:+Diffusion-based+span+prediction+for+masked+text+modeling manually and check the results.
        -> Author(s): Nuo Lou and et al
        -> Title:     Dsp: Diffusion-based span prediction for masked text modeling
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 7/65:
  -> INFO: Now checking 10 results for matching title: 'Maskgpt: Uniform denoising diffusion for language'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Shi', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Maskgpt:+Uniform+denoising+diffusion+for+language manually and check the results.
        -> Author(s): Sheng Shi and et al
        -> Title:     Maskgpt: Uniform denoising diffusion for language
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 8/65:
  -> INFO: Now checking 10 results for matching title: 'inatk: Iterative noise aware text denoising'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sahoo', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=inatk:+Iterative+noise+aware+text+denoising manually and check the results.
        -> Author(s): A  Sahoo and et al
        -> Title:     inatk: Iterative noise aware text denoising
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 9/65:
  -> INFO: Now checking 3 results for matching title: 'Tuqdm: Token unmasking with quantized diffusion models'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ou', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Tuqdm:+Token+unmasking+with+quantized+diffusion+models manually and check the results.
        -> Author(s): X  Ou and et al
        -> Title:     Tuqdm: Token unmasking with quantized diffusion models
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 10/65:
  -> INFO: Now checking 9 results for matching title: 'Llada: Large language auto-diffusion for accelerated denoising'
  -> WARNING: None of the 9 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Nie', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Llada:+Large+language+auto-diffusion+for+accelerated+denoising manually and check the results.
        -> Author(s): Yuxin Nie and et al
        -> Title:     Llada: Large language auto-diffusion for accelerated denoising
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 11/65:
  -> INFO: Now checking 1 results for matching title: 'A broad-coverage challenge corpus for sentence understanding through inference'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/65:
  -> INFO: Now checking 10 results for matching title: 'Deberta: Decoding-enhanced bert with disentangled attention'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/65:
  -> INFO: Now checking 1 results for matching title: 'Glue: A multi-task benchmark and analysis platform for natural language understanding'
       -> INFO: All authors matched!
- Checking reference 14/65:
  -> INFO: Now checking 1 results for matching title: 'Triviaqa: A large scale distantly supervised challenge for reading comprehension'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Joshi', 'Choi', 'Weld', 'Zettlemoyer', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Triviaqa:+A+large+scale+distantly+supervised+challenge+for+reading+comprehension manually and check the results.
        -> Author(s): Mandar Joshi, Eunsol Choi, Daniel S  Weld, and Luke Zettlemoyer
        -> Title:     Triviaqa: A large scale distantly supervised challenge for reading comprehension
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 15/65:
  -> INFO: Now checking 10 results for matching title: 'Dropout as a bayesian approximation: Representing model uncertainty in deep learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/65:
  -> INFO: Now checking 10 results for matching title: 'Simple and scalable predictive uncertainty estimation using deep ensembles'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/65:
  -> INFO: Now checking 10 results for matching title: 'Predictive uncertainty estimation via prior networks'
       -> INFO: All authors matched!
- Checking reference 18/65:
  -> INFO: Now checking 10 results for matching title: 'Ensemble distribution distillation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Mlodozeniec'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 19/65:
  -> INFO: Now checking 4 results for matching title: 'To trust or not to trust a classifier'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Kim, Gupta'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/65:
  -> INFO: Now checking 10 results for matching title: 'Calibration of text generation models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Desai', 'Durrett', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Calibration+of+text+generation+models manually and check the results.
        -> Author(s): Yayati Desai and Gregory Durrett
        -> Title:     Calibration of text generation models
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 21/65:
  -> INFO: Now checking 10 results for matching title: 'Uncertainty estimation in neural text regression'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Glushkova', 'Kobayashi', 'Suzuki', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Uncertainty+estimation+in+neural+text+regression manually and check the results.
        -> Author(s): Maria Glushkova, Shiori Kobayashi, and Junichi Suzuki
        -> Title:     Uncertainty estimation in neural text regression
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 22/65:
  -> INFO: Now checking 10 results for matching title: 'Uncertainty quantification in abstractive summarization'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Zhou', 'Lopez', 'Snyder', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Uncertainty+quantification+in+abstractive+summarization manually and check the results.
        -> Author(s): Yichao Wang, Bowen Zhou, Adam Lopez, and Benjamin Snyder
        -> Title:     Uncertainty quantification in abstractive summarization
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 23/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2023.emnlp-main.522/.
  -> INFO: Now checking 2 results for matching title: 'Increasing probability mass on answer choices does not always improve accuracy'
       -> INFO: All authors matched!
- Checking reference 24/65:
  -> INFO: Now checking 10 results for matching title: 'Teaching language models to script their confidence'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lin', 'Roller', 'Stewart', 'Zettlemoyer', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Teaching+language+models+to+script+their+confidence manually and check the results.
        -> Author(s): Jason Lin, Stephen Roller, Ashwin Stewart, and Luke Zettlemoyer
        -> Title:     Teaching language models to script their confidence
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 25/65:
  -> INFO: Now checking 10 results for matching title: 'Answer me this: Self-verifying large language models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kadavath', 'Khandelwal', 'Radford', 'Shazeer', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Answer+me+this:+Self-verifying+large+language+models manually and check the results.
        -> Author(s): Srinivasan Kadavath, Urvashi Khandelwal, Alec Radford, and Noam Shazeer
        -> Title:     Answer me this: Self-verifying large language models
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 26/65:
  -> INFO: Now checking 1 results for matching title: 'Evaluating the reliability of self-assessment in language models'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Mielke', 'Akyürek', 'Dusek', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Evaluating+the+reliability+of+self-assessment+in+language+models manually and check the results.
        -> Author(s): Sam Mielke, Elif Akyürek, and Ondˇrej Dusek
        -> Title:     Evaluating the reliability of self-assessment in language models
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 27/65:
  -> INFO: Now checking 10 results for matching title: 'Learning to predict confidence for language models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jain', 'Perez', 'Glass', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Learning+to+predict+confidence+for+language+models manually and check the results.
        -> Author(s): Mohit Jain, Ethan Perez, and James Glass
        -> Title:     Learning to predict confidence for language models
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 28/65:
  -> INFO: Now checking 1 results for matching title: 'Crawling the internal knowledgebase of language models'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Cohen', 'Geva', 'Berant', 'Globerson', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Crawling+the+internal+knowledgebase+of+language+models manually and check the results.
        -> Author(s): Roi Cohen, Mor Geva, Jonathan Berant, and Amir Globerson
        -> Title:     Crawling the internal knowledgebase of language models
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 29/65:
  -> INFO: Now checking 1 results for matching title: 'The capacity for moral self-correction in large language models'
       -> WARNING: Not all 48 authors from the found ref. were matched (only 46)
                   Unmatched authors = 'Lukovsiut.e, Hatfield-Dodds'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/65:
  -> Checking if provided link is pingable: https://proceedings.mlr.press/v239/ren23a.html.
  -> INFO: Now checking 10 results for matching title: 'Self-evaluation improves selective generation in large language models'
       -> INFO: All authors matched!
- Checking reference 31/65:
  -> INFO: Now checking 1 results for matching title: 'Just ask for calibration: Strategies for eliciting calibrated confidence scores from language models fine-tuned with human feedback'
       -> INFO: All authors matched!
- Checking reference 32/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2024.emnlp-main.578/.
  -> INFO: Now checking 1 results for matching title: 'Contextualized sequence likelihood: Enhanced confidence scores for natural language generation'
       -> INFO: All authors matched!
- Checking reference 33/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2024.acl-long.276/.
  -> INFO: Now checking 1 results for matching title: 'Shifting attention to relevance: Towards the predictive uncertainty quantification of free-form large language models'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/65:
  -> INFO: Now checking 1 results for matching title: 'LM vs LM: Detecting factual errors via cross examination'
       -> INFO: All authors matched!
- Checking reference 35/65:
  -> INFO: Now checking 10 results for matching title: 'Conformal prediction in neural forecasting'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Angelopoulos', 'Bates', 'Uhler', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Conformal+prediction+in+neural+forecasting manually and check the results.
        -> Author(s): Alexandros N  Angelopoulos, Stephen Bates, and Caroline Uhler
        -> Title:     Conformal prediction in neural forecasting
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 36/65:
  -> INFO: Now checking 10 results for matching title: 'Well-calibrated language models can be produced with small calibration sets'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ravfogel', 'Zalmanski', 'Goldberg', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Well-calibrated+language+models+can+be+produced+with+small+calibration+sets manually and check the results.
        -> Author(s): Shauli Ravfogel, Shachar Zalmanski, and Yoav Goldberg
        -> Title:     Well-calibrated language models can be produced with small calibration sets
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 37/65:
  -> INFO: Now checking 1 results for matching title: 'Distinguishing the knowable from the unknowable with language models'
       -> INFO: All authors matched!
- Checking reference 38/65:
  -> INFO: Now checking 10 results for matching title: 'Experts don’t cheat: learning what you don’t know by predicting pairs'
       -> INFO: All authors matched!
- Checking reference 39/65:
  -> INFO: Now checking 10 results for matching title: 'Diverse beam search: Decoding diverse solutions from neural sequence models'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 40/65:
  -> INFO: Now checking 10 results for matching title: 'Contrastive decoding: Open-ended text generation as optimization'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 41/65:
  -> INFO: Now checking 4 results for matching title: 'A diversity-promoting objective function for neural conversation models'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 42/65:
  -> INFO: Now checking 1 results for matching title: 'Cluster-based beam search for pointer-generator chatbot grounded by knowledge'
       -> INFO: All authors matched!
- Checking reference 43/65:
  -> Checking if provided link is pingable: https://aclanthology.org/D16-1250/.
  -> INFO: Now checking 1 results for matching title: 'Learning principled bilingual mappings of word embeddings while preserving monolingual invariance'
       -> INFO: All authors matched!
- Checking reference 44/65:
  -> INFO: Now checking 10 results for matching title: 'Comparison of diverse decoding methods from conditional language models'
       -> INFO: All authors matched!
- Checking reference 45/65:
  -> INFO: Now checking 10 results for matching title: 'Paraphrase generation and information retrieval from stored text'
       -> INFO: All authors matched!
- Checking reference 46/65:
  -> INFO: Now checking 10 results for matching title: 'Machine translation evaluation with textual entailment features'
       -> INFO: All authors matched!
- Checking reference 47/65:
  -> INFO: Now checking 1 results for matching title: 'A survey of paraphrasing and textual entailment methods'
       -> INFO: All authors matched!
       -> WARNING: Year (2009) does not match expected year (2010)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/65:
  -> INFO: Now checking 10 results for matching title: 'Semantic similarity based on lexical substitution'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Fernando', 'Stevenson', '2008']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Semantic+similarity+based+on+lexical+substitution manually and check the results.
        -> Author(s): Shyam Fernando and Mark Stevenson
        -> Title:     Semantic similarity based on lexical substitution
        -> Year:      2008
     -> Manual search was skipped by the user.
- Checking reference 49/65:
  -> INFO: Now checking 10 results for matching title: 'Paraphrase identification using deep contextualized representations'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Issa', 'Mohler', 'Johnson', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Paraphrase+identification+using+deep+contextualized+representations manually and check the results.
        -> Author(s): Asma Issa, George Mohler, and John Johnson
        -> Title:     Paraphrase identification using deep contextualized representations
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 50/65:
  -> INFO: Now checking 10 results for matching title: 'Deep paraphrase identification'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yu', 'Dumsmyr', 'Knight', '2014']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+paraphrase+identification manually and check the results.
        -> Author(s): Lei Yu, Jimmy Dumsmyr, and Kevin Knight
        -> Title:     Deep paraphrase identification
        -> Year:      2014
     -> Manual search was skipped by the user.
- Checking reference 51/65:
  -> INFO: Now checking 2 results for matching title: 'Dynamic pooling and unfolding recursive autoencoders for paraphrase detection'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Pennington'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 52/65:
  -> INFO: Now checking 6 results for matching title: 'Reasoning with heterogeneous graph representations for knowledge-aware question answering'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tay', 'Fu', 'Wu', 'Casanueva', 'Liu', 'Wallace', 'Wang', 'Singh', 'McAuley', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Reasoning+with+heterogeneous+graph+representations+for+knowledge-aware+question+answering manually and check the results.
        -> Author(s): Yi Tay, Kelvin Fu, Kai Wu, Ivan Casanueva, Jianfeng Liu, Byron Wallace, Shuohang Wang, Bajrang Singh, and Julian McAuley
        -> Title:     Reasoning with heterogeneous graph representations for knowledge-aware question answering
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 53/65:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Efficient fewshot learning with efl: A single transformer for all tasks
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Bommasani', 'Hendrycks', 'Song', 'Zhang', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Efficient+fewshot+learning+with+efl:+A+single+transformer+for+all+tasks manually and check the results.
        -> Author(s): Alex Wang, Rishi Bommasani, Dan Hendrycks, Daniel Song, and Zhilin Zhang
        -> Title:     Efficient fewshot learning with efl: A single transformer for all tasks
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 54/65:
  -> INFO: Now checking 10 results for matching title: 'Generating with confidence: Uncertainty quantification for black-box large language models'
       -> INFO: All authors matched!
- Checking reference 55/65:
  -> INFO: Now checking 10 results for matching title: 'Coqa: A conversational question answering challenge'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 56/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2022.acl-long.229/.
  -> INFO: Now checking 10 results for matching title: 'TruthfulQA: Measuring how models mimic human falsehoods'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 57/65:
  -> INFO: Now checking 10 results for matching title: 'Ambigqa: Answering ambiguous open-domain questions'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Michael, Hajishirzi, Zettlemoyer'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 58/65:
  -> INFO: Now checking 10 results for matching title: 'Opt: Open pre-trained transformer language models'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Li, Lin, Mihaylov, Ott, Shleifer, Shuster, Simig, Koura, Sridhar, Wang, Zettlemoyer'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/65:
  -> INFO: Now checking 10 results for matching title: 'Llama: Open and efficient foundation language models'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lavril, Izacard, Martinet, Lacroix, Rozière, Goyal, Hambro, Azhar, Rodriguez, Joulin, Grave, Lample'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 60/65:
  -> Checking if provided link is pingable: https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md.
  -> INFO: Now checking 10 results for matching title: 'Llama 3 model card'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['AI@Meta', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Llama+3+model+card manually and check the results.
        -> Author(s): AI@Meta
        -> Title:     Llama 3 model card
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 61/65:
  -> INFO: Now checking 10 results for matching title: 'A note on importance sampling using standardized weights'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kong', '1992']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+note+on+importance+sampling+using+standardized+weights manually and check the results.
        -> Author(s): Augustine Kong
        -> Title:     A note on importance sampling using standardized weights
        -> Year:      1992
     -> Manual search was skipped by the user.
- Checking reference 62/65:
  -> INFO: Now checking 1 results for matching title: 'Importance of search and evaluation strategies in neural dialogue modeling'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 63/65:
  -> Checking if provided link is pingable: http://arxiv.org/abs/1707.06347.
  -> INFO: Now checking 10 results for matching title: 'Proximal policy optimization algorithms'
       -> INFO: All authors matched!
- Checking reference 64/65:
  -> INFO: Now checking 10 results for matching title: 'Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Guo', 'Yang', 'Zhang', 'Song', 'Zhang', 'Xu', 'Zhu', 'Ma', 'Wang', 'Bi', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepseek-r1:+Incentivizing+reasoning+capability+in+llms+via+reinforcement+learning manually and check the results.
        -> Author(s): Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al
        -> Title:     Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 65/65:
  -> INFO: Now checking 10 results for matching title: 'Decoupled weight decay regularization'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 1: = −
-> Invalid unicode use found on p. 2: log q(yt|y<t) = log p(yt|y<t) −λ max
-> Invalid unicode use found on p. 3: ℓ′(next) ←ℓ(next) −λπ
-> Invalid unicode use found on p. 3: log q(y(t)|y(t+1)) = log p(y(t)|y(t+1)) −λ max
-> Invalid unicode use found on p. 5: ˆH = −
-> Invalid unicode use found on p. 6: Denote Yi = −log ˆp(c(s(i))), where c(s(i)) is the cluster containing s(i). The estimator in Equation 10 is then PN
-> Invalid unicode use found on p. 6: i=1 ˜wiYi. Now define Xi = −log p(s(i)), and let X′
-> Invalid unicode use found on p. 6: i = Xi−µX and Y ′
-> Invalid unicode use found on p. 6: i = Yi−µY
-> Invalid unicode use found on p. 6: −α
-> Invalid unicode use found on p. 6: ˜wi,jointYi −αMI
-> Invalid unicode use found on p. 8: numbers are mean±std over 5 jackknife samples of size 200. The symbol “−” indicates that the
-> Invalid unicode use found on p. 15: for t = T−1 downto 0 do
-> Invalid unicode use found on p. 15: ℓ′(next) ←ℓ(next) −λπ
-> Invalid unicode use found on p. 16: pair, (ii) all proper prefixes of the hypothesis (lengths 1 . . . Lh −1) each followed by [TRUNC], and
-> Invalid unicode use found on p. 16: (iii) all proper prefixes of the premise (lengths 1 . . . Lp −1) similarly tagged. A single example with
-> Invalid unicode use found on p. 16: tokenized lengths (Lp, Lh) thus contributes 1 + (Lh −1) + (Lp −1) training instances, covering
-> Invalid unicode use found on p. 17: s∈S E(y≤t, s) −Etarget
-> Invalid unicode use found on p. 17: Var{ ˆH} −Vtarget
-> Invalid unicode use found on p. 17: defined by 1 −E(si, sj) for every pair si, sj of iteratively prompted responses (see Equation 6 for
-> Invalid unicode use found on p. 20: h(Zi) −α
-> Invalid unicode use found on p. 20: g(Zi) −µg
-> Invalid unicode use found on p. 20: is unbiased, because Ep[g(Z) −µg] = 0.
-> Invalid unicode use found on p. 20: g = Var[g(Z)], and σhg = Cov[h(Z), g(Z)]. Writing H = h(Z) −µ and G =
-> Invalid unicode use found on p. 20: g(Z) −µg, we have
-> Invalid unicode use found on p. 20: H −αG
-> Invalid unicode use found on p. 20: h −2α σhg + α2σ2
-> Invalid unicode use found on p. 21: −2σhg + 2ασ2
-> Invalid unicode use found on p. 21: h (1 −ρ2),
-> Invalid unicode use found on p. 21: σhσg is the correlation between h and g, so variance is reduced by the factor 1 −ρ2 such
-> Invalid unicode use found on p. 21: i = Xi −µX with Xi = −log p(s(i))
-> Invalid unicode use found on p. 21: are strongly correlated with the negative cluster probabilities Yi = −log ˆp(c(s(i))), being based on
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 420 sentences on 11 pages -> Avg. of 43.0 sentences per page
-> Warning: Reference '43' never used in the document's text.
-> Warning: Reference '65' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
  // LLM calling counter = 2
  => WARNING: A Syntax Error occured during parsing: unterminated string literal (detected at line 1) (<string>, line 1)
     Structurally parsing response as string: [(" To adapt an off-the-shelf NLI model with minimal overhead, we begin by loading a model finetuned on a natural language understanding dataset such as the MNLI benchmark dataset [11] (e"", True, "supports"), (" In brief, clustering works by querying the DeBERTa-large-MNLI model [12], finetuned on the NLI dataset MNLI [11], on every pair of sampled responses", True, "not enough information")]
  -> Warning: The LLM response has not 3 values per sentence;                 len(response_splitted) % 3 = 1
  -> LLM list extracted as follows:
[['not enough information")', 'on every pair of sampled responses', 'True'], ['not enough information")', 'on every pair of sampled responses', 'True'], ['not enough information")', 'on every pair of sampled responses', 'True']]
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 17
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 18
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
  // LLM calling counter = 19
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
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
  -> Found 25 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 20
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 21
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 22
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 23
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 24
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
###############################
# Starting Author Check
###############################
Resorting to unclean kill browser.
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\4 Efficient Semantic Uncertainty Quantification\PAU_results.md
```

---

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\4 Efficient Semantic Uncertainty Quantification\Efficient semantic uncertainty quantification in.pdf"
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
 - 'authoryear_round'  = Authors' names and the year places insince round brackets (e.g., (Speckmann et al., 2025))
                      -> Multiple references are separated by a semicolon (e.g., (Speckmann et al. 2025; Janiesch et al. 2021))
                      -> Please note that the author and year are *not* separated
 - 'authoryear_square' = Authors' names and the year places insince square brackets (e.g., [Speckmann et al., 2025])
                      -> Multiple references are separated by a comma (e.g., [Speckmann et al., 2025, Janiesch et al., 2021])
                      -> Please note that the author and year are also separated by a comma
Enter a supported referencing template (['numeric', 'authoryear_round', 'authoryear_square']): numeric
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Estimating the predictive uncertainty of free-form responses' on page 2
- Found following heading '3 - Methods' on page 3
- Found following heading '4 - Related Work' on page 7
- Found following heading '5 - Experiments' on page 8
- Found following heading '6 - Discussion and limitations' on page 9
- Found following heading '7 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Extension to masked diffusion models' on page 16
- Found following appendix 'B - Additional implementation details' on page 17
- Found following appendix 'C - Qualitative case studies' on page 19
- Found following appendix 'D - Mutual information results' on page 21
- Found following appendix 'E - Variance reduction with control variates' on page 21
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 16
All found references: 65
-> Warning: Malformed author string: 'AI@Meta'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors                                 normalized_authors  ...                                             outlet                              link  valid
0       1     Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar                     [Kuhn L., Gal Y., Farquhar S.]  ...  International Conference on Learning Represent...                                     None
1       2  Yasin Abbasi Yadkori, Ilja Kuzborskij, András ...  [Yadkori Y., Kuzborskij I., György A., Szepesv...  ...                   arXiv preprint arXiv:2406. 02543                                     None
2       3  Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes,...  [Holtzman A., Buys J., Du L., Forbes M., Choi Y.]  ...                   arXiv preprint arXiv:1904. 09751                                     None
3       4        Franz Aichberger, Lily Chen, and John Smith                 [Aichberger F., Chen L., Smith J.]  ...  International Conference on Learning Represent...                                     None
4       5                             Jacob Austin and et al                                        [Austin J.]  ...                                               ICLR                                     None
..    ...                                                ...                                                ...  ...                                                ...                               ...    ...
60     61                                     Augustine Kong                                          [Kong A.]  ...  University of Chicago, Dept of Statistics, Tec...                                     None
61     62  Ilia Kulikov, Alexander Miller, Kyunghyun Cho,...         [Kulikov I., Miller A., Cho K., Weston J.]  ...                                                                                        None
62     63  John Schulman, Filip Wolski, Prafulla Dhariwal...  [Schulman J., Wolski F., Dhariwal P., Radford ...  ...                                               CoRR  http://arxiv.org/abs/1707.06347.   None
63     64  Daya Guo, Dejian Yang, Haowei Zhang, Junxiao S...  [Guo D., Yang D., Zhang H., Song J., Zhang R.,...  ...                   arXiv preprint arXiv:2501. 12948                                     None
64     65                   Ilya Loshchilov and Frank Hutter                         [Loshchilov I., Hutter F.]  ...                   arXiv preprint arXiv:1711. 05101                                     None

[65 rows x 10 columns]
- Checking reference 1/65:
  -> INFO: Now checking 4 results for matching title: 'Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation'
       -> INFO: All authors matched!
- Checking reference 2/65:
  -> INFO: Now checking 1 results for matching title: 'To believe or not to believe your llm'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Abbasi-Yadkori, Szepesv'ari'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/65:
  -> INFO: Now checking 3 results for matching title: 'The curious case of neural text degeneration'
       -> INFO: All authors matched!
- Checking reference 4/65:
  -> INFO: Now checking 10 results for matching title: 'Semantically diverse language generation'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Aichberger', 'Chen', 'Smith', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Semantically+diverse+language+generation manually and check the results.
        -> Author(s): Franz Aichberger, Lily Chen, and John Smith
        -> Title:     Semantically diverse language generation
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 5/65:
  -> INFO: Now checking 6 results for matching title: 'Diffuseq: Sequence to sequence text generation with diffusion models'
  -> WARNING: None of the 6 results matched the expected title!
  -> INFO: Now checking 335 results for matching title: 'Diffuseq: Sequence to sequence text generation with diffusion models'
  -> WARNING: None of the 335 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Diffuseq:+Sequence+to+sequence+text+generation+with+diffusion+models manually and check the results.
        -> Author(s): Jacob Austin and et al
        -> Title:     Diffuseq: Sequence to sequence text generation with diffusion models
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 6/65:
  -> INFO: Now checking 2 results for matching title: 'Dsp: Diffusion-based span prediction for masked text modeling'
  -> WARNING: None of the 2 results matched the expected title!
  -> INFO: Now checking 998 results for matching title: 'Dsp: Diffusion-based span prediction for masked text modeling'
  -> WARNING: None of the 998 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dsp:+Diffusion-based+span+prediction+for+masked+text+modeling manually and check the results.
        -> Author(s): Nuo Lou and et al
        -> Title:     Dsp: Diffusion-based span prediction for masked text modeling
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 7/65:
  -> INFO: Now checking 10 results for matching title: 'Maskgpt: Uniform denoising diffusion for language'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Shi', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Maskgpt:+Uniform+denoising+diffusion+for+language manually and check the results.
        -> Author(s): Sheng Shi and et al
        -> Title:     Maskgpt: Uniform denoising diffusion for language
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 8/65:
  -> INFO: Now checking 10 results for matching title: 'inatk: Iterative noise aware text denoising'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sahoo', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=inatk:+Iterative+noise+aware+text+denoising manually and check the results.
        -> Author(s): A  Sahoo and et al
        -> Title:     inatk: Iterative noise aware text denoising
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 9/65:
  -> INFO: Now checking 3 results for matching title: 'Tuqdm: Token unmasking with quantized diffusion models'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ou', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Tuqdm:+Token+unmasking+with+quantized+diffusion+models manually and check the results.
        -> Author(s): X  Ou and et al
        -> Title:     Tuqdm: Token unmasking with quantized diffusion models
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 10/65:
  -> INFO: Now checking 9 results for matching title: 'Llada: Large language auto-diffusion for accelerated denoising'
  -> WARNING: None of the 9 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Nie', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Llada:+Large+language+auto-diffusion+for+accelerated+denoising manually and check the results.
        -> Author(s): Yuxin Nie and et al
        -> Title:     Llada: Large language auto-diffusion for accelerated denoising
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 11/65:
  -> INFO: Now checking 1 results for matching title: 'A broad-coverage challenge corpus for sentence understanding through inference'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/65:
  -> INFO: Now checking 10 results for matching title: 'Deberta: Decoding-enhanced bert with disentangled attention'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/65:
  -> INFO: Now checking 1 results for matching title: 'Glue: A multi-task benchmark and analysis platform for natural language understanding'
       -> INFO: All authors matched!
- Checking reference 14/65:
  -> INFO: Now checking 1 results for matching title: 'Triviaqa: A large scale distantly supervised challenge for reading comprehension'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Joshi', 'Choi', 'Weld', 'Zettlemoyer', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Triviaqa:+A+large+scale+distantly+supervised+challenge+for+reading+comprehension manually and check the results.
        -> Author(s): Mandar Joshi, Eunsol Choi, Daniel S  Weld, and Luke Zettlemoyer
        -> Title:     Triviaqa: A large scale distantly supervised challenge for reading comprehension
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 15/65:
  -> INFO: Now checking 10 results for matching title: 'Dropout as a bayesian approximation: Representing model uncertainty in deep learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/65:
  -> INFO: Now checking 10 results for matching title: 'Simple and scalable predictive uncertainty estimation using deep ensembles'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/65:
  -> INFO: Now checking 10 results for matching title: 'Predictive uncertainty estimation via prior networks'
       -> INFO: All authors matched!
- Checking reference 18/65:
  -> INFO: Now checking 10 results for matching title: 'Ensemble distribution distillation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Mlodozeniec'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 19/65:
  -> INFO: Now checking 4 results for matching title: 'To trust or not to trust a classifier'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Kim, Gupta'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/65:
  -> INFO: Now checking 10 results for matching title: 'Calibration of text generation models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Desai', 'Durrett', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Calibration+of+text+generation+models manually and check the results.
        -> Author(s): Yayati Desai and Gregory Durrett
        -> Title:     Calibration of text generation models
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 21/65:
  -> INFO: Now checking 10 results for matching title: 'Uncertainty estimation in neural text regression'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Glushkova', 'Kobayashi', 'Suzuki', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Uncertainty+estimation+in+neural+text+regression manually and check the results.
        -> Author(s): Maria Glushkova, Shiori Kobayashi, and Junichi Suzuki
        -> Title:     Uncertainty estimation in neural text regression
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 22/65:
  -> INFO: Now checking 10 results for matching title: 'Uncertainty quantification in abstractive summarization'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Zhou', 'Lopez', 'Snyder', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Uncertainty+quantification+in+abstractive+summarization manually and check the results.
        -> Author(s): Yichao Wang, Bowen Zhou, Adam Lopez, and Benjamin Snyder
        -> Title:     Uncertainty quantification in abstractive summarization
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 23/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2023.emnlp-main.522/.
  -> INFO: Now checking 2 results for matching title: 'Increasing probability mass on answer choices does not always improve accuracy'
       -> INFO: All authors matched!
- Checking reference 24/65:
  -> INFO: Now checking 10 results for matching title: 'Teaching language models to script their confidence'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lin', 'Roller', 'Stewart', 'Zettlemoyer', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Teaching+language+models+to+script+their+confidence manually and check the results.
        -> Author(s): Jason Lin, Stephen Roller, Ashwin Stewart, and Luke Zettlemoyer
        -> Title:     Teaching language models to script their confidence
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 25/65:
  -> INFO: Now checking 10 results for matching title: 'Answer me this: Self-verifying large language models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kadavath', 'Khandelwal', 'Radford', 'Shazeer', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Answer+me+this:+Self-verifying+large+language+models manually and check the results.
        -> Author(s): Srinivasan Kadavath, Urvashi Khandelwal, Alec Radford, and Noam Shazeer
        -> Title:     Answer me this: Self-verifying large language models
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 26/65:
  -> INFO: Now checking 1 results for matching title: 'Evaluating the reliability of self-assessment in language models'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Mielke', 'Akyürek', 'Dusek', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Evaluating+the+reliability+of+self-assessment+in+language+models manually and check the results.
        -> Author(s): Sam Mielke, Elif Akyürek, and Ondˇrej Dusek
        -> Title:     Evaluating the reliability of self-assessment in language models
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 27/65:
  -> INFO: Now checking 10 results for matching title: 'Learning to predict confidence for language models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jain', 'Perez', 'Glass', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Learning+to+predict+confidence+for+language+models manually and check the results.
        -> Author(s): Mohit Jain, Ethan Perez, and James Glass
        -> Title:     Learning to predict confidence for language models
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 28/65:
  -> INFO: Now checking 1 results for matching title: 'Crawling the internal knowledgebase of language models'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Cohen', 'Geva', 'Berant', 'Globerson', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Crawling+the+internal+knowledgebase+of+language+models manually and check the results.
        -> Author(s): Roi Cohen, Mor Geva, Jonathan Berant, and Amir Globerson
        -> Title:     Crawling the internal knowledgebase of language models
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 29/65:
  -> INFO: Now checking 1 results for matching title: 'The capacity for moral self-correction in large language models'
       -> WARNING: Not all 48 authors from the found ref. were matched (only 46)
                   Unmatched authors = 'Lukovsiut.e, Hatfield-Dodds'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/65:
  -> Checking if provided link is pingable: https://proceedings.mlr.press/v239/ren23a.html.
  -> INFO: Now checking 10 results for matching title: 'Self-evaluation improves selective generation in large language models'
       -> INFO: All authors matched!
- Checking reference 31/65:
  -> INFO: Now checking 1 results for matching title: 'Just ask for calibration: Strategies for eliciting calibrated confidence scores from language models fine-tuned with human feedback'
       -> INFO: All authors matched!
- Checking reference 32/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2024.emnlp-main.578/.
  -> INFO: Now checking 1 results for matching title: 'Contextualized sequence likelihood: Enhanced confidence scores for natural language generation'
       -> INFO: All authors matched!
- Checking reference 33/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2024.acl-long.276/.
  -> INFO: Now checking 1 results for matching title: 'Shifting attention to relevance: Towards the predictive uncertainty quantification of free-form large language models'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/65:
  -> INFO: Now checking 1 results for matching title: 'LM vs LM: Detecting factual errors via cross examination'
       -> INFO: All authors matched!
- Checking reference 35/65:
  -> INFO: Now checking 10 results for matching title: 'Conformal prediction in neural forecasting'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Angelopoulos', 'Bates', 'Uhler', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Conformal+prediction+in+neural+forecasting manually and check the results.
        -> Author(s): Alexandros N  Angelopoulos, Stephen Bates, and Caroline Uhler
        -> Title:     Conformal prediction in neural forecasting
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 36/65:
  -> INFO: Now checking 10 results for matching title: 'Well-calibrated language models can be produced with small calibration sets'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ravfogel', 'Zalmanski', 'Goldberg', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Well-calibrated+language+models+can+be+produced+with+small+calibration+sets manually and check the results.
        -> Author(s): Shauli Ravfogel, Shachar Zalmanski, and Yoav Goldberg
        -> Title:     Well-calibrated language models can be produced with small calibration sets
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 37/65:
  -> INFO: Now checking 1 results for matching title: 'Distinguishing the knowable from the unknowable with language models'
       -> INFO: All authors matched!
- Checking reference 38/65:
  -> INFO: Now checking 10 results for matching title: 'Experts don’t cheat: learning what you don’t know by predicting pairs'
       -> INFO: All authors matched!
- Checking reference 39/65:
  -> INFO: Now checking 10 results for matching title: 'Diverse beam search: Decoding diverse solutions from neural sequence models'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 40/65:
  -> INFO: Now checking 10 results for matching title: 'Contrastive decoding: Open-ended text generation as optimization'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 41/65:
  -> INFO: Now checking 4 results for matching title: 'A diversity-promoting objective function for neural conversation models'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 42/65:
  -> INFO: Now checking 1 results for matching title: 'Cluster-based beam search for pointer-generator chatbot grounded by knowledge'
       -> INFO: All authors matched!
- Checking reference 43/65:
  -> Checking if provided link is pingable: https://aclanthology.org/D16-1250/.
  -> INFO: Now checking 1 results for matching title: 'Learning principled bilingual mappings of word embeddings while preserving monolingual invariance'
       -> INFO: All authors matched!
- Checking reference 44/65:
  -> INFO: Now checking 10 results for matching title: 'Comparison of diverse decoding methods from conditional language models'
       -> INFO: All authors matched!
- Checking reference 45/65:
  -> INFO: Now checking 10 results for matching title: 'Paraphrase generation and information retrieval from stored text'
       -> INFO: All authors matched!
- Checking reference 46/65:
  -> INFO: Now checking 10 results for matching title: 'Machine translation evaluation with textual entailment features'
       -> INFO: All authors matched!
- Checking reference 47/65:
  -> INFO: Now checking 1 results for matching title: 'A survey of paraphrasing and textual entailment methods'
       -> INFO: All authors matched!
       -> WARNING: Year (2009) does not match expected year (2010)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/65:
  -> INFO: Now checking 10 results for matching title: 'Semantic similarity based on lexical substitution'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Fernando', 'Stevenson', '2008']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Semantic+similarity+based+on+lexical+substitution manually and check the results.
        -> Author(s): Shyam Fernando and Mark Stevenson
        -> Title:     Semantic similarity based on lexical substitution
        -> Year:      2008
     -> Manual search was skipped by the user.
- Checking reference 49/65:
  -> INFO: Now checking 10 results for matching title: 'Paraphrase identification using deep contextualized representations'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Issa', 'Mohler', 'Johnson', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Paraphrase+identification+using+deep+contextualized+representations manually and check the results.
        -> Author(s): Asma Issa, George Mohler, and John Johnson
        -> Title:     Paraphrase identification using deep contextualized representations
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 50/65:
  -> INFO: Now checking 10 results for matching title: 'Deep paraphrase identification'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yu', 'Dumsmyr', 'Knight', '2014']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+paraphrase+identification manually and check the results.
        -> Author(s): Lei Yu, Jimmy Dumsmyr, and Kevin Knight
        -> Title:     Deep paraphrase identification
        -> Year:      2014
     -> Manual search was skipped by the user.
- Checking reference 51/65:
  -> INFO: Now checking 2 results for matching title: 'Dynamic pooling and unfolding recursive autoencoders for paraphrase detection'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Pennington'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 52/65:
  -> INFO: Now checking 6 results for matching title: 'Reasoning with heterogeneous graph representations for knowledge-aware question answering'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tay', 'Fu', 'Wu', 'Casanueva', 'Liu', 'Wallace', 'Wang', 'Singh', 'McAuley', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Reasoning+with+heterogeneous+graph+representations+for+knowledge-aware+question+answering manually and check the results.
        -> Author(s): Yi Tay, Kelvin Fu, Kai Wu, Ivan Casanueva, Jianfeng Liu, Byron Wallace, Shuohang Wang, Bajrang Singh, and Julian McAuley
        -> Title:     Reasoning with heterogeneous graph representations for knowledge-aware question answering
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 53/65:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Efficient fewshot learning with efl: A single transformer for all tasks
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Bommasani', 'Hendrycks', 'Song', 'Zhang', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Efficient+fewshot+learning+with+efl:+A+single+transformer+for+all+tasks manually and check the results.
        -> Author(s): Alex Wang, Rishi Bommasani, Dan Hendrycks, Daniel Song, and Zhilin Zhang
        -> Title:     Efficient fewshot learning with efl: A single transformer for all tasks
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 54/65:
  -> INFO: Now checking 10 results for matching title: 'Generating with confidence: Uncertainty quantification for black-box large language models'
       -> INFO: All authors matched!
- Checking reference 55/65:
  -> INFO: Now checking 10 results for matching title: 'Coqa: A conversational question answering challenge'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 56/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2022.acl-long.229/.
  -> INFO: Now checking 10 results for matching title: 'TruthfulQA: Measuring how models mimic human falsehoods'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 57/65:
  -> INFO: Now checking 10 results for matching title: 'Ambigqa: Answering ambiguous open-domain questions'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Michael, Hajishirzi, Zettlemoyer'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 58/65:
  -> INFO: Now checking 10 results for matching title: 'Opt: Open pre-trained transformer language models'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Li, Lin, Mihaylov, Ott, Shleifer, Shuster, Simig, Koura, Sridhar, Wang, Zettlemoyer'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/65:
  -> INFO: Now checking 10 results for matching title: 'Llama: Open and efficient foundation language models'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lavril, Izacard, Martinet, Lacroix, Rozière, Goyal, Hambro, Azhar, Rodriguez, Joulin, Grave, Lample'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 60/65:
  -> Checking if provided link is pingable: https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md.
  -> INFO: Now checking 10 results for matching title: 'Llama 3 model card'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['AI@Meta', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Llama+3+model+card manually and check the results.
        -> Author(s): AI@Meta
        -> Title:     Llama 3 model card
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 61/65:
  -> INFO: Now checking 10 results for matching title: 'A note on importance sampling using standardized weights'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kong', '1992']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+note+on+importance+sampling+using+standardized+weights manually and check the results.
        -> Author(s): Augustine Kong
        -> Title:     A note on importance sampling using standardized weights
        -> Year:      1992
     -> Manual search was skipped by the user.
- Checking reference 62/65:
  -> INFO: Now checking 1 results for matching title: 'Importance of search and evaluation strategies in neural dialogue modeling'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 63/65:
  -> Checking if provided link is pingable: http://arxiv.org/abs/1707.06347.
  -> INFO: Now checking 10 results for matching title: 'Proximal policy optimization algorithms'
       -> INFO: All authors matched!
- Checking reference 64/65:
  -> INFO: Now checking 10 results for matching title: 'Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Guo', 'Yang', 'Zhang', 'Song', 'Zhang', 'Xu', 'Zhu', 'Ma', 'Wang', 'Bi', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepseek-r1:+Incentivizing+reasoning+capability+in+llms+via+reinforcement+learning manually and check the results.
        -> Author(s): Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al
        -> Title:     Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 65/65:
  -> INFO: Now checking 10 results for matching title: 'Decoupled weight decay regularization'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 1: = −
-> Invalid unicode use found on p. 2: log q(yt|y<t) = log p(yt|y<t) −λ max
-> Invalid unicode use found on p. 3: ℓ′(next) ←ℓ(next) −λπ
-> Invalid unicode use found on p. 3: log q(y(t)|y(t+1)) = log p(y(t)|y(t+1)) −λ max
-> Invalid unicode use found on p. 5: ˆH = −
-> Invalid unicode use found on p. 6: Denote Yi = −log ˆp(c(s(i))), where c(s(i)) is the cluster containing s(i). The estimator in Equation 10 is then PN
-> Invalid unicode use found on p. 6: i=1 ˜wiYi. Now define Xi = −log p(s(i)), and let X′
-> Invalid unicode use found on p. 6: i = Xi−µX and Y ′
-> Invalid unicode use found on p. 6: i = Yi−µY
-> Invalid unicode use found on p. 6: −α
-> Invalid unicode use found on p. 6: ˜wi,jointYi −αMI
-> Invalid unicode use found on p. 8: numbers are mean±std over 5 jackknife samples of size 200. The symbol “−” indicates that the
-> Invalid unicode use found on p. 15: for t = T−1 downto 0 do
-> Invalid unicode use found on p. 15: ℓ′(next) ←ℓ(next) −λπ
-> Invalid unicode use found on p. 16: pair, (ii) all proper prefixes of the hypothesis (lengths 1 . . . Lh −1) each followed by [TRUNC], and
-> Invalid unicode use found on p. 16: (iii) all proper prefixes of the premise (lengths 1 . . . Lp −1) similarly tagged. A single example with
-> Invalid unicode use found on p. 16: tokenized lengths (Lp, Lh) thus contributes 1 + (Lh −1) + (Lp −1) training instances, covering
-> Invalid unicode use found on p. 17: s∈S E(y≤t, s) −Etarget
-> Invalid unicode use found on p. 17: Var{ ˆH} −Vtarget
-> Invalid unicode use found on p. 17: defined by 1 −E(si, sj) for every pair si, sj of iteratively prompted responses (see Equation 6 for
-> Invalid unicode use found on p. 20: h(Zi) −α
-> Invalid unicode use found on p. 20: g(Zi) −µg
-> Invalid unicode use found on p. 20: is unbiased, because Ep[g(Z) −µg] = 0.
-> Invalid unicode use found on p. 20: g = Var[g(Z)], and σhg = Cov[h(Z), g(Z)]. Writing H = h(Z) −µ and G =
-> Invalid unicode use found on p. 20: g(Z) −µg, we have
-> Invalid unicode use found on p. 20: H −αG
-> Invalid unicode use found on p. 20: h −2α σhg + α2σ2
-> Invalid unicode use found on p. 21: −2σhg + 2ασ2
-> Invalid unicode use found on p. 21: h (1 −ρ2),
-> Invalid unicode use found on p. 21: σhσg is the correlation between h and g, so variance is reduced by the factor 1 −ρ2 such
-> Invalid unicode use found on p. 21: i = Xi −µX with Xi = −log p(s(i))
-> Invalid unicode use found on p. 21: are strongly correlated with the negative cluster probabilities Yi = −log ˆp(c(s(i))), being based on
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
Backend tkagg is interactive backend. Turning interactive mode on.
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 420 sentences on 11 pages -> Avg. of 43.0 sentences per page
-> Warning: Reference '43' never used in the document's text.
-> Warning: Reference '65' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 17
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 18
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
  // LLM calling counter = 19
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
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
  -> Found 25 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 20
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━  96% 0:00:01
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 21
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 22
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 23
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 24
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━━  82% 0:00:01
###############################
# Starting Author Check
###############################
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\4 Efficient Semantic Uncertainty Quantification\PAU_results.md
```

---

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\4 Efficient Semantic Uncertainty Quantification\Efficient semantic uncertainty quantification in.pdf"
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
 - 'authoryear_round'  = Authors' names and the year places insince round brackets (e.g., (Speckmann et al., 2025))
                      -> Multiple references are separated by a semicolon (e.g., (Speckmann et al. 2025; Janiesch et al. 2021))
                      -> Please note that the author and year are *not* separated
 - 'authoryear_square' = Authors' names and the year places insince square brackets (e.g., [Speckmann et al., 2025])
                      -> Multiple references are separated by a comma (e.g., [Speckmann et al., 2025, Janiesch et al., 2021])
                      -> Please note that the author and year are also separated by a comma
Enter a supported referencing template (['numeric', 'authoryear_round', 'authoryear_square']): numeric
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Estimating the predictive uncertainty of free-form responses' on page 2
- Found following heading '3 - Methods' on page 3
- Found following heading '4 - Related Work' on page 7
- Found following heading '5 - Experiments' on page 8
- Found following heading '6 - Discussion and limitations' on page 9
- Found following heading '7 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Extension to masked diffusion models' on page 16
- Found following appendix 'B - Additional implementation details' on page 17
- Found following appendix 'C - Qualitative case studies' on page 19
- Found following appendix 'D - Mutual information results' on page 21
- Found following appendix 'E - Variance reduction with control variates' on page 21
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 16
All found references: 65
-> Warning: Malformed author string: 'AI@Meta'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors                                 normalized_authors  ...                                             outlet                              link  valid
0       1     Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar                     [Kuhn L., Gal Y., Farquhar S.]  ...  International Conference on Learning Represent...                                     None
1       2  Yasin Abbasi Yadkori, Ilja Kuzborskij, András ...  [Yadkori Y., Kuzborskij I., György A., Szepesv...  ...                   arXiv preprint arXiv:2406. 02543                                     None
2       3  Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes,...  [Holtzman A., Buys J., Du L., Forbes M., Choi Y.]  ...                   arXiv preprint arXiv:1904. 09751                                     None
3       4        Franz Aichberger, Lily Chen, and John Smith                 [Aichberger F., Chen L., Smith J.]  ...  International Conference on Learning Represent...                                     None
4       5                             Jacob Austin and et al                                        [Austin J.]  ...                                               ICLR                                     None
..    ...                                                ...                                                ...  ...                                                ...                               ...    ...
60     61                                     Augustine Kong                                          [Kong A.]  ...  University of Chicago, Dept of Statistics, Tec...                                     None
61     62  Ilia Kulikov, Alexander Miller, Kyunghyun Cho,...         [Kulikov I., Miller A., Cho K., Weston J.]  ...                                                                                        None
62     63  John Schulman, Filip Wolski, Prafulla Dhariwal...  [Schulman J., Wolski F., Dhariwal P., Radford ...  ...                                               CoRR  http://arxiv.org/abs/1707.06347.   None
63     64  Daya Guo, Dejian Yang, Haowei Zhang, Junxiao S...  [Guo D., Yang D., Zhang H., Song J., Zhang R.,...  ...                   arXiv preprint arXiv:2501. 12948                                     None
64     65                   Ilya Loshchilov and Frank Hutter                         [Loshchilov I., Hutter F.]  ...                   arXiv preprint arXiv:1711. 05101                                     None

[65 rows x 10 columns]
- Checking reference 1/65:
  -> INFO: Now checking 4 results for matching title: 'Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation'
Backend tkagg is interactive backend. Turning interactive mode on.
       -> INFO: All authors matched!
- Checking reference 2/65:
  -> INFO: Now checking 1 results for matching title: 'To believe or not to believe your llm'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Abbasi-Yadkori, Szepesv'ari'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/65:
  -> INFO: Now checking 3 results for matching title: 'The curious case of neural text degeneration'
       -> INFO: All authors matched!
- Checking reference 4/65:
  -> INFO: Now checking 10 results for matching title: 'Semantically diverse language generation'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Aichberger', 'Chen', 'Smith', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Semantically+diverse+language+generation manually and check the results.
        -> Author(s): Franz Aichberger, Lily Chen, and John Smith
        -> Title:     Semantically diverse language generation
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 5/65:
  -> INFO: Now checking 6 results for matching title: 'Diffuseq: Sequence to sequence text generation with diffusion models'
  -> WARNING: None of the 6 results matched the expected title!
  -> INFO: Now checking 335 results for matching title: 'Diffuseq: Sequence to sequence text generation with diffusion models'
  -> WARNING: None of the 335 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Diffuseq:+Sequence+to+sequence+text+generation+with+diffusion+models manually and check the results.
        -> Author(s): Jacob Austin and et al
        -> Title:     Diffuseq: Sequence to sequence text generation with diffusion models
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 6/65:
  -> INFO: Now checking 2 results for matching title: 'Dsp: Diffusion-based span prediction for masked text modeling'
  -> WARNING: None of the 2 results matched the expected title!
  -> INFO: Now checking 998 results for matching title: 'Dsp: Diffusion-based span prediction for masked text modeling'
  -> WARNING: None of the 998 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Dsp:+Diffusion-based+span+prediction+for+masked+text+modeling manually and check the results.
        -> Author(s): Nuo Lou and et al
        -> Title:     Dsp: Diffusion-based span prediction for masked text modeling
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 7/65:
  -> INFO: Now checking 10 results for matching title: 'Maskgpt: Uniform denoising diffusion for language'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 999 results for matching title: 'Maskgpt: Uniform denoising diffusion for language'
  -> WARNING: None of the 999 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Maskgpt:+Uniform+denoising+diffusion+for+language manually and check the results.
        -> Author(s): Sheng Shi and et al
        -> Title:     Maskgpt: Uniform denoising diffusion for language
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 8/65:
  -> INFO: Now checking 10 results for matching title: 'inatk: Iterative noise aware text denoising'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 333 results for matching title: 'inatk: Iterative noise aware text denoising'
  -> WARNING: None of the 333 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=inatk:+Iterative+noise+aware+text+denoising manually and check the results.
        -> Author(s): A  Sahoo and et al
        -> Title:     inatk: Iterative noise aware text denoising
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 9/65:
  -> INFO: Now checking 3 results for matching title: 'Tuqdm: Token unmasking with quantized diffusion models'
  -> WARNING: None of the 3 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ou', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Tuqdm:+Token+unmasking+with+quantized+diffusion+models manually and check the results.
        -> Author(s): X  Ou and et al
        -> Title:     Tuqdm: Token unmasking with quantized diffusion models
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 10/65:
  -> INFO: Now checking 9 results for matching title: 'Llada: Large language auto-diffusion for accelerated denoising'
  -> WARNING: None of the 9 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Nie', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Llada:+Large+language+auto-diffusion+for+accelerated+denoising manually and check the results.
        -> Author(s): Yuxin Nie and et al
        -> Title:     Llada: Large language auto-diffusion for accelerated denoising
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 11/65:
  -> INFO: Now checking 1 results for matching title: 'A broad-coverage challenge corpus for sentence understanding through inference'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/65:
  -> INFO: Now checking 10 results for matching title: 'Deberta: Decoding-enhanced bert with disentangled attention'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/65:
  -> INFO: Now checking 1 results for matching title: 'Glue: A multi-task benchmark and analysis platform for natural language understanding'
       -> INFO: All authors matched!
- Checking reference 14/65:
  -> INFO: Now checking 1 results for matching title: 'Triviaqa: A large scale distantly supervised challenge for reading comprehension'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Joshi', 'Choi', 'Weld', 'Zettlemoyer', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Triviaqa:+A+large+scale+distantly+supervised+challenge+for+reading+comprehension manually and check the results.
        -> Author(s): Mandar Joshi, Eunsol Choi, Daniel S  Weld, and Luke Zettlemoyer
        -> Title:     Triviaqa: A large scale distantly supervised challenge for reading comprehension
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 15/65:
  -> INFO: Now checking 10 results for matching title: 'Dropout as a bayesian approximation: Representing model uncertainty in deep learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/65:
  -> INFO: Now checking 10 results for matching title: 'Simple and scalable predictive uncertainty estimation using deep ensembles'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/65:
  -> INFO: Now checking 10 results for matching title: 'Predictive uncertainty estimation via prior networks'
       -> INFO: All authors matched!
- Checking reference 18/65:
  -> INFO: Now checking 10 results for matching title: 'Ensemble distribution distillation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Mlodozeniec'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 19/65:
  -> INFO: Now checking 4 results for matching title: 'To trust or not to trust a classifier'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Kim, Gupta'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/65:
  -> INFO: Now checking 10 results for matching title: 'Calibration of text generation models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Desai', 'Durrett', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Calibration+of+text+generation+models manually and check the results.
        -> Author(s): Yayati Desai and Gregory Durrett
        -> Title:     Calibration of text generation models
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 21/65:
  -> INFO: Now checking 10 results for matching title: 'Uncertainty estimation in neural text regression'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Glushkova', 'Kobayashi', 'Suzuki', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Uncertainty+estimation+in+neural+text+regression manually and check the results.
        -> Author(s): Maria Glushkova, Shiori Kobayashi, and Junichi Suzuki
        -> Title:     Uncertainty estimation in neural text regression
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 22/65:
  -> INFO: Now checking 10 results for matching title: 'Uncertainty quantification in abstractive summarization'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Zhou', 'Lopez', 'Snyder', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Uncertainty+quantification+in+abstractive+summarization manually and check the results.
        -> Author(s): Yichao Wang, Bowen Zhou, Adam Lopez, and Benjamin Snyder
        -> Title:     Uncertainty quantification in abstractive summarization
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 23/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2023.emnlp-main.522/.
  -> INFO: Now checking 2 results for matching title: 'Increasing probability mass on answer choices does not always improve accuracy'
       -> INFO: All authors matched!
- Checking reference 24/65:
  -> INFO: Now checking 10 results for matching title: 'Teaching language models to script their confidence'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lin', 'Roller', 'Stewart', 'Zettlemoyer', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Teaching+language+models+to+script+their+confidence manually and check the results.
        -> Author(s): Jason Lin, Stephen Roller, Ashwin Stewart, and Luke Zettlemoyer
        -> Title:     Teaching language models to script their confidence
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 25/65:
  -> INFO: Now checking 10 results for matching title: 'Answer me this: Self-verifying large language models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kadavath', 'Khandelwal', 'Radford', 'Shazeer', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Answer+me+this:+Self-verifying+large+language+models manually and check the results.
        -> Author(s): Srinivasan Kadavath, Urvashi Khandelwal, Alec Radford, and Noam Shazeer
        -> Title:     Answer me this: Self-verifying large language models
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 26/65:
  -> INFO: Now checking 1 results for matching title: 'Evaluating the reliability of self-assessment in language models'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Mielke', 'Akyürek', 'Dusek', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Evaluating+the+reliability+of+self-assessment+in+language+models manually and check the results.
        -> Author(s): Sam Mielke, Elif Akyürek, and Ondˇrej Dusek
        -> Title:     Evaluating the reliability of self-assessment in language models
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 27/65:
  -> INFO: Now checking 10 results for matching title: 'Learning to predict confidence for language models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jain', 'Perez', 'Glass', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Learning+to+predict+confidence+for+language+models manually and check the results.
        -> Author(s): Mohit Jain, Ethan Perez, and James Glass
        -> Title:     Learning to predict confidence for language models
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 28/65:
  -> INFO: Now checking 1 results for matching title: 'Crawling the internal knowledgebase of language models'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Cohen', 'Geva', 'Berant', 'Globerson', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Crawling+the+internal+knowledgebase+of+language+models manually and check the results.
        -> Author(s): Roi Cohen, Mor Geva, Jonathan Berant, and Amir Globerson
        -> Title:     Crawling the internal knowledgebase of language models
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 29/65:
  -> INFO: Now checking 1 results for matching title: 'The capacity for moral self-correction in large language models'
       -> WARNING: Not all 48 authors from the found ref. were matched (only 46)
                   Unmatched authors = 'Lukovsiut.e, Hatfield-Dodds'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/65:
  -> Checking if provided link is pingable: https://proceedings.mlr.press/v239/ren23a.html.
  -> INFO: Now checking 10 results for matching title: 'Self-evaluation improves selective generation in large language models'
       -> INFO: All authors matched!
- Checking reference 31/65:
  -> INFO: Now checking 1 results for matching title: 'Just ask for calibration: Strategies for eliciting calibrated confidence scores from language models fine-tuned with human feedback'
       -> INFO: All authors matched!
- Checking reference 32/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2024.emnlp-main.578/.
  -> INFO: Now checking 1 results for matching title: 'Contextualized sequence likelihood: Enhanced confidence scores for natural language generation'
       -> INFO: All authors matched!
- Checking reference 33/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2024.acl-long.276/.
  -> INFO: Now checking 1 results for matching title: 'Shifting attention to relevance: Towards the predictive uncertainty quantification of free-form large language models'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/65:
  -> INFO: Now checking 1 results for matching title: 'LM vs LM: Detecting factual errors via cross examination'
       -> INFO: All authors matched!
- Checking reference 35/65:
  -> INFO: Now checking 10 results for matching title: 'Conformal prediction in neural forecasting'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Angelopoulos', 'Bates', 'Uhler', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Conformal+prediction+in+neural+forecasting manually and check the results.
        -> Author(s): Alexandros N  Angelopoulos, Stephen Bates, and Caroline Uhler
        -> Title:     Conformal prediction in neural forecasting
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 36/65:
  -> INFO: Now checking 10 results for matching title: 'Well-calibrated language models can be produced with small calibration sets'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ravfogel', 'Zalmanski', 'Goldberg', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Well-calibrated+language+models+can+be+produced+with+small+calibration+sets manually and check the results.
        -> Author(s): Shauli Ravfogel, Shachar Zalmanski, and Yoav Goldberg
        -> Title:     Well-calibrated language models can be produced with small calibration sets
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 37/65:
  -> INFO: Now checking 1 results for matching title: 'Distinguishing the knowable from the unknowable with language models'
       -> INFO: All authors matched!
- Checking reference 38/65:
  -> INFO: Now checking 10 results for matching title: 'Experts don’t cheat: learning what you don’t know by predicting pairs'
       -> INFO: All authors matched!
- Checking reference 39/65:
  -> INFO: Now checking 10 results for matching title: 'Diverse beam search: Decoding diverse solutions from neural sequence models'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 40/65:
  -> INFO: Now checking 10 results for matching title: 'Contrastive decoding: Open-ended text generation as optimization'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 41/65:
  -> INFO: Now checking 4 results for matching title: 'A diversity-promoting objective function for neural conversation models'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 42/65:
  -> INFO: Now checking 1 results for matching title: 'Cluster-based beam search for pointer-generator chatbot grounded by knowledge'
       -> INFO: All authors matched!
- Checking reference 43/65:
  -> Checking if provided link is pingable: https://aclanthology.org/D16-1250/.
  -> INFO: Now checking 1 results for matching title: 'Learning principled bilingual mappings of word embeddings while preserving monolingual invariance'
       -> INFO: All authors matched!
- Checking reference 44/65:
  -> INFO: Now checking 10 results for matching title: 'Comparison of diverse decoding methods from conditional language models'
       -> INFO: All authors matched!
- Checking reference 45/65:
  -> INFO: Now checking 10 results for matching title: 'Paraphrase generation and information retrieval from stored text'
       -> INFO: All authors matched!
- Checking reference 46/65:
  -> INFO: Now checking 10 results for matching title: 'Machine translation evaluation with textual entailment features'
       -> INFO: All authors matched!
- Checking reference 47/65:
  -> INFO: Now checking 1 results for matching title: 'A survey of paraphrasing and textual entailment methods'
       -> INFO: All authors matched!
       -> WARNING: Year (2009) does not match expected year (2010)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/65:
  -> INFO: Now checking 10 results for matching title: 'Semantic similarity based on lexical substitution'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Fernando', 'Stevenson', '2008']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Semantic+similarity+based+on+lexical+substitution manually and check the results.
        -> Author(s): Shyam Fernando and Mark Stevenson
        -> Title:     Semantic similarity based on lexical substitution
        -> Year:      2008
     -> Manual search was skipped by the user.
- Checking reference 49/65:
  -> INFO: Now checking 10 results for matching title: 'Paraphrase identification using deep contextualized representations'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Issa', 'Mohler', 'Johnson', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Paraphrase+identification+using+deep+contextualized+representations manually and check the results.
        -> Author(s): Asma Issa, George Mohler, and John Johnson
        -> Title:     Paraphrase identification using deep contextualized representations
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 50/65:
  -> INFO: Now checking 10 results for matching title: 'Deep paraphrase identification'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yu', 'Dumsmyr', 'Knight', '2014']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+paraphrase+identification manually and check the results.
        -> Author(s): Lei Yu, Jimmy Dumsmyr, and Kevin Knight
        -> Title:     Deep paraphrase identification
        -> Year:      2014
     -> Manual search was skipped by the user.
- Checking reference 51/65:
  -> INFO: Now checking 2 results for matching title: 'Dynamic pooling and unfolding recursive autoencoders for paraphrase detection'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Pennington'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 52/65:
  -> INFO: Now checking 6 results for matching title: 'Reasoning with heterogeneous graph representations for knowledge-aware question answering'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tay', 'Fu', 'Wu', 'Casanueva', 'Liu', 'Wallace', 'Wang', 'Singh', 'McAuley', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Reasoning+with+heterogeneous+graph+representations+for+knowledge-aware+question+answering manually and check the results.
        -> Author(s): Yi Tay, Kelvin Fu, Kai Wu, Ivan Casanueva, Jianfeng Liu, Byron Wallace, Shuohang Wang, Bajrang Singh, and Julian McAuley
        -> Title:     Reasoning with heterogeneous graph representations for knowledge-aware question answering
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 53/65:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Efficient fewshot learning with efl: A single transformer for all tasks
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Bommasani', 'Hendrycks', 'Song', 'Zhang', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Efficient+fewshot+learning+with+efl:+A+single+transformer+for+all+tasks manually and check the results.
        -> Author(s): Alex Wang, Rishi Bommasani, Dan Hendrycks, Daniel Song, and Zhilin Zhang
        -> Title:     Efficient fewshot learning with efl: A single transformer for all tasks
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 54/65:
  -> INFO: Now checking 10 results for matching title: 'Generating with confidence: Uncertainty quantification for black-box large language models'
       -> INFO: All authors matched!
- Checking reference 55/65:
  -> INFO: Now checking 10 results for matching title: 'Coqa: A conversational question answering challenge'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 56/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2022.acl-long.229/.
  -> INFO: Now checking 10 results for matching title: 'TruthfulQA: Measuring how models mimic human falsehoods'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 57/65:
  -> INFO: Now checking 10 results for matching title: 'Ambigqa: Answering ambiguous open-domain questions'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Michael, Hajishirzi, Zettlemoyer'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 58/65:
  -> INFO: Now checking 10 results for matching title: 'Opt: Open pre-trained transformer language models'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Li, Lin, Mihaylov, Ott, Shleifer, Shuster, Simig, Koura, Sridhar, Wang, Zettlemoyer'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/65:
  -> INFO: Now checking 10 results for matching title: 'Llama: Open and efficient foundation language models'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lavril, Izacard, Martinet, Lacroix, Rozière, Goyal, Hambro, Azhar, Rodriguez, Joulin, Grave, Lample'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 60/65:
  -> Checking if provided link is pingable: https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md.
  -> INFO: Now checking 10 results for matching title: 'Llama 3 model card'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['AI@Meta', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Llama+3+model+card manually and check the results.
        -> Author(s): AI@Meta
        -> Title:     Llama 3 model card
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 61/65:
  -> INFO: Now checking 10 results for matching title: 'A note on importance sampling using standardized weights'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kong', '1992']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+note+on+importance+sampling+using+standardized+weights manually and check the results.
        -> Author(s): Augustine Kong
        -> Title:     A note on importance sampling using standardized weights
        -> Year:      1992
     -> Manual search was skipped by the user.
- Checking reference 62/65:
  -> INFO: Now checking 1 results for matching title: 'Importance of search and evaluation strategies in neural dialogue modeling'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 63/65:
  -> Checking if provided link is pingable: http://arxiv.org/abs/1707.06347.
  -> INFO: Now checking 10 results for matching title: 'Proximal policy optimization algorithms'
       -> INFO: All authors matched!
- Checking reference 64/65:
  -> INFO: Now checking 10 results for matching title: 'Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Guo', 'Yang', 'Zhang', 'Song', 'Zhang', 'Xu', 'Zhu', 'Ma', 'Wang', 'Bi', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deepseek-r1:+Incentivizing+reasoning+capability+in+llms+via+reinforcement+learning manually and check the results.
        -> Author(s): Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al
        -> Title:     Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 65/65:
  -> INFO: Now checking 10 results for matching title: 'Decoupled weight decay regularization'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 1: = −
-> Invalid unicode use found on p. 2: log q(yt|y<t) = log p(yt|y<t) −λ max
-> Invalid unicode use found on p. 3: ℓ′(next) ←ℓ(next) −λπ
-> Invalid unicode use found on p. 3: log q(y(t)|y(t+1)) = log p(y(t)|y(t+1)) −λ max
-> Invalid unicode use found on p. 5: ˆH = −
-> Invalid unicode use found on p. 6: Denote Yi = −log ˆp(c(s(i))), where c(s(i)) is the cluster containing s(i). The estimator in Equation 10 is then PN
-> Invalid unicode use found on p. 6: i=1 ˜wiYi. Now define Xi = −log p(s(i)), and let X′
-> Invalid unicode use found on p. 6: i = Xi−µX and Y ′
-> Invalid unicode use found on p. 6: i = Yi−µY
-> Invalid unicode use found on p. 6: −α
-> Invalid unicode use found on p. 6: ˜wi,jointYi −αMI
-> Invalid unicode use found on p. 8: numbers are mean±std over 5 jackknife samples of size 200. The symbol “−” indicates that the
-> Invalid unicode use found on p. 15: for t = T−1 downto 0 do
-> Invalid unicode use found on p. 15: ℓ′(next) ←ℓ(next) −λπ
-> Invalid unicode use found on p. 16: pair, (ii) all proper prefixes of the hypothesis (lengths 1 . . . Lh −1) each followed by [TRUNC], and
-> Invalid unicode use found on p. 16: (iii) all proper prefixes of the premise (lengths 1 . . . Lp −1) similarly tagged. A single example with
-> Invalid unicode use found on p. 16: tokenized lengths (Lp, Lh) thus contributes 1 + (Lh −1) + (Lp −1) training instances, covering
-> Invalid unicode use found on p. 17: s∈S E(y≤t, s) −Etarget
-> Invalid unicode use found on p. 17: Var{ ˆH} −Vtarget
-> Invalid unicode use found on p. 17: defined by 1 −E(si, sj) for every pair si, sj of iteratively prompted responses (see Equation 6 for
-> Invalid unicode use found on p. 20: h(Zi) −α
-> Invalid unicode use found on p. 20: g(Zi) −µg
-> Invalid unicode use found on p. 20: is unbiased, because Ep[g(Z) −µg] = 0.
-> Invalid unicode use found on p. 20: g = Var[g(Z)], and σhg = Cov[h(Z), g(Z)]. Writing H = h(Z) −µ and G =
-> Invalid unicode use found on p. 20: g(Z) −µg, we have
-> Invalid unicode use found on p. 20: H −αG
-> Invalid unicode use found on p. 20: h −2α σhg + α2σ2
-> Invalid unicode use found on p. 21: −2σhg + 2ασ2
-> Invalid unicode use found on p. 21: h (1 −ρ2),
-> Invalid unicode use found on p. 21: σhσg is the correlation between h and g, so variance is reduced by the factor 1 −ρ2 such
-> Invalid unicode use found on p. 21: i = Xi −µX with Xi = −log p(s(i))
-> Invalid unicode use found on p. 21: are strongly correlated with the negative cluster probabilities Yi = −log ˆp(c(s(i))), being based on
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################

```

---

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\4 Efficient Semantic Uncertainty Quantification\Efficient semantic uncertainty quantification in.pdf"
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
 - 'authoryear_round'  = Authors' names and the year places insince round brackets (e.g., (Speckmann et al., 2025))
                      -> Multiple references are separated by a semicolon (e.g., (Speckmann et al. 2025; Janiesch et al. 2021))
                      -> Please note that the author and year are *not* separated
 - 'authoryear_square' = Authors' names and the year places insince square brackets (e.g., [Speckmann et al., 2025])
                      -> Multiple references are separated by a comma (e.g., [Speckmann et al., 2025, Janiesch et al., 2021])
                      -> Please note that the author and year are also separated by a comma
Enter a supported referencing template (['numeric', 'authoryear_round', 'authoryear_square']): numeric
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Estimating the predictive uncertainty of free-form responses' on page 2
- Found following heading '3 - Methods' on page 3
- Found following heading '4 - Related Work' on page 7
- Found following heading '5 - Experiments' on page 8
- Found following heading '6 - Discussion and limitations' on page 9
- Found following heading '7 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Extension to masked diffusion models' on page 16
- Found following appendix 'B - Additional implementation details' on page 17
- Found following appendix 'C - Qualitative case studies' on page 19
- Found following appendix 'D - Mutual information results' on page 21
- Found following appendix 'E - Variance reduction with control variates' on page 21
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 16
All found references: 65
-> Warning: Malformed author string: 'AI@Meta'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                              link  valid
0       1     Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar  ...                                     None
1       2  Yasin Abbasi Yadkori, Ilja Kuzborskij, András ...  ...                                     None
2       3  Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes,...  ...                                     None
3       4        Franz Aichberger, Lily Chen, and John Smith  ...                                     None
4       5                             Jacob Austin and et al  ...                                     None
..    ...                                                ...  ...                               ...    ...
60     61                                     Augustine Kong  ...                                     None
61     62  Ilia Kulikov, Alexander Miller, Kyunghyun Cho,...  ...                                     None
62     63  John Schulman, Filip Wolski, Prafulla Dhariwal...  ...  http://arxiv.org/abs/1707.06347.   None
63     64  Daya Guo, Dejian Yang, Haowei Zhang, Junxiao S...  ...                                     None
64     65                   Ilya Loshchilov and Frank Hutter  ...                                     None

[65 rows x 10 columns]
- Checking reference 1/65:
  -> INFO: Now checking 4 results for matching title: 'Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation'
       -> INFO: All authors matched!
- Checking reference 2/65:
  -> INFO: Now checking 1 results for matching title: 'To believe or not to believe your llm'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Abbasi-Yadkori, Szepesv'ari'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/65:
  -> INFO: Now checking 3 results for matching title: 'The curious case of neural text degeneration'
       -> INFO: All authors matched!
- Checking reference 4/65:
  -> INFO: Now checking 10 results for matching title: 'Semantically diverse language generation'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Schweighofer, Ielanskyi, Hochreiter'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yu, Tong, Fu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 5/65:
  -> INFO: Now checking 6 results for matching title: 'Diffuseq: Sequence to sequence text generation with diffusion models'
  -> WARNING: None of the 6 results matched the expected title!
  -> INFO: Now checking 335 results for matching title: 'Diffuseq: Sequence to sequence text generation with diffusion models'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 6/65:
  -> INFO: Now checking 2 results for matching title: 'Dsp: Diffusion-based span prediction for masked text modeling'
  -> WARNING: None of the 2 results matched the expected title!
  -> INFO: Now checking 998 results for matching title: 'Dsp: Diffusion-based span prediction for masked text modeling'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Li, Huo, Liang, Qu, Soleil'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lin, 0015, 0008, 0001, 0001'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zhou, Lin, 0015, 0008, 0001, Chen'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lin, 0008, 0015, 0001'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wan, Li, Li, 0014, Li'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lin, 0008, 0015, 0001'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lin, 0015, 0008, 0001, 0001'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Zhou, Lin, 0015, 0008, 0001, Chen'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Ma, Lin, 0001, Chen'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> INFO: All authors matched!
- Checking reference 7/65:
  -> INFO: Now checking 10 results for matching title: 'Maskgpt: Uniform denoising diffusion for language'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 999 results for matching title: 'Maskgpt: Uniform denoising diffusion for language'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 8/65:
  -> INFO: Now checking 10 results for matching title: 'inatk: Iterative noise aware text denoising'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sahoo', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=inatk:+Iterative+noise+aware+text+denoising manually and check the results.
        -> Author(s): A  Sahoo and et al
        -> Title:     inatk: Iterative noise aware text denoising
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 9/65:
  -> INFO: Now checking 3 results for matching title: 'Tuqdm: Token unmasking with quantized diffusion models'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ou', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Tuqdm:+Token+unmasking+with+quantized+diffusion+models manually and check the results.
        -> Author(s): X  Ou and et al
        -> Title:     Tuqdm: Token unmasking with quantized diffusion models
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 10/65:
  -> INFO: Now checking 9 results for matching title: 'Llada: Large language auto-diffusion for accelerated denoising'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Year (2026) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/65:
  -> INFO: Now checking 1 results for matching title: 'A broad-coverage challenge corpus for sentence understanding through inference'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/65:
  -> INFO: Now checking 10 results for matching title: 'Deberta: Decoding-enhanced bert with disentangled attention'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lu, Ming, Mao, Wang, Zhao'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/65:
  -> INFO: Now checking 1 results for matching title: 'Glue: A multi-task benchmark and analysis platform for natural language understanding'
       -> INFO: All authors matched!
- Checking reference 14/65:
  -> INFO: Now checking 1 results for matching title: 'Triviaqa: A large scale distantly supervised challenge for reading comprehension'
       -> INFO: All authors matched!
- Checking reference 15/65:
  -> INFO: Now checking 10 results for matching title: 'Dropout as a bayesian approximation: Representing model uncertainty in deep learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
       -> WARNING: Not all 1 authors from the found ref. were matched (only 1)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/65:
  -> INFO: Now checking 10 results for matching title: 'Simple and scalable predictive uncertainty estimation using deep ensembles'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Liu, Lin, Padhy, Tran, Bedrax-Weiss'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/65:
  -> INFO: Now checking 10 results for matching title: 'Predictive uncertainty estimation via prior networks'
       -> INFO: All authors matched!
- Checking reference 18/65:
  -> INFO: Now checking 10 results for matching title: 'Ensemble distribution distillation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Mlodozeniec'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Fathullah, Xia'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Ryabinin'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ding, Jiang, Zhang, Guo'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 19/65:
  -> INFO: Now checking 4 results for matching title: 'To trust or not to trust a classifier'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Kim, Gupta'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/65:
  -> INFO: Now checking 10 results for matching title: 'Calibration of text generation models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Desai', 'Durrett', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Calibration+of+text+generation+models manually and check the results.
        -> Author(s): Yayati Desai and Gregory Durrett
        -> Title:     Calibration of text generation models
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 21/65:
  -> INFO: Now checking 10 results for matching title: 'Uncertainty estimation in neural text regression'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Glushkova', 'Kobayashi', 'Suzuki', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Uncertainty+estimation+in+neural+text+regression manually and check the results.
        -> Author(s): Maria Glushkova, Shiori Kobayashi, and Junichi Suzuki
        -> Title:     Uncertainty estimation in neural text regression
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 22/65:
  -> INFO: Now checking 10 results for matching title: 'Uncertainty quantification in abstractive summarization'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Zhou', 'Lopez', 'Snyder', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Uncertainty+quantification+in+abstractive+summarization manually and check the results.
        -> Author(s): Yichao Wang, Bowen Zhou, Adam Lopez, and Benjamin Snyder
        -> Title:     Uncertainty quantification in abstractive summarization
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 23/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2023.emnlp-main.522/.
  -> INFO: Now checking 2 results for matching title: 'Increasing probability mass on answer choices does not always improve accuracy'
       -> INFO: All authors matched!
- Checking reference 24/65:
  -> INFO: Now checking 10 results for matching title: 'Teaching language models to script their confidence'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lin', 'Roller', 'Stewart', 'Zettlemoyer', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Teaching+language+models+to+script+their+confidence manually and check the results.
        -> Author(s): Jason Lin, Stephen Roller, Ashwin Stewart, and Luke Zettlemoyer
        -> Title:     Teaching language models to script their confidence
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 25/65:
  -> INFO: Now checking 10 results for matching title: 'Answer me this: Self-verifying large language models'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Jiang, Yu, Liu, Zhang, Li, Kwok'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zhang, Xu, Wang, Cui, Liu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/65:
  -> INFO: Now checking 1 results for matching title: 'Evaluating the reliability of self-assessment in language models'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Steiner, Buse, jumah, Westergaard, Jensen, Reed, Prilipko, Mennini, Láinez, Ravishankar, Sakai, Fontebasso, Khathami, MacGregor, Antonaci, Tassorelli, Lipton, Headache'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 27/65:
  -> INFO: Now checking 10 results for matching title: 'Learning to predict confidence for language models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jain', 'Perez', 'Glass', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Learning+to+predict+confidence+for+language+models manually and check the results.
        -> Author(s): Mohit Jain, Ethan Perez, and James Glass
        -> Title:     Learning to predict confidence for language models
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 28/65:
  -> INFO: Now checking 1 results for matching title: 'Crawling the internal knowledgebase of language models'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Cohen', 'Geva', 'Berant', 'Globerson', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Crawling+the+internal+knowledgebase+of+language+models manually and check the results.
        -> Author(s): Roi Cohen, Mor Geva, Jonathan Berant, and Amir Globerson
        -> Title:     Crawling the internal knowledgebase of language models
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 29/65:
  -> INFO: Now checking 1 results for matching title: 'The capacity for moral self-correction in large language models'
       -> WARNING: Not all 48 authors from the found ref. were matched (only 46)
                   Unmatched authors = 'Lukovsiut.e, Hatfield-Dodds'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/65:
  -> Checking if provided link is pingable: https://proceedings.mlr.press/v239/ren23a.html.
  -> INFO: Now checking 10 results for matching title: 'Self-evaluation improves selective generation in large language models'
       -> INFO: All authors matched!
- Checking reference 31/65:
  -> INFO: Now checking 1 results for matching title: 'Just ask for calibration: Strategies for eliciting calibrated confidence scores from language models fine-tuned with human feedback'
       -> INFO: All authors matched!
- Checking reference 32/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2024.emnlp-main.578/.
  -> INFO: Now checking 1 results for matching title: 'Contextualized sequence likelihood: Enhanced confidence scores for natural language generation'
       -> INFO: All authors matched!
- Checking reference 33/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2024.acl-long.276/.
  -> INFO: Now checking 1 results for matching title: 'Shifting attention to relevance: Towards the predictive uncertainty quantification of free-form large language models'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/65:
  -> INFO: Now checking 1 results for matching title: 'LM vs LM: Detecting factual errors via cross examination'
       -> INFO: All authors matched!
- Checking reference 35/65:
  -> INFO: Now checking 10 results for matching title: 'Conformal prediction in neural forecasting'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Rodríguez'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Rodr'iguez'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zhang, Wang, Hu, Kang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 36/65:
  -> INFO: Now checking 10 results for matching title: 'Well-calibrated language models can be produced with small calibration sets'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ravfogel', 'Zalmanski', 'Goldberg', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Well-calibrated+language+models+can+be+produced+with+small+calibration+sets manually and check the results.
        -> Author(s): Shauli Ravfogel, Shachar Zalmanski, and Yoav Goldberg
        -> Title:     Well-calibrated language models can be produced with small calibration sets
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 37/65:
  -> INFO: Now checking 1 results for matching title: 'Distinguishing the knowable from the unknowable with language models'
       -> INFO: All authors matched!
- Checking reference 38/65:
  -> INFO: Now checking 10 results for matching title: 'Experts don’t cheat: learning what you don’t know by predicting pairs'
       -> INFO: All authors matched!
- Checking reference 39/65:
  -> INFO: Now checking 10 results for matching title: 'Diverse beam search: Decoding diverse solutions from neural sequence models'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2018)!
       -> INFO: All authors matched!
- Checking reference 40/65:
  -> INFO: Now checking 10 results for matching title: 'Contrastive decoding: Open-ended text generation as optimization'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Xu'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Arias, Rodemann, Heumann, Aßenmacher'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ding, Arias, Rodemann, Aßenmacher, Chen, Fan, Heumann, Zhang'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Nguyen, Gupta'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 41/65:
  -> INFO: Now checking 4 results for matching title: 'A diversity-promoting objective function for neural conversation models'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Block, Becker, Duval, Clark, Al-Qawasmeh, Walker-VanSingel, Mannella, Phan, Monk, Fitzgerald'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 42/65:
  -> INFO: Now checking 1 results for matching title: 'Cluster-based beam search for pointer-generator chatbot grounded by knowledge'
       -> INFO: All authors matched!
- Checking reference 43/65:
  -> Checking if provided link is pingable: https://aclanthology.org/D16-1250/.
  -> INFO: Now checking 1 results for matching title: 'Learning principled bilingual mappings of word embeddings while preserving monolingual invariance'
       -> INFO: All authors matched!
- Checking reference 44/65:
  -> INFO: Now checking 10 results for matching title: 'Comparison of diverse decoding methods from conditional language models'
       -> INFO: All authors matched!
- Checking reference 45/65:
  -> INFO: Now checking 10 results for matching title: 'Paraphrase generation and information retrieval from stored text'
       -> INFO: All authors matched!
- Checking reference 46/65:
  -> INFO: Now checking 10 results for matching title: 'Machine translation evaluation with textual entailment features'
       -> INFO: All authors matched!
- Checking reference 47/65:
  -> INFO: Now checking 1 results for matching title: 'A survey of paraphrasing and textual entailment methods'
       -> INFO: All authors matched!
       -> WARNING: Year (2009) does not match expected year (2010)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/65:
  -> INFO: Now checking 10 results for matching title: 'Semantic similarity based on lexical substitution'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Fernando', 'Stevenson', '2008']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Semantic+similarity+based+on+lexical+substitution manually and check the results.
        -> Author(s): Shyam Fernando and Mark Stevenson
        -> Title:     Semantic similarity based on lexical substitution
        -> Year:      2008
     -> Manual search was skipped by the user.
- Checking reference 49/65:
  -> INFO: Now checking 10 results for matching title: 'Paraphrase identification using deep contextualized representations'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Issa', 'Mohler', 'Johnson', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Paraphrase+identification+using+deep+contextualized+representations manually and check the results.
        -> Author(s): Asma Issa, George Mohler, and John Johnson
        -> Title:     Paraphrase identification using deep contextualized representations
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 50/65:
  -> INFO: Now checking 10 results for matching title: 'Deep paraphrase identification'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yu', 'Dumsmyr', 'Knight', '2014']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+paraphrase+identification manually and check the results.
        -> Author(s): Lei Yu, Jimmy Dumsmyr, and Kevin Knight
        -> Title:     Deep paraphrase identification
        -> Year:      2014
     -> Manual search was skipped by the user.
- Checking reference 51/65:
  -> INFO: Now checking 2 results for matching title: 'Dynamic pooling and unfolding recursive autoencoders for paraphrase detection'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Pennington'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 52/65:
  -> INFO: Now checking 6 results for matching title: 'Reasoning with heterogeneous graph representations for knowledge-aware question answering'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Wen, Zhou, Huang, Sun, Pan'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Zhu, Yu, Sun'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Du, Huang, Zhang, Zhao'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Sun, Zhang, Zhang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 53/65:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Efficient fewshot learning with efl: A single transformer for all tasks
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Bommasani', 'Hendrycks', 'Song', 'Zhang', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Efficient+fewshot+learning+with+efl:+A+single+transformer+for+all+tasks manually and check the results.
        -> Author(s): Alex Wang, Rishi Bommasani, Dan Hendrycks, Daniel Song, and Zhilin Zhang
        -> Title:     Efficient fewshot learning with efl: A single transformer for all tasks
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 54/65:
  -> INFO: Now checking 10 results for matching title: 'Generating with confidence: Uncertainty quantification for black-box large language models'
       -> INFO: All authors matched!
- Checking reference 55/65:
  -> INFO: Now checking 10 results for matching title: 'Coqa: A conversational question answering challenge'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
       -> WARNING: Not all 11 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Tanjim, Bursztyn, Rossi, Kim, Ren, Muppala, Jiang, Kim, Park'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Tanjim, Bursztyn, Rossi, Kim, Ren, Muppala, Jiang, Kim, Park'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Venkataraghavan, Chavan'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 56/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2022.acl-long.229/.
  -> INFO: Now checking 10 results for matching title: 'TruthfulQA: Measuring how models mimic human falsehoods'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 57/65:
  -> INFO: Now checking 10 results for matching title: 'Ambigqa: Answering ambiguous open-domain questions'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Michael, Hajishirzi, Zettlemoyer'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Karpukhin, Oğuz, Wu, Edunov, Chen, Yih'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 58/65:
  -> INFO: Now checking 10 results for matching title: 'Opt: Open pre-trained transformer language models'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Li, Lin, Mihaylov, Ott, Shleifer, Shuster, Simig, Koura, Sridhar, Wang, Zettlemoyer'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Gonzalez, Roubaud, Schaverien, Largo, Parham, Francis, Hoffman, Dickey, Markey, Reece'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/65:
  -> INFO: Now checking 10 results for matching title: 'Llama: Open and efficient foundation language models'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lavril, Izacard, Martinet, Lacroix, Rozière, Goyal, Hambro, Azhar, Rodriguez, Joulin, Grave, Lample'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 60/65:
  -> Checking if provided link is pingable: https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md.
  -> INFO: Now checking 10 results for matching title: 'Llama 3 model card'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['AI@Meta', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Llama+3+model+card manually and check the results.
        -> Author(s): AI@Meta
        -> Title:     Llama 3 model card
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 61/65:
  -> INFO: Now checking 10 results for matching title: 'A note on importance sampling using standardized weights'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kong', '1992']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+note+on+importance+sampling+using+standardized+weights manually and check the results.
        -> Author(s): Augustine Kong
        -> Title:     A note on importance sampling using standardized weights
        -> Year:      1992
     -> Manual search was skipped by the user.
- Checking reference 62/65:
  -> INFO: Now checking 1 results for matching title: 'Importance of search and evaluation strategies in neural dialogue modeling'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 63/65:
  -> Checking if provided link is pingable: http://arxiv.org/abs/1707.06347.
  -> INFO: Now checking 10 results for matching title: 'Proximal policy optimization algorithms'
       -> INFO: All authors matched!
- Checking reference 64/65:
  -> INFO: Now checking 10 results for matching title: 'Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'He, Liu, Tao, Luo, Zeng, Su, Meng, Chen, Yoshie'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Jiang, Min, Chen, Chen, Zhao, Fang, Wen'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Zhuang, Jin, Chen'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Huang, Zhai, Cao, Ye, Zhao, Lin'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wu, Lu, Zuo, Wu'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Cao, Liu, Zhou, Dong'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wu, Zou, Liang'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Qian, Zhou, Peng, Zhao, Huang, Xie, Nie'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Whitehouse, Li, Weston, Kulikov, Saha'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 65/65:
  -> INFO: Now checking 10 results for matching title: 'Decoupled weight decay regularization'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 1: = −
-> Invalid unicode use found on p. 2: log q(yt|y<t) = log p(yt|y<t) −λ max
-> Invalid unicode use found on p. 3: ℓ′(next) ←ℓ(next) −λπ
-> Invalid unicode use found on p. 3: log q(y(t)|y(t+1)) = log p(y(t)|y(t+1)) −λ max
-> Invalid unicode use found on p. 5: ˆH = −
-> Invalid unicode use found on p. 6: Denote Yi = −log ˆp(c(s(i))), where c(s(i)) is the cluster containing s(i). The estimator in Equation 10 is then PN
-> Invalid unicode use found on p. 6: i=1 ˜wiYi. Now define Xi = −log p(s(i)), and let X′
-> Invalid unicode use found on p. 6: i = Xi−µX and Y ′
-> Invalid unicode use found on p. 6: i = Yi−µY
-> Invalid unicode use found on p. 6: −α
-> Invalid unicode use found on p. 6: ˜wi,jointYi −αMI
-> Invalid unicode use found on p. 8: numbers are mean±std over 5 jackknife samples of size 200. The symbol “−” indicates that the
-> Invalid unicode use found on p. 15: for t = T−1 downto 0 do
-> Invalid unicode use found on p. 15: ℓ′(next) ←ℓ(next) −λπ
-> Invalid unicode use found on p. 16: pair, (ii) all proper prefixes of the hypothesis (lengths 1 . . . Lh −1) each followed by [TRUNC], and
-> Invalid unicode use found on p. 16: (iii) all proper prefixes of the premise (lengths 1 . . . Lp −1) similarly tagged. A single example with
-> Invalid unicode use found on p. 16: tokenized lengths (Lp, Lh) thus contributes 1 + (Lh −1) + (Lp −1) training instances, covering
-> Invalid unicode use found on p. 17: s∈S E(y≤t, s) −Etarget
-> Invalid unicode use found on p. 17: Var{ ˆH} −Vtarget
-> Invalid unicode use found on p. 17: defined by 1 −E(si, sj) for every pair si, sj of iteratively prompted responses (see Equation 6 for
-> Invalid unicode use found on p. 20: h(Zi) −α
-> Invalid unicode use found on p. 20: g(Zi) −µg
-> Invalid unicode use found on p. 20: is unbiased, because Ep[g(Z) −µg] = 0.
-> Invalid unicode use found on p. 20: g = Var[g(Z)], and σhg = Cov[h(Z), g(Z)]. Writing H = h(Z) −µ and G =
-> Invalid unicode use found on p. 20: g(Z) −µg, we have
-> Invalid unicode use found on p. 20: H −αG
-> Invalid unicode use found on p. 20: h −2α σhg + α2σ2
-> Invalid unicode use found on p. 21: −2σhg + 2ασ2
-> Invalid unicode use found on p. 21: h (1 −ρ2),
-> Invalid unicode use found on p. 21: σhσg is the correlation between h and g, so variance is reduced by the factor 1 −ρ2 such
-> Invalid unicode use found on p. 21: i = Xi −µX with Xi = −log p(s(i))
-> Invalid unicode use found on p. 21: are strongly correlated with the negative cluster probabilities Yi = −log ˆp(c(s(i))), being based on
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Bracket content ['5–10'] on p. 1 could not be matched to a reference.
   -> Sentence:  These models extend masked language modeling by learning iterative denoising schedules to
progressively resolve masked spans [5–10]
-> Warning: Bracket content ['0', ' 1'] on p. 4 could not be matched to a reference.
   -> Sentence:  For MDMs, we randomly select the masking probability uniformly in [0, 1] and 
independently replace tokens with [MASK] with that probability
-> Warning: Bracket content ['19–22'] on p. 7 could not be matched to a reference.
   -> Sentence:  While these methods have also been adapted for text classification and regression in NLP 
[19–22], their extension to free-form NLG presents specific challenges due to semantic invariances 
inherent in generated text [1, 23]
-> Warning: Bracket content ['24–31'] on p. 7 could not be matched to a reference.
   -> Sentence:  Several studies have proposed prompting or fine-tuning language models to explicitly 
articulate their confidence levels [24–31], though this typically requires additional supervision
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 420 sentences on 11 pages -> Avg. of 43.0 sentences per page
-> Warning: Reference '5' never used in the document's text.
-> Warning: Reference '6' never used in the document's text.
-> Warning: Reference '7' never used in the document's text.
-> Warning: Reference '8' never used in the document's text.
-> Warning: Reference '9' never used in the document's text.
-> Warning: Reference '18' never used in the document's text.
-> Warning: Reference '19' never used in the document's text.
-> Warning: Reference '20' never used in the document's text.
-> Warning: Reference '21' never used in the document's text.
-> Warning: Reference '22' never used in the document's text.
-> Warning: Reference '23' never used in the document's text.
-> Warning: Reference '24' never used in the document's text.
-> Warning: Reference '25' never used in the document's text.
-> Warning: Reference '26' never used in the document's text.
-> Warning: Reference '27' never used in the document's text.
-> Warning: Reference '28' never used in the document's text.
-> Warning: Reference '29' never used in the document's text.
-> Warning: Reference '30' never used in the document's text.
-> Warning: Reference '31' never used in the document's text.
-> Warning: Reference '33' never used in the document's text.
-> Warning: Reference '36' never used in the document's text.
-> Warning: Reference '38' never used in the document's text.
-> Warning: Reference '42' never used in the document's text.
-> Warning: Reference '43' never used in the document's text.
-> Warning: Reference '47' never used in the document's text.
-> Warning: Reference '49' never used in the document's text.
-> Warning: Reference '51' never used in the document's text.
-> Warning: Reference '52' never used in the document's text.
-> Warning: Reference '53' never used in the document's text.
-> Warning: Reference '54' never used in the document's text.
-> Warning: Reference '65' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> WARNING: Reference with index 17 (Ref. ID = 18) has no associated sentence!
-> WARNING: Reference with index 18 (Ref. ID = 19) has no associated sentence!
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> WARNING: Reference with index 25 (Ref. ID = 26) has no associated sentence!
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> WARNING: Reference with index 28 (Ref. ID = 29) has no associated sentence!
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
-> WARNING: Reference with index 32 (Ref. ID = 33) has no associated sentence!
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
-> WARNING: Reference with index 46 (Ref. ID = 47) has no associated sentence!
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> WARNING: Reference with index 51 (Ref. ID = 52) has no associated sentence!
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
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
  -> Found 25 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 17
```

---

```
...
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
Enter a supported referencing template (['numeric', 'authoryear_round', 'authoryear_square']): numeric
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Estimating the predictive uncertainty of free-form responses' on page 2
- Found following heading '3 - Methods' on page 3
- Found following heading '4 - Related Work' on page 7
- Found following heading '5 - Experiments' on page 8
- Found following heading '6 - Discussion and limitations' on page 9
- Found following heading '7 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Extension to masked diffusion models' on page 16
- Found following appendix 'B - Additional implementation details' on page 17
- Found following appendix 'C - Qualitative case studies' on page 19
- Found following appendix 'D - Mutual information results' on page 21
- Found following appendix 'E - Variance reduction with control variates' on page 21
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 16
All found references: 65
-> Warning: Malformed author string: 'AI@Meta'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                              link  valid
0       1     Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar  ...                                     None
1       2  Yasin Abbasi Yadkori, Ilja Kuzborskij, András ...  ...                                     None
2       3  Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes,...  ...                                     None
3       4        Franz Aichberger, Lily Chen, and John Smith  ...                                     None
4       5                             Jacob Austin and et al  ...                                     None
..    ...                                                ...  ...                               ...    ...
60     61                                     Augustine Kong  ...                                     None
61     62  Ilia Kulikov, Alexander Miller, Kyunghyun Cho,...  ...                                     None
62     63  John Schulman, Filip Wolski, Prafulla Dhariwal...  ...  http://arxiv.org/abs/1707.06347.   None
63     64  Daya Guo, Dejian Yang, Haowei Zhang, Junxiao S...  ...                                     None
64     65                   Ilya Loshchilov and Frank Hutter  ...                                     None

[65 rows x 10 columns]
- Checking reference 1/65:
  -> INFO: Now checking 4 results for matching title: 'Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation'
       -> INFO: All authors matched!
- Checking reference 2/65:
  -> INFO: Now checking 1 results for matching title: 'To believe or not to believe your llm'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Abbasi-Yadkori, Szepesv'ari'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/65:
  -> INFO: Now checking 3 results for matching title: 'The curious case of neural text degeneration'
       -> INFO: All authors matched!
- Checking reference 4/65:
  -> INFO: Now checking 10 results for matching title: 'Semantically diverse language generation'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Schweighofer, Ielanskyi, Hochreiter'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yu, Tong, Fu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 5/65:
  -> INFO: Now checking 6 results for matching title: 'Diffuseq: Sequence to sequence text generation with diffusion models'
  -> WARNING: None of the 6 results matched the expected title!
  -> INFO: Now checking 63 results for matching title: 'Diffuseq: Sequence to sequence text generation with diffusion models'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Bathen, Saldamli, 0003, 0003'
       -> WARNING: Not all 62 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zia, Bhattacharyya, Liu, Berniker, 0003, Nespolo, Kondo, Kasai, Hirasawa, Liu, Wang, Futrega, Puget, 0002, 0001, Fujii, Hachiuma, Masuda, 0001, 0007, Xu, Islam, 0008, Pang, 0001, Nwoye, Sestini, Padoy, Nielsen, Schüttler, Sentker, Husseini, Baltruschat, Schmitz, Werner, Matsun, Farooq, Saeed, Viera, Yaqub, Getty, Xia, Zhao, Duan, Yao, Lou, 0011, Han, Noble, Wu, Alshirbaji, Jalal, Arabian, Ding, Moeller, Chen, He, Maier-Hein, Stoyanov, Speidel, Jarc'
       -> WARNING: Not all 75 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Thomas, Foraker, Zamstein, Morrow, Payne, Wilcox, Haendel, Chute, Gersing, Walden, Bennett, Eichmann, Guinney, Kibbe, Liu, Pfaff, Robinson, Saltz, Spratt, Starren, Suver, Wu, Gabriel, Hong, Kostka, Lehmann, Moffitt, Morris, Palchuk, Zhang, Zhu, Amor, Bissell, Clark, Girvin, Lee, Miller, Walters, Chae, Cook, Dest, Dietz, Dillon, Francis, Fuentes, Graves, Neumann, O&apos;Neil, Sheikh, Volz, Zampino, Bozzette, Deacy, Garbarini, Kurilla, Michael, Rutter, Temple-O&apos;Connor, Bradwell, Manna, Qureshi, Saltz, McMurry, Bramante, Harper, Hernandez, Koraishy, Mariona, Mattapally, Saha, Vedula, Fu, Mathews, Mendelevitch'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zitomer, Karr, Kerstens, Perry, Ruth, Adrean, Cornelius, Dachenhaus, Dinkins, Harrington, Kim, Owens, Revekant, Schroeder, Sink, Valente, Woodis, Rivers'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Estuar, Tan, Tan, Abao, Aureus'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Tan, Estuar, Tan, Abao, Aureus'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Tan, Estuar, Tan, Abao, Aureus'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Chang, Bathen, Troia, 0003'
       -> WARNING: Not all 43 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Roberts, Chung, Levskaya, Mishra, Bradbury, Andor, Narang, Lester, Gaffney, Mohiuddin, Hawthorne, Lewkowycz, Salcianu, Zee, Goodman, Soares, Hu, Tsvyashchenko, Chowdhery, Bastings, Bulian, Garcia, Ni, Chen, Kenealy, Clark, Lee, Garrette, Lee-Thorp, Raffel, Shazeer, Ritter, Bosma, Passos, Maitin-Shepard, Fiedel, Omernick, Saeta, Sepassi, Spiridonov, Newlan, Gesmundo'
       -> WARNING: Not all 67 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Chowdhery, Narang, Devlin, Bosma, Mishra, Roberts, 0001, Chung, Sutton, Gehrmann, Schuh, Shi, Tsvyashchenko, Maynez, Rao, Barnes, Tay, Shazeer, Prabhakaran, Reif, 0002, Hutchinson, Pope, Bradbury, Isard, Gur-Ari, Yin, Duke, Levskaya, Ghemawat, Dev, Michalewski, Garcia, Misra, Robinson, Fedus, Zhou, Ippolito, Luan, Lim, Zoph, Spiridonov, Sepassi, Dohan, Agrawal, Omernick, Dai, Pillai, Pellat, Lewkowycz, Moreira, Child, Polozov, Lee, Zhou, 0002, Saeta, Diaz, Firat, Catasta, Wei, Meier-Hellstern, Eck, Dean, Petrov, Fiedel'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Clay, Wyetzner, Gaudio, Xia, Moshova, Segan, Lipson'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 6/65:
  -> INFO: Now checking 2 results for matching title: 'Dsp: Diffusion-based span prediction for masked text modeling'
  -> WARNING: None of the 2 results matched the expected title!
  -> INFO: Now checking 446 results for matching title: 'Dsp: Diffusion-based span prediction for masked text modeling'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Silva, Melo, Oliveira, Santos, Jr.'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang, Tolentino, Lu, Jose, Sangalang, Lee, Chang'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ghanim, Santriaji, Solihin'
       -> WARNING: Not all 72 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, Min, 0029, 0001, 0008, Timofte, Zhai, Gao, Cao, Kou, Dong, Jia, Li, 0002, Hu, Deng, Xiao, 0011, 0012, 0011, 0003, 0008, Cong, 0073, Fu, Zhang, Zhang, Shi, Xu, Xiao, Ma, Agarla, Celona, Rota, Schettini, Huang, 0006, Wang, Lei, Liu, Hong, Chuang, Lin, Guan, Chen, Huang, Tasi, Kao, Fan, Kong, Zhou, 0026, Lai, Chen, Wang, 0001, Chen, Zhu, Guo, Zhao, Yin, Wang, Meftah, Fezza, Hamidouche, Déforges, Shi, Mansouri, Motamednia, Bakhtiari, Aznaveh'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ghosal, Ishai, Korb, Kushilevitz, Sahai'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lee, Li, Abbasi, 0001'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Belmekki, Alouini'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, Sabek, Cafarella'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lee, Li, Abbasi, 0001'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Belmekki, Alouini'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cheng, Cheng, Chiu, Chong'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Alzayer, Abuolaim, Chan, Yang, 0001, Kar'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Gao, Xu, Comaniciu, Kamen'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Nguyen, Torres, Rueda, Sim, Campbell, Kapralos, Beavers, Dubrowski, Bhat, 0001'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0005, Raheja, Kaiser-Schatzlein, Perry, Joshi, Hugues-Nuger, Chowdhury'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lingelbach, 0002, Hwang, Kurenkov, Martín-Martín, Zhang, 0001, 0001'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Hart, Yu, 0001'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ghosal, Ishai, Korb, Kushilevitz, Sahai'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'He, She, Guo, Watson, Weng, Perepechaenko, Kuang'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Kuang, He, McKenzie, Redding'
       -> WARNING: Not all 54 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Laurençon, Saulnier, Wang, Akiki, Moral, Scao, Werra, Mou, Ponferrada, Nguyen, Frohberg, Sasko, Lhoest, McMillan-Major, Dupont, Biderman, Rogers, Allal, Toni, Pistilli, Nguyen, Nikpoor, Masoud, Colombo, 0001, Villegas, Thrush, Longpre, 0005, Weber, Muñoz, Zhu, Strien, Alyafeai, Almubarak, Vu, Gonzalez-Dios, Soroa, Dey, Suarez, Gokaslan, Bose, Adelani, Phan, Tran, Yu, Pai, Chim, Lepercq, Ilic, Mitchell, Luccioni, Jernite'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Belmekki, Alouini'
       -> WARNING: Not all 16 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Chen, Paredes, 0001, Brunson, Thomas, Martinez, Lucero, Magoc, Solberg, Snigurska, Ser, Prosperi, 0001, Bjarnadottir, 0001'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Alzayer, Abuolaim, Chan, Yang, 0001, Kar'
       -> WARNING: Not all 62 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zia, Bhattacharyya, Liu, Berniker, 0003, Nespolo, Kondo, Kasai, Hirasawa, Liu, Austin, Wang, Futrega, Puget, 0002, 0001, Fujii, Hachiuma, Masuda, 0001, 0007, Xu, Islam, 0008, Pang, 0001, Nwoye, Sestini, Padoy, Nielsen, Schüttler, Sentker, Husseini, Baltruschat, Schmitz, Werner, Matsun, Farooq, Saeed, Viera, Yaqub, Getty, Xia, Zhao, Duan, Yao, 0011, Han, Noble, Wu, Alshirbaji, Jalal, Arabian, Ding, Moeller, Chen, He, Maier-Hein, Stoyanov, Speidel, Jarc'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lingelbach, 0002, Hwang, Kurenkov, Martín-Martín, Zhang, 0001, 0001'
       -> WARNING: Not all 39 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0016, Xie, Ayyadhury, Ge, Gupta, Gupta, Gu, 0010, Lee, Kim, Li, Upschulte, Dickscheid, Almeida, 0003, Han, 0009, Labagnara, Rahi, Kempster, Pollitt, Espinosa, Mignot, Middeke, Eckardt, Li, Li, Cai, Bai, Greenwald, Valen, Weisbart, Cimini, Li, Zuo, Brück, Bader, 0044'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Belmekki, Alouini'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0005, Raheja, Kaiser-Schatzlein, Perry, Joshi, Hugues-Nuger, Chowdhury'
       -> WARNING: Not all 25 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ji, Qiu, 0008, Zhang, Wang, Duan, He, Zhou, 0001, Zeng, Ng, Dai, Pan, O&apos;Gara, Lei, Xu, Tse, 0001, McAleer, 0001, 0001, Zhu, Guo, 0001'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Hart, Yu, 0001'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang, Belmekki, Kishk, Alouini'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ghosal, Ishai, Korb, Kushilevitz, Sahai'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/65:
  -> INFO: Now checking 10 results for matching title: 'Maskgpt: Uniform denoising diffusion for language'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Maskgpt: Uniform denoising diffusion for language'
       -> WARNING: Not all 78 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Huang, Chen, Yang, Liu, Li, Lin, Tseng, Diwan, Shih, Chen, Chen, Hsiao, Peng, Wang, Kuan, Lu, 0001, Yang, Gutierrez, Chuang, Huang, Arora, Lin, Yeo, Chang, Chien, Choi, Hsieh, Lin, Yu, Chiu, Guimarães, Han, Lin, Lin, Chang, Chang, Chen, Chen, Chen, Cheng, Dhawan, Fang, Fang, Chiang, Fu, Hsiao, Hsu, Huang, Wei, Lin, Lin, Lin, Lin, Liu, Lu, Pai, Pasad, Kuan, Shon, Tang, Tsai, Wei, Wei, Wu, Wu, Yang, Yang, Yip, Yuan, Noroozi, Chen, Wu, Livescu, Harwath, 0001, Lee'
       -> WARNING: Not all 17 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Shim, Tian, Arora, Wu, Petermann, Yip, Zhang, Tang, Zhang, Alharthi, Huang, Saito, Han, Zhao, Donahue, 0001'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0002, 0003, Wu, 0003, Gao, Li, Al-Dhahir'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yang, 0004, Cong, Bi, Hawbani'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yin, 0008, Gong, Albrecht'
       -> WARNING: Not all 100 authors from the found ref. were matched (only 4)
                   Unmatched authors = '0001, 0003, You, Alvarez, Gemeren, Chen, Zou, Wang, Li, Han, Zhang, Wang, Liu, 0004, Lv, 0001, Zhang, Ji, Chen, 0006, 0001, 0001, Xu, Gou, Li, Xu, Zhang, Jiang, Lu, Jiao, 0001, 0006, 0002, 0001, 0001, Xie, 0006, Huang, Cheng, 0007, Zhu, 0001, 0042, 0003, 0005, 0001, Zhang, Jiang, Song, Lei, Luo, 0013, Liu, Li, Zhang, Wang, Chen, Luo, 0009, Cao, Chen, Dou, Liu, 0037, 0003, 0008, Gou, Wang, 0119, Zhao, Zhang, Yan, 0001, Li, Gao, Che, Sun, 0015, 0058, Pan, Xie, 0004, Li, Deng, Huang, 0001, Wan, Xu, 0001, 0001, 0005, Zou, Pan, Dai, 0004, Zhang'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yang, Jiang, Fang, Guo, Al-qaness'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0062, Wang, Liew'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0002, Zhang, Wu, 0003, Li, Al-Dhahir'
       -> WARNING: Not all 25 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Nandy, Adalgeirsson, Sinha, Kraljic, Cleron, Singh, Chaudhary, Ganti, Melancon, Zhang, Robishaw, Ciurdar, Secor, Robertsen, Climer, Le, Venkatesan, Chi, Li, McDermott, Shim, Onsan, Vaishnav, Guamán'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Chen, Ye, 0018, 0001, Liu, Xu, Ye, Yang, 0001, Huang, 0004, Zhang'
       -> WARNING: Not all 279 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'O&apos;Neill, Rehman, Maddukuri, 0004, Padalkar, Lee, Pooley, Gupta, Mandlekar, Jain, Tung, Bewley, Herzog, Irpan, Khazatsky, Rai, Gupta, Wang, Singh, Garg, Kembhavi, Xie, Brohan, Raffin, Sharma, Yavary, Jain, Balakrishna, Wahid, Burgess-Limerick, Kim, Schölkopf, Wulfe, Ichter, Lu, 0003, Le, Finn, 0053, Xu, 0001, Huang, Chan, Agia, Pan, Fu, Devin, Xu, Morton, Driess, Chen, Pathak, Shah, Büchler, Jayaraman, Kalashnikov, Sadigh, Johns, Foster, Liu, Ceola, 0002, Zhao, Stulp, Zhou, Sukhatme, Salhotra, Yan, Feng, Schiavi, Berseth, Kahn, Wang, 0001, Fang, Bao, Amor, Christensen, Furuta, Walke, Fang, Ha, Mordatch, Radosavovic, Leal, Liang, Abou-Chakra, 0001, Drake, 0001, 0007, Hsu, Bohg, Bingham, Wu, Gao, Hu, 0001, Wu, Sun, Luo, Gu, 0001, Oh, Wu, Lu, Yang, Malik, Silvério, Hejna, Booher, Tompson, Yang, Salvador, Lim, Han, Wang, Rao, Pertsch, Hausman, Go, Gopalakrishnan, Goldberg, Byrne, Oslund, Kawaharazuka, Black, Lin, 0002, Ehsani, Lekkala, Ellis, Rana, Srinivasan, Fang, Singh, Zeng, Hatch, Hsu, Itti, Chen, Pinto, 0001, Tan, Fan, Ott, Lee, Weihs, Chen, Lepert, Memmel, Tomizuka, Itkina, Castro, Spero, Du, Ahn, Yip, 0003, Ding, Heo, Srirama, 0001, Kim, Kanazawa, 0001, Heess, Joshi, Sünderhauf, Liu, Palo, Shafiullah, Mees, Kroemer, Bastani, Sanketi, Miller, Yin, Wohlhart, 0010, Fagan, Mitrano, Sermanet, Abbeel, Sundaresan, Chen, Vuong, Rafailov, Tian, Doshi, Martín-Martín, Baijal, Scalise, Hendrix, Lin, Qian, Zhang, Mendonca, Shah, Hoque, Julian, Bustamante-Gomez, Kirmani, Levine, Lin, Moore, Bahl, Dass, Sonawani, Song, Xu, Haldar, Karamcheti, Adebola, Guist, Nasiriany, Schaal, Welker, Tian, Ramamoorthy, Dasari, Belkhale, Park, 0003, Mirchandani, Osa, Gupta, Harada, Matsushima, Xiao, Kollar, Yu, Ding, Davchev, Zhao, Armstrong, Darrell, Chung, Jain, Vanhoucke, Zhan, Zhou, Burgard, Chen, 0004, Zhu, Geng, Liu, Xu, Li, Lu, 0001, 0003, Chebotar, Zhou, Zhu, 0003, Xu, Wang, Bisk, Cho, Lee, Cui, Cao, Wu, Tang, Zhu, Zhang, 0001, Li, Li, Iwasawa, Matsuo, Ma, Xu, Cui, 0016, Lin'
       -> WARNING: Not all 44 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ahmad, Anastasopoulos, Bojar, Borg, Carpuat, Cattoni, Cettolo, Chen, Dong, Federico, Haddow, Javorský, Krubinski, Lam, Ma, Mathur, Matusov, Maurya, McCrae, Murray, 0001, Negri, Niehues, 0001, Ojha, Ortega, Papi, Polák, Pospísil, Pecina, Salesky, Sethiya, Sarkar, Sikasote, Sperber, Stüker, Sudoh, 0001, Waibel, 0001, Wilken, Zemánek, Zevallos'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang, Yu, Jiang, Lan, Chang, Kautz, Li, 0004'
       -> WARNING: Not all 100 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Silva, Bard, Chard, Witt, Foster, Gibbs, Goble, Godoy, 0001, Haus, Hudson, Jha, Los, Paine, Suter, Ward, Wilkinson, Amaris, Babuji, Bader, Balin, Balouek, Beecroft, Belhajjame, Bhattarai, Brewer, Brunk, Caíno-Lores, Casanova, Cassol, Coleman, Coleman, Colonnelli, Silva, 0001, Elahi, Elfaramawy, Elwasif, Etz, Fahringer, Ferreira, Filgueira, Fosso-Tande, Gadelha, Gallo, Garijo, 0002, Gritsch, Grubel, Gueroudji, Guilloteau, Hamalainen, Enriquez, Huet, Kesling, Iborra, Jahangiri, Janssen, Jordan, Kanwal, Kunstmann, Lehmann, Leser, 0001, Liu, Lüttgau, Lupat, Fernández, Maheshwari, Malik, Marquez, Matsuda, Medic, Mohammadi, Mulone, Navarro, Nölp, Kinoshita, Prout, Crusoe, Ristov, Robila, Rosendo, Rowell, Rybicki, Sanchez, Saurabh, Saurav, Scogland, Senanayake, Shin, Sirvent, Skluzacek, Sly-Delgado, Soiland-Reyes, Souza, 0001, Talia, Tallent'
       -> WARNING: Not all 45 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ahmad, Anastasopoulos, Bojar, Borg, Carpuat, Cattoni, Cettolo, Chen, Dong, Federico, Haddow, Javorský, Krubinski, Lam, Ma, Mathur, Matusov, Maurya, McCrae, Murray, 0001, Negri, Niehues, 0001, Ojha, Ortega, Papi, Polák, Pospísil, Pecina, Salesky, Sethiya, Sarkar, Sikasote, Sperber, Stüker, Sudoh, 0001, Turchi, Waibel, 0001, Wilken, Zemánek, Zevallos'
       -> WARNING: Not all 42 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wake, Chen, Lv, Li, Huang, Cai, Zheng, Cooper, Zhou, Hu, Wang, Ji, Qiu, Zhu, Tian, Su, Zhang, Li, Song, Li, Liu, Hu, Wang, Zhou, Yang, Li, Zhu, Xie, Chen, Hu, Ren, Niu, Li, Zhao, Luo, Xu, Sha, Yan, Liu, Zhang, Dai'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Fattahi, Kontar'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Kontar'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Jiang, 0006, 0013, Zhang, Zhang, Wang, Alberts, Rominger, Zuo'
       -> WARNING: Not all 22 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0002, Hou, Xu, Xu, Zhou, Ke, 0001, 0012, Brendel, Maasch, Bai, Zhang, 0003, Cincotta, Henchcliffe, Leverenz, Cummings, Okun, 0001, Cheng, 0001'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, Kontar, Chowdhury'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Fan, 0001, Xie, 0002, Al-Dhahir'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Yu, Shin, Deng, Yuille, Chen'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0066, Al-Quraan, Sambo, Onireti, 0001'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0002, Sun, 0003, 0006, 0004, Safari, Al-Dhahir, Li'
       -> WARNING: Not all 15 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Miao, Oliaro, 0001, Cheng, Wang, Zhang, Wong, 0001, 0003, Chen, Arfeen, Abhyankar, Jia'
       -> WARNING: Not all 58 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Ramirez, Tosi, Stefano, Timofte, Costanzino, Poggi, Salti, Mattoccia, Zhang, Wu, Yin, Dong, Liu, 0014, 0008, Jin, Li, Ke, Obukhov, Wang, Metzger, Huang, Schindler, Huang, 0007, 0003, 0005, 0001, 0003, 0001, Li, Wang, Zhu, Geng, Zhang, Lan, Xu, 0005, Xu, Saini, Gupta, Mistry, Shukla, Jakhetiya, Jaiswal, Sun, Zheng, Ning, Cheng, Liu, Huang, Yang, Jiang, Peng, Huang, Hwang'
       -> WARNING: Not all 55 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Yang, Timofte, 0001, 0082, Guo, Zhao, 0006, 0001, 0002, Arora, Arora, Chen, Tang, 0085, Zhao, Chen, 0001, Mo, Bao, Hao, Ding, Li, Sun, 0003, Zhu, Jin, Wang, Zhan, Wu, Wu, Tu, 0001, Yeo, Oh, Kim, Ryu, Sun, Zhen, Pan, Dong, 0001, Du, Li, Luo, Zhu, Yao, Khowaja, Lee, Lee, Kim, Sharif, Khujaev, Tsoy'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cheng, 0002, 0015, Hu, O&apos;Connor, Hauptmann, Whitefoot'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Masud, Bouazizi, Ohtsuki'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Jung, Zhang, Aldeneh, Higuchi, Gichamba, Theobald, Abdelaziz, 0001'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0036, Serra-Gómez, Wu, Alonso-Mora'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Forhad'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, Hwu'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Li, Luo, Mirzaei, Rafiei, Riley, Sheikhi, Siavashpour, Tavakoli, Hauer, Kondrak'
       -> WARNING: Not all 20 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Tian, 0008, Jung, Yip, Masuyama, Chen, 0001, Tang, Baali, Alharthi, Zhang, Deng, Srivastava, Wu, Liu, Raj, Jin, Song, 0001'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, Liu'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0037, Ashbaugh, Chimitt, Hassan, 0001, Jaiswal, Kim, Mao, Perry, Ren, Su, Varghaei, 0058, Chan, Ross, Wang, Jain, 0002'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Jung, Zhang, Aldeneh, Higuchi, Theobald, Abdelaziz, 0001'
       -> WARNING: Not all 25 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Yang, Jin, Huang, Kuang, 0001, Gu, Liu, Liu, Chai, Xiao, 0011, Xu, Du, Yan, Tang, Alessio, Holste, Zhang, Wang, Che, Pfister, 0005, Ni'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, Hwu'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Fan, 0001, Xie, 0002, Al-Dhahir'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Fattahi, Kontar'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0036, Serra-Gómez, Wu, Alonso-Mora'
       -> WARNING: Not all 17 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Fu, Song, Lv, Cao, Jia, Li, 0001, Liu, Luo, Qiu, Tu, Wang, Wei, 0001, Yi, Zou'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0001, Vinod, Mahmud, 0001, Delp, Wong, Xi, AlMughrabi, Haroon, Marques, Radeva, Tang, Yang, Gao, Liang, Jueluo, Wang'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cheng, Shu, Lee, Zhu, Suhail, Chen, Chen, Wang, Zhang, Wang, Yang, Hsin, Shih, Lee, Cheng, Pamarti, Kou, Wang'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cheng, 0002, 0015, Hu, O&apos;Connor, 0001, Whitefoot'
       -> WARNING: Not all 20 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Tian, 0008, Jung, Yip, Masuyama, Chen, 0001, Tang, Baali, Alharthi, Zhang, Deng, Srivastava, Wu, Liu, Raj, Jin, Song, 0001'
       -> WARNING: Not all 45 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Dang, Singh, D&apos;souza, Ahmadian, Salamanca, Smith, Peppin, Hong, Govindassamy, Zhao, Kublik, Amer, Aryabumi, Campos, Tan, Kocmi, Strub, Grinsztajn, Flet-Berliac, Locatelli, Lin, Talupuru, Venkitesh, Cairuz, Yang, Chung, Ko, Shukayev, Bae, Piktus, Castagné, Cruz-Salinas, Kim, Crawhall-Stein, Morisot, 0006, Blunsom, Zhang, Gomez, Frosst, Fadaee, Ermis, Üstün, Hooker'
       -> WARNING: Not all 47 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Li, Li, 0003, Gui, Yang, Yu, Wang, Cai, Zhou, Qian, Chen, Xue, 0001, 0001, Chen, Ding, Du, Mu, Pei, 0001, Swayamdipta, Neiswanger, 0001, Hu, Zhu, 0001, Lu, Qin, Fu, Tu, 0005, Yoo, Zhang, Rossi, Zhan, 0002, Ferrara, 0002, Huang, 0001, Rothenberg, Ji, Yu, 0016, Dong'
       -> WARNING: Not all 47 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Deng, Yao, Tang, Guo, Lu, Xiong, Yu, Cap, Cai, Lan, Zhao, Galdran, Kumar, Deotale, Das, Paik, Lee, Lee, Chen, Li, Li, Hou, Wu, Wang, Fischer, Kramer, Du, Zhang, Sanchez, Ulloa, Heredia, Garcia, Xu, Cheng, Wang, Moreau, Bozek, Innani, Baid, Kefas, Landman, Wang, Zhao, Yin, Yang, Huo'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Jiang, Ho, Lin'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Maldonado-Ruiz, Pulval-Dady, Wang, Madhoun, 0001'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0035, Osei, Hu, Stein'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang, Lin, Johnson, 0004, Tan, Gao, Min, Hu, 0009'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yuan, 0059, Proutière'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cai, 0001, Mojahedfar, Liu'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Linderman, Wallace, Heyde, Wieman, Brey, Hansen, Shamsi, Liu, Gelb, Bashir'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0023, Cai, Heidari, 0001, Chen'
       -> WARNING: Not all 18 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Goodman, Buehler, Clary, Coenen, Donsbach, Horne, Lahav, MacDonald, Michaels, Narayanan, Pushkarna, Riley, Santana, Sweeney, Weaver, Yuan, Morris'
       -> WARNING: Not all 32 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Gómez-Pascual, Naccache, Xu, Hooshmand, Wretlind, Gabrielli, Lombardo, Buckley, Tijms, Vos, Kate, Engelborghs, Sleegers, Frisoni, Wallin, Lleó, Popp, Martinez-Lage, Streffer, Barkhof, Zetterberg, Visser, Lovestone, Bertram, Nevado-Holgado, Gualerzi, Picciolini, Proitsi, Verderio, Botía, Legido-Quigley'
       -> WARNING: Not all 15 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Jevsikov, Lane, Alajrami, Naidoo, Fernandes, Sehmi, Alzetani, Demetrescu, Azarmehr, Serej, Stowell, Shun-Shin, Francis, Zolgharni'
       -> WARNING: Not all 102 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Qiu, Yu, Zhao, Zhang, Xu, Li, Li, Bao, Chai, Chen, Chen, Cheng, Dai, Di, Dong, Duan, Feng, Fu, Guo, Guo, 0001, Hu, Hu, Hu, Huang, Huang, 0004, Kong, Li, Li, Li, Liao, Liu, Liu, Liu, Liu, Liu, Liu, Liu, Liu, Lu, Ma, Miao, Ni, Ning, Pan, Ren, Shu, Sun, Sun, Tao, Tian, Wang, Wang, 0005, Wang, Wang, Wang, Wang, Wang, Wang, Wang, Wen, Wu, Wu, Wu, Wu, Xia, Xiang, Xing, Xiong, Xiong, Xu, Xu, 0035, Yang, Yang, Yang, Ye, Ye, Yu, Yu, Zeng, Zhang, Zhang, 0001, Zhang, 0090, Zhang, Zhang, Zhao, Zhao, Zheng, 0021, Zhou, Zhu, Yang, Wang, Wang'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ali, Wang'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Alagic, Bai, Poremba'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = '0023, Cai, Heidari, 0001'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Alajrami, Jevsikov, Naidoo, Fernandes, Azarmehr, Dinmohammadi, Shun-Shin, Serej, Francis, Zolgharni'
       -> WARNING: Not all 15 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cedergren, Laval, Falahati, Falk, Kang, Karlsson, Lyazidi, Mirzaei, 0001, Pradas, Schliwa-Bertling, Singh, Tano, Voicu'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0023, Wang, Heidari, 0048, 0001, Chen, Sun'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yuan, Proutière'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Berry, Kath, Lodhy, Ly, Percus, Hyman, Moran, Strait, Sweeney, Viswanathan, Stauffer'
       -> WARNING: Not all 34 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Li, Chen, Langda, Pu, Zhu, Zhou, Kalds, Zhang, Bhati, Leonard, Huang, Li, Cuoji, Wang, Zhu, Wu, Cuomu, Gui, Li, Wang, 0135, Fang, Jia, Pu, Pan, 0003, Wang, 0014, Han, Chen, Zhou, Pausch, Wang'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Nusair, Karatepe, Okumus, Alfarhan'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ali, Chew'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lo, Teferi, Wong, Abi-Jaoudé, Chopra, Charow, Zhang, 0006, Levinson, Cleverley, Henderson, Voineskos, Wiljer'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0005, Vakanski, Xian'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Salvatore, Kundu, Friese, Lee, Fritsche, Mondul, Hanauer, Pearce, Mukherjee'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Tiwari, Budhathoki, Baker, Sekizkardes, Zhu, Kusuma, Hopkinson, Steckel'
       -> WARNING: Not all 38 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Boulogne, Lorenz, Kienzle, Schön, Ludwig, Lienhart, Jégou, Li, Chen, Wang, Maniparambil, Müller, Mertes, Schröter, Hellmann, Elia, Dirks, Bossa, Berenguer, Mukherjee, Vandemeulebroucke, Sahli, Deligiannis, Gonidakis, Huynh, Razzak, Bouadjenek, Verdicchio, Borrelli, 0003, Meakin, Lemm, Russ, Ionasec, Paragios, Ginneken, Revel'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Guo, Chen, Liu, 0009, Xie, Liu, Palyo, Miller, Sinusas, Staib, Spottiswoode, 0001, Dvornek'
       -> WARNING: Not all 21 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Li, Qu, Chen, Bassi, Lai, 0012, Xue, Chen, Lin, Tang, Cao, Han, Zhang, Liu, Zhang, Ma, Wang, Zhang, Yuille, Zhou'
       -> WARNING: Not all 49 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Sudre, Wijnen, Dubost, Adams, Atkinson, Barkhof, Birhanu, Bron, Camarasa, Chaturvedi, Chen, Chen, Chen, 0001, Evans, Ezhov, Gao, Gironés-Sangüesa, Gispert, Anson, Hughes, Ikram, Ingala, Jäger, Kofler, Kuijf, Kutnar, Lee, 0088, Lorenzini, Menze, Molinuevo, Pan, Puybareau, Rehwald, Su, Smith, Tillin, Tochon, Urien, Velden, Velpen, Wiestler, Wolters, Yilmaz, Groot, Vernooij, Bruijne'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ali, Wang'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Jia, 0003, Zhang, Bing, Quan, Chen, Knoll, 0002'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yin, Feng, Lau, Qiu, Sham, So'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ma, Guerra, Caillet, Zhao, Clarke, Maksymenko, Deslauriers-Gauthier, Zhu, Farina'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Unmesh, 0018, Manam, Chi, Chidambaram, Quinn, Ramani'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Brierley, Perry, Gao, Li, Prishchepov, Li, Han'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yang, Qiao, Zuo, Wu, Ben-Gal'
       -> WARNING: Not all 17 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ye, Wang, 0010, Guo, Zhang, Dai, Zhai, Hu, Ali, Ji, Ran, Qiu, Che, Wang, 0029, Zhu'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ahmad, 0001, Lai, 0003'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Asfour, Khamas, Ball, Huang, Allanic, Berre, Quendo, Leuliet, Merlet'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Liu, Qi, Khan, Meng, Li'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang, Chen, Bernardo, Hong, Altafini'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Rosenberg, Zhao, Hamey, Nguyen, Orgun'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wu, Qin, 0002, Jeon'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Du, Cao, Garg, Alrashoud, Shukla'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Du, Cao, Garg, Kaddoum, Alrashoud'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Li, Yi, Alfarraj, Tolba, Sangaiah, Sherratt'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang, Mao, Dharejo, Javed, Alathbah'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yu, Cai, 0054, Yang, Kot'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lin, Alemu, Nanayakkara, Shull'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, 0005, 0001, Zomaya'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, Smolic'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0003, Xiao, Ali, Ye, Jiao'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ye, Tian, 0008, 0001, Ye, Yang, Wang, 0011, 0001, 0001'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Grimson, Almeida, Bai, Angarita, Pacheco, Schmitt, Flecker, Gomes'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Anagolum, Alavisamani, 0005, Qureshi'
       -> WARNING: Not all 26 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Chen, Mistry, Sayed, Williams, Iotti, Atef, Padmaraju, Malinowski, Che, Sukkar, Younce, Horth, Dziashko, Guan, Gill, Seyoum, Marsh, Schmidt, Burrell, Basak, Chapman, Mikami, Rylyakov, Leven, Jaeger'
       -> WARNING: Not all 24 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wood, Lublinsky, Roytman, Singh, Adam, Adebayo, Chang, Dang, Desai, Dolfi, Emami-Gohari, Eres, Goto, Joshi, Koyfman, Nassar, Patel, Selvam, Shah, Surendran, Tsuzuku, Zerfos, Daijavad'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Xu, Wan, Parisio'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Han, Soon, Ruan, Moghaddassian, Leon-Garcia'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'II, Shoemaker, Goldman, Stewart, Rytting, Findlater, Boyd-Graber'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Liao, Gong, Sun, Zhang, Ning, Au'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Yu, Lipani'
       -> WARNING: Not all 94 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Kristan, Matas, Tokmakov, Felsberg, Zajc, Lukezic, Tran, Vu, Björklund, Chang, Fernández, Attari, Chan, Chen, 0032, Collins, Cui, Devarapu, Du, 0001, Fan, 0001, 0003, Gorthi, Goyal, Han, Hatuwal, 0001, Hu, Huang, Huang, Jiang, Kang, Palaniappan, Kittler, Lai, 0044, Li, 0034, Liang, Lin, Ling, 0018, Liu, Lu, Luo, Miao, Mogollon, Pang, Pochimireddy, Prutyanov, Rahmon, 0001, Siam, Sigal, Sivapuram, Solovyev, Kazemi, Toubal, 0001, 0002, 0005, 0001, Wang, Wang, Wu, Wu, 0001, Xia, Xie, Xu, 0001, 0007, Xue, Yang, Yang, 0001, Yu, Yu, 0001, 0006, Zhang, 0001, Zheng, 0001, Zhou, Zhou, Zhou, Zhou, Zhu, 0003, 0003, Zunin'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0001, Jing, Wu, Zhu, Ji, Jiang, Hung, Funkhouser, Kuo, Angelova, Zhou'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = '0012, Lipani'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cao, Christofferson, Ruth, Rabbani, Mariakakis, 0001, Patel'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Guefrachi, Ghazzai, Alsharoa'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Tan, Qiu, Qu, Nie, Cheng, Chu, 0001, 0001'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/65:
  -> INFO: Now checking 10 results for matching title: 'inatk: Iterative noise aware text denoising'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sahoo', 'al', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=inatk:+Iterative+noise+aware+text+denoising manually and check the results.
        -> Author(s): A  Sahoo and et al
        -> Title:     inatk: Iterative noise aware text denoising
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 9/65:
  -> INFO: Now checking 3 results for matching title: 'Tuqdm: Token unmasking with quantized diffusion models'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ou', 'al', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Tuqdm:+Token+unmasking+with+quantized+diffusion+models manually and check the results.
        -> Author(s): X  Ou and et al
        -> Title:     Tuqdm: Token unmasking with quantized diffusion models
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 10/65:
  -> INFO: Now checking 9 results for matching title: 'Llada: Large language auto-diffusion for accelerated denoising'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Feng, Chen, Wei, Gao, Wu, Hu, Pu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/65:
  -> INFO: Now checking 1 results for matching title: 'A broad-coverage challenge corpus for sentence understanding through inference'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/65:
  -> INFO: Now checking 10 results for matching title: 'Deberta: Decoding-enhanced bert with disentangled attention'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wang'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lu, Ming, Mao, Wang, Zhao'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/65:
  -> INFO: Now checking 1 results for matching title: 'Glue: A multi-task benchmark and analysis platform for natural language understanding'
       -> INFO: All authors matched!
- Checking reference 14/65:
  -> INFO: Now checking 1 results for matching title: 'Triviaqa: A large scale distantly supervised challenge for reading comprehension'
       -> INFO: All authors matched!
- Checking reference 15/65:
  -> INFO: Now checking 10 results for matching title: 'Dropout as a bayesian approximation: Representing model uncertainty in deep learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
       -> WARNING: Not all 1 authors from the found ref. were matched (only 1)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/65:
  -> INFO: Now checking 10 results for matching title: 'Simple and scalable predictive uncertainty estimation using deep ensembles'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Liu, Lin, Padhy, Tran, Bedrax-Weiss'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/65:
  -> INFO: Now checking 10 results for matching title: 'Predictive uncertainty estimation via prior networks'
       -> INFO: All authors matched!
- Checking reference 18/65:
  -> INFO: Now checking 10 results for matching title: 'Ensemble distribution distillation'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Mlodozeniec'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Fathullah, Xia'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Ryabinin'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ding, Jiang, Zhang, Guo'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 19/65:
  -> INFO: Now checking 4 results for matching title: 'To trust or not to trust a classifier'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Kim, Gupta'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/65:
  -> INFO: Now checking 10 results for matching title: 'Calibration of text generation models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Desai', 'Durrett', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Calibration+of+text+generation+models manually and check the results.
        -> Author(s): Yayati Desai and Gregory Durrett
        -> Title:     Calibration of text generation models
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 21/65:
  -> INFO: Now checking 10 results for matching title: 'Uncertainty estimation in neural text regression'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Glushkova', 'Kobayashi', 'Suzuki', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Uncertainty+estimation+in+neural+text+regression manually and check the results.
        -> Author(s): Maria Glushkova, Shiori Kobayashi, and Junichi Suzuki
        -> Title:     Uncertainty estimation in neural text regression
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 22/65:
  -> INFO: Now checking 10 results for matching title: 'Uncertainty quantification in abstractive summarization'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Zhou', 'Lopez', 'Snyder', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Uncertainty+quantification+in+abstractive+summarization manually and check the results.
        -> Author(s): Yichao Wang, Bowen Zhou, Adam Lopez, and Benjamin Snyder
        -> Title:     Uncertainty quantification in abstractive summarization
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 23/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2023.emnlp-main.522/.
  -> INFO: Now checking 2 results for matching title: 'Increasing probability mass on answer choices does not always improve accuracy'
       -> INFO: All authors matched!
- Checking reference 24/65:
  -> INFO: Now checking 10 results for matching title: 'Teaching language models to script their confidence'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lin', 'Roller', 'Stewart', 'Zettlemoyer', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Teaching+language+models+to+script+their+confidence manually and check the results.
        -> Author(s): Jason Lin, Stephen Roller, Ashwin Stewart, and Luke Zettlemoyer
        -> Title:     Teaching language models to script their confidence
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 25/65:
  -> INFO: Now checking 10 results for matching title: 'Answer me this: Self-verifying large language models'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Jiang, Yu, Liu, Zhang, Li, Kwok'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zhang, Xu, Wang, Cui, Liu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/65:
  -> INFO: Now checking 1 results for matching title: 'Evaluating the reliability of self-assessment in language models'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Steiner, Buse, jumah, Westergaard, Jensen, Reed, Prilipko, Mennini, Láinez, Ravishankar, Sakai, Fontebasso, Khathami, MacGregor, Antonaci, Tassorelli, Lipton, Headache'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 27/65:
  -> INFO: Now checking 10 results for matching title: 'Learning to predict confidence for language models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jain', 'Perez', 'Glass', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Learning+to+predict+confidence+for+language+models manually and check the results.
        -> Author(s): Mohit Jain, Ethan Perez, and James Glass
        -> Title:     Learning to predict confidence for language models
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 28/65:
  -> INFO: Now checking 1 results for matching title: 'Crawling the internal knowledgebase of language models'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Cohen', 'Geva', 'Berant', 'Globerson', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Crawling+the+internal+knowledgebase+of+language+models manually and check the results.
        -> Author(s): Roi Cohen, Mor Geva, Jonathan Berant, and Amir Globerson
        -> Title:     Crawling the internal knowledgebase of language models
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 29/65:
  -> INFO: Now checking 1 results for matching title: 'The capacity for moral self-correction in large language models'
       -> WARNING: Not all 48 authors from the found ref. were matched (only 46)
                   Unmatched authors = 'Lukovsiut.e, Hatfield-Dodds'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/65:
  -> Checking if provided link is pingable: https://proceedings.mlr.press/v239/ren23a.html.
  -> INFO: Now checking 10 results for matching title: 'Self-evaluation improves selective generation in large language models'
       -> INFO: All authors matched!
- Checking reference 31/65:
  -> INFO: Now checking 1 results for matching title: 'Just ask for calibration: Strategies for eliciting calibrated confidence scores from language models fine-tuned with human feedback'
       -> INFO: All authors matched!
- Checking reference 32/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2024.emnlp-main.578/.
  -> INFO: Now checking 1 results for matching title: 'Contextualized sequence likelihood: Enhanced confidence scores for natural language generation'
       -> INFO: All authors matched!
- Checking reference 33/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2024.acl-long.276/.
  -> INFO: Now checking 1 results for matching title: 'Shifting attention to relevance: Towards the predictive uncertainty quantification of free-form large language models'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/65:
  -> INFO: Now checking 1 results for matching title: 'LM vs LM: Detecting factual errors via cross examination'
       -> INFO: All authors matched!
- Checking reference 35/65:
  -> INFO: Now checking 10 results for matching title: 'Conformal prediction in neural forecasting'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Rodríguez'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Rodr'iguez'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Zhang, Wang, Hu, Kang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 36/65:
  -> INFO: Now checking 10 results for matching title: 'Well-calibrated language models can be produced with small calibration sets'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ravfogel', 'Zalmanski', 'Goldberg', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Well-calibrated+language+models+can+be+produced+with+small+calibration+sets manually and check the results.
        -> Author(s): Shauli Ravfogel, Shachar Zalmanski, and Yoav Goldberg
        -> Title:     Well-calibrated language models can be produced with small calibration sets
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 37/65:
  -> INFO: Now checking 1 results for matching title: 'Distinguishing the knowable from the unknowable with language models'
       -> INFO: All authors matched!
- Checking reference 38/65:
  -> INFO: Now checking 10 results for matching title: 'Experts don’t cheat: learning what you don’t know by predicting pairs'
       -> INFO: All authors matched!
- Checking reference 39/65:
  -> INFO: Now checking 10 results for matching title: 'Diverse beam search: Decoding diverse solutions from neural sequence models'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2018)!
       -> INFO: All authors matched!
- Checking reference 40/65:
  -> INFO: Now checking 10 results for matching title: 'Contrastive decoding: Open-ended text generation as optimization'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Xu'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Arias, Rodemann, Heumann, Aßenmacher'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Ding, Arias, Rodemann, Aßenmacher, Chen, Fan, Heumann, Zhang'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Nguyen, Gupta'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 41/65:
  -> INFO: Now checking 4 results for matching title: 'A diversity-promoting objective function for neural conversation models'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Block, Becker, Duval, Clark, Al-Qawasmeh, Walker-VanSingel, Mannella, Phan, Monk, Fitzgerald'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 42/65:
  -> INFO: Now checking 1 results for matching title: 'Cluster-based beam search for pointer-generator chatbot grounded by knowledge'
       -> INFO: All authors matched!
- Checking reference 43/65:
  -> Checking if provided link is pingable: https://aclanthology.org/D16-1250/.
  -> INFO: Now checking 1 results for matching title: 'Learning principled bilingual mappings of word embeddings while preserving monolingual invariance'
       -> INFO: All authors matched!
- Checking reference 44/65:
  -> INFO: Now checking 10 results for matching title: 'Comparison of diverse decoding methods from conditional language models'
       -> INFO: All authors matched!
- Checking reference 45/65:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Paraphrase generation and information retrieval from stored text'
       -> INFO: All authors matched!
- Checking reference 46/65:
  -> INFO: Now checking 10 results for matching title: 'Machine translation evaluation with textual entailment features'
       -> INFO: All authors matched!
- Checking reference 47/65:
  -> INFO: Now checking 1 results for matching title: 'A survey of paraphrasing and textual entailment methods'
       -> INFO: All authors matched!
       -> WARNING: Year (2009) does not match expected year (2010)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/65:
  -> INFO: Now checking 10 results for matching title: 'Paraphrase identification using deep contextualized representations'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Issa', 'Mohler', 'Johnson', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Paraphrase+identification+using+deep+contextualized+representations manually and check the results.
        -> Author(s): Asma Issa, George Mohler, and John Johnson
        -> Title:     Paraphrase identification using deep contextualized representations
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 50/65:
  -> INFO: Now checking 10 results for matching title: 'Deep paraphrase identification'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yu', 'Dumsmyr', 'Knight', '2014']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+paraphrase+identification manually and check the results.
        -> Author(s): Lei Yu, Jimmy Dumsmyr, and Kevin Knight
        -> Title:     Deep paraphrase identification
        -> Year:      2014
     -> Manual search was skipped by the user.
- Checking reference 51/65:
  -> INFO: Now checking 2 results for matching title: 'Dynamic pooling and unfolding recursive autoencoders for paraphrase detection'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Pennington'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 52/65:
  -> INFO: Now checking 6 results for matching title: 'Reasoning with heterogeneous graph representations for knowledge-aware question answering'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Wen, Zhou, Huang, Sun, Pan'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Zhu, Yu, Sun'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Du, Huang, Zhang, Zhao'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Sun, Zhang, Zhang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 53/65:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Efficient fewshot learning with efl: A single transformer for all tasks
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Bommasani', 'Hendrycks', 'Song', 'Zhang', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Efficient+fewshot+learning+with+efl:+A+single+transformer+for+all+tasks manually and check the results.
        -> Author(s): Alex Wang, Rishi Bommasani, Dan Hendrycks, Daniel Song, and Zhilin Zhang
        -> Title:     Efficient fewshot learning with efl: A single transformer for all tasks
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 54/65:
  -> INFO: Now checking 10 results for matching title: 'Generating with confidence: Uncertainty quantification for black-box large language models'
       -> INFO: All authors matched!
- Checking reference 55/65:
  -> INFO: Now checking 10 results for matching title: 'Coqa: A conversational question answering challenge'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
       -> WARNING: Not all 11 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Tanjim, Bursztyn, Rossi, Kim, Ren, Muppala, Jiang, Kim, Park'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Tanjim, Bursztyn, Rossi, Kim, Ren, Muppala, Jiang, Kim, Park'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Venkataraghavan, Chavan'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 56/65:
  -> Checking if provided link is pingable: https://aclanthology.org/2022.acl-long.229/.
  -> INFO: Now checking 10 results for matching title: 'TruthfulQA: Measuring how models mimic human falsehoods'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 57/65:
  -> INFO: Now checking 10 results for matching title: 'Ambigqa: Answering ambiguous open-domain questions'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Michael, Hajishirzi, Zettlemoyer'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Karpukhin, Oğuz, Wu, Edunov, Chen, Yih'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 58/65:
  -> INFO: Now checking 10 results for matching title: 'Opt: Open pre-trained transformer language models'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Li, Lin, Mihaylov, Ott, Shleifer, Shuster, Simig, Koura, Sridhar, Wang, Zettlemoyer'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Gonzalez, Roubaud, Schaverien, Largo, Parham, Francis, Hoffman, Dickey, Markey, Reece'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/65:
  -> INFO: Now checking 10 results for matching title: 'Llama: Open and efficient foundation language models'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Lavril, Izacard, Martinet, Lacroix, Rozière, Goyal, Hambro, Azhar, Rodriguez, Joulin, Grave, Lample'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 60/65:
  -> Checking if provided link is pingable: https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md.
  -> INFO: Now checking 10 results for matching title: 'Llama 3 model card'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['AI@Meta', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Llama+3+model+card manually and check the results.
        -> Author(s): AI@Meta
        -> Title:     Llama 3 model card
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 61/65:
  -> INFO: Now checking 10 results for matching title: 'A note on importance sampling using standardized weights'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kong', '1992']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+note+on+importance+sampling+using+standardized+weights manually and check the results.
        -> Author(s): Augustine Kong
        -> Title:     A note on importance sampling using standardized weights
        -> Year:      1992
     -> Manual search was skipped by the user.
- Checking reference 62/65:
  -> INFO: Now checking 1 results for matching title: 'Importance of search and evaluation strategies in neural dialogue modeling'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 63/65:
  -> Checking if provided link is pingable: http://arxiv.org/abs/1707.06347.
  -> INFO: Now checking 10 results for matching title: 'Proximal policy optimization algorithms'
       -> INFO: All authors matched!
- Checking reference 64/65:
  -> INFO: Now checking 10 results for matching title: 'Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'He, Liu, Tao, Luo, Zeng, Su, Meng, Chen, Yoshie'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Jiang, Min, Chen, Chen, Zhao, Fang, Wen'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Zhuang, Jin, Chen'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Huang, Zhai, Cao, Ye, Zhao, Lin'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Wu, Lu, Zuo, Wu'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Cao, Liu, Zhou, Dong'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wu, Zou, Liang'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Qian, Zhou, Peng, Zhao, Huang, Xie, Nie'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Whitehouse, Li, Weston, Kulikov, Saha'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 65/65:
  -> INFO: Now checking 10 results for matching title: 'Decoupled weight decay regularization'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 1: = −
-> Invalid unicode use found on p. 2: log q(yt|y<t) = log p(yt|y<t) −λ max
-> Invalid unicode use found on p. 3: ℓ′(next) ←ℓ(next) −λπ
-> Invalid unicode use found on p. 3: log q(y(t)|y(t+1)) = log p(y(t)|y(t+1)) −λ max
-> Invalid unicode use found on p. 5: ˆH = −
-> Invalid unicode use found on p. 6: Denote Yi = −log ˆp(c(s(i))), where c(s(i)) is the cluster containing s(i). The estimator in Equation 10 is then PN
-> Invalid unicode use found on p. 6: i=1 ˜wiYi. Now define Xi = −log p(s(i)), and let X′
-> Invalid unicode use found on p. 6: i = Xi−µX and Y ′
-> Invalid unicode use found on p. 6: i = Yi−µY
-> Invalid unicode use found on p. 6: −α
-> Invalid unicode use found on p. 6: ˜wi,jointYi −αMI
-> Invalid unicode use found on p. 8: numbers are mean±std over 5 jackknife samples of size 200. The symbol “−” indicates that the
-> Invalid unicode use found on p. 15: for t = T−1 downto 0 do
-> Invalid unicode use found on p. 15: ℓ′(next) ←ℓ(next) −λπ
-> Invalid unicode use found on p. 16: pair, (ii) all proper prefixes of the hypothesis (lengths 1 . . . Lh −1) each followed by [TRUNC], and
-> Invalid unicode use found on p. 16: (iii) all proper prefixes of the premise (lengths 1 . . . Lp −1) similarly tagged. A single example with
-> Invalid unicode use found on p. 16: tokenized lengths (Lp, Lh) thus contributes 1 + (Lh −1) + (Lp −1) training instances, covering
-> Invalid unicode use found on p. 17: s∈S E(y≤t, s) −Etarget
-> Invalid unicode use found on p. 17: Var{ ˆH} −Vtarget
-> Invalid unicode use found on p. 17: defined by 1 −E(si, sj) for every pair si, sj of iteratively prompted responses (see Equation 6 for
-> Invalid unicode use found on p. 20: h(Zi) −α
-> Invalid unicode use found on p. 20: g(Zi) −µg
-> Invalid unicode use found on p. 20: is unbiased, because Ep[g(Z) −µg] = 0.
-> Invalid unicode use found on p. 20: g = Var[g(Z)], and σhg = Cov[h(Z), g(Z)]. Writing H = h(Z) −µ and G =
-> Invalid unicode use found on p. 20: g(Z) −µg, we have
-> Invalid unicode use found on p. 20: H −αG
-> Invalid unicode use found on p. 20: h −2α σhg + α2σ2
-> Invalid unicode use found on p. 21: −2σhg + 2ασ2
-> Invalid unicode use found on p. 21: h (1 −ρ2),
-> Invalid unicode use found on p. 21: σhσg is the correlation between h and g, so variance is reduced by the factor 1 −ρ2 such
-> Invalid unicode use found on p. 21: i = Xi −µX with Xi = −log p(s(i))
-> Invalid unicode use found on p. 21: are strongly correlated with the negative cluster probabilities Yi = −log ˆp(c(s(i))), being based on
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Bracket content ['5–10'] on p. 1 could not be matched to a reference.
   -> Sentence:  These models extend masked language modeling by learning iterative denoising schedules to
progressively resolve masked spans [5–10]
-> Warning: Bracket content ['0', ' 1'] on p. 4 could not be matched to a reference.
   -> Sentence:  For MDMs, we randomly select the masking probability uniformly in [0, 1] and 
independently replace tokens with [MASK] with that probability
-> Warning: Bracket content ['19–22'] on p. 7 could not be matched to a reference.
   -> Sentence:  While these methods have also been adapted for text classification and regression in NLP 
[19–22], their extension to free-form NLG presents specific challenges due to semantic invariances 
inherent in generated text [1, 23]
-> Warning: Bracket content ['24–31'] on p. 7 could not be matched to a reference.
   -> Sentence:  Several studies have proposed prompting or fine-tuning language models to explicitly 
articulate their confidence levels [24–31], though this typically requires additional supervision
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 420 sentences on 11 pages -> Avg. of 43.0 sentences per page
-> Warning: Reference '5' never used in the document's text.
-> Warning: Reference '6' never used in the document's text.
-> Warning: Reference '7' never used in the document's text.
-> Warning: Reference '8' never used in the document's text.
-> Warning: Reference '9' never used in the document's text.
-> Warning: Reference '18' never used in the document's text.
-> Warning: Reference '19' never used in the document's text.
-> Warning: Reference '20' never used in the document's text.
-> Warning: Reference '21' never used in the document's text.
-> Warning: Reference '22' never used in the document's text.
-> Warning: Reference '23' never used in the document's text.
-> Warning: Reference '24' never used in the document's text.
-> Warning: Reference '25' never used in the document's text.
-> Warning: Reference '26' never used in the document's text.
-> Warning: Reference '27' never used in the document's text.
-> Warning: Reference '28' never used in the document's text.
-> Warning: Reference '29' never used in the document's text.
-> Warning: Reference '30' never used in the document's text.
-> Warning: Reference '31' never used in the document's text.
-> Warning: Reference '33' never used in the document's text.
-> Warning: Reference '36' never used in the document's text.
-> Warning: Reference '38' never used in the document's text.
-> Warning: Reference '42' never used in the document's text.
-> Warning: Reference '43' never used in the document's text.
-> Warning: Reference '47' never used in the document's text.
-> Warning: Reference '49' never used in the document's text.
-> Warning: Reference '51' never used in the document's text.
-> Warning: Reference '52' never used in the document's text.
-> Warning: Reference '53' never used in the document's text.
-> Warning: Reference '54' never used in the document's text.
-> Warning: Reference '65' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> WARNING: Reference with index 17 (Ref. ID = 18) has no associated sentence!
-> WARNING: Reference with index 18 (Ref. ID = 19) has no associated sentence!
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> WARNING: Reference with index 25 (Ref. ID = 26) has no associated sentence!
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> WARNING: Reference with index 28 (Ref. ID = 29) has no associated sentence!
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
-> WARNING: Reference with index 32 (Ref. ID = 33) has no associated sentence!
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
-> WARNING: Reference with index 46 (Ref. ID = 47) has no associated sentence!
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> WARNING: Reference with index 51 (Ref. ID = 52) has no associated sentence!
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
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
  -> Found 25 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 17
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 18
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 19
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 20
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━╸━━━━━━━━━━━━━━━━━━━━  49% 0:00:01
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 21
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━╸━━━━━━━━━━━━━━━━━━━━  49% 0:00:01
###############################
# Starting Author Check
###############################
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\4 Efficient Semantic Uncertainty Quantification\PAU_results.md  
```