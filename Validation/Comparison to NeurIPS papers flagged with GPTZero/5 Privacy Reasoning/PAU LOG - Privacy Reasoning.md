
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\5 Privacy Reasoning\Privacy Reasoning Partnergate Version.pdf"
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
- Found following heading '2 - Background and Related Work' on page 2
- Found following heading '3 - Problem Statement' on page 3
- Found following heading '4 - Context Ambiguity Analysis' on page 4
- Found following heading '5 - Camber: A Context Disambiguation Framework' on page 5
- Found following heading '6 - Results' on page 8
- Found following heading '7 - Discussion and Limitations' on page 9
- Found following heading '8 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Motivating examples from PrivacyLens+' on page 20
- Found following appendix 'B - Detailed Results' on page 21
- Found following appendix 'C - Detailed description of the Camber disambiguation framework' on page 29
- Found following appendix 'D - Datasets and dataset expansions' on page 31
- Found following appendix 'E - Evaluation' on page 52
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 20
All found references: 34
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                               link  valid
0       1                                   Helen Nissenbaum  ...                                                      None
1       2                                   Helen Nissenbaum  ...                                                      None
2       3  Niloofar Mireshghallah, Hyunwoo Kim, Xuhui Zho...  ...  https://github.com/skywalker023/confAIde/tree/...   None
3       4  Yijia Shao, Tianshi Li, Weiyan Shi, Yanchen Li...  ...           https://github.com/SALT-NLP/PrivacyLens.   None
4       5  Lichao Sun, Yue Huang, Haoran Wang, Siyuan Wu,...  ...                                                      None
5       6              Yan Shvartzshnaider and Vasisht Duddu  ...                                                      None
6       7  Hyunwoo Kim, Melanie Sclar, Zhili Feng Li, Maa...  ...                                                      None
7       8  Melanie Sclar, Sachin Kumar, Peter West, Alane...  ...                                                      None
8       9  Mor Geva, Daniel Khashabi, Elad Segal, Tushar ...  ...                                                      None
9      10  Zayne Sprague, Xi Ye, Kyle Richardson, and Gre...  ...                                                      None
10     11  Bill Yuchen Lin, Ronan Le Bras, Kyle Richardso...  ...                                                      None
11     12  Alon Jacovi, Yonatan Bitton, Bernd Bohnet, Jon...  ...                                                      None
12     13                Belinda Z Li, Been Kim, and Zi Wang  ...                                                      None
13     14  Nicholas Carlini, Florian Tramer, Eric Wallace...  ...                                                      None
14     15  Robin Staab, Mark Vero, Mislav Balunovi´c, and...  ...                                                      None
15     16  Martin Abadi, Andy Chu, Ian Goodfellow, H Bren...  ...                                                      None
16     17  Xuechen Li, Florian Tramer, Percy Liang, and T...  ...                                                      None
17     18  Da Yu, Saurabh Naik, Arturs Backurs, Sivakanth...  ...                                                      None
18     19  Patrick Lewis, Ethan Perez, Aleksandra Piktus,...  ...                                                      None
19     20  Eugene Bagdasarian, Ren Yi, Sahra Ghalebikesab...  ...                                                      None
20     21  Ivoline Ngong, Swanand Kadhe, Hao Wang, Keerth...  ...                                                      None
21     22  Arman Zharmagambetov, Chuan Guo, Ivan Evtimov,...  ...                                                      None
22     23  Yue Huang, Chujie Gao, Siyuan Wu, Haoran Wang,...  ...                                                      None
23     24  Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin X...  ...                                                      None
24     25  Yichi Zhang, Yao Huang, Yitong Sun, Chang Liu,...  ...                                                      None
25     26  Haoran Li, Wei Fan, Yulin Chen, Jiayang Cheng,...  ...                                                      None
26     27  Haoran Li, Wei Fan, Yulin Chen, Jiayang Cheng,...  ...                                                      None
27     28  Yan Shvartzshnaider, Vasisht Duddu, and John L...  ...                                                      None
28     29  Sahra Ghalebikesabi, Eugene Bagdasaryan, Ren Y...  ...                                                      None
29     30  Haoran Li, Wei Fan, Yulin Chen, Jiayang Cheng,...  ...                                                      None
30     31  Zhao Cheng, Diane Wan, Matthew Abueg, Sahra Gh...  ...                                                      None
31     32  Guangchen Lan, Huseyin A Inan, Sahar Abdelnabi...  ...                                                      None
32     33  Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jo...  ...                                                      None
33     34  M  Ariel Cascio, Eunlye Lee, Nicole Vaudrin, a...  ...  https://github.com/google-parfait/contextual-p...   None

[34 rows x 10 columns]
- Checking reference 1/34:
  -> INFO: Now checking 10 results for matching title: 'Privacy as contextual integrity'
       -> INFO: All authors matched!
- Checking reference 2/34:
  -> INFO: Now checking 9 results for matching title: 'Privacy in context: Technology, policy, and the integrity of social life'
       -> INFO: All authors matched!
- Checking reference 3/34:
  -> Checking if provided link is pingable: https://github.com/skywalker023/confAIde/tree/main/benchmark.
  -> INFO: Now checking 1 results for matching title: 'Can LLMs keep a secret? testing privacy implications of language models via contextual integrity theory'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/34:
  -> Checking if provided link is pingable: https://github.com/SALT-NLP/PrivacyLens.
  -> INFO: Now checking 1 results for matching title: 'PrivacyLens: Evaluating privacy norm awareness of language models in action'
       -> INFO: All authors matched!
- Checking reference 5/34:
  -> INFO: Now checking 10 results for matching title: 'Trustllm: Trustworthiness in large language models'
       -> WARNING: Not all 66 authors from the found ref. were matched (only 30)
                   Unmatched authors = 'Liu, Liu, Kailkhura, Xiong, Xiao, Xing, Liu, Yao, Kellis, Zitnik, Jiang, Bansal, Zou, Pei, Liu, Zhao, Tang, Mitchell, Shu, Chang, He, Backes, Gong, Chen, Gu, Ying, Jana, Chen, Liu, Zhou, Xie, Chen, Liu, Ye, Cao, Zhao'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 6/34:
  -> INFO: Now checking 10 results for matching title: 'Position: Contextual integrity washing for language models'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Position: Contextual integrity washing for language models'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Position:+Contextual+integrity+washing+for+language+models manually and check the results.
        -> Author(s): Yan Shvartzshnaider and Vasisht Duddu
        -> Title:     Position: Contextual integrity washing for language models
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 7/34:
  -> INFO: Now checking 2 results for matching title: 'FANToM: A benchmark for stress-testing machine theory of mind in interactions'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 5)
                   Unmatched authors = 'Zhou, Bras'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/34:
  -> INFO: Now checking 1 results for matching title: 'Minding language models’ (lack of) theory of mind: A plug-and-play multi-character belief tracker'
       -> INFO: All authors matched!
- Checking reference 9/34:
  -> INFO: Now checking 1 results for matching title: 'Did aristotle use a laptop? a question answering benchmark with implicit reasoning strategies'
       -> INFO: All authors matched!
- Checking reference 10/34:
  -> INFO: Now checking 2 results for matching title: 'MuSR: Testing the limits of chain-of-thought with multistep soft reasoning'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Bostrom, Chaudhuri'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Bostrom, Chaudhuri'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/34:
  -> INFO: Now checking 1 results for matching title: 'Zebralogic: On the scaling limits of llms for logical reasoning'
       -> INFO: All authors matched!
- Checking reference 12/34:
  -> INFO: Now checking 1 results for matching title: 'A chain-of-thought is as strong as its weakest link: A benchmark for verifiers of reasoning chains'
       -> INFO: All authors matched!
- Checking reference 13/34:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: QuestBench: Can llm ask the right question to acquire information in reasoning tasks? arXiv preprint arXiv:2503
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 234 results for matching title: 'QuestBench: Can llm ask the right question to acquire information in reasoning tasks? arXiv preprint arXiv:2503'
  -> WARNING: None of the 234 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=QuestBench:+Can+llm+ask+the+right+question+to+acquire+information+in+reasoning+tasks?+arXiv+preprint+arXiv:2503 manually and check the results.
        -> Author(s): Belinda Z Li, Been Kim, and Zi Wang
        -> Title:     QuestBench: Can llm ask the right question to acquire information in reasoning tasks? arXiv preprint arXiv:2503
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 14/34:
  -> INFO: Now checking 10 results for matching title: 'Extracting training data from large language models'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 9)
                   Unmatched authors = 'Tramèr, Oprea, Raffel'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 15/34:
  -> INFO: Now checking 2 results for matching title: 'Beyond memorization: Violating privacy via inference with large language models'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Balunovi'c'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/34:
  -> INFO: Now checking 10 results for matching title: 'Deep learning with differential privacy'
       -> INFO: All authors matched!
- Checking reference 17/34:
  -> INFO: Now checking 10 results for matching title: 'Large language models can be strong differentially private learners'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Tramèr'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/34:
  -> INFO: Now checking 10 results for matching title: 'Differentially private fine-tuning of language models'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 19/34:
  -> INFO: Now checking 10 results for matching title: 'Retrieval-augmented generation for knowledgeintensive NLP tasks'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Retrieval-augmented generation for knowledgeintensive NLP tasks'
  -> WARNING: None of the 2 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Retrieval-augmented+generation+for+knowledgeintensive+NLP+tasks manually and check the results.
        -> Author(s): Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al
        -> Title:     Retrieval-augmented generation for knowledgeintensive NLP tasks
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 20/34:
  -> INFO: Now checking 10 results for matching title: 'Airgapagent: Protecting privacy-conscious conversational agents'
       -> INFO: All authors matched!
- Checking reference 21/34:
  -> INFO: Now checking 1 results for matching title: 'Protecting users from themselves: Safeguarding contextual privacy in interactions with conversational agents'
       -> INFO: All authors matched!
- Checking reference 22/34:
  -> INFO: Now checking 3 results for matching title: 'AgentDAM: Privacy leakage evaluation for autonomous web agents'
       -> INFO: All authors matched!
- Checking reference 23/34:
  -> INFO: Now checking 1 results for matching title: 'On the trustworthiness of generative foundation models: Guideline, assessment, and perspective'
       -> WARNING: Not all 65 authors from the found ref. were matched (only 24)
                   Unmatched authors = 'Li, Bao, Liu, Guan, Chen, Chen, Guo, Zou, Kuen-Yew, Xiong, Stengel-Eskin, Yin, Yao, Yoon, Shu, Zhu, Krishna, Swayamdipta, Li, Li, Li, Chen, Tu, Zhao, Sun, Sasson, Sattigeri, Reuel, Lamparth, Zhao, Dziri, Su, Sun, Xiao, Bansal, Chawla, Pei, Backes, Gong, Chen, Li'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 24/34:
  -> INFO: Now checking 2 results for matching title: 'Decodingtrust: A comprehensive assessment of trustworthiness in gpt models'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 12)
                   Unmatched authors = 'Truong, Arora, Mazeika, Hendrycks, Cheng, Koyejo, Song'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 12)
                   Unmatched authors = 'Arora, Cheng, Hendrycks, Koyejo, Mazeika, Song, Truong'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 25/34:
  -> INFO: Now checking 10 results for matching title: 'Multitrust: A comprehensive benchmark towards trustworthy multimodal large language models'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Dong, Zhu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/34:
  -> INFO: Now checking 1 results for matching title: 'GOLDCOIN: Grounding large language models in privacy laws via contextual integrity theory'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Deng, Wang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 27/34:
  -> INFO: Now checking 1 results for matching title: 'Privacy Checklist: Privacy violation detection grounding on contextual integrity theory'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 28/34:
  -> INFO: Now checking 5 results for matching title: 'LLM-CI: Assessing contextual integrity norms in language models'
  -> WARNING: None of the 5 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'LLM-CI: Assessing contextual integrity norms in language models'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=LLM-CI:+Assessing+contextual+integrity+norms+in+language+models manually and check the results.
        -> Author(s): Yan Shvartzshnaider, Vasisht Duddu, and John Lacalamita
        -> Title:     LLM-CI: Assessing contextual integrity norms in language models
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 29/34:
  -> INFO: Now checking 3 results for matching title: 'Operationalizing contextual integrity in privacy-conscious assistants'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/34:
  -> INFO: Now checking 1 results for matching title: 'PrivaCI-Bench: Evaluating privacy with contextual integrity and legal compliance'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Jing'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/34:
  -> INFO: Now checking 1 results for matching title: 'Ci-bench: Benchmarking contextual integrity of ai assistants on synthetic data'
       -> INFO: All authors matched!
- Checking reference 32/34:
  -> INFO: Now checking 3 results for matching title: 'Contextual integrity in llms via reasoning and reinforcement learning'
       -> INFO: All authors matched!
- Checking reference 33/34:
  -> INFO: Now checking 10 results for matching title: 'Reasoning models don’t always say what they think'
       -> WARNING: Not all 15 authors from the found ref. were matched (only 14)
                   Unmatched authors = 'Perez'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/34:
  -> Checking if provided link is pingable: https://github.com/google-parfait/contextual-privacy-and-security.Guidelines:•
  -> INFO: Now checking 1 results for matching title: 'A team-based approach to open coding: Considerations for creating intercoder consensus'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 3: (denoted as S−) to measure privacy leakage, we augment them by incorporating instances where
-> Invalid unicode use found on p. 3: For each S−, we generate a corresponding positive scenario S+ by modifying a subset of its fields.
-> Invalid unicode use found on p. 3: S−, and contain 986 and 540 examples respectively. A detailed description of the dataset generation
-> Invalid unicode use found on p. 5: −to [Data
-> Invalid unicode use found on p. 5: −based
-> Invalid unicode use found on p. 5: example’s appropriateness label. Specifically, we generate inappropriate contexts (denoted N −) for
-> Invalid unicode use found on p. 5: S−examples to reinforce their inappropriateness and appropriate contexts (denoted N +) for S+
-> Invalid unicode use found on p. 5: context. In total, this procedure generates an additional 5 × 493 = 2,465 pairs of S−
-> Invalid unicode use found on p. 5: procedure, including prompts and the generated S−
-> Invalid unicode use found on p. 5: NI and S−
-> Invalid unicode use found on p. 5: adds contextual details to S−and S+ examples according to the definition of the fields in each
-> Invalid unicode use found on p. 5: dataset. These label-dependent contexts are either inappropriate or appropriate, denoted as N −
-> Invalid unicode use found on p. 6: D respectively. Incorporating these contexts yields examples denoted as S−
-> Invalid unicode use found on p. 6: N −
-> Invalid unicode use found on p. 6: both datasets, we first ask the LLM to generate N −
-> Invalid unicode use found on p. 6: D ) for a specific field in S−
-> Invalid unicode use found on p. 6: dataset, resulting in an additional 2,465 pairs of S−
-> Invalid unicode use found on p. 6: N −
-> Invalid unicode use found on p. 7: To test if codes are more effective at reducing implicit reasoning assumptions, we prompt the LLM to generate label-dependent contexts based on each code (denoted as N −
-> Invalid unicode use found on p. 7: C ) for all S−and S+ examples respectively in both datasets. Our instruction specifically asks
-> Invalid unicode use found on p. 7: then to expand the selected field following this code to make the S−more inappropriate, or S+ more
-> Invalid unicode use found on p. 7: we again need to further integrate N −
-> Invalid unicode use found on p. 7: C into S−and S+. In total, we generate an additional
-> Invalid unicode use found on p. 7: 9 × 493 = 4,437 pairs of S−
-> Invalid unicode use found on p. 7: N −
-> Invalid unicode use found on p. 21: −0.4
-> Invalid unicode use found on p. 21: −7.5
-> Invalid unicode use found on p. 21: −5.0
-> Invalid unicode use found on p. 21: −1.5
-> Invalid unicode use found on p. 21: −0.6
-> Invalid unicode use found on p. 21: −1.6
-> Invalid unicode use found on p. 21: −3.5
-> Invalid unicode use found on p. 21: −0.4
-> Invalid unicode use found on p. 21: −1.2
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 22: −0.2
-> Invalid unicode use found on p. 22: −1.0
-> Invalid unicode use found on p. 22: −0.2
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 22: −2.6
-> Invalid unicode use found on p. 22: −2.0
-> Invalid unicode use found on p. 22: −1.1
-> Invalid unicode use found on p. 22: −0.8
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 22: −2.2
-> Invalid unicode use found on p. 22: −1.7
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 22: −0.2
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 22: −0.7
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 28: Each pair of S−and S+ in PrivacyLens+ and ConfAIde+ are constructed based on a set of fields. In
-> Invalid unicode use found on p. 28: PrivacyLens+ each S−and S+ is an contextual integrity information flow containing 5 fields: data
-> Invalid unicode use found on p. 28: on one field at a time per S−or S+ example. To avoid generating additional contexts that contradicts
-> Invalid unicode use found on p. 28: (denoted N −) are generated for S−examples to reinforce their inappropriateness, while appropriate
-> Invalid unicode use found on p. 28: We denote the resulting S−and S+ with one or more fields expanded with the additional context N
-> Invalid unicode use found on p. 28: as S−
-> Invalid unicode use found on p. 28: we expand each field in S−and S+ separately with their corresponding NI to form an S−
-> Invalid unicode use found on p. 28: NI. The PrivacyLens dataset includes narrative stories each expanded based on an S−using an
-> Invalid unicode use found on p. 28: them to the relevant fields in the original S−and S+ examples. For ConfAIde+, however, these
-> Invalid unicode use found on p. 28: label-independent contexts need to be generated. For each of the 7 fields in an S−example (or an S+
-> Invalid unicode use found on p. 28: neutral context, and then integrate this expanded context into the original S−(or S+).
-> Invalid unicode use found on p. 28: In total, this procedure generates an additional 5 × 493 = 2465 pairs of S−
-> Invalid unicode use found on p. 28: including prompts and the generated S−
-> Invalid unicode use found on p. 28: NI and S−
-> Invalid unicode use found on p. 28: label-dependent contextual details to S−and S+ examples according to the definition of the fields in
-> Invalid unicode use found on p. 28: N −
-> Invalid unicode use found on p. 28: D respectively. Incorporating these contexts yields examples denoted as S−
-> Invalid unicode use found on p. 28: N −
-> Invalid unicode use found on p. 29: For both datasets, an N −
-> Invalid unicode use found on p. 29: in S−(or S+, respectively) to make the example more inappropriate (or appropriate, respectively).
-> Invalid unicode use found on p. 29: and all 7 fields in ConfAIde+, resulting in an additional 2465 pairs of S−
-> Invalid unicode use found on p. 29: N −
-> Invalid unicode use found on p. 29: reducing implicit reasoning assumptions. We denote the label-dependent contexts we add to the S−
-> Invalid unicode use found on p. 29: and S+ examples as, respectively N −
-> Invalid unicode use found on p. 29: C . To generate an N −
-> Invalid unicode use found on p. 29: in the expansions. This process is repeated for all S−and S+ examples in PrivacyLens+, adding
-> Invalid unicode use found on p. 29: an additional 9 × 493 = 4,437 pairs of S−
-> Invalid unicode use found on p. 29: N −
-> Invalid unicode use found on p. 29: LLM is additionally instructed to incorporate generated N −
-> Invalid unicode use found on p. 29: C into the original S−and S+
-> Invalid unicode use found on p. 29: examples, creating an additional 9 × 270 = 2,430 pairs of S−
-> Invalid unicode use found on p. 29: N −
-> Invalid unicode use found on p. 30: seed that defines a core privacy-norm-violating scenario. S−is then developed into an elaborate
-> Invalid unicode use found on p. 30: examples of negative scenarios S−, and has been used extensively by prior work [28, 5, 25].
-> Invalid unicode use found on p. 31: information flows. We refer to each of them as S−. Example 2 is the S−example of the Example 1
-> Invalid unicode use found on p. 31: Example 2: An S−example representing an inappropriate information flow in PrivacyLens+.
-> Invalid unicode use found on p. 31: data_subject fields of S−using the contextually appropriate information in the story. The LLM is
-> Invalid unicode use found on p. 31: "marital status") to align with the abstraction level of S−. Systematic application of this procedure
-> Invalid unicode use found on p. 31: across all original Privacylens examples yields 493 S−and 493 S+. See Prompt 1 for the procedure
-> Invalid unicode use found on p. 33: We generate examples with label-independent contexts, S−
-> Invalid unicode use found on p. 33: each S−with contextual details from its corresponding PrivacyLens story. PrivacyLens includes
-> Invalid unicode use found on p. 33: version of S−(Example 5). For each flow, the data_type is directly updated with this more concrete
-> Invalid unicode use found on p. 33: We replace fields in S−with fields generated in this step one field at a time to form S−
-> Invalid unicode use found on p. 35: Prompt 4: Prompt to add label-independent contexts from story to the transmission_principle field in S−.
-> Invalid unicode use found on p. 38: by applying this example input to Example 2 is shown in Example 8 The contexts N −
-> Invalid unicode use found on p. 38: generated at this step are used to replace the corresponding fields in S−and S+ to assess the
-> Invalid unicode use found on p. 40: Example 8: An example inappropriate contexts (N −
-> Invalid unicode use found on p. 40: input to the LLM, an example generated context (N −
-> Invalid unicode use found on p. 41: Example 9: An example inappropriate context (N −
-> Invalid unicode use found on p. 41: Tier 3 of the ConfAIde dataset consists of 270 seeds S−with multiple fields. We modify the original
-> Invalid unicode use found on p. 41: S−example describes an inappropriate scenario where an aware agent tries to disclose a sensitive
-> Invalid unicode use found on p. 42: expand it by creating positive equivalents. To generate the corresponding S+ for a seed S−, we
-> Invalid unicode use found on p. 42: prompt Gemini 2.0 Pro to generate a non-sensitive detail about the subject agent contained in S−
-> Invalid unicode use found on p. 43: step yields the enhanced seeds for the negative examples S−in ConfAIde. The seeds for the positive
-> Invalid unicode use found on p. 45: corresponding story in Example 11 is shown in Example 15. The contexts N −
-> Invalid unicode use found on p. 45: this step are used to replace the corresponding fields in S−and S+ and in the stories, to assess the
-> Invalid unicode use found on p. 46: Example 15: An example context (N −
-> Invalid unicode use found on p. 47: its story in Example 12 is shown in Example 16. The contexts N −
-> Invalid unicode use found on p. 47: used to replace the corresponding fields in S−and S+ and in the stories, to assess the information
-> Invalid unicode use found on p. 48: Example 16: An example context (N −
-> Invalid unicode use found on p. 49: Example 17. The contexts N −
-> Invalid unicode use found on p. 49: fields in S−and S+ and in the stories, to assess the information sharing decisions after labelindependent expansion.
-> Invalid unicode use found on p. 50: Example 17: An example context (N −
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 443 sentences on 11 pages -> Avg. of 45.3 sentences per page
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
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
  -> Found 1 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 6 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 16
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 17
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 18
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 19
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 20
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
###############################
# Starting Author Check
###############################
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\5 Privacy Reasoning\PAU_results.md
```

---

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\5 Privacy Reasoning\Privacy Reasoning Partnergate Version.pdf"
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
- Found following heading '2 - Background and Related Work' on page 2
- Found following heading '3 - Problem Statement' on page 3
- Found following heading '4 - Context Ambiguity Analysis' on page 4
- Found following heading '5 - Camber: A Context Disambiguation Framework' on page 5
- Found following heading '6 - Results' on page 8
- Found following heading '7 - Discussion and Limitations' on page 9
- Found following heading '8 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Motivating examples from PrivacyLens+' on page 20
- Found following appendix 'B - Detailed Results' on page 21
- Found following appendix 'C - Detailed description of the Camber disambiguation framework' on page 29
- Found following appendix 'D - Datasets and dataset expansions' on page 31
- Found following appendix 'E - Evaluation' on page 52
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 20
All found references: 34
-----------
 -> Parsed references DataFrame:
   ref_id  ... valid
0       1  ...  None
1       2  ...  None
2       3  ...  None
3       4  ...  None
4       5  ...  None
5       6  ...  None
6       7  ...  None
7       8  ...  None
8       9  ...  None
9      10  ...  None
10     11  ...  None
11     12  ...  None
12     13  ...  None
13     14  ...  None
14     15  ...  None
15     16  ...  None
16     17  ...  None
17     18  ...  None
18     19  ...  None
19     20  ...  None
20     21  ...  None
21     22  ...  None
22     23  ...  None
23     24  ...  None
24     25  ...  None
25     26  ...  None
26     27  ...  None
27     28  ...  None
28     29  ...  None
29     30  ...  None
30     31  ...  None
31     32  ...  None
32     33  ...  None
33     34  ...  None

[34 rows x 10 columns]
- Checking reference 1/34:
  -> INFO: Now checking 10 results for matching title: 'Privacy as contextual integrity'
       -> INFO: All authors matched!
- Checking reference 2/34:
  -> INFO: Now checking 9 results for matching title: 'Privacy in context: Technology, policy, and the integrity of social life'
       -> INFO: All authors matched!
- Checking reference 3/34:
  -> Checking if provided link is pingable: https://github.com/skywalker023/confAIde/tree/main/benchmark.
  -> INFO: Now checking 1 results for matching title: 'Can LLMs keep a secret? testing privacy implications of language models via contextual integrity theory'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/34:
  -> Checking if provided link is pingable: https://github.com/SALT-NLP/PrivacyLens.
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'PrivacyLens: Evaluating privacy norm awareness of language models in action'
       -> INFO: All authors matched!
- Checking reference 5/34:
  -> INFO: Now checking 10 results for matching title: 'Trustllm: Trustworthiness in large language models'
       -> WARNING: Not all 66 authors from the found ref. were matched (only 30)
                   Unmatched authors = 'Liu, Liu, Kailkhura, Xiong, Xiao, Xing, Liu, Yao, Kellis, Zitnik, Jiang, Bansal, Zou, Pei, Liu, Zhao, Tang, Mitchell, Shu, Chang, He, Backes, Gong, Chen, Gu, Ying, Jana, Chen, Liu, Zhou, Xie, Chen, Liu, Ye, Cao, Zhao'
       -> WARNING: Not all 71 authors from the found ref. were matched (only 32)
                   Unmatched authors = 'Liu, Liu, Vidgen, Kailkhura, Xiong, Xiao, Xing, Liu, Yao, Kellis, Zitnik, Jiang, Bansal, Zou, Pei, Liu, Zhao, Tang, Vanschoren, Mitchell, Shu, Chang, He, Backes, Gong, Chen, Gu, Ying, Jana, Chen, Liu, Zhou, Xie, Chen, Liu, Ye, Cao, Chen, Zhao'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cerqueira, Kemell, Rousi, Hamari, Abrahamsson'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Aljohani, Hou, Kommu'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Liang, He'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 6/34:
  -> INFO: Now checking 10 results for matching title: 'Position: Contextual integrity washing for language models'
       -> INFO: All authors matched!
       -> WARNING: Year (2025) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/34:
  -> INFO: Now checking 2 results for matching title: 'FANToM: A benchmark for stress-testing machine theory of mind in interactions'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 5)
                   Unmatched authors = 'Zhou, Bras'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Chan, Jiayang, Yim, Deng, Fan, Liu, Zhang, Wang, Song'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/34:
  -> INFO: Now checking 1 results for matching title: 'Minding language models’ (lack of) theory of mind: A plug-and-play multi-character belief tracker'
       -> INFO: All authors matched!
- Checking reference 9/34:
  -> INFO: Now checking 1 results for matching title: 'Did aristotle use a laptop? a question answering benchmark with implicit reasoning strategies'
       -> INFO: All authors matched!
- Checking reference 10/34:
  -> INFO: Now checking 2 results for matching title: 'MuSR: Testing the limits of chain-of-thought with multistep soft reasoning'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Bostrom, Chaudhuri'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Bostrom, Chaudhuri'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/34:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 1 results for matching title: 'Zebralogic: On the scaling limits of llms for logical reasoning'
       -> INFO: All authors matched!
- Checking reference 12/34:
  -> INFO: Now checking 1 results for matching title: 'A chain-of-thought is as strong as its weakest link: A benchmark for verifiers of reasoning chains'
       -> INFO: All authors matched!
- Checking reference 13/34:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: QuestBench: Can llm ask the right question to acquire information in reasoning tasks? arXiv preprint arXiv:2503
  -> WARNING: No results were found through the dblp search!
  -> Failed to query dblp API. Status code: 503
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Li', 'Kim', 'Wang', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=QuestBench:+Can+llm+ask+the+right+question+to+acquire+information+in+reasoning+tasks?+arXiv+preprint+arXiv:2503 manually and check the results.
        -> Author(s): Belinda Z Li, Been Kim, and Zi Wang
        -> Title:     QuestBench: Can llm ask the right question to acquire information in reasoning tasks? arXiv preprint arXiv:2503
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 14/34:
  -> INFO: Now checking 10 results for matching title: 'Extracting training data from large language models'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 9)
                   Unmatched authors = 'Tramèr, Oprea, Raffel'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Jiang, Xu, Yang, Zhang, Guo'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cao, Wei'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 15/34:
  -> INFO: Now checking 2 results for matching title: 'Beyond memorization: Violating privacy via inference with large language models'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Balunovi'c'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/34:
  -> INFO: Now checking 10 results for matching title: 'Deep learning with differential privacy'
       -> INFO: All authors matched!
- Checking reference 17/34:
  -> INFO: Now checking 10 results for matching title: 'Large language models can be strong differentially private learners'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Tramèr'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/34:
  -> INFO: Now checking 10 results for matching title: 'Differentially private fine-tuning of language models'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 19/34:
  -> INFO: Now checking 10 results for matching title: 'Retrieval-augmented generation for knowledgeintensive NLP tasks'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 9)
                   Unmatched authors = 'Kuttler, Riedel, Kiela'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wang, Singh, Chaudhary'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/34:
  -> INFO: Now checking 10 results for matching title: 'Airgapagent: Protecting privacy-conscious conversational agents'
       -> INFO: All authors matched!
- Checking reference 21/34:
  -> INFO: Now checking 1 results for matching title: 'Protecting users from themselves: Safeguarding contextual privacy in interactions with conversational agents'
       -> INFO: All authors matched!
- Checking reference 22/34:
  -> INFO: Now checking 3 results for matching title: 'AgentDAM: Privacy leakage evaluation for autonomous web agents'
       -> INFO: All authors matched!
- Checking reference 23/34:
  -> INFO: Now checking 1 results for matching title: 'On the trustworthiness of generative foundation models: Guideline, assessment, and perspective'
       -> WARNING: Not all 65 authors from the found ref. were matched (only 24)
                   Unmatched authors = 'Li, Bao, Liu, Guan, Chen, Chen, Guo, Zou, Kuen-Yew, Xiong, Stengel-Eskin, Yin, Yao, Yoon, Shu, Zhu, Krishna, Swayamdipta, Li, Li, Li, Chen, Tu, Zhao, Sun, Sasson, Sattigeri, Reuel, Lamparth, Zhao, Dziri, Su, Sun, Xiao, Bansal, Chawla, Pei, Backes, Gong, Chen, Li'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 24/34:
  -> INFO: Now checking 2 results for matching title: 'Decodingtrust: A comprehensive assessment of trustworthiness in gpt models'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 12)
                   Unmatched authors = 'Truong, Arora, Mazeika, Hendrycks, Cheng, Koyejo, Song'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 12)
                   Unmatched authors = 'Arora, Cheng, Hendrycks, Koyejo, Mazeika, Song, Truong'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 25/34:
  -> INFO: Now checking 10 results for matching title: 'Multitrust: A comprehensive benchmark towards trustworthy multimodal large language models'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Dong, Zhu'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Shen, Qian, Lu, Zhou'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
       -> WARNING: Not all 13 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Dong, Zhu'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Yu, Cui, Chua'
       -> WARNING: Not all 22 authors from the found ref. were matched (only 5)
                   Unmatched authors = 'Surana, Mundada, Jiang, Tang, Jiao, Xiong, Wu, Yu, Jain, Kuang, Zhou, Jin, Chu, Yu, Rossi, Shang, McAuley'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Rahman, Jamil, Hossain, Khan, Zia, Paracha, Alrashoud, Al-Hazzaa'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 26/34:
  -> INFO: Now checking 1 results for matching title: 'GOLDCOIN: Grounding large language models in privacy laws via contextual integrity theory'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Deng, Wang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 27/34:
  -> INFO: Now checking 1 results for matching title: 'Privacy Checklist: Privacy violation detection grounding on contextual integrity theory'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 28/34:
  -> INFO: Now checking 5 results for matching title: 'LLM-CI: Assessing contextual integrity norms in language models'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 2)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/34:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 3 results for matching title: 'Operationalizing contextual integrity in privacy-conscious assistants'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Year (2024) does not match expected year (2025)!
       -> INFO: All named authors matched; rest may fall under 'et al.'.
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/34:
  -> INFO: Now checking 1 results for matching title: 'PrivaCI-Bench: Evaluating privacy with contextual integrity and legal compliance'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Jing'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/34:
  -> INFO: Now checking 1 results for matching title: 'Ci-bench: Benchmarking contextual integrity of ai assistants on synthetic data'
       -> INFO: All authors matched!
- Checking reference 32/34:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 3 results for matching title: 'Contextual integrity in llms via reasoning and reinforcement learning'
       -> INFO: All authors matched!
- Checking reference 33/34:
  -> INFO: Now checking 10 results for matching title: 'Reasoning models don’t always say what they think'
       -> WARNING: Not all 15 authors from the found ref. were matched (only 14)
                   Unmatched authors = 'Perez'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Turpin, Michael, Perez'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/34:
  -> Checking if provided link is pingable: https://github.com/google-parfait/contextual-privacy-and-security.Guidelines:•
  -> INFO: Now checking 1 results for matching title: 'A team-based approach to open coding: Considerations for creating intercoder consensus'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 3: (denoted as S−) to measure privacy leakage, we augment them by incorporating instances where
-> Invalid unicode use found on p. 3: For each S−, we generate a corresponding positive scenario S+ by modifying a subset of its fields.
-> Invalid unicode use found on p. 3: S−, and contain 986 and 540 examples respectively. A detailed description of the dataset generation
-> Invalid unicode use found on p. 5: −to [Data
-> Invalid unicode use found on p. 5: −based
-> Invalid unicode use found on p. 5: example’s appropriateness label. Specifically, we generate inappropriate contexts (denoted N −) for
-> Invalid unicode use found on p. 5: S−examples to reinforce their inappropriateness and appropriate contexts (denoted N +) for S+
-> Invalid unicode use found on p. 5: context. In total, this procedure generates an additional 5 × 493 = 2,465 pairs of S−
-> Invalid unicode use found on p. 5: procedure, including prompts and the generated S−
-> Invalid unicode use found on p. 5: NI and S−
-> Invalid unicode use found on p. 5: adds contextual details to S−and S+ examples according to the definition of the fields in each
-> Invalid unicode use found on p. 5: dataset. These label-dependent contexts are either inappropriate or appropriate, denoted as N −
-> Invalid unicode use found on p. 6: D respectively. Incorporating these contexts yields examples denoted as S−
-> Invalid unicode use found on p. 6: N −
-> Invalid unicode use found on p. 6: both datasets, we first ask the LLM to generate N −
-> Invalid unicode use found on p. 6: D ) for a specific field in S−
-> Invalid unicode use found on p. 6: dataset, resulting in an additional 2,465 pairs of S−
-> Invalid unicode use found on p. 6: N −
-> Invalid unicode use found on p. 7: To test if codes are more effective at reducing implicit reasoning assumptions, we prompt the LLM to generate label-dependent contexts based on each code (denoted as N −
-> Invalid unicode use found on p. 7: C ) for all S−and S+ examples respectively in both datasets. Our instruction specifically asks
-> Invalid unicode use found on p. 7: then to expand the selected field following this code to make the S−more inappropriate, or S+ more
-> Invalid unicode use found on p. 7: we again need to further integrate N −
-> Invalid unicode use found on p. 7: C into S−and S+. In total, we generate an additional
-> Invalid unicode use found on p. 7: 9 × 493 = 4,437 pairs of S−
-> Invalid unicode use found on p. 7: N −
-> Invalid unicode use found on p. 21: −0.4
-> Invalid unicode use found on p. 21: −7.5
-> Invalid unicode use found on p. 21: −5.0
-> Invalid unicode use found on p. 21: −1.5
-> Invalid unicode use found on p. 21: −0.6
-> Invalid unicode use found on p. 21: −1.6
-> Invalid unicode use found on p. 21: −3.5
-> Invalid unicode use found on p. 21: −0.4
-> Invalid unicode use found on p. 21: −1.2
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 22: −0.2
-> Invalid unicode use found on p. 22: −1.0
-> Invalid unicode use found on p. 22: −0.2
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 22: −2.6
-> Invalid unicode use found on p. 22: −2.0
-> Invalid unicode use found on p. 22: −1.1
-> Invalid unicode use found on p. 22: −0.8
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 22: −2.2
-> Invalid unicode use found on p. 22: −1.7
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 22: −0.2
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 22: −0.7
-> Invalid unicode use found on p. 22: −0.5
-> Invalid unicode use found on p. 28: Each pair of S−and S+ in PrivacyLens+ and ConfAIde+ are constructed based on a set of fields. In
-> Invalid unicode use found on p. 28: PrivacyLens+ each S−and S+ is an contextual integrity information flow containing 5 fields: data
-> Invalid unicode use found on p. 28: on one field at a time per S−or S+ example. To avoid generating additional contexts that contradicts
-> Invalid unicode use found on p. 28: (denoted N −) are generated for S−examples to reinforce their inappropriateness, while appropriate
-> Invalid unicode use found on p. 28: We denote the resulting S−and S+ with one or more fields expanded with the additional context N
-> Invalid unicode use found on p. 28: as S−
-> Invalid unicode use found on p. 28: we expand each field in S−and S+ separately with their corresponding NI to form an S−
-> Invalid unicode use found on p. 28: NI. The PrivacyLens dataset includes narrative stories each expanded based on an S−using an
-> Invalid unicode use found on p. 28: them to the relevant fields in the original S−and S+ examples. For ConfAIde+, however, these
-> Invalid unicode use found on p. 28: label-independent contexts need to be generated. For each of the 7 fields in an S−example (or an S+
-> Invalid unicode use found on p. 28: neutral context, and then integrate this expanded context into the original S−(or S+).
-> Invalid unicode use found on p. 28: In total, this procedure generates an additional 5 × 493 = 2465 pairs of S−
-> Invalid unicode use found on p. 28: including prompts and the generated S−
-> Invalid unicode use found on p. 28: NI and S−
-> Invalid unicode use found on p. 28: label-dependent contextual details to S−and S+ examples according to the definition of the fields in
-> Invalid unicode use found on p. 28: N −
-> Invalid unicode use found on p. 28: D respectively. Incorporating these contexts yields examples denoted as S−
-> Invalid unicode use found on p. 28: N −
-> Invalid unicode use found on p. 29: For both datasets, an N −
-> Invalid unicode use found on p. 29: in S−(or S+, respectively) to make the example more inappropriate (or appropriate, respectively).
-> Invalid unicode use found on p. 29: and all 7 fields in ConfAIde+, resulting in an additional 2465 pairs of S−
-> Invalid unicode use found on p. 29: N −
-> Invalid unicode use found on p. 29: reducing implicit reasoning assumptions. We denote the label-dependent contexts we add to the S−
-> Invalid unicode use found on p. 29: and S+ examples as, respectively N −
-> Invalid unicode use found on p. 29: C . To generate an N −
-> Invalid unicode use found on p. 29: in the expansions. This process is repeated for all S−and S+ examples in PrivacyLens+, adding
-> Invalid unicode use found on p. 29: an additional 9 × 493 = 4,437 pairs of S−
-> Invalid unicode use found on p. 29: N −
-> Invalid unicode use found on p. 29: LLM is additionally instructed to incorporate generated N −
-> Invalid unicode use found on p. 29: C into the original S−and S+
-> Invalid unicode use found on p. 29: examples, creating an additional 9 × 270 = 2,430 pairs of S−
-> Invalid unicode use found on p. 29: N −
-> Invalid unicode use found on p. 30: seed that defines a core privacy-norm-violating scenario. S−is then developed into an elaborate
-> Invalid unicode use found on p. 30: examples of negative scenarios S−, and has been used extensively by prior work [28, 5, 25].
-> Invalid unicode use found on p. 31: information flows. We refer to each of them as S−. Example 2 is the S−example of the Example 1
-> Invalid unicode use found on p. 31: Example 2: An S−example representing an inappropriate information flow in PrivacyLens+.
-> Invalid unicode use found on p. 31: data_subject fields of S−using the contextually appropriate information in the story. The LLM is
-> Invalid unicode use found on p. 31: "marital status") to align with the abstraction level of S−. Systematic application of this procedure
-> Invalid unicode use found on p. 31: across all original Privacylens examples yields 493 S−and 493 S+. See Prompt 1 for the procedure
-> Invalid unicode use found on p. 33: We generate examples with label-independent contexts, S−
-> Invalid unicode use found on p. 33: each S−with contextual details from its corresponding PrivacyLens story. PrivacyLens includes
-> Invalid unicode use found on p. 33: version of S−(Example 5). For each flow, the data_type is directly updated with this more concrete
-> Invalid unicode use found on p. 33: We replace fields in S−with fields generated in this step one field at a time to form S−
-> Invalid unicode use found on p. 35: Prompt 4: Prompt to add label-independent contexts from story to the transmission_principle field in S−.
-> Invalid unicode use found on p. 38: by applying this example input to Example 2 is shown in Example 8 The contexts N −
-> Invalid unicode use found on p. 38: generated at this step are used to replace the corresponding fields in S−and S+ to assess the
-> Invalid unicode use found on p. 40: Example 8: An example inappropriate contexts (N −
-> Invalid unicode use found on p. 40: input to the LLM, an example generated context (N −
-> Invalid unicode use found on p. 41: Example 9: An example inappropriate context (N −
-> Invalid unicode use found on p. 41: Tier 3 of the ConfAIde dataset consists of 270 seeds S−with multiple fields. We modify the original
-> Invalid unicode use found on p. 41: S−example describes an inappropriate scenario where an aware agent tries to disclose a sensitive
-> Invalid unicode use found on p. 42: expand it by creating positive equivalents. To generate the corresponding S+ for a seed S−, we
-> Invalid unicode use found on p. 42: prompt Gemini 2.0 Pro to generate a non-sensitive detail about the subject agent contained in S−
-> Invalid unicode use found on p. 43: step yields the enhanced seeds for the negative examples S−in ConfAIde. The seeds for the positive
-> Invalid unicode use found on p. 45: corresponding story in Example 11 is shown in Example 15. The contexts N −
-> Invalid unicode use found on p. 45: this step are used to replace the corresponding fields in S−and S+ and in the stories, to assess the
-> Invalid unicode use found on p. 46: Example 15: An example context (N −
-> Invalid unicode use found on p. 47: its story in Example 12 is shown in Example 16. The contexts N −
-> Invalid unicode use found on p. 47: used to replace the corresponding fields in S−and S+ and in the stories, to assess the information
-> Invalid unicode use found on p. 48: Example 16: An example context (N −
-> Invalid unicode use found on p. 49: Example 17. The contexts N −
-> Invalid unicode use found on p. 49: fields in S−and S+ and in the stories, to assess the information sharing decisions after labelindependent expansion.
-> Invalid unicode use found on p. 50: Example 17: An example context (N −
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 443 sentences on 11 pages -> Avg. of 45.3 sentences per page
-> Warning: Reference '2' never used in the document's text.
-> Warning: Reference '8' never used in the document's text.
-> Warning: Reference '15' never used in the document's text.
-> Warning: Reference '17' never used in the document's text.
-> Warning: Reference '18' never used in the document's text.
-> Warning: Reference '21' never used in the document's text.
-> Warning: Reference '22' never used in the document's text.
-> Warning: Reference '25' never used in the document's text.
-> Warning: Reference '27' never used in the document's text.
-> Warning: Reference '28' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> WARNING: Reference with index 14 (Ref. ID = 15) has no associated sentence!
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> WARNING: Reference with index 16 (Ref. ID = 17) has no associated sentence!
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> WARNING: Reference with index 24 (Ref. ID = 25) has no associated sentence!
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> WARNING: Reference with index 26 (Ref. ID = 27) has no associated sentence!
-> WARNING: Reference with index 27 (Ref. ID = 28) has no associated sentence!
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
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
  -> Found 1 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 6 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 13
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 14
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 15
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 16
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 17
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
###############################
# Starting Author Check
###############################
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\5 Privacy Reasoning\PAU_results.md
```