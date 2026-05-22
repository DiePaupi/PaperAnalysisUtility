
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\43 Learning Grouped Lattice Vector Quantizers\Learning Grouped Lattice Vector Quantizers for Low-Bit LLM Compression.pdf"
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
- Found following heading '2 - Background and Related Work' on page 3
- Found following heading '3 - Method' on page 4
- Found following heading '4 - Experiments' on page 7
- Found following heading '5 - Conclusion' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - A Brief Theoretical Derivation of Babai Rounding’s Error Bound' on page 15
- Found following appendix 'B - Storage Overhead Analysis' on page 17
- Found following appendix 'C - Broader Impact' on page 17
- Found following appendix 'D - Ablation Study of Bit Allocation' on page 18
- Found following appendix 'E - Ablation Study of Group-Specific Lattice Quantization' on page 18
- Found following appendix 'F - Ablation Study of Group-Specific Companding' on page 18
- Found following appendix 'G - Ablation Study of Group Size' on page 19
- Found following appendix 'H - Ablation Study of Calibration Dataset Size' on page 19
- Found following appendix 'I - Babai Rounding vs. Greedy Coordinate Descent (GCD)' on page 20
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 15
All found references: 64
-> Warning: Malformed author string: '1988'
-> Warning: Malformed author string: 'NVIDIA'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ... link  valid
0       1  Pulse code modulation (PCM) of voice frequenci...  ...        None
1       2                                       László Babai  ...        None
2       3  Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Ka...  ...        None
3       4  Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda ...  ...        None
4       5  Rocco Banner, Elad Hoffer, Itay Hubara, and Ra...  ...        None
..    ...                                                ...  ...  ...    ...
59     60                   Hao Xu, Xiaolin Wu, and Xi Zhang  ...        None
60     61  Zhewei Yao, Reza Yazdani Aminabadi, Minjia Zha...  ...        None
61     62                            Xi Zhang and Xiaolin Wu  ...        None
62     63                            Xi Zhang and Xiaolin Wu  ...        None
63     64                            Xi Zhang and Xiaolin Wu  ...        None

[64 rows x 10 columns]
- Checking reference 1/64:
  -> INFO: Now checking 1 results for matching title: 'Recommendation ITU-T G 711, originally approved in.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['frequencies', '1988', '1972']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Recommendation+ITU-T+G+711%2C+originally+approved+in. manually and check the results.
        -> Author(s): Pulse code modulation (PCM) of voice frequencies, 1988
        -> Title:     Recommendation ITU-T G 711, originally approved in.
        -> Year:      1972
     -> Manual search was skipped by the user.
- Checking reference 2/64:
  -> INFO: Now checking 2 results for matching title: 'On Lovász’ lattice reduction and the nearest lattice point problem'
       -> INFO: All authors matched!
- Checking reference 3/64:
  -> INFO: Now checking 10 results for matching title: 'Qwen technical report'
       -> WARNING: Not all 50 authors from the found ref. were matched (only 17)
                   Unmatched authors = 'Hui, Li, Lin, Lin, Liu, Liu, Lu, Lu, Ma, Men, Ren, Ren, Tan, Tan, Tu, Wang, Wang, Wang, Wu, Xu, Xu, Yao, Bowen, Yuan, Yuan, Zhang, Zhang, Zhang, Zhang, Zhou, Zhou, Zhou, Zhu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/64:
  -> INFO: Now checking 2 results for matching title: 'Training a helpful and harmless assistant with reinforcement learning from human feedback'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 5/64:
  -> INFO: Now checking 10 results for matching title: 'Post-training quantization for deep neural networks'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Banner', 'Hoffer', 'Hubara', 'El-Yaniv', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Post-training+quantization+for+deep+neural+networks manually and check the results.
        -> Author(s): Rocco Banner, Elad Hoffer, Itay Hubara, and Rami El-Yaniv
        -> Title:     Post-training quantization for deep neural networks
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 6/64:
  -> INFO: Now checking 10 results for matching title: 'Language models are few-shot learners'
       -> WARNING: Not all 31 authors from the found ref. were matched (only 7)
                   Unmatched authors = 'Shyam, Sastry, Askell, Agarwal, Herbert-Voss, Krueger, Henighan, Child, Ramesh, Ziegler, Wu, Winter, Hesse, Chen, Sigler, Litwin, Gray, Chess, Clark, Berner, McCandlish, Radford, Sutskever, Amodei'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/64:
  -> INFO: Now checking 3 results for matching title: 'Quip: 2-bit quantization of large language models with guarantees'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/64:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Redpajama: An open source recipe to reproduce llama training dataset, April.
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 923 results for matching title: 'Redpajama: An open source recipe to reproduce llama training dataset, April.'
  -> WARNING: None of the 923 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Redpajama:+An+open+source+recipe+to+reproduce+llama+training+dataset%2C+April. manually and check the results.
        -> Author(s): Together Computer
        -> Title:     Redpajama: An open source recipe to reproduce llama training dataset, April.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 9/64:
  -> INFO: Now checking 10 results for matching title: 'Sphere-packings, lattices, and groups.'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Conway', 'Sloane', 'Bannai', '1987']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Sphere-packings%2C+lattices%2C+and+groups. manually and check the results.
        -> Author(s): JH Conway, NJA Sloane, and E Bannai
        -> Title:     Sphere-packings, lattices, and groups.
        -> Year:      1987
     -> Manual search was skipped by the user.
- Checking reference 10/64:
  -> INFO: Now checking 10 results for matching title: 'Gpt3'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Dettmers', 'Lewis', 'Belkada', 'Zettlemoyer', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gpt3 manually and check the results.
        -> Author(s): Tim Dettmers, Mike Lewis, Younes Belkada, and Luke Zettlemoyer
        -> Title:     Gpt3
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 11/64:
  -> INFO: Now checking 1 results for matching title: 'Spqr: A sparse-quantized representation for near-lossless llm weight compression'
       -> INFO: All authors matched!
- Checking reference 12/64:
  -> INFO: Now checking 8 results for matching title: 'The case for 4-bit precision: k-bit inference scaling laws'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/64:
  -> INFO: Now checking 10 results for matching title: 'Bert: Pre-training of deep bidirectional transformers for language understanding'
       -> INFO: All authors matched!
- Checking reference 14/64:
  -> INFO: Now checking 10 results for matching title: 'Cbq: Cross-block quantization for large language models'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 15/64:
  -> INFO: Now checking 10 results for matching title: 'Extreme compression of large language models via additive quantization'
       -> INFO: All authors matched!
- Checking reference 16/64:
  -> INFO: Now checking 1 results for matching title: 'Achieving 1/2 log (1 + snr) on the awgn channel with lattice encoding and decoding'
       -> INFO: All authors matched!
- Checking reference 17/64:
  -> INFO: Now checking 10 results for matching title: 'Serl: Self-play reinforcement learning for large language models with limited data'
       -> INFO: All authors matched!
- Checking reference 18/64:
  -> INFO: Now checking 1 results for matching title: 'Optimal brain compression: A framework for accurate posttraining quantization and pruning'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Frantar', 'Alistarh', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Optimal+brain+compression:+A+framework+for+accurate+posttraining+quantization+and+pruning manually and check the results.
        -> Author(s): Elias Frantar and Dan Alistarh
        -> Title:     Optimal brain compression: A framework for accurate posttraining quantization and pruning
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 19/64:
  -> INFO: Now checking 1 results for matching title: 'Gptq: Accurate post-training quantization for generative pre-trained transformers'
       -> INFO: All authors matched!
- Checking reference 20/64:
  -> INFO: Now checking 4 results for matching title: 'A survey of quantization methods for efficient neural network inference'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 21/64:
  -> INFO: Now checking 10 results for matching title: 'Lattice quantization'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Gibson', 'Sayood', '1988']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Lattice+quantization manually and check the results.
        -> Author(s): Jerry D Gibson and Khalid Sayood
        -> Title:     Lattice quantization
        -> Year:      1988
     -> Manual search was skipped by the user.
- Checking reference 22/64:
  -> INFO: Now checking 2 results for matching title: 'A survey of low-bit large language models: Basics, systems, and algorithms'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 11)
                   Unmatched authors = 'Yong, Lin'
       -> INFO: All authors matched!
- Checking reference 23/64:
  -> INFO: Now checking 10 results for matching title: 'Vector quantization'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (1984)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 24/64:
  -> INFO: Now checking 3 results for matching title: 'An Introduction to Analog and Digital Communications'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Haykin', '1994']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=An+Introduction+to+Analog+and+Digital+Communications manually and check the results.
        -> Author(s): Simon Haykin
        -> Title:     An Introduction to Analog and Digital Communications
        -> Year:      1994
     -> Manual search was skipped by the user.
- Checking reference 25/64:
  -> INFO: Now checking 10 results for matching title: 'Slim-llm: Salience-driven mixed-precision quantization for large language models'
       -> INFO: All authors matched!
- Checking reference 26/64:
  -> INFO: Now checking 10 results for matching title: 'Quantizing deep convolutional networks for efficient inference: A whitepaper'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hubara', 'Courbariaux', 'Soudry', 'El-Yaniv', 'Bengio', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Quantizing+deep+convolutional+networks+for+efficient+inference:+A+whitepaper manually and check the results.
        -> Author(s): Itay Hubara, Matthieu Courbariaux, Daniel Soudry, Rami El-Yaniv, and Yoshua Bengio
        -> Title:     Quantizing deep convolutional networks for efficient inference: A whitepaper
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 27/64:
  -> INFO: Now checking 10 results for matching title: 'Accurate post training quantization with small calibration sets'
       -> INFO: All authors matched!
- Checking reference 28/64:
  -> INFO: Now checking 1 results for matching title: 'A unified formulation of segment companding laws and synthesis of codecs and digital compandors'
       -> INFO: All authors matched!
- Checking reference 29/64:
  -> INFO: Now checking 1 results for matching title: 'Ll-vq-vae: Learnable lattice vector-quantization for efficient representations'
       -> INFO: All authors matched!
- Checking reference 30/64:
  -> INFO: Now checking 1 results for matching title: 'Squeezellm: Dense-and-sparse quantization'
       -> INFO: All authors matched!
- Checking reference 31/64:
  -> INFO: Now checking 1 results for matching title: 'Brecq: Pushing the limit of post-training quantization by block reconstruction'
       -> INFO: All authors matched!
- Checking reference 32/64:
  -> INFO: Now checking 3 results for matching title: 'Awq: Activation-aware weight quantization for on-device llm compression and acceleration'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 6)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/64:
  -> INFO: Now checking 10 results for matching title: 'Transformer-vq: Linear-time transformers via vector quantization'
       -> INFO: All authors matched!
- Checking reference 34/64:
  -> INFO: Now checking 10 results for matching title: 'Deepseek-v3 technical report'
       -> WARNING: Not all 198 authors from the found ref. were matched (only 103)
                   Unmatched authors = 'DeepSeek-AI, Dai, Guo, Yang, Ji, Lin, Dai, Luo, Bao, Ding, Gao, Qu, Cai, Liang, Guo, Ni, Yuan, Qiu, Song, Dong, Hu, Gao, Guan, Huang, Xia, Tang, Tian, Huang, Zhu, Du, Jin, Ge, Pan, Zhou, Ye, Ma, Zhou, Zhou, Pan, Yun, Pei, Sun, Xiao, Zeng, Liang, Gao, Jin, Shen, Nie, Sun, Xie, Song, Shan, Zhou, Yang, Su, Lin, Wei, Zhu, Huang, Sun, Zheng, Shi, Xiong, Tang, Piao, Tan, Ma, Guo, Ou, Zhu, Gong, Zou, Xiong, Ma, Yan, Luo, You, Zhou, Ren, Ren, Sha, Fu, Huang, Xie, Gou, Ma, Yan, Shao, Gu, Zhu, Xie, Song, Gao, Pan'
       -> WARNING: Not all 198 authors from the found ref. were matched (only 103)
                   Unmatched authors = 'DeepSeek-AI, Dai, Guo, Yang, Ji, Lin, Dai, Luo, Bao, Ding, Gao, Qu, Cai, Liang, Guo, Ni, Yuan, Qiu, Song, Dong, Hu, Gao, Guan, Huang, Xia, Tang, Tian, Huang, Zhu, Du, Jin, Ge, Pan, Zhou, Ye, Ma, Zhou, Zhou, Pan, Yun, Pei, Sun, Xiao, Zeng, Liang, Gao, Jin, Shen, Nie, Sun, Xie, Song, Shan, Zhou, Yang, Su, Lin, Wei, Zhu, Huang, Sun, Zheng, Shi, Xiong, Tang, Piao, Tan, Ma, Guo, Ou, Zhu, Gong, Zou, Xiong, Ma, Yan, Luo, You, Zhou, Ren, Ren, Sha, Fu, Huang, Xie, Gou, Ma, Yan, Shao, Gu, Zhu, Xie, Song, Gao, Pan'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 35/64:
  -> INFO: Now checking 10 results for matching title: 'A survey of direct preference optimization'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 12)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 36/64:
  -> INFO: Now checking 10 results for matching title: 'Verigui: Verifiable long-chain gui dataset'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Liu', 'Liu', 'Zhou', 'Cui', 'Zhou', 'Zhou', 'Fan', 'Zhang', 'Shi', 'Xuan', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Verigui:+Verifiable+long-chain+gui+dataset manually and check the results.
        -> Author(s): Shunyu Liu, Minghao Liu, Huichi Zhou, Zhenyu Cui, Yang Zhou, Yuhao Zhou, Wendong Fan, Ge Zhang, Jiajun Shi, Weihao Xuan, et al
        -> Title:     Verigui: Verifiable long-chain gui dataset
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 37/64:
  -> INFO: Now checking 1 results for matching title: 'Pv-tuning: Beyond straight-through estimation for extreme llm compression'
       -> INFO: All authors matched!
- Checking reference 38/64:
  -> INFO: Now checking 10 results for matching title: 'Pointer sentinel mixture models.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Merity', 'Xiong', 'Bradbury', 'Socher', '2016']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Pointer+sentinel+mixture+models. manually and check the results.
        -> Author(s): Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher
        -> Title:     Pointer sentinel mixture models.
        -> Year:      2016
     -> Manual search was skipped by the user.
- Checking reference 39/64:
  -> INFO: Now checking 1 results for matching title: 'Up or down? adaptive rounding for post-training quantization'
       -> INFO: All authors matched!
- Checking reference 40/64:
  -> INFO: Now checking 10 results for matching title: 'Cuda, release: 10.2.89.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['NVIDIA', 'Vingelmann', 'Fitzek', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Cuda%2C+release:+10.2.89. manually and check the results.
        -> Author(s): NVIDIA, Péter Vingelmann, and Frank H P Fitzek
        -> Title:     Cuda, release: 10.2.89.
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 41/64:
  -> INFO: Now checking 10 results for matching title: 'Training language models to follow instructions with human feedback'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 42/64:
  -> INFO: Now checking 2 results for matching title: 'Lut-gemm: Quantized matrix multiplication based on luts for efficient inference in large-scale generative language models'
       -> INFO: All authors matched!
- Checking reference 43/64:
  -> INFO: Now checking 10 results for matching title: 'Automatic differentiation in pytorch'
       -> INFO: All authors matched!
- Checking reference 44/64:
  -> INFO: Now checking 10 results for matching title: 'Language models are unsupervised multitask learners'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Wu, Child, Luan, Amodei'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 45/64:
  -> INFO: Now checking 1 results for matching title: 'Exploring the limits of transfer learning with a unified text-to-text transformer'
       -> INFO: All authors matched!
- Checking reference 46/64:
  -> INFO: Now checking 1 results for matching title: 'Nestquant: Nested lattice quantization for matrix products and llms'
       -> INFO: All authors matched!
- Checking reference 47/64:
  -> INFO: Now checking 1 results for matching title: 'Omniquant: Omnidirectionally calibrated quantization for large language models'
       -> INFO: All authors matched!
- Checking reference 48/64:
  -> INFO: Now checking 10 results for matching title: 'Instantaneous companding of quantized signals'
       -> INFO: All authors matched!
- Checking reference 49/64:
  -> INFO: Now checking 10 results for matching title: 'Learning to summarize with human feedback'
       -> INFO: All authors matched!
- Checking reference 50/64:
  -> INFO: Now checking 10 results for matching title: 'Llama: Open and efficient foundation language models'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Lavril, Izacard, Martinet, Lachaux, Lacroix, Rozière, Goyal, Hambro, Azhar, Rodriguez, Joulin, Grave, Lample'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 51/64:
  -> INFO: Now checking 1 results for matching title: 'Quip#: Even better llm quantization with hadamard incoherence and lattice codebooks'
       -> INFO: All authors matched!
- Checking reference 52/64:
  -> INFO: Now checking 1 results for matching title: 'Qtip: Quantization with trellises and incoherence processing'
       -> INFO: All authors matched!
- Checking reference 53/64:
  -> INFO: Now checking 10 results for matching title: 'Companding in signal processing'
       -> INFO: All authors matched!
- Checking reference 54/64:
  -> INFO: Now checking 1 results for matching title: 'Gptvq: The blessing of dimensionality for llm quantization'
       -> INFO: All authors matched!
- Checking reference 55/64:
  -> INFO: Now checking 10 results for matching title: 'Attention is all you need'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 7)
                   Unmatched authors = 'Gomez'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 56/64:
  -> INFO: Now checking 1 results for matching title: 'Towards accurate post-training network quantization via bit-split and stitching'
       -> INFO: All authors matched!
- Checking reference 57/64:
  -> INFO: Now checking 4 results for matching title: 'A survey of model compression and acceleration for deep neural networks'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Cheng, Zhou, Tao'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 58/64:
  -> INFO: Now checking 10 results for matching title: 'Smoothquant: Accurate and efficient post-training quantization for large language models'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 5)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/64:
  -> INFO: Now checking 1 results for matching title: 'Improving 3d gaussian splatting compression by sceneadaptive lattice vector quantization'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Xu', 'Wu', 'Zhang', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Improving+3d+gaussian+splatting+compression+by+sceneadaptive+lattice+vector+quantization manually and check the results.
        -> Author(s): Hao Xu, Xiaolin Wu, and Xi Zhang
        -> Title:     Improving 3d gaussian splatting compression by sceneadaptive lattice vector quantization
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 60/64:
  -> INFO: Now checking 6 results for matching title: 'Multirate neural image compression with adaptive lattice vector quantization'
       -> INFO: All authors matched!
- Checking reference 61/64:
  -> INFO: Now checking 2 results for matching title: 'Zeroquant: Efficient and affordable post-training quantization for large-scale transformers'
       -> INFO: All authors matched!
- Checking reference 62/64:
  -> INFO: Now checking 1 results for matching title: 'Lvqac: Lattice vector quantization coupled with spatially adaptive companding for efficient learned image compression'
       -> INFO: All authors matched!
- Checking reference 63/64:
  -> INFO: Now checking 3 results for matching title: 'Learning optimal lattice vector quantizers for end-to-end neural image compression'
       -> INFO: All authors matched!
- Checking reference 64/64:
  -> INFO: Now checking 1 results for matching title: 'Receptive field expanded look-up tables for vision inference: Advancing from low-level to high-level tasks'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 3: z∈Zd ∥x −G z∥.
-> Invalid unicode use found on p. 3: and the inverse function is applied after quantization to obtain the reconstruction ˆx = F −1(ˆz),
-> Invalid unicode use found on p. 4: Wg = F −1
-> Invalid unicode use found on p. 4: |GN+1| = |GN−1|,
-> Invalid unicode use found on p. 4: N −1, N + 1
-> Invalid unicode use found on p. 4: and GN−1 = {g | bg = N −1}. This constraint ensures a balanced allocation: the number of groups
-> Invalid unicode use found on p. 4: assigned N + 1 bits equals those assigned N −1 bits, while the majority receive N bits. For example,
-> Invalid unicode use found on p. 4: where Zg ∈Zd×ℓg holds the integer lattice indices computed by rounding each column of G−1
-> Invalid unicode use found on p. 4: WgX −c
-> Invalid unicode use found on p. 4: WgX −GgZgX
-> Invalid unicode use found on p. 4: G−1
-> Invalid unicode use found on p. 5: ∇GgLg = −2
-> Invalid unicode use found on p. 5: WgX −GgZgX
-> Invalid unicode use found on p. 5: Gg −G(0)
-> Invalid unicode use found on p. 5: F −1
-> Invalid unicode use found on p. 5: (y) = sgn(y) (1 + µg)|y| −1
-> Invalid unicode use found on p. 5: G−1
-> Invalid unicode use found on p. 5: Wg = F −1
-> Invalid unicode use found on p. 5: WgX −c
-> Invalid unicode use found on p. 5: 2 + λ∥Gg −G0∥2
-> Invalid unicode use found on p. 5: Because both Fg and F −1
-> Invalid unicode use found on p. 6: G−1
-> Invalid unicode use found on p. 6: F −1
-> Invalid unicode use found on p. 6: WgX −c
-> Invalid unicode use found on p. 6: Gg −G(0)
-> Invalid unicode use found on p. 6: Gg ←Gg −ηG∇GgLg
-> Invalid unicode use found on p. 6: µg ←µg −ηµ∇µgLg
-> Invalid unicode use found on p. 6: −L(t−1)
-> Invalid unicode use found on p. 6: /L(t−1)
-> Invalid unicode use found on p. 6: F −1
-> Invalid unicode use found on p. 14: 1. Compute the real coordinate vector: x = B−1t. This step expresses the target vector t in
-> Invalid unicode use found on p. 14: e = t −v = B(x −c) = Bδ,
-> Invalid unicode use found on p. 14: i−1
-> Invalid unicode use found on p. 14: i−1
-> Invalid unicode use found on p. 15: |µj,i| ≤n −j
-> Invalid unicode use found on p. 15: i=j+1 |µj,i| ≤n−j
-> Invalid unicode use found on p. 15: 1 + n −j
-> Invalid unicode use found on p. 15: 1 + n −j
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Bracket content ['0', ' m/(2g)'] on p. 5 could not be matched to a reference.
   -> Sentence:  For a weight matrix with m output channels and group size g = 128, the search space is limited to [0, m/(2g)], 
requiring only O(log m) iterations
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 780 sentences on 11 pages -> Avg. of 79.0 sentences per page
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
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
-> Missing an abstract for reference with index 40 (Ref. ID = 41); Skipping LLM check...
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
-> Missing an abstract for reference with index 46 (Ref. ID = 47); Skipping LLM check...
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
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
  -> Found 4 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 12 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 12
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 13
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 14
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 15
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 16
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\43 Learning Grouped Lattice Vector Quantizers\PAU_results.md
```