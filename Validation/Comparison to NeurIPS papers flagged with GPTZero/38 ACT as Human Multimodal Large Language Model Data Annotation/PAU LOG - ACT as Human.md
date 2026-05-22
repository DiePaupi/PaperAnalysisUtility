
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\38 ACT as Human Multimodal Large Language Model Data Annotation\ACT as Human Multimodal Large Language Model Data Annotation with Cri.pdf"
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
- Found following heading '2 - ACT Data Pipeline: Formulation & Key Evaluation Metrics' on page 2
- Found following heading '3 - Experimental Details' on page 4
- Found following heading '4 - What Makes ACT Work Better?' on page 4
- Found following heading '5 - ACT as Human: Enhance Downstream Performance with Modified Loss' on page 8
- Found following heading '6 - Related Works' on page 9
- Found following heading '7 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Supplementary Experimental Details' on page 17
- Found following appendix 'B - Stability Analyses' on page 18
- Found following appendix 'C - Examples of Prompt Strategies' on page 19
- Found following appendix 'D - Theoretical Proofs' on page 22
- Found following appendix 'E - (1 −πi)' on page 23
- Found following appendix 'F - Sensitivity Analyses of Human Budget' on page 25
- Found following appendix 'G - Extended Discussions and Experiments' on page 27
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 17
All found references: 67
-> Warning: Malformed author string: 'OpenAI'
-> Warning: Malformed author string: 'Anthropic'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors                                 normalized_authors  contains_et_al  ... abstract                                             outlet link valid
0       1  Alexander J Ratner, Christopher M De Sa, Sen W...        [Ratner A., Sa C., Wu S., Selsam D., Ré C.]           False  ...     None  Advances in Neural Information Processing Systems       None
1       2          Jiangfan Han, Ping Luo, and Xiaogang Wang                          [Han J., Luo P., Wang X.]           False  ...     None  Proceedings of the IEEE/CVF international conf...       None
2       3  Junnan Li, Yongkang Wong, Qi Zhao, and Mohan S...          [Li J., Wong Y., Zhao Q., Kankanhalli M.]           False  ...     None  Proceedings of the IEEE/CVF conference on comp...       None
3       4  Hwanjun Song, Minseok Kim, Dongmin Park, Yooju...        [Song H., Kim M., Park D., Shin Y., Lee J.]           False  ...     None  IEEE transactions on neural networks and learn...       None
4       5  Curtis G Northcutt, Anish Athalye, and Jonas M...             [Northcutt C., Athalye A., Mueller J.]           False  ...     None  Advances in Neural Information Processing Systems       None
..    ...                                                ...                                                ...             ...  ...      ...                                                ...  ...   ...
62     63  Yifan Wang, David Stevens, Pranay Shah, Wenwen...  [Wang Y., Stevens D., Shah P., Jiang W., Liu M...           False  ...     None                                                          None
63     64                 Corinna Cortes and Vladimir Vapnik                             [Cortes C., Vapnik V.]           False  ...     None                                   Machine Learning       None
64     65                                        Leo Breiman                                       [Breiman L.]           False  ...     None                                   Machine Learning       None
65     66  Jacob Devlin, Ming-Wei Chang, Kenton Lee, and ...        [Devlin J., Chang M., Lee K., Toutanova K.]           False  ...     None                                              arXiv       None
66     67  Alicja R ˛aczkowska, Aleksandra Osowska-Kurcza...  [˛aczkowska A., Osowska-Kurczab A., Szczerbi´n...           False  ...     None                                              arXiv       None

[67 rows x 10 columns]
- Checking reference 1/67:
  -> INFO: Now checking 10 results for matching title: 'Data programming: Creating large training sets, quickly'
       -> INFO: All authors matched!
- Checking reference 2/67:
  -> INFO: Now checking 10 results for matching title: 'Deep self-learning from noisy labels'
       -> INFO: All authors matched!
- Checking reference 3/67:
  -> INFO: Now checking 10 results for matching title: 'Learning to learn from noisy labeled data'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/67:
  -> INFO: Now checking 10 results for matching title: 'Learning from noisy labels with deep neural networks: A survey'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 5/67:
  -> INFO: Now checking 3 results for matching title: 'Pervasive label errors in test sets destabilize machine learning benchmarks'
       -> INFO: All authors matched!
- Checking reference 6/67:
  -> INFO: Now checking 1 results for matching title: 'Large language models for data annotation and synthesis: A survey'
       -> INFO: All authors matched!
- Checking reference 7/67:
  -> INFO: Now checking 10 results for matching title: 'Llmaaa: Making large language models as active annotators'
       -> INFO: All authors matched!
- Checking reference 8/67:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Is a large language model a good annotator for event extraction? In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages 17772–17780.
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 6 results for matching title: 'Is a large language model a good annotator for event extraction? In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages 17772–17780.'
  -> WARNING: None of the 6 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Is+a+large+language+model+a+good+annotator+for+event+extraction?+In+Proceedings+of+the+AAAI+Conference+on+Artificial+Intelligence%2C+volume+38%2C+pages+17772–17780. manually and check the results.
        -> Author(s): Ruirui Chen, Chengwei Qin, Weifeng Jiang, and Dongkyu Choi
        -> Title:     Is a large language model a good annotator for event extraction? In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages 17772–17780.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 9/67:
  -> INFO: Now checking 1 results for matching title: 'Zero-shot topic classification of column headers: Leveraging llms for metadata enrichment'
       -> INFO: All authors matched!
- Checking reference 10/67:
  -> INFO: Now checking 4 results for matching title: 'From human annotation to llms: Silicon annotation workflow for management research'
  -> WARNING: None of the 4 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'From human annotation to llms: Silicon annotation workflow for management research'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=From+human+annotation+to+llms:+Silicon+annotation+workflow+for+management+research manually and check the results.
        -> Author(s): Xiang Cheng, Raveesh Mayya, and João Sedoc
        -> Title:     From human annotation to llms: Silicon annotation workflow for management research
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 11/67:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Are large language models good annotators? In NeurIPS 2023 Workshop: I Can’t Believe It’s Not Better: Failure Modes in the Age of Foundation Models.
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 1 results for matching title: 'Are large language models good annotators? In NeurIPS 2023 Workshop: I Can’t Believe It’s Not Better: Failure Modes in the Age of Foundation Models.'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Are+large+language+models+good+annotators?+In+NeurIPS+2023+Workshop:+I+Can’t+Believe+It’s+Not+Better:+Failure+Modes+in+the+Age+of+Foundation+Models. manually and check the results.
        -> Author(s): Jay Mohta, Kenan E Ak, Yan Xu, and Mingwei Shen
        -> Title:     Are large language models good annotators? In NeurIPS 2023 Workshop: I Can’t Believe It’s Not Better: Failure Modes in the Age of Foundation Models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 12/67:
  -> INFO: Now checking 1 results for matching title: 'Knowledge distillation in automated annotation: Supervised text classification with llm-generated training labels'
       -> INFO: All authors matched!
- Checking reference 13/67:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Are expert-level language models expert-level annotators? In NeurIPS 2024 Workshop, Proceedings of Machine Learning Research.
  -> WARNING: No results were found through the dblp search!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tseng', 'Chen', 'Chen', 'Chen', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Are+expert-level+language+models+expert-level+annotators?+In+NeurIPS+2024+Workshop%2C+Proceedings+of+Machine+Learning+Research. manually and check the results.
        -> Author(s): Yu-Min Tseng, Wei-Lin Chen, Chung-Chi Chen, and Hsin-Hsi Chen
        -> Title:     Are expert-level language models expert-level annotators? In NeurIPS 2024 Workshop, Proceedings of Machine Learning Research.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 14/67:
  -> INFO: Now checking 1 results for matching title: 'Coannotating: Uncertainty-guided work allocation between human and large language models for data annotation'
       -> INFO: All authors matched!
- Checking reference 15/67:
  -> INFO: Now checking 10 results for matching title: 'Meganno+: A human-llm collaborative annotation system'
       -> INFO: All authors matched!
- Checking reference 16/67:
  -> INFO: Now checking 8 results for matching title: 'Human-llm collaborative annotation through effective verification of llm labels'
       -> INFO: All authors matched!
- Checking reference 17/67:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Can unconfident llm annotations be used for confident conclusions? Nations of the Americas Chapter of the Association for Computational Linguistics.
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gligori´c', 'Zrnic', 'Lee', 'Candès', 'Jurafsky', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Can+unconfident+llm+annotations+be+used+for+confident+conclusions?+Nations+of+the+Americas+Chapter+of+the+Association+for+Computational+Linguistics. manually and check the results.
        -> Author(s): Kristina Gligori´c, Tijana Zrnic, Cinoo Lee, Emmanuel J Candès, and Dan Jurafsky
        -> Title:     Can unconfident llm annotations be used for confident conclusions? Nations of the Americas Chapter of the Association for Computational Linguistics.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 18/67:
  -> INFO: Now checking 1 results for matching title: 'Which examples to annotate for in-context learning? towards effective and efficient selection'
       -> INFO: All authors matched!
- Checking reference 19/67:
  -> INFO: Now checking 1 results for matching title: 'Model-in-the-loop (milo): Accelerating multimodal ai data annotation with llms'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 20/67:
  -> INFO: Now checking 10 results for matching title: 'Active statistical inference'
       -> INFO: All authors matched!
- Checking reference 21/67:
  -> INFO: Now checking 10 results for matching title: 'Large language models can self-improve'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 22/67:
  -> INFO: Now checking 1 results for matching title: 'When can llms actually correct their own mistakes? a critical survey of self-correction of llms'
       -> INFO: All authors matched!
- Checking reference 23/67:
  -> INFO: Now checking 10 results for matching title: 'A survey on llm-as-a-judge'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 24/67:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Mind the gap: Examining the self-improvement capabilities of large language models
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Song', 'Zhang', 'Eisenach', 'Kakade', 'Foster', 'Ghai', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Mind+the+gap:+Examining+the+self-improvement+capabilities+of+large+language+models manually and check the results.
        -> Author(s): Yuda Song, Hanlin Zhang, Carson Eisenach, Sham M Kakade, Dean Foster, and Udaya Ghai
        -> Title:     Mind the gap: Examining the self-improvement capabilities of large language models
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 25/67:
  -> INFO: Now checking 10 results for matching title: 'Learning multiple layers of features from tiny images'
       -> INFO: All authors matched!
- Checking reference 26/67:
  -> INFO: Now checking 10 results for matching title: 'Fashion-mnist: a novel image dataset for benchmarking machine learning algorithms'
       -> INFO: All authors matched!
- Checking reference 27/67:
  -> INFO: Now checking 10 results for matching title: '3d object representations for finegrained categorization'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Krause', 'Stark', 'Deng', 'Fei-Fei', '2013']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=3d+object+representations+for+finegrained+categorization manually and check the results.
        -> Author(s): Jonathan Krause, Michael Stark, Jia Deng, and Li Fei-Fei
        -> Title:     3d object representations for finegrained categorization
        -> Year:      2013
     -> Manual search was skipped by the user.
- Checking reference 28/67:
  -> INFO: Now checking 1 results for matching title: 'Tweeteval: Unified benchmark and comparative evaluation for tweet classification'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Espinosa-Anke'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/67:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: A dataset and exploration of models for understanding radiology images through dialogue
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lau', 'Gayen', 'Tschandl', 'Burns', 'Yuan', 'SyedaMahmood', 'Moradi', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+dataset+and+exploration+of+models+for+understanding+radiology+images+through+dialogue manually and check the results.
        -> Author(s): Jack Lau, Ankan Gayen, Philipp Tschandl, Gregory A Burns, Jiahong Yuan, Tanveer SyedaMahmood, and Mehdi Moradi
        -> Title:     A dataset and exploration of models for understanding radiology images through dialogue
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 30/67:
  -> Checking if provided link is pingable: https://openai.com/index/gpt-4o
  -> INFO: Now checking 10 results for matching title: 'Gpt-4o technical report.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['OpenAI', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://openai.com/index/gpt-4o manually and check the results.
        -> Author(s): OpenAI
        -> Title:     Gpt-4o technical report.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 31/67:
  -> Checking if provided link is pingable: https://deepmind.google/technologies/gemini/gemini-1-5/
  -> INFO: Now checking 10 results for matching title: 'Gemini 1.5 technical report.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['DeepMind', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gemini+1.5+technical+report. manually and check the results.
        -> Author(s): Google DeepMind
        -> Title:     Gemini 1.5 technical report.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 32/67:
  -> Checking if provided link is pingable: https://www.anthropic.com/index/claude-3
  -> INFO: Now checking 10 results for matching title: 'Claude 3.5 sonnet overview.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Anthropic', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://www.anthropic.com/index/claude-3 manually and check the results.
        -> Author(s): Anthropic
        -> Title:     Claude 3.5 sonnet overview.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 33/67:
  -> Checking if provided link is pingable: https://llava-vl.github.io/
  -> INFO: Now checking 1 results for matching title: 'Llava-one-for-all: Unified visual instruction model across different image types and tasks.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', 'Xu', 'Zhang', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://llava-vl.github.io/ manually and check the results.
        -> Author(s): Haotian Liu, Chunyuan Xu, Zhengyuan Zhang, et al
        -> Title:     Llava-one-for-all: Unified visual instruction model across different image types and tasks.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 34/67:
  -> Checking if provided link is pingable: https://huggingface.co/Qwen/Qwen-VL
  -> INFO: Now checking 3 results for matching title: 'Qwen-vl: A multimodal large language model for understanding images, texts, and more.'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://huggingface.co/Qwen/Qwen-VL manually and check the results.
        -> Author(s): Alibaba Group Qwen Team
        -> Title:     Qwen-vl: A multimodal large language model for understanding images, texts, and more.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 35/67:
  -> Checking if provided link is pingable: https://github.com/OpenGVLab/InternVL
  -> INFO: Now checking 10 results for matching title: 'Internvl 2.5 technical overview.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Laboratory', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://github.com/OpenGVLab/InternVL manually and check the results.
        -> Author(s): Shanghai AI Laboratory
        -> Title:     Internvl 2.5 technical overview.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 36/67:
  -> INFO: Now checking 10 results for matching title: 'Deep residual learning for image recognition'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 37/67:
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
- Checking reference 38/67:
  -> INFO: Now checking 10 results for matching title: 'Roberta: A robustly optimized bert pretraining approach'
       -> INFO: All authors matched!
- Checking reference 39/67:
  -> INFO: Now checking 2 results for matching title: 'Blip: Bootstrapping languageimage pre-training for unified vision-language understanding and generation'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Li', 'Li', 'Xiong', 'Hoi', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Blip:+Bootstrapping+languageimage+pre-training+for+unified+vision-language+understanding+and+generation manually and check the results.
        -> Author(s): Junnan Li, Dongxu Li, Caiming Xiong, and Steven CH Hoi
        -> Title:     Blip: Bootstrapping languageimage pre-training for unified vision-language understanding and generation
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 40/67:
  -> INFO: Now checking 10 results for matching title: 'Chain-of-thought prompting elicits reasoning in large language models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wei', 'Wang', 'Schuurmans', 'Bosma', 'Xia', 'Chi', 'Le', 'Zhou', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Chain-of-thought+prompting+elicits+reasoning+in+large+language+models manually and check the results.
        -> Author(s): Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al
        -> Title:     Chain-of-thought prompting elicits reasoning in large language models
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 41/67:
  -> INFO: Now checking 1 results for matching title: 'The devil is in the errors: Leveraging large language models for fine-grained machine translation evaluation'
       -> INFO: All authors matched!
- Checking reference 42/67:
  -> INFO: Now checking 10 results for matching title: 'Self-rewarding language models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yuan', 'Pang', 'Cho', 'Sukhbaatar', 'Xu', 'Weston', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Self-rewarding+language+models. manually and check the results.
        -> Author(s): Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Sainbayar Sukhbaatar, Jing Xu, and Jason Weston
        -> Title:     Self-rewarding language models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 43/67:
  -> INFO: Now checking 1 results for matching title: 'I-sheep: Self-alignment of llm from scratch through an iterative self-enhancement paradigm'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Huang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 44/67:
  -> INFO: Now checking 10 results for matching title: 'Deductive verification of chain-of-thought reasoning'
       -> INFO: All authors matched!
- Checking reference 45/67:
  -> INFO: Now checking 1 results for matching title: 'Can llms learn from previous mistakes? investigating llms’ errors to boost for reasoning'
       -> INFO: All authors matched!
- Checking reference 46/67:
  -> INFO: Now checking 6 results for matching title: 'Slichf: Sequence likelihood calibration with human feedback'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhao', 'Joshi', 'Liu', 'Khalman', 'Saleh', 'Liu', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Slichf:+Sequence+likelihood+calibration+with+human+feedback manually and check the results.
        -> Author(s): Yao Zhao, Rishabh Joshi, Tianqi Liu, Misha Khalman, Mohammad Saleh, and Peter J Liu
        -> Title:     Slichf: Sequence likelihood calibration with human feedback
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 47/67:
  -> INFO: Now checking 10 results for matching title: 'Statistical rejection sampling improves preference optimization'
       -> INFO: All authors matched!
- Checking reference 48/67:
  -> INFO: Now checking 10 results for matching title: 'Rlhf workflow: From reward modeling to online rlhf'
       -> INFO: All authors matched!
- Checking reference 49/67:
  -> INFO: Now checking 10 results for matching title: 'Xgboost: A scalable tree boosting system'
       -> INFO: All authors matched!
- Checking reference 50/67:
  -> INFO: Now checking 10 results for matching title: 'Llms-as-judges: A comprehensive survey on llm-based evaluation methods.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Li', 'Dong', 'Chen', 'Su', 'Zhou', 'Ai', 'Ye', 'Liu', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Llms-as-judges:+A+comprehensive+survey+on+llm-based+evaluation+methods. manually and check the results.
        -> Author(s): Haitao Li, Qian Dong, Junjie Chen, Huixue Su, Yujia Zhou, Qingyao Ai, Ziyi Ye, and Yiqun Liu
        -> Title:     Llms-as-judges: A comprehensive survey on llm-based evaluation methods.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 51/67:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Can large language models be an alternative to human evaluations? The 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP).
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Chiang', 'Lee', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Can+large+language+models+be+an+alternative+to+human+evaluations?+The+2023+Conference+on+Empirical+Methods+in+Natural+Language+Processing+(EMNLP). manually and check the results.
        -> Author(s): Cheng-Han Chiang and Hung-yi Lee
        -> Title:     Can large language models be an alternative to human evaluations? The 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP).
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 52/67:
  -> INFO: Now checking 1 results for matching title: 'Judging llm-as-a-judge with mt-bench and chatbot arena'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Gonzalez, Stoica'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 53/67:
  -> INFO: Now checking 10 results for matching title: 'Beyond human data: Scaling self-training for problem-solving with language models'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 54/67:
  -> INFO: Now checking 10 results for matching title: 'Teaching large language models to self-debug'
       -> INFO: All authors matched!
- Checking reference 55/67:
  -> INFO: Now checking 1 results for matching title: 'Volcano: Mitigating Multimodal Hallucination through Self-Feedback Guided Revision, April.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lee', 'Park', 'Jo', 'Seo', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Volcano:+Mitigating+Multimodal+Hallucination+through+Self-Feedback+Guided+Revision%2C+April. manually and check the results.
        -> Author(s): Seongyun Lee, Sue Hyun Park, Yongrae Jo, and Minjoon Seo
        -> Title:     Volcano: Mitigating Multimodal Hallucination through Self-Feedback Guided Revision, April.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 56/67:
  -> INFO: Now checking 10 results for matching title: 'Self-critiquing models for assisting human evaluators'
       -> INFO: All authors matched!
- Checking reference 57/67:
  -> INFO: Now checking 1 results for matching title: 'Justice or prejudice? quantifying biases in llm-as-a-judge'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Chawla'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 58/67:
  -> INFO: Now checking 1 results for matching title: 'Preference leakage: A contamination problem in llm-as-a-judge'
       -> INFO: All authors matched!
- Checking reference 59/67:
  -> INFO: Now checking 10 results for matching title: 'Sub-sampled cubic regularization for non-convex optimization'
       -> INFO: All authors matched!
- Checking reference 60/67:
  -> INFO: Now checking 10 results for matching title: 'Ppi++: Efficient predictionpowered inference'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Angelopoulos', 'Duchi', 'Zrnic', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Ppi++:+Efficient+predictionpowered+inference manually and check the results.
        -> Author(s): Anastasios N Angelopoulos, John C Duchi, and Tijana Zrnic
        -> Title:     Ppi++: Efficient predictionpowered inference
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 61/67:
  -> INFO: Now checking 1 results for matching title: 'LOOK-M: Look-once optimization in kv cache for efficient multimodal long-context inference'
       -> INFO: All authors matched!
- Checking reference 62/67:
  -> INFO: Now checking 6 results for matching title: 'Longllava: Scaling multi-modal large language models to 1000 images efficiently via hybrid architecture'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Song', 'Chen', 'Zhang', 'Wang', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Longllava:+Scaling+multi-modal+large+language+models+to+1000+images+efficiently+via+hybrid+architecture manually and check the results.
        -> Author(s): Xidong Wang, Dingjie Song, Shunian Chen, Chen Zhang, and Benyou Wang
        -> Title:     Longllava: Scaling multi-modal large language models to 1000 images efficiently via hybrid architecture
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 63/67:
  -> INFO: Now checking 1 results for matching title: 'Model-in-theLoop (MILO): Accelerating Multimodal AI Data Annotation with LLMs, September.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Stevens', 'Shah', 'Jiang', 'Liu', 'Chen', 'Kuo', 'Li', 'Gong', 'Lee', 'Hu', 'Zhang', 'Kamma', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Model-in-theLoop+(MILO):+Accelerating+Multimodal+AI+Data+Annotation+with+LLMs%2C+September. manually and check the results.
        -> Author(s): Yifan Wang, David Stevens, Pranay Shah, Wenwen Jiang, Miao Liu, Xu Chen, Robert Kuo, Na Li, Boying Gong, Daniel Lee, Jiabo Hu, Ning Zhang, and Bob Kamma
        -> Title:     Model-in-theLoop (MILO): Accelerating Multimodal AI Data Annotation with LLMs, September.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 64/67:
  -> INFO: Now checking 10 results for matching title: 'Support-vector networks'
       -> INFO: All authors matched!
- Checking reference 65/67:
  -> INFO: Now checking 10 results for matching title: 'Random forests'
       -> INFO: All authors matched!
- Checking reference 66/67:
  -> INFO: Now checking 10 results for matching title: 'Bert: Pre-training of deep bidirectional transformers for language understanding'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 67/67:
  -> INFO: Now checking 6 results for matching title: 'Allenoise: large-scale text classification benchmark dataset with realworld label noise'
  -> WARNING: None of the 6 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['˛aczkowska', 'Osowska-Kurczab', 'Szczerbi´nski', 'Jasinska-Kobus', 'Nazarko', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Allenoise:+large-scale+text+classification+benchmark+dataset+with+realworld+label+noise manually and check the results.
        -> Author(s): Alicja R ˛aczkowska, Aleksandra Osowska-Kurczab, Jacek Szczerbi´nski, Kalina Jasinska-Kobus, and Klaudia Nazarko
        -> Title:     Allenoise: large-scale text classification benchmark dataset with realworld label noise
        -> Year:      2024
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: can be done via a correction operator: κδ[f (m)](xi) = (1 −δi) f (m)(xi) + δif ∗(xi). Practically,
-> Invalid unicode use found on p. 2: δ [f (m)](xi) = (1 −δi) f (m)(xi) + δif (h)(xi).
-> Invalid unicode use found on p. 2: • Exponential Weighting: πB(ˆϵi) = 1/(1 + e−β(ˆϵi−α)), where α ∈[0, 1] and β ∈R+ are
-> Invalid unicode use found on p. 3: δ(B)[f (m)]) −Q
-> Invalid unicode use found on p. 3: Qmax −Q
-> Invalid unicode use found on p. 3: where the denominator Qmax−Q(f (h), f (m)) scales AQG into range [0, 1], which offsets the influence
-> Invalid unicode use found on p. 7: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 7: ℓθ −ℓ(m)
-> Invalid unicode use found on p. 7: πB(ˆϵ) −1
-> Invalid unicode use found on p. 8: θ,i −∇ℓθ,i∥≤C for all i ∈{1, 2, ..., N}. Then, for an arbitrary p ∈(0, 1), with
-> Invalid unicode use found on p. 8: probability at least 1 −p, we can bound
-> Invalid unicode use found on p. 8: −θ∗∥≤
-> Invalid unicode use found on p. 8: , θ∗= arg minθ Lθ, and c1 = (1 −q)C2/q.
-> Invalid unicode use found on p. 21: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: i ] −(E[Zi])2. We first expand:
-> Invalid unicode use found on p. 21: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: θ,i (ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: πB(ˆϵi) + (ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: θ,i −
-> Invalid unicode use found on p. 21: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: πB(ˆϵi) −1
-> Invalid unicode use found on p. 21: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: πB(ˆϵi) −1
-> Invalid unicode use found on p. 21: −E2[ℓθ,i]
-> Invalid unicode use found on p. 21: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: πB(ˆϵi) −1
-> Invalid unicode use found on p. 21: ℓθ,i −ℓ(m)
-> Invalid unicode use found on p. 21: πB(ˆϵi) −1
-> Invalid unicode use found on p. 21: ℓθ −ℓ(m)
-> Invalid unicode use found on p. 21: πB(ˆϵ) −1
-> Invalid unicode use found on p. 22: (1 −πi)∇ℓ(m)
-> Invalid unicode use found on p. 22: πi∇ℓθ,i −1
-> Invalid unicode use found on p. 22: (1 −πi)∇ℓ(m)
-> Invalid unicode use found on p. 22: (1 −πi)
-> Invalid unicode use found on p. 22: θ,i −∇ℓθ,i
-> Invalid unicode use found on p. 22: (1 −πi)
-> Invalid unicode use found on p. 22: θ,i −∇ℓθ,i
-> Invalid unicode use found on p. 22: θ,i −∇ℓθ,i
-> Invalid unicode use found on p. 22: (1 −πi)
-> Invalid unicode use found on p. 22: θ,i −∇ℓθ,i
 ≤|1 −πi|d unicode use found on p. 22: 
-> Invalid unicode use found on p. 22: θ,i −∇ℓθ,i
-> Invalid unicode use found on p. 22: 1, 1 −q
-> Invalid unicode use found on p. 22: (1 −πi)
-> Invalid unicode use found on p. 22: θ,i −∇ℓθ,i
∇ℓ(m)valid unicode use found on p. 22: (1 −πi)2 
-> Invalid unicode use found on p. 22: θ,i −∇ℓθ,i
-> Invalid unicode use found on p. 22: ≤1 −q
-> Invalid unicode use found on p. 22: (1 −πi)
-> Invalid unicode use found on p. 22: θ,i −∇ℓθ,i
-> Invalid unicode use found on p. 22: −Nϵ2/(8c1)
-> Invalid unicode use found on p. 22: c0 . Then, with a probability of at least 1 −p where p ∈(0, 1), we have
-> Invalid unicode use found on p. 22: (1 −πi)
-> Invalid unicode use found on p. 22: θ,i −∇ℓθ,i
-> Invalid unicode use found on p. 22: θ , with a probability of at least 1 −p, we
-> Invalid unicode use found on p. 22: −θ∗
-> Invalid unicode use found on p. 22: −∇L(ACT )
-> Invalid unicode use found on p. 22: ∇Lθ∗−∇L(ACT )
-> Invalid unicode use found on p. 22: (1 −πi)
-> Invalid unicode use found on p. 22: θ∗,i −∇ℓθ∗,i
-> Invalid unicode use found on p. 23: ℓθ,i −λℓ(m)
-> Invalid unicode use found on p. 23: ℓθ,i −λℓ(m)
-> Invalid unicode use found on p. 23: 1 + e−β(ˆϵi−α)
-> Invalid unicode use found on p. 23: ℓθ,i −λℓ(m)
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Numeric reference range couldn't be parsed as Integers: ['Vanilla - Generally good and without model selection']
-> Warning: Numeric reference range couldn't be parsed as Integers: ['Pro - Optimize annotation efficiency via model selection']
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 642 sentences on 11 pages -> Avg. of 65.2 sentences per page
-> Warning: Reference '59' never used in the document's text.
-> Warning: Reference '60' never used in the document's text.
-> Warning: Reference '61' never used in the document's text.
-> Warning: Reference '62' never used in the document's text.
-> Warning: Reference '63' never used in the document's text.
-> Warning: Reference '64' never used in the document's text.
-> Warning: Reference '65' never used in the document's text.
-> Warning: Reference '66' never used in the document's text.
-> Warning: Reference '67' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
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
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
-> Missing an abstract for reference with index 40 (Ref. ID = 41); Skipping LLM check...
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 57 (Ref. ID = 58); Skipping LLM check...
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
-> Missing an abstract for reference with index 61 (Ref. ID = 62); Skipping LLM check...
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
-> WARNING: Reference with index 65 (Ref. ID = 66) has no associated sentence!
-> Missing an abstract for reference with index 66 (Ref. ID = 67); Skipping LLM check...
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
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
  -> Found 4 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 22 matches in this ranking!
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
Resorting to unclean kill browser.
-> Saved chapter_fig on try 1
-> Saved lit_fig on try 1
-> Saved rank_fig on try 1
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\38 ACT as Human Multimodal Large Language Model Data Annotation\PAU_results.md
```