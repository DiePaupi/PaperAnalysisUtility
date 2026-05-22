# Paper Analysis Utility - Results

Paper: PANTHER Generative Pretraining Beyond Language.pdf


## Document Structure

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/12 PANTHER/chapter_fig.jpg]]

1) 'Introduction' -- p. 1 (ca. 2 pages)
2) 'Related Work' -- p. 3 (ca. 0 pages)
3) 'PANTHER' -- p. 3 (ca. 3 pages)
4) 'Experiments' -- p. 6 (ca. 4 pages)
5) 'Conclusions' -- p. 10 (ca. 0 pages)
6) 'References' -- p. 10 (ca. 3 pages)
A) 'Notation Table' -- p. 13 (ca. 1 pages)
B) 'Implementation Details' -- p. 14 (ca. 1 pages)
C) 'Transferability of PANTHER' -- p. 15 (ca. 0 pages)
D) 'Ablation Experiments' -- p. 15 (ca. 0 pages)


## Unicode Character Usage

> [!NOTE]
> *Please note that this list may contain false positives since this is feature is still in early stages of development.*

- Dashes:
	- Stats for minus signs ():
		- Valid uses: 1/7=14.29%
		- Invalid uses: 6/7=85.71%
	- Sentences with invalid dashes:
		- Lines containing invalid dashes:
		- Page 3: −log Prθ(xt | x<t, xprofile)
		- Page 5: LCL = −
		- Page 5: exp(−∥ei −ej∥2/τ)
		- Page 5: k∈U\{i} exp(−∥ei −ek∥2/τ),
		- Page 5: L = (1 −λ)Lgen
		- Page 6: positives for users with naturally varied transaction patterns: ∆u,m = Pu(m)−µu
- Non-breaking spaces:
	- Stats:
  	- Valid uses: 0/3=0.00%
  	- Invalid uses: 3/3=100.00%
	- Lines containing invalid non-breaking spaces:
		- Page 3: User Profile Contrastive
		- Page 3: Age, City,  Payment


## References not in Bibliography

> [!NOTE]
> The sentences listed below contain references that were not found in the 'References' section.
> *Please note that this list may contain false positives as, e.g., the content of a normal bracket might have been mistaken for a reference, or a natural reference (Authorname in text and year in brackets) might have been mismatched.*

-  For live transactions, we compute risk scores through feature fusion: Pr(y = 1|·) = gϕ  ψ(cnew) | {z } context , fenc(X[L-100:L] u ) | {z } recent patterns , eu |{z} long-term profile , ∆(ˆxL+1, xnew) | {z } behavior deviation  , (3) where the function gϕ represents a general downstream discriminative model, which can take various flexible forms depending on specific tasks or use cases, ψ(·) embeds transaction context features, fenc encodes the last 100 transactions via TextCNN [23], and ∆measures the distance between predicted and observed behaviors


## Unused References in Bibliography

All references stated in the 'References' section were also used at least once in the document's (main) text.


## Frequently Referenced Authors

> [!NOTE]
> The following authors appear more than 2 times in the bibliography.
> *Please note that only the lastname and the first letter of the first name are compared for counting.*

- Sun F.: 3


## Reference Checker Results

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/12 PANTHER/literature_validation_results_fig.jpg]]

References section starts on page 10.

- No link provided: $23/29=79.31\%$
- Unchecked links: $4/29=13.79\%$
- Valid links: $0/29=0.00\%$
- Invalid link: $2/29=6.90\%$
	- Invalid entries:
		=> total = 2
		- \[13\] Balazs Hidasi, Alexandros Karatzoglou, Linas Baltrunas, and Domonkos Tikk. Session-based recommendations with recurrent neural networks. In Proceedings of the 4th International Conference on Learning Representations (ICLR), 2016. URL https://arxiv.org/abs/1511.06939.
			-> Returned with status code 404!
		- \[25\] Eric Altman et al. Credit card transactions (cct) dataset, 2019. URL https://www.kaggle.com/datasets/ealtman2019/credit-card-transactions. Accessed: 2025-01-31.
			-> Returned with status code 404!

- Different links: $0/29=0.00\%$

- Successful searches: $8/29=27.59\%$
- Skipped searches: $0/29=0.00\%$
- Mismatching infos: $9/29=31.03\%$
	- **Entries with mismatching author information:**
		=> total = 8
		- `[2] Jacob Devlin. Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805, 2018.`
			- Authors (Chang, Lee, Toutanova) did not match found publication titled 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding'
		- `[4] Mark Chen, Alec Radford, Rewon Child, Jeffrey Wu, Heewoo Jun, David Luan, and Ilya Sutskever. Generative pretraining from pixels. In International conference on machine learning, pages 1691–1703. PMLR, 2020.`
			- Authors (Dhariwal) did not match found publication titled 'Generative Pretraining From Pixels'
		- `[5] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick. Masked autoencoders are scalable vision learners. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 16000–16009, 2022.`
			- Authors (Doll'ar) did not match found publication titled 'Masked Autoencoders Are Scalable Vision Learners'
		- `[6] Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang, Rui Li, Xuan Cao, Leon Gao, Zhaojie Gong, Fangda Gu, Michael He, et al. Actions speak louder than words: Trillion-parameter sequential transducers for generative recommendations. arXiv preprint arXiv:2402.17152, 2024.`
			- Authors (Shi) did not match found publication titled 'Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations'
		- `[9] Bin Liu, Chenxu Zhu, Guilin Li, Weinan Zhang, Jincai Lai, Ruiming Tang, Xiuqiang He, and Zhenguo Li. Autofis: Automatic feature interaction selection in factorization models for click-through rate prediction. Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, pages 2636–2645, 2020.`
			- Authors (Yu) did not match found publication titled 'AutoFIS: Automatic Feature Interaction Selection in Factorization Models for Click-Through Rate Prediction'
		- `[10] Guorui Zhou, Na Mou, Ying Fan, Qi Pi, Weijie Cai, Yang Liu, Han Zhu, Xiao Ma, Yanghui Yan, Junqi Jin, and Kun Gai. Deep interest evolution network for click-through rate prediction. Proceedings of the AAAI Conference on Artificial Intelligence, 33(1):5941–5948, 2019.`
			- Authors (Bian) did not match found publication titled 'Deep Interest Evolution Network for Click-Through Rate Prediction'
		- `[12] Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang, Rui Li, Xuan Cao, Leon Gao, Zhaojie Gong, Fangda Gu, Michael He, et al. Actions speak louder than words: Trillion-parameter sequential transducers for generative recommendations. arXiv preprint arXiv:2402.17152, 2024.`
			- Authors (Shi) did not match found publication titled 'Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations'
		- `[24] A Vaswani. Attention is all you need. Advances in Neural Information Processing Systems, 2017.`
			- Authors (Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin) did not match found publication titled 'Attention is All you Need'
	- **Entries with mismatching years (where the difference is = 1 year):**
		=> total = 1
		- `[29] Inkit Padhi, Yair Schiff, Igor Melnyk, Mattia Rigotti, Youssef Mroueh, Pierre Dognin, Jerret Ross, Ravi Nair, and Erik Altman. Tabular transformers for modeling multivariate time series. In ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 3565–3569. IEEE, 2021. Appendix A`
			- Year (2020) does not match expected year (2021)
- No entry found: $12/29=41.38\%$
	- Unfound entries:
		=> total = 12
		- \[1\] Enterprise Apps Today. Global digital payment platforms user statistics (2022). https://www.enterpriseappstoday.com/stats/online-payment-statistics.html, 2022.Accessed: 2025-01-23.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: None of the 43 results matched the expected title!
		- \[3\] Yu Sun, Shuohuan Wang, Yukun Li, Shikun Feng, Hao Tian, Hua Wu, and Haifeng Wang. Ernie 2.0: A continual pre-training framework for language understanding. In Proceedings of the AAAI conference on artificial intelligence, volume 34, pages 8968–8975, 2020.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: None of the 2 results matched the expected title!
		- \[13\] Balazs Hidasi, Alexandros Karatzoglou, Linas Baltrunas, and Domonkos Tikk. Session-based recommendations with recurrent neural networks. In Proceedings of the 4th International Conference on Learning Representations (ICLR), 2016. URL https://arxiv.org/abs/1511.06939.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: None of the 1 results matched the expected title!
		- \[16\] Fei Sun, Jun Liu, and Jian Wu. Bert4rec: Sequential recommendation with bidirectional encoder representations from transformers. In Proceedings of the 28th ACM International Conference on Information and Knowledge Management (CIKM), pages 1441–1450, 2019. doi: 10.1145/3357384.3357895.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: None of the 133 results matched the expected title!
		- \[17\] Shubham Rajput, Mingxuan Chen, and Fei Sun. Tiger: Token-based generative retrieval for sequential recommendation. In Advances in Neural Information Processing Systems (NeurIPS), pages 789–798, 2023. doi: 10.48550/arXiv.2306.01234.
			-> WARNING: None of the 5 results matched the expected title! | WARNING: No results were found through the dblp search!
		- ==\[18\] Majid Zolghadr, Mohsen Jamali, and Jiawei Zhang. Diffurecsys: Diffusion-based generative modeling for sequential recommendation. Proceedings of the ACM Web Conference (WWW), pages 2156–2165, 2024. doi: 10.1145/3545678.3557899.==
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- ==\[21\] Humberto Acevedo-Viloria, Juan Martinez, and Maria Garcia. Relational graph convolutional networks for financial fraud detection. IEEE Transactions on Knowledge and Data Engineering, 33(7):1357–1370, 2021. doi: 10.1109/TKDE.2020.3007655.==
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[22\] Hao Wang, Wei Zhang, and Fei Sun. Heterogeneous graph neural networks for user behavior prediction. In Proceedings of the 28th ACM International Conference on Information and Knowledge Management (CIKM), pages 765–774, 2019. doi: 10.1145/3357384.3357907.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[25\] Eric Altman et al. Credit card transactions (cct) dataset, 2019. URL https://www.kaggle.com/datasets/ealtman2019/credit-card-transactions. Accessed: 2025-01-31.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[26\] AI Lab et al. Mbd-mini dataset, 2020. URL https://huggingface.co/datasets/ai-lab/MBD-mini. Accessed: 2025-01-31.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[27\] GroupLens et al. Movielens-1m dataset, 2000. URL https://grouplens.org/datasets/movielens/1m/. Accessed: 2025-01-31.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- \[28\] Yelp. Yelp dataset, 2014. URL https://business.yelp.com/data/resources/open-dataset/.
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

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/12 PANTHER/ranking_results_fig.jpg]]

### References and Their Rankings

- arXiv
	- References literatures count from this outlet: 4
- Advances in Neural Information Processing Systems (was NIPS)
	- Parsed as: Advances in Neural Information Processing Systems
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 2
- ACM International Conference on Information and Knowledge Management
	- Parsed as: Proceedings of the 28th ACM International Conference on Information and Knowledge Management
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A
	- References literatures count from this outlet: 2
- Empirical Methods in Natural Language Processing
	- Parsed as: Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- IEEE Transactions on Knowledge and Data Engineering,
	- References literatures count from this outlet: 1
- STATISTICAL SCIENCE
	- Parsed as: Statistical Science
	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = 3.3
	- References literatures count from this outlet: 1
- International World Wide Web Conference
	- Parsed as: Proceedings of the ACM Web Conference
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- IEEE International Conference on Data Mining
	- Parsed as: IEEE International Conference on Data Mining
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = C
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- ACM International Conference on Web Search and Data Mining
	- Parsed as: Proceedings of the 11th ACM International Conference on Web Search and Data Mining
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A
	- References literatures count from this outlet: 1
- International Conference on Learning Representations
	- Parsed as: Proceedings of the 4th International Conference on Learning Representations
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- ACM International Conference on Recommender Systems
	- Parsed as: Proceedings of the 10th ACM Conference on Recommender Systems
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A
	- References literatures count from this outlet: 1
- National Conference of the American Association for Artificial Intelligence
	- Parsed as: Proceedings of the AAAI Conference on Artificial Intelligence
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- ACM International Conference on Knowledge Discovery and Data Mining
	- Parsed as: Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- Proceedings of the ADKDD’17
	- References literatures count from this outlet: 1
- International Joint Conference on Artificial Intelligence
	- Parsed as: Proceedings of the 26th International Joint Conference on Artificial Intelligence
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- IEEE Conference on Computer Vision and Pattern Recognition
	- Parsed as: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- International Conference on Machine Learning
	- Parsed as: International conference on machine learning
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- National Conference of the American Association for Artificial Intelligence
	- Parsed as: 0: A continual pre-training framework for language understanding In Proceedings of the AAAI conference on artificial intelligence, volume 34
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- IEEE International Conference on Acoustics, Speech and Signal Processing
	- Parsed as: ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = 4603
	- References literatures count from this outlet: 1



---
## Extracted References

- **Number 1:**
	- Ref. ID: *1*
	- Authors: *Enterprise Apps Today*
	- Normalized Authors: `['Today E.']`
	- Authors contain 'et al.': *False*
	- Title: *Global digital payment platforms user statistics (.*
	- Year: *2022*
	- Outlet: **
	- Link: *https://www.enterpriseappstoday.com/stats/online-payment-statistics.html,*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: None of the 43 results matched the expected title!*
- **Number 2:**
	- Ref. ID: *2*
	- Authors: *Jacob Devlin*
	- Normalized Authors: `['Devlin J.']`
	- Authors contain 'et al.': *False*
	- Title: *Bert: Pre-training of deep bidirectional transformers for language understanding*
	- Year: *2018*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *CHECK - Authors (Chang, Lee, Toutanova) did not match found publication titled 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding'*
- **Number 3:**
	- Ref. ID: *3*
	- Authors: *Yu Sun, Shuohuan Wang, Yukun Li, Shikun Feng, Hao Tian, Hua Wu, and Haifeng Wang*
	- Normalized Authors: `['Sun Y.', 'Wang S.', 'Li Y.', 'Feng S.', 'Tian H.', 'Wu H.', 'Wang H.']`
	- Authors contain 'et al.': *False*
	- Title: *Ernie 2*
	- Year: *2020*
	- Outlet: *0: A continual pre-training framework for language understanding In Proceedings of the AAAI conference on artificial intelligence, volume 34*
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: None of the 2 results matched the expected title!*
- **Number 4:**
	- Ref. ID: *4*
	- Authors: *Mark Chen, Alec Radford, Rewon Child, Jeffrey Wu, Heewoo Jun, David Luan, and Ilya Sutskever*
	- Normalized Authors: `['Chen M.', 'Radford A.', 'Child R.', 'Wu J.', 'Jun H.', 'Luan D.', 'Sutskever I.']`
	- Authors contain 'et al.': *False*
	- Title: *Generative pretraining from pixels*
	- Year: *2020*
	- Outlet: *International conference on machine learning*
	- Link: **
	- **Valid?**: *CHECK - Authors (Dhariwal) did not match found publication titled 'Generative Pretraining From Pixels'*
- **Number 5:**
	- Ref. ID: *5*
	- Authors: *Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick*
	- Normalized Authors: `['He K.', 'Chen X.', 'Xie S.', 'Li Y.', 'Dollár P.', 'Girshick R.']`
	- Authors contain 'et al.': *False*
	- Title: *Masked autoencoders are scalable vision learners*
	- Year: *2022*
	- Outlet: *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*
	- Link: **
	- **Valid?**: *CHECK - Authors (Doll'ar) did not match found publication titled 'Masked Autoencoders Are Scalable Vision Learners'*
- **Number 6:**
	- Ref. ID: *6*
	- Authors: *Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang, Rui Li, Xuan Cao, Leon Gao, Zhaojie Gong, Fangda Gu, Michael He, et al*
	- Normalized Authors: `['Zhai J.', 'Liao L.', 'Liu X.', 'Wang Y.', 'Li R.', 'Cao X.', 'Gao L.', 'Gong Z.', 'Gu F.', 'He M.']`
	- Authors contain 'et al.': *True*
	- Title: *Actions speak louder than words: Trillion-parameter sequential transducers for generative recommendations*
	- Year: *2024*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *CHECK - Authors (Shi) did not match found publication titled 'Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations'*
- **Number 7:**
	- Ref. ID: *7*
	- Authors: *Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, and Xiuqiang He*
	- Normalized Authors: `['Guo H.', 'Tang R.', 'Ye Y.', 'Li Z.', 'He X.']`
	- Authors contain 'et al.': *False*
	- Title: *Deepfm: A factorization-machine based neural network for ctr prediction*
	- Year: *2017*
	- Outlet: *Proceedings of the 26th International Joint Conference on Artificial Intelligence*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 8:**
	- Ref. ID: *8*
	- Authors: *Ruoxi Wang, Bin Fu, Gang Fu, and Mingliang Wang*
	- Normalized Authors: `['Wang R.', 'Fu B.', 'Fu G.', 'Wang M.']`
	- Authors contain 'et al.': *False*
	- Title: *Deep & cross network for ad click predictions*
	- Year: *2017*
	- Outlet: *Proceedings of the ADKDD’17*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 9:**
	- Ref. ID: *9*
	- Authors: *Bin Liu, Chenxu Zhu, Guilin Li, Weinan Zhang, Jincai Lai, Ruiming Tang, Xiuqiang He, and Zhenguo Li*
	- Normalized Authors: `['Liu B.', 'Zhu C.', 'Li G.', 'Zhang W.', 'Lai J.', 'Tang R.', 'He X.', 'Li Z.']`
	- Authors contain 'et al.': *False*
	- Title: *Autofis: Automatic feature interaction selection in factorization models for click-through rate prediction*
	- Year: *2020*
	- Outlet: *Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*
	- Link: **
	- **Valid?**: *CHECK - Authors (Yu) did not match found publication titled 'AutoFIS: Automatic Feature Interaction Selection in Factorization Models for Click-Through Rate Prediction'*
- **Number 10:**
	- Ref. ID: *10*
	- Authors: *Guorui Zhou, Na Mou, Ying Fan, Qi Pi, Weijie Cai, Yang Liu, Han Zhu, Xiao Ma, Yanghui Yan, Junqi Jin, and Kun Gai*
	- Normalized Authors: `['Zhou G.', 'Mou N.', 'Fan Y.', 'Pi Q.', 'Cai W.', 'Liu Y.', 'Zhu H.', 'Ma X.', 'Yan Y.', 'Jin J.', 'Gai K.']`
	- Authors contain 'et al.': *False*
	- Title: *Deep interest evolution network for click-through rate prediction*
	- Year: *2019*
	- Outlet: *Proceedings of the AAAI Conference on Artificial Intelligence*
	- Link: **
	- **Valid?**: *CHECK - Authors (Bian) did not match found publication titled 'Deep Interest Evolution Network for Click-Through Rate Prediction'*
- **Number 11:**
	- Ref. ID: *11*
	- Authors: *Paul Covington, Jay Adams, and Emre Sargin*
	- Normalized Authors: `['Covington P.', 'Adams J.', 'Sargin E.']`
	- Authors contain 'et al.': *False*
	- Title: *Deep neural networks for youtube recommendations*
	- Year: *2016*
	- Outlet: *Proceedings of the 10th ACM Conference on Recommender Systems*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 12:**
	- Ref. ID: *12*
	- Authors: *Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang, Rui Li, Xuan Cao, Leon Gao, Zhaojie Gong, Fangda Gu, Michael He, et al*
	- Normalized Authors: `['Zhai J.', 'Liao L.', 'Liu X.', 'Wang Y.', 'Li R.', 'Cao X.', 'Gao L.', 'Gong Z.', 'Gu F.', 'He M.']`
	- Authors contain 'et al.': *True*
	- Title: *Actions speak louder than words: Trillion-parameter sequential transducers for generative recommendations*
	- Year: *2024*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *CHECK - Authors (Shi) did not match found publication titled 'Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations'*
- **Number 13:**
	- Ref. ID: *13*
	- Authors: *Balazs Hidasi, Alexandros Karatzoglou, Linas Baltrunas, and Domonkos Tikk*
	- Normalized Authors: `['Hidasi B.', 'Karatzoglou A.', 'Baltrunas L.', 'Tikk D.']`
	- Authors contain 'et al.': *False*
	- Title: *Session-based recommendations with recurrent neural networks*
	- Year: *2016*
	- Outlet: *Proceedings of the 4th International Conference on Learning Representations*
	- Link: *https://arxiv.org/abs/1511.06939.*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: None of the 1 results matched the expected title!*
- **Number 14:**
	- Ref. ID: *14*
	- Authors: *Jiaxi Tang and Ke Wang*
	- Normalized Authors: `['Tang J.', 'Wang K.']`
	- Authors contain 'et al.': *False*
	- Title: *Personalized top-n sequential recommendation via convolutional sequence embedding*
	- Year: *2018*
	- Outlet: *Proceedings of the 11th ACM International Conference on Web Search and Data Mining*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 15:**
	- Ref. ID: *15*
	- Authors: *Wang-Cheng Kang and Julian McAuley*
	- Normalized Authors: `['Kang W.', 'McAuley J.']`
	- Authors contain 'et al.': *False*
	- Title: *Self-attentive sequential recommendation*
	- Year: *2018*
	- Outlet: *IEEE International Conference on Data Mining*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 16:**
	- Ref. ID: *16*
	- Authors: *Fei Sun, Jun Liu, and Jian Wu*
	- Normalized Authors: `['Sun F.', 'Liu J.', 'Wu J.']`
	- Authors contain 'et al.': *False*
	- Title: *Bert4rec: Sequential recommendation with bidirectional encoder representations from transformers*
	- Year: *2019*
	- Outlet: *Proceedings of the 28th ACM International Conference on Information and Knowledge Management*
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: None of the 133 results matched the expected title!*
- **Number 17:**
	- Ref. ID: *17*
	- Authors: *Shubham Rajput, Mingxuan Chen, and Fei Sun*
	- Normalized Authors: `['Rajput S.', 'Chen M.', 'Sun F.']`
	- Authors contain 'et al.': *False*
	- Title: *Tiger: Token-based generative retrieval for sequential recommendation*
	- Year: *2023*
	- Outlet: *Advances in Neural Information Processing Systems*
	- Link: **
	- **Valid?**: *WARNING: None of the 5 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 18:**
	- Ref. ID: *18*
	- Authors: *Majid Zolghadr, Mohsen Jamali, and Jiawei Zhang*
	- Normalized Authors: `['Zolghadr M.', 'Jamali M.', 'Zhang J.']`
	- Authors contain 'et al.': *False*
	- Title: *Diffurecsys: Diffusion-based generative modeling for sequential recommendation*
	- Year: *2024*
	- Outlet: *Proceedings of the ACM Web Conference*
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 19:**
	- Ref. ID: *19*
	- Authors: *Junyi Chen, Lu Chi, Bingyue Peng, and Zehuan Yuan*
	- Normalized Authors: `['Chen J.', 'Chi L.', 'Peng B.', 'Yuan Z.']`
	- Authors contain 'et al.': *False*
	- Title: *Hllm: Enhancing sequential recommendations via hierarchical large language models for item and user modeling*
	- Year: *2024*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 20:**
	- Ref. ID: *20*
	- Authors: *Richard J Bolton and David J Hand*
	- Normalized Authors: `['Bolton R.', 'Hand D.']`
	- Authors contain 'et al.': *False*
	- Title: *Statistical fraud detection: A review*
	- Year: *2002*
	- Outlet: *Statistical Science*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 21:**
	- Ref. ID: *21*
	- Authors: *Humberto Acevedo-Viloria, Juan Martinez, and Maria Garcia*
	- Normalized Authors: `['Acevedo-Viloria H.', 'Martinez J.', 'Garcia M.']`
	- Authors contain 'et al.': *False*
	- Title: *Relational graph convolutional networks for financial fraud detection*
	- Year: *2020*
	- Outlet: *IEEE Transactions on Knowledge and Data Engineering,*
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 22:**
	- Ref. ID: *22*
	- Authors: *Hao Wang, Wei Zhang, and Fei Sun*
	- Normalized Authors: `['Wang H.', 'Zhang W.', 'Sun F.']`
	- Authors contain 'et al.': *False*
	- Title: *Heterogeneous graph neural networks for user behavior prediction*
	- Year: *2019*
	- Outlet: *Proceedings of the 28th ACM International Conference on Information and Knowledge Management*
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 23:**
	- Ref. ID: *23*
	- Authors: *Yoon Kim*
	- Normalized Authors: `['Kim Y.']`
	- Authors contain 'et al.': *False*
	- Title: *Convolutional neural networks for sentence classification*
	- Year: *2014*
	- Outlet: *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 24:**
	- Ref. ID: *24*
	- Authors: *A Vaswani*
	- Normalized Authors: `['Vaswani A.']`
	- Authors contain 'et al.': *False*
	- Title: *Attention is all you need*
	- Year: *2017*
	- Outlet: *Advances in Neural Information Processing Systems*
	- Link: **
	- **Valid?**: *CHECK - Authors (Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin) did not match found publication titled 'Attention is All you Need'*
- **Number 25:**
	- Ref. ID: *25*
	- Authors: *Eric Altman et al*
	- Normalized Authors: `['Altman E.']`
	- Authors contain 'et al.': *True*
	- Title: *Credit card transactions (cct) dataset.*
	- Year: *2019*
	- Outlet: **
	- Link: *https://www.kaggle.com/datasets/ealtman2019/credit-card-transactions.*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 26:**
	- Ref. ID: *26*
	- Authors: *AI Lab et al*
	- Normalized Authors: `['Lab A.']`
	- Authors contain 'et al.': *True*
	- Title: *Mbd-mini dataset.*
	- Year: *2020*
	- Outlet: **
	- Link: *https://huggingface.co/datasets/ai-lab/MBD-mini.*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 27:**
	- Ref. ID: *27*
	- Authors: *GroupLens et al*
	- Normalized Authors: `['GroupLens']`
	- Authors contain 'et al.': *True*
	- Title: *Movielens-1m dataset.*
	- Year: *2000*
	- Outlet: **
	- Link: *https://grouplens.org/datasets/movielens/1m/.*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 28:**
	- Ref. ID: *28*
	- Authors: *Yelp*
	- Normalized Authors: `['Yelp']`
	- Authors contain 'et al.': *False*
	- Title: *Yelp dataset.*
	- Year: *2014*
	- Outlet: **
	- Link: *https://business.yelp.com/data/resources/open-dataset/.*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 29:**
	- Ref. ID: *29*
	- Authors: *Inkit Padhi, Yair Schiff, Igor Melnyk, Mattia Rigotti, Youssef Mroueh, Pierre Dognin, Jerret Ross, Ravi Nair, and Erik Altman*
	- Normalized Authors: `['Padhi I.', 'Schiff Y.', 'Melnyk I.', 'Rigotti M.', 'Mroueh Y.', 'Dognin P.', 'Ross J.', 'Nair R.', 'Altman E.']`
	- Authors contain 'et al.': *False*
	- Title: *Tabular transformers for modeling multivariate time series*
	- Year: *2021*
	- Outlet: *ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing*
	- Link: **
	- **Valid?**: *CHECK - Year (2020) does not match expected year (2021)*



---
## Full List of Reference Support Check

**Sentences with references to papers that are thematically related / relevant papers but REFUTE the statement they are referenced in:**
- None

**Sentences with references to papers that are thematically related / relevant papers that we had not enough info about to determine the stance on the statement they are referenced in:**
- '*Subway Canteen Taxi Cinema Popcorn Parking Clothes Canteen Coffee Necessities Subway Canteen Taxi Daily Commute  Daily Commute Scenic Area Visit Mall Shopping Historical Payment  Behavior Sequence 8:00 12:00 18:00 19:00 19:15 21:00 8:00 12:00 18:00 10:00 12:00 14:00 16:00 Figure 1: Illustration of the periodic pattern of user behaviors Recent advances in self-supervised pretraining have transformed representation learning in language, vision, and recommendation [2–6]*'
	- This flag is for the paper with Ref. ID = 2
- '*Subway Canteen Taxi Cinema Popcorn Parking Clothes Canteen Coffee Necessities Subway Canteen Taxi Daily Commute  Daily Commute Scenic Area Visit Mall Shopping Historical Payment  Behavior Sequence 8:00 12:00 18:00 19:00 19:15 21:00 8:00 12:00 18:00 10:00 12:00 14:00 16:00 Figure 1: Illustration of the periodic pattern of user behaviors Recent advances in self-supervised pretraining have transformed representation learning in language, vision, and recommendation [2–6]*'
	- This flag is for the paper with Ref. ID = 6
- '*, DeepFM [7], DCN [8], AutoFIS [9], DIEN [10]), rely primarily on supervised discriminative models for transaction-level classification*'
	- This flag is for the paper with Ref. ID = 10
- '*Although sequential recommenders increasingly adopt generative objectives, they typically use generation as an end task (next-item prediction) (for example HSTU [12]) rather than as a pretraining mechanism to compress user knowledge into transferable representations*'
	- This flag is for the paper with Ref. ID = 12
- '*We benchmark PANTHER against several strong baseline models, including Transformer [24], SASRec [15], and HSTU [12]*'
	- This flag is for the paper with Ref. ID = 24
- '*9% over the TabBERT-MLP ([29]) baseline (Table 4), enhancing the model’s effectiveness in detecting fraudulent activity*'
	- This flag is for the paper with Ref. ID = 29

**Sentences with references to papers that are thematically related / relevant papers that SUPPORT the statement they are referenced in:**
- '*Subway Canteen Taxi Cinema Popcorn Parking Clothes Canteen Coffee Necessities Subway Canteen Taxi Daily Commute  Daily Commute Scenic Area Visit Mall Shopping Historical Payment  Behavior Sequence 8:00 12:00 18:00 19:00 19:15 21:00 8:00 12:00 18:00 10:00 12:00 14:00 16:00 Figure 1: Illustration of the periodic pattern of user behaviors Recent advances in self-supervised pretraining have transformed representation learning in language, vision, and recommendation [2–6]*'
	- This flag is for the paper with Ref. ID = 5
- '*, DeepFM [7], DCN [8], AutoFIS [9], DIEN [10]), rely primarily on supervised discriminative models for transaction-level classification*'
	- This flag is for the paper with Ref. ID = 9
- '*Generative sequential models, such as HSTU [12], TIGER [17], DiffuRecSys [18], and HLLM [19] have further advanced the field by modeling complex temporal dependencies and uncertainties*'
	- This flag is for the paper with Ref. ID = 12


**Sentences with references to papers that seem thematically unrelated / irrelevant:**
- '*We benchmark PANTHER against several strong baseline models, including Transformer [24], SASRec [15], and HSTU [12]*'
	- This flag is for the paper with Ref. ID = 12


**Sentences with references to papers that we didn't have an abstract for to check against:**
- '*1 Introduction Online payment platforms, such as WeChat Pay, Alipay, and PayPal, process billions of transactions daily, supported by critical applications like fraud detection, credit risk assessment, and personalized marketing [1]*'
	- This flag is for the paper with Ref. ID = 1
- '*Subway Canteen Taxi Cinema Popcorn Parking Clothes Canteen Coffee Necessities Subway Canteen Taxi Daily Commute  Daily Commute Scenic Area Visit Mall Shopping Historical Payment  Behavior Sequence 8:00 12:00 18:00 19:00 19:15 21:00 8:00 12:00 18:00 10:00 12:00 14:00 16:00 Figure 1: Illustration of the periodic pattern of user behaviors Recent advances in self-supervised pretraining have transformed representation learning in language, vision, and recommendation [2–6]*'
	- This flag is for the paper with Ref. ID = 3
- '*Subway Canteen Taxi Cinema Popcorn Parking Clothes Canteen Coffee Necessities Subway Canteen Taxi Daily Commute  Daily Commute Scenic Area Visit Mall Shopping Historical Payment  Behavior Sequence 8:00 12:00 18:00 19:00 19:15 21:00 8:00 12:00 18:00 10:00 12:00 14:00 16:00 Figure 1: Illustration of the periodic pattern of user behaviors Recent advances in self-supervised pretraining have transformed representation learning in language, vision, and recommendation [2–6]*'
	- This flag is for the paper with Ref. ID = 4
- '*, DeepFM [7], DCN [8], AutoFIS [9], DIEN [10]), rely primarily on supervised discriminative models for transaction-level classification*'
	- This flag is for the paper with Ref. ID = 7
- '*2 Hybrid Real-Time Fraud Detection ›We evaluate PANTHER’s fraud detection performance through a 10-day full-traffic A/B test on WeChat Pay’s production system, using the DeepFM model [7] as the baseline*'
	- This flag is for the paper with Ref. ID = 7
- '*, DeepFM [7], DCN [8], AutoFIS [9], DIEN [10]), rely primarily on supervised discriminative models for transaction-level classification*'
	- This flag is for the paper with Ref. ID = 8
- '*At billion-user scale they face four persistent limitations: (1) label scarcity—positive examples are too few to span the combinatorial feature space; (2) overfitting to high-dimensional categories—models memorize spurious co-occurrences rather than meaningful risk patterns; (3) latency-driven truncation of long histories—weakening the ability to leverage long-range behavior; and (4) static embeddings—biased toward frequent labels and brittle under cold-start and long-tail distributions [11]*'
	- This flag is for the paper with Ref. ID = 11
- '*, GRU4Rec [13], Caser [14]) to recent transformer-based approaches (e*'
	- This flag is for the paper with Ref. ID = 13
- '*, GRU4Rec [13], Caser [14]) to recent transformer-based approaches (e*'
	- This flag is for the paper with Ref. ID = 14
- '*, SASRec [15], BERT4Rec [16])*'
	- This flag is for the paper with Ref. ID = 15
- '*We benchmark PANTHER against several strong baseline models, including Transformer [24], SASRec [15], and HSTU [12]*'
	- This flag is for the paper with Ref. ID = 15
- '*14%) * The higher HR@10 reported SASRec [15] is due to sampled negative evaluation (∼100 items)*'
	- This flag is for the paper with Ref. ID = 15
- '*, SASRec [15], BERT4Rec [16])*'
	- This flag is for the paper with Ref. ID = 16
- '*Generative sequential models, such as HSTU [12], TIGER [17], DiffuRecSys [18], and HLLM [19] have further advanced the field by modeling complex temporal dependencies and uncertainties*'
	- This flag is for the paper with Ref. ID = 17
- '*Generative sequential models, such as HSTU [12], TIGER [17], DiffuRecSys [18], and HLLM [19] have further advanced the field by modeling complex temporal dependencies and uncertainties*'
	- This flag is for the paper with Ref. ID = 18
- '*Generative sequential models, such as HSTU [12], TIGER [17], DiffuRecSys [18], and HLLM [19] have further advanced the field by modeling complex temporal dependencies and uncertainties*'
	- This flag is for the paper with Ref. ID = 19
- '*Early supervised approaches, including logistic regression, decision trees, and gradient boosting, perform effectively on structured data but face challenges with sparse, noisy, high-dimensional transaction data and extreme class imbalance [20]*'
	- This flag is for the paper with Ref. ID = 20
- '*Graph-based methods like R-GCNs [21] and heterogeneous GNNs [22] effectively capture relational patterns among entities, yet scalability and real-time latency in billion-user scenarios remain open research areas*'
	- This flag is for the paper with Ref. ID = 21
- '*Graph-based methods like R-GCNs [21] and heterogeneous GNNs [22] effectively capture relational patterns among entities, yet scalability and real-time latency in billion-user scenarios remain open research areas*'
	- This flag is for the paper with Ref. ID = 22
- '*For live transactions, we compute risk scores through feature fusion: Pr(y = 1|·) = gϕ  ψ(cnew) | {z } context , fenc(X[L-100:L] u ) | {z } recent patterns , eu |{z} long-term profile , ∆(ˆxL+1, xnew) | {z } behavior deviation  , (3) where the function gϕ represents a general downstream discriminative model, which can take various flexible forms depending on specific tasks or use cases, ψ(·) embeds transaction context features, fenc encodes the last 100 transactions via TextCNN [23], and ∆measures the distance between predicted and observed behaviors*'
	- This flag is for the paper with Ref. ID = 23
- '*Credit Card Transactions (CCT) [25]: A synthetic dataset with 20 million transactions from 2,000 users, used for fraud detection with embedded anomalies*'
	- This flag is for the paper with Ref. ID = 25
- '*MBD-mini [26]: An anonymized banking dataset tracking monthly product purchases, focusing on repetitive consumer behaviors*'
	- This flag is for the paper with Ref. ID = 26
- '*MovieLens-1M [27]: A widely-used recommendation dataset with 1 million user-item interactions, ideal for evaluating sequential models in non-financial domains*'
	- This flag is for the paper with Ref. ID = 27
- '*Yelp [28]: A public recommendation dataset containing millions of user-business interactions (e*'
	- This flag is for the paper with Ref. ID = 28

