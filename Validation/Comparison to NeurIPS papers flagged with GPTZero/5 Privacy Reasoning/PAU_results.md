# Paper Analysis Utility - Results

Paper: Privacy Reasoning Partnergate Version.pdf


## Document Structure

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/5 Privacy Reasoning/chapter_fig.jpg]]

1) 'Introduction' -- p. 1 (ca. 1 pages)
2) 'Background and Related Work' -- p. 2 (ca. 1 pages)
3) 'Problem Statement' -- p. 3 (ca. 1 pages)
4) 'Context Ambiguity Analysis' -- p. 4 (ca. 1 pages)
5) 'Camber: A Context Disambiguation Framework' -- p. 5 (ca. 3 pages)
6) 'Results' -- p. 8 (ca. 1 pages)
7) 'Discussion and Limitations' -- p. 9 (ca. 1 pages)
8) 'Conclusion' -- p. 10 (ca. 1 pages)
9) 'References' -- p. 11 (ca. 9 pages)
A) 'Motivating examples from PrivacyLens+' -- p. 20 (ca. 1 pages)
B) 'Detailed Results' -- p. 21 (ca. 8 pages)
C) 'Detailed description of the Camber disambiguation framework' -- p. 29 (ca. 2 pages)
D) 'Datasets and dataset expansions' -- p. 31 (ca. 21 pages)
E) 'Evaluation' -- p. 52 (ca. 2 pages)


## Unicode Character Usage

> [!NOTE]
> *Please note that this list may contain false positives since this is feature is still in early stages of development.*

- Dashes:
	- Stats for minus signs ():
		- Valid uses: 0/114=0.00%
		- Invalid uses: 114/114=100.00%
	- Sentences with invalid dashes:
		- Lines containing invalid dashes:
		- Page 3: (denoted as S−) to measure privacy leakage, we augment them by incorporating instances where
		- Page 3: For each S−, we generate a corresponding positive scenario S+ by modifying a subset of its fields.
		- Page 3: S−, and contain 986 and 540 examples respectively. A detailed description of the dataset generation
		- Page 5: −to [Data
		- Page 5: −based
		- Page 5: example’s appropriateness label. Specifically, we generate inappropriate contexts (denoted N −) for
		- Page 5: S−examples to reinforce their inappropriateness and appropriate contexts (denoted N +) for S+
		- Page 5: context. In total, this procedure generates an additional 5 × 493 = 2,465 pairs of S−
		- Page 5: procedure, including prompts and the generated S−
		- Page 5: NI and S−
		- Page 5: adds contextual details to S−and S+ examples according to the definition of the fields in each
		- Page 5: dataset. These label-dependent contexts are either inappropriate or appropriate, denoted as N −
		- Page 6: D respectively. Incorporating these contexts yields examples denoted as S−
		- Page 6: N −
		- Page 6: both datasets, we first ask the LLM to generate N −
		- Page 6: D ) for a specific field in S−
		- Page 6: dataset, resulting in an additional 2,465 pairs of S−
		- Page 6: N −
		- Page 7: To test if codes are more effective at reducing implicit reasoning assumptions, we prompt the LLM to generate label-dependent contexts based on each code (denoted as N −
		- Page 7: C ) for all S−and S+ examples respectively in both datasets. Our instruction specifically asks
		- Page 7: then to expand the selected field following this code to make the S−more inappropriate, or S+ more
		- Page 7: we again need to further integrate N −
		- Page 7: C into S−and S+. In total, we generate an additional
		- Page 7: 9 × 493 = 4,437 pairs of S−
		- Page 7: N −
		- Page 21: −0.4
		- Page 21: −7.5
		- Page 21: −5.0
		- Page 21: −1.5
		- Page 21: −0.6
		- Page 21: −1.6
		- Page 21: −3.5
		- Page 21: −0.4
		- Page 21: −1.2
		- Page 22: −0.5
		- Page 22: −0.2
		- Page 22: −1.0
		- Page 22: −0.2
		- Page 22: −0.5
		- Page 22: −2.6
		- Page 22: −2.0
		- Page 22: −1.1
		- Page 22: −0.8
		- Page 22: −0.5
		- Page 22: −2.2
		- Page 22: −1.7
		- Page 22: −0.5
		- Page 22: −0.2
		- Page 22: −0.5
		- Page 22: −0.7
		- Page 22: −0.5
		- Page 28: Each pair of S−and S+ in PrivacyLens+ and ConfAIde+ are constructed based on a set of fields. In
		- Page 28: PrivacyLens+ each S−and S+ is an contextual integrity information flow containing 5 fields: data
		- Page 28: on one field at a time per S−or S+ example. To avoid generating additional contexts that contradicts
		- Page 28: (denoted N −) are generated for S−examples to reinforce their inappropriateness, while appropriate
		- Page 28: We denote the resulting S−and S+ with one or more fields expanded with the additional context N
		- Page 28: as S−
		- Page 28: we expand each field in S−and S+ separately with their corresponding NI to form an S−
		- Page 28: NI. The PrivacyLens dataset includes narrative stories each expanded based on an S−using an
		- Page 28: them to the relevant fields in the original S−and S+ examples. For ConfAIde+, however, these
		- Page 28: label-independent contexts need to be generated. For each of the 7 fields in an S−example (or an S+
		- Page 28: neutral context, and then integrate this expanded context into the original S−(or S+).
		- Page 28: In total, this procedure generates an additional 5 × 493 = 2465 pairs of S−
		- Page 28: including prompts and the generated S−
		- Page 28: NI and S−
		- Page 28: label-dependent contextual details to S−and S+ examples according to the definition of the fields in
		- Page 28: N −
		- Page 28: D respectively. Incorporating these contexts yields examples denoted as S−
		- Page 28: N −
		- Page 29: For both datasets, an N −
		- Page 29: in S−(or S+, respectively) to make the example more inappropriate (or appropriate, respectively).
		- Page 29: and all 7 fields in ConfAIde+, resulting in an additional 2465 pairs of S−
		- Page 29: N −
		- Page 29: reducing implicit reasoning assumptions. We denote the label-dependent contexts we add to the S−
		- Page 29: and S+ examples as, respectively N −
		- Page 29: C . To generate an N −
		- Page 29: in the expansions. This process is repeated for all S−and S+ examples in PrivacyLens+, adding
		- Page 29: an additional 9 × 493 = 4,437 pairs of S−
		- Page 29: N −
		- Page 29: LLM is additionally instructed to incorporate generated N −
		- Page 29: C into the original S−and S+
		- Page 29: examples, creating an additional 9 × 270 = 2,430 pairs of S−
		- Page 29: N −
		- Page 30: seed that defines a core privacy-norm-violating scenario. S−is then developed into an elaborate
		- Page 30: examples of negative scenarios S−, and has been used extensively by prior work [28, 5, 25].
		- Page 31: information flows. We refer to each of them as S−. Example 2 is the S−example of the Example 1
		- Page 31: Example 2: An S−example representing an inappropriate information flow in PrivacyLens+.
		- Page 31: data_subject fields of S−using the contextually appropriate information in the story. The LLM is
		- Page 31: "marital status") to align with the abstraction level of S−. Systematic application of this procedure
		- Page 31: across all original Privacylens examples yields 493 S−and 493 S+. See Prompt 1 for the procedure
		- Page 33: We generate examples with label-independent contexts, S−
		- Page 33: each S−with contextual details from its corresponding PrivacyLens story. PrivacyLens includes
		- Page 33: version of S−(Example 5). For each flow, the data_type is directly updated with this more concrete
		- Page 33: We replace fields in S−with fields generated in this step one field at a time to form S−
		- Page 35: Prompt 4: Prompt to add label-independent contexts from story to the transmission_principle field in S−.
		- Page 38: by applying this example input to Example 2 is shown in Example 8 The contexts N −
		- Page 38: generated at this step are used to replace the corresponding fields in S−and S+ to assess the
		- Page 40: Example 8: An example inappropriate contexts (N −
		- Page 40: input to the LLM, an example generated context (N −
		- Page 41: Example 9: An example inappropriate context (N −
		- Page 41: Tier 3 of the ConfAIde dataset consists of 270 seeds S−with multiple fields. We modify the original
		- Page 41: S−example describes an inappropriate scenario where an aware agent tries to disclose a sensitive
		- Page 42: expand it by creating positive equivalents. To generate the corresponding S+ for a seed S−, we
		- Page 42: prompt Gemini 2.0 Pro to generate a non-sensitive detail about the subject agent contained in S−
		- Page 43: step yields the enhanced seeds for the negative examples S−in ConfAIde. The seeds for the positive
		- Page 45: corresponding story in Example 11 is shown in Example 15. The contexts N −
		- Page 45: this step are used to replace the corresponding fields in S−and S+ and in the stories, to assess the
		- Page 46: Example 15: An example context (N −
		- Page 47: its story in Example 12 is shown in Example 16. The contexts N −
		- Page 47: used to replace the corresponding fields in S−and S+ and in the stories, to assess the information
		- Page 48: Example 16: An example context (N −
		- Page 49: Example 17. The contexts N −
		- Page 49: fields in S−and S+ and in the stories, to assess the information sharing decisions after labelindependent expansion.
		- Page 50: Example 17: An example context (N −


## References not in Bibliography

All references used in the document's (main) text were also found in the 'References' section.


## Unused References in Bibliography

All references stated in the 'References' section were also used at least once in the document's (main) text.


## Frequently Referenced Authors

> [!NOTE]
> The following authors appear more than 2 times in the bibliography.
> *Please note that only the lastname and the first letter of the first name are compared for counting.*

- Zhou X.: 4
- Choi Y.: 4
- Huang Y.: 4
- Chen Y.: 4
- Tsvetkov Y.: 3
- Wang H.: 3
- Zhang Y.: 3
- Yi R.: 3
- Ghalebikesabi S.: 3
- Li H.: 3
- Fan W.: 3
- Cheng J.: 3
- Chu T.: 3
- Hu P.: 3
- Song Y.: 3


## Reference Checker Results

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/5 Privacy Reasoning/literature_validation_results_fig.jpg]]

References section starts on page 11.

- No link provided: $31/34=91.18\%$
- Unchecked links: $0/34=0.00\%$
- Valid links: $0/34=0.00\%$
- Invalid link: $3/34=8.82\%$
	- Invalid entries:
		=> total = 3
		- \[3\] Niloofar Mireshghallah, Hyunwoo Kim, Xuhui Zhou, Yulia Tsvetkov, Maarten Sap, Reza Shokri, and Yejin Choi. Can LLMs keep a secret? testing privacy implications of language models via contextual integrity theory. In International Conference on Learning Representations (ICLR)., 2024 https://github.com/skywalker023/confAIde/tree/main/benchmark. MIT License.
			-> Returned with status code 404!
		- \[4\] Yijia Shao, Tianshi Li, Weiyan Shi, Yanchen Liu, and Diyi Yang. PrivacyLens: Evaluating privacy norm awareness of language models in action. In Proceedings of the 2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pages 1–18, Mexico City, Mexico, June 2024. Association for Computational Linguistics. https://github.com/SALT-NLP/PrivacyLens. MIT License.
			-> Returned with status code 404!
		- \[34\] M. Ariel Cascio, Eunlye Lee, Nicole Vaudrin, and Darcy A. Freedman. A team-based approach to open coding: Considerations for creating intercoder consensus. Field Methods, 31:116–130, 2019. NeurIPS Paper Checklist 1. Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: \[Yes\] Justification: We did our best to summarize our approach to surface limitations of the state of-the-art, as well as our subsequent contributions to improve it. Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper. • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers. • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper. 2. Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: \[Yes\] Justification: We explicitly address limitations in Section 7. Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate "Limitations" section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. • The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. • The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations. 3. Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: \[NA\] Justification: The paper does not include theoretical results. Guidelines: • The answer NA means that the paper does not include theoretical results. • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced. • All assumptions should be clearly stated or referenced in the statement of any theorems. • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. • Theorems and Lemmas that the proof relies upon should be properly referenced. 4. Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: \[Yes\] Justification: The paper’s results can be reproduced using public datasets and inference calls to existing public LLM APIs, for which we provide version and checkpoint information. Guidelines: • The answer NA means that the paper does not include experiments. • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. • Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results. 5. Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? Answer: \[Yes\] Justification: Our dataset is available at https://github.com/google-parfait/contextual-privacy-and-security.Guidelines:• The answer NA means that paper does not include experiments requiring code.• Please see the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• While we encourage the release of code and data, we understand that this might not bepossible, so “No” is an acceptable answer. Papers cannot be rejected simply for notincluding code, unless this is central to the contribution (e.g., for a new open-sourcebenchmark).• The instructions should contain the exact command and environment needed to run toreproduce the results. See the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• The authors should provide instructions on data access and preparation, including howto access the raw data, preprocessed data, intermediate data, and generated data, etc.• The authors should provide scripts to reproduce all experimental results for the newproposed method and baselines. If only a subset of experiments are reproducible, theyshould state which ones are omitted from the script and why.• At submission time, to preserve anonymity, the authors should release anonymizedversions (if applicable).• Providing as much information as possible in supplemental material (appended to thepaper) is recommended, but including URLs to data and code is permitted.6. Experimental setting/detailsQuestion: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand theresults?Answer: \[Yes\]Justification: We describe all prompts, as well as data slit sizes for coding, in the appendixof the paper.Guidelines:• The answer NA means that the paper does not include experiments.• The experimental setting should be presented in the core of the paper to a level of detailthat is necessary to appreciate the results and make sense of them.• The full details can be provided either with the code, in appendix, or as supplementalmaterial.7. Experiment statistical significanceQuestion: Does the paper report error bars suitably and correctly defined or other appropriateinformation about the statistical significance of the experiments?Answer: \[Yes\] .Justification: In all our evaluations with LLMs we set temperature to 0, which in most of ourcases (predicting ‘yes‘ or ‘no‘) results in the same output being produced across executions.In any plots where there’s a small variance in our results due to a bigger output space,e.g., when we use LLMs to generate additional context, we obtain confidence intervals viabootstrapping.Guidelines:• The answer NA means that the paper does not include experiments.• The authors should answer "Yes" if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that supportthe main claims of the paper.• The factors of variability that the error bars are capturing should be clearly stated (forexample, train/test split, initialization, random drawing of some parameter, or overallrun with given experimental conditions).• The method for calculating the error bars should be explained (closed form formula,call to a library function, bootstrap, etc.)• The assumptions made should be given (e.g., Normally distributed errors).• It should be clear whether the error bar is the standard deviation or the standard errorof the mean.• It is OK to report 1-sigma error bars, but one should state it. The authors shouldpreferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesisof Normality of errors is not verified.• For asymmetric distributions, the authors should be careful not to show in tables orfigures symmetric error bars that would yield results that are out of range (e.g. negativeerror rates).• If error bars are reported in tables or plots, The authors should explain in the text howthey were calculated and reference the corresponding figures or tables in the text.8. Experiments compute resourcesQuestion: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproducethe experiments?Answer: \[Yes\] ,Justification: We give details on computing resources in Section 7.Guidelines:• The answer NA means that the paper does not include experiments.• The paper should indicate the type of compute workers CPU or GPU, internal cluster,or cloud provider, including relevant memory and storage.• The paper should provide the amount of compute required for each of the individualexperimental runs as well as estimate the total compute.• The paper should disclose whether the full research project required more computethan the experiments reported in the paper (e.g., preliminary or failed experiments thatdidn’t make it into the paper).9. Code of ethicsQuestion: Does the research conducted in the paper conform, in every respect, with theNeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines?Answer: \[Yes\]Justification: We used public datasets. The two authors involved in the coding task followeda established procedure, with a protocol in place to handle any emotional distress that mightarise from the scenarios discussed in the datasets.Guidelines:• The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics.• If the authors answer No, they should explain the special circumstances that require adeviation from the Code of Ethics.• The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).10. Broader impactsQuestion: Does the paper discuss both potential positive societal impacts and negativesocietal impacts of the work performed?Answer: \[Yes\] .Justification: We discuss limitations of our exploration in Section 7. Our work doesnot propose a concrete deployment, but a venue for further research, for which societalimplications should be carefully considered.Guidelines:• The answer NA means that there is no societal impact of the work performed.• If the authors answer NA or No, they should explain why their work has no societalimpact or why the paper does not address societal impact.• Examples of negative societal impacts include potential malicious or unintended uses(e.g., disinformation, generating fake profiles, surveillance), fairness considerations(e.g., deployment of technologies that could make decisions that unfairly impact specificgroups), privacy considerations, and security considerations.• The conference expects that many papers will be foundational research and not tiedto particular applications, let alone deployments. However, if there is a direct path toany negative applications, the authors should point it out. For example, it is legitimateto point out that an improvement in the quality of generative models could be used togenerate deepfakes for disinformation. On the other hand, it is not needed to point outthat a generic algorithm for optimizing neural networks could enable people to trainmodels that generate Deepfakes faster.• The authors should consider possible harms that could arise when the technology isbeing used as intended and functioning correctly, harms that could arise when thetechnology is being used as intended but gives incorrect results, and harms followingfrom (intentional or unintentional) misuse of the technology.• If there are negative societal impacts, the authors could also discuss possible mitigationstrategies (e.g., gated release of models, providing defenses in addition to attacks,mechanisms for monitoring misuse, mechanisms to monitor how a system learns fromfeedback over time, improving the efficiency and accessibility of ML).11. SafeguardsQuestion: Does the paper describe safeguards that have been put in place for responsiblerelease of data or models that have a high risk for misuse (e.g., pretrained language models,image generators, or scraped datasets)?Answer: \[NA\] .Justification: The paper’s datasets are either public or derived from public using an established procedure via LLM prompting.Guidelines:• The answer NA means that the paper poses no such risks.• Released models that have a high risk for misuse or dual-use should be released withnecessary safeguards to allow for controlled use of the model, for example by requiringthat users adhere to usage guidelines or restrictions to access the model or implementingsafety filters.• Datasets that have been scraped from the Internet could pose safety risks. The authorsshould describe how they avoided releasing unsafe images.• We recognize that providing effective safeguards is challenging, and many papers donot require this, but we encourage authors to take this into account and make a bestfaith effort.12. Licenses for existing assetsQuestion: Are the creators or original owners of assets (e.g., code, data, models), used inthe paper, properly credited and are the license and terms of use explicitly mentioned andproperly respected?Answer: \[Yes\] ,Justification: Yes, we cite the corresponding papers for datasets we use.Guidelines:• The answer NA means that the paper does not use existing assets.• The authors should cite the original paper that produced the code package or dataset.• The authors should state which version of the asset is used and, if possible, include aURL.• The name of the license (e.g., CC-BY 4.0) should be included for each asset.• For scraped data from a particular source (e.g., website), the copyright and terms ofservice of that source should be provided.• If assets are released, the license, copyright information, and terms of use in the packageshould be provided. For popular datasets, paperswithcode.com/datasets hascurated licenses for some datasets. Their licensing guide can help determine the licenseof a dataset.• For existing datasets that are re-packaged, both the original license and the license ofthe derived asset (if it has changed) should be provided.• If this information is not available online, the authors are encouraged to reach out tothe asset’s creators.13. New assetsQuestion: Are new assets introduced in the paper well documented and is the documentationprovided alongside the assets?Answer: \[Yes\] .Justification: Our dataset is documented.Guidelines:• The answer NA means that the paper does not release new assets.• Researchers should communicate the details of the dataset/code/model as part of theirsubmissions via structured templates. This includes details about training, license,limitations, etc.• The paper should discuss whether and how consent was obtained from people whoseasset is used.• At submission time, remember to anonymize your assets (if applicable). You can eithercreate an anonymized URL or include an anonymized zip file.14. Crowdsourcing and research with human subjectsQuestion: For crowdsourcing experiments and research with human subjects, does the paperinclude the full text of instructions given to participants and screenshots, if applicable, aswell as details about compensation (if any)?Answer: \[NA\] .Justification: No crowdsourcing.Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should beincluded in the main paper.• According to the NeurIPS Code of Ethics, workers involved in data collection, curation,or other labor should be paid at least the minimum wage in the country of the datacollector.15. Institutional review board (IRB) approvals or equivalent for research with humansubjectsQuestion: Does the paper describe potential risks incurred by study participants, whethersuch risks were disclosed to the subjects, and whether Institutional Review Board (IRB)approvals (or an equivalent approval/review based on the requirements of your country orinstitution) were obtained?Answer: \[NA\]Justification: The paper does not involve crowdsourcing nor research with human subjects.Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Depending on the country in which research is conducted, IRB approval (or equivalent)may be required for any human subjects research. If you obtained IRB approval, youshould clearly state this in the paper.• We recognize that the procedures for this may vary significantly between institutionsand locations, and we expect authors to adhere to the NeurIPS Code of Ethics and theguidelines for their institution.• For initial submissions, do not include any information that would break anonymity (ifapplicable), such as the institution conducting the review.16. Declaration of LLM usageQuestion: Does the paper describe the usage of LLMs if it is an important, original, ornon-standard component of the core methods in this research? Note that if the LLM is usedonly for writing, editing, or formatting purposes and does not impact the core methodology,scientific rigorousness, or originality of the research, declaration is not required.Answer: \[Yes\] ,Justification: While LLMs are the object of study in this research, they were not used as acore component of the methodology beyond some aspects of dataset (expansion) generationthat are thoroughly described in the paper, including precise prompts in appendix.Guidelines:• The answer NA means that the core method development in this research does notinvolve LLMs as any important, original, or non-standard components.• Please refer to our LLM policy (https://neurips.cc/Conferences/2025/LLM)for what should or should not be described.Technical Appendices and Supplementary MaterialA
			-> Returned with status code 404!

- Different links: $0/34=0.00\%$

- Successful searches: $15/34=44.12\%$
- Skipped searches: $0/34=0.00\%$
- Mismatching infos: $15/34=44.12\%$
	- **Entries with mismatching author information:**
		=> total = 12
		- `[5] Lichao Sun, Yue Huang, Haoran Wang, Siyuan Wu, Qihui Zhang, Chujie Gao, Yixin Huang, Wenhan Lyu, Yixuan Zhang, Xiner Li, et al. Trustllm: Trustworthiness in large language models. arXiv preprint arXiv:2401.05561, 3, 2024.`
			- Authors (Liu, Liu, Kailkhura, Xiong, Xiao, Xing, Liu, Yao, Kellis, Zitnik, Jiang, Bansal, Zou, Pei, Liu, Zhao, Tang, Mitchell, Shu, Chang, He, Backes, Gong, Chen, Gu, Ying, Jana, Chen, Liu, Zhou, Xie, Chen, Liu, Ye, Cao, Zhao) did not match found publication titled 'TrustLLM: Trustworthiness in Large Language Models'
		- `[7] Hyunwoo Kim, Melanie Sclar, Zhili Feng Li, Maarten Sap, Yejin Choi, and Yulia Tsvetkov. FANToM: A benchmark for stress-testing machine theory of mind in interactions. In Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track, 2023.`
			- Authors (Zhou, Bras) did not match found publication titled 'FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions'
		- ==`[10] Zayne Sprague, Xi Ye, Kyle Richardson, and Greg Durrett. MuSR: Testing the limits of chain-of-thought with multistep soft reasoning. In EMNLP, 2023.`==
			- Authors (Bostrom, Chaudhuri) did not match found publication titled 'MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning'
		- `[14] Nicholas Carlini, Florian Tramer, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam Roberts, Tom Brown, Dawn Song, Ulfar Erlingsson, et al. Extracting training data from large language models. In USENIX Security, 2021.`
			- Authors (Tramèr, Oprea, Raffel) did not match found publication titled 'Extracting Training Data from Large Language Models'
		- `[15] Robin Staab, Mark Vero, Mislav Balunovi´c, and Martin Vechev. Beyond memorization: Violating privacy via inference with large language models. In ICLR, 2024.`
			- Authors (Balunovi'c) did not match found publication titled 'Beyond Memorization: Violating Privacy Via Inference with Large Language Models'
		- `[17] Xuechen Li, Florian Tramer, Percy Liang, and Tatsunori Hashimoto. Large language models can be strong differentially private learners. arXiv preprint arXiv:2110.05679, 2021.`
			- Authors (Tramèr) did not match found publication titled 'Large Language Models Can Be Strong Differentially Private Learners'
		- `[23] Yue Huang, Chujie Gao, Siyuan Wu, Haoran Wang, Xiangqi Wang, Yujun Zhou, Yanbo Wang, Jiayi Ye, Jiawen Shi, Qihui Zhang, et al. On the trustworthiness of generative foundation models: Guideline, assessment, and perspective. arXiv preprint arXiv:2502.14296, 2025.`
			- Authors (Li, Bao, Liu, Guan, Chen, Chen, Guo, Zou, Kuen-Yew, Xiong, Stengel-Eskin, Yin, Yao, Yoon, Shu, Zhu, Krishna, Swayamdipta, Li, Li, Li, Chen, Tu, Zhao, Sun, Sasson, Sattigeri, Reuel, Lamparth, Zhao, Dziri, Su, Sun, Xiao, Bansal, Chawla, Pei, Backes, Gong, Chen, Li) did not match found publication titled 'On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective'
		- `[24] Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie, Mintong Kang, Chenhui Zhang, Chejian Xu, Zidi Xiong, Ritik Dutta, Rylan Schaeffer, et al. Decodingtrust: A comprehensive assessment of trustworthiness in gpt models. In NeurIPS, 2023.`
			- Authors (Truong, Arora, Mazeika, Hendrycks, Cheng, Koyejo, Song) did not match found publication titled 'DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models'
		- `[25] Yichi Zhang, Yao Huang, Yitong Sun, Chang Liu, Zhe Zhao, Zhengwei Fang, Yifan Wang, Huanran Chen, Xiao Yang, Xingxing Wei, et al. Multitrust: A comprehensive benchmark towards trustworthy multimodal large language models. NeurIPS, 2024.`
			- Authors (Dong, Zhu) did not match found publication titled 'MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models'
		- `[26] Haoran Li, Wei Fan, Yulin Chen, Jiayang Cheng, Tianshu Chu, Xuebing Zhou, Peizhao Hu, and Yangqiu Song. GOLDCOIN: Grounding large language models in privacy laws via contextual integrity theory. In EMNLP, 2024.`
			- Authors (Deng, Wang) did not match found publication titled 'GoldCoin: Grounding Large Language Models in Privacy Laws via Contextual Integrity Theory'
		- `[30] Haoran Li, Wei Fan, Yulin Chen, Jiayang Cheng, Tianshu Chu, Xuebing Zhou, Peizhao Hu, Yangqiu Song, and Yong Zhang. PrivaCI-Bench: Evaluating privacy with contextual integrity and legal compliance. arXiv preprint arXiv:2502.17041, 2024.`
			- Authors (Jing) did not match found publication titled 'PrivaCI-Bench: Evaluating Privacy with Contextual Integrity and Legal Compliance'
		- `[33] Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato Carson Denison, John Schulman, Arushi Somani, Peter Hase, Misha Wagner Fabien Roger Vlad Mikulik, Sam Bowman, Jan Leike Jared Kaplan, et al. Reasoning models don’t always say what they think. Anthropic Research, 2025.`
			- Authors (Perez) did not match found publication titled 'Reasoning Models Don't Always Say What They Think'
	- **Entries with mismatching years (where the difference is = 1 year):**
		=> total = 3
		- `[3] Niloofar Mireshghallah, Hyunwoo Kim, Xuhui Zhou, Yulia Tsvetkov, Maarten Sap, Reza Shokri, and Yejin Choi. Can LLMs keep a secret? testing privacy implications of language models via contextual integrity theory. In International Conference on Learning Representations (ICLR)., 2024 https://github.com/skywalker023/confAIde/tree/main/benchmark. MIT License.`
			- Year (2023) does not match expected year (2024)
		- `[27] Haoran Li, Wei Fan, Yulin Chen, Jiayang Cheng, Tianshu Chu, Xuebing Zhou, Peizhao Hu, and Yangqiu Song. Privacy Checklist: Privacy violation detection grounding on contextual integrity theory. 2025.`
			- Year (2024) does not match expected year (2025)
		- `[29] Sahra Ghalebikesabi, Eugene Bagdasaryan, Ren Yi, Itay Yona, Ilia Shumailov, Aneesh Pappu, Chongyang Shi, Laura Weidinger, Robert Stanforth, Leonard Berrada, et al. Operationalizing contextual integrity in privacy-conscious assistants. TMLR, 2025.`
			- Year (2024) does not match expected year (2025)
- No entry found: $4/34=11.76\%$
	- Unfound entries:
		=> total = 4
		- \[6\] Yan Shvartzshnaider and Vasisht Duddu. Position: Contextual integrity washing for language models. arXiv preprint arXiv:2501.19173, 2024.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: None of the 1 results matched the expected title!
		- \[13\] Belinda Z Li, Been Kim, and Zi Wang. QuestBench: Can llm ask the right question to acquire information in reasoning tasks? arXiv preprint arXiv:2503.22674, 2024.
			-> WARNING: No results were found through the dblp search! | WARNING: None of the 234 results matched the expected title!
		- \[19\] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. Retrieval-augmented generation for knowledgeintensive NLP tasks. NeurIPS, 2020.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: None of the 2 results matched the expected title!
		- \[28\] Yan Shvartzshnaider, Vasisht Duddu, and John Lacalamita. LLM-CI: Assessing contextual integrity norms in language models. arXiv preprint arXiv:2409.03735, 2024.
			-> WARNING: None of the 5 results matched the expected title! | WARNING: None of the 1 results matched the expected title!



## References Support for Statements

> [!NOTE]
> *Please note that only references with a retrieved abstract can be checked here.*
> *You can find a complete list, including which sentences were skipped due to a missing abstract, at the bottom of the report.*

**Sentences with references to papers that are thematically related / relevant but REFUTE the statement they are referenced in:**
- 'capturing the refusal to answer [24, 25, 5], and do not assess utility in terms of sharing sensitive data in appropriate contexts'
	- This flag is for the paper with Ref. ID = 5

**Sentences with references to papers that are thematically unrelated / irrelevant to the statement they are referenced in:**
- None



---
## Outlet Rankings

### Outlet Ranking Results

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/5 Privacy Reasoning/ranking_results_fig.jpg]]

### References and Their Rankings

- arXiv
	- References literatures count from this outlet: 13
- Advances in Neural Information Processing Systems (was NIPS)
	- Parsed as: NeurIPS
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 3
- CCS Chemistry
	- Parsed as: CCS
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = National: USA
	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = 8.8
	- References literatures count from this outlet: 2
- Empirical Methods in Natural Language Processing
	- Parsed as: EMNLP
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 2
- Wash.  L  Rev.
	- References literatures count from this outlet: 1
- Usenix Security Symposium
	- Parsed as: USENIX Security
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- Anthropic Research
	- References literatures count from this outlet: 1
- TMLR
	- References literatures count from this outlet: 1
- International Conference on Learning Representations
	- Parsed as: ICLR
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- 22674
	- References literatures count from this outlet: 1
- Privacy in context.  Stanford University Press
	- References literatures count from this outlet: 1
- Transactions of the Association for Computational Linguistics
	- Parsed as: Transactions of the Association for Computational Linguistics
	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = 6.5
	- References literatures count from this outlet: 1
- Association for Computational Linguistics
	- Parsed as: Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- Advances in Neural Information Processing Systems (was NIPS)
	- Parsed as: Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- Proceedings of the 2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),
	- References literatures count from this outlet: 1
- International Conference on Learning Representations
	- Parsed as: International Conference on Learning Representations (ICLR). 
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- Field Methods
	- Parsed as: Field Methods
	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = 1.3
	- References literatures count from this outlet: 1



---
## Extracted References

- **Number 1:**
	- Ref. ID: *1*
	- Authors: *Helen Nissenbaum*
	- Normalized Authors: `['Nissenbaum H.']`
	- Authors contain 'et al.': *False*
	- Title: *Privacy as contextual integrity*
	- Year: *2004*
	- Outlet: *Wash.  L  Rev.*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 2:**
	- Ref. ID: *2*
	- Authors: *Helen Nissenbaum*
	- Normalized Authors: `['Nissenbaum H.']`
	- Authors contain 'et al.': *False*
	- Title: *Privacy in context: Technology, policy, and the integrity of social life*
	- Year: *2009*
	- Outlet: *Privacy in context.  Stanford University Press*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 3:**
	- Ref. ID: *3*
	- Authors: *Niloofar Mireshghallah, Hyunwoo Kim, Xuhui Zhou, Yulia Tsvetkov, Maarten Sap, Reza Shokri, and Yejin Choi*
	- Normalized Authors: `['Mireshghallah N.', 'Kim H.', 'Zhou X.', 'Tsvetkov Y.', 'Sap M.', 'Shokri R.', 'Choi Y.']`
	- Authors contain 'et al.': *False*
	- Title: *Can LLMs keep a secret? testing privacy implications of language models via contextual integrity theory*
	- Year: *2024*
	- Outlet: *International Conference on Learning Representations (ICLR). *
	- Link: *https://github.com/skywalker023/confAIde/tree/main/benchmark.*
	- **Valid?**: *CHECK - Year (2023) does not match expected year (2024)*
- **Number 4:**
	- Ref. ID: *4*
	- Authors: *Yijia Shao, Tianshi Li, Weiyan Shi, Yanchen Liu, and Diyi Yang*
	- Normalized Authors: `['Shao Y.', 'Li T.', 'Shi W.', 'Liu Y.', 'Yang D.']`
	- Authors contain 'et al.': *False*
	- Title: *PrivacyLens: Evaluating privacy norm awareness of language models in action*
	- Year: *2024*
	- Outlet: *Proceedings of the 2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),*
	- Link: *https://github.com/SALT-NLP/PrivacyLens.*
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 5:**
	- Ref. ID: *5*
	- Authors: *Lichao Sun, Yue Huang, Haoran Wang, Siyuan Wu, Qihui Zhang, Chujie Gao, Yixin Huang, Wenhan Lyu, Yixuan Zhang, Xiner Li, et al*
	- Normalized Authors: `['Sun L.', 'Huang Y.', 'Wang H.', 'Wu S.', 'Zhang Q.', 'Gao C.', 'Huang Y.', 'Lyu W.', 'Zhang Y.', 'Li X.']`
	- Authors contain 'et al.': *True*
	- Title: *Trustllm: Trustworthiness in large language models*
	- Year: *2024*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *CHECK - Authors (Liu, Liu, Kailkhura, Xiong, Xiao, Xing, Liu, Yao, Kellis, Zitnik, Jiang, Bansal, Zou, Pei, Liu, Zhao, Tang, Mitchell, Shu, Chang, He, Backes, Gong, Chen, Gu, Ying, Jana, Chen, Liu, Zhou, Xie, Chen, Liu, Ye, Cao, Zhao) did not match found publication titled 'TrustLLM: Trustworthiness in Large Language Models'*
- **Number 6:**
	- Ref. ID: *6*
	- Authors: *Yan Shvartzshnaider and Vasisht Duddu*
	- Normalized Authors: `['Shvartzshnaider Y.', 'Duddu V.']`
	- Authors contain 'et al.': *False*
	- Title: *Position: Contextual integrity washing for language models*
	- Year: *2024*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: None of the 1 results matched the expected title!*
- **Number 7:**
	- Ref. ID: *7*
	- Authors: *Hyunwoo Kim, Melanie Sclar, Zhili Feng Li, Maarten Sap, Yejin Choi, and Yulia Tsvetkov*
	- Normalized Authors: `['Kim H.', 'Sclar M.', 'Li Z.', 'Sap M.', 'Choi Y.', 'Tsvetkov Y.']`
	- Authors contain 'et al.': *False*
	- Title: *FANToM: A benchmark for stress-testing machine theory of mind in interactions*
	- Year: *2023*
	- Outlet: *Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track*
	- Link: **
	- **Valid?**: *CHECK - Authors (Zhou, Bras) did not match found publication titled 'FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions'*
- **Number 8:**
	- Ref. ID: *8*
	- Authors: *Melanie Sclar, Sachin Kumar, Peter West, Alane Suhr, Yejin Choi, and Yulia Tsvetkov*
	- Normalized Authors: `['Sclar M.', 'Kumar S.', 'West P.', 'Suhr A.', 'Choi Y.', 'Tsvetkov Y.']`
	- Authors contain 'et al.': *False*
	- Title: *Minding language models’ (lack of) theory of mind: A plug-and-play multi-character belief tracker*
	- Year: *2023*
	- Outlet: *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 9:**
	- Ref. ID: *9*
	- Authors: *Mor Geva, Daniel Khashabi, Elad Segal, Tushar Khot, Dan Roth, and Jonathan Berant*
	- Normalized Authors: `['Geva M.', 'Khashabi D.', 'Segal E.', 'Khot T.', 'Roth D.', 'Berant J.']`
	- Authors contain 'et al.': *False*
	- Title: *Did aristotle use a laptop? a question answering benchmark with implicit reasoning strategies*
	- Year: *2021*
	- Outlet: *Transactions of the Association for Computational Linguistics*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 10:**
	- Ref. ID: *10*
	- Authors: *Zayne Sprague, Xi Ye, Kyle Richardson, and Greg Durrett*
	- Normalized Authors: `['Sprague Z.', 'Ye X.', 'Richardson K.', 'Durrett G.']`
	- Authors contain 'et al.': *False*
	- Title: *MuSR: Testing the limits of chain-of-thought with multistep soft reasoning*
	- Year: *2023*
	- Outlet: *EMNLP*
	- Link: **
	- **Valid?**: *CHECK - Authors (Bostrom, Chaudhuri) did not match found publication titled 'MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning'*
- **Number 11:**
	- Ref. ID: *11*
	- Authors: *Bill Yuchen Lin, Ronan Le Bras, Kyle Richardson, Ashish Sabharwal, Radha Poovendran, Peter Clark, and Yejin Choi*
	- Normalized Authors: `['Lin B.', 'Bras R.', 'Richardson K.', 'Sabharwal A.', 'Poovendran R.', 'Clark P.', 'Choi Y.']`
	- Authors contain 'et al.': *False*
	- Title: *Zebralogic: On the scaling limits of llms for logical reasoning*
	- Year: *2025*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 12:**
	- Ref. ID: *12*
	- Authors: *Alon Jacovi, Yonatan Bitton, Bernd Bohnet, Jonathan Herzig, Or Honovich, Michael Tseng, Michael Collins, Roee Aharoni, and Mor Geva*
	- Normalized Authors: `['Jacovi A.', 'Bitton Y.', 'Bohnet B.', 'Herzig J.', 'Honovich O.', 'Tseng M.', 'Collins M.', 'Aharoni R.', 'Geva M.']`
	- Authors contain 'et al.': *False*
	- Title: *A chain-of-thought is as strong as its weakest link: A benchmark for verifiers of reasoning chains*
	- Year: *2024*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 13:**
	- Ref. ID: *13*
	- Authors: *Belinda Z Li, Been Kim, and Zi Wang*
	- Normalized Authors: `['Li B.', 'Kim B.', 'Wang Z.']`
	- Authors contain 'et al.': *False*
	- Title: *QuestBench: Can llm ask the right question to acquire information in reasoning tasks? arXiv preprint arXiv:2503*
	- Year: *2024*
	- Outlet: *22674*
	- Link: **
	- **Valid?**: *WARNING: No results were found through the dblp search! | WARNING: None of the 234 results matched the expected title!*
- **Number 14:**
	- Ref. ID: *14*
	- Authors: *Nicholas Carlini, Florian Tramer, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam Roberts, Tom Brown, Dawn Song, Ulfar Erlingsson, et al*
	- Normalized Authors: `['Carlini N.', 'Tramer F.', 'Wallace E.', 'Jagielski M.', 'Herbert-Voss A.', 'Lee K.', 'Roberts A.', 'Brown T.', 'Song D.', 'Erlingsson U.']`
	- Authors contain 'et al.': *True*
	- Title: *Extracting training data from large language models*
	- Year: *2021*
	- Outlet: *USENIX Security*
	- Link: **
	- **Valid?**: *CHECK - Authors (Tramèr, Oprea, Raffel) did not match found publication titled 'Extracting Training Data from Large Language Models'*
- **Number 15:**
	- Ref. ID: *15*
	- Authors: *Robin Staab, Mark Vero, Mislav Balunovi´c, and Martin Vechev*
	- Normalized Authors: `['Staab R.', 'Vero M.', 'Balunovi´c M.', 'Vechev M.']`
	- Authors contain 'et al.': *False*
	- Title: *Beyond memorization: Violating privacy via inference with large language models*
	- Year: *2024*
	- Outlet: *ICLR*
	- Link: **
	- **Valid?**: *CHECK - Authors (Balunovi'c) did not match found publication titled 'Beyond Memorization: Violating Privacy Via Inference with Large Language Models'*
- **Number 16:**
	- Ref. ID: *16*
	- Authors: *Martin Abadi, Andy Chu, Ian Goodfellow, H Brendan McMahan, Ilya Mironov, Kunal Talwar, and Li Zhang*
	- Normalized Authors: `['Abadi M.', 'Chu A.', 'Goodfellow I.', 'McMahan H.', 'Mironov I.', 'Talwar K.', 'Zhang L.']`
	- Authors contain 'et al.': *False*
	- Title: *Deep learning with differential privacy*
	- Year: *2016*
	- Outlet: *CCS*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 17:**
	- Ref. ID: *17*
	- Authors: *Xuechen Li, Florian Tramer, Percy Liang, and Tatsunori Hashimoto*
	- Normalized Authors: `['Li X.', 'Tramer F.', 'Liang P.', 'Hashimoto T.']`
	- Authors contain 'et al.': *False*
	- Title: *Large language models can be strong differentially private learners*
	- Year: *2021*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *CHECK - Authors (Tramèr) did not match found publication titled 'Large Language Models Can Be Strong Differentially Private Learners'*
- **Number 18:**
	- Ref. ID: *18*
	- Authors: *Da Yu, Saurabh Naik, Arturs Backurs, Sivakanth Gopi, Huseyin A Inan, Gautam Kamath, Janardhan Kulkarni, Yin Tat Lee, Andre Manoel, Lukas Wutschitz, et al*
	- Normalized Authors: `['Yu D.', 'Naik S.', 'Backurs A.', 'Gopi S.', 'Inan H.', 'Kamath G.', 'Kulkarni J.', 'Lee Y.', 'Manoel A.', 'Wutschitz L.']`
	- Authors contain 'et al.': *True*
	- Title: *Differentially private fine-tuning of language models*
	- Year: *2021*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 19:**
	- Ref. ID: *19*
	- Authors: *Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al*
	- Normalized Authors: `['Lewis P.', 'Perez E.', 'Piktus A.', 'Petroni F.', 'Karpukhin V.', 'Goyal N.', 'Küttler H.', 'Lewis M.', 'Yih W.', 'Rocktäschel T.']`
	- Authors contain 'et al.': *True*
	- Title: *Retrieval-augmented generation for knowledgeintensive NLP tasks*
	- Year: *2020*
	- Outlet: *NeurIPS*
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: None of the 2 results matched the expected title!*
- **Number 20:**
	- Ref. ID: *20*
	- Authors: *Eugene Bagdasarian, Ren Yi, Sahra Ghalebikesabi, Peter Kairouz, Marco Gruteser, Sewoong Oh, Borja Balle, and Daniel Ramage*
	- Normalized Authors: `['Bagdasarian E.', 'Yi R.', 'Ghalebikesabi S.', 'Kairouz P.', 'Gruteser M.', 'Oh S.', 'Balle B.', 'Ramage D.']`
	- Authors contain 'et al.': *False*
	- Title: *Airgapagent: Protecting privacy-conscious conversational agents*
	- Year: *2024*
	- Outlet: *CCS*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 21:**
	- Ref. ID: *21*
	- Authors: *Ivoline Ngong, Swanand Kadhe, Hao Wang, Keerthiram Murugesan, Justin D Weisz, Amit Dhurandhar, and Karthikeyan Natesan Ramamurthy*
	- Normalized Authors: `['Ngong I.', 'Kadhe S.', 'Wang H.', 'Murugesan K.', 'Weisz J.', 'Dhurandhar A.', 'Ramamurthy K.']`
	- Authors contain 'et al.': *False*
	- Title: *Protecting users from themselves: Safeguarding contextual privacy in interactions with conversational agents*
	- Year: *2025*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 22:**
	- Ref. ID: *22*
	- Authors: *Arman Zharmagambetov, Chuan Guo, Ivan Evtimov, Maya Pavlova, Ruslan Salakhutdinov, and Kamalika Chaudhuri*
	- Normalized Authors: `['Zharmagambetov A.', 'Guo C.', 'Evtimov I.', 'Pavlova M.', 'Salakhutdinov R.', 'Chaudhuri K.']`
	- Authors contain 'et al.': *False*
	- Title: *AgentDAM: Privacy leakage evaluation for autonomous web agents*
	- Year: *2025*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 23:**
	- Ref. ID: *23*
	- Authors: *Yue Huang, Chujie Gao, Siyuan Wu, Haoran Wang, Xiangqi Wang, Yujun Zhou, Yanbo Wang, Jiayi Ye, Jiawen Shi, Qihui Zhang, et al*
	- Normalized Authors: `['Huang Y.', 'Gao C.', 'Wu S.', 'Wang H.', 'Wang X.', 'Zhou Y.', 'Wang Y.', 'Ye J.', 'Shi J.', 'Zhang Q.']`
	- Authors contain 'et al.': *True*
	- Title: *On the trustworthiness of generative foundation models: Guideline, assessment, and perspective*
	- Year: *2025*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *CHECK - Authors (Li, Bao, Liu, Guan, Chen, Chen, Guo, Zou, Kuen-Yew, Xiong, Stengel-Eskin, Yin, Yao, Yoon, Shu, Zhu, Krishna, Swayamdipta, Li, Li, Li, Chen, Tu, Zhao, Sun, Sasson, Sattigeri, Reuel, Lamparth, Zhao, Dziri, Su, Sun, Xiao, Bansal, Chawla, Pei, Backes, Gong, Chen, Li) did not match found publication titled 'On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective'*
- **Number 24:**
	- Ref. ID: *24*
	- Authors: *Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie, Mintong Kang, Chenhui Zhang, Chejian Xu, Zidi Xiong, Ritik Dutta, Rylan Schaeffer, et al*
	- Normalized Authors: `['Wang B.', 'Chen W.', 'Pei H.', 'Xie C.', 'Kang M.', 'Zhang C.', 'Xu C.', 'Xiong Z.', 'Dutta R.', 'Schaeffer R.']`
	- Authors contain 'et al.': *True*
	- Title: *Decodingtrust: A comprehensive assessment of trustworthiness in gpt models*
	- Year: *2023*
	- Outlet: *NeurIPS*
	- Link: **
	- **Valid?**: *CHECK - Authors (Truong, Arora, Mazeika, Hendrycks, Cheng, Koyejo, Song) did not match found publication titled 'DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models'*
- **Number 25:**
	- Ref. ID: *25*
	- Authors: *Yichi Zhang, Yao Huang, Yitong Sun, Chang Liu, Zhe Zhao, Zhengwei Fang, Yifan Wang, Huanran Chen, Xiao Yang, Xingxing Wei, et al*
	- Normalized Authors: `['Zhang Y.', 'Huang Y.', 'Sun Y.', 'Liu C.', 'Zhao Z.', 'Fang Z.', 'Wang Y.', 'Chen H.', 'Yang X.', 'Wei X.']`
	- Authors contain 'et al.': *True*
	- Title: *Multitrust: A comprehensive benchmark towards trustworthy multimodal large language models*
	- Year: *2024*
	- Outlet: *NeurIPS*
	- Link: **
	- **Valid?**: *CHECK - Authors (Dong, Zhu) did not match found publication titled 'MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models'*
- **Number 26:**
	- Ref. ID: *26*
	- Authors: *Haoran Li, Wei Fan, Yulin Chen, Jiayang Cheng, Tianshu Chu, Xuebing Zhou, Peizhao Hu, and Yangqiu Song*
	- Normalized Authors: `['Li H.', 'Fan W.', 'Chen Y.', 'Cheng J.', 'Chu T.', 'Zhou X.', 'Hu P.', 'Song Y.']`
	- Authors contain 'et al.': *False*
	- Title: *GOLDCOIN: Grounding large language models in privacy laws via contextual integrity theory*
	- Year: *2024*
	- Outlet: *EMNLP*
	- Link: **
	- **Valid?**: *CHECK - Authors (Deng, Wang) did not match found publication titled 'GoldCoin: Grounding Large Language Models in Privacy Laws via Contextual Integrity Theory'*
- **Number 27:**
	- Ref. ID: *27*
	- Authors: *Haoran Li, Wei Fan, Yulin Chen, Jiayang Cheng, Tianshu Chu, Xuebing Zhou, Peizhao Hu, and Yangqiu Song*
	- Normalized Authors: `['Li H.', 'Fan W.', 'Chen Y.', 'Cheng J.', 'Chu T.', 'Zhou X.', 'Hu P.', 'Song Y.']`
	- Authors contain 'et al.': *False*
	- Title: *Privacy Checklist: Privacy violation detection grounding on contextual integrity theory*
	- Year: *2025*
	- Outlet: **
	- Link: **
	- **Valid?**: *CHECK - Year (2024) does not match expected year (2025)*
- **Number 28:**
	- Ref. ID: *28*
	- Authors: *Yan Shvartzshnaider, Vasisht Duddu, and John Lacalamita*
	- Normalized Authors: `['Shvartzshnaider Y.', 'Duddu V.', 'Lacalamita J.']`
	- Authors contain 'et al.': *False*
	- Title: *LLM-CI: Assessing contextual integrity norms in language models*
	- Year: *2024*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *WARNING: None of the 5 results matched the expected title! | WARNING: None of the 1 results matched the expected title!*
- **Number 29:**
	- Ref. ID: *29*
	- Authors: *Sahra Ghalebikesabi, Eugene Bagdasaryan, Ren Yi, Itay Yona, Ilia Shumailov, Aneesh Pappu, Chongyang Shi, Laura Weidinger, Robert Stanforth, Leonard Berrada, et al*
	- Normalized Authors: `['Ghalebikesabi S.', 'Bagdasaryan E.', 'Yi R.', 'Yona I.', 'Shumailov I.', 'Pappu A.', 'Shi C.', 'Weidinger L.', 'Stanforth R.', 'Berrada L.']`
	- Authors contain 'et al.': *True*
	- Title: *Operationalizing contextual integrity in privacy-conscious assistants*
	- Year: *2025*
	- Outlet: *TMLR*
	- Link: **
	- **Valid?**: *CHECK - Year (2024) does not match expected year (2025)*
- **Number 30:**
	- Ref. ID: *30*
	- Authors: *Haoran Li, Wei Fan, Yulin Chen, Jiayang Cheng, Tianshu Chu, Xuebing Zhou, Peizhao Hu, Yangqiu Song, and Yong Zhang*
	- Normalized Authors: `['Li H.', 'Fan W.', 'Chen Y.', 'Cheng J.', 'Chu T.', 'Zhou X.', 'Hu P.', 'Song Y.', 'Zhang Y.']`
	- Authors contain 'et al.': *False*
	- Title: *PrivaCI-Bench: Evaluating privacy with contextual integrity and legal compliance*
	- Year: *2024*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *CHECK - Authors (Jing) did not match found publication titled 'PrivaCI-Bench: Evaluating Privacy with Contextual Integrity and Legal Compliance'*
- **Number 31:**
	- Ref. ID: *31*
	- Authors: *Zhao Cheng, Diane Wan, Matthew Abueg, Sahra Ghalebikesabi, Ren Yi, Eugene Bagdasarian, Borja Balle, Stefan Mellem, and Shawn O'Banion*
	- Normalized Authors: `['Cheng Z.', 'Wan D.', 'Abueg M.', 'Ghalebikesabi S.', 'Yi R.', 'Bagdasarian E.', 'Balle B.', 'Mellem S.', "O'Banion S."]`
	- Authors contain 'et al.': *False*
	- Title: *Ci-bench: Benchmarking contextual integrity of ai assistants on synthetic data*
	- Year: *2024*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 32:**
	- Ref. ID: *32*
	- Authors: *Guangchen Lan, Huseyin A Inan, Sahar Abdelnabi, Janardhan Kulkarni, Lukas Wutschitz, Reza Shokri, Christopher G Brinton, and Robert Sim*
	- Normalized Authors: `['Lan G.', 'Inan H.', 'Abdelnabi S.', 'Kulkarni J.', 'Wutschitz L.', 'Shokri R.', 'Brinton C.', 'Sim R.']`
	- Authors contain 'et al.': *False*
	- Title: *Contextual integrity in llms via reasoning and reinforcement learning*
	- Year: *2025*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 33:**
	- Ref. ID: *33*
	- Authors: *Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato Carson Denison, John Schulman, Arushi Somani, Peter Hase, Misha Wagner Fabien Roger Vlad Mikulik, Sam Bowman, Jan Leike Jared Kaplan, et al*
	- Normalized Authors: `['Chen Y.', 'Benton J.', 'Radhakrishnan A.', 'Denison J.', 'Schulman J.', 'Somani A.', 'Hase P.', 'Mikulik M.', 'Bowman S.', 'Kaplan J.']`
	- Authors contain 'et al.': *True*
	- Title: *Reasoning models don’t always say what they think*
	- Year: *2025*
	- Outlet: *Anthropic Research*
	- Link: **
	- **Valid?**: *CHECK - Authors (Perez) did not match found publication titled 'Reasoning Models Don't Always Say What They Think'*
- **Number 34:**
	- Ref. ID: *34*
	- Authors: *M  Ariel Cascio, Eunlye Lee, Nicole Vaudrin, and Darcy A  Freedman*
	- Normalized Authors: `['Cascio M.', 'Lee E.', 'Vaudrin N.', 'Freedman D.']`
	- Authors contain 'et al.': *False*
	- Title: *A team-based approach to open coding: Considerations for creating intercoder consensus*
	- Year: *2019*
	- Outlet: *Field Methods*
	- Link: *https://github.com/google-parfait/contextual-privacy-and-security.Guidelines:•*
	- **Valid?**: *Found: Years matched; reference checks out :)*



---
## Full List of Reference Support Check

**Sentences with references to papers that are thematically related / relevant papers but REFUTE the statement they are referenced in:**
- '*capturing the refusal to answer [24, 25, 5], and do not assess utility in terms of sharing sensitive data in appropriate contexts*'
	- This flag is for the paper with Ref. ID = 5

**Sentences with references to papers that are thematically related / relevant papers that we had not enough info about to determine the stance on the statement they are referenced in:**
- '*Such capabilities of LLMs have been studied both generally [7, 8] and in relation to privacy [3]*'
	- This flag is for the paper with Ref. ID = 3
- '*The two publicly available benchmarks that we use in our work are PrivacyLens [4] and ConfAIde [3], which we describe in detail in Appendix D and expand upon in Section 4*'
	- This flag is for the paper with Ref. ID = 3
- '*To better evaluate both the privacy and utility of LLMs in probing-style tasks, we use two existing privacy benchmarks: PrivacyLens [4] and ConfAIde [3]*'
	- This flag is for the paper with Ref. ID = 3
- '*Following existing benchmarks [3], we start with a neutral prompt that asks “is it okay” to share the relevant data without providing more information or context*'
	- This flag is for the paper with Ref. ID = 3
- '*More recent findings with advanced LLMs, however, indicate substantial improvements on certain datasets [5]*'
	- This flag is for the paper with Ref. ID = 5
- '*Such capabilities of LLMs have been studied both generally [7, 8] and in relation to privacy [3]*'
	- This flag is for the paper with Ref. ID = 7
- '*StrategyQA [9] and MuSR [10] test implicit and multi-step reasoning*'
	- This flag is for the paper with Ref. ID = 10
- '*Building on extensive research into LLM reasoning [9, 10, 11, 12] and factors influencing their outputs, we seek to understand appropriateness decisions of LLMs by prompting them to provide concise reasoning alongside each yes/no decision (our prompts can be found in Appendix E)*'
	- This flag is for the paper with Ref. ID = 10
- '*capturing the refusal to answer [24, 25, 5], and do not assess utility in terms of sharing sensitive data in appropriate contexts*'
	- This flag is for the paper with Ref. ID = 24
- '*capturing the refusal to answer [24, 25, 5], and do not assess utility in terms of sharing sensitive data in appropriate contexts*'
	- This flag is for the paper with Ref. ID = 25
- '*Several studies focus on the alignment of models with norms and user preferences [26, 27, 28]*'
	- This flag is for the paper with Ref. ID = 26
- '*Several studies focus on the alignment of models with norms and user preferences [26, 27, 28]*'
	- This flag is for the paper with Ref. ID = 27

**Sentences with references to papers that are thematically related / relevant papers that SUPPORT the statement they are referenced in:**
- '*Prior research [3, 4] has investigated the ability of large language models (LLMs) to maintain the secrecy of sensitive information, with initial studies reporting limited success*'
	- This flag is for the paper with Ref. ID = 3
- '*Next, we create a restrictive prompt variant by adding “Please answer the question considering privacy norms in the response” to the neutral prompt, akin to prior work [3]*'
	- This flag is for the paper with Ref. ID = 3
- '*One line of work aims to assess [14, 15] and mitigate [16, 17, 18] leakage of training data*'
	- This flag is for the paper with Ref. ID = 14
- '*One line of work aims to assess [14, 15] and mitigate [16, 17, 18] leakage of training data*'
	- This flag is for the paper with Ref. ID = 15
- '*One line of work aims to assess [14, 15] and mitigate [16, 17, 18] leakage of training data*'
	- This flag is for the paper with Ref. ID = 17
- '*The work by Ghalebikesabi et al [29] develops a benchmark for form-filling*'
	- This flag is for the paper with Ref. ID = 29
- '*PrivaCI-Bench [30] focuses on benchmarks for legal compliance*'
	- This flag is for the paper with Ref. ID = 30
- '*Although elicited reasoning may not perfectly represent internal processes for models, it offers valuable insights into their decision-making [33]*'
	- This flag is for the paper with Ref. ID = 33
- '*This is likely due to LLM-provided reasoning not reflecting the underlying reasoning that led to the specific judgment, as also reported in prior work [33]*'
	- This flag is for the paper with Ref. ID = 33


**Sentences with references to papers that seem thematically unrelated / irrelevant:**
- '*The high precision also aligns with prior work finding that models more easily distinguish negative examples [5]*'
	- This flag is for the paper with Ref. ID = 5
- '*Inference-time privacy assessments can generally be categorized as either studies of privacy leakage or privacy awareness [23]*'
	- This flag is for the paper with Ref. ID = 23


**Sentences with references to papers that we didn't have an abstract for to check against:**
- '*To be truly useful, the agent must therefore be able to judge based on the context of the interaction when it is appropriate (as defined in the contextual integrity framework [1, 2]) and consistent with a specific user’s expectations to share personal information in interactions with third-party tools and agents*'
	- This flag is for the paper with Ref. ID = 1
- '*Due to the contextual nature of appropriateness, many privacy awareness assessments of LLMs have been grounded in contextual integrity theory [1, 2], which defines privacy as adherence to context-specific informational norms*'
	- This flag is for the paper with Ref. ID = 1
- '*Such information is served to the model through data structures called scenarios SC, parameterized by a set of contextual fields C, often inspired by the contextual integrity theory [1, 2]*'
	- This flag is for the paper with Ref. ID = 1
- '*ing to disambiguate context outperforms the disambiguation based on contextual integrity parameters, which the theory identifies as the key determinants of privacy decision-making [1]*'
	- This flag is for the paper with Ref. ID = 1
- '*To be truly useful, the agent must therefore be able to judge based on the context of the interaction when it is appropriate (as defined in the contextual integrity framework [1, 2]) and consistent with a specific user’s expectations to share personal information in interactions with third-party tools and agents*'
	- This flag is for the paper with Ref. ID = 2
- '*Due to the contextual nature of appropriateness, many privacy awareness assessments of LLMs have been grounded in contextual integrity theory [1, 2], which defines privacy as adherence to context-specific informational norms*'
	- This flag is for the paper with Ref. ID = 2
- '*Such information is served to the model through data structures called scenarios SC, parameterized by a set of contextual fields C, often inspired by the contextual integrity theory [1, 2]*'
	- This flag is for the paper with Ref. ID = 2
- '*Prior research [3, 4] has investigated the ability of large language models (LLMs) to maintain the secrecy of sensitive information, with initial studies reporting limited success*'
	- This flag is for the paper with Ref. ID = 4
- '*The two publicly available benchmarks that we use in our work are PrivacyLens [4] and ConfAIde [3], which we describe in detail in Appendix D and expand upon in Section 4*'
	- This flag is for the paper with Ref. ID = 4
- '*To better evaluate both the privacy and utility of LLMs in probing-style tasks, we use two existing privacy benchmarks: PrivacyLens [4] and ConfAIde [3]*'
	- This flag is for the paper with Ref. ID = 4
- '*example, we prompt the model to generate only neutral information, in line with prior work [4]*'
	- This flag is for the paper with Ref. ID = 4
- '*We achieve this by prompting the context-generating LLM to avoid directly expanding on the appropriateness label, and using heuristics that remove certain words indicative of the label, in line with prior work [4]*'
	- This flag is for the paper with Ref. ID = 4
- '*Similarly to Shao et al [4], we explicitly ask the LLM to add descriptive contexts and avoid using evaluative words like “sensitive” and “non-sensitive” that would introduce reasoning shortcuts in the expansions*'
	- This flag is for the paper with Ref. ID = 4
- '*Our study then reveals an oversensitivity to prompt variations in LLM decisions—a signal that can indicate complexity in contextual integrity analysis [6]*'
	- This flag is for the paper with Ref. ID = 6
- '*Such capabilities of LLMs have been studied both generally [7, 8] and in relation to privacy [3]*'
	- This flag is for the paper with Ref. ID = 8
- '*StrategyQA [9] and MuSR [10] test implicit and multi-step reasoning*'
	- This flag is for the paper with Ref. ID = 9
- '*Building on extensive research into LLM reasoning [9, 10, 11, 12] and factors influencing their outputs, we seek to understand appropriateness decisions of LLMs by prompting them to provide concise reasoning alongside each yes/no decision (our prompts can be found in Appendix E)*'
	- This flag is for the paper with Ref. ID = 9
- '*Logical reasoning errors have been explored in ZebraLogic [11], the cause of reasoning errors has been investigated in REVEAL [12], and recently the ability to ask clarifying questions in underspecified contexts has been studied in QuestBench [13] on logical puzzles, planning, and math problems*'
	- This flag is for the paper with Ref. ID = 11
- '*Building on extensive research into LLM reasoning [9, 10, 11, 12] and factors influencing their outputs, we seek to understand appropriateness decisions of LLMs by prompting them to provide concise reasoning alongside each yes/no decision (our prompts can be found in Appendix E)*'
	- This flag is for the paper with Ref. ID = 11
- '*Logical reasoning errors have been explored in ZebraLogic [11], the cause of reasoning errors has been investigated in REVEAL [12], and recently the ability to ask clarifying questions in underspecified contexts has been studied in QuestBench [13] on logical puzzles, planning, and math problems*'
	- This flag is for the paper with Ref. ID = 12
- '*Building on extensive research into LLM reasoning [9, 10, 11, 12] and factors influencing their outputs, we seek to understand appropriateness decisions of LLMs by prompting them to provide concise reasoning alongside each yes/no decision (our prompts can be found in Appendix E)*'
	- This flag is for the paper with Ref. ID = 12
- '*Logical reasoning errors have been explored in ZebraLogic [11], the cause of reasoning errors has been investigated in REVEAL [12], and recently the ability to ask clarifying questions in underspecified contexts has been studied in QuestBench [13] on logical puzzles, planning, and math problems*'
	- This flag is for the paper with Ref. ID = 13
- '*One line of work aims to assess [14, 15] and mitigate [16, 17, 18] leakage of training data*'
	- This flag is for the paper with Ref. ID = 16
- '*One line of work aims to assess [14, 15] and mitigate [16, 17, 18] leakage of training data*'
	- This flag is for the paper with Ref. ID = 18
- '*As the capability of LLMs to consume larger contexts has improved [19], allowing them to perform agent tasks on user data [20, 21, 22], the research area of inference-time privacy has emerged*'
	- This flag is for the paper with Ref. ID = 19
- '*As the capability of LLMs to consume larger contexts has improved [19], allowing them to perform agent tasks on user data [20, 21, 22], the research area of inference-time privacy has emerged*'
	- This flag is for the paper with Ref. ID = 20
- '*As the capability of LLMs to consume larger contexts has improved [19], allowing them to perform agent tasks on user data [20, 21, 22], the research area of inference-time privacy has emerged*'
	- This flag is for the paper with Ref. ID = 21
- '*As the capability of LLMs to consume larger contexts has improved [19], allowing them to perform agent tasks on user data [20, 21, 22], the research area of inference-time privacy has emerged*'
	- This flag is for the paper with Ref. ID = 22
- '*Several studies focus on the alignment of models with norms and user preferences [26, 27, 28]*'
	- This flag is for the paper with Ref. ID = 28
- '*CI-Bench [31] builds a benchmark for assistant tasks*'
	- This flag is for the paper with Ref. ID = 31
- '*A concurrent study by Lan et al [32] focuses on improving privacy reasoning through reinforcement learning*'
	- This flag is for the paper with Ref. ID = 32
- '*Disagreement was resolved through discussion to achieve consensus [34]*'
	- This flag is for the paper with Ref. ID = 34

