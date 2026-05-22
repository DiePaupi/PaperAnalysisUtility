
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\37 MIP against Agent Malicious Image Patches\MIP against Agent Malicious Image Patches Hijacking Multimodal OS Agents.pdf"
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
- Found Introduction on page 2
- Found following heading '2 - Related Work' on page 3
- Found following heading '3 - Attacking OS Agents with MIPs' on page 4
- Found following heading '4 - Experiments' on page 6
- Found following heading '5 - Conclusion and Discussion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Appendix' on page 15
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 15
All found references: 64
Backend tkagg is interactive backend. Turning interactive mode on.
-> Warning: Malformed author string: 'Anthropic'
-> Warning: Malformed author string: 'elderplinius'
-> Warning: Malformed author string: 'OpenAI'
-> Warning: Malformed author string: 'OpenAI'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors                                 normalized_authors  ...                                             outlet                                               link  valid
0       1  Maksym Andriushchenko, Alexandra Souly, Mateus...  [Andriushchenko M., Souly A., Dziemian M., Due...  ...                                              arXiv                                                      None
1       2                                          Anthropic                                        [Anthropic]  ...                                                     https://www.anthropic.com/news/3-5-models-and-...   None
2       3  Anish Athalye, Nicholas Carlini, and David Wagner                [Athalye A., Carlini N., Wagner D.]  ...       International Conference on Machine Learning                                                      None
3       4  Luke Bailey, Euan Ong, Stuart Russell, and Sco...         [Bailey L., Ong E., Russell S., Emmons S.]  ...                                              arXiv                                                      None
4       5                                     Bluesky Social                                        [Social B.]  ...                                                                                  https://bsky.social/   None
..    ...                                                ...                                                ...  ...                                                ...                                                ...    ...
59     60                Yanzhe Zhang, Tao Yu, and Diyi Yang                         [Zhang Y., Yu T., Yang D.]  ...                                              arXiv                                                      None
60     61  Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zh...  [Zhang Z., Cui S., Lu Y., Zhou J., Yang J., Wa...  ...                                              arXiv                                                      None
61     62  Yunqing Zhao, Tianyu Pang, Chao Du, Xiao Yang,...  [Zhao Y., Pang T., Du C., Yang X., Li C., Cheu...  ...  Advances in Neural Information Processing Systems                                                      None
62     63  Zhiyu Zhu, Xinyi Wang, Zhibo Jin, Jiayu Zhang,...       [Zhu Z., Wang X., Jin Z., Zhang J., Chen H.]  ...  International Conference on Learning Represent...                                                      None
63     64  Andy Zou, Zifan Wang, J Zico Kolter, and Matt ...        [Zou A., Wang Z., Kolter J., Fredrikson M.]  ...                                              arXiv                                                      None

[64 rows x 10 columns]
- Checking reference 1/64:
  -> INFO: Now checking 1 results for matching title: 'Agentharm: A benchmark for measuring harmfulness of llm agents'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 2/64:
  -> Checking if provided link is pingable: https://www.anthropic.com/news/3-5-models-and-computer-use
  -> INFO: Now checking 10 results for matching title: '3.5 Models and Computer Use.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 6 results for matching title: '3.5 Models and Computer Use.'
  -> WARNING: None of the 6 results matched the expected title!
     -> You could also open https://www.anthropic.com/news/3-5-models-and-computer-use manually and check the results.
        -> Author(s): Anthropic
        -> Title:     3.5 Models and Computer Use.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 3/64:
  -> INFO: Now checking 2 results for matching title: 'Obfuscated gradients give a false sense of security: Circumventing defenses to adversarial examples'
       -> INFO: All authors matched!
- Checking reference 4/64:
  -> INFO: Now checking 4 results for matching title: 'Image hijacks: Adversarial images can control generative models at runtime'
       -> INFO: All authors matched!
- Checking reference 5/64:
  -> Checking if provided link is pingable: https://bsky.social/
  -> INFO: Now checking 10 results for matching title: 'Bluesky social.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 993 results for matching title: 'Bluesky social.'
  -> WARNING: None of the 993 results matched the expected title!
     -> You could also open https://bsky.social/ manually and check the results.
        -> Author(s): Bluesky Social
        -> Title:     Bluesky social.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 6/64:
  -> INFO: Now checking 1 results for matching title: 'Windows agent arena: Evaluating multi-modal os agents at scale'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 7/64:
  -> INFO: Now checking 10 results for matching title: 'Adversarial attacks and defences: A survey'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/64:
  -> INFO: Now checking 10 results for matching title: 'Jailbreaking black box large language models in twenty queries'
       -> INFO: All authors matched!
- Checking reference 9/64:
  -> INFO: Now checking 1 results for matching title: 'Agentpoison: Red-teaming LLM agents via poisoning memory or knowledge bases'
       -> INFO: All authors matched!
- Checking reference 10/64:
  -> INFO: Now checking 2 results for matching title: 'How deep learning sees the world: A survey on adversarial attacks & defenses'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/64:
  -> INFO: Now checking 1 results for matching title: 'Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks'
       -> INFO: All authors matched!
- Checking reference 12/64:
  -> INFO: Now checking 1 results for matching title: 'Agentdojo: A dynamic environment to evaluate prompt injection attacks and defenses for llm agents'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Debenedetti', 'Zhang', 'Balunovi´c', 'Beurer-Kellner', 'Fischer', 'Tramèr', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Agentdojo:+A+dynamic+environment+to+evaluate+prompt+injection+attacks+and+defenses+for+llm+agents manually and check the results.
        -> Author(s): Edoardo Debenedetti, Jie Zhang, Mislav Balunovi´c, Luca Beurer-Kellner, Marc Fischer, and Florian Tramèr
        -> Title:     Agentdojo: A dynamic environment to evaluate prompt injection attacks and defenses for llm agents
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 13/64:
  -> INFO: Now checking 10 results for matching title: 'The llama 3 herd of models'
       -> WARNING: Not all 500 authors from the found ref. were matched (only 19)
                   Unmatched authors = 'Goyal, Hartshorn, Mitra, Sravankumar, Korenev, Hinsvark, Rao, Zhang, Rodriguez, Gregerson, Spataru, Rozière, Biron, Tang, Chern, Caucheteux, Nayak, Bi, Marra, McConnell, Keller, Touret, Wu, Wong, Ferrer, Nikolaidis, Allonsius, Song, Pintz, Livshits, Esiobu, Choudhary, Mahajan, Garcia-Olano, Perino, Hupkes, Lakomkin, AlBadawy, Lobanova, Dinan, Smith, Radenovic, Zhang, Synnaeve, Lee, Anderson, Nail, Mialon, Pang, Cucurell, Nguyen, Korevaar, Xu, Touvron, Zarov, Ibarra, Kloumann, Misra, Evtimov, Copet, Lee, Geffert, Vranes, Park, Mahadeokar, Shah, Linde, Billock, Hong, Lee, Fu, Chi, Huang, Liu, Wang, Bitton, Spisak, Park, Rocca, Johnstun, Saxe, Jia, Alwala, Upasani, Plawiak, Li, Heafield, Stone, El-Arini, Iyer, Malik, Chiu, Bhalla, Rantala-Yeary, Maaten, Chen, Tan, Jenkins, Martin, Madaan, Malo, Blecher, Landzaat, Oliveira, Muzzi, Pasupuleti, Singh, Paluri, Kardas, Oldham, Rita, Pavlova, Kambadur, Lewis, Si, Singh, Hassan, Goyal, Torabi, Bashlykov, Bogoychev, Chatterji, Duchenne, cCelebi, Alrassy, Zhang, Li, Vasić, Weng, Bhargava, Dubal, Krishnan, Koura, Xu, Dong, Srinivasan, Ganapathy, Calderer, Cabral, Stojnic, Raileanu, Girdhar, Patel, Sauvestre, Polidoro, Sumbaly, Taylor, Silva, Hou, Wang, Hosseini, Chennabasappa, Singh, Bell, Kim, Edunov, Nie, Narang, Raparthy, Shen, Wan, Bhosale, Zhang, Vandenhende, Batra, Whitman, Sootla, Collot, Gururangan, Borodinsky, Herman, Fowler, Sheasha, Georgiou, Scialom, Speckbacher, Mihaylov, Xiao, Karn, Goswami, Gupta, Ramanathan, Kerkez, Gonguet, Do, Vogeti, Petrovic, Chu, Xiong, Fu, Meers, Martinet, Wang, Tan, Xie, Jia, Wang, Goldschlag, Gaur, Babaei, Wen, Song, Zhang, Li, Mao, Coudert, Chen, Papakipos, Singh, Grattafiori, Jain, Kelsey, Shajnfeld, Gangidi, Victoria, Goldstand, Menon, Sharma, Boesenberg, Vaughan, Baevski, Feinstein, Kallet, Sangani, Yunus, Lupu, Alvarado, Caples, Gu, Ho, Poulton, Ryan, Ramchandani, Franco, Saraf, Chowdhury, Gabriel, Bharambe, Eisenman, Yazdan, James, Maurer, Leonhardi, Huang, Loyd, Paola, Paranjape, Liu, Wu, Ni, Hancock, Wasti, Spence, Stojkovic, Gamido, Montalvo, Parker, Burton, Mejia, Wang, Kim, Zhou, Chu, Cai, Tindal, Feichtenhofer, Civin, Beaty, Kreymer, Li, Wyatt, Adkins, Xu, Testuggine, David, Parikh, Liskovich, Foss, Wang, Holland, Dowling, Jamil, Montgomery, Presani, Hahn, Wood, Brinkman, Arcaute, Dunbar, Smothers, Sun, Kreuk, Tian, Ozgenel, Caggioni, Guzmán, Kanayet, Seide, Florez, Schwarz, Badeer, Swee, Halpern, Thattai, Herman, Sizov, Zhang, Lakshminarayanan, Shojanazeri, Zou, Wang, Zha, Habeeb, Rudolph, Suk, Aspegren, Goldman, Molybog, Tufanov, Veliche, Gat, Weissman, Geboski, Kohli, Asher, Gaya, Marcus, Tang, Chan, Zhen, Reizenstein, Teboul, Zhong, Jin, Cummings, Carvill, Shepard, McPhie, Torres, Ginsburg, Wang, Wu, KamHou, Saxena, Prasad, Khandelwal, Zand, Matosich, Veeraraghavan, Michelena, Li, Huang, Chawla, Lakhotia, Huang, Chen, Garg, Lavender, Silva, Bell, Zhang, Guo, Moshkovich, Wehrstedt, Khabsa, Avalani, Bhatt, Tsimpoukelli, Mankus, Hasson, Lennie, Reso, Groshev, Naumov, Lathi, Keneally, Seltzer, Valko, Restrepo, Patel, Vyatskov, Samvelyan, Clark, Macey, Wang, Hermoso, Metanat, Rastegari, Bansal, Santhanam, Parks, White, Bawa, Singhal, Egebo, Usunier, Laptev, Dong, Zhang, Cheng, Chernoguz, Hart, Salpekar, Kalinli, Kent, Parekh, Saab, Balaji, Rittner, Bontrager, Roux, Dollár, Zvyagina, Ratanchandani, Yuvraj, Liang, Alao, Rodriguez, Ayub, Murthy, Nayani, Mitra, Li, Hogan, Battey, Wang, Maheswari, Howes, Rinott, Bondu, Datta, Chugh, Hunt, Dhillon, Sidorov, Verma, Yamamoto, Ramaswamy, Lindsay, Feng, Lin, Zha, Shankar, Zhang, Wang, Agarwal, Sajuyigbe, Chintala, Max, Chen, Kehoe, Satterfield, Govindaprasad, Gupta, Cho, Virk, Subramanian, Choudhury, Goldman, Remez, Glaser, Best, Kohler, Robinson, Li, Zhang, Matthews, Chou, Shaked, Vontimitta, Ajayi, Montanez, Mohan, Kumar, Mangla, Ionescu, Poenaru, Mihailescu, Ivanov, Li, Wang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 14/64:
  -> Checking if provided link is pingable: https://x.com/elder_plinius/status/1848868762327650411
  -> INFO: Now checking 10 results for matching title: 'elderplinius, August'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['elderplinius', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://x.com/elder_plinius/status/1848868762327650411 manually and check the results.
        -> Author(s): elderplinius
        -> Title:     elderplinius, August
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 15/64:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: ZombAIs: From Prompt Injection to C2 with Claude Computer Use.
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 997 results for matching title: 'ZombAIs: From Prompt Injection to C2 with Claude Computer Use.'
  -> WARNING: None of the 997 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=ZombAIs:+From+Prompt+Injection+to+C2+with+Claude+Computer+Use. manually and check the results.
        -> Author(s): Embrace The Red
        -> Title:     ZombAIs: From Prompt Injection to C2 with Claude Computer Use.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 16/64:
  -> INFO: Now checking 1 results for matching title: 'Shh, don’t say that! domain certification in LLMs'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Ghanem'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/64:
  -> INFO: Now checking 10 results for matching title: 'Wasp: Benchmarking web agent security against prompt injection attacks'
       -> INFO: All authors matched!
- Checking reference 18/64:
  -> INFO: Now checking 1 results for matching title: 'Imprompter: Tricking llm agents into improper tool use'
       -> INFO: All authors matched!
- Checking reference 19/64:
  -> INFO: Now checking 10 results for matching title: 'Explaining and harnessing adversarial examples'
       -> INFO: All authors matched!
       -> WARNING: Year (2014) does not match expected year (2015)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/64:
  -> INFO: Now checking 1 results for matching title: 'Agent smith: A single image can jailbreak one million multimodal LLM agents exponentially fast'
       -> INFO: All authors matched!
- Checking reference 21/64:
  -> INFO: Now checking 10 results for matching title: 'Multimodal adversarial examples'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 4 results for matching title: 'Multimodal adversarial examples'
  -> WARNING: None of the 4 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Multimodal+adversarial+examples manually and check the results.
        -> Author(s): Yiran Guo, Linqing Duan, Yuexiang Zhang, Xiangyan Zhang, and Dinggang Shen
        -> Title:     Multimodal adversarial examples
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 22/64:
  -> INFO: Now checking 10 results for matching title: 'Best-of-n jailbreaking'
       -> INFO: All authors matched!
- Checking reference 23/64:
  -> INFO: Now checking 7 results for matching title: 'Adversarial examples are not bugs, they are features'
  -> WARNING: None of the 7 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Jia', 'Liang', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Adversarial+examples+are+not+bugs%2C+they+are+features manually and check the results.
        -> Author(s): Robin Jia and Percy Liang
        -> Title:     Adversarial examples are not bugs, they are features
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 24/64:
  -> INFO: Now checking 10 results for matching title: 'Adam: A method for stochastic optimization'
       -> INFO: All authors matched!
- Checking reference 25/64:
  -> INFO: Now checking 10 results for matching title: 'Visualwebarena: Evaluating multimodal agents on realistic visual web tasks'
       -> INFO: All authors matched!
- Checking reference 26/64:
  -> INFO: Now checking 1 results for matching title: 'A reading survey on adversarial machine learning: Adversarial attacks and their understanding'
       -> INFO: All authors matched!
- Checking reference 27/64:
  -> INFO: Now checking 1 results for matching title: 'Adversarial examples are not easily detected: Bypassing ten detection methods'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Kurakin', 'Goodfellow', 'Bengio', '2016']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Adversarial+examples+are+not+easily+detected:+Bypassing+ten+detection+methods manually and check the results.
        -> Author(s): Alexey Kurakin, Ian J Goodfellow, and Samy Bengio
        -> Title:     Adversarial examples are not easily detected: Bypassing ten detection methods
        -> Year:      2016
     -> Manual search was skipped by the user.
- Checking reference 28/64:
  -> INFO: Now checking 10 results for matching title: 'Adversarial examples in the physical world'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/64:
  -> INFO: Now checking 10 results for matching title: 'Adversarial attack on vision-language models via cross-modal denoising'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', 'Zhu', 'Zhang', 'Li', 'Li', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Adversarial+attack+on+vision-language+models+via+cross-modal+denoising manually and check the results.
        -> Author(s): Dong Liu, Ji Zhu, Tao Zhang, Bo Li, and Hongyang Li
        -> Title:     Adversarial attack on vision-language models via cross-modal denoising
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 30/64:
  -> INFO: Now checking 1 results for matching title: 'Grounding dino: Marrying dino with grounded pre-training for open-set object detection'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 11)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 31/64:
  -> INFO: Now checking 1 results for matching title: 'Apigen: Automated pipeline for generating verifiable and diverse function-calling datasets'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 32/64:
  -> INFO: Now checking 5 results for matching title: 'Omniparser for pure vision based gui agent'
       -> INFO: All authors matched!
- Checking reference 33/64:
  -> INFO: Now checking 10 results for matching title: 'Towards deep learning models resistant to adversarial attacks'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Ma̧dry'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/64:
  -> INFO: Now checking 1 results for matching title: 'Harmbench: A standardized evaluation framework for automated red teaming and robust refusal'
       -> INFO: All authors matched!
- Checking reference 35/64:
  -> INFO: Now checking 10 results for matching title: 'Multimodal adversarial robustness: Attack and defense'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Nguyen', 'Li', 'Qin', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Multimodal+adversarial+robustness:+Attack+and+defense manually and check the results.
        -> Author(s): Anh Tuan Nguyen, Shengping Li, and Chao Qin
        -> Title:     Multimodal adversarial robustness: Attack and defense
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 36/64:
  -> INFO: Now checking 10 results for matching title: 'Gpt-4 technical report'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 37/64:
  -> Checking if provided link is pingable: https://openai.com/dall-e-3/
  -> INFO: Now checking 10 results for matching title: 'Dall·e 3'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['OpenAI', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://openai.com/dall-e-3/ manually and check the results.
        -> Author(s): OpenAI
        -> Title:     Dall·e 3
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 38/64:
  -> Checking if provided link is pingable: https://github.com/gpt-engineer-org/gpt-engineer
  -> INFO: Now checking 10 results for matching title: 'gpt-engineer.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Osika', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://github.com/gpt-engineer-org/gpt-engineer manually and check the results.
        -> Author(s): Anton Osika
        -> Title:     gpt-engineer.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 39/64:
  -> INFO: Now checking 10 results for matching title: 'Training language models to follow instructions with human feedback'
       -> INFO: All authors matched!
- Checking reference 40/64:
  -> INFO: Now checking 1 results for matching title: 'Gorilla: Large language model connected with massive apis'
       -> INFO: All authors matched!
- Checking reference 41/64:
  -> INFO: Now checking 10 results for matching title: 'Cross-modal adversarial training for multimodal classification'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Qi', 'Tan', 'Zhang', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Cross-modal+adversarial+training+for+multimodal+classification manually and check the results.
        -> Author(s): Heng Qi, Zhaokang Tan, and Xingxing Zhang
        -> Title:     Cross-modal adversarial training for multimodal classification
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 42/64:
  -> INFO: Now checking 2 results for matching title: 'Toolllm: Facilitating large language models to master 16000+ real-world apis'
       -> WARNING: Not all 18 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Zhao, Tian, Xie, Zhou, Gerstein, Liu, Sun'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 43/64:
  -> INFO: Now checking 10 results for matching title: 'Hierarchical text-conditional image generation with clip latents.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ramesh', 'Pavlov', 'Goh', 'Gray', 'Voss', 'Radford', 'Chen', 'Sutskever', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Hierarchical+text-conditional+image+generation+with+clip+latents. manually and check the results.
        -> Author(s): Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford, Mark Chen, and Ilya Sutskever
        -> Title:     Hierarchical text-conditional image generation with clip latents.
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 44/64:
  -> INFO: Now checking 2 results for matching title: 'Gradientbased jailbreak images for multimodal fusion models'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Rando', 'Korevaar', 'Brinkman', 'Evtimov', 'Tramèr', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gradientbased+jailbreak+images+for+multimodal+fusion+models manually and check the results.
        -> Author(s): Javier Rando, Hannah Korevaar, Erik Brinkman, Ivan Evtimov, and Florian Tramèr
        -> Title:     Gradientbased jailbreak images for multimodal fusion models
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 45/64:
  -> INFO: Now checking 4 results for matching title: 'Failures to find transferable image jailbreaks between vision-language models'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Year (2024) does not match expected year (2025)!
       -> INFO: All named authors matched; rest may fall under 'et al.'.
  -> INFO: No perfect match found; taking the next best!
- Checking reference 46/64:
  -> INFO: Now checking 1 results for matching title: 'An overview of the tesseract ocr engine'
       -> INFO: All authors matched!
- Checking reference 47/64:
  -> INFO: Now checking 4 results for matching title: 'Calibrated interpretation: Confidence estimation in semantic parsing'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/64:
  -> INFO: Now checking 10 results for matching title: 'Intriguing properties of neural networks'
       -> INFO: All authors matched!
       -> WARNING: Year (2013) does not match expected year (2014)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 49/64:
  -> INFO: Now checking 8 results for matching title: 'Gemini: A family of highly capable multimodal models'
  -> WARNING: None of the 8 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gemini:+A+family+of+highly+capable+multimodal+models manually and check the results.
        -> Author(s): Gemini Team
        -> Title:     Gemini: A family of highly capable multimodal models
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 50/64:
  -> INFO: Now checking 10 results for matching title: 'Attention is all you need'
       -> INFO: All authors matched!
- Checking reference 51/64:
  -> INFO: Now checking 3 results for matching title: 'Toolgen: Unified tool retrieval and calling via generation'
       -> INFO: All authors matched!
- Checking reference 52/64:
  -> INFO: Now checking 1 results for matching title: 'Jailbreak defense in a narrow domain: Limitations of existing methods and a new transcript-classifier approach'
       -> INFO: All authors matched!
- Checking reference 53/64:
  -> INFO: Now checking 1 results for matching title: 'Dissecting adversarial robustness of multimodal lm agents'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 5)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/64:
  -> INFO: Now checking 1 results for matching title: 'Chain of attack: On the robustness of vision-language models against transfer-based adversarial attacks'
       -> INFO: All authors matched!
- Checking reference 55/64:
  -> INFO: Now checking 4 results for matching title: 'Osworld: Benchmarking multimodal agents for open-ended tasks in real computer environments'
       -> WARNING: Not all 17 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Liu, Savarese, Xiong, Zhong'
       -> WARNING: Not all 17 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Liu, Savarese, Xiong, Zhong'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 56/64:
  -> INFO: Now checking 10 results for matching title: 'Crab: Cross-environment agent benchmark for multimodal language model agents'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Torr, Ghanem'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 57/64:
  -> INFO: Now checking 4 results for matching title: 'Set-of-mark prompting unleashes extraordinary visual grounding in gpt-4v'
       -> INFO: All authors matched!
- Checking reference 58/64:
  -> INFO: Now checking 1 results for matching title: 'Ufo: A ui-focused agent for windows os interaction'
       -> INFO: All authors matched!
- Checking reference 59/64:
  -> INFO: Now checking 3 results for matching title: 'xlam: A family of large action models to empower ai agent systems'
       -> WARNING: Not all 22 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Feng, Awalgaonkar, Murthy, Xu, Niebles, Heinecke, Wang, Savarese, Xiong'
       -> WARNING: Not all 21 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Feng, Awalgaonkar, Xu, Niebles, Heinecke, Wang, Savarese, Xiong'
       -> WARNING: Not all 21 authors from the found ref. were matched (only 12)
                   Unmatched authors = 'Feng, Awalgaonkar, RitheshR., Xu, Niebles, Heinecke, Wang, Savarese, Xiong'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 60/64:
  -> INFO: Now checking 10 results for matching title: 'Attacking vision-language computer agents via pop-ups'
       -> INFO: All authors matched!
- Checking reference 61/64:
  -> INFO: Now checking 10 results for matching title: 'Agent-safetybench: Evaluating the safety of llm agents'
       -> INFO: All authors matched!
- Checking reference 62/64:
  -> INFO: Now checking 10 results for matching title: 'On evaluating adversarial robustness of large vision-language models'
       -> INFO: All authors matched!
- Checking reference 63/64:
  -> INFO: Now checking 1 results for matching title: 'Enhancing transferable adversarial attacks on vision transformers through gradient normalization scaling and highfrequency adaptation'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhu', 'Wang', 'Jin', 'Zhang', 'Chen', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Enhancing+transferable+adversarial+attacks+on+vision+transformers+through+gradient+normalization+scaling+and+highfrequency+adaptation manually and check the results.
        -> Author(s): Zhiyu Zhu, Xinyi Wang, Zhibo Jin, Jiayu Zhang, and Huaming Chen
        -> Title:     Enhancing transferable adversarial attacks on vision transformers through gradient normalization scaling and highfrequency adaptation
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 64/64:
  -> INFO: Now checking 10 results for matching title: 'Universal and transferable adversarial attacks on aligned language models'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 4: screenshot, referred to as the image patch region R ⊆{0, . . . , H −1} × {0, . . . , W −1} × {0, 1, 2}.
-> Invalid unicode use found on p. 6: tasks, one per WAA domain: p ∈P+ ⊂P used to optimise MIPs, and p ∈P−⊂P reserved for
-> Invalid unicode use found on p. 6: s ∈S+ ⊂S as screenshots for optimising and s ∈S−⊂S as screenshots for evaluating MIPs. For
-> Invalid unicode use found on p. 6: −contain screenshots of the desktop, where icons are placed at
-> Invalid unicode use found on p. 6: −contain screenshots of the social media website, where
-> Invalid unicode use found on p. 6: MIPs transfer to unseen user prompts p ∈P−, with an ASR of at least 0.3 on (p, s) ∈P−× {s},
-> Invalid unicode use found on p. 6: screenshots s ∈S−, where the ASR drops to 0.0 on (p, s) ∈{p} × S−.
-> Invalid unicode use found on p. 7: prompts p ∈P−as well as on unseen screens
-> Invalid unicode use found on p. 7: s ∈S−(shaded in grey ).
-> Invalid unicode use found on p. 7: P−×{s}
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: P−×{s}
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: P−×{s}
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: P−×{s}
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: (p, s) ∈P+ × S+. The MIPs are also evaluated on unseen pairs (p, s) ∈P−× S−, and an
-> Invalid unicode use found on p. 7: unseen screen parser g ∈G−(shaded in grey ).
-> Invalid unicode use found on p. 7: G+× P−× Sd
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: G−× P−× Sd
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: G+× P−× Sd
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: G−× P−× Sd
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: G+× P−× Ss
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: G−× P−× Ss
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: G+× P−× Ss
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: G−× P−× Ss
-> Invalid unicode use found on p. 7: −
-> Invalid unicode use found on p. 7: (p, s) ∈P−× S−. This confirms that MIPs can be crafted to generalise across diverse and previously
-> Invalid unicode use found on p. 7: that generalise well across the pairs (p, s) ∈(P+ ∪P−) × (S+ ∪S−) perform on OS agents with an
-> Invalid unicode use found on p. 7: [32] with the unseen parser g ∈G−that utilises GroundingDINO [30] and TesseractOCR [46]. This
-> Invalid unicode use found on p. 8: −.
-> Invalid unicode use found on p. 8: −
-> Invalid unicode use found on p. 8: −
-> Invalid unicode use found on p. 8: + and unseen (p, s) ∈P−×Sd
-> Invalid unicode use found on p. 8: −.
-> Invalid unicode use found on p. 8: P−× Sd
-> Invalid unicode use found on p. 8: −
-> Invalid unicode use found on p. 8: P−× Sd
-> Invalid unicode use found on p. 8: −
-> Invalid unicode use found on p. 8: −and report the ASR
-> Invalid unicode use found on p. 8: on 576 pairs (p, s) ∈(P+ ∪P−) × (S+ ∪S−), with 16 generations per pair (five stochastic outputs
-> Invalid unicode use found on p. 15: 2. The subset P−includes user prompts to evaluate whether MIPs generalise to unseen tasks.
-> Invalid unicode use found on p. 15: −of
-> Invalid unicode use found on p. 15: −of screenshots used to optimise or
-> Invalid unicode use found on p. 18: unseen user prompts p ∈P−were solely used for evaluation.
-> Invalid unicode use found on p. 18: P−
-> Invalid unicode use found on p. 19: −were solely used for evaluation.
-> Invalid unicode use found on p. 19: −
-> Invalid unicode use found on p. 20: −were solely used for evaluation.
-> Invalid unicode use found on p. 20: −
-> Invalid unicode use found on p. 22: GroundingDINO (G−) and unseen prompts and screenshots (P−× S−)
-> Invalid unicode use found on p. 22: G+× P−× Sd
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G+× P−× Sd
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G−× P+× Sd
-> Invalid unicode use found on p. 22: G−× P−× Sd
-> Invalid unicode use found on p. 22: G−× P+× Sd
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G−× P−× Sd
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G+× P−× Sd
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G+× P−× Sd
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G−× P+× Sd
-> Invalid unicode use found on p. 22: G−× P−× Sd
-> Invalid unicode use found on p. 22: G−× P+× Sd
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G−× P−× Sd
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G+× P−× Ss
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G+× P−× Ss
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G−× P+× Ss
-> Invalid unicode use found on p. 22: G−× P−× Ss
-> Invalid unicode use found on p. 22: G−× P+× Ss
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G−× P−× Ss
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G+× P−× Ss
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G+× P−× Ss
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G−× P+× Ss
-> Invalid unicode use found on p. 22: G−× P−× Ss
-> Invalid unicode use found on p. 22: G−× P+× Ss
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 22: G−× P−× Ss
-> Invalid unicode use found on p. 22: −
-> Invalid unicode use found on p. 23: P−× Sd
-> Invalid unicode use found on p. 23: −
-> Invalid unicode use found on p. 23: P−× Sd
-> Invalid unicode use found on p. 23: −
-> Invalid unicode use found on p. 23: P−× Sd
-> Invalid unicode use found on p. 23: −
-> Invalid unicode use found on p. 23: P−× Sd
-> Invalid unicode use found on p. 23: −
-> Invalid unicode use found on p. 23: P−× Sd
-> Invalid unicode use found on p. 23: −
-> Invalid unicode use found on p. 23: P−× Sd
-> Invalid unicode use found on p. 23: −
-> Invalid unicode use found on p. 23: P−× Sd
-> Invalid unicode use found on p. 23: −
-> Invalid unicode use found on p. 23: P−× Sd
-> Invalid unicode use found on p. 23: −
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 561 sentences on 11 pages -> Avg. of 57.1 sentences per page
-> Warning: Reference '24' never used in the document's text.
-> Warning: Reference '37' never used in the document's text.
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
-> Missing an abstract for reference with index 40 (Ref. ID = 41); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
-> Missing an abstract for reference with index 57 (Ref. ID = 58); Skipping LLM check...
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
-> Missing an abstract for reference with index 61 (Ref. ID = 62); Skipping LLM check...
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
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
  -> Found 1 matches in this ranking!
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
  -> Found 6 matches in this ranking!
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
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 21
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\37 MIP against Agent Malicious Image Patches\PAU_results.md
```