# Paper Analysis Utility - Results

Paper: MTRec Learning to Align with User Preferences via.pdf


## Document Structure

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/9 MTRec/chapter_fig.jpg]]

1) 'Introduction' -- p. 1 (ca. 1 pages)
2) 'Related Works' -- p. 2 (ca. 1 pages)
3) 'Preliminaries' -- p. 3 (ca. 1 pages)
4) 'Method' -- p. 4 (ca. 3 pages)
5) 'Experiments' -- p. 7 (ca. 3 pages)
6) 'Conclusions' -- p. 10 (ca. 1 pages)
7) 'References' -- p. 11 (ca. 8 pages)
A) 'Technical Appendices and Supplementary Material' -- p. 19 (ca. 2 pages)


## Unicode Character Usage

> [!NOTE]
> *Please note that this list may contain false positives since this is feature is still in early stages of development.*

- Dashes:
	- Stats for minus signs ():
		- Valid uses: 0/33=0.00%
		- Invalid uses: 33/33=100.00%
	- Sentences with invalid dashes:
		- Lines containing invalid dashes:
		- Page 2: i∈I pϕ(ˆa|i, ht−1),
		- Page 2: π∈Π EπE[r(s, a)] −Eπ[r(s, a)] −H(π),
		- Page 2: where H(π) ≜Eπ[−log π(a|s)] denotes the entropy of policy π. Intuitively, this formulation learns
		- Page 2: π∈Π EρE[r(s, a)] −Eρ[r(s, a)] −H(π) −ϕ(r),
		- Page 2: If we define the regularizer as ψ(x) = x −ϕ(x), then EρE[r(s, a)] −ϕ(r) can be compactly represented by
		- Page 3: r(s, a) = Q(s, a) −γEs′∼P (s,a)V (s′), where V (s) = Ea∼π(·|s)[Q(s, a) −log π(a|s)]. Also the
		- Page 3: Q∈ΩEs,a∼ρE[ψ(Q(s, a) −γEs′∼P (s,a)V ∗(s′))] −(1 −γ)Es0∼ρ0[V ∗(s0)],
		- Page 3: r(s, a) = Q(s, a) −γEρE[log
		- Page 5: D= Q(s, a) −γEρE[log
		- Page 5: in Problem 4 (i.e., (1 −γ)Es0∼ρ0[V (s0)]) can be replaced by E(s,a)∼ρE[V (s) −γV (s′)]. In other
		- Page 5: Garg et al. [2021], we choose the regularizer as ψ(x) = x −
		- Page 5: Qλ EρE[Qλ(s, a) −log
		- Page 5: exp Qλ(s, a)] −1
		- Page 5: 4αEρE[(Qλ(s, a) −log
		- Page 5: λ(s, a) −γEρE[log
		- Page 6: LCE(ζ) = −EDE[aP log(Fζ(i|h)) + aN log(1 −Fζ(i|h))],
		- Page 6: LAlign(ζ) = −EDE[r∗(s, aP ) · Fζ(i|h) + r∗(s, aN) · (1 −Fζ(i|h))],
		- Page 6: LRL(ζ) = −Eit∼Fζ[
		- Page 6: ˆr(ht−1, it, at)]
		- Page 6: LF inal(ζ) = −Eit∼Fζ[
		- Page 6: ˆr(ht−1, it, at) + κ · r∗(ht−1, it, at)]
		- Page 18: Q∈ΩEs,a∼ρE[ψ(Q(s, a) −γEs′∼P (s,a)V ∗(s′))] −(1 −γ)Es0∼ρ0[V ∗(s0)],
		- Page 18: (1 −γ)Es0∼ρ0[V ∗(s0)] = (1 −γ)
		- Page 18: EDE[V ∗(st)] −(1 −γ)
		- Page 18: = EρE[V ∗(s) −γV ∗(s′)],
		- Page 18: Then, on substituting ψ(x) = x −
		- Page 18: Q EρE[Q(s, a) −log
		- Page 18: exp Q(s, a)] −1
		- Page 18: 4αEρE[(Q(s, a) −log
		- Page 19: (λ −1) · u,
		- Page 19: λi(s, a) = λi(s, a) −log
		- Page 19: 4α(λi(s, a) −log
		- Page 20: λ(s, a) −γV ∗(s′), ∀s, a ∼DE;


## References not in Bibliography

> [!NOTE]
> The sentences listed below contain references that were not found in the 'References' section.
> *Please note that this list may contain false positives as, e.g., the content of a normal bracket might have been mistaken for a reference, or a natural reference (Authorname in text and year in brackets) might have been mismatched.*

-  max Q∈ΩEs,a∼ρE[ψ(Q(s, a) −γEs′∼P (s,a)V ∗(s′))] −(1 −γ)Es0∼ρ0[V ∗(s0)], (4) where V ∗(s) = log P a exp Q(s, a)
- , (1 −γ)Es0∼ρ0[V (s0)]) can be replaced by E(s,a)∼ρE[V (s) −γV (s′)]
-  In other words, Es0∼ρ0[V (s0)] is irrelevant with the initial state distribution ρ0
-  In this context, Fζ(i|h) represents the RL-based recommendation policy, whose goal is to maximize the expectation of accumulated rewards ˆr: LRL(ζ) = −Eit∼Fζ[ X t ˆr(ht−1, it, at)] (11) Since we want the recommendation model to also maximize the mental rewards of the user
-  LF inal(ζ) = −Eit∼Fζ[ X t ˆr(ht−1, it, at) + κ · r∗(ht−1, it, at)] (12) See Appendix A
-  Wide&Deep Cheng et al [2016] is a hybrid recommendation model combining a wide linear model and deep neural network for collaborative filtering
-  PNN Qu et al [2016] is a neural network architecture designed for CTR prediction in recommender systems
-  DeepFM Guo et al [2017] is a hybrid recommendation model combining factorization machines and deep neural networks
-  SASRec Wang-Cheng and McAuley [2018] uses the self-attention mechanism to model sequential patterns for recommendation systems
-  DIN Zhou et al [2018] is an attention-based neural model for sequential recommendation, where the attention mechanism aims to distinguish the interest of a user’s historical behaviors
-  DIEN Zhou et al [2019] designs a sequential architecture to model interest evolution for recommendation, 7 
-  LinRec Liu et al [2023b] is a lightweight linear recommendation model designed for efficient computation and scalability with large datasets
-  SIGMA Liu et al [2024] is a sequential recommendation model that uses a selective gating mechanism to focus on the most relevant user behaviors for improved performance
-  Both training and testing of the algorithms are conducted in simulated interactive recommendation environments on Virtual Taobao Shi et al [2019]


## Unused References in Bibliography

> [!NOTE]
> The references listed below were listed in the 'References' section but never used in the document's main text (excluding appendices).
> -> Total = 20
> *Please note that this list may contain false positives as, e.g., the references ID (e.g., first author's lastname + year) was not correctly parsed or the in-text reference was not recognized due to linebreaks.*

- Parsed Ref. ID: Chen et al, 2021b
	- Full reference: `Xiaocong Chen, Lina Yao, Aixin Sun, Xianzhi Wang, Xiwei Xu, and Liming Zhu. Generative inverse deep reinforcement learning for online recommendation. In Proceedings of the 30th ACM International Conference on Information and Knowledge Management, pages 201–210, 2021b.`
- Parsed Ref. ID: Cheng et al, 2016
	- Full reference: `Heng-Tze Cheng, Levent Koc, Jeremiah Harmsen, Tal Shaked, Tushar Chandra, Hrishi Aradhye, Glen Anderson, Greg Corrado, Wei Chai, Mustafa Ispir, et al. Wide & deep learning for recommender systems. In Proceedings of the 1st workshop on deep learning for recommender systems, pages 7–10, 2016.`
- Parsed Ref. ID: Covington et al, 2016
	- Full reference: `Paul Covington, Jay Adams, Emre Sargin, and Mengchen Zhao. Deep neural networks for youtube recommendations. In Proceedings of the 10th ACM Conference on Recommender Systems, page 191–198, 2016.`
- Parsed Ref. ID: Dai et al, 2021
	- Full reference: `Xinyi Dai, Jianghao Lin, Weinan Zhang, Shuai Li, Weiwen Liu, Ruiming Tang, Xiuqiang He, Jianye Hao, Jun Wang, and Yong Yu. An adversarial imitation click model for information retrieval. In Proceedings of the Web Conference, pages 1809–1820, 2021.`
- Parsed Ref. ID: Deepak and Amir, 2007
	- Full reference: `Ramachandran Deepak and Eyal Amir. Bayesian inverse reinforcement learning. In Proceedings of the 20th International Joint Conference on Artificial Intelligence, pages 2586–2591, 2007.`
- Parsed Ref. ID: Garg et al, 2021
	- Full reference: `Divyansh Garg, Shuvam Chakraborty, Chris Cundy, Jiaming Song, and Stefano Ermon. Iq-learn: Inverse soft-q learning for imitation. In Advances in Neural Information Processing Systems, pages 4028–4039, 2021.`
- Parsed Ref. ID: Guo et al, 2017
	- Full reference: `Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, and Xiuqiang He. Deepfm: a factorizationmachine based neural network for ctr prediction. In Proceedings of the 26th International Joint Conference on Artificial Intelligence, 2017.`
- Parsed Ref. ID: Jiawei et al, 2023
	- Full reference: `Chen Jiawei, Hande Dong, Xiang Wang, Fuli Feng, Meng Wang, and Xiangnan He. Bias and debias in recommender system: A survey and future directions. ACM Transactions on Information Systems, 41(3):1–39, 2023.`
- Parsed Ref. ID: Kingma and Ba, 2015
	- Full reference: `Diederik P. Kingma and Jimmy Ba. Deepfm: a factorization-machine based neural network for ctr prediction. In International Conference on Learning Representations, 2015.`
- Parsed Ref. ID: Liu et al, 2023b
	- Full reference: `Langming Liu, Liu Cai, Chi Zhang, Xiangyu Zhao, Jingtong Gao, Wanyu Wang, Yifu Lv, Wenqi Fan, Yiqi Wang, Ming He, et al. Linrec: Linear attention mechanism for long-term sequential recommender systems. In Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval, pages 289–299, 2023b.`
- Parsed Ref. ID: Liu et al, 2024
	- Full reference: `Ziwei Liu, Qidong Liu, Yejing Wang, Wanyu Wang, Pengyue Jia, Maolin Wang, Zitao Liu, Yi Chang, and Xiangyu Zhao. Bidirectional gated mamba for sequential recommendation. arXiv preprint arXiv:2408.11451, 2024.`
- Parsed Ref. ID: Qu et al, 2016
	- Full reference: `Yanru Qu, Han Cai, Kan Ren, Weinan Zhang, Yong Yu, Ying Wen, and Jun Wang. Product-based neural networks for user response prediction. In 2016 IEEE 16th international conference on data mining (ICDM), pages 1149–1154. IEEE, 2016.`
- Parsed Ref. ID: Shi et al, 2019
	- Full reference: `Jing-Cheng Shi, Yang Yu, Qing Da, Shi-Yong Chen, and An-Xiang Zeng. Virtual-taobao: Virtualizing real-world online retail environment for reinforcement learning. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 33, pages 4902–4909, 2019.`
- Parsed Ref. ID: Wang et al, 2017
	- Full reference: `Ruoxi Wang, Bin Fu, Gang Fu, and Mingliang Wang. Deep & cross network for ad click predictions. In Proceedings of the ADKDD’17, 2017.`
- Parsed Ref. ID: Wang-Cheng and McAuley, 2018
	- Full reference: `Kang Wang-Cheng and Julian McAuley. Self-attentive sequential recommendation. In Proceedings of the International Conference on Data Mining, pages 197–206, 2018.`
- Parsed Ref. ID: Will et al, 2018
	- Full reference: `Dabney Will, Mark Rowland, Marc Bellemare, and Rémi Munos. Distributional reinforcement learning with quantile regression. In Proceedings of the 33rd AAAI Conference on Artificial Intelligence, 2018.`
- Parsed Ref. ID: Lee et al, 2021
	- Full reference: `Jae woong Lee, Seongmin Park, Jongwuk Lee, and mengchen zhao. Dual unbiased recommender learning for implicit feedback. In Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval, pages 1647–1651, 2021.`
- Parsed Ref. ID: Yu and Qin, 2020
	- Full reference: `Wenhui Yu and Zheng Qin. Sampler design for implicit feedback data by noisy-label robust learning. In Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval, pages 861–870, 2020.`
- Parsed Ref. ID: Zhou et al, 2018
	- Full reference: `Guorui Zhou, Xiaoqiang Zhu, Chenru Song, Ying Fan, Han Zhu, Xiao Ma, Yanghui Yan, Junqi Jin, Han Li, and Kun Gai. Deep interest network for click-through rate prediction. In Proceedings of the 24th ACM SIGKDD international conference on knowledge discovery and data mining, pages 1059–1068, 2018.`
- Parsed Ref. ID: 1, 0
	- Full reference: `NeurIPS Paper Checklist 1. Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: Our main contribution is the MTRec framework with the QR-IQL algorithm, which is described in Section 4 and justified in Section 5. Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper. • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers. • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper. 2. Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes] Justification: The limitation is discussed in Appendix A.5. Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate "Limitations" section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. • The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. • The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations. 3. Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: [Yes] Justification: The derivations details are provided in Appendix A. Guidelines: • The answer NA means that the paper does not include theoretical results. • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced. • All assumptions should be clearly stated or referenced in the statement of any theorems. • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. • Theorems and Lemmas that the proof relies upon should be properly referenced. 4. Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: [Yes] Justification: The implementation details are provided in Appendix A.3. Guidelines: • The answer NA means that the paper does not include experiments. • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. • Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results. 5. Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? Answer: [No] Justification: We provide implementation details in Appendix A.3 and will release the code upon acceptance of this paper. Guidelines: • The answer NA means that paper does not include experiments requiring code. • Please see the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• While we encourage the release of code and data, we understand that this might not bepossible, so “No” is an acceptable answer. Papers cannot be rejected simply for notincluding code, unless this is central to the contribution (e.g., for a new open-sourcebenchmark).• The instructions should contain the exact command and environment needed to run toreproduce the results. See the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• The authors should provide instructions on data access and preparation, including howto access the raw data, preprocessed data, intermediate data, and generated data, etc.• The authors should provide scripts to reproduce all experimental results for the newproposed method and baselines. If only a subset of experiments are reproducible, theyshould state which ones are omitted from the script and why.• At submission time, to preserve anonymity, the authors should release anonymizedversions (if applicable).• Providing as much information as possible in supplemental material (appended to thepaper) is recommended, but including URLs to data and code is permitted.6. Experimental setting/detailsQuestion: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand theresults?Answer: [Yes]Justification: All the data processing, training and evaluation details are described inSection 5 and Appendix A.Guidelines:• The answer NA means that the paper does not include experiments.• The experimental setting should be presented in the core of the paper to a level of detailthat is necessary to appreciate the results and make sense of them.• The full details can be provided either with the code, in appendix, or as supplementalmaterial.7. Experiment statistical significanceQuestion: Does the paper report error bars suitably and correctly defined or other appropriateinformation about the statistical significance of the experiments?Answer: [Yes]Justification: We report the mean CTR with 95% confidence interval in Figure 2.Guidelines:• The answer NA means that the paper does not include experiments.• The authors should answer "Yes" if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that supportthe main claims of the paper.• The factors of variability that the error bars are capturing should be clearly stated (forexample, train/test split, initialization, random drawing of some parameter, or overallrun with given experimental conditions).• The method for calculating the error bars should be explained (closed form formula,call to a library function, bootstrap, etc.)• The assumptions made should be given (e.g., Normally distributed errors).• It should be clear whether the error bar is the standard deviation or the standard errorof the mean.• It is OK to report 1-sigma error bars, but one should state it. The authors shouldpreferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesisof Normality of errors is not verified.• For asymmetric distributions, the authors should be careful not to show in tables orfigures symmetric error bars that would yield results that are out of range (e.g. negativeerror rates).• If error bars are reported in tables or plots, The authors should explain in the text howthey were calculated and reference the corresponding figures or tables in the text.8. Experiments compute resourcesQuestion: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproducethe experiments?Answer: [Yes]Justification: The computational resources and training times are provided in Appendix A.3.Guidelines:• The answer NA means that the paper does not include experiments.• The paper should indicate the type of compute workers CPU or GPU, internal cluster,or cloud provider, including relevant memory and storage.• The paper should provide the amount of compute required for each of the individualexperimental runs as well as estimate the total compute.• The paper should disclose whether the full research project required more computethan the experiments reported in the paper (e.g., preliminary or failed experiments thatdidn’t make it into the paper).9. Code of ethicsQuestion: Does the research conducted in the paper conform, in every respect, with theNeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines?Answer: [Yes]Justification: We respect the NeurIPS Code of Ethics.Guidelines:• The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics.• If the authors answer No, they should explain the special circumstances that require adeviation from the Code of Ethics.• The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).10. Broader impactsQuestion: Does the paper discuss both potential positive societal impacts and negativesocietal impacts of the work performed?Answer: [NA]Justification: This work focuses on the technical foundations of sequential recommendation.Guidelines:• The answer NA means that there is no societal impact of the work performed.• If the authors answer NA or No, they should explain why their work has no societalimpact or why the paper does not address societal impact.• Examples of negative societal impacts include potential malicious or unintended uses(e.g., disinformation, generating fake profiles, surveillance), fairness considerations(e.g., deployment of technologies that could make decisions that unfairly impact specificgroups), privacy considerations, and security considerations.• The conference expects that many papers will be foundational research and not tiedto particular applications, let alone deployments. However, if there is a direct path toany negative applications, the authors should point it out. For example, it is legitimateto point out that an improvement in the quality of generative models could be used togenerate deepfakes for disinformation. On the other hand, it is not needed to point outthat a generic algorithm for optimizing neural networks could enable people to trainmodels that generate Deepfakes faster.• The authors should consider possible harms that could arise when the technology isbeing used as intended and functioning correctly, harms that could arise when thetechnology is being used as intended but gives incorrect results, and harms followingfrom (intentional or unintentional) misuse of the technology.• If there are negative societal impacts, the authors could also discuss possible mitigationstrategies (e.g., gated release of models, providing defenses in addition to attacks,mechanisms for monitoring misuse, mechanisms to monitor how a system learns fromfeedback over time, improving the efficiency and accessibility of ML).11. SafeguardsQuestion: Does the paper describe safeguards that have been put in place for responsiblerelease of data or models that have a high risk for misuse (e.g., pretrained language models,image generators, or scraped datasets)?Answer: [NA]Justification: Our paper does not release data or models with a high risk for misuse.Guidelines:• The answer NA means that the paper poses no such risks.• Released models that have a high risk for misuse or dual-use should be released withnecessary safeguards to allow for controlled use of the model, for example by requiringthat users adhere to usage guidelines or restrictions to access the model or implementingsafety filters.• Datasets that have been scraped from the Internet could pose safety risks. The authorsshould describe how they avoided releasing unsafe images.• We recognize that providing effective safeguards is challenging, and many papers donot require this, but we encourage authors to take this into account and make a bestfaith effort.12. Licenses for existing assetsQuestion: Are the creators or original owners of assets (e.g., code, data, models), used inthe paper, properly credited and are the license and terms of use explicitly mentioned andproperly respected?Answer: [Yes]Justification: All the baselines are properly cited and introduced in Section 5.Guidelines:• The answer NA means that the paper does not use existing assets.• The authors should cite the original paper that produced the code package or dataset.• The authors should state which version of the asset is used and, if possible, include aURL.• The name of the license (e.g., CC-BY 4.0) should be included for each asset.• For scraped data from a particular source (e.g., website), the copyright and terms ofservice of that source should be provided.• If assets are released, the license, copyright information, and terms of use in thepackage should be provided. For popular datasets, paperswithcode.com/datasetshas curated licenses for some datasets. Their licensing guide can help determine thelicense of a dataset.• For existing datasets that are re-packaged, both the original license and the license ofthe derived asset (if it has changed) should be provided.• If this information is not available online, the authors are encouraged to reach out tothe asset’s creators.13. New assetsQuestion: Are new assets introduced in the paper well documented and is the documentationprovided alongside the assets?Answer: [NA]Justification: The paper does not release new assets.Guidelines:• The answer NA means that the paper does not release new assets.• Researchers should communicate the details of the dataset/code/model as part of theirsubmissions via structured templates. This includes details about training, license,limitations, etc.• The paper should discuss whether and how consent was obtained from people whoseasset is used.• At submission time, remember to anonymize your assets (if applicable). You can eithercreate an anonymized URL or include an anonymized zip file.14. Crowdsourcing and research with human subjectsQuestion: For crowdsourcing experiments and research with human subjects, does the paperinclude the full text of instructions given to participants and screenshots, if applicable, aswell as details about compensation (if any)?Answer: [NA]Justification: The paper does not involve crowdsourcing or research with human subjects.Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should beincluded in the main paper.• According to the NeurIPS Code of Ethics, workers involved in data collection, curation,or other labor should be paid at least the minimum wage in the country of the datacollector.15. Institutional review board (IRB) approvals or equivalent for research with humansubjectsQuestion: Does the paper describe potential risks incurred by study participants, whethersuch risks were disclosed to the subjects, and whether Institutional Review Board (IRB)approvals (or an equivalent approval/review based on the requirements of your country orinstitution) were obtained?Answer: [NA]Justification: Our paper does not involve crowdsourcing or research with human subjects.Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Depending on the country in which research is conducted, IRB approval (or equivalent)may be required for any human subjects research. If you obtained IRB approval, youshould clearly state this in the paper.• We recognize that the procedures for this may vary significantly between institutionsand locations, and we expect authors to adhere to the NeurIPS Code of Ethics and theguidelines for their institution.• For initial submissions, do not include any information that would break anonymity (ifapplicable), such as the institution conducting the review.16. Declaration of LLM usageQuestion: Does the paper describe the usage of LLMs if it is an important, original, ornon-standard component of the core methods in this research? Note that if the LLM is usedonly for writing, editing, or formatting purposes and does not impact the core methodology,scientific rigorousness, or originality of the research, declaration is not required.Answer: [NA]Justification: The core method development in this research does not involve LLMs.Guidelines:• The answer NA means that the core method development in this research does notinvolve LLMs as any important, original, or non-standard components.• Please refer to our LLM policy (https://neurips.cc/Conferences/2025/LLM)for what should or should not be described.A`


## Frequently Referenced Authors

> [!NOTE]
> The following authors appear more than 2 times in the bibliography.
> *Please note that only the lastname and the first letter of the first name are compared for counting.*

- He X.: 4
- Wang X.: 3
- Yu Y.: 3
- Wang M.: 3
- Zhao X.: 3
- Wang W.: 3


## Reference Checker Results

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/9 MTRec/literature_validation_results_fig.jpg]]

References section starts on page 11.

- No link provided: $39/40=97.50\%$
- Unchecked links: $0/40=0.00\%$
- Valid links: $0/40=0.00\%$
- Invalid link: $1/40=2.50\%$
	- Invalid entries:
		=> total = 1
		- NeurIPS Paper Checklist 1. Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: \[Yes\] Justification: Our main contribution is the MTRec framework with the QR-IQL algorithm, which is described in Section 4 and justified in Section 5. Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper. • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers. • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper. 2. Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: \[Yes\] Justification: The limitation is discussed in Appendix A.5. Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate "Limitations" section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. • The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. • The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations. 3. Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: \[Yes\] Justification: The derivations details are provided in Appendix A. Guidelines: • The answer NA means that the paper does not include theoretical results. • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced. • All assumptions should be clearly stated or referenced in the statement of any theorems. • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. • Theorems and Lemmas that the proof relies upon should be properly referenced. 4. Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: \[Yes\] Justification: The implementation details are provided in Appendix A.3. Guidelines: • The answer NA means that the paper does not include experiments. • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. • Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results. 5. Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? Answer: \[No\] Justification: We provide implementation details in Appendix A.3 and will release the code upon acceptance of this paper. Guidelines: • The answer NA means that paper does not include experiments requiring code. • Please see the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• While we encourage the release of code and data, we understand that this might not bepossible, so “No” is an acceptable answer. Papers cannot be rejected simply for notincluding code, unless this is central to the contribution (e.g., for a new open-sourcebenchmark).• The instructions should contain the exact command and environment needed to run toreproduce the results. See the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• The authors should provide instructions on data access and preparation, including howto access the raw data, preprocessed data, intermediate data, and generated data, etc.• The authors should provide scripts to reproduce all experimental results for the newproposed method and baselines. If only a subset of experiments are reproducible, theyshould state which ones are omitted from the script and why.• At submission time, to preserve anonymity, the authors should release anonymizedversions (if applicable).• Providing as much information as possible in supplemental material (appended to thepaper) is recommended, but including URLs to data and code is permitted.6. Experimental setting/detailsQuestion: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand theresults?Answer: \[Yes\]Justification: All the data processing, training and evaluation details are described inSection 5 and Appendix A.Guidelines:• The answer NA means that the paper does not include experiments.• The experimental setting should be presented in the core of the paper to a level of detailthat is necessary to appreciate the results and make sense of them.• The full details can be provided either with the code, in appendix, or as supplementalmaterial.7. Experiment statistical significanceQuestion: Does the paper report error bars suitably and correctly defined or other appropriateinformation about the statistical significance of the experiments?Answer: \[Yes\]Justification: We report the mean CTR with 95% confidence interval in Figure 2.Guidelines:• The answer NA means that the paper does not include experiments.• The authors should answer "Yes" if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that supportthe main claims of the paper.• The factors of variability that the error bars are capturing should be clearly stated (forexample, train/test split, initialization, random drawing of some parameter, or overallrun with given experimental conditions).• The method for calculating the error bars should be explained (closed form formula,call to a library function, bootstrap, etc.)• The assumptions made should be given (e.g., Normally distributed errors).• It should be clear whether the error bar is the standard deviation or the standard errorof the mean.• It is OK to report 1-sigma error bars, but one should state it. The authors shouldpreferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesisof Normality of errors is not verified.• For asymmetric distributions, the authors should be careful not to show in tables orfigures symmetric error bars that would yield results that are out of range (e.g. negativeerror rates).• If error bars are reported in tables or plots, The authors should explain in the text howthey were calculated and reference the corresponding figures or tables in the text.8. Experiments compute resourcesQuestion: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproducethe experiments?Answer: \[Yes\]Justification: The computational resources and training times are provided in Appendix A.3.Guidelines:• The answer NA means that the paper does not include experiments.• The paper should indicate the type of compute workers CPU or GPU, internal cluster,or cloud provider, including relevant memory and storage.• The paper should provide the amount of compute required for each of the individualexperimental runs as well as estimate the total compute.• The paper should disclose whether the full research project required more computethan the experiments reported in the paper (e.g., preliminary or failed experiments thatdidn’t make it into the paper).9. Code of ethicsQuestion: Does the research conducted in the paper conform, in every respect, with theNeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines?Answer: \[Yes\]Justification: We respect the NeurIPS Code of Ethics.Guidelines:• The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics.• If the authors answer No, they should explain the special circumstances that require adeviation from the Code of Ethics.• The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).10. Broader impactsQuestion: Does the paper discuss both potential positive societal impacts and negativesocietal impacts of the work performed?Answer: \[NA\]Justification: This work focuses on the technical foundations of sequential recommendation.Guidelines:• The answer NA means that there is no societal impact of the work performed.• If the authors answer NA or No, they should explain why their work has no societalimpact or why the paper does not address societal impact.• Examples of negative societal impacts include potential malicious or unintended uses(e.g., disinformation, generating fake profiles, surveillance), fairness considerations(e.g., deployment of technologies that could make decisions that unfairly impact specificgroups), privacy considerations, and security considerations.• The conference expects that many papers will be foundational research and not tiedto particular applications, let alone deployments. However, if there is a direct path toany negative applications, the authors should point it out. For example, it is legitimateto point out that an improvement in the quality of generative models could be used togenerate deepfakes for disinformation. On the other hand, it is not needed to point outthat a generic algorithm for optimizing neural networks could enable people to trainmodels that generate Deepfakes faster.• The authors should consider possible harms that could arise when the technology isbeing used as intended and functioning correctly, harms that could arise when thetechnology is being used as intended but gives incorrect results, and harms followingfrom (intentional or unintentional) misuse of the technology.• If there are negative societal impacts, the authors could also discuss possible mitigationstrategies (e.g., gated release of models, providing defenses in addition to attacks,mechanisms for monitoring misuse, mechanisms to monitor how a system learns fromfeedback over time, improving the efficiency and accessibility of ML).11. SafeguardsQuestion: Does the paper describe safeguards that have been put in place for responsiblerelease of data or models that have a high risk for misuse (e.g., pretrained language models,image generators, or scraped datasets)?Answer: \[NA\]Justification: Our paper does not release data or models with a high risk for misuse.Guidelines:• The answer NA means that the paper poses no such risks.• Released models that have a high risk for misuse or dual-use should be released withnecessary safeguards to allow for controlled use of the model, for example by requiringthat users adhere to usage guidelines or restrictions to access the model or implementingsafety filters.• Datasets that have been scraped from the Internet could pose safety risks. The authorsshould describe how they avoided releasing unsafe images.• We recognize that providing effective safeguards is challenging, and many papers donot require this, but we encourage authors to take this into account and make a bestfaith effort.12. Licenses for existing assetsQuestion: Are the creators or original owners of assets (e.g., code, data, models), used inthe paper, properly credited and are the license and terms of use explicitly mentioned andproperly respected?Answer: \[Yes\]Justification: All the baselines are properly cited and introduced in Section 5.Guidelines:• The answer NA means that the paper does not use existing assets.• The authors should cite the original paper that produced the code package or dataset.• The authors should state which version of the asset is used and, if possible, include aURL.• The name of the license (e.g., CC-BY 4.0) should be included for each asset.• For scraped data from a particular source (e.g., website), the copyright and terms ofservice of that source should be provided.• If assets are released, the license, copyright information, and terms of use in thepackage should be provided. For popular datasets, paperswithcode.com/datasetshas curated licenses for some datasets. Their licensing guide can help determine thelicense of a dataset.• For existing datasets that are re-packaged, both the original license and the license ofthe derived asset (if it has changed) should be provided.• If this information is not available online, the authors are encouraged to reach out tothe asset’s creators.13. New assetsQuestion: Are new assets introduced in the paper well documented and is the documentationprovided alongside the assets?Answer: \[NA\]Justification: The paper does not release new assets.Guidelines:• The answer NA means that the paper does not release new assets.• Researchers should communicate the details of the dataset/code/model as part of theirsubmissions via structured templates. This includes details about training, license,limitations, etc.• The paper should discuss whether and how consent was obtained from people whoseasset is used.• At submission time, remember to anonymize your assets (if applicable). You can eithercreate an anonymized URL or include an anonymized zip file.14. Crowdsourcing and research with human subjectsQuestion: For crowdsourcing experiments and research with human subjects, does the paperinclude the full text of instructions given to participants and screenshots, if applicable, aswell as details about compensation (if any)?Answer: \[NA\]Justification: The paper does not involve crowdsourcing or research with human subjects.Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should beincluded in the main paper.• According to the NeurIPS Code of Ethics, workers involved in data collection, curation,or other labor should be paid at least the minimum wage in the country of the datacollector.15. Institutional review board (IRB) approvals or equivalent for research with humansubjectsQuestion: Does the paper describe potential risks incurred by study participants, whethersuch risks were disclosed to the subjects, and whether Institutional Review Board (IRB)approvals (or an equivalent approval/review based on the requirements of your country orinstitution) were obtained?Answer: \[NA\]Justification: Our paper does not involve crowdsourcing or research with human subjects.Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Depending on the country in which research is conducted, IRB approval (or equivalent)may be required for any human subjects research. If you obtained IRB approval, youshould clearly state this in the paper.• We recognize that the procedures for this may vary significantly between institutionsand locations, and we expect authors to adhere to the NeurIPS Code of Ethics and theguidelines for their institution.• For initial submissions, do not include any information that would break anonymity (ifapplicable), such as the institution conducting the review.16. Declaration of LLM usageQuestion: Does the paper describe the usage of LLMs if it is an important, original, ornon-standard component of the core methods in this research? Note that if the LLM is usedonly for writing, editing, or formatting purposes and does not impact the core methodology,scientific rigorousness, or originality of the research, declaration is not required.Answer: \[NA\]Justification: The core method development in this research does not involve LLMs.Guidelines:• The answer NA means that the core method development in this research does notinvolve LLMs as any important, original, or non-standard components.• Please refer to our LLM policy (https://neurips.cc/Conferences/2025/LLM)for what should or should not be described.A
			-> Returned with status code 404!

- Different links: $0/40=0.00\%$

- Successful searches: $23/40=57.50\%$
- Skipped searches: $0/40=0.00\%$
- Mismatching infos: $14/40=35.00\%$
	- **Entries with mismatching author information:**
		=> total = 5
		- `Paul Covington, Jay Adams, Emre Sargin, and Mengchen Zhao. Deep neural networks for youtube recommendations. In Proceedings of the 10th ACM Conference on Recommender Systems, page 191–198, 2016.`
			- Authors () did not match found publication titled 'Deep Neural Networks for YouTube Recommendations'
		- `Hanze Dong, Wei Xiong, Deepanshu Goyal, Rui Pan, Shizhe Diao, Jipeng Zhang, Kashun Shum, and Tong Zhang. Raft: Reward ranked finetuning for generative foundation model alignment, 2023.`
			- Authors (0015, Chow, 0002, 0001) did not match found publication titled 'RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment.'
		- `Langming Liu, Liu Cai, Chi Zhang, Xiangyu Zhao, Jingtong Gao, Wanyu Wang, Yifu Lv, Wenqi Fan, Yiqi Wang, Ming He, et al. Linrec: Linear attention mechanism for long-term sequential recommender systems. In Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval, pages 289–299, 2023b.`
			- Authors () did not match found publication titled 'LinRec: Linear Attention Mechanism for Long-term Sequential Recommender Systems'
		- `Jae woong Lee, Seongmin Park, Jongwuk Lee, and mengchen zhao. Dual unbiased recommender learning for implicit feedback. In Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval, pages 1647–1651, 2021.`
			- Authors () did not match found publication titled 'Dual Unbiased Recommender Learning for Implicit Feedback'
		- `Guorui Zhou, Xiaoqiang Zhu, Chenru Song, Ying Fan, Han Zhu, Xiao Ma, Yanghui Yan, Junqi Jin, Han Li, and Kun Gai. Deep interest network for click-through rate prediction. In Proceedings of the 24th ACM SIGKDD international conference on knowledge discovery and data mining, pages 1059–1068, 2018.`
			- Authors (Dai) did not match found publication titled 'Deep Interest Network for Click-Through Rate Prediction'
	- **Entries with mismatching years (where the difference is > 1 year):**
		=> total = 2
		- `Chen Jiawei, Hande Dong, Xiang Wang, Fuli Feng, Meng Wang, and Xiangnan He. Bias and debias in recommender system: A survey and future directions. ACM Transactions on Information Systems, 41(3):1–39, 2023.`
			- Year (2020) does not match expected year (2023)
		- `Arora Saurabh and Prashant Doshi. A survey of inverse reinforcement learning: Challenges, methods and progress. Artificial Intelligence, 297(103500), 2021.`
			- Year (2018) does not match expected year (2021)
	- **Entries with mismatching years (where the difference is = 1 year):**
		=> total = 7
		- `Minmin Chen, Alex Beutel, Paul Covington, Sagar Jain, Francois Belletti, and Ed H. Chi. Top-k off-policy correction for a REINFORCE recommender system. In Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining, pages 456–464, 2019.`
			- Year (2018) does not match expected year (2019)
		- `Xiaocong Chen, Lina Yao, Aixin Sun, Xianzhi Wang, Xiwei Xu, and Liming Zhu. Generative inverse deep reinforcement learning for online recommendation. In Proceedings of the 30th ACM International Conference on Information and Knowledge Management, pages 201–210, 2021b.`
			- Year (2020) does not match expected year (2021)
		- `Jing-Cheng Shi, Yang Yu, Qing Da, Shi-Yong Chen, and An-Xiang Zeng. Virtual-taobao: Virtualizing real-world online retail environment for reinforcement learning. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 33, pages 4902–4909, 2019.`
			- Year (2018) does not match expected year (2019)
		- `Wenjie Wang, Fuli Feng, Xiangnan He, Liqiang Nie, and Tat-Seng Chua. Denoising implicit feedback for recommendation. In Proceedings of the 14th ACM International Conference on Web Search and Data Mining, pages 373–381, 2021.`
			- Year (2020) does not match expected year (2021)
		- `Dabney Will, Mark Rowland, Marc Bellemare, and Rémi Munos. Distributional reinforcement learning with quantile regression. In Proceedings of the 33rd AAAI Conference on Artificial Intelligence, 2018.`
			- Year (2017) does not match expected year (2018)
		- `Jiaqi Yang, Xiang Li, Shuguang Han, Tao Zhuang, Dechuan Zhan, Xiaoyi Zeng, and Bin Tong. Capturing delayed feedback in conversion rate prediction via elapsed-time sampling. In Proceedings of the AAAI Conference on Artificial Intelligence, pages 4582–4589, 2021.`
			- Year (2020) does not match expected year (2021)
		- `Guorui Zhou, Na Mou, Ying Fan, Qi Pi, Weijie Bian, Chang Zhou, Xiaoqiang Zhu, and Kun Gai. Deep interest evolution network for click-through rate prediction. In Proceedings of the AAAI conference on artificial intelligence, volume 33, pages 5941–5948, 2019.`
			- Year (2018) does not match expected year (2019)
- No entry found: $3/40=7.50\%$
	- Unfound entries:
		=> total = 3
		- Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, and Xiuqiang He. Deepfm: a factorizationmachine based neural network for ctr prediction. In Proceedings of the 26th International Joint Conference on Artificial Intelligence, 2017.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: None of the 4 results matched the expected title!
		- ==Diederik P. Kingma and Jimmy Ba. Deepfm: a factorization-machine based neural network for ctr prediction. In International Conference on Learning Representations, 2015.==
			-> WARNING: None of the 10 results matched the expected title! | WARNING: None of the 1 results matched the expected title!
		- NeurIPS Paper Checklist 1. Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: \[Yes\] Justification: Our main contribution is the MTRec framework with the QR-IQL algorithm, which is described in Section 4 and justified in Section 5. Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper. • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers. • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper. 2. Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: \[Yes\] Justification: The limitation is discussed in Appendix A.5. Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate "Limitations" section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. • The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. • The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations. 3. Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: \[Yes\] Justification: The derivations details are provided in Appendix A. Guidelines: • The answer NA means that the paper does not include theoretical results. • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced. • All assumptions should be clearly stated or referenced in the statement of any theorems. • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. • Theorems and Lemmas that the proof relies upon should be properly referenced. 4. Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: \[Yes\] Justification: The implementation details are provided in Appendix A.3. Guidelines: • The answer NA means that the paper does not include experiments. • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. • Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results. 5. Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? Answer: \[No\] Justification: We provide implementation details in Appendix A.3 and will release the code upon acceptance of this paper. Guidelines: • The answer NA means that paper does not include experiments requiring code. • Please see the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• While we encourage the release of code and data, we understand that this might not bepossible, so “No” is an acceptable answer. Papers cannot be rejected simply for notincluding code, unless this is central to the contribution (e.g., for a new open-sourcebenchmark).• The instructions should contain the exact command and environment needed to run toreproduce the results. See the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• The authors should provide instructions on data access and preparation, including howto access the raw data, preprocessed data, intermediate data, and generated data, etc.• The authors should provide scripts to reproduce all experimental results for the newproposed method and baselines. If only a subset of experiments are reproducible, theyshould state which ones are omitted from the script and why.• At submission time, to preserve anonymity, the authors should release anonymizedversions (if applicable).• Providing as much information as possible in supplemental material (appended to thepaper) is recommended, but including URLs to data and code is permitted.6. Experimental setting/detailsQuestion: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand theresults?Answer: \[Yes\]Justification: All the data processing, training and evaluation details are described inSection 5 and Appendix A.Guidelines:• The answer NA means that the paper does not include experiments.• The experimental setting should be presented in the core of the paper to a level of detailthat is necessary to appreciate the results and make sense of them.• The full details can be provided either with the code, in appendix, or as supplementalmaterial.7. Experiment statistical significanceQuestion: Does the paper report error bars suitably and correctly defined or other appropriateinformation about the statistical significance of the experiments?Answer: \[Yes\]Justification: We report the mean CTR with 95% confidence interval in Figure 2.Guidelines:• The answer NA means that the paper does not include experiments.• The authors should answer "Yes" if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that supportthe main claims of the paper.• The factors of variability that the error bars are capturing should be clearly stated (forexample, train/test split, initialization, random drawing of some parameter, or overallrun with given experimental conditions).• The method for calculating the error bars should be explained (closed form formula,call to a library function, bootstrap, etc.)• The assumptions made should be given (e.g., Normally distributed errors).• It should be clear whether the error bar is the standard deviation or the standard errorof the mean.• It is OK to report 1-sigma error bars, but one should state it. The authors shouldpreferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesisof Normality of errors is not verified.• For asymmetric distributions, the authors should be careful not to show in tables orfigures symmetric error bars that would yield results that are out of range (e.g. negativeerror rates).• If error bars are reported in tables or plots, The authors should explain in the text howthey were calculated and reference the corresponding figures or tables in the text.8. Experiments compute resourcesQuestion: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproducethe experiments?Answer: \[Yes\]Justification: The computational resources and training times are provided in Appendix A.3.Guidelines:• The answer NA means that the paper does not include experiments.• The paper should indicate the type of compute workers CPU or GPU, internal cluster,or cloud provider, including relevant memory and storage.• The paper should provide the amount of compute required for each of the individualexperimental runs as well as estimate the total compute.• The paper should disclose whether the full research project required more computethan the experiments reported in the paper (e.g., preliminary or failed experiments thatdidn’t make it into the paper).9. Code of ethicsQuestion: Does the research conducted in the paper conform, in every respect, with theNeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines?Answer: \[Yes\]Justification: We respect the NeurIPS Code of Ethics.Guidelines:• The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics.• If the authors answer No, they should explain the special circumstances that require adeviation from the Code of Ethics.• The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).10. Broader impactsQuestion: Does the paper discuss both potential positive societal impacts and negativesocietal impacts of the work performed?Answer: \[NA\]Justification: This work focuses on the technical foundations of sequential recommendation.Guidelines:• The answer NA means that there is no societal impact of the work performed.• If the authors answer NA or No, they should explain why their work has no societalimpact or why the paper does not address societal impact.• Examples of negative societal impacts include potential malicious or unintended uses(e.g., disinformation, generating fake profiles, surveillance), fairness considerations(e.g., deployment of technologies that could make decisions that unfairly impact specificgroups), privacy considerations, and security considerations.• The conference expects that many papers will be foundational research and not tiedto particular applications, let alone deployments. However, if there is a direct path toany negative applications, the authors should point it out. For example, it is legitimateto point out that an improvement in the quality of generative models could be used togenerate deepfakes for disinformation. On the other hand, it is not needed to point outthat a generic algorithm for optimizing neural networks could enable people to trainmodels that generate Deepfakes faster.• The authors should consider possible harms that could arise when the technology isbeing used as intended and functioning correctly, harms that could arise when thetechnology is being used as intended but gives incorrect results, and harms followingfrom (intentional or unintentional) misuse of the technology.• If there are negative societal impacts, the authors could also discuss possible mitigationstrategies (e.g., gated release of models, providing defenses in addition to attacks,mechanisms for monitoring misuse, mechanisms to monitor how a system learns fromfeedback over time, improving the efficiency and accessibility of ML).11. SafeguardsQuestion: Does the paper describe safeguards that have been put in place for responsiblerelease of data or models that have a high risk for misuse (e.g., pretrained language models,image generators, or scraped datasets)?Answer: \[NA\]Justification: Our paper does not release data or models with a high risk for misuse.Guidelines:• The answer NA means that the paper poses no such risks.• Released models that have a high risk for misuse or dual-use should be released withnecessary safeguards to allow for controlled use of the model, for example by requiringthat users adhere to usage guidelines or restrictions to access the model or implementingsafety filters.• Datasets that have been scraped from the Internet could pose safety risks. The authorsshould describe how they avoided releasing unsafe images.• We recognize that providing effective safeguards is challenging, and many papers donot require this, but we encourage authors to take this into account and make a bestfaith effort.12. Licenses for existing assetsQuestion: Are the creators or original owners of assets (e.g., code, data, models), used inthe paper, properly credited and are the license and terms of use explicitly mentioned andproperly respected?Answer: \[Yes\]Justification: All the baselines are properly cited and introduced in Section 5.Guidelines:• The answer NA means that the paper does not use existing assets.• The authors should cite the original paper that produced the code package or dataset.• The authors should state which version of the asset is used and, if possible, include aURL.• The name of the license (e.g., CC-BY 4.0) should be included for each asset.• For scraped data from a particular source (e.g., website), the copyright and terms ofservice of that source should be provided.• If assets are released, the license, copyright information, and terms of use in thepackage should be provided. For popular datasets, paperswithcode.com/datasetshas curated licenses for some datasets. Their licensing guide can help determine thelicense of a dataset.• For existing datasets that are re-packaged, both the original license and the license ofthe derived asset (if it has changed) should be provided.• If this information is not available online, the authors are encouraged to reach out tothe asset’s creators.13. New assetsQuestion: Are new assets introduced in the paper well documented and is the documentationprovided alongside the assets?Answer: \[NA\]Justification: The paper does not release new assets.Guidelines:• The answer NA means that the paper does not release new assets.• Researchers should communicate the details of the dataset/code/model as part of theirsubmissions via structured templates. This includes details about training, license,limitations, etc.• The paper should discuss whether and how consent was obtained from people whoseasset is used.• At submission time, remember to anonymize your assets (if applicable). You can eithercreate an anonymized URL or include an anonymized zip file.14. Crowdsourcing and research with human subjectsQuestion: For crowdsourcing experiments and research with human subjects, does the paperinclude the full text of instructions given to participants and screenshots, if applicable, aswell as details about compensation (if any)?Answer: \[NA\]Justification: The paper does not involve crowdsourcing or research with human subjects.Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should beincluded in the main paper.• According to the NeurIPS Code of Ethics, workers involved in data collection, curation,or other labor should be paid at least the minimum wage in the country of the datacollector.15. Institutional review board (IRB) approvals or equivalent for research with humansubjectsQuestion: Does the paper describe potential risks incurred by study participants, whethersuch risks were disclosed to the subjects, and whether Institutional Review Board (IRB)approvals (or an equivalent approval/review based on the requirements of your country orinstitution) were obtained?Answer: \[NA\]Justification: Our paper does not involve crowdsourcing or research with human subjects.Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Depending on the country in which research is conducted, IRB approval (or equivalent)may be required for any human subjects research. If you obtained IRB approval, youshould clearly state this in the paper.• We recognize that the procedures for this may vary significantly between institutionsand locations, and we expect authors to adhere to the NeurIPS Code of Ethics and theguidelines for their institution.• For initial submissions, do not include any information that would break anonymity (ifapplicable), such as the institution conducting the review.16. Declaration of LLM usageQuestion: Does the paper describe the usage of LLMs if it is an important, original, ornon-standard component of the core methods in this research? Note that if the LLM is usedonly for writing, editing, or formatting purposes and does not impact the core methodology,scientific rigorousness, or originality of the research, declaration is not required.Answer: \[NA\]Justification: The core method development in this research does not involve LLMs.Guidelines:• The answer NA means that the core method development in this research does notinvolve LLMs as any important, original, or non-standard components.• Please refer to our LLM policy (https://neurips.cc/Conferences/2025/LLM)for what should or should not be described.A
			-> WARNING: No results were found through the dblp search! | WARNING: None of the 998 results matched the expected title!



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

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/9 MTRec/ranking_results_fig.jpg]]

### References and Their Rankings

- Advances in Neural Information Processing Systems (was NIPS)
	- Parsed as: Advances in Neural Information Processing Systems
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 5
- arXiv
	- References literatures count from this outlet: 3
- ACM International Conference on Research and Development in Information Retrieval
	- Parsed as: Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 2
- ACM International Conference on Knowledge Discovery and Data Mining
	- Parsed as: Proceedings of the 24th ACM SIGKDD international conference on knowledge discovery and data mining
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- International World Wide Web Conference
	- Parsed as: Proceedings of the 2018 world wide web conference
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- ACM International Conference on Research and Development in Information Retrieval
	- Parsed as: Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- National Conference of the American Association for Artificial Intelligence
	- Parsed as: Proceedings of the AAAI Conference on Artificial Intelligence
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- ACM International Conference on Research and Development in Information Retrieval
	- Parsed as: Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- IEEE International Conference on Data Mining
	- Parsed as: 2016 IEEE 16th international conference on data mining
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = C
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- IEEE International Conference on Data Mining
	- Parsed as: Proceedings of the International Conference on Data Mining
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = C
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- ACM International Conference on Web Search and Data Mining
	- Parsed as: Proceedings of the 14th ACM International Conference on Web Search and Data Mining
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A
	- References literatures count from this outlet: 1
- Proceedings of the ADKDD’17
	- References literatures count from this outlet: 1
- Advances in Neural Information Processing Systems (was NIPS)
	- Parsed as: advances in neural information processing systems
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- National Conference of the American Association for Artificial Intelligence
	- Parsed as: Proceedings of the AAAI Conference on Artificial Intelligence, volume 33
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- ARTIFICIAL INTELLIGENCE REVIEW
	- Parsed as: Artificial Intelligence
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = 13.4
	- References literatures count from this outlet: 1
- National Conference of the American Association for Artificial Intelligence
	- Parsed as: Proceedings of the AAAI conference on artificial intelligence, volume 33
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- National Conference of the American Association for Artificial Intelligence
	- Parsed as: Proceedings of the 33rd AAAI Conference on Artificial Intelligence
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- National Conference of the American Association for Artificial Intelligence
	- Parsed as: Proceedings of the 23rd AAAI Conference on Artificial Intelligence
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- ACM International Conference on Research and Development in Information Retrieval
	- Parsed as: Proceedings of the 38th international ACM SIGIR conference on research and development in information retrieval
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- International Conference on Learning Representations
	- Parsed as: International Conference on Learning Representations
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- ACM TRANSACTIONS ON INFORMATION SYSTEMS
	- Parsed as: ACM Transactions on Information Systems
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = 7.8
	- References literatures count from this outlet: 1
- International Conference on Machine Learning
	- Parsed as: International conference on machine learning
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- International Joint Conference on Artificial Intelligence
	- Parsed as: Proceedings of the 26th International Joint Conference on Artificial Intelligence
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- ACM International Conference on Web Search and Data Mining
	- Parsed as: Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A
	- References literatures count from this outlet: 1
- PATTERN RECOGNITION LETTERS
	- Parsed as: Pattern recognition letters
	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = 2.9
	- References literatures count from this outlet: 1
- International Joint Conference on Artificial Intelligence
	- Parsed as: Proceedings of the 20th International Joint Conference on Artificial Intelligence
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- International World Wide Web Conference
	- Parsed as: Proceedings of the Web Conference
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- ACM International Conference on Recommender Systems
	- Parsed as: Proceedings of the 10th ACM Conference on Recommender Systems
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A
	- References literatures count from this outlet: 1
- Proceedings of the 1st workshop on deep learning for recommender systems
	- References literatures count from this outlet: 1
- ACM International Conference on Information and Knowledge Management
	- Parsed as: Proceedings of the 30th ACM International Conference on Information and Knowledge Management
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A
	- References literatures count from this outlet: 1
- ACM International Conference on Web Search and Data Mining
	- Parsed as: Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A
	- References literatures count from this outlet: 1
- Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations A No or NA answer to this question will not be perceived well by the reviewers • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes] Justification: The limitation is discussed in Appendix A 5 Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper • The authors are encouraged to create a separate "Limitations" section in their paper • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e g , independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally) The authors should reflect on how these assumptions might be violated in practice and what the implications would be • The authors should reflect on the scope of the claims made, e g , if the approach was only tested on a few datasets or with a few runs In general, empirical results often depend on implicit assumptions, which should be articulated • The authors should reflect on the factors that influence the performance of the approach For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community Reviewers will be specifically instructed to not penalize honesty concerning limitations Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: [Yes] Justification: The derivations details are provided in Appendix A  Guidelines: • The answer NA means that the paper does not include theoretical results • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced • All assumptions should be clearly stated or referenced in the statement of any theorems • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material • Theorems and Lemmas that the proof relies upon should be properly referenced Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: [Yes] Justification: The implementation details are provided in Appendix A 3 Guidelines: • The answer NA means that the paper does not include experiments • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable • Depending on the contribution, reproducibility can be accomplished in various ways For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model In general releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e g , in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully (c) If the contribution is a new model (e g , a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e g , with an open-source dataset or instructions for how to construct the dataset) (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility In the case of closed-source models, it may be that access to the model is limited in some way (e g , to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results
	- References literatures count from this outlet: 1



---
## Extracted References

- **Number 1:**
	- Ref. ID: *Brian et al, 2008*
	- Authors: *Ziebart Brian, Andrew Maas, Andrew Bagnell, and Anind Dey*
	- Normalized Authors: `['Brian Z.', 'Maas A.', 'Bagnell A.', 'Dey A.']`
	- Authors contain 'et al.': *False*
	- Title: *Maximum entropy inverse reinforcement learning*
	- Year: *2008*
	- Outlet: *Proceedings of the 23rd AAAI Conference on Artificial Intelligence*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 2:**
	- Ref. ID: *Chen et al, 2021a*
	- Authors: *Hong Chen, Yudong Chen, Xin Wang, Ruobing Xie, Rui Wang, Feng Xia, and Wenwu Zhu*
	- Normalized Authors: `['Chen H.', 'Chen Y.', 'Wang X.', 'Xie R.', 'Wang R.', 'Xia F.', 'Zhu W.']`
	- Authors contain 'et al.': *False*
	- Title: *Curriculum disentangled recommendation with noisy multi-feedback*
	- Year: *2021*
	- Outlet: *Advances in Neural Information Processing Systems*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 3:**
	- Ref. ID: *Chen et al, 2019*
	- Authors: *Minmin Chen, Alex Beutel, Paul Covington, Sagar Jain, Francois Belletti, and Ed H  Chi*
	- Normalized Authors: `['Chen M.', 'Beutel A.', 'Covington P.', 'Jain S.', 'Belletti F.', 'Chi E.']`
	- Authors contain 'et al.': *False*
	- Title: *Top-k off-policy correction for a REINFORCE recommender system*
	- Year: *2019*
	- Outlet: *Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining*
	- Link: **
	- **Valid?**: *CHECK - Year (2018) does not match expected year (2019)*
- **Number 4:**
	- Ref. ID: *Chen et al, 2021b*
	- Authors: *Xiaocong Chen, Lina Yao, Aixin Sun, Xianzhi Wang, Xiwei Xu, and Liming Zhu*
	- Normalized Authors: `['Chen X.', 'Yao L.', 'Sun A.', 'Wang X.', 'Xu X.', 'Zhu L.']`
	- Authors contain 'et al.': *False*
	- Title: *Generative inverse deep reinforcement learning for online recommendation*
	- Year: *2021*
	- Outlet: *Proceedings of the 30th ACM International Conference on Information and Knowledge Management*
	- Link: **
	- **Valid?**: *CHECK - Year (2020) does not match expected year (2021)*
- **Number 5:**
	- Ref. ID: *Cheng et al, 2016*
	- Authors: *Heng-Tze Cheng, Levent Koc, Jeremiah Harmsen, Tal Shaked, Tushar Chandra, Hrishi Aradhye, Glen Anderson, Greg Corrado, Wei Chai, Mustafa Ispir, et al*
	- Normalized Authors: `['Cheng H.', 'Koc L.', 'Harmsen J.', 'Shaked T.', 'Chandra T.', 'Aradhye H.', 'Anderson G.', 'Corrado G.', 'Chai W.', 'Ispir M.']`
	- Authors contain 'et al.': *True*
	- Title: *Wide & deep learning for recommender systems*
	- Year: *2016*
	- Outlet: *Proceedings of the 1st workshop on deep learning for recommender systems*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 6:**
	- Ref. ID: *Covington et al, 2016*
	- Authors: *Paul Covington, Jay Adams, Emre Sargin, and Mengchen Zhao*
	- Normalized Authors: `['Covington P.', 'Adams J.', 'Sargin E.', 'Zhao M.']`
	- Authors contain 'et al.': *False*
	- Title: *Deep neural networks for youtube recommendations*
	- Year: *2016*
	- Outlet: *Proceedings of the 10th ACM Conference on Recommender Systems*
	- Link: **
	- **Valid?**: *CHECK - Authors () did not match found publication titled 'Deep Neural Networks for YouTube Recommendations'*
- **Number 7:**
	- Ref. ID: *Dai et al, 2021*
	- Authors: *Xinyi Dai, Jianghao Lin, Weinan Zhang, Shuai Li, Weiwen Liu, Ruiming Tang, Xiuqiang He, Jianye Hao, Jun Wang, and Yong Yu*
	- Normalized Authors: `['Dai X.', 'Lin J.', 'Zhang W.', 'Li S.', 'Liu W.', 'Tang R.', 'He X.', 'Hao J.', 'Wang J.', 'Yu Y.']`
	- Authors contain 'et al.': *False*
	- Title: *An adversarial imitation click model for information retrieval*
	- Year: *2021*
	- Outlet: *Proceedings of the Web Conference*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 8:**
	- Ref. ID: *Deepak and Amir, 2007*
	- Authors: *Ramachandran Deepak and Eyal Amir*
	- Normalized Authors: `['Deepak R.', 'Amir E.']`
	- Authors contain 'et al.': *False*
	- Title: *Bayesian inverse reinforcement learning*
	- Year: *2007*
	- Outlet: *Proceedings of the 20th International Joint Conference on Artificial Intelligence*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 9:**
	- Ref. ID: *Dong et al, 2023*
	- Authors: *Hanze Dong, Wei Xiong, Deepanshu Goyal, Rui Pan, Shizhe Diao, Jipeng Zhang, Kashun Shum, and Tong Zhang*
	- Normalized Authors: `['Dong H.', 'Xiong W.', 'Goyal D.', 'Pan R.', 'Diao S.', 'Zhang J.', 'Shum K.', 'Zhang T.']`
	- Authors contain 'et al.': *False*
	- Title: *Raft: Reward ranked finetuning for generative foundation model alignment.*
	- Year: *2023*
	- Outlet: **
	- Link: **
	- **Valid?**: *CHECK - Authors (0015, Chow, 0002, 0001) did not match found publication titled 'RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment.'*
- **Number 10:**
	- Ref. ID: *Fawcett, 2006*
	- Authors: *Tom Fawcett*
	- Normalized Authors: `['Fawcett T.']`
	- Authors contain 'et al.': *False*
	- Title: *An introduction to roc analysis*
	- Year: *2006*
	- Outlet: *Pattern recognition letters*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 11:**
	- Ref. ID: *Garg et al, 2021*
	- Authors: *Divyansh Garg, Shuvam Chakraborty, Chris Cundy, Jiaming Song, and Stefano Ermon*
	- Normalized Authors: `['Garg D.', 'Chakraborty S.', 'Cundy C.', 'Song J.', 'Ermon S.']`
	- Authors contain 'et al.': *False*
	- Title: *Iq-learn: Inverse soft-q learning for imitation*
	- Year: *2021*
	- Outlet: *Advances in Neural Information Processing Systems*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 12:**
	- Ref. ID: *Gilotte et al, 2018*
	- Authors: *Alexandre Gilotte, Clément Calauzènes, Thomas Nedelec, Alexandre Abraham, and Simon Dollé*
	- Normalized Authors: `['Gilotte A.', 'Calauzènes C.', 'Nedelec T.', 'Abraham A.', 'Dollé S.']`
	- Authors contain 'et al.': *False*
	- Title: *Offline a/b testing for recommender systems*
	- Year: *2018*
	- Outlet: *Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 13:**
	- Ref. ID: *Guo et al, 2017*
	- Authors: *Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, and Xiuqiang He*
	- Normalized Authors: `['Guo H.', 'Tang R.', 'Ye Y.', 'Li Z.', 'He X.']`
	- Authors contain 'et al.': *False*
	- Title: *Deepfm: a factorizationmachine based neural network for ctr prediction*
	- Year: *2017*
	- Outlet: *Proceedings of the 26th International Joint Conference on Artificial Intelligence*
	- Link: **
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: None of the 4 results matched the expected title!*
- **Number 14:**
	- Ref. ID: *Haarnoja et al, 2018*
	- Authors: *Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine*
	- Normalized Authors: `['Haarnoja T.', 'Zhou A.', 'Abbeel P.', 'Levine S.']`
	- Authors contain 'et al.': *False*
	- Title: *Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor*
	- Year: *2018*
	- Outlet: *International conference on machine learning*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 15:**
	- Ref. ID: *Jaedeug and Kim, 2012*
	- Authors: *Choi Jaedeug and Kee-Eung Kim*
	- Normalized Authors: `['Jaedeug C.', 'Kim K.']`
	- Authors contain 'et al.': *False*
	- Title: *Nonparametric bayesian inverse reinforcement learning for multiple reward functions*
	- Year: *2012*
	- Outlet: *Advances in Neural Information Processing Systems*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 16:**
	- Ref. ID: *Jiawei et al, 2023*
	- Authors: *Chen Jiawei, Hande Dong, Xiang Wang, Fuli Feng, Meng Wang, and Xiangnan He*
	- Normalized Authors: `['Jiawei C.', 'Dong H.', 'Wang X.', 'Feng F.', 'Wang M.', 'He X.']`
	- Authors contain 'et al.': *False*
	- Title: *Bias and debias in recommender system: A survey and future directions*
	- Year: *2023*
	- Outlet: *ACM Transactions on Information Systems*
	- Link: **
	- **Valid?**: *CHECK - Year (2020) does not match expected year (2023)*
- **Number 17:**
	- Ref. ID: *Jonathan and Ermon, 2016*
	- Authors: *Ho Jonathan and Stefano Ermon*
	- Normalized Authors: `['Jonathan H.', 'Ermon S.']`
	- Authors contain 'et al.': *False*
	- Title: *Generative adversarial imitation learning*
	- Year: *2016*
	- Outlet: *Advances in Neural Information Processing Systems*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 18:**
	- Ref. ID: *Kingma and Ba, 2015*
	- Authors: *Diederik P  Kingma and Jimmy Ba*
	- Normalized Authors: `['Kingma D.', 'Ba J.']`
	- Authors contain 'et al.': *False*
	- Title: *Deepfm: a factorization-machine based neural network for ctr prediction*
	- Year: *2015*
	- Outlet: *International Conference on Learning Representations*
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: None of the 1 results matched the expected title!*
- **Number 19:**
	- Ref. ID: *Liu et al, 2023a*
	- Authors: *Jialin Liu, Xinyan Su, Zeyu He, Xiangyu Zhao, and Jun Li*
	- Normalized Authors: `['Liu J.', 'Su X.', 'He Z.', 'Zhao X.', 'Li J.']`
	- Authors contain 'et al.': *False*
	- Title: *Adversarial batch inverse reinforcement learning: Learn to reward from imperfect demonstration for interactive recommendation*
	- Year: *2023*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 20:**
	- Ref. ID: *Liu et al, 2023b*
	- Authors: *Langming Liu, Liu Cai, Chi Zhang, Xiangyu Zhao, Jingtong Gao, Wanyu Wang, Yifu Lv, Wenqi Fan, Yiqi Wang, Ming He, et al*
	- Normalized Authors: `['Liu L.', 'Cai L.', 'Zhang C.', 'Zhao X.', 'Gao J.', 'Wang W.', 'Lv Y.', 'Fan W.', 'Wang Y.', 'He M.']`
	- Authors contain 'et al.': *True*
	- Title: *Linrec: Linear attention mechanism for long-term sequential recommender systems*
	- Year: *2023*
	- Outlet: *Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval*
	- Link: **
	- **Valid?**: *CHECK - Authors () did not match found publication titled 'LinRec: Linear Attention Mechanism for Long-term Sequential Recommender Systems'*
- **Number 21:**
	- Ref. ID: *Liu et al, 2024*
	- Authors: *Ziwei Liu, Qidong Liu, Yejing Wang, Wanyu Wang, Pengyue Jia, Maolin Wang, Zitao Liu, Yi Chang, and Xiangyu Zhao*
	- Normalized Authors: `['Liu Z.', 'Liu Q.', 'Wang Y.', 'Wang W.', 'Jia P.', 'Wang M.', 'Liu Z.', 'Chang Y.', 'Zhao X.']`
	- Authors contain 'et al.': *False*
	- Title: *Bidirectional gated mamba for sequential recommendation*
	- Year: *2024*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 22:**
	- Ref. ID: *McAuley et al, 2015*
	- Authors: *Julian McAuley, Christopher Targett, Qinfeng Shi, and Anton Van Den Hengel*
	- Normalized Authors: `['McAuley J.', 'Targett C.', 'Shi Q.', 'Hengel A.']`
	- Authors contain 'et al.': *False*
	- Title: *Image-based recommendations on styles and substitutes*
	- Year: *2015*
	- Outlet: *Proceedings of the 38th international ACM SIGIR conference on research and development in information retrieval*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 23:**
	- Ref. ID: *Ouyang et al, 2022*
	- Authors: *Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Gray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, and Ryan Lowe*
	- Normalized Authors: `['Ouyang L.', 'Wu J.', 'Jiang X.', 'Almeida D.', 'Wainwright C.', 'Mishkin P.', 'Zhang C.', 'Agarwal S.', 'Slama K.', 'Gray A.', 'Schulman J.', 'Hilton J.', 'Kelton F.', 'Miller L.', 'Simens M.', 'Askell A.', 'Welinder P.', 'Christiano P.', 'Leike J.', 'Lowe R.']`
	- Authors contain 'et al.': *False*
	- Title: *Training language models to follow instructions with human feedback*
	- Year: *2022*
	- Outlet: *Advances in Neural Information Processing Systems*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 24:**
	- Ref. ID: *Qu et al, 2016*
	- Authors: *Yanru Qu, Han Cai, Kan Ren, Weinan Zhang, Yong Yu, Ying Wen, and Jun Wang*
	- Normalized Authors: `['Qu Y.', 'Cai H.', 'Ren K.', 'Zhang W.', 'Yu Y.', 'Wen Y.', 'Wang J.']`
	- Authors contain 'et al.': *False*
	- Title: *Product-based neural networks for user response prediction*
	- Year: *2016*
	- Outlet: *2016 IEEE 16th international conference on data mining*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 25:**
	- Ref. ID: *Saurabh and Doshi, 2021*
	- Authors: *Arora Saurabh and Prashant Doshi*
	- Normalized Authors: `['Saurabh A.', 'Doshi P.']`
	- Authors contain 'et al.': *False*
	- Title: *A survey of inverse reinforcement learning: Challenges, methods and progress*
	- Year: *2021*
	- Outlet: *Artificial Intelligence*
	- Link: **
	- **Valid?**: *CHECK - Year (2018) does not match expected year (2021)*
- **Number 26:**
	- Ref. ID: *Schulman et al, 2017*
	- Authors: *John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov*
	- Normalized Authors: `['Schulman J.', 'Wolski F.', 'Dhariwal P.', 'Radford A.', 'Klimov O.']`
	- Authors contain 'et al.': *False*
	- Title: *Proximal policy optimization algorithms*
	- Year: *2017*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 27:**
	- Ref. ID: *Shi et al, 2019*
	- Authors: *Jing-Cheng Shi, Yang Yu, Qing Da, Shi-Yong Chen, and An-Xiang Zeng*
	- Normalized Authors: `['Shi J.', 'Yu Y.', 'Da Q.', 'Chen S.', 'Zeng A.']`
	- Authors contain 'et al.': *False*
	- Title: *Virtual-taobao: Virtualizing real-world online retail environment for reinforcement learning*
	- Year: *2019*
	- Outlet: *Proceedings of the AAAI Conference on Artificial Intelligence, volume 33*
	- Link: **
	- **Valid?**: *CHECK - Year (2018) does not match expected year (2019)*
- **Number 28:**
	- Ref. ID: *Swaminathan and Joachims, 2015*
	- Authors: *Adith Swaminathan and Thorsten Joachims*
	- Normalized Authors: `['Swaminathan A.', 'Joachims T.']`
	- Authors contain 'et al.': *False*
	- Title: *The self-normalized estimator for counterfactual learning*
	- Year: *2015*
	- Outlet: *advances in neural information processing systems*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 29:**
	- Ref. ID: *Wang et al, 2017*
	- Authors: *Ruoxi Wang, Bin Fu, Gang Fu, and Mingliang Wang*
	- Normalized Authors: `['Wang R.', 'Fu B.', 'Fu G.', 'Wang M.']`
	- Authors contain 'et al.': *False*
	- Title: *Deep & cross network for ad click predictions*
	- Year: *2017*
	- Outlet: *Proceedings of the ADKDD’17*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 30:**
	- Ref. ID: *Wang et al, 2021*
	- Authors: *Wenjie Wang, Fuli Feng, Xiangnan He, Liqiang Nie, and Tat-Seng Chua*
	- Normalized Authors: `['Wang W.', 'Feng F.', 'He X.', 'Nie L.', 'Chua T.']`
	- Authors contain 'et al.': *False*
	- Title: *Denoising implicit feedback for recommendation*
	- Year: *2021*
	- Outlet: *Proceedings of the 14th ACM International Conference on Web Search and Data Mining*
	- Link: **
	- **Valid?**: *CHECK - Year (2020) does not match expected year (2021)*
- **Number 31:**
	- Ref. ID: *Wang-Cheng and McAuley, 2018*
	- Authors: *Kang Wang-Cheng and Julian McAuley*
	- Normalized Authors: `['Wang-Cheng K.', 'McAuley J.']`
	- Authors contain 'et al.': *False*
	- Title: *Self-attentive sequential recommendation*
	- Year: *2018*
	- Outlet: *Proceedings of the International Conference on Data Mining*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 32:**
	- Ref. ID: *Will et al, 2018*
	- Authors: *Dabney Will, Mark Rowland, Marc Bellemare, and Rémi Munos*
	- Normalized Authors: `['Will D.', 'Rowland M.', 'Bellemare M.', 'Munos R.']`
	- Authors contain 'et al.': *False*
	- Title: *Distributional reinforcement learning with quantile regression*
	- Year: *2018*
	- Outlet: *Proceedings of the 33rd AAAI Conference on Artificial Intelligence*
	- Link: **
	- **Valid?**: *CHECK - Year (2017) does not match expected year (2018)*
- **Number 33:**
	- Ref. ID: *Lee et al, 2021*
	- Authors: *Jae woong Lee, Seongmin Park, Jongwuk Lee, and mengchen zhao*
	- Normalized Authors: `['Lee J.', 'Park S.', 'Lee J.', 'zhao m.']`
	- Authors contain 'et al.': *False*
	- Title: *Dual unbiased recommender learning for implicit feedback*
	- Year: *2021*
	- Outlet: *Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval*
	- Link: **
	- **Valid?**: *CHECK - Authors () did not match found publication titled 'Dual Unbiased Recommender Learning for Implicit Feedback'*
- **Number 34:**
	- Ref. ID: *Yang et al, 2021*
	- Authors: *Jiaqi Yang, Xiang Li, Shuguang Han, Tao Zhuang, Dechuan Zhan, Xiaoyi Zeng, and Bin Tong*
	- Normalized Authors: `['Yang J.', 'Li X.', 'Han S.', 'Zhuang T.', 'Zhan D.', 'Zeng X.', 'Tong B.']`
	- Authors contain 'et al.': *False*
	- Title: *Capturing delayed feedback in conversion rate prediction via elapsed-time sampling*
	- Year: *2021*
	- Outlet: *Proceedings of the AAAI Conference on Artificial Intelligence*
	- Link: **
	- **Valid?**: *CHECK - Year (2020) does not match expected year (2021)*
- **Number 35:**
	- Ref. ID: *Yi et al, 2023*
	- Authors: *Ren Yi, Hongyan Tang, Jiangpeng Rong, and Siwen Zhu*
	- Normalized Authors: `['Yi R.', 'Tang H.', 'Rong J.', 'Zhu S.']`
	- Authors contain 'et al.': *False*
	- Title: *Unbiased pairwise learning from implicit feedback for recommender systems without biased variance control*
	- Year: *2023*
	- Outlet: *Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 36:**
	- Ref. ID: *Yu and Qin, 2020*
	- Authors: *Wenhui Yu and Zheng Qin*
	- Normalized Authors: `['Yu W.', 'Qin Z.']`
	- Authors contain 'et al.': *False*
	- Title: *Sampler design for implicit feedback data by noisy-label robust learning*
	- Year: *2020*
	- Outlet: *Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 37:**
	- Ref. ID: *Zheng et al, 2018*
	- Authors: *Guanjie Zheng, Fuzheng Zhang, Zihan Zheng, Yang Xiang, Nicholas Jing Yuan, Xing Xie, and Zhenhui Li*
	- Normalized Authors: `['Zheng G.', 'Zhang F.', 'Zheng Z.', 'Xiang Y.', 'Yuan N.', 'Xie X.', 'Li Z.']`
	- Authors contain 'et al.': *False*
	- Title: *DRN: A deep reinforcement learning framework for news recommendation*
	- Year: *2018*
	- Outlet: *Proceedings of the 2018 world wide web conference*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 38:**
	- Ref. ID: *Zhou et al, 2018*
	- Authors: *Guorui Zhou, Xiaoqiang Zhu, Chenru Song, Ying Fan, Han Zhu, Xiao Ma, Yanghui Yan, Junqi Jin, Han Li, and Kun Gai*
	- Normalized Authors: `['Zhou G.', 'Zhu X.', 'Song C.', 'Fan Y.', 'Zhu H.', 'Ma X.', 'Yan Y.', 'Jin J.', 'Li H.', 'Gai K.']`
	- Authors contain 'et al.': *False*
	- Title: *Deep interest network for click-through rate prediction*
	- Year: *2018*
	- Outlet: *Proceedings of the 24th ACM SIGKDD international conference on knowledge discovery and data mining*
	- Link: **
	- **Valid?**: *CHECK - Authors (Dai) did not match found publication titled 'Deep Interest Network for Click-Through Rate Prediction'*
- **Number 39:**
	- Ref. ID: *Zhou et al, 2019*
	- Authors: *Guorui Zhou, Na Mou, Ying Fan, Qi Pi, Weijie Bian, Chang Zhou, Xiaoqiang Zhu, and Kun Gai*
	- Normalized Authors: `['Zhou G.', 'Mou N.', 'Fan Y.', 'Pi Q.', 'Bian W.', 'Zhou C.', 'Zhu X.', 'Gai K.']`
	- Authors contain 'et al.': *False*
	- Title: *Deep interest evolution network for click-through rate prediction*
	- Year: *2019*
	- Outlet: *Proceedings of the AAAI conference on artificial intelligence, volume 33*
	- Link: **
	- **Valid?**: *CHECK - Year (2018) does not match expected year (2019)*
- **Number 40:**
	- Ref. ID: *1, 0*
	- Authors: *NeurIPS Paper Checklist 1*
	- Normalized Authors: `['1 N.']`
	- Authors contain 'et al.': *False*
	- Title: *Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: Our main contribution is the MTRec framework with the QR-IQL algorithm, which is described in Section 4 and justified in Section 5*
	- Year: *0*
	- Outlet: *Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations A No or NA answer to this question will not be perceived well by the reviewers • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes] Justification: The limitation is discussed in Appendix A 5 Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper • The authors are encouraged to create a separate "Limitations" section in their paper • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e g , independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally) The authors should reflect on how these assumptions might be violated in practice and what the implications would be • The authors should reflect on the scope of the claims made, e g , if the approach was only tested on a few datasets or with a few runs In general, empirical results often depend on implicit assumptions, which should be articulated • The authors should reflect on the factors that influence the performance of the approach For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community Reviewers will be specifically instructed to not penalize honesty concerning limitations Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: [Yes] Justification: The derivations details are provided in Appendix A  Guidelines: • The answer NA means that the paper does not include theoretical results • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced • All assumptions should be clearly stated or referenced in the statement of any theorems • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material • Theorems and Lemmas that the proof relies upon should be properly referenced Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: [Yes] Justification: The implementation details are provided in Appendix A 3 Guidelines: • The answer NA means that the paper does not include experiments • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable • Depending on the contribution, reproducibility can be accomplished in various ways For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model In general releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e g , in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully (c) If the contribution is a new model (e g , a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e g , with an open-source dataset or instructions for how to construct the dataset) (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility In the case of closed-source models, it may be that access to the model is limited in some way (e g , to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results*
	- Link: *https://nips.cc/public/guides/CodeSubmissionPolicy)*
	- **Valid?**: *WARNING: No results were found through the dblp search! | WARNING: None of the 998 results matched the expected title!*



---
## Full List of Reference Support Check

**Sentences with references to papers that are thematically related / relevant papers but REFUTE the statement they are referenced in:**
- None

**Sentences with references to papers that are thematically related / relevant papers that we had not enough info about to determine the stance on the statement they are referenced in:**
- '*Prior studies treat erroneous feedback signals as noisy labels and applying denoising techniques to address them, yet their effectiveness remains limited because erroneous feedback is not random noise by its nature Wang et al [2021]*'
	- This flag is for the paper with Ref. ID = Wang et al, 2021
- '*Therefore, most existing works focus on optimizing some surrogate objectives such as click-through rate and conversion rate Wang et al [2017], Zhou et al [2019]*'
	- This flag is for the paper with Ref. ID = Zhou et al, 2019

**Sentences with references to papers that are thematically related / relevant papers that SUPPORT the statement they are referenced in:**
- '*Existing works usually model the recommender system as agent, who recommends items and receives user feedback as reward Zheng et al [2018], Chen et al [2019]*'
	- This flag is for the paper with Ref. ID = Chen et al, 2019
- '*2 Uncovering the Mental Reward Model Inverse reinforcement learning (IRL) aims to find a reward model that explains behaviors of the expert policy Saurabh and Doshi [2021]*'
	- This flag is for the paper with Ref. ID = Saurabh and Doshi, 2021


**Sentences with references to papers that seem thematically unrelated / irrelevant:**
- '*[2020], Wang et al [2021]*'
	- This flag is for the paper with Ref. ID = Wang et al, 2021
- '*, click, video watching) to train recommendation models Covington et al [2016], Zhou et al [2018], Dai et al [2021], Yang et al [2021]*'
	- This flag is for the paper with Ref. ID = Yang et al, 2021
- '*, click, video watching) to train recommendation models Covington et al [2016], Zhou et al [2018], Dai et al [2021], Yang et al [2021]*'
	- This flag is for the paper with Ref. ID = Yang et al, 2021


**Sentences with references to papers that we didn't have an abstract for to check against:**
- '*Conventionally, maximum entropy IRL aims to learn a deterministic reward function r : S × A →R by solving Problem 2 Brian et al [2008]*'
	- This flag is for the paper with Ref. ID = Brian et al, 2008
- '*1 A distributional perspective on IRL Conventional IRL methods such as MaxEntIRL iteratively optimize the reward function and the policy until convergence Brian et al [2008]*'
	- This flag is for the paper with Ref. ID = Brian et al, 2008
- '*Some alternative methods attempt to mitigate erroneous feedback via multi-feedback fusion, yet they often struggle when confronted with conflicting feedback Chen et al [2021a]*'
	- This flag is for the paper with Ref. ID = Chen et al, 2021a
- '*Reward rAnked FineTuning (RAFT) uses a reward model to select the best set of training samples based on model outputs Dong et al [2023]*'
	- This flag is for the paper with Ref. ID = Dong et al, 2023
- '*We use the following two metrics: Area Under Curve (AUC) Fawcett [2006] and Normalised Capped Importance Sampling (NCIS) Swaminathan and Joachims [2015]*'
	- This flag is for the paper with Ref. ID = Fawcett, 2006
- '*AUC is used to measure the model’s ranking ability and NCIS is used to approximate the model’s online performance Gilotte et al [2018]*'
	- This flag is for the paper with Ref. ID = Gilotte et al, 2018
- '*Then, the inner problem becomes trivial so that Problem 3 can be reformulated as follows Brian et al [2008], Haarnoja et al [2018]*'
	- This flag is for the paper with Ref. ID = Haarnoja et al, 2018
- '*We use Proximal Policy Optimization (PPO) Schulman et al [2017] and Soft Actor-Critic (SAC) Haarnoja et al [2018] as baselines*'
	- This flag is for the paper with Ref. ID = Haarnoja et al, 2018
- '*functions and focus on estimating their posterior distribution using Bayes’ rule Deepak and Amir [2007], Jaedeug and Kim [2012]*'
	- This flag is for the paper with Ref. ID = Jaedeug and Kim, 2012
- '*Then, Problem 2 can rewritten as: max r∈R min π∈Π EρE[r(s, a)] −Eρ[r(s, a)] −H(π) −ϕ(r), (3) where ϕ is a convex regularizer on r Jonathan and Ermon [2016]*'
	- This flag is for the paper with Ref. ID = Jonathan and Ermon, 2016
- '*Some works apply IRL to infer the reward function for the recommender system, assuming expert recommendation policies are available Chen et al [2021b], Liu et al [2023a]*'
	- This flag is for the paper with Ref. ID = Liu et al, 2023a
- '*The Amazon dataset McAuley et al [2015] collects user review data from Amazon e-commerce platform*'
	- This flag is for the paper with Ref. ID = McAuley et al, 2015
- '*For example, Reinforcement Learning from Human Feedback (RLHF) learns human preferences through a reward model trained with human-rated outputs Ouyang et al [2022]*'
	- This flag is for the paper with Ref. ID = Ouyang et al, 2022
- '*In the context of LLM, the alignment problem is defined as optimizing the outputs of LLMs towards matching human values Ouyang et al [2022]*'
	- This flag is for the paper with Ref. ID = Ouyang et al, 2022
- '*We use Proximal Policy Optimization (PPO) Schulman et al [2017] and Soft Actor-Critic (SAC) Haarnoja et al [2018] as baselines*'
	- This flag is for the paper with Ref. ID = Schulman et al, 2017
- '*We use the following two metrics: Area Under Curve (AUC) Fawcett [2006] and Normalised Capped Importance Sampling (NCIS) Swaminathan and Joachims [2015]*'
	- This flag is for the paper with Ref. ID = Swaminathan and Joachims, 2015
- '*Another line of works address various types of biases in user feedback, including position bias, selection bias, popularity bias and exposure bias woong Lee et al [2021], Yi et al [2023]*'
	- This flag is for the paper with Ref. ID = Yi et al, 2023
- '*Prior works have explored using reinforcement learning (RL) to optimize recommendation policy, where the recommender system is modeled as an agent and the users are treated as key components of environment Chen et al [2019], Zheng et al [2018]*'
	- This flag is for the paper with Ref. ID = Zheng et al, 2018

