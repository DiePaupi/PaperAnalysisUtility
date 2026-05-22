# Paper Analysis Utility - Results

Paper: A Unified Stability Analysis of SAM vs SGD.pdf


## Document Structure

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/27 A Unified Stability Analysis/chapter_fig.jpg]]

1) 'Introduction' -- p. 1 (ca. 2 pages)
2) 'Background' -- p. 3 (ca. 1 pages)
3) 'Main Results' -- p. 4 (ca. 4 pages)
4) 'Experiments' -- p. 8 (ca. 2 pages)
5) 'References' -- p. 10 (ca. 9 pages)
A) 'More discussion on limitation and practical implication' -- p. 19 (ca. 1 pages)
B) 'Related Work' -- p. 20 (ca. 2 pages)
C) 'Appendix – Experiments and Proofs' -- p. 22 (ca. 17 pages)


## Unicode Character Usage

> [!NOTE]
> *Please note that this list may contain false positives since this is feature is still in early stages of development.*

- Dashes:
	- Stats for minus signs ():
		- Valid uses: 0/239=0.00%
		- Invalid uses: 239/239=100.00%
	- Sentences with invalid dashes:
		- Lines containing invalid dashes:
		- Page 2: model parameters w ∈Rd, and suppose w⋆is a local minimum. Let δt = wt−w⋆be the perturbation
		- Page 2: since ∇L(w⋆) = 0. For a generic optimization algorithm with update rule wt+1 = wt −ηgt, the
		- Page 2: δt+1 = (I −ηHt)δt,
		- Page 2: wt+1 = wt −ηHtwt = (I −ηHt)wt = ˆJtwt,
		- Page 3: wt+1 = wt −η∇Sl(w + δt)
		- Page 3: = wt −ηHtwt −ηHtδt
		- Page 3: b −1)−1
		- Page 4: wt+1 = wt −η∇Sl(wt + ρ ∇l(wt)
		- Page 4: = (I −ηHt(I +
		- Page 4: I −ηHt
		- Page 4: B −1
		- Page 4: −1/2 
		- Page 4: −1
		- Page 4: i ≤2 −ϵ
		- Page 5: B −1)−1,
		- Page 5: x ∈{−1, 1}d are drawn i.i.d. and labels are generated y = x[0]x[1], ensuring that both simple and
		- Page 6: W1,j = r · [(−1)a1, (−1)a2, . . . , (−1)aC, 0, . . . , 0],
		- Page 6: with j indexing a binary encoding of the ai’s i.e. j = 1 + P 2i−1ai. We set W2[j] = 1
		- Page 6: r(−1)a1+a2
		- Page 6: probability at least 1−δ, for a randomly drawn dataset of size n, the top eigenvalue of the coherence
		- Page 7: 2c −1
		- Page 21: jth row of W1 be W1,j = r[(−1)a1, (−1)a2, ...(−1)aC, 0, 0, ...0], with j = 1+P 2i−1ai. Similarly,
		- Page 21: let b[j] = −r(C −1). We set W2[j] = 1
		- Page 21: r(−1)a1+a2. For k > C, W1,k = 0, W2[k] = 0, b[k] = 0.
		- Page 21: −1
		- Page 21: −1
		- Page 21: −1
		- Page 21: −1
		- Page 21: −1
		- Page 21: −1
		- Page 21: −1
		- Page 21: −1
		- Page 21: −1
		- Page 21: −1
		- Page 21: −1
		- Page 21: −1
		- Page 22: −1
		- Page 22: −1
		- Page 22: −1
		- Page 22: −1
		- Page 23: 1 for all i ∈[σ] and Hi = mei−σ+1eT
		- Page 23: i−σ+1 otherwise. We use m = 2n
		- Page 25: n −1
		- Page 25: k −1
		- Page 25: n −1
		- Page 25: b −1)−1
		- Page 25: wk = ˆJk... ˆJ1w0 −η
		- Page 25: k wk] = E[( ˆJk... ˆJ1w0 −η
		- Page 25: Jt′)Htδt)T ( ˆJk... ˆJ1w0 −η
		- Page 26: Bn −1
		- Page 26: b −1)tλmax(H)2t)
		- Page 26: b −1)λmax(H)2 to be larger than 1. i.e.,
		- Page 26: b −1)−1
		- Page 26: b −1)tλ2t
		- Page 26: b −1)(( η
		- Page 26: b −1)k −1)
		- Page 26: b −1) −1
		- Page 26: C0αt = C0α(αk −1)
		- Page 26: α −1
		- Page 26: b −1) to be r and the overall lower bound
		- Page 26: min(C0α(αk −1)
		- Page 26: α −1
		- Page 26: r(rk −1)
		- Page 26: r −1
		- Page 27: α −1
		- Page 27: r −1
		- Page 27: 1... ˆJk] ≤C((1 −ϵ)2 + ϵ)k. Here, we temporarily denote ((1 −ϵ)2 + ϵ) to be r. We apply
		- Page 27: r(1 −rk)
		- Page 27: 1 −r
		- Page 27: 1 −r
		- Page 28: Wt+1 = (I −ηHt(I + ρ
		- Page 28: Define ˆJt = (I −ηHt(I + ρ
		- Page 28: Bn −1
		- Page 28: Bn −1
		- Page 28: B −1)k(1 + ρ
		- Page 28: B −1)−1
		- Page 28: αλmin(H))−1
		- Page 28: T ˆJ1] = E[(I −ηHt(I + ρ
		- Page 28: α)H)T (I −ηHt(I + ρ
		- Page 28: = E[I −2ηHt −ηρ
		- Page 28: = I −2ηH −2ηρ
		- Page 28: Bn −1
		- Page 28: Bn −1
		- Page 29: T Mk−1 ˆJk]
		- Page 29: = E[(I −ηHk −ηρ
		- Page 29: α HkH)T Mk−1(I −ηHk −ηρ
		- Page 29: = E[Mk−1 −ηMk−1Hk −ηρ
		- Page 29: α Mk−1HkH −ηHkMk−1 + η2HkMk−1Hk + η2ρ
		- Page 29: α HkMk−1HkH−
		- Page 29: α HHkMk−1 + η2ρ
		- Page 29: α HHkMk−1Hk + η2ρ2
		- Page 29: α2 HHkMk−1HkH]
		- Page 29: = JMk−1J + η2( 1
		- Page 29: nB −1
		- Page 29: HiMk−1Hi)(I + ρ
		- Page 29: Now, we subsititude the expression of Mk−1 into the expression and we will have the follows:
		- Page 29: T ˆJ1... ˆJk] ⪰JMk−1J + η2( 1
		- Page 29: nB −1
		- Page 29: HiMk−1Hi)(I + ρ
		- Page 29: = J[J2(k−1) + η2(k−1)( 1
		- Page 29: Bn −1
		- Page 29: n2 )(k−1)
		- Page 29: αH)Hyk−1...(I + ρ
		- Page 29: αH)...Hyk−1(I + ρ
		- Page 29: nB −1
		- Page 29: Hi[J2(k−1)+
		- Page 29: η2(k−1)( 1
		- Page 29: Bn −1
		- Page 29: n2 )(k−1)
		- Page 29: αH)Hyk−1...(I + ρ
		- Page 29: αH)...Hyk−1(I + ρ
		- Page 29: Bn −1
		- Page 29: Bn −1
		- Page 29: αH)Hyk−1...(I + ρ
		- Page 29: αH)...Hyk−1(I + ρ
		- Page 29: αλmin(H))3 Tr[Hyk−1...(I + ρ
		- Page 29: αH)...Hyk−1(I + ρ
		- Page 29: αλmin(H))4 Tr[Hyk−1H2
		- Page 29: ykHyk−1(I + ρ
		- Page 30: Bn −1
		- Page 30: Bn −1
		- Page 30: Bn −1
		- Page 30: Bn −1
		- Page 30: Bn −1
		- Page 30: Bn −1
		- Page 30: Bn −1
		- Page 30: Bn −1
		- Page 30: Bn −1
		- Page 30: B −1)k(1 + ρ
		- Page 30: B −1)k(1 + ρ
		- Page 30: B −1)−1
		- Page 30: αλmin(H))−1
		- Page 31: Wt+1 = (I −ηHt(I + ρ
		- Page 31: (1 −ϵ)2(k−r)
		- Page 31: nB −1
		- Page 31: B −1
		- Page 31: i ≤2 −ϵ
		- Page 31: nB −1
		- Page 31: nB −1
		- Page 31: (1 −ϵ)2(k−r)
		- Page 31: 1 ˆJ1] = E[(I −η ˆH −ηρ
		- Page 31: ˆHH)T (I −η ˆH −ηρ
		- Page 31: nB −1
		- Page 31: ⪯(1 −ϵ)2N0 + N1
		- Page 31: The first condition (1 −ϵ)2I is achieved when the condition of the assumption is satisfied. We
		- Page 31: J = I −ηH(I + ρ
		- Page 32: −(1 −ϵ)2I ⪯J2 ⪯(1 −ϵ)2I
		- Page 32: J2 ⪯(1 −ϵ)2I
		- Page 32: (I −ηH(I + ρ
		- Page 32: αH))2 ⪯(1 −ϵ)2I
		- Page 32: (I −ηH(I + ρ
		- Page 32: αH)) ⪯(1 −ϵ)I
		- Page 32: i ≤2 −ϵ
		- Page 32: Compared to SGD, the ϵ can be larger as the term I −ηH is larger than I −ηH −η ρ
		- Page 32: k−1
		- Page 32: (1 −ϵ)2(k−1−r)
		- Page 32: k −1
		- Page 32: k−1
		- Page 32: (1 −ϵ)2(k−1−r)
		- Page 32: k −1
		- Page 32: nb −1
		- Page 32: k−1
		- Page 32: (1 −ϵ)2(k−1−r)
		- Page 32: k −1
		- Page 32: ⪯(1 −ϵ)2
		- Page 32: k−1
		- Page 32: (1 −ϵ)2(k−1−r)
		- Page 32: k −1
		- Page 32: nb −1
		- Page 32: k−1
		- Page 32: (1 −ϵ)2(k−1−r)
		- Page 32: k −1
		- Page 32: k−1
		- Page 32: (1 −ϵ)2(k−r)
		- Page 32: k −1
		- Page 32: nb −1
		- Page 32: k−1
		- Page 32: (1 −ϵ)2(k−1−r)
		- Page 32: k −1
		- Page 32: k−1
		- Page 32: (1 −ϵ)2(k−r)
		- Page 32: k −1
		- Page 32: k−1
		- Page 32: (1 −ϵ)2(k−1−r)
		- Page 32: k −1
		- Page 33: k−1
		- Page 33: (1 −ϵ)2(k−r)
		- Page 33: k −1
		- Page 33: (1 −ϵ)2(k−r)
		- Page 33: k −1
		- Page 33: r −1
		- Page 33: = (1 −ϵ)2kN0 +
		- Page 33: k−1
		- Page 33: ((1 −ϵ)2(k−r)
		- Page 33: k −1
		- Page 33: + (1 −ϵ)2(k−r)
		- Page 33: k −1
		- Page 33: r −1
		- Page 33: (1 −ϵ)2(k−r)
		- Page 33: (1 −ϵ)2(k−r)
		- Page 33: (1 −ϵ)2(k−r)ϵr
		- Page 33: = C((1 −ϵ)2 + ϵ)k
		- Page 34: nB −1
		- Page 34: nB −1
		- Page 34: nB −1
		- Page 34: B −1
		- Page 34: B −1
		- Page 34: B −1
		- Page 34: B −1
		- Page 35: Xj ≥u + ϵ) ≤exp(−2ϵn2) ≤exp(−(C + log 1
		- Page 35: δ )) = e−Cδ
		- Page 35: e−Cδ
		- Page 36: 2c −
		- Page 36: 2c −1
		- Page 36: 2c −1
		- Page 36: probability statement. With probability 1 −δ, the eigenvalue of the coherence matrix is upper
		- Page 36: 2c −
		- Page 37: where ˆJ = I −ηHt −ηρ
		- Page 37: JT ˆJ] = E[(I −ηHt −ηρ
		- Page 37: α HHt)(I −ηHt −ηρ
		- Page 37: = E[I −2ηHt −ηρ
		- Page 37: = I −2ηHt −2ηρ
		- Page 37: Bn −1
		- Page 37: JT ˆJ]e1 = 1 −2ηλ1 −2ηρ
		- Page 37: Bn −1
		- Page 37: 1 −2ηλ1 −2ηρ
		- Page 37: Bn −1
		- Page 37: −2ηλ1(1 + ρ
		- Page 37: B −1)(1 + ρ
		- Page 37: −2 + ηλ1(1 + ρ
		- Page 37: B −1)(1 + ρ
		- Page 37: B −1
		- Page 37: B −1 + σ) ≤2
		- Page 37: B −1 + σ)−1
		- Page 38: B −1)−1
		- Page 38: B −1)−1
		- Page 38: nB −η2
		- Page 38: η < λi(H) < 2 −ϵ
		- Page 38: nB −η2


## References not in Bibliography

> [!NOTE]
> The sentences listed below contain references that were not found in the 'References' section.
> *Please note that this list may contain false positives as, e.g., the content of a normal bracket might have been mistaken for a reference, or a natural reference (Authorname in text and year in brackets) might have been mismatched.*

-  This built-in Occam’s razor has been offered as an explanation for why DNNs do not overfit even when they could in principle memorize the training set [Valle-P´erez et al, 2019]
-  To study the long-term behavior of the iterates, we analyze the expected squared norm of the weights: E[∥wk∥2] = E[w⊤ 0 ˆJ⊤ 1 · · · ˆJ⊤ k ˆJk · · · ˆJ1w0] = E[Tr( ˆJk · · · ˆJ1w0w⊤ 0 ˆJ⊤ 1 · · · ˆJ⊤ k )]
-  Assuming w0 ∼N(0, I), we reduce to analyzing the quantity E[Tr( ˆJ⊤ k · · · ˆJ⊤ 1 ˆJ1 · · · ˆJk)], which captures the contraction or expansion behavior of the iterates under the sequence of update matrices
-  (Comparative Divergence Speed) Suppose Tr[J2k] ≤C0αk for some constants C0 and αk, then the divergence rate of the random perturbation method is asymptotically within a constant factor of that of standard SGD: lim k→∞ E[∥wk∥2]Random, lower bound E[∥wk∥2]SGD, lower bound = O(1) 3


## Unused References in Bibliography

> [!NOTE]
> The references listed below were listed in the 'References' section but never used in the document's main text (excluding appendices).
> -> Total = 26
> *Please note that this list may contain false positives as, e.g., the references ID (e.g., first author's lastname + year) was not correctly parsed or the in-text reference was not recognized due to linebreaks.*

- Parsed Ref. ID: Achour et al, 2024
	- Full reference: `E. M. Achour, F. Malgouyres, and S. Gerchinovitz. The loss landscape of deep linear neural networks: a second-order analysis, 2024. URL https://arxiv.org/abs/2107.13289.`
- Parsed Ref. ID: Bhatia, 2013
	- Full reference: `R. Bhatia. Matrix analysis, volume 169. Springer Science & Business Media, 2013.`
- Parsed Ref. ID: Chatterjee, 2020
	- Full reference: `S. Chatterjee. Coherent gradients: An approach to understanding generalization in gradient descentbased optimization. In 8th International Conference on Learning Representations (ICLR), 2020.`
- Parsed Ref. ID: Chen and Flammarion, 2022
	- Full reference: `Z. Chen and N. Flammarion. When and why sam generalizes better: An optimization perspective. arXiv preprint arXiv:2206.09267, 2022.`
- Parsed Ref. ID: Chen et al, 2023a
	- Full reference: `Z. Chen, J. Zhang, Y. Kou, X. Chen, C.-J. Hsieh, and Q. Gu. Why does sharpness-aware minimization generalize better than sgd?, 2023a. URL https://arxiv.org/abs/2310.07269.`
- Parsed Ref. ID: Dinh et al, 2017
	- Full reference: `L. Dinh, R. Pascanu, S. Bengio, and Y. Bengio. Sharp minima can generalize for deep nets. In Proceedings of the 34th International Conference on Machine Learning (ICML), volume 70, pages 1019–1028, 2017.`
- Parsed Ref. ID: Gunasekar et al, 2018
	- Full reference: `S. Gunasekar, B. Woodworth, S. Bhojanapalli, B. Neyshabur, and N. Srebro. Implicit regularization in matrix factorization. In 31st Conference on Learning Theory (COLT), pages 185–210, 2018.`
- Parsed Ref. ID: Hardt et al, 2016
	- Full reference: `M. Hardt, B. Recht, and Y. Singer. Train faster, generalize better: Stability of stochastic gradient descent. In 34th International Conference on Machine Learning (ICML), volume 48, pages 1225–1234, 2016.`
- Parsed Ref. ID: Jiang et al, 2020
	- Full reference: `Y. Jiang, B. Neyshabur, H. Mobahi, D. Krishnan, and S. Bengio. Fantastic generalization measures and where to find them. In 8th International Conference on Learning Representations (ICLR), 2020.`
- Parsed Ref. ID: Kalimeris et al, 2019
	- Full reference: `D. Kalimeris, C. Caramanis, S. Sanghavi, C. Uhler, and A. Risteski. Sgd on neural networks learns functions of increasing complexity. In Advances in Neural Information Processing Systems (NeurIPS) 32, 2019.`
- Parsed Ref. ID: Khanna et al, 2018
	- Full reference: `R. Khanna, B. Kim, J. Ghosh, and O. Koyejo. Interpreting black box predictions using fisher kernels, 2018. URL https://arxiv.org/abs/1810.10118.`
- Parsed Ref. ID: Kwon et al, 2021
	- Full reference: `J. Kwon, S. Yoon, C. Kim, and S. J. Hwang. Asam: Adaptive sharpness-aware minimization for scale-invariant learning of deep neural networks. In 38th International Conference on Machine Learning (ICML), pages 5905–5914, 2021.`
- Parsed Ref. ID: Li et al, 2018
	- Full reference: `H. Li, Z. Xu, G. Taylor, C. Studer, and T. Goldstein. Visualizing the loss landscape of neural nets, 2018. URL https://arxiv.org/abs/1712.09913.`
- Parsed Ref. ID: Lyu and Li, 2019
	- Full reference: `K. Lyu and J. Li. Gradient descent maximizes the margin of homogeneous neural networks. In 7th International Conference on Learning Representations (ICLR), 2019.`
- Parsed Ref. ID: Ma and Ying, 2021
	- Full reference: `C. Ma and L. Ying. On linear stability of sgd and input-smoothness of neural networks, 2021. URL https://arxiv.org/abs/2105.13462.`
- Parsed Ref. ID: Morwani et al, 2023
	- Full reference: `D. Morwani, J. Batra, P. Jain, and P. Netrapalli. Simplicity bias in 1-hidden layer neural networks. In Advances in Neural Information Processing Systems (NeurIPS) 36, 2023.`
- Parsed Ref. ID: Papyan et al, 2020
	- Full reference: `V. Papyan, X. Han, and D. L. Donoho. Prevalence of neural collapse during the terminal phase of deep learning training. Proceedings of the National Academy of Sciences, 117(40):24652–24663, 2020.`
- Parsed Ref. ID: Sankararaman et al, 2020
	- Full reference: `K. A. Sankararaman, S. Sankararaman, H. Pandey, S. Ganguli, and F. Bromberg. The impact of neural network overparameterization on gradient confusion and stochastic gradient descent. In 37th International Conference on Machine Learning (ICML), pages 8469–8479, 2020.`
- Parsed Ref. ID: Soudry et al, 2018
	- Full reference: `D. Soudry, E. Hoffer, M. Nacson, S. Gunasekar, and N. Srebro. The implicit bias of gradient descent on separable data. Journal of Machine Learning Research, 19(70):1–57, 2018.`
- Parsed Ref. ID: Valle-Pérez et al, 2019
	- Full reference: `G. Valle-P´erez, C. Q. Camargo, and A. A. Louis. Deep learning generalizes because the parameterfunction map is biased towards simple functions. In 7th International Conference on Learning Representations (ICLR), 2019.`
- Parsed Ref. ID: Wen et al, 2023b
	- Full reference: `K. Wen, T. Ma, and Z. Li. How does sharpness-aware minimization minimize sharpness?, 2023b. URL https://arxiv.org/abs/2211.05729.`
- Parsed Ref. ID: Wu and Su, 2023
	- Full reference: `L. Wu and W. J. Su. The implicit regularization of dynamical stability in stochastic gradient descent, 2023. URL https://arxiv.org/abs/2305.17490.`
- Parsed Ref. ID: Wu and Ma, 2018
	- Full reference: `L. Wu, C. Ma, et al. How sgd selects the global minima in over-parameterized learning: A dynamical stability perspective. Advances in Neural Information Processing Systems, 31, 2018.`
- Parsed Ref. ID: Wu et al, 2022
	- Full reference: `L. Wu, M. Wang, and W. Su. The alignment property of sgd noise and how it helps select flat minima: A stability analysis, 2022. URL https://arxiv.org/abs/2207.02628.`
- Parsed Ref. ID: Zhang et al, 2024
	- Full reference: `Y. Zhang, H. He, J. Zhu, H. Chen, Y. Wang, and Z. Wei. On the duality between sharpness-aware minimization and adversarial training, 2024. URL https://arxiv.org/abs/2402.15152.`
- Parsed Ref. ID: research et al, 0
	- Full reference: `NeurIPS Paper Checklist The checklist is designed to encourage best practices for responsible machine learning research, addressing issues of reproducibility, transparency, research ethics, and societal impact. Do not remove the checklist: The papers not including the checklist will be desk rejected. The checklist should follow the references and follow the (optional) supplemental material. The checklist does NOT count towards the page limit. Please read the checklist guidelines carefully for information on how to answer these questions. For each question in the checklist: • You should answer [Yes] , [No] , or [NA] . • [NA] means either that the question is Not Applicable for that particular paper or the relevant information is Not Available. • Please provide a short (1–2 sentence) justification right after your answer (even for NA). The checklist answers are an integral part of your paper submission. They are visible to the reviewers, area chairs, senior area chairs, and ethics reviewers. You will be asked to also include it (after eventual revisions) with the final version of your paper, and its final version will be published with the paper. The reviewers of your paper will be asked to use the checklist as one of the factors in their evaluation. While ”[Yes] ” is generally preferable to ”[No] ”, it is perfectly acceptable to answer ”[No] ” provided a proper justification is given (e.g., ”error bars are not reported because it would be too computationally expensive” or ”we were unable to find the license for the dataset we used”). In general, answering ”[No] ” or ”[NA] ” is not grounds for rejection. While the questions are phrased in a binary way, we acknowledge that the true answer is often more nuanced, so please just use your best judgment and write a justification to elaborate. All supporting evidence can appear either in the main paper or the supplemental material, provided in appendix. If you answer [Yes] to a question, in the justification please point to the section(s) where related material for the question can be found. IMPORTANT, please: • Delete this instruction block, but keep the section heading “NeurIPS Paper Checklist”, • Keep the checklist subsection headings, questions/answers and guidelines below. • Do not modify the questions and only use the provided macros for your answers. 1. Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: see main context and abstract Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper. • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers. • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper. 2. Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes] Justification: See the limitation of the paper at the end Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate ”Limitations” section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. • The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. • The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations. 3. Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: [Yes] Justification: See proof in appendix C.9, C.11, C.13, C.7 and theory section Guidelines: • The answer NA means that the paper does not include theoretical results. • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced. • All assumptions should be clearly stated or referenced in the statement of any theorems. • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. • Theorems and Lemmas that the proof relies upon should be properly referenced. 4. Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: [Yes] Justification: See experiment section in main context and details in section C.5, C.3, C.4 Guidelines: • The answer NA means that the paper does not include experiments. • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. • Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results. 5. Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? Answer: [No] Justification: Will provide code in camera ready version once accpeted Guidelines: • The answer NA means that paper does not include experiments requiring code. • Please see the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• While we encourage the release of code and data, we understand that this might not bepossible, so “No” is an acceptable answer. Papers cannot be rejected simply for notincluding code, unless this is central to the contribution (e.g., for a new open-sourcebenchmark).• The instructions should contain the exact command and environment needed to run toreproduce the results. See the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• The authors should provide instructions on data access and preparation, including howto access the raw data, preprocessed data, intermediate data, and generated data, etc.• The authors should provide scripts to reproduce all experimental results for the newproposed method and baselines. If only a subset of experiments are reproducible, theyshould state which ones are omitted from the script and why.• At submission time, to preserve anonymity, the authors should release anonymizedversions (if applicable).• Providing as much information as possible in supplemental material (appended to thepaper) is recommended, but including URLs to data and code is permitted.6. Experimental setting/detailsQuestion: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand theresults?Answer: [Yes]Justification: See experiment in main context and details in section C.5, C.3, C.4Guidelines:• The answer NA means that the paper does not include experiments.• The experimental setting should be presented in the core of the paper to a level ofdetail that is necessary to appreciate the results and make sense of them.• The full details can be provided either with the code, in appendix, or as supplementalmaterial.7. Experiment statistical significanceQuestion: Does the paper report error bars suitably and correctly defined or other appropriateinformation about the statistical significance of the experiments?Answer: [Yes]Justification: See experiment section and details in section C.5, C.3, C.4Guidelines:• The answer NA means that the paper does not include experiments.• The authors should answer ”Yes” if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that supportthe main claims of the paper.• The factors of variability that the error bars are capturing should be clearly stated (forexample, train/test split, initialization, random drawing of some parameter, or overallrun with given experimental conditions).• The method for calculating the error bars should be explained (closed form formula,call to a library function, bootstrap, etc.)• The assumptions made should be given (e.g., Normally distributed errors).• It should be clear whether the error bar is the standard deviation or the standard errorof the mean.• It is OK to report 1-sigma error bars, but one should state it. The authors shouldpreferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesisof Normality of errors is not verified.• For asymmetric distributions, the authors should be careful not to show in tables orfigures symmetric error bars that would yield results that are out of range (e.g. negativeerror rates).• If error bars are reported in tables or plots, The authors should explain in the text howthey were calculated and reference the corresponding figures or tables in the text.8. Experiments compute resourcesQuestion: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproducethe experiments?Answer: [Yes]Justification: See experiment section in main content and details in section C.5, C.3,C.4Guidelines:• The answer NA means that the paper does not include experiments.• The paper should indicate the type of compute workers CPU or GPU, internal cluster,or cloud provider, including relevant memory and storage.• The paper should provide the amount of compute required for each of the individualexperimental runs as well as estimate the total compute.• The paper should disclose whether the full research project required more computethan the experiments reported in the paper (e.g., preliminary or failed experiments thatdidn’t make it into the paper).9. Code of ethicsQuestion: Does the research conducted in the paper conform, in every respect, with theNeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines?Answer: [Yes]Justification: See details in experiment section in main context and details in sectionC.5, C.3, C.4Guidelines:• The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics.• If the authors answer No, they should explain the special circumstances that require adeviation from the Code of Ethics.• The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).10. Broader impactsQuestion: Does the paper discuss both potential positive societal impacts and negativesocietal impacts of the work performed?Answer: [NA]Justification:Guidelines:• The answer NA means that there is no societal impact of the work performed.• If the authors answer NA or No, they should explain why their work has no societalimpact or why the paper does not address societal impact.• Examples of negative societal impacts include potential malicious or unintended uses(e.g., disinformation, generating fake profiles, surveillance), fairness considerations(e.g., deployment of technologies that could make decisions that unfairly impact specific groups), privacy considerations, and security considerations.• The conference expects that many papers will be foundational research and not tiedto particular applications, let alone deployments. However, if there is a direct path toany negative applications, the authors should point it out. For example, it is legitimateto point out that an improvement in the quality of generative models could be used togenerate deepfakes for disinformation. On the other hand, it is not needed to point outthat a generic algorithm for optimizing neural networks could enable people to trainmodels that generate Deepfakes faster.• The authors should consider possible harms that could arise when the technology isbeing used as intended and functioning correctly, harms that could arise when thetechnology is being used as intended but gives incorrect results, and harms followingfrom (intentional or unintentional) misuse of the technology.• If there are negative societal impacts, the authors could also discuss possible mitigationstrategies (e.g., gated release of models, providing defenses in addition to attacks,mechanisms for monitoring misuse, mechanisms to monitor how a system learns fromfeedback over time, improving the efficiency and accessibility of ML).11. SafeguardsQuestion: Does the paper describe safeguards that have been put in place for responsiblerelease of data or models that have a high risk for misuse (e.g., pretrained language models,image generators, or scraped datasets)?Answer: [NA]Justification:Guidelines:• The answer NA means that the paper poses no such risks.• Released models that have a high risk for misuse or dual-use should be releasedwith necessary safeguards to allow for controlled use of the model, for example byrequiring that users adhere to usage guidelines or restrictions to access the model orimplementing safety filters.• Datasets that have been scraped from the Internet could pose safety risks. The authorsshould describe how they avoided releasing unsafe images.• We recognize that providing effective safeguards is challenging, and many papers donot require this, but we encourage authors to take this into account and make a bestfaith effort.12. Licenses for existing assetsQuestion: Are the creators or original owners of assets (e.g., code, data, models), used inthe paper, properly credited and are the license and terms of use explicitly mentioned andproperly respected?Answer: [NA]Justification: See experiment section in main context and details in section C.5, C.3,C.4 and related work in appendix BGuidelines:• The answer NA means that the paper does not use existing assets.• The authors should cite the original paper that produced the code package or dataset.• The authors should state which version of the asset is used and, if possible, include aURL.• The name of the license (e.g., CC-BY 4.0) should be included for each asset.• For scraped data from a particular source (e.g., website), the copyright and terms ofservice of that source should be provided.• If assets are released, the license, copyright information, and terms of use in thepackage should be provided. For popular datasets, paperswithcode.com/datasetshas curated licenses for some datasets. Their licensing guide can help determine thelicense of a dataset.• For existing datasets that are re-packaged, both the original license and the license ofthe derived asset (if it has changed) should be provided.• If this information is not available online, the authors are encouraged to reach out tothe asset’s creators.13. New assetsQuestion: Are new assets introduced in the paper well documented and is the documentationprovided alongside the assets?Answer: [NA]Justification:Guidelines:• The answer NA means that the paper does not release new assets.• Researchers should communicate the details of the dataset/code/model as part of theirsubmissions via structured templates. This includes details about training, license,limitations, etc.• The paper should discuss whether and how consent was obtained from people whoseasset is used.• At submission time, remember to anonymize your assets (if applicable). You can eithercreate an anonymized URL or include an anonymized zip file.14. Crowdsourcing and research with human subjectsQuestion: For crowdsourcing experiments and research with human subjects, does the paperinclude the full text of instructions given to participants and screenshots, if applicable, aswell as details about compensation (if any)?Answer: [NA]Justification:Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should beincluded in the main paper.• According to the NeurIPS Code of Ethics, workers involved in data collection, curation,or other labor should be paid at least the minimum wage in the country of the datacollector.15. Institutional review board (IRB) approvals or equivalent for research with humansubjectsQuestion: Does the paper describe potential risks incurred by study participants, whethersuch risks were disclosed to the subjects, and whether Institutional Review Board (IRB)approvals (or an equivalent approval/review based on the requirements of your country orinstitution) were obtained?Answer: [NA]Justification:Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Depending on the country in which research is conducted, IRB approval (or equivalent)may be required for any human subjects research. If you obtained IRB approval, youshould clearly state this in the paper.• We recognize that the procedures for this may vary significantly between institutionsand locations, and we expect authors to adhere to the NeurIPS Code of Ethics and theguidelines for their institution.• For initial submissions, do not include any information that would break anonymity (ifapplicable), such as the institution conducting the review.16. Declaration of LLM usageQuestion: Does the paper describe the usage of LLMs if it is an important, original, ornon-standard component of the core methods in this research? Note that if the LLM is usedonly for writing, editing, or formatting purposes and does not impact the core methodology,scientific rigorousness, or originality of the research, declaration is not required.Answer: [NA]Justification:Guidelines:• The answer NA means that the core method development in this research does notinvolve LLMs as any important, original, or non-standard components.• Please refer to our LLM policy (https://neurips.cc/Conferences/2025/LLM)for what should or should not be described.`


## Frequently Referenced Authors

> [!NOTE]
> The following authors appear more than 2 times in the bibliography.
> *Please note that only the lastname and the first letter of the first name are compared for counting.*

- Flammarion N.: 3
- Mobahi H.: 3
- Chen Z.: 3
- Neyshabur B.: 3
- Wu L.: 3


## Reference Checker Results

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/27 A Unified Stability Analysis/literature_validation_results_fig.jpg]]

References section starts on page 10.

- No link provided: $23/40=57.50\%$
- Unchecked links: $2/40=5.00\%$
- Valid links: $0/40=0.00\%$
- Invalid link: $15/40=37.50\%$
	- Invalid entries:
		=> total = 15
		- E. M. Achour, F. Malgouyres, and S. Gerchinovitz. The loss landscape of deep linear neural networks: a second-order analysis, 2024. URL https://arxiv.org/abs/2107.13289.
			-> Returned with status code 404!
		- M. Andriushchenko and N. Flammarion. Towards understanding sharpness-aware minimization, 2022. URL https://arxiv.org/abs/2206.06232.
			-> Returned with status code 404!
		- D. Bisla, J. Wang, and A. Choromanska. Low-pass filtering sgd for recovering flat optima in the deep learning optimization landscape, 2022. URL https://arxiv.org/abs/2201.08025.
			-> Returned with status code 404!
		- Z. Chen, J. Zhang, Y. Kou, X. Chen, C.-J. Hsieh, and Q. Gu. Why does sharpness-aware minimization generalize better than sgd?, 2023a. URL https://arxiv.org/abs/2310.07269.
			-> Returned with status code 404!
		- J. Du, H. Yan, J. Feng, J. T. Zhou, L. Zhen, R. S. M. Goh, and V. Y. F. Tan. Efficient sharpness-aware minimization for improved training of neural networks, 2022. URL https://arxiv.org/abs/2110.03141.
			-> Returned with status code 404!
		- R. Khanna, B. Kim, J. Ghosh, and O. Koyejo. Interpreting black box predictions using fisher kernels, 2018. URL https://arxiv.org/abs/1810.10118.
			-> Returned with status code 404!
		- H. Li, Z. Xu, G. Taylor, C. Studer, and T. Goldstein. Visualizing the loss landscape of neural nets, 2018. URL https://arxiv.org/abs/1712.09913.
			-> Returned with status code 404!
		- C. Ma and L. Ying. On linear stability of sgd and input-smoothness of neural networks, 2021. URL https://arxiv.org/abs/2105.13462.
			-> Returned with status code 404!
		- K. Wen, Z. Li, and T. Ma. Sharpness minimization algorithms do not only minimize sharpness to achieve better generalization, 2023a. URL https://arxiv.org/abs/2307.11007.
			-> Returned with status code 404!
		- K. Wen, T. Ma, and Z. Li. How does sharpness-aware minimization minimize sharpness?, 2023b. URL https://arxiv.org/abs/2211.05729.
			-> Returned with status code 404!
		- L. Wu and W. J. Su. The implicit regularization of dynamical stability in stochastic gradient descent, 2023. URL https://arxiv.org/abs/2305.17490.
			-> Returned with status code 404!
		- L. Wu, M. Wang, and W. Su. The alignment property of sgd noise and how it helps select flat minima: A stability analysis, 2022. URL https://arxiv.org/abs/2207.02628.
			-> Returned with status code 404!
		- Y. Zhang, H. He, J. Zhu, H. Chen, Y. Wang, and Z. Wei. On the duality between sharpness-aware minimization and adversarial training, 2024. URL https://arxiv.org/abs/2402.15152.
			-> Returned with status code 404!
		- Z. Zhou, M. Wang, Y. Mao, B. Li, and J. Yan. Sharpness-aware minimization efficiently selects flatter minima late in training, 2025. URL https://arxiv.org/abs/2410.10373.
			-> Returned with status code 404!
		- NeurIPS Paper Checklist The checklist is designed to encourage best practices for responsible machine learning research, addressing issues of reproducibility, transparency, research ethics, and societal impact. Do not remove the checklist: The papers not including the checklist will be desk rejected. The checklist should follow the references and follow the (optional) supplemental material. The checklist does NOT count towards the page limit. Please read the checklist guidelines carefully for information on how to answer these questions. For each question in the checklist: • You should answer \[Yes\] , \[No\] , or \[NA\] . • \[NA\] means either that the question is Not Applicable for that particular paper or the relevant information is Not Available. • Please provide a short (1–2 sentence) justification right after your answer (even for NA). The checklist answers are an integral part of your paper submission. They are visible to the reviewers, area chairs, senior area chairs, and ethics reviewers. You will be asked to also include it (after eventual revisions) with the final version of your paper, and its final version will be published with the paper. The reviewers of your paper will be asked to use the checklist as one of the factors in their evaluation. While ”\[Yes\] ” is generally preferable to ”\[No\] ”, it is perfectly acceptable to answer ”\[No\] ” provided a proper justification is given (e.g., ”error bars are not reported because it would be too computationally expensive” or ”we were unable to find the license for the dataset we used”). In general, answering ”\[No\] ” or ”\[NA\] ” is not grounds for rejection. While the questions are phrased in a binary way, we acknowledge that the true answer is often more nuanced, so please just use your best judgment and write a justification to elaborate. All supporting evidence can appear either in the main paper or the supplemental material, provided in appendix. If you answer \[Yes\] to a question, in the justification please point to the section(s) where related material for the question can be found. IMPORTANT, please: • Delete this instruction block, but keep the section heading “NeurIPS Paper Checklist”, • Keep the checklist subsection headings, questions/answers and guidelines below. • Do not modify the questions and only use the provided macros for your answers. 1. Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: \[Yes\] Justification: see main context and abstract Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper. • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers. • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper. 2. Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: \[Yes\] Justification: See the limitation of the paper at the end Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate ”Limitations” section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. • The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. • The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations. 3. Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: \[Yes\] Justification: See proof in appendix C.9, C.11, C.13, C.7 and theory section Guidelines: • The answer NA means that the paper does not include theoretical results. • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced. • All assumptions should be clearly stated or referenced in the statement of any theorems. • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. • Theorems and Lemmas that the proof relies upon should be properly referenced. 4. Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: \[Yes\] Justification: See experiment section in main context and details in section C.5, C.3, C.4 Guidelines: • The answer NA means that the paper does not include experiments. • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. • Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results. 5. Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? Answer: \[No\] Justification: Will provide code in camera ready version once accpeted Guidelines: • The answer NA means that paper does not include experiments requiring code. • Please see the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• While we encourage the release of code and data, we understand that this might not bepossible, so “No” is an acceptable answer. Papers cannot be rejected simply for notincluding code, unless this is central to the contribution (e.g., for a new open-sourcebenchmark).• The instructions should contain the exact command and environment needed to run toreproduce the results. See the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• The authors should provide instructions on data access and preparation, including howto access the raw data, preprocessed data, intermediate data, and generated data, etc.• The authors should provide scripts to reproduce all experimental results for the newproposed method and baselines. If only a subset of experiments are reproducible, theyshould state which ones are omitted from the script and why.• At submission time, to preserve anonymity, the authors should release anonymizedversions (if applicable).• Providing as much information as possible in supplemental material (appended to thepaper) is recommended, but including URLs to data and code is permitted.6. Experimental setting/detailsQuestion: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand theresults?Answer: \[Yes\]Justification: See experiment in main context and details in section C.5, C.3, C.4Guidelines:• The answer NA means that the paper does not include experiments.• The experimental setting should be presented in the core of the paper to a level ofdetail that is necessary to appreciate the results and make sense of them.• The full details can be provided either with the code, in appendix, or as supplementalmaterial.7. Experiment statistical significanceQuestion: Does the paper report error bars suitably and correctly defined or other appropriateinformation about the statistical significance of the experiments?Answer: \[Yes\]Justification: See experiment section and details in section C.5, C.3, C.4Guidelines:• The answer NA means that the paper does not include experiments.• The authors should answer ”Yes” if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that supportthe main claims of the paper.• The factors of variability that the error bars are capturing should be clearly stated (forexample, train/test split, initialization, random drawing of some parameter, or overallrun with given experimental conditions).• The method for calculating the error bars should be explained (closed form formula,call to a library function, bootstrap, etc.)• The assumptions made should be given (e.g., Normally distributed errors).• It should be clear whether the error bar is the standard deviation or the standard errorof the mean.• It is OK to report 1-sigma error bars, but one should state it. The authors shouldpreferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesisof Normality of errors is not verified.• For asymmetric distributions, the authors should be careful not to show in tables orfigures symmetric error bars that would yield results that are out of range (e.g. negativeerror rates).• If error bars are reported in tables or plots, The authors should explain in the text howthey were calculated and reference the corresponding figures or tables in the text.8. Experiments compute resourcesQuestion: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproducethe experiments?Answer: \[Yes\]Justification: See experiment section in main content and details in section C.5, C.3,C.4Guidelines:• The answer NA means that the paper does not include experiments.• The paper should indicate the type of compute workers CPU or GPU, internal cluster,or cloud provider, including relevant memory and storage.• The paper should provide the amount of compute required for each of the individualexperimental runs as well as estimate the total compute.• The paper should disclose whether the full research project required more computethan the experiments reported in the paper (e.g., preliminary or failed experiments thatdidn’t make it into the paper).9. Code of ethicsQuestion: Does the research conducted in the paper conform, in every respect, with theNeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines?Answer: \[Yes\]Justification: See details in experiment section in main context and details in sectionC.5, C.3, C.4Guidelines:• The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics.• If the authors answer No, they should explain the special circumstances that require adeviation from the Code of Ethics.• The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).10. Broader impactsQuestion: Does the paper discuss both potential positive societal impacts and negativesocietal impacts of the work performed?Answer: \[NA\]Justification:Guidelines:• The answer NA means that there is no societal impact of the work performed.• If the authors answer NA or No, they should explain why their work has no societalimpact or why the paper does not address societal impact.• Examples of negative societal impacts include potential malicious or unintended uses(e.g., disinformation, generating fake profiles, surveillance), fairness considerations(e.g., deployment of technologies that could make decisions that unfairly impact specific groups), privacy considerations, and security considerations.• The conference expects that many papers will be foundational research and not tiedto particular applications, let alone deployments. However, if there is a direct path toany negative applications, the authors should point it out. For example, it is legitimateto point out that an improvement in the quality of generative models could be used togenerate deepfakes for disinformation. On the other hand, it is not needed to point outthat a generic algorithm for optimizing neural networks could enable people to trainmodels that generate Deepfakes faster.• The authors should consider possible harms that could arise when the technology isbeing used as intended and functioning correctly, harms that could arise when thetechnology is being used as intended but gives incorrect results, and harms followingfrom (intentional or unintentional) misuse of the technology.• If there are negative societal impacts, the authors could also discuss possible mitigationstrategies (e.g., gated release of models, providing defenses in addition to attacks,mechanisms for monitoring misuse, mechanisms to monitor how a system learns fromfeedback over time, improving the efficiency and accessibility of ML).11. SafeguardsQuestion: Does the paper describe safeguards that have been put in place for responsiblerelease of data or models that have a high risk for misuse (e.g., pretrained language models,image generators, or scraped datasets)?Answer: \[NA\]Justification:Guidelines:• The answer NA means that the paper poses no such risks.• Released models that have a high risk for misuse or dual-use should be releasedwith necessary safeguards to allow for controlled use of the model, for example byrequiring that users adhere to usage guidelines or restrictions to access the model orimplementing safety filters.• Datasets that have been scraped from the Internet could pose safety risks. The authorsshould describe how they avoided releasing unsafe images.• We recognize that providing effective safeguards is challenging, and many papers donot require this, but we encourage authors to take this into account and make a bestfaith effort.12. Licenses for existing assetsQuestion: Are the creators or original owners of assets (e.g., code, data, models), used inthe paper, properly credited and are the license and terms of use explicitly mentioned andproperly respected?Answer: \[NA\]Justification: See experiment section in main context and details in section C.5, C.3,C.4 and related work in appendix BGuidelines:• The answer NA means that the paper does not use existing assets.• The authors should cite the original paper that produced the code package or dataset.• The authors should state which version of the asset is used and, if possible, include aURL.• The name of the license (e.g., CC-BY 4.0) should be included for each asset.• For scraped data from a particular source (e.g., website), the copyright and terms ofservice of that source should be provided.• If assets are released, the license, copyright information, and terms of use in thepackage should be provided. For popular datasets, paperswithcode.com/datasetshas curated licenses for some datasets. Their licensing guide can help determine thelicense of a dataset.• For existing datasets that are re-packaged, both the original license and the license ofthe derived asset (if it has changed) should be provided.• If this information is not available online, the authors are encouraged to reach out tothe asset’s creators.13. New assetsQuestion: Are new assets introduced in the paper well documented and is the documentationprovided alongside the assets?Answer: \[NA\]Justification:Guidelines:• The answer NA means that the paper does not release new assets.• Researchers should communicate the details of the dataset/code/model as part of theirsubmissions via structured templates. This includes details about training, license,limitations, etc.• The paper should discuss whether and how consent was obtained from people whoseasset is used.• At submission time, remember to anonymize your assets (if applicable). You can eithercreate an anonymized URL or include an anonymized zip file.14. Crowdsourcing and research with human subjectsQuestion: For crowdsourcing experiments and research with human subjects, does the paperinclude the full text of instructions given to participants and screenshots, if applicable, aswell as details about compensation (if any)?Answer: \[NA\]Justification:Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should beincluded in the main paper.• According to the NeurIPS Code of Ethics, workers involved in data collection, curation,or other labor should be paid at least the minimum wage in the country of the datacollector.15. Institutional review board (IRB) approvals or equivalent for research with humansubjectsQuestion: Does the paper describe potential risks incurred by study participants, whethersuch risks were disclosed to the subjects, and whether Institutional Review Board (IRB)approvals (or an equivalent approval/review based on the requirements of your country orinstitution) were obtained?Answer: \[NA\]Justification:Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Depending on the country in which research is conducted, IRB approval (or equivalent)may be required for any human subjects research. If you obtained IRB approval, youshould clearly state this in the paper.• We recognize that the procedures for this may vary significantly between institutionsand locations, and we expect authors to adhere to the NeurIPS Code of Ethics and theguidelines for their institution.• For initial submissions, do not include any information that would break anonymity (ifapplicable), such as the institution conducting the review.16. Declaration of LLM usageQuestion: Does the paper describe the usage of LLMs if it is an important, original, ornon-standard component of the core methods in this research? Note that if the LLM is usedonly for writing, editing, or formatting purposes and does not impact the core methodology,scientific rigorousness, or originality of the research, declaration is not required.Answer: \[NA\]Justification:Guidelines:• The answer NA means that the core method development in this research does notinvolve LLMs as any important, original, or non-standard components.• Please refer to our LLM policy (https://neurips.cc/Conferences/2025/LLM)for what should or should not be described.
			-> Returned with status code 404!

- Different links: $0/40=0.00\%$

- Successful searches: $13/40=32.50\%$
- Skipped searches: $0/40=0.00\%$
- Mismatching infos: $11/40=27.50\%$
	- **Entries with mismatching author information:**
		=> total = 7
		- `D. Kalimeris, C. Caramanis, S. Sanghavi, C. Uhler, and A. Risteski. Sgd on neural networks learns functions of increasing complexity. In Advances in Neural Information Processing Systems (NeurIPS) 32, 2019.`
			- Authors (Nakkiran, Kaplun, Yang, Edelman, Zhang, Barak) did not match found publication titled 'SGD on Neural Networks Learns Functions of Increasing Complexity'
		- `N. S. Keskar, D. Mudigere, J. Nocedal, P. Tak PT, Y. Smelyanskiy, and P. T. P. Tang. On large-batch training for deep learning: Generalization gap and sharp minima. In 5th International Conference on Learning Representations (ICLR), 2017.`
			- Authors () did not match found publication titled 'On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima'
		- `J. Kwon, S. Yoon, C. Kim, and S. J. Hwang. Asam: Adaptive sharpness-aware minimization for scale-invariant learning of deep neural networks. In 38th International Conference on Machine Learning (ICML), pages 5905–5914, 2021.`
			- Authors (Park, Choi) did not match found publication titled 'ASAM: Adaptive Sharpness-Aware Minimization for Scale-Invariant Learning of Deep Neural Networks'
		- `H. Li, Z. Xu, G. Taylor, C. Studer, and T. Goldstein. Visualizing the loss landscape of neural nets, 2018. URL https://arxiv.org/abs/1712.09913.`
			- Authors (0022, 0002) did not match found publication titled 'Visualizing the Loss Landscape of Neural Nets.'
		- `C. Ma and L. Ying. On linear stability of sgd and input-smoothness of neural networks, 2021. URL https://arxiv.org/abs/2105.13462.`
			- Authors (0012) did not match found publication titled 'On Linear Stability of SGD and Input-Smoothness of Neural Networks.'
		- ==`K. A. Sankararaman, S. Sankararaman, H. Pandey, S. Ganguli, and F. Bromberg. The impact of neural network overparameterization on gradient confusion and stochastic gradient descent. In 37th International Conference on Machine Learning (ICML), pages 8469–8479, 2020.`==
			- Authors (Xu, Huang, Goldstein) did not match found publication titled 'The Impact of Neural Network Overparameterization on Gradient Confusion and Stochastic Gradient Descent'
		- `D. Soudry, E. Hoffer, M. Nacson, S. Gunasekar, and N. Srebro. The implicit bias of gradient descent on separable data. Journal of Machine Learning Research, 19(70):1–57, 2018.`
			- Authors () did not match found publication titled 'The Implicit Bias of Gradient Descent on Separable Data'
	- **Entries with mismatching years (where the difference is = 1 year):**
		=> total = 4
		- `P. Foret, A. Kleiner, H. Mobahi, and B. Neyshabur. Sharpness-aware minimization for efficiently improving generalization. In 9th International Conference on Learning Representations (ICLR), 2021.`
			- Year (2020) does not match expected year (2021)
		- `S. Gunasekar, B. Woodworth, S. Bhojanapalli, B. Neyshabur, and N. Srebro. Implicit regularization in matrix factorization. In 31st Conference on Learning Theory (COLT), pages 185–210, 2018.`
			- Year (2017) does not match expected year (2018)
		- `M. Hardt, B. Recht, and Y. Singer. Train faster, generalize better: Stability of stochastic gradient descent. In 34th International Conference on Machine Learning (ICML), volume 48, pages 1225–1234, 2016.`
			- Year (2015) does not match expected year (2016)
		- `Y. Jiang, B. Neyshabur, H. Mobahi, D. Krishnan, and S. Bengio. Fantastic generalization measures and where to find them. In 8th International Conference on Learning Representations (ICLR), 2020.`
			- Year (2019) does not match expected year (2020)
- No entry found: $16/40=40.00\%$
	- Unfound entries:
		=> total = 16
		- R. Bhatia. Matrix analysis, volume 169. Springer Science & Business Media, 2013.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: None of the 69 results matched the expected title!
		- D. Bisla, J. Wang, and A. Choromanska. Low-pass filtering sgd for recovering flat optima in the deep learning optimization landscape, 2022. URL https://arxiv.org/abs/2201.08025.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!
		- S. Chatterjee. Coherent gradients: An approach to understanding generalization in gradient descentbased optimization. In 8th International Conference on Learning Representations (ICLR), 2020.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!
		- ==Z. Chen and N. Flammarion. When and why sam generalizes better: An optimization perspective. arXiv preprint arXiv:2206.09267, 2022.==
			-> WARNING: No results were found through the dblp search! | WARNING: No results were found through the dblp search!
		- Z. Chen, J. Zhang, Y. Kou, X. Chen, C.-J. Hsieh, and Q. Gu. Why does sharpness-aware minimization generalize better than sgd?, 2023a. URL https://arxiv.org/abs/2310.07269.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- Z. Chen, J. Zhang, Y. Kou, X. Chen, C.-J. Hsieh, and Q. Gu. Why does sharpness-aware minimization generalize better than sgd? In Advances in Neural Information Processing Systems (NeurIPS), 2023b. URL https://openreview.net/forum?id=3WAnGWLpSQ.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- J. Du, H. Yan, J. Feng, J. T. Zhou, L. Zhen, R. S. M. Goh, and V. Y. F. Tan. Efficient sharpness-aware minimization for improved training of neural networks, 2022. URL https://arxiv.org/abs/2110.03141.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- S. Hochreiter and J. Schmidhuber. Flat minima. Neural Computation, 9(1):1–42, 1997.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- G. Valle-P´erez, C. Q. Camargo, and A. A. Louis. Deep learning generalizes because the parameterfunction map is biased towards simple functions. In 7th International Conference on Learning Representations (ICLR), 2019.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!
		- K. Wen, Z. Li, and T. Ma. Sharpness minimization algorithms do not only minimize sharpness to achieve better generalization, 2023a. URL https://arxiv.org/abs/2307.11007.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- K. Wen, T. Ma, and Z. Li. How does sharpness-aware minimization minimize sharpness?, 2023b. URL https://arxiv.org/abs/2211.05729.
			-> WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!
		- L. Wu and W. J. Su. The implicit regularization of dynamical stability in stochastic gradient descent, 2023. URL https://arxiv.org/abs/2305.17490.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!
		- L. Wu, M. Wang, and W. Su. The alignment property of sgd noise and how it helps select flat minima: A stability analysis, 2022. URL https://arxiv.org/abs/2207.02628.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!
		- Y. Zhang, H. He, J. Zhu, H. Chen, Y. Wang, and Z. Wei. On the duality between sharpness-aware minimization and adversarial training, 2024. URL https://arxiv.org/abs/2402.15152.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!
		- Z. Zhou, M. Wang, Y. Mao, B. Li, and J. Yan. Sharpness-aware minimization efficiently selects flatter minima late in training, 2025. URL https://arxiv.org/abs/2410.10373.
			-> WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!
		- NeurIPS Paper Checklist
			- The checklist is designed to encourage best practices for responsible machine learning research, addressing issues of reproducibility, transparency, research ethics, and societal impact. Do not remove the checklist: The papers not including the checklist will be desk rejected. The checklist should follow the references and follow the (optional) supplemental material. The checklist does NOT count towards the page limit. Please read the checklist guidelines carefully for information on how to answer these questions. For each question in the checklist: • You should answer \[Yes\] , \[No\] , or \[NA\] . • \[NA\] means either that the question is Not Applicable for that particular paper or the relevant information is Not Available. • Please provide a short (1–2 sentence) justification right after your answer (even for NA). The checklist answers are an integral part of your paper submission. They are visible to the reviewers, area chairs, senior area chairs, and ethics reviewers. You will be asked to also include it (after eventual revisions) with the final version of your paper, and its final version will be published with the paper. The reviewers of your paper will be asked to use the checklist as one of the factors in their evaluation. While ”\[Yes\] ” is generally preferable to ”\[No\] ”, it is perfectly acceptable to answer ”\[No\] ” provided a proper justification is given (e.g., ”error bars are not reported because it would be too computationally expensive” or ”we were unable to find the license for the dataset we used”). In general, answering ”\[No\] ” or ”\[NA\] ” is not grounds for rejection. While the questions are phrased in a binary way, we acknowledge that the true answer is often more nuanced, so please just use your best judgment and write a justification to elaborate. All supporting evidence can appear either in the main paper or the supplemental material, provided in appendix. If you answer \[Yes\] to a question, in the justification please point to the section(s) where related material for the question can be found. IMPORTANT, please: • Delete this instruction block, but keep the section heading “NeurIPS Paper Checklist”, • Keep the checklist subsection headings, questions/answers and guidelines below. • Do not modify the questions and only use the provided macros for your answers. 1. Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: \[Yes\] Justification: see main context and abstract Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper. • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers. • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper. 2. Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: \[Yes\] Justification: See the limitation of the paper at the end Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate ”Limitations” section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. • The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. • The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations. 3. Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: \[Yes\] Justification: See proof in appendix C.9, C.11, C.13, C.7 and theory section Guidelines: • The answer NA means that the paper does not include theoretical results. • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced. • All assumptions should be clearly stated or referenced in the statement of any theorems. • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. • Theorems and Lemmas that the proof relies upon should be properly referenced. 4. Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: \[Yes\] Justification: See experiment section in main context and details in section C.5, C.3, C.4 Guidelines: • The answer NA means that the paper does not include experiments. • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. • Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results. 5. Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? Answer: \[No\] Justification: Will provide code in camera ready version once accpeted Guidelines: • The answer NA means that paper does not include experiments requiring code. • Please see the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• While we encourage the release of code and data, we understand that this might not bepossible, so “No” is an acceptable answer. Papers cannot be rejected simply for notincluding code, unless this is central to the contribution (e.g., for a new open-sourcebenchmark).• The instructions should contain the exact command and environment needed to run toreproduce the results. See the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details.• The authors should provide instructions on data access and preparation, including howto access the raw data, preprocessed data, intermediate data, and generated data, etc.• The authors should provide scripts to reproduce all experimental results for the newproposed method and baselines. If only a subset of experiments are reproducible, theyshould state which ones are omitted from the script and why.• At submission time, to preserve anonymity, the authors should release anonymizedversions (if applicable).• Providing as much information as possible in supplemental material (appended to thepaper) is recommended, but including URLs to data and code is permitted.6. Experimental setting/detailsQuestion: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand theresults?Answer: \[Yes\]Justification: See experiment in main context and details in section C.5, C.3, C.4Guidelines:• The answer NA means that the paper does not include experiments.• The experimental setting should be presented in the core of the paper to a level ofdetail that is necessary to appreciate the results and make sense of them.• The full details can be provided either with the code, in appendix, or as supplementalmaterial.7. Experiment statistical significanceQuestion: Does the paper report error bars suitably and correctly defined or other appropriateinformation about the statistical significance of the experiments?Answer: \[Yes\]Justification: See experiment section and details in section C.5, C.3, C.4Guidelines:• The answer NA means that the paper does not include experiments.• The authors should answer ”Yes” if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that supportthe main claims of the paper.• The factors of variability that the error bars are capturing should be clearly stated (forexample, train/test split, initialization, random drawing of some parameter, or overallrun with given experimental conditions).• The method for calculating the error bars should be explained (closed form formula,call to a library function, bootstrap, etc.)• The assumptions made should be given (e.g., Normally distributed errors).• It should be clear whether the error bar is the standard deviation or the standard errorof the mean.• It is OK to report 1-sigma error bars, but one should state it. The authors shouldpreferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesisof Normality of errors is not verified.• For asymmetric distributions, the authors should be careful not to show in tables orfigures symmetric error bars that would yield results that are out of range (e.g. negativeerror rates).• If error bars are reported in tables or plots, The authors should explain in the text howthey were calculated and reference the corresponding figures or tables in the text.8. Experiments compute resourcesQuestion: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproducethe experiments?Answer: \[Yes\]Justification: See experiment section in main content and details in section C.5, C.3,C.4Guidelines:• The answer NA means that the paper does not include experiments.• The paper should indicate the type of compute workers CPU or GPU, internal cluster,or cloud provider, including relevant memory and storage.• The paper should provide the amount of compute required for each of the individualexperimental runs as well as estimate the total compute.• The paper should disclose whether the full research project required more computethan the experiments reported in the paper (e.g., preliminary or failed experiments thatdidn’t make it into the paper).9. Code of ethicsQuestion: Does the research conducted in the paper conform, in every respect, with theNeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines?Answer: \[Yes\]Justification: See details in experiment section in main context and details in sectionC.5, C.3, C.4Guidelines:• The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics.• If the authors answer No, they should explain the special circumstances that require adeviation from the Code of Ethics.• The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).10. Broader impactsQuestion: Does the paper discuss both potential positive societal impacts and negativesocietal impacts of the work performed?Answer: \[NA\]Justification:Guidelines:• The answer NA means that there is no societal impact of the work performed.• If the authors answer NA or No, they should explain why their work has no societalimpact or why the paper does not address societal impact.• Examples of negative societal impacts include potential malicious or unintended uses(e.g., disinformation, generating fake profiles, surveillance), fairness considerations(e.g., deployment of technologies that could make decisions that unfairly impact specific groups), privacy considerations, and security considerations.• The conference expects that many papers will be foundational research and not tiedto particular applications, let alone deployments. However, if there is a direct path toany negative applications, the authors should point it out. For example, it is legitimateto point out that an improvement in the quality of generative models could be used togenerate deepfakes for disinformation. On the other hand, it is not needed to point outthat a generic algorithm for optimizing neural networks could enable people to trainmodels that generate Deepfakes faster.• The authors should consider possible harms that could arise when the technology isbeing used as intended and functioning correctly, harms that could arise when thetechnology is being used as intended but gives incorrect results, and harms followingfrom (intentional or unintentional) misuse of the technology.• If there are negative societal impacts, the authors could also discuss possible mitigationstrategies (e.g., gated release of models, providing defenses in addition to attacks,mechanisms for monitoring misuse, mechanisms to monitor how a system learns fromfeedback over time, improving the efficiency and accessibility of ML).11. SafeguardsQuestion: Does the paper describe safeguards that have been put in place for responsiblerelease of data or models that have a high risk for misuse (e.g., pretrained language models,image generators, or scraped datasets)?Answer: \[NA\]Justification:Guidelines:• The answer NA means that the paper poses no such risks.• Released models that have a high risk for misuse or dual-use should be releasedwith necessary safeguards to allow for controlled use of the model, for example byrequiring that users adhere to usage guidelines or restrictions to access the model orimplementing safety filters.• Datasets that have been scraped from the Internet could pose safety risks. The authorsshould describe how they avoided releasing unsafe images.• We recognize that providing effective safeguards is challenging, and many papers donot require this, but we encourage authors to take this into account and make a bestfaith effort.12. Licenses for existing assetsQuestion: Are the creators or original owners of assets (e.g., code, data, models), used inthe paper, properly credited and are the license and terms of use explicitly mentioned andproperly respected?Answer: \[NA\]Justification: See experiment section in main context and details in section C.5, C.3,C.4 and related work in appendix BGuidelines:• The answer NA means that the paper does not use existing assets.• The authors should cite the original paper that produced the code package or dataset.• The authors should state which version of the asset is used and, if possible, include aURL.• The name of the license (e.g., CC-BY 4.0) should be included for each asset.• For scraped data from a particular source (e.g., website), the copyright and terms ofservice of that source should be provided.• If assets are released, the license, copyright information, and terms of use in thepackage should be provided. For popular datasets, paperswithcode.com/datasetshas curated licenses for some datasets. Their licensing guide can help determine thelicense of a dataset.• For existing datasets that are re-packaged, both the original license and the license ofthe derived asset (if it has changed) should be provided.• If this information is not available online, the authors are encouraged to reach out tothe asset’s creators.13. New assetsQuestion: Are new assets introduced in the paper well documented and is the documentationprovided alongside the assets?Answer: \[NA\]Justification:Guidelines:• The answer NA means that the paper does not release new assets.• Researchers should communicate the details of the dataset/code/model as part of theirsubmissions via structured templates. This includes details about training, license,limitations, etc.• The paper should discuss whether and how consent was obtained from people whoseasset is used.• At submission time, remember to anonymize your assets (if applicable). You can eithercreate an anonymized URL or include an anonymized zip file.14. Crowdsourcing and research with human subjectsQuestion: For crowdsourcing experiments and research with human subjects, does the paperinclude the full text of instructions given to participants and screenshots, if applicable, aswell as details about compensation (if any)?Answer: \[NA\]Justification:Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should beincluded in the main paper.• According to the NeurIPS Code of Ethics, workers involved in data collection, curation,or other labor should be paid at least the minimum wage in the country of the datacollector.15. Institutional review board (IRB) approvals or equivalent for research with humansubjectsQuestion: Does the paper describe potential risks incurred by study participants, whethersuch risks were disclosed to the subjects, and whether Institutional Review Board (IRB)approvals (or an equivalent approval/review based on the requirements of your country orinstitution) were obtained?Answer: \[NA\]Justification:Guidelines:• The answer NA means that the paper does not involve crowdsourcing nor research withhuman subjects.• Depending on the country in which research is conducted, IRB approval (or equivalent)may be required for any human subjects research. If you obtained IRB approval, youshould clearly state this in the paper.• We recognize that the procedures for this may vary significantly between institutionsand locations, and we expect authors to adhere to the NeurIPS Code of Ethics and theguidelines for their institution.• For initial submissions, do not include any information that would break anonymity (ifapplicable), such as the institution conducting the review.16. Declaration of LLM usageQuestion: Does the paper describe the usage of LLMs if it is an important, original, ornon-standard component of the core methods in this research? Note that if the LLM is usedonly for writing, editing, or formatting purposes and does not impact the core methodology,scientific rigorousness, or originality of the research, declaration is not required.Answer: \[NA\]Justification:Guidelines:• The answer NA means that the core method development in this research does notinvolve LLMs as any important, original, or non-standard components.• Please refer to our LLM policy (https://neurips.cc/Conferences/2025/LLM)for what should or should not be described.
			-> WARNING: No results were found through the dblp search! | WARNING: No results were found through the dblp search!



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

![[Paper-Projekte/PQC/PAU - All  GPTZero NeurIPS Paper with H/27 A Unified Stability Analysis/ranking_results_fig.jpg]]

### References and Their Rankings

- International Conference on Learning Representations
	- Parsed as: 8th International Conference on Learning Representations
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 2
- International Conference on Learning Representations
	- Parsed as: 7th International Conference on Learning Representations
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 2
- Advances in Neural Information Processing Systems (was NIPS)
	- Parsed as: Advances in Neural Information Processing Systems (NeurIPS) 36
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 2
- Advances in Neural Information Processing Systems (was NIPS)
	- Parsed as: Advances in Neural Information Processing Systems (NeurIPS) 32
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- Advances in Neural Information Processing Systems (was NIPS)
	- Parsed as: Advances in Neural Information Processing Systems
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- International Conference on Learning Representations
	- Parsed as: Proceedings of the 12th International Conference on Learning Representations
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- JOURNAL OF MACHINE LEARNING RESEARCH
	- Parsed as: Journal of Machine Learning Research
	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = 5.0
	- References literatures count from this outlet: 1
- Advances in Neural Information Processing Systems (was NIPS)
	- Parsed as: Advances in Neural Information Processing Systems (NeurIPS) 33
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = B
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- International Conference on Machine Learning
	- Parsed as: 37th International Conference on Machine Learning
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- PROCEEDINGS OF THE NATIONAL ACADEMY OF SCIENCES OF THE UNITED STATES OF AMERICA
	- Parsed as: Proceedings of the National Academy of Sciences
	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = 8.9
	- References literatures count from this outlet: 1
- International Conference on Machine Learning
	- Parsed as: 38th International Conference on Machine Learning
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- International Conference on Learning Representations
	- Parsed as: 5th International Conference on Learning Representations
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- 34th International Conference on Machine Learning (ICML), volume 48
	- References literatures count from this outlet: 1
- NEURAL COMPUTATION
	- Parsed as: Neural Computation
	- [Journal Impact Factor](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/publishers/first-time-journal-citation-reports-inclusion-list-2025/) (without self cites) = 2.0
	- References literatures count from this outlet: 1
- Conference on Learning Theory
	- Parsed as: 31st Conference on Learning Theory
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- International Conference on Learning Representations
	- Parsed as: 9th International Conference on Learning Representations
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- Proceedings of the 34th International Conference on Machine Learning (ICML), volume 70
	- References literatures count from this outlet: 1
- International Conference on Learning Representations
	- Parsed as: International Conference on Learning Representations
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- Advances in Neural Information Processing Systems (was NIPS)
	- Parsed as: Why does sharpness-aware minimization generalize better than sgd? In Advances in Neural Information Processing Systems
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- Why does sharpness-aware minimization generalize better than sgd?
	- References literatures count from this outlet: 1
- arXiv
	- References literatures count from this outlet: 1
- Springer Science & Business Media
	- References literatures count from this outlet: 1
- International Conference on Machine Learning
	- Parsed as: Proceedings of the 34th International Conference on Machine Learning
	- [JQ Ranking](https://www.vhbonline.org/verband/wissenschaftliche-kommissionen/wirtschaftsinformatik/vhb-rating-2024-wirtschaftsinformatik) = A
	- [CORE Ranking](https://portal.core.edu.au/conf-ranks/?search=&by=all&source=ICORE2026&sort=arank&page=1) = A*
	- References literatures count from this outlet: 1
- The checklist should follow the references and follow the (optional) supplemental material The checklist does NOT count towards the page limit Please read the checklist guidelines carefully for information on how to answer these questions For each question in the checklist: • You should answer [Yes] , [No] , or [NA] • [NA] means either that the question is Not Applicable for that particular paper or the relevant information is Not Available • Please provide a short (1–2 sentence) justification right after your answer (even for NA) The checklist answers are an integral part of your paper submission They are visible to the reviewers, area chairs, senior area chairs, and ethics reviewers You will be asked to also include it (after eventual revisions) with the final version of your paper, and its final version will be published with the paper The reviewers of your paper will be asked to use the checklist as one of the factors in their evaluation While ”[Yes] ” is generally preferable to ”[No] ”, it is perfectly acceptable to answer ”[No] ” provided a proper justification is given (e g , ”error bars are not reported because it would be too computationally expensive” or ”we were unable to find the license for the dataset we used”) In general, answering ”[No] ” or ”[NA] ” is not grounds for rejection While the questions are phrased in a binary way, we acknowledge that the true answer is often more nuanced, so please just use your best judgment and write a justification to elaborate All supporting evidence can appear either in the main paper or the supplemental material, provided in appendix If you answer [Yes] to a question, in the justification please point to the section(s) where related material for the question can be found IMPORTANT, please: • Delete this instruction block, but keep the section heading “NeurIPS Paper Checklist”, • Keep the checklist subsection headings, questions/answers and guidelines below • Do not modify the questions and only use the provided macros for your answers Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: see main context and abstract Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations A No or NA answer to this question will not be perceived well by the reviewers • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes] Justification: See the limitation of the paper at the end Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper • The authors are encouraged to create a separate ”Limitations” section in their paper • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e g , independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally) The authors should reflect on how these assumptions might be violated in practice and what the implications would be • The authors should reflect on the scope of the claims made, e g , if the approach was only tested on a few datasets or with a few runs In general, empirical results often depend on implicit assumptions, which should be articulated • The authors should reflect on the factors that influence the performance of the approach For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community Reviewers will be specifically instructed to not penalize honesty concerning limitations Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: [Yes] Justification: See proof in appendix C 9, C 11, C 13, C 7 and theory section Guidelines: • The answer NA means that the paper does not include theoretical results • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced • All assumptions should be clearly stated or referenced in the statement of any theorems • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material • Theorems and Lemmas that the proof relies upon should be properly referenced Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: [Yes] Justification: See experiment section in main context and details in section C 5, C 3, C 4 Guidelines: • The answer NA means that the paper does not include experiments • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable • Depending on the contribution, reproducibility can be accomplished in various ways For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model In general releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e g , in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully (c) If the contribution is a new model (e g , a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e g , with an open-source dataset or instructions for how to construct the dataset) (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility In the case of closed-source models, it may be that access to the model is limited in some way (e g , to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results
	- References literatures count from this outlet: 1



---
## Extracted References

- **Number 1:**
	- Ref. ID: *Achour et al, 2024*
	- Authors: *E  M  Achour, F  Malgouyres, and S  Gerchinovitz*
	- Normalized Authors: `['Achour E.', 'Malgouyres F.', 'Gerchinovitz S.']`
	- Authors contain 'et al.': *False*
	- Title: *The loss landscape of deep linear neural networks: a second-order analysis.*
	- Year: *2024*
	- Outlet: **
	- Link: *https://arxiv.org/abs/2107.13289.*
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 2:**
	- Ref. ID: *Andriushchenko and Flammarion, 2022*
	- Authors: *M  Andriushchenko and N  Flammarion*
	- Normalized Authors: `['Andriushchenko M.', 'Flammarion N.']`
	- Authors contain 'et al.': *False*
	- Title: *Towards understanding sharpness-aware minimization.*
	- Year: *2022*
	- Outlet: **
	- Link: *https://arxiv.org/abs/2206.06232.*
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 3:**
	- Ref. ID: *Andriushchenko et al, 2023*
	- Authors: *M  Andriushchenko, D  Bahri, H  Mobahi, and N  Flammarion*
	- Normalized Authors: `['Andriushchenko M.', 'Bahri D.', 'Mobahi H.', 'Flammarion N.']`
	- Authors contain 'et al.': *False*
	- Title: *Sharpness-aware minimization leads to low-rank features*
	- Year: *2023*
	- Outlet: *Advances in Neural Information Processing Systems (NeurIPS) 36*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 4:**
	- Ref. ID: *Arpit et al, 2017*
	- Authors: *D  Arpit, S  Jastrzebski, N  Ballas, D  Krueger, E  Bengio, M  Kanwal, T  Maharaj, A  Fischer, A  Courville, Y  Bengio, et al*
	- Normalized Authors: `['Arpit D.', 'Jastrzebski S.', 'Ballas N.', 'Krueger D.', 'Bengio E.', 'Kanwal M.', 'Maharaj T.', 'Fischer A.', 'Courville A.', 'Bengio Y.']`
	- Authors contain 'et al.': *True*
	- Title: *A closer look at memorization in deep networks*
	- Year: *2017*
	- Outlet: *Proceedings of the 34th International Conference on Machine Learning*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 5:**
	- Ref. ID: *Bhatia, 2013*
	- Authors: *R  Bhatia*
	- Normalized Authors: `['Bhatia R.']`
	- Authors contain 'et al.': *False*
	- Title: *Matrix analysis, volume 169*
	- Year: *2013*
	- Outlet: *Springer Science & Business Media*
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: None of the 69 results matched the expected title!*
- **Number 6:**
	- Ref. ID: *Bisla et al, 2022*
	- Authors: *D  Bisla, J  Wang, and A  Choromanska*
	- Normalized Authors: `['Bisla D.', 'Wang J.', 'Choromanska A.']`
	- Authors contain 'et al.': *False*
	- Title: *Low-pass filtering sgd for recovering flat optima in the deep learning optimization landscape.*
	- Year: *2022*
	- Outlet: **
	- Link: *https://arxiv.org/abs/2201.08025.*
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 7:**
	- Ref. ID: *Chatterjee, 2020*
	- Authors: *S  Chatterjee*
	- Normalized Authors: `['Chatterjee S.']`
	- Authors contain 'et al.': *False*
	- Title: *Coherent gradients: An approach to understanding generalization in gradient descentbased optimization*
	- Year: *2020*
	- Outlet: *8th International Conference on Learning Representations*
	- Link: **
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 8:**
	- Ref. ID: *Chen and Flammarion, 2022*
	- Authors: *Z  Chen and N  Flammarion*
	- Normalized Authors: `['Chen Z.', 'Flammarion N.']`
	- Authors contain 'et al.': *False*
	- Title: *When and why sam generalizes better: An optimization perspective*
	- Year: *2022*
	- Outlet: *arXiv*
	- Link: **
	- **Valid?**: *WARNING: No results were found through the dblp search! | WARNING: No results were found through the dblp search!*
- **Number 9:**
	- Ref. ID: *Chen et al, 2023a*
	- Authors: *Z  Chen, J  Zhang, Y  Kou, X  Chen, C -J*
	- Normalized Authors: `['Chen Z.', 'Zhang J.', 'Kou Y.', 'Chen X.', '-J C.']`
	- Authors contain 'et al.': *False*
	- Title: *Hsieh, and Q  Gu*
	- Year: *2023*
	- Outlet: *Why does sharpness-aware minimization generalize better than sgd?*
	- Link: *https://arxiv.org/abs/2310.07269.*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 10:**
	- Ref. ID: *Chen et al, 2023b*
	- Authors: *Z  Chen, J  Zhang, Y  Kou, X  Chen, C -J*
	- Normalized Authors: `['Chen Z.', 'Zhang J.', 'Kou Y.', 'Chen X.', '-J C.']`
	- Authors contain 'et al.': *False*
	- Title: *Hsieh, and Q  Gu*
	- Year: *2023*
	- Outlet: *Why does sharpness-aware minimization generalize better than sgd? In Advances in Neural Information Processing Systems*
	- Link: *https://openreview.net/forum?id=3WAnGWLpSQ.*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 11:**
	- Ref. ID: *Dexter et al, 2024*
	- Authors: *G  Dexter, B  Ocejo, S  S  Keerthi, A  Gupta, A  Acharya, and R  Khanna*
	- Normalized Authors: `['Dexter G.', 'Ocejo B.', 'Keerthi S.', 'Gupta A.', 'Acharya A.', 'Khanna R.']`
	- Authors contain 'et al.': *False*
	- Title: *A precise characterization of sgd stability using loss surface geometry*
	- Year: *2024*
	- Outlet: *International Conference on Learning Representations*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 12:**
	- Ref. ID: *Dinh et al, 2017*
	- Authors: *L  Dinh, R  Pascanu, S  Bengio, and Y  Bengio*
	- Normalized Authors: `['Dinh L.', 'Pascanu R.', 'Bengio S.', 'Bengio Y.']`
	- Authors contain 'et al.': *False*
	- Title: *Sharp minima can generalize for deep nets*
	- Year: *2017*
	- Outlet: *Proceedings of the 34th International Conference on Machine Learning (ICML), volume 70*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 13:**
	- Ref. ID: *Du et al, 2022*
	- Authors: *J  Du, H  Yan, J  Feng, J  T  Zhou, L  Zhen, R  S  M  Goh, and V  Y  F  Tan*
	- Normalized Authors: `['Du J.', 'Yan H.', 'Feng J.', 'Zhou J.', 'Zhen L.', 'Goh R.', 'Tan V.']`
	- Authors contain 'et al.': *False*
	- Title: *Efficient sharpness-aware minimization for improved training of neural networks.*
	- Year: *2022*
	- Outlet: **
	- Link: *https://arxiv.org/abs/2110.03141.*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 14:**
	- Ref. ID: *Foret et al, 2021*
	- Authors: *P  Foret, A  Kleiner, H  Mobahi, and B  Neyshabur*
	- Normalized Authors: `['Foret P.', 'Kleiner A.', 'Mobahi H.', 'Neyshabur B.']`
	- Authors contain 'et al.': *False*
	- Title: *Sharpness-aware minimization for efficiently improving generalization*
	- Year: *2021*
	- Outlet: *9th International Conference on Learning Representations*
	- Link: **
	- **Valid?**: *CHECK - Year (2020) does not match expected year (2021)*
- **Number 15:**
	- Ref. ID: *Gunasekar et al, 2018*
	- Authors: *S  Gunasekar, B  Woodworth, S  Bhojanapalli, B  Neyshabur, and N  Srebro*
	- Normalized Authors: `['Gunasekar S.', 'Woodworth B.', 'Bhojanapalli S.', 'Neyshabur B.', 'Srebro N.']`
	- Authors contain 'et al.': *False*
	- Title: *Implicit regularization in matrix factorization*
	- Year: *2018*
	- Outlet: *31st Conference on Learning Theory*
	- Link: **
	- **Valid?**: *CHECK - Year (2017) does not match expected year (2018)*
- **Number 16:**
	- Ref. ID: *Hardt et al, 2016*
	- Authors: *M  Hardt, B  Recht, and Y  Singer*
	- Normalized Authors: `['Hardt M.', 'Recht B.', 'Singer Y.']`
	- Authors contain 'et al.': *False*
	- Title: *Train faster, generalize better: Stability of stochastic gradient descent*
	- Year: *2016*
	- Outlet: *34th International Conference on Machine Learning (ICML), volume 48*
	- Link: **
	- **Valid?**: *CHECK - Year (2015) does not match expected year (2016)*
- **Number 17:**
	- Ref. ID: *Hochreiter and Schmidhuber, 1997*
	- Authors: *S  Hochreiter and J  Schmidhuber*
	- Normalized Authors: `['Hochreiter S.', 'Schmidhuber J.']`
	- Authors contain 'et al.': *False*
	- Title: *Flat minima*
	- Year: *1997*
	- Outlet: *Neural Computation*
	- Link: **
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 18:**
	- Ref. ID: *Jiang et al, 2020*
	- Authors: *Y  Jiang, B  Neyshabur, H  Mobahi, D  Krishnan, and S  Bengio*
	- Normalized Authors: `['Jiang Y.', 'Neyshabur B.', 'Mobahi H.', 'Krishnan D.', 'Bengio S.']`
	- Authors contain 'et al.': *False*
	- Title: *Fantastic generalization measures and where to find them*
	- Year: *2020*
	- Outlet: *8th International Conference on Learning Representations*
	- Link: **
	- **Valid?**: *CHECK - Year (2019) does not match expected year (2020)*
- **Number 19:**
	- Ref. ID: *Kalimeris et al, 2019*
	- Authors: *D  Kalimeris, C  Caramanis, S  Sanghavi, C  Uhler, and A  Risteski*
	- Normalized Authors: `['Kalimeris D.', 'Caramanis C.', 'Sanghavi S.', 'Uhler C.', 'Risteski A.']`
	- Authors contain 'et al.': *False*
	- Title: *Sgd on neural networks learns functions of increasing complexity*
	- Year: *2019*
	- Outlet: *Advances in Neural Information Processing Systems (NeurIPS) 32*
	- Link: **
	- **Valid?**: *CHECK - Authors (Nakkiran, Kaplun, Yang, Edelman, Zhang, Barak) did not match found publication titled 'SGD on Neural Networks Learns Functions of Increasing Complexity'*
- **Number 20:**
	- Ref. ID: *Keskar et al, 2017*
	- Authors: *N  S  Keskar, D  Mudigere, J  Nocedal, P  Tak PT, Y  Smelyanskiy, and P  T  P  Tang*
	- Normalized Authors: `['Keskar N.', 'Mudigere D.', 'Nocedal J.', 'PT P.', 'Smelyanskiy Y.', 'Tang P.']`
	- Authors contain 'et al.': *False*
	- Title: *On large-batch training for deep learning: Generalization gap and sharp minima*
	- Year: *2017*
	- Outlet: *5th International Conference on Learning Representations*
	- Link: **
	- **Valid?**: *CHECK - Authors () did not match found publication titled 'On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima'*
- **Number 21:**
	- Ref. ID: *Khanna et al, 2018*
	- Authors: *R  Khanna, B  Kim, J  Ghosh, and O  Koyejo*
	- Normalized Authors: `['Khanna R.', 'Kim B.', 'Ghosh J.', 'Koyejo O.']`
	- Authors contain 'et al.': *False*
	- Title: *Interpreting black box predictions using fisher kernels.*
	- Year: *2018*
	- Outlet: **
	- Link: *https://arxiv.org/abs/1810.10118.*
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 22:**
	- Ref. ID: *Kwon et al, 2021*
	- Authors: *J  Kwon, S  Yoon, C  Kim, and S  J  Hwang*
	- Normalized Authors: `['Kwon J.', 'Yoon S.', 'Kim C.', 'Hwang S.']`
	- Authors contain 'et al.': *False*
	- Title: *Asam: Adaptive sharpness-aware minimization for scale-invariant learning of deep neural networks*
	- Year: *2021*
	- Outlet: *38th International Conference on Machine Learning*
	- Link: **
	- **Valid?**: *CHECK - Authors (Park, Choi) did not match found publication titled 'ASAM: Adaptive Sharpness-Aware Minimization for Scale-Invariant Learning of Deep Neural Networks'*
- **Number 23:**
	- Ref. ID: *Li et al, 2018*
	- Authors: *H  Li, Z  Xu, G  Taylor, C  Studer, and T  Goldstein*
	- Normalized Authors: `['Li H.', 'Xu Z.', 'Taylor G.', 'Studer C.', 'Goldstein T.']`
	- Authors contain 'et al.': *False*
	- Title: *Visualizing the loss landscape of neural nets.*
	- Year: *2018*
	- Outlet: **
	- Link: *https://arxiv.org/abs/1712.09913.*
	- **Valid?**: *CHECK - Authors (0022, 0002) did not match found publication titled 'Visualizing the Loss Landscape of Neural Nets.'*
- **Number 24:**
	- Ref. ID: *Lyu and Li, 2019*
	- Authors: *K  Lyu and J  Li*
	- Normalized Authors: `['Lyu K.', 'Li J.']`
	- Authors contain 'et al.': *False*
	- Title: *Gradient descent maximizes the margin of homogeneous neural networks*
	- Year: *2019*
	- Outlet: *7th International Conference on Learning Representations*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 25:**
	- Ref. ID: *Ma and Ying, 2021*
	- Authors: *C  Ma and L  Ying*
	- Normalized Authors: `['Ma C.', 'Ying L.']`
	- Authors contain 'et al.': *False*
	- Title: *On linear stability of sgd and input-smoothness of neural networks.*
	- Year: *2021*
	- Outlet: **
	- Link: *https://arxiv.org/abs/2105.13462.*
	- **Valid?**: *CHECK - Authors (0012) did not match found publication titled 'On Linear Stability of SGD and Input-Smoothness of Neural Networks.'*
- **Number 26:**
	- Ref. ID: *Morwani et al, 2023*
	- Authors: *D  Morwani, J  Batra, P  Jain, and P  Netrapalli*
	- Normalized Authors: `['Morwani D.', 'Batra J.', 'Jain P.', 'Netrapalli P.']`
	- Authors contain 'et al.': *False*
	- Title: *Simplicity bias in 1-hidden layer neural networks*
	- Year: *2023*
	- Outlet: *Advances in Neural Information Processing Systems (NeurIPS) 36*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 27:**
	- Ref. ID: *Papyan et al, 2020*
	- Authors: *V  Papyan, X  Han, and D  L  Donoho*
	- Normalized Authors: `['Papyan V.', 'Han X.', 'Donoho D.']`
	- Authors contain 'et al.': *False*
	- Title: *Prevalence of neural collapse during the terminal phase of deep learning training*
	- Year: *2020*
	- Outlet: *Proceedings of the National Academy of Sciences*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 28:**
	- Ref. ID: *Sankararaman et al, 2020*
	- Authors: *K  A  Sankararaman, S  Sankararaman, H  Pandey, S  Ganguli, and F  Bromberg*
	- Normalized Authors: `['Sankararaman K.', 'Sankararaman S.', 'Pandey H.', 'Ganguli S.', 'Bromberg F.']`
	- Authors contain 'et al.': *False*
	- Title: *The impact of neural network overparameterization on gradient confusion and stochastic gradient descent*
	- Year: *2020*
	- Outlet: *37th International Conference on Machine Learning*
	- Link: **
	- **Valid?**: *CHECK - Authors (Xu, Huang, Goldstein) did not match found publication titled 'The Impact of Neural Network Overparameterization on Gradient Confusion and Stochastic Gradient Descent'*
- **Number 29:**
	- Ref. ID: *Shah et al, 2020*
	- Authors: *H  Shah, K  Tamuly, A  Raghunathan, P  Jain, and P  Netrapalli*
	- Normalized Authors: `['Shah H.', 'Tamuly K.', 'Raghunathan A.', 'Jain P.', 'Netrapalli P.']`
	- Authors contain 'et al.': *False*
	- Title: *The pitfalls of simplicity bias in neural networks*
	- Year: *2020*
	- Outlet: *Advances in Neural Information Processing Systems (NeurIPS) 33*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 30:**
	- Ref. ID: *Soudry et al, 2018*
	- Authors: *D  Soudry, E  Hoffer, M  Nacson, S  Gunasekar, and N  Srebro*
	- Normalized Authors: `['Soudry D.', 'Hoffer E.', 'Nacson M.', 'Gunasekar S.', 'Srebro N.']`
	- Authors contain 'et al.': *False*
	- Title: *The implicit bias of gradient descent on separable data*
	- Year: *2018*
	- Outlet: *Journal of Machine Learning Research*
	- Link: **
	- **Valid?**: *CHECK - Authors () did not match found publication titled 'The Implicit Bias of Gradient Descent on Separable Data'*
- **Number 31:**
	- Ref. ID: *Springer et al, 2024*
	- Authors: *J  M  Springer, V  Nagarajan, and A  Raghunathan*
	- Normalized Authors: `['Springer J.', 'Nagarajan V.', 'Raghunathan A.']`
	- Authors contain 'et al.': *False*
	- Title: *Sharpness-aware minimization enhances feature quality via balanced learning*
	- Year: *2024*
	- Outlet: *Proceedings of the 12th International Conference on Learning Representations*
	- Link: *https://openreview.net/forum?id=3xDaj4pRna.*
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 32:**
	- Ref. ID: *Valle-Pérez et al, 2019*
	- Authors: *G  Valle-Pérez, C  Q  Camargo, and A  A  Louis*
	- Normalized Authors: `['Valle-Pérez G.', 'Camargo C.', 'Louis A.']`
	- Authors contain 'et al.': *False*
	- Title: *Deep learning generalizes because the parameterfunction map is biased towards simple functions*
	- Year: *2019*
	- Outlet: *7th International Conference on Learning Representations*
	- Link: **
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 33:**
	- Ref. ID: *Wen et al, 2023a*
	- Authors: *K  Wen, Z  Li, and T  Ma*
	- Normalized Authors: `['Wen K.', 'Li Z.', 'Ma T.']`
	- Authors contain 'et al.': *False*
	- Title: *Sharpness minimization algorithms do not only minimize sharpness to achieve better generalization.*
	- Year: *2023*
	- Outlet: **
	- Link: *https://arxiv.org/abs/2307.11007.*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 34:**
	- Ref. ID: *Wen et al, 2023b*
	- Authors: *K  Wen, T  Ma, and Z  Li*
	- Normalized Authors: `['Wen K.', 'Ma T.', 'Li Z.']`
	- Authors contain 'et al.': *False*
	- Title: *How does sharpness-aware minimization minimize sharpness?.*
	- Year: *2023*
	- Outlet: **
	- Link: *https://arxiv.org/abs/2211.05729.*
	- **Valid?**: *WARNING: None of the 10 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 35:**
	- Ref. ID: *Wu and Su, 2023*
	- Authors: *L  Wu and W  J  Su*
	- Normalized Authors: `['Wu L.', 'Su W.']`
	- Authors contain 'et al.': *False*
	- Title: *The implicit regularization of dynamical stability in stochastic gradient descent.*
	- Year: *2023*
	- Outlet: **
	- Link: *https://arxiv.org/abs/2305.17490.*
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 36:**
	- Ref. ID: *Wu and Ma, 2018*
	- Authors: *L  Wu, C  Ma, et al*
	- Normalized Authors: `['Wu L.', 'Ma C.']`
	- Authors contain 'et al.': *True*
	- Title: *How sgd selects the global minima in over-parameterized learning: A dynamical stability perspective*
	- Year: *2018*
	- Outlet: *Advances in Neural Information Processing Systems*
	- Link: **
	- **Valid?**: *Found: Years matched; reference checks out :)*
- **Number 37:**
	- Ref. ID: *Wu et al, 2022*
	- Authors: *L  Wu, M  Wang, and W  Su*
	- Normalized Authors: `['Wu L.', 'Wang M.', 'Su W.']`
	- Authors contain 'et al.': *False*
	- Title: *The alignment property of sgd noise and how it helps select flat minima: A stability analysis.*
	- Year: *2022*
	- Outlet: **
	- Link: *https://arxiv.org/abs/2207.02628.*
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 38:**
	- Ref. ID: *Zhang et al, 2024*
	- Authors: *Y  Zhang, H  He, J  Zhu, H  Chen, Y  Wang, and Z  Wei*
	- Normalized Authors: `['Zhang Y.', 'He H.', 'Zhu J.', 'Chen H.', 'Wang Y.', 'Wei Z.']`
	- Authors contain 'et al.': *False*
	- Title: *On the duality between sharpness-aware minimization and adversarial training.*
	- Year: *2024*
	- Outlet: **
	- Link: *https://arxiv.org/abs/2402.15152.*
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 39:**
	- Ref. ID: *Zhou et al, 2025*
	- Authors: *Z  Zhou, M  Wang, Y  Mao, B  Li, and J  Yan*
	- Normalized Authors: `['Zhou Z.', 'Wang M.', 'Mao Y.', 'Li B.', 'Yan J.']`
	- Authors contain 'et al.': *False*
	- Title: *Sharpness-aware minimization efficiently selects flatter minima late in training.*
	- Year: *2025*
	- Outlet: **
	- Link: *https://arxiv.org/abs/2410.10373.*
	- **Valid?**: *WARNING: None of the 1 results matched the expected title! | WARNING: No results were found through the dblp search!*
- **Number 40:**
	- Ref. ID: *research et al, 0*
	- Authors: *NeurIPS Paper Checklist The checklist is designed to encourage best practices for responsible machine learning research, addressing issues of reproducibility, transparency, research ethics, and societal impact*
	- Normalized Authors: `['research N.', 'reproducibility a.', 'transparency', 'ethics r.', 'impact s.']`
	- Authors contain 'et al.': *False*
	- Title: *Do not remove the checklist: The papers not including the checklist will be desk rejected*
	- Year: *0*
	- Outlet: *The checklist should follow the references and follow the (optional) supplemental material The checklist does NOT count towards the page limit Please read the checklist guidelines carefully for information on how to answer these questions For each question in the checklist: • You should answer [Yes] , [No] , or [NA] • [NA] means either that the question is Not Applicable for that particular paper or the relevant information is Not Available • Please provide a short (1–2 sentence) justification right after your answer (even for NA) The checklist answers are an integral part of your paper submission They are visible to the reviewers, area chairs, senior area chairs, and ethics reviewers You will be asked to also include it (after eventual revisions) with the final version of your paper, and its final version will be published with the paper The reviewers of your paper will be asked to use the checklist as one of the factors in their evaluation While ”[Yes] ” is generally preferable to ”[No] ”, it is perfectly acceptable to answer ”[No] ” provided a proper justification is given (e g , ”error bars are not reported because it would be too computationally expensive” or ”we were unable to find the license for the dataset we used”) In general, answering ”[No] ” or ”[NA] ” is not grounds for rejection While the questions are phrased in a binary way, we acknowledge that the true answer is often more nuanced, so please just use your best judgment and write a justification to elaborate All supporting evidence can appear either in the main paper or the supplemental material, provided in appendix If you answer [Yes] to a question, in the justification please point to the section(s) where related material for the question can be found IMPORTANT, please: • Delete this instruction block, but keep the section heading “NeurIPS Paper Checklist”, • Keep the checklist subsection headings, questions/answers and guidelines below • Do not modify the questions and only use the provided macros for your answers Claims Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes] Justification: see main context and abstract Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations A No or NA answer to this question will not be perceived well by the reviewers • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper Limitations Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes] Justification: See the limitation of the paper at the end Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper • The authors are encouraged to create a separate ”Limitations” section in their paper • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e g , independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally) The authors should reflect on how these assumptions might be violated in practice and what the implications would be • The authors should reflect on the scope of the claims made, e g , if the approach was only tested on a few datasets or with a few runs In general, empirical results often depend on implicit assumptions, which should be articulated • The authors should reflect on the factors that influence the performance of the approach For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community Reviewers will be specifically instructed to not penalize honesty concerning limitations Theory assumptions and proofs Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: [Yes] Justification: See proof in appendix C 9, C 11, C 13, C 7 and theory section Guidelines: • The answer NA means that the paper does not include theoretical results • All the theorems, formulas, and proofs in the paper should be numbered and crossreferenced • All assumptions should be clearly stated or referenced in the statement of any theorems • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material • Theorems and Lemmas that the proof relies upon should be properly referenced Experimental result reproducibility Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: [Yes] Justification: See experiment section in main context and details in section C 5, C 3, C 4 Guidelines: • The answer NA means that the paper does not include experiments • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable • Depending on the contribution, reproducibility can be accomplished in various ways For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model In general releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e g , in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully (c) If the contribution is a new model (e g , a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e g , with an open-source dataset or instructions for how to construct the dataset) (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility In the case of closed-source models, it may be that access to the model is limited in some way (e g , to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results Open access to data and code Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results*
	- Link: *https://nips.cc/public/guides/CodeSubmissionPolicy)*
	- **Valid?**: *WARNING: No results were found through the dblp search! | WARNING: No results were found through the dblp search!*



---
## Full List of Reference Support Check

**Sentences with references to papers that are thematically related / relevant papers but REFUTE the statement they are referenced in:**
- None

**Sentences with references to papers that are thematically related / relevant papers that we had not enough info about to determine the stance on the statement they are referenced in:**
- '*In particular, why should an algorithm like SGD prefer flat minima or feature-simple solutions in the first place? And how do modifications to the optimizer - such as adding random noise or using Sharpness-Aware Minimization (SAM) [Foret et al, 2021] - alter these preferences? Intriguingly, recent empirical evidence further suggests that even among multiple minima of equal overall flatness, SAM can exhibit an additional implicit bias favoring those solutions that generalize better [Andriushchenko 39th Conference on Neural Information Processing Systems (NeurIPS 2025)*'
	- This flag is for the paper with Ref. ID = Foret et al, 2021
- '*This theoretical insight aligns well with SAM’s design goal of seeking flat minima [Foret et al, 2021], but it goes further by pinpointing which sharp minima are especially disfavored: namely, those where the sharpness arises from directions that are not supported uniformly by all training examples*'
	- This flag is for the paper with Ref. ID = Foret et al, 2021

**Sentences with references to papers that are thematically related / relevant papers that SUPPORT the statement they are referenced in:**
- '*Recent algorithms like Sharpness-Aware Minimization (SAM) explicitly optimize for flatness and further improve generalization [Foret et al, 2021]*'
	- This flag is for the paper with Ref. ID = Foret et al, 2021
- '*wide, low-curvature regions of the loss) which correlate with better generalization [Keskar et al, 2017, Hochreiter and Schmidhuber, 1997]*'
	- This flag is for the paper with Ref. ID = Keskar et al, 2017


**Sentences with references to papers that seem thematically unrelated / irrelevant:**
- None


**Sentences with references to papers that we didn't have an abstract for to check against:**
- '*To facilitate tractable analysis, we follow prior works [Andriushchenko and Flammarion, 2022, Du et al, 2022, Zhou et al, 2025] and replace this quantity by a fixed scalar value α*'
	- This flag is for the paper with Ref. ID = Andriushchenko and Flammarion, 2022
- '*We articulate this connection rigorously and in doing so, also suggest that interventions like SAM, which further insist on flatness, are effectively heightening the simplicity bias – an interpretation consistent with recent findings that SAM-trained models prefer more parsimonious representations [Andriushchenko et al, 2023], can enlarge the regime of benign overfitting when compared to SGD [Chen et al, 2023b] and can empirically choose better generalizing minima even there are multiple minima with the same flatness [Wen et al, 2023a]*'
	- This flag is for the paper with Ref. ID = Andriushchenko et al, 2023
- '*This aligns with recent empirical observations that SAM leads to simpler or more generalizable representations in deep models [Andriushchenko et al, 2023, Wen et al, 2023a, Springer et al, 2024]*'
	- This flag is for the paper with Ref. ID = Andriushchenko et al, 2023
- '*Empirical evidence shows that neural networks often learn the most predictive yet simplest patterns in the data first, and may entirely ignore more complex features if the simple ones already suffice [Arpit et al, 2017, Shah et al, 2020]*'
	- This flag is for the paper with Ref. ID = Arpit et al, 2017
- '*1 SGD under Random Perturbation To better understand how optimization algorithms behave near critical points, we begin by analyzing a simple but illustrative baseline: random perturbation-based SGD [Bisla et al, 2022]*'
	- This flag is for the paper with Ref. ID = Bisla et al, 2022
- '*We articulate this connection rigorously and in doing so, also suggest that interventions like SAM, which further insist on flatness, are effectively heightening the simplicity bias – an interpretation consistent with recent findings that SAM-trained models prefer more parsimonious representations [Andriushchenko et al, 2023], can enlarge the regime of benign overfitting when compared to SGD [Chen et al, 2023b] and can empirically choose better generalizing minima even there are multiple minima with the same flatness [Wen et al, 2023a]*'
	- This flag is for the paper with Ref. ID = Chen et al, 2023b
- '*Crucially, we focus on a notion of data coherence [Dexter et al, 2024] that captures how similar or aligned the contributions of different training examples are to the local curvature of the loss*'
	- This flag is for the paper with Ref. ID = Dexter et al, 2024
- '*This framework has been used to study convergence properties of SGD and its variants and has recently emerged as a useful tool to characterize generalization-relevant behavior such as the ability to escape sharp minima [Wu et al, 2018, Dexter et al, 2024]*'
	- This flag is for the paper with Ref. ID = Dexter et al, 2024
- '*Coherence measure [Dexter et al, 2024]*'
	- This flag is for the paper with Ref. ID = Dexter et al, 2024
- '*We find that the divergence threshold for instability remains unchanged from standard SGD as derived by Dexter et al [2024] (part 1), implying that adding random noise does not alter which minima are stable*'
	- This flag is for the paper with Ref. ID = Dexter et al, 2024
- '*11 for dependency of δ) combining with Theorem for the SGD bounds [Dexter et al, 2024], this implies that simpler (low-C) generalizing solutions are more stable under SGD, even when all candidate solutions lie in equally flat regions of the loss*'
	- This flag is for the paper with Ref. ID = Dexter et al, 2024
- '*To facilitate tractable analysis, we follow prior works [Andriushchenko and Flammarion, 2022, Du et al, 2022, Zhou et al, 2025] and replace this quantity by a fixed scalar value α*'
	- This flag is for the paper with Ref. ID = Du et al, 2022
- '*wide, low-curvature regions of the loss) which correlate with better generalization [Keskar et al, 2017, Hochreiter and Schmidhuber, 1997]*'
	- This flag is for the paper with Ref. ID = Hochreiter and Schmidhuber, 1997
- '*Empirical evidence shows that neural networks often learn the most predictive yet simplest patterns in the data first, and may entirely ignore more complex features if the simple ones already suffice [Arpit et al, 2017, Shah et al, 2020]*'
	- This flag is for the paper with Ref. ID = Shah et al, 2020
- '*This aligns with recent empirical observations that SAM leads to simpler or more generalizable representations in deep models [Andriushchenko et al, 2023, Wen et al, 2023a, Springer et al, 2024]*'
	- This flag is for the paper with Ref. ID = Springer et al, 2024
- '*We articulate this connection rigorously and in doing so, also suggest that interventions like SAM, which further insist on flatness, are effectively heightening the simplicity bias – an interpretation consistent with recent findings that SAM-trained models prefer more parsimonious representations [Andriushchenko et al, 2023], can enlarge the regime of benign overfitting when compared to SGD [Chen et al, 2023b] and can empirically choose better generalizing minima even there are multiple minima with the same flatness [Wen et al, 2023a]*'
	- This flag is for the paper with Ref. ID = Wen et al, 2023a
- '*This aligns with recent empirical observations that SAM leads to simpler or more generalizable representations in deep models [Andriushchenko et al, 2023, Wen et al, 2023a, Springer et al, 2024]*'
	- This flag is for the paper with Ref. ID = Wen et al, 2023a
- '*We adopt a synthetic data distribution from prior work [Wen et al, 2023a] where inputs x ∈{−1, 1}d are drawn i*'
	- This flag is for the paper with Ref. ID = Wen et al, 2023a
- '*We begin by characterizing memorization in our setup – a data point is memorized if it activates a unique hidden neuron [Wen et al, 2023a]*'
	- This flag is for the paper with Ref. ID = Wen et al, 2023a
- '*To facilitate tractable analysis, we follow prior works [Andriushchenko and Flammarion, 2022, Du et al, 2022, Zhou et al, 2025] and replace this quantity by a fixed scalar value α*'
	- This flag is for the paper with Ref. ID = Zhou et al, 2025

