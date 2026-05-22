
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\10 Redefining Experts Interpretable Decomposition\Redefining Experts Interpretable Decomposition of Language Models.pdf"
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
- Found following heading '2 - Methodology' on page 2
- Found following heading '3 - Experiments' on page 5
- Found following heading '4 - Results and Analysis' on page 6
- Found following heading '5 - Related Work' on page 9
- Found following heading '6 - Limitations and Future Work' on page 9
- Found following heading '7 - Conclusion' on page 9
=> Found references/literature section on page 10
- Found first appendix 'A - Preliminaries' on page 13
- Found following appendix 'B - Algorithms for Expert Neuron and Layer Identification' on page 13
- Found following appendix 'C - Experimental setup' on page 14
- Found following appendix 'D - Detailed Results' on page 18
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 13
All found references: 36
-> Warning: Could not parse year in reference 'Jigsaw and Conversation AI. Toxic comment classification challenge.'!
-> Warning: Malformed author string: 'Jigsaw'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                               link  valid
0       1  David Bau, Bolei Zhou, Aditya Khosla, Aude Oli...  ...                                                      None
1       2  David Bau, Jun-Yan Zhu, Hendrik Strobelt, Bole...  ...                                                      None
2       3  Tom B  Brown, Benjamin Mann, Nick Ryder, Melan...  ...                                                      None
3       4  Alexis Conneau, Kartikay Khandelwal, Naman Goy...  ...                                                      None
4       5  Xavier Suau Cuadros, Pieter Delobelle, Rin Met...  ...                                                      None
5       6  Xavier Suau Cuadros, Luca Zappella, and Nichol...  ...                                                      None
6       7  Sumanth Dathathri, Andrea Madotto, Janice Lan,...  ...                                                      None
7       8  Jacob Devlin, Ming-Wei Chang, Kenton Lee, and ...  ...                                                      None
8       9                                   Robert M  French  ...                                                      None
9      10  Samuel Gehman, Suchin Gururangan, Maarten Sap,...  ...                                                      None
10     11  Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chen...  ...                                                      None
11     12  Aaron Grattafiori, Abhimanyu Dubey, Abhinav Ja...  ...                                                      None
12     13  Albert Q  Jiang, Alexandre Sablayrolles, Arthu...  ...                                                      None
13     14                         Jigsaw and Conversation AI  ...  https://www.kaggle.com/c/jigsaw-toxic-comment-...   None
14     15  Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Gh...  ...                                                      None
15     16  Nathaniel Li, Alexander Pan, Anjali Gopal, Sum...  ...                                                      None
16     17  Junyu Lu, Bo Xu, Xiaokun Zhang, Changrong Min,...  ...                                                      None
17     18  Shervin Minaee, Tomas Mikolov, Narjes Nikzad, ...  ...                                                      None
18     19  Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhamm...  ...                                                      None
19     20  Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida,...  ...                                                      None
20     21  Alec Radford, Rafal Jozefowicz, and Ilya Sutsk...  ...                                                      None
21     22  Shashwat Singh, Shauli Ravfogel, Jonathan Herz...  ...                                                      None
22     23  Oscar Skean, Md Rifat Arefin, Dan Zhao, Niket ...  ...                                                      None
23     24  Aseem Srivastava, Smriti Joshi, Tanmoy Chakrab...  ...                                                      None
24     25  Aseem Srivastava, Ishan Pandey, Md Shad Akhtar...  ...                                                      None
25     26  Nitish Srivastava, Geoffrey Hinton, Alex Krizh...  ...                                                      None
26     27  Xavier Suau, Pieter Delobelle, Katherine Metca...  ...                                                      None
27     28  Xavier Suau, Pieter Delobelle, Katherine Metca...  ...                                                      None
28     29  Xavier Suau, Luca Zappella, and Nicholas Apost...  ...                                                      None
29     30  Xavier Suau, Luca Zappella, and Nicholas Apost...  ...                                                      None
30     31  Rheeya Uppaal, Apratim Dey, Yiting He, Yiqiao ...  ...                                                      None
31     32                  Bertie Vidgen and Leon Derczynski  ...                                                      None
32     33            Weijia Xu, Xing Niu, and Marine Carpuat  ...                                                      None
33     34                           Kevin Yang and Dan Klein  ...                                                      None
34     35  Xiang Zhang, Xuehai Wei, Xian Zhang, and Xue Z...  ...                                                      None
35     36  Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tan...  ...                                                      None

[36 rows x 10 columns]
- Checking reference 1/36:
  -> INFO: Now checking 10 results for matching title: 'Network dissection: Quantifying interpretability of deep visual representations'
       -> INFO: All authors matched!
- Checking reference 2/36:
  -> INFO: Now checking 10 results for matching title: 'Gan dissection: Visualizing and understanding generative adversarial networks'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
       -> WARNING: Not all 6 authors from the found ref. were matched (only 6)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/36:
  -> INFO: Now checking 10 results for matching title: 'Language models are few-shot learners.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Language models are few-shot learners.'
       -> WARNING: Not all 31 authors from the found ref. were matched (only 29)
                   Unmatched authors = '0003, 0003'
       -> WARNING: Not all 31 authors from the found ref. were matched (only 29)
                   Unmatched authors = '0003, 0003'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/36:
  -> INFO: Now checking 10 results for matching title: 'Unsupervised cross-lingual representation learning at scale'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 5/36:
  -> INFO: Now checking 1 results for matching title: 'Whispering experts: Toxicity mitigation in pre-trained language models by dampening expert neurons'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Cuadros', 'Delobelle', 'Susa', 'Joulin', 'Apostoloff', 'Zappella', 'Lopez', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Whispering+experts:+Toxicity+mitigation+in+pre-trained+language+models+by+dampening+expert+neurons manually and check the results.
        -> Author(s): Xavier Suau Cuadros, Pieter Delobelle, Rin Metcalf Susa, Armand Joulin, Nick Apostoloff, Luca Zappella, and Pau Rodriguez Lopez
        -> Title:     Whispering experts: Toxicity mitigation in pre-trained language models by dampening expert neurons
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 6/36:
  -> INFO: Now checking 10 results for matching title: 'Self-conditioning pre-trained language models'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
       -> WARNING: Not all 1 authors from the found ref. were matched (only 1)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/36:
  -> INFO: Now checking 10 results for matching title: 'Plug and play language models: A simple approach to controlled text generation'
       -> INFO: All authors matched!
       -> WARNING: Year (2019) does not match expected year (2020)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/36:
  -> INFO: Now checking 10 results for matching title: 'Bert: Pre-training of deep bidirectional transformers for language understanding'
       -> INFO: All authors matched!
- Checking reference 9/36:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Catastrophic interference in connectionist networks: can it be predicted, can it be prevented? In Proceedings of the 7th International Conference on Neural Information Processing Systems, NIPS’93, page 1176–1177, San Francisco, CA, USA.
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 28 results for matching title: 'Catastrophic interference in connectionist networks: can it be predicted, can it be prevented? In Proceedings of the 7th International Conference on Neural Information Processing Systems, NIPS’93, page 1176–1177, San Francisco, CA, USA.'
  -> WARNING: None of the 28 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Catastrophic+interference+in+connectionist+networks:+can+it+be+predicted%2C+can+it+be+prevented?+In+Proceedings+of+the+7th+International+Conference+on+Neural+Information+Processing+Systems%2C+NIPS’93%2C+page+1176–1177%2C+San+Francisco%2C+CA%2C+USA. manually and check the results.
        -> Author(s): Robert M  French
        -> Title:     Catastrophic interference in connectionist networks: can it be predicted, can it be prevented? In Proceedings of the 7th International Conference on Neural Information Processing Systems, NIPS’93, page 1176–1177, San Francisco, CA, USA.
        -> Year:      1993
     -> Manual search was skipped by the user.
- Checking reference 10/36:
  -> INFO: Now checking 4 results for matching title: 'Realtoxicityprompts: Evaluating neural toxic degeneration in language models'
       -> INFO: All authors matched!
- Checking reference 11/36:
  -> INFO: Now checking 1 results for matching title: 'Chatglm: A family of large language models from glm-130b to glm-4 all tools.'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Chatglm: A family of large language models from glm-130b to glm-4 all tools.'
       -> WARNING: Not all 55 authors from the found ref. were matched (only 45)
                   Unmatched authors = '0001, 0030, 0001, 0001, 0077, 0002, 0036, 0014, 0001, 0034'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/36:
  -> INFO: Now checking 10 results for matching title: 'The llama 3 herd of models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Grattafiori', 'Dubey', 'Jauhri', 'Pandey', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=The+llama+3+herd+of+models. manually and check the results.
        -> Author(s): Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, and Abhinav Pandey
        -> Title:     The llama 3 herd of models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 13/36:
  -> INFO: Now checking 10 results for matching title: 'Mistral 7b.'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jiang', 'Sablayrolles', 'Mensch', 'Bamford', 'Chaplot', 'Casas', 'Bressand', 'Lengyel', 'Lample', 'Saulnier', 'Lavaud', 'Lachaux', 'Stock', 'Scao', 'Lavril', 'Wang', 'Lacroix', 'Sayed', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Mistral+7b. manually and check the results.
        -> Author(s): Albert Q  Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed
        -> Title:     Mistral 7b.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 14/36:
  -> Checking if provided link is pingable: https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge,
  -> INFO: Now checking 10 results for matching title: 'Toxic comment classification challenge'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jigsaw', 'AI', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Toxic+comment+classification+challenge manually and check the results.
        -> Author(s): Jigsaw and Conversation AI
        -> Title:     Toxic comment classification challenge
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 15/36:
  -> INFO: Now checking 1 results for matching title: 'BART: Denoising sequence-to-sequence pretraining for natural language generation, translation, and comprehension'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lewis', 'Liu', 'Goyal', 'Ghazvininejad', 'Mohamed', 'Levy', 'Stoyanov', 'Zettlemoyer', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=BART:+Denoising+sequence-to-sequence+pretraining+for+natural+language+generation%2C+translation%2C+and+comprehension manually and check the results.
        -> Author(s): Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov, and Luke Zettlemoyer
        -> Title:     BART: Denoising sequence-to-sequence pretraining for natural language generation, translation, and comprehension
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 16/36:
  -> INFO: Now checking 1 results for matching title: 'The wmdp benchmark: Measuring and reducing malicious use with unlearning'
       -> WARNING: Not all 53 authors from the found ref. were matched (only 51)
                   Unmatched authors = 'Helm-Burger, Herbert-Voss'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/36:
  -> INFO: Now checking 1 results for matching title: 'Facilitating fine-grained detection of Chinese toxic language: Hierarchical taxonomy, resources, and benchmarks'
       -> INFO: All authors matched!
- Checking reference 18/36:
  -> INFO: Now checking 10 results for matching title: 'Large language models: A survey.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Minaee', 'Mikolov', 'Nikzad', 'Chenaghlu', 'Socher', 'Amatriain', 'Gao', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Large+language+models:+A+survey. manually and check the results.
        -> Author(s): Shervin Minaee, Tomas Mikolov, Narjes Nikzad, Meysam Chenaghlu, Richard Socher, Xavier Amatriain, and Jianfeng Gao
        -> Title:     Large language models: A survey.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 19/36:
  -> INFO: Now checking 10 results for matching title: 'A comprehensive overview of large language models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Naveed', 'Khan', 'Qiu', 'Saqib', 'Anwar', 'Usman', 'Akhtar', 'Barnes', 'Mian', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+comprehensive+overview+of+large+language+models. manually and check the results.
        -> Author(s): Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad Saqib, Saeed Anwar, Muhammad Usman, Naveed Akhtar, Nick Barnes, and Ajmal Mian
        -> Title:     A comprehensive overview of large language models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 20/36:
  -> INFO: Now checking 10 results for matching title: 'Training language models to follow instructions with human feedback'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 21/36:
  -> INFO: Now checking 10 results for matching title: 'Learning to generate reviews and discovering sentiment'
       -> INFO: All authors matched!
- Checking reference 22/36:
  -> INFO: Now checking 1 results for matching title: 'Representation surgery: Theory and practice of affine steering'
       -> INFO: All authors matched!
- Checking reference 23/36:
  -> INFO: Now checking 10 results for matching title: 'Layer by layer: Uncovering hidden representations in language models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Skean', 'Arefin', 'Zhao', 'Patel', 'Naghiyev', 'LeCun', 'Shwartz-Ziv', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Layer+by+layer:+Uncovering+hidden+representations+in+language+models. manually and check the results.
        -> Author(s): Oscar Skean, Md Rifat Arefin, Dan Zhao, Niket Patel, Jalal Naghiyev, Yann LeCun, and Ravid Shwartz-Ziv
        -> Title:     Layer by layer: Uncovering hidden representations in language models.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 24/36:
  -> INFO: Now checking 5 results for matching title: 'Knowledge planning in large language models for domain-aligned counseling summarization'
       -> INFO: All authors matched!
- Checking reference 25/36:
  -> INFO: Now checking 2 results for matching title: 'Response-act guided reinforced dialogue generation for mental health counseling'
       -> INFO: All authors matched!
- Checking reference 26/36:
  -> INFO: Now checking 10 results for matching title: 'Dropout: a simple way to prevent neural networks from overfitting'
       -> INFO: All authors matched!
- Checking reference 27/36:
  -> INFO: Now checking 1 results for matching title: 'Whispering experts: neural interventions for toxicity mitigation in language models'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 6)
                   Unmatched authors = 'Rodr'iguez'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 28/36:
  -> INFO: Now checking 1 results for matching title: 'Whispering experts: Neural interventions for toxicity mitigation in language models.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Suau', 'Delobelle', 'Metcalf', 'Joulin', 'Apostoloff', 'Zappella', 'Rodríguez', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Whispering+experts:+Neural+interventions+for+toxicity+mitigation+in+language+models. manually and check the results.
        -> Author(s): Xavier Suau, Pieter Delobelle, Katherine Metcalf, Armand Joulin, Nicholas Apostoloff, Luca Zappella, and Pau Rodríguez
        -> Title:     Whispering experts: Neural interventions for toxicity mitigation in language models.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 29/36:
  -> INFO: Now checking 10 results for matching title: 'Self-conditioning pre-trained language models'
       -> INFO: All authors matched!
- Checking reference 30/36:
  -> INFO: Now checking 10 results for matching title: 'Self-conditioning pre-trained language models'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
       -> WARNING: Not all 1 authors from the found ref. were matched (only 1)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/36:
  -> INFO: Now checking 1 results for matching title: 'Model editing as a robust and denoised variant of dpo: A case study on toxicity.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Uppaal', 'Dey', 'He', 'Zhong', 'Hu', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Model+editing+as+a+robust+and+denoised+variant+of+dpo:+A+case+study+on+toxicity. manually and check the results.
        -> Author(s): Rheeya Uppaal, Apratim Dey, Yiting He, Yiqiao Zhong, and Junjie Hu
        -> Title:     Model editing as a robust and denoised variant of dpo: A case study on toxicity.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 32/36:
  -> INFO: Now checking 2 results for matching title: 'Directions in abusive language training data, a systematic review: Garbage in, garbage out'
       -> INFO: All authors matched!
- Checking reference 33/36:
  -> INFO: Now checking 10 results for matching title: 'Controlling toxicity in neural machine translation'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Xu', 'Niu', 'Carpuat', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Controlling+toxicity+in+neural+machine+translation manually and check the results.
        -> Author(s): Weijia Xu, Xing Niu, and Marine Carpuat
        -> Title:     Controlling toxicity in neural machine translation
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 34/36:
  -> INFO: Now checking 10 results for matching title: 'Fudge: Controlled text generation with future discriminators'
       -> INFO: All authors matched!
- Checking reference 35/36:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Adversarial attacks and defenses in toxicity detection: A survey
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Wei', 'Zhang', 'Zhang', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Adversarial+attacks+and+defenses+in+toxicity+detection:+A+survey manually and check the results.
        -> Author(s): Xiang Zhang, Xuehai Wei, Xian Zhang, and Xue Zhang
        -> Title:     Adversarial attacks and defenses in toxicity detection: A survey
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 36/36:
  -> INFO: Now checking 10 results for matching title: 'A survey of large language models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhao', 'Zhou', 'Li', 'Tang', 'Wang', 'Hou', 'Min', 'Zhang', 'Zhang', 'Dong', 'Du', 'Yang', 'Chen', 'Chen', 'Jiang', 'Ren', 'Li', 'Tang', 'Liu', 'Liu', 'Nie', 'Wen', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+survey+of+large+language+models. manually and check the results.
        -> Author(s): Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, Yifan Du, Chen Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, Peiyu Liu, Jian-Yun Nie, and Ji-Rong Wen
        -> Title:     A survey of large language models.
        -> Year:      2025
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: causally influenced by the semantic choice encoded in the preceding hidden state hn−1 ∈Rd.
-> Invalid unicode use found on p. 6: As Figure 3 shows, most neurons across models cluster in the narrow AUROC band of 0.50 −0.55,
-> Invalid unicode use found on p. 7: principal decision axis. When the model selects a token tn given context {t1 . . . tn−1}, a
-> Invalid unicode use found on p. 15: Lrecon = ∥W −ˆW∥F =
-> Invalid unicode use found on p. 15: (Wij −ˆWij)2
-> Invalid unicode use found on p. 16: from the set {−1, −0.5, 0, 0.1, 0.5, 0.9}. The figure illustrates how varying α influences toxicity
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 656 sentences on 10 pages -> Avg. of 73.88888888888889 sentences per page
-> Warning: Reference '26' never used in the document's text.
-> Warning: Reference '32' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
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
  -> Found 2 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\10 Redefining Experts Interpretable Decomposition\PAU_results.md
```