# Paper Analysis Utility - Results

Paper: Redefining Experts Interpretable Decomposition of Language Models.pdf


## Document Structure

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/10 Redefining Experts Interpretable Decomposition/chapter_fig.jpg]]

1) 'Introduction' -- p. 1 (ca. 1 pages)
2) 'Methodology' -- p. 2 (ca. 3 pages)
3) 'Experiments' -- p. 5 (ca. 1 pages)
4) 'Results and Analysis' -- p. 6 (ca. 3 pages)
5) 'Related Work' -- p. 9 (ca. 0 pages)
6) 'Limitations and Future Work' -- p. 9 (ca. 0 pages)
7) 'Conclusion' -- p. 9 (ca. 1 pages)
8) 'References' -- p. 10 (ca. 3 pages)
A) 'Preliminaries' -- p. 13 (ca. 0 pages)
B) 'Algorithms for Expert Neuron and Layer Identification' -- p. 13 (ca. 1 pages)
C) 'Experimental setup' -- p. 14 (ca. 4 pages)
D) 'Detailed Results' -- p. 18 (ca. 3 pages)


## Unicode Character Usage

> [!NOTE]
> *Please note that this list may contain false positives since this is feature is still in early stages of development.*

- Dashes:
	- Stats for minus signs ():
		- Valid uses: 5/11=45.45%
		- Invalid uses: 6/11=54.55%
	- Sentences with invalid dashes:
		- Lines containing invalid dashes:
		- Page 2: causally influenced by the semantic choice encoded in the preceding hidden state hn−1 ∈Rd.
		- Page 6: As Figure 3 shows, most neurons across models cluster in the narrow AUROC band of 0.50 −0.55,
		- Page 7: principal decision axis. When the model selects a token tn given context {t1 . . . tn−1}, a
		- Page 15: Lrecon = ∥W −ˆW∥F =
		- Page 15: (Wij −ˆWij)2
		- Page 16: from the set {−1, −0.5, 0, 0.1, 0.5, 0.9}. The figure illustrates how varying α influences toxicity


## References not in Bibliography

All references used in the document's (main) text were also found in the 'References' section.


## Unused References in Bibliography

> [!NOTE]
> The references listed below were listed in the 'References' section but never used in the document's main text (excluding appendices).
> -> Total = 2
> *Please note that this list may contain false positives as, e.g., the references ID (e.g., first author's lastname + year) was not correctly parsed or the in-text reference was not recognized due to linebreaks.*

- Parsed Ref. ID: 26
	- Full reference: `[26] Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov. Dropout: a simple way to prevent neural networks from overfitting. The journal of machine learning research, 15(1):1929–1958, 2014.`
- Parsed Ref. ID: 32
	- Full reference: `[32] Bertie Vidgen and Leon Derczynski. Directions in abusive language training data, a systematic review: Garbage in, garbage out. Plos one, 15(12):e0243300, 2020.`


## Frequently Referenced Authors

> [!NOTE]
> The following authors appear more than 2 times in the bibliography.
> *Please note that only the lastname and the first letter of the first name are compared for counting.*

- Apostoloff N.: 6
- Zappella L.: 6
- Zhang X.: 6
- Suau X.: 4
- Sutskever I.: 3
- Delobelle P.: 3
- Joulin A.: 3
- Zhang J.: 3
- Li J.: 3
- Liu X.: 3
- Wang Z.: 3


## Reference Checker Results

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/10 Redefining Experts Interpretable Decomposition/literature_validation_results_fig.jpg]]

References section starts on page 10.

- No link provided: $35/36=97.22\%$
- Unchecked links: $0/36=0.00\%$
- Valid links: $0/36=0.00\%$
- Invalid link: $1/36=2.78\%$
	- Invalid entries:
		=> total = 1
		- \[14\] Jigsaw and Conversation AI. Toxic comment classification challenge. https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge, 2018. Accessed: 2025-0513.
			-> Returned with status code 404!

- Different links: $1/36=2.78\%$
	- *Please note that if no link was provided, a found link will also show up in this statistic!*
	- Different links:
		=> total = 1
		- \[11\] Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Diego Rojas, Guanyu Feng, Hanlin Zhao, Hanyu Lai, Hao Yu, Hongning Wang, Jiadai Sun, Jiajie Zhang, Jiale Cheng, Jiayi Gui, Jie Tang, Jing Zhang, Juanzi Li, Lei Zhao, Lindong Wu, Lucen Zhong, Mingdao Liu, Minlie Huang, Peng Zhang, Qinkai Zheng, Rui Lu, Shuaiqi Duan, Shudan Zhang, Shulin Cao, Shuxun Yang, Weng Lam Tam, Wenyi Zhao, Xiao Liu, Xiao Xia, Xiaohan Zhang, Xiaotao Gu, Xin Lv, Xinghan Liu, Xinyi Liu, Xinyue Yang, Xixuan Song, Xunkai Zhang, Yifan An, Yifan Xu, Yilin Niu, Yuantao Yang, Yueyan Li, Yushi Bai, Yuxiao Dong, Zehan Qi, Zhaoyu Wang, Zhen Yang, Zhengxiao Du, Zhenyu Hou, and Zihan Wang. Chatglm: A family of large language models from glm-130b to glm-4 all tools, 2024.
			-> CHECK - Authors (0001, 0030, 0001, 0001, 0077, 0002, 0036, 0014, 0001, 0034) did not match found information: https://doi.org/10.48550/arXiv.2406.12793; https://doi.org/10.48550/arXiv.2406.12793

- Successful searches: $13/36=36.11\%$
- Skipped searches: $0/36=0.00\%$
- Mismatching infos: $9/36=25.00\%$
	- **Entries with mismatching author information:**
		=> total = 4
		- `[3] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners, 2020.`
			- Authors (0003, 0003) did not match found publication titled 'Language Models are Few-Shot Learners.'
		- `[11] Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Diego Rojas, Guanyu Feng, Hanlin Zhao, Hanyu Lai, Hao Yu, Hongning Wang, Jiadai Sun, Jiajie Zhang, Jiale Cheng, Jiayi Gui, Jie Tang, Jing Zhang, Juanzi Li, Lei Zhao, Lindong Wu, Lucen Zhong, Mingdao Liu, Minlie Huang, Peng Zhang, Qinkai Zheng, Rui Lu, Shuaiqi Duan, Shudan Zhang, Shulin Cao, Shuxun Yang, Weng Lam Tam, Wenyi Zhao, Xiao Liu, Xiao Xia, Xiaohan Zhang, Xiaotao Gu, Xin Lv, Xinghan Liu, Xinyi Liu, Xinyue Yang, Xixuan Song, Xunkai Zhang, Yifan An, Yifan Xu, Yilin Niu, Yuantao Yang, Yueyan Li, Yushi Bai, Yuxiao Dong, Zehan Qi, Zhaoyu Wang, Zhen Yang, Zhengxiao Du, Zhenyu Hou, and Zihan Wang. Chatglm: A family of large language models from glm-130b to glm-4 all tools, 2024.`
			- Authors (0001, 0030, 0001, 0001, 0077, 0002, 0036, 0014, 0001, 0034) did not match found information: https://doi.org/10.48550/arXiv.2406.12793
		- `[16] Nathaniel Li, Alexander Pan, Anjali Gopal, Summer Yue, Daniel Berrios, Alice Gatti, Justin D. Li, Ann-Kathrin Dombrowski, Shashwat Goel, Long Phan, Gabriel Mukobi, Nathan HelmBurger, Rassin R. Lababidi, Lennart Justen, Andrew B. Liu, Michael Chen, Isabelle Barrass, Oliver Zhang, Xiaoyuan Zhu, Rishub Tamirisa, Bhrugu Bharathi, Adam Khoja, Ariel HerbertVoss, Cort B. Breuer, Andy Zou, Mantas Mazeika, Zifan Wang, Palash Oswal, Weiran Liu, Adam A. Hunt, Justin Tienken-Harder, Kevin Y. Shih, Kemper Talley, John Guan, Russell Kaplan, Ian Steneker, David Campbell, Brad Jokubaitis, Alex Levinson, Jean Wang, William Qian, K. Karmakar, Steven Basart, Stephen Fitz, Mindy Levine, P. Kumaraguru, U. Tupakula, Vijay Varadharajan, Yan Shoshitaishvili, Jimmy Ba, K. Esvelt, Alexandr Wang, and Dan Hendrycks. The wmdp benchmark: Measuring and reducing malicious use with unlearning. ArXiv, abs/2403.03218, 2024.`
			- Authors (Helm-Burger, Herbert-Voss) did not match found publication titled 'The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning'
		- `[27] Xavier Suau, Pieter Delobelle, Katherine Metcalf, Armand Joulin, Nicholas Apostoloff, Luca Zappella, and Pau Rodríguez. Whispering experts: neural interventions for toxicity mitigation in language models. In Proceedings of the 41st International Conference on Machine Learning, ICML’24. JMLR.org, 2024.`
			- Authors (Rodr'iguez) did not match found publication titled 'Whispering Experts: Neural Interventions for Toxicity Mitigation in Language Models'
	- **Entries with mismatching years (where the difference is = 1 year):**
		=> total = 5
		- `[2] David Bau, Jun-Yan Zhu, Hendrik Strobelt, Bolei Zhou, Joshua B Tenenbaum, Antonio Torralba, and William T Freeman. Gan dissection: Visualizing and understanding generative adversarial networks. arXiv preprint arXiv:1811.10597, 2019.`
			- Year (2018) does not match expected year (2019)
		- `[4] Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. Unsupervised cross-lingual representation learning at scale. arXiv preprint arXiv:1911.02116, 2020.`
			- Year (2019) does not match expected year (2020)
		- `[6] Xavier Suau Cuadros, Luca Zappella, and Nicholas Apostoloff. Self-conditioning pre-trained language models. In International Conference on Machine Learning, pages 4455–4473. PMLR, 2022.`
			- Year (2021) does not match expected year (2022)
		- `[7] Sumanth Dathathri, Andrea Madotto, Janice Lan, Jane Hung, Eric Frank, Piero Molino, Jason Yosinski, and Rosanne Liu. Plug and play language models: A simple approach to controlled text generation. In International Conference on Learning Representations (ICLR), 2020.`
			- Year (2019) does not match expected year (2020)
		- `[30] Xavier Suau, Luca Zappella, and Nicholas Apostoloff. Self-conditioning pre-trained language models. arXiv preprint arXiv:2203.XXXXX, 2022.`
			- Year (2021) does not match expected year (2022)
- No entry found: $14/36=38.89\%$
	- Unfound entries:
		=> total = 14
		- \[5\] Xavier Suau Cuadros, Pieter Delobelle, Rin Metcalf Susa, Armand Joulin, Nick Apostoloff, Luca Zappella, and Pau Rodriguez Lopez. Whispering experts: Toxicity mitigation in pre-trained language models by dampening expert neurons. In ICML, 2024.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[9\] Robert M. French. Catastrophic interference in connectionist networks: can it be predicted, can it be prevented? In Proceedings of the 7th International Conference on Neural Information Processing Systems, NIPS’93, page 1176–1177, San Francisco, CA, USA, 1993. Morgan Kaufmann Publishers Inc.
			-> WARNING: No results were found through the dblp search! | WARNING: None of the 28 results matched the expected title!
		- \[12\] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, and Abhinav Pandey. The llama 3 herd of models, 2024.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[13\] Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. Mistral 7b, 2023.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[14\] Jigsaw and Conversation AI. Toxic comment classification challenge. https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge, 2018. Accessed: 2025-0513.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[15\] Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov, and Luke Zettlemoyer. BART: Denoising sequence-to-sequence pretraining for natural language generation, translation, and comprehension. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault, editors, Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 7871–7880, Online, July 2020. Association for Computational Linguistics.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[18\] Shervin Minaee, Tomas Mikolov, Narjes Nikzad, Meysam Chenaghlu, Richard Socher, Xavier Amatriain, and Jianfeng Gao. Large language models: A survey, 2025.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[19\] Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad Saqib, Saeed Anwar, Muhammad Usman, Naveed Akhtar, Nick Barnes, and Ajmal Mian. A comprehensive overview of large language models, 2024.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[23\] Oscar Skean, Md Rifat Arefin, Dan Zhao, Niket Patel, Jalal Naghiyev, Yann LeCun, and Ravid Shwartz-Ziv. Layer by layer: Uncovering hidden representations in language models, 2025.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[28\] Xavier Suau, Pieter Delobelle, Katherine Metcalf, Armand Joulin, Nicholas Apostoloff, Luca Zappella, and Pau Rodríguez. Whispering experts: Neural interventions for toxicity mitigation in language models, 2024.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[31\] Rheeya Uppaal, Apratim Dey, Yiting He, Yiqiao Zhong, and Junjie Hu. Model editing as a robust and denoised variant of dpo: A case study on toxicity, 2025.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!
		- ==\[33\] Weijia Xu, Xing Niu, and Marine Carpuat. Controlling toxicity in neural machine translation. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 4245–4256, 2020.==
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- ==\[35\] Xiang Zhang, Xuehai Wei, Xian Zhang, and Xue Zhang. Adversarial attacks and defenses in toxicity detection: A survey. In Proceedings of the 2020 International Joint Conference on Neural Networks (IJCNN), pages 1–8. IEEE, 2020.==
			-> WARNING: No results were found through the dblp search! | WARNING: No results were found through the dblp search!
		- \[36\] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, Yifan Du, Chen Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, Peiyu Liu, Jian-Yun Nie, and Ji-Rong Wen. A survey of large language models, 2025. Appendix A
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!



## References Support for Statements

> [!NOTE]
> *Please note that only references with a retrieved abstract can be checked here.*
> *You can find a complete list, including which sentences were skipped due to a missing abstract, at the bottom of the report.*

**Sentences with references to papers that are thematically related / relevant but REFUTE the statement they are referenced in:**
- None

**Sentences with references to papers that are thematically unrelated / irrelevant to the statement they are referenced in:**
- None



---
## Outlet Rankings

### Outlet Ranking Results

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/10 Redefining Experts Interpretable Decomposition/ranking_results_fig.jpg]]

### References and Their Rankings

- arXiv
	- References literatures count from this outlet: 8
- International Conference on Machine Learning
	- Parsed as: International Conference on Machine Learning
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 2
- IEEE Conference on Computer Vision and Pattern Recognition
	- Parsed as: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- Proceedings of the ACM Web Conference 2023, WWW ’23, page 1118–1129, New York, NY
	- References literatures count from this outlet: 1
- North American Association for Computational Linguistics
	- Parsed as: Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A
	- References literatures count from this outlet: 1
- Empirical Methods in Natural Language Processing
	- Parsed as: Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- PLoS One
	- Parsed as: Plos one
	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = 2.5
	- References literatures count from this outlet: 1
- International Conference on Machine Learning
	- Parsed as: Proceedings of the 41st International Conference on Machine Learning
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- The journal of machine learning research
	- References literatures count from this outlet: 1
- Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki, editors, Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
	- References literatures count from this outlet: 1
- Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, editors, Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing,
	- References literatures count from this outlet: 1
- Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault, editors, Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics,
	- References literatures count from this outlet: 1
- Findings
	- References literatures count from this outlet: 1
- International Conference on Learning Representations
	- Parsed as: International Conference on Learning Representations
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- International Conference on Machine Learning
	- Parsed as: ICML
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- IEEE International Joint Conference on Neural Networks
	- Parsed as: Proceedings of the 2020 International Joint Conference on Neural Networks
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = B
	- References literatures count from this outlet: 1



---
## Extracted References

- **Number 1:**
	- Ref. ID: *1*
	- Authors: *David Bau, Bolei Zhou, Aditya Khosla, Aude Oliva, and Antonio Torralba*
	- Normalized Authors: `['Bau D.', 'Zhou B.', 'Khosla A.', 'Oliva A.', 'Torralba A.']`
	- Authors contain 'et al.': *False*
	- Title: *Network dissection: Quantifying interpretability of deep visual representations*
	- Year: *2017*
	- Outlet: *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 2:**
	- Ref. ID: *2*
	- Authors: *David Bau, Jun-Yan Zhu, Hendrik Strobelt, Bolei Zhou, Joshua B Tenenbaum, Antonio Torralba, and William T Freeman*
	- Normalized Authors: `['Bau D.', 'Zhu J.', 'Strobelt H.', 'Zhou B.', 'Tenenbaum J.', 'Torralba A.', 'Freeman W.']`
	- Authors contain 'et al.': *False*
	- Title: *Gan dissection: Visualizing and understanding generative adversarial networks*
	- Year: *2019*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *CHECK - Year (2018) does not match expected year (2019)*
- **Number 3:**
	- Ref. ID: *3*
	- Authors: *Tom B  Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M  Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei*
	- Normalized Authors: `['Brown T.', 'Mann B.', 'Ryder N.', 'Subbiah M.', 'Kaplan J.', 'Dhariwal P.', 'Neelakantan A.', 'Shyam P.', 'Sastry G.', 'Askell A.', 'Agarwal S.', 'Herbert-Voss A.', 'Krueger G.', 'Henighan T.', 'Child R.', 'Ramesh A.', 'Ziegler D.', 'Wu J.', 'Winter C.', 'Hesse C.', 'Chen M.', 'Sigler E.', 'Litwin M.', 'Gray S.', 'Chess B.', 'Clark J.', 'Berner C.', 'McCandlish S.', 'Radford A.', 'Sutskever I.', 'Amodei D.']`
	- Authors contain 'et al.': *False*
	- Title: *Language models are few-shot learners.*
	- Year: *2020*
	- Outlet: **
	- Link: **
	- **Valid?**: *CHECK - Authors (0003, 0003) did not match found publication titled 'Language Models are Few-Shot Learners.'*
- **Number 4:**
	- Ref. ID: *4*
	- Authors: *Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov*
	- Normalized Authors: `['Conneau A.', 'Khandelwal K.', 'Goyal N.', 'Chaudhary V.', 'Wenzek G.', 'Guzmán F.', 'Grave E.', 'Ott M.', 'Zettlemoyer L.', 'Stoyanov V.']`
	- Authors contain 'et al.': *False*
	- Title: *Unsupervised cross-lingual representation learning at scale*
	- Year: *2020*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *CHECK - Year (2019) does not match expected year (2020)*
- **Number 5:**
	- Ref. ID: *5*
	- Authors: *Xavier Suau Cuadros, Pieter Delobelle, Rin Metcalf Susa, Armand Joulin, Nick Apostoloff, Luca Zappella, and Pau Rodriguez Lopez*
	- Normalized Authors: `['Cuadros X.', 'Delobelle P.', 'Susa R.', 'Joulin A.', 'Apostoloff N.', 'Zappella L.', 'Lopez P.']`
	- Authors contain 'et al.': *False*
	- Title: *Whispering experts: Toxicity mitigation in pre-trained language models by dampening expert neurons*
	- Year: *2024*
	- Outlet: *ICML*
	- Link: **
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 6:**
	- Ref. ID: *6*
	- Authors: *Xavier Suau Cuadros, Luca Zappella, and Nicholas Apostoloff*
	- Normalized Authors: `['Cuadros X.', 'Zappella L.', 'Apostoloff N.']`
	- Authors contain 'et al.': *False*
	- Title: *Self-conditioning pre-trained language models*
	- Year: *2022*
	- Outlet: *International Conference on Machine Learning*
	- Link: **
	- **Valid?**: *CHECK - Year (2021) does not match expected year (2022)*
- **Number 7:**
	- Ref. ID: *7*
	- Authors: *Sumanth Dathathri, Andrea Madotto, Janice Lan, Jane Hung, Eric Frank, Piero Molino, Jason Yosinski, and Rosanne Liu*
	- Normalized Authors: `['Dathathri S.', 'Madotto A.', 'Lan J.', 'Hung J.', 'Frank E.', 'Molino P.', 'Yosinski J.', 'Liu R.']`
	- Authors contain 'et al.': *False*
	- Title: *Plug and play language models: A simple approach to controlled text generation*
	- Year: *2020*
	- Outlet: *International Conference on Learning Representations*
	- Link: **
	- **Valid?**: *CHECK - Year (2019) does not match expected year (2020)*
- **Number 8:**
	- Ref. ID: *8*
	- Authors: *Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova*
	- Normalized Authors: `['Devlin J.', 'Chang M.', 'Lee K.', 'Toutanova K.']`
	- Authors contain 'et al.': *False*
	- Title: *Bert: Pre-training of deep bidirectional transformers for language understanding*
	- Year: *2019*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 9:**
	- Ref. ID: *9*
	- Authors: *Robert M  French*
	- Normalized Authors: `['French R.']`
	- Authors contain 'et al.': *False*
	- Title: *Catastrophic interference in connectionist networks: can it be predicted, can it be prevented? In Proceedings of the 7th International Conference on Neural Information Processing Systems, NIPS’93, page 1176–1177, San Francisco, CA, USA.*
	- Year: *1993*
	- Outlet: **
	- Link: **
	- **Valid?**: *WARNING: No results were found through the dblp search! | WARNING: None of the 28 results matched the expected title!*
- **Number 10:**
	- Ref. ID: *10*
	- Authors: *Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, and Noah A  Smith*
	- Normalized Authors: `['Gehman S.', 'Gururangan S.', 'Sap M.', 'Choi Y.', 'Smith N.']`
	- Authors contain 'et al.': *False*
	- Title: *Realtoxicityprompts: Evaluating neural toxic degeneration in language models*
	- Year: *2020*
	- Outlet: *Findings*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 11:**
	- Ref. ID: *11*
	- Authors: *Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Diego Rojas, Guanyu Feng, Hanlin Zhao, Hanyu Lai, Hao Yu, Hongning Wang, Jiadai Sun, Jiajie Zhang, Jiale Cheng, Jiayi Gui, Jie Tang, Jing Zhang, Juanzi Li, Lei Zhao, Lindong Wu, Lucen Zhong, Mingdao Liu, Minlie Huang, Peng Zhang, Qinkai Zheng, Rui Lu, Shuaiqi Duan, Shudan Zhang, Shulin Cao, Shuxun Yang, Weng Lam Tam, Wenyi Zhao, Xiao Liu, Xiao Xia, Xiaohan Zhang, Xiaotao Gu, Xin Lv, Xinghan Liu, Xinyi Liu, Xinyue Yang, Xixuan Song, Xunkai Zhang, Yifan An, Yifan Xu, Yilin Niu, Yuantao Yang, Yueyan Li, Yushi Bai, Yuxiao Dong, Zehan Qi, Zhaoyu Wang, Zhen Yang, Zhengxiao Du, Zhenyu Hou, and Zihan Wang*
	- Normalized Authors: `['GLM T.', 'Zeng A.', 'Xu B.', 'Wang B.', 'Zhang C.', 'Yin D.', 'Rojas D.', 'Feng G.', 'Zhao H.', 'Lai H.', 'Yu H.', 'Wang H.', 'Sun J.', 'Zhang J.', 'Cheng J.', 'Gui J.', 'Tang J.', 'Zhang J.', 'Li J.', 'Zhao L.', 'Wu L.', 'Zhong L.', 'Liu M.', 'Huang M.', 'Zhang P.', 'Zheng Q.', 'Lu R.', 'Duan S.', 'Zhang S.', 'Cao S.', 'Yang S.', 'Tam W.', 'Zhao W.', 'Liu X.', 'Xia X.', 'Zhang X.', 'Gu X.', 'Lv X.', 'Liu X.', 'Liu X.', 'Yang X.', 'Song X.', 'Zhang X.', 'An Y.', 'Xu Y.', 'Niu Y.', 'Yang Y.', 'Li Y.', 'Bai Y.', 'Dong Y.', 'Qi Z.', 'Wang Z.', 'Yang Z.', 'Du Z.', 'Hou Z.', 'Wang Z.']`
	- Authors contain 'et al.': *False*
	- Title: *Chatglm: A family of large language models from glm-130b to glm-4 all tools.*
	- Year: *2024*
	- Outlet: **
	- Link: *https://doi.org/10.48550/arXiv.2406.12793*
	- **Valid?**: *CHECK - Authors (0001, 0030, 0001, 0001, 0077, 0002, 0036, 0014, 0001, 0034) did not match found information: https://doi.org/10.48550/arXiv.2406.12793*
- **Number 12:**
	- Ref. ID: *12*
	- Authors: *Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, and Abhinav Pandey*
	- Normalized Authors: `['Grattafiori A.', 'Dubey A.', 'Jauhri A.', 'Pandey A.']`
	- Authors contain 'et al.': *False*
	- Title: *The llama 3 herd of models.*
	- Year: *2024*
	- Outlet: **
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 13:**
	- Ref. ID: *13*
	- Authors: *Albert Q  Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed*
	- Normalized Authors: `['Jiang A.', 'Sablayrolles A.', 'Mensch A.', 'Bamford C.', 'Chaplot D.', 'Casas D.', 'Bressand F.', 'Lengyel G.', 'Lample G.', 'Saulnier L.', 'Lavaud L.', 'Lachaux M.', 'Stock P.', 'Scao T.', 'Lavril T.', 'Wang T.', 'Lacroix T.', 'Sayed W.']`
	- Authors contain 'et al.': *False*
	- Title: *Mistral 7b.*
	- Year: *2023*
	- Outlet: **
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 14:**
	- Ref. ID: *14*
	- Authors: *Jigsaw and Conversation AI*
	- Normalized Authors: `['Jigsaw', 'AI C.']`
	- Authors contain 'et al.': *False*
	- Title: *Toxic comment classification challenge*
	- Year: *0*
	- Outlet: **
	- Link: *https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge,*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 15:**
	- Ref. ID: *15*
	- Authors: *Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov, and Luke Zettlemoyer*
	- Normalized Authors: `['Lewis M.', 'Liu Y.', 'Goyal N.', 'Ghazvininejad M.', 'Mohamed A.', 'Levy O.', 'Stoyanov V.', 'Zettlemoyer L.']`
	- Authors contain 'et al.': *False*
	- Title: *BART: Denoising sequence-to-sequence pretraining for natural language generation, translation, and comprehension*
	- Year: *2020*
	- Outlet: *Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault, editors, Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics,*
	- Link: **
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 16:**
	- Ref. ID: *16*
	- Authors: *Nathaniel Li, Alexander Pan, Anjali Gopal, Summer Yue, Daniel Berrios, Alice Gatti, Justin D  Li, Ann-Kathrin Dombrowski, Shashwat Goel, Long Phan, Gabriel Mukobi, Nathan HelmBurger, Rassin R  Lababidi, Lennart Justen, Andrew B  Liu, Michael Chen, Isabelle Barrass, Oliver Zhang, Xiaoyuan Zhu, Rishub Tamirisa, Bhrugu Bharathi, Adam Khoja, Ariel HerbertVoss, Cort B  Breuer, Andy Zou, Mantas Mazeika, Zifan Wang, Palash Oswal, Weiran Liu, Adam A  Hunt, Justin Tienken-Harder, Kevin Y  Shih, Kemper Talley, John Guan, Russell Kaplan, Ian Steneker, David Campbell, Brad Jokubaitis, Alex Levinson, Jean Wang, William Qian, K  Karmakar, Steven Basart, Stephen Fitz, Mindy Levine, P  Kumaraguru, U  Tupakula, Vijay Varadharajan, Yan Shoshitaishvili, Jimmy Ba, K  Esvelt, Alexandr Wang, and Dan Hendrycks*
	- Normalized Authors: `['Li N.', 'Pan A.', 'Gopal A.', 'Yue S.', 'Berrios D.', 'Gatti A.', 'Li J.', 'Dombrowski A.', 'Goel S.', 'Phan L.', 'Mukobi G.', 'HelmBurger N.', 'Lababidi R.', 'Justen L.', 'Liu A.', 'Chen M.', 'Barrass I.', 'Zhang O.', 'Zhu X.', 'Tamirisa R.', 'Bharathi B.', 'Khoja A.', 'HerbertVoss A.', 'Breuer C.', 'Zou A.', 'Mazeika M.', 'Wang Z.', 'Oswal P.', 'Liu W.', 'Hunt A.', 'Tienken-Harder J.', 'Shih K.', 'Talley K.', 'Guan J.', 'Kaplan R.', 'Steneker I.', 'Campbell D.', 'Jokubaitis B.', 'Levinson A.', 'Wang J.', 'Qian W.', 'Karmakar K.', 'Basart S.', 'Fitz S.', 'Levine M.', 'Kumaraguru P.', 'Tupakula U.', 'Varadharajan V.', 'Shoshitaishvili Y.', 'Ba J.', 'Esvelt K.', 'Wang A.', 'Hendrycks D.']`
	- Authors contain 'et al.': *False*
	- Title: *The wmdp benchmark: Measuring and reducing malicious use with unlearning*
	- Year: *2024*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *CHECK - Authors (Helm-Burger, Herbert-Voss) did not match found publication titled 'The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning'*
- **Number 17:**
	- Ref. ID: *17*
	- Authors: *Junyu Lu, Bo Xu, Xiaokun Zhang, Changrong Min, Liang Yang, and Hongfei Lin*
	- Normalized Authors: `['Lu J.', 'Xu B.', 'Zhang X.', 'Min C.', 'Yang L.', 'Lin H.']`
	- Authors contain 'et al.': *False*
	- Title: *Facilitating fine-grained detection of Chinese toxic language: Hierarchical taxonomy, resources, and benchmarks*
	- Year: *2023*
	- Outlet: *Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki, editors, Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 18:**
	- Ref. ID: *18*
	- Authors: *Shervin Minaee, Tomas Mikolov, Narjes Nikzad, Meysam Chenaghlu, Richard Socher, Xavier Amatriain, and Jianfeng Gao*
	- Normalized Authors: `['Minaee S.', 'Mikolov T.', 'Nikzad N.', 'Chenaghlu M.', 'Socher R.', 'Amatriain X.', 'Gao J.']`
	- Authors contain 'et al.': *False*
	- Title: *Large language models: A survey.*
	- Year: *2025*
	- Outlet: **
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 19:**
	- Ref. ID: *19*
	- Authors: *Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad Saqib, Saeed Anwar, Muhammad Usman, Naveed Akhtar, Nick Barnes, and Ajmal Mian*
	- Normalized Authors: `['Naveed H.', 'Khan A.', 'Qiu S.', 'Saqib M.', 'Anwar S.', 'Usman M.', 'Akhtar N.', 'Barnes N.', 'Mian A.']`
	- Authors contain 'et al.': *False*
	- Title: *A comprehensive overview of large language models.*
	- Year: *2024*
	- Outlet: **
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 20:**
	- Ref. ID: *20*
	- Authors: *Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Christian Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al*
	- Normalized Authors: `['Ouyang L.', 'Wu J.', 'Jiang X.', 'Almeida D.', 'Wainwright C.', 'Mishkin P.', 'Zhang C.', 'Agarwal S.', 'Slama K.', 'Ray A.']`
	- Authors contain 'et al.': *True*
	- Title: *Training language models to follow instructions with human feedback*
	- Year: *2022*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 21:**
	- Ref. ID: *21*
	- Authors: *Alec Radford, Rafal Jozefowicz, and Ilya Sutskever*
	- Normalized Authors: `['Radford A.', 'Jozefowicz R.', 'Sutskever I.']`
	- Authors contain 'et al.': *False*
	- Title: *Learning to generate reviews and discovering sentiment*
	- Year: *2017*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 22:**
	- Ref. ID: *22*
	- Authors: *Shashwat Singh, Shauli Ravfogel, Jonathan Herzig, Roee Aharoni, Ryan Cotterell, and Ponnurangam Kumaraguru*
	- Normalized Authors: `['Singh S.', 'Ravfogel S.', 'Herzig J.', 'Aharoni R.', 'Cotterell R.', 'Kumaraguru P.']`
	- Authors contain 'et al.': *False*
	- Title: *Representation surgery: Theory and practice of affine steering*
	- Year: *2024*
	- Outlet: *International Conference on Machine Learning*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 23:**
	- Ref. ID: *23*
	- Authors: *Oscar Skean, Md Rifat Arefin, Dan Zhao, Niket Patel, Jalal Naghiyev, Yann LeCun, and Ravid Shwartz-Ziv*
	- Normalized Authors: `['Skean O.', 'Arefin M.', 'Zhao D.', 'Patel N.', 'Naghiyev J.', 'LeCun Y.', 'Shwartz-Ziv R.']`
	- Authors contain 'et al.': *False*
	- Title: *Layer by layer: Uncovering hidden representations in language models.*
	- Year: *2025*
	- Outlet: **
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 24:**
	- Ref. ID: *24*
	- Authors: *Aseem Srivastava, Smriti Joshi, Tanmoy Chakraborty, and Md Shad Akhtar*
	- Normalized Authors: `['Srivastava A.', 'Joshi S.', 'Chakraborty T.', 'Akhtar M.']`
	- Authors contain 'et al.': *False*
	- Title: *Knowledge planning in large language models for domain-aligned counseling summarization*
	- Year: *2024*
	- Outlet: *Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, editors, Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing,*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 25:**
	- Ref. ID: *25*
	- Authors: *Aseem Srivastava, Ishan Pandey, Md Shad Akhtar, and Tanmoy Chakraborty*
	- Normalized Authors: `['Srivastava A.', 'Pandey I.', 'Akhtar M.', 'Chakraborty T.']`
	- Authors contain 'et al.': *False*
	- Title: *Response-act guided reinforced dialogue generation for mental health counseling*
	- Year: *2023*
	- Outlet: *Proceedings of the ACM Web Conference 2023, WWW ’23, page 1118–1129, New York, NY*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 26:**
	- Ref. ID: *26*
	- Authors: *Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov*
	- Normalized Authors: `['Srivastava N.', 'Hinton G.', 'Krizhevsky A.', 'Sutskever I.', 'Salakhutdinov R.']`
	- Authors contain 'et al.': *False*
	- Title: *Dropout: a simple way to prevent neural networks from overfitting*
	- Year: *2014*
	- Outlet: *The journal of machine learning research*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 27:**
	- Ref. ID: *27*
	- Authors: *Xavier Suau, Pieter Delobelle, Katherine Metcalf, Armand Joulin, Nicholas Apostoloff, Luca Zappella, and Pau Rodríguez*
	- Normalized Authors: `['Suau X.', 'Delobelle P.', 'Metcalf K.', 'Joulin A.', 'Apostoloff N.', 'Zappella L.', 'Rodríguez P.']`
	- Authors contain 'et al.': *False*
	- Title: *Whispering experts: neural interventions for toxicity mitigation in language models*
	- Year: *2024*
	- Outlet: *Proceedings of the 41st International Conference on Machine Learning*
	- Link: **
	- **Valid?**: *CHECK - Authors (Rodr'iguez) did not match found publication titled 'Whispering Experts: Neural Interventions for Toxicity Mitigation in Language Models'*
- **Number 28:**
	- Ref. ID: *28*
	- Authors: *Xavier Suau, Pieter Delobelle, Katherine Metcalf, Armand Joulin, Nicholas Apostoloff, Luca Zappella, and Pau Rodríguez*
	- Normalized Authors: `['Suau X.', 'Delobelle P.', 'Metcalf K.', 'Joulin A.', 'Apostoloff N.', 'Zappella L.', 'Rodríguez P.']`
	- Authors contain 'et al.': *False*
	- Title: *Whispering experts: Neural interventions for toxicity mitigation in language models.*
	- Year: *2024*
	- Outlet: **
	- Link: **
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 29:**
	- Ref. ID: *29*
	- Authors: *Xavier Suau, Luca Zappella, and Nicholas Apostoloff*
	- Normalized Authors: `['Suau X.', 'Zappella L.', 'Apostoloff N.']`
	- Authors contain 'et al.': *False*
	- Title: *Self-conditioning pre-trained language models*
	- Year: *2021*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 30:**
	- Ref. ID: *30*
	- Authors: *Xavier Suau, Luca Zappella, and Nicholas Apostoloff*
	- Normalized Authors: `['Suau X.', 'Zappella L.', 'Apostoloff N.']`
	- Authors contain 'et al.': *False*
	- Title: *Self-conditioning pre-trained language models*
	- Year: *2022*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *CHECK - Year (2021) does not match expected year (2022)*
- **Number 31:**
	- Ref. ID: *31*
	- Authors: *Rheeya Uppaal, Apratim Dey, Yiting He, Yiqiao Zhong, and Junjie Hu*
	- Normalized Authors: `['Uppaal R.', 'Dey A.', 'He Y.', 'Zhong Y.', 'Hu J.']`
	- Authors contain 'et al.': *False*
	- Title: *Model editing as a robust and denoised variant of dpo: A case study on toxicity.*
	- Year: *2025*
	- Outlet: **
	- Link: **
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 32:**
	- Ref. ID: *32*
	- Authors: *Bertie Vidgen and Leon Derczynski*
	- Normalized Authors: `['Vidgen B.', 'Derczynski L.']`
	- Authors contain 'et al.': *False*
	- Title: *Directions in abusive language training data, a systematic review: Garbage in, garbage out*
	- Year: *2020*
	- Outlet: *Plos one*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 33:**
	- Ref. ID: *33*
	- Authors: *Weijia Xu, Xing Niu, and Marine Carpuat*
	- Normalized Authors: `['Xu W.', 'Niu X.', 'Carpuat M.']`
	- Authors contain 'et al.': *False*
	- Title: *Controlling toxicity in neural machine translation*
	- Year: *2020*
	- Outlet: *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing*
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 34:**
	- Ref. ID: *34*
	- Authors: *Kevin Yang and Dan Klein*
	- Normalized Authors: `['Yang K.', 'Klein D.']`
	- Authors contain 'et al.': *False*
	- Title: *Fudge: Controlled text generation with future discriminators*
	- Year: *2021*
	- Outlet: *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 35:**
	- Ref. ID: *35*
	- Authors: *Xiang Zhang, Xuehai Wei, Xian Zhang, and Xue Zhang*
	- Normalized Authors: `['Zhang X.', 'Wei X.', 'Zhang X.', 'Zhang X.']`
	- Authors contain 'et al.': *False*
	- Title: *Adversarial attacks and defenses in toxicity detection: A survey*
	- Year: *2020*
	- Outlet: *Proceedings of the 2020 International Joint Conference on Neural Networks*
	- Link: **
	- **Valid?**: *WARNING: No results were found through the dblp search! | WARNING: No results were found through the dblp search!*
- **Number 36:**
	- Ref. ID: *36*
	- Authors: *Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, Yifan Du, Chen Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, Peiyu Liu, Jian-Yun Nie, and Ji-Rong Wen*
	- Normalized Authors: `['Zhao W.', 'Zhou K.', 'Li J.', 'Tang T.', 'Wang X.', 'Hou Y.', 'Min Y.', 'Zhang B.', 'Zhang J.', 'Dong Z.', 'Du Y.', 'Yang C.', 'Chen Y.', 'Chen Z.', 'Jiang J.', 'Ren R.', 'Li Y.', 'Tang X.', 'Liu Z.', 'Liu P.', 'Nie J.', 'Wen J.']`
	- Authors contain 'et al.': *False*
	- Title: *A survey of large language models.*
	- Year: *2025*
	- Outlet: **
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*



---
## Full List of Reference Support Check

**Sentences with references to papers that are thematically related / relevant papers but REFUTE the statement they are referenced in:**
- None

**Sentences with references to papers that are thematically related / relevant papers that we had not enough info about to determine the stance on the statement they are referenced in:**
- '*Prior work has primarily focused on neuron-level interventions, where specific neurons, often termed concept experts, are identified and manipulated based on their activation in response to toxic inputs [5, 6, 21]*'
	- This flag is for the paper with Ref. ID = 6
- '*Works have also proposed PPLM, which uses the product of experts framework to guide text generation without retraining [7]*'
	- This flag is for the paper with Ref. ID = 7
- '*A prominent line of work [16, 22, 31] focuses on steering the hidden representations of LMs to mitigate toxic or biased generations*'
	- This flag is for the paper with Ref. ID = 16
- '*DAMP, a less aggressive variant that uniformly scales down activations with a parameter α [29, 27]*'
	- This flag is for the paper with Ref. ID = 27
- '*Other works expanded this by introducing expert neurons for arbitrary concepts, but are still limited by the inability to capture distributed semantics [30]*'
	- This flag is for the paper with Ref. ID = 30

**Sentences with references to papers that are thematically related / relevant papers that SUPPORT the statement they are referenced in:**
- '*Conneau et al [4] demonstrated that multilingual models capture shared semantic spaces across languages*'
	- This flag is for the paper with Ref. ID = 4
- '*AURA, a data-driven intervention where expert activations are damped in proportion to their AUROC-derived expertise, using the Gini coefficient to modulate the scaling factor [27]*'
	- This flag is for the paper with Ref. ID = 27
- '*Also, a self-conditioning approach has been proposed, identifying expert neurons directly within the PLMs, which eliminates the need for external components [30]*'
	- This flag is for the paper with Ref. ID = 30


**Sentences with references to papers that seem thematically unrelated / irrelevant:**
- '*Layer-wise representations have gained attention [23, 4, 8] for multilingual and domain-specific toxicity detection*'
	- This flag is for the paper with Ref. ID = 4
- '*Aura [27] The alleged ringleader of a group of young men involved in the recent assaults on a number of women, is seen during an*'
	- This flag is for the paper with Ref. ID = 27
- '*Damp [30] The alleged ringleader of a An hour that looks like an image without\nThis has become a matter of the*'
	- This flag is for the paper with Ref. ID = 30


**Sentences with references to papers that we didn't have an abstract for to check against:**
- '*Early work focused on identifying individual neurons as concept detectors, drawing inspiration from discoveries in image processing [1, 2]*'
	- This flag is for the paper with Ref. ID = 1
- '*Early work focused on identifying individual neurons as concept detectors, drawing inspiration from discoveries in image processing [1, 2]*'
	- This flag is for the paper with Ref. ID = 2
- '*1 Introduction The rise of large language models has brought remarkable advancements across tasks involving human-like generation [19, 36, 18, 3, 24, 25]*'
	- This flag is for the paper with Ref. ID = 3
- '*Prior work has primarily focused on neuron-level interventions, where specific neurons, often termed concept experts, are identified and manipulated based on their activation in response to toxic inputs [5, 6, 21]*'
	- This flag is for the paper with Ref. ID = 5
- '*However, neuron activations are often stochastic and brittle, leading to inconsistent behavior across contexts [5], which we also show in our analysis on the way*'
	- This flag is for the paper with Ref. ID = 5
- '*5) used in [5]*'
	- This flag is for the paper with Ref. ID = 5
- '*(a) Architectural Baselines: For English benchmarks, we use BERT [8], BART [15], Llama-3*'
	- This flag is for the paper with Ref. ID = 8
- '*Layer-wise representations have gained attention [23, 4, 8] for multilingual and domain-specific toxicity detection*'
	- This flag is for the paper with Ref. ID = 8
- '*Similarly, Devlin et al [8] showed that different layers in BERT encode varying levels of semantic and syntactic information, supporting the idea that layer-wise analysis can generalize better across languages and domains*'
	- This flag is for the paper with Ref. ID = 8
- '*Furthermore, interventions at early layers propagate disruption downstream, resulting in catastrophic forgetting and significant degradation in language modeling performance [9]*'
	- This flag is for the paper with Ref. ID = 9
- '*Most existing interventions conflate these two, suppressing both types of activations, which inadvertently damages the model’s ability to recognize toxicity, leading to catastrophic forgetting and degraded language performance [9]*'
	- This flag is for the paper with Ref. ID = 9
- '*To assess if a given intervention effectively reduces toxic generation without degrading fluency, we adopt an established evaluation framework [10]*'
	- This flag is for the paper with Ref. ID = 10
- '*For the Chinese benchmark, we use their corresponding Chinese-pretrained variants: GLM-4 [11]*'
	- This flag is for the paper with Ref. ID = 11
- '*1 [12], and Mistral [13]*'
	- This flag is for the paper with Ref. ID = 12
- '*1 [12], and Mistral [13]*'
	- This flag is for the paper with Ref. ID = 13
- '*activations merely reflect unstable correlations? ▶RQ2: Can layer-wise or structural representations capture toxicity more robustly, particularly across multilingual and specialized domains? ▶RQ3: Can we uncover interpretable components beyond just layers and neurons that contribute to toxic generation, aiming to make black box models more understandable? In our work, we conduct a comprehensive analysis using two toxicity detection datasets: Jigsaw (English) [14] and ToxiCN (Chinese) [17]*'
	- This flag is for the paper with Ref. ID = 14
- '*With our approach, EigenShift, we evaluate it on two benchmark datasets that focus on toxicity-related concepts: the Jigsaw dataset [14] and the ToxiCN dataset [17]*'
	- This flag is for the paper with Ref. ID = 14
- '*(a) Architectural Baselines: For English benchmarks, we use BERT [8], BART [15], Llama-3*'
	- This flag is for the paper with Ref. ID = 15
- '*activations merely reflect unstable correlations? ▶RQ2: Can layer-wise or structural representations capture toxicity more robustly, particularly across multilingual and specialized domains? ▶RQ3: Can we uncover interpretable components beyond just layers and neurons that contribute to toxic generation, aiming to make black box models more understandable? In our work, we conduct a comprehensive analysis using two toxicity detection datasets: Jigsaw (English) [14] and ToxiCN (Chinese) [17]*'
	- This flag is for the paper with Ref. ID = 17
- '*With our approach, EigenShift, we evaluate it on two benchmark datasets that focus on toxicity-related concepts: the Jigsaw dataset [14] and the ToxiCN dataset [17]*'
	- This flag is for the paper with Ref. ID = 17
- '*1 Introduction The rise of large language models has brought remarkable advancements across tasks involving human-like generation [19, 36, 18, 3, 24, 25]*'
	- This flag is for the paper with Ref. ID = 18
- '*1 Introduction The rise of large language models has brought remarkable advancements across tasks involving human-like generation [19, 36, 18, 3, 24, 25]*'
	- This flag is for the paper with Ref. ID = 19
- '*Toxicity detection and mitigation techniques like fine-tuning with human feedback [20], postprocessing filters [33], and adversarial training [35] have been long studied*'
	- This flag is for the paper with Ref. ID = 20
- '*Prior work has primarily focused on neuron-level interventions, where specific neurons, often termed concept experts, are identified and manipulated based on their activation in response to toxic inputs [5, 6, 21]*'
	- This flag is for the paper with Ref. ID = 21
- '*Previous works have identified sentiment neurons in LSTMs showing specific neurons influence sentiment in text generation [21]*'
	- This flag is for the paper with Ref. ID = 21
- '*A prominent line of work [16, 22, 31] focuses on steering the hidden representations of LMs to mitigate toxic or biased generations*'
	- This flag is for the paper with Ref. ID = 22
- '*For instance, Singh et al, [22] formally investigate such steering functions and propose least-squares optimal affine transformations under various constraints, demonstrating their empirical effectiveness in reducing toxic and biased outputs*'
	- This flag is for the paper with Ref. ID = 22
- '*Layer-wise representations have gained attention [23, 4, 8] for multilingual and domain-specific toxicity detection*'
	- This flag is for the paper with Ref. ID = 23
- '*1 Introduction The rise of large language models has brought remarkable advancements across tasks involving human-like generation [19, 36, 18, 3, 24, 25]*'
	- This flag is for the paper with Ref. ID = 24
- '*1 Introduction The rise of large language models has brought remarkable advancements across tasks involving human-like generation [19, 36, 18, 3, 24, 25]*'
	- This flag is for the paper with Ref. ID = 25
- '*Neuron-centric toxicity mitigation, such as Suau et al [28], attempts to identify and deactivate toxic neurons, reducing harmful outputs while preserving model performance*'
	- This flag is for the paper with Ref. ID = 28
- '*(b) Intervention Baselines: To benchmark intervention effectiveness in mitigating toxic generation, we re-implement three key methods grounded in recent literature: DetZero[29], where expert activations are replaced by the mean maximum activation for concept c to induce targeted suppression*'
	- This flag is for the paper with Ref. ID = 29
- '*DetZero, the intervention provided in work [29] that sets expert activations to zero*'
	- This flag is for the paper with Ref. ID = 29
- '*DAMP, a less aggressive variant that uniformly scales down activations with a parameter α [29, 27]*'
	- This flag is for the paper with Ref. ID = 29
- '*Det-0 [29] The alleged ringleader of a O´gainedLAYNN ufffddph u200bps saysNNbaOoceOOO iU*'
	- This flag is for the paper with Ref. ID = 29
- '*A prominent line of work [16, 22, 31] focuses on steering the hidden representations of LMs to mitigate toxic or biased generations*'
	- This flag is for the paper with Ref. ID = 31
- '*Toxicity detection and mitigation techniques like fine-tuning with human feedback [20], postprocessing filters [33], and adversarial training [35] have been long studied*'
	- This flag is for the paper with Ref. ID = 33
- '*Similarly, authors have developed FUDGE, which adjusts output probabilities using a discriminator [34]*'
	- This flag is for the paper with Ref. ID = 34
- '*Toxicity detection and mitigation techniques like fine-tuning with human feedback [20], postprocessing filters [33], and adversarial training [35] have been long studied*'
	- This flag is for the paper with Ref. ID = 35
- '*1 Introduction The rise of large language models has brought remarkable advancements across tasks involving human-like generation [19, 36, 18, 3, 24, 25]*'
	- This flag is for the paper with Ref. ID = 36

