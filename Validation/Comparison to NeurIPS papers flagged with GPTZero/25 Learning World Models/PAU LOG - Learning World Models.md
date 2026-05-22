
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\25 Learning World Models\Learning World Models for Interactive Video Generation.pdf"
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
- Found following heading '2 - Related Works' on page 2
- Found following heading '3 - Methodology' on page 3
- Found following heading '4 - Experiments' on page 6
- Found following heading '5 - Conclusions and Discussions' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Baseline Method Details' on page 15
- Found following appendix 'B - Implementation Details' on page 16
- Found following appendix 'C - Additional Experiments' on page 16
- Found following appendix 'D - More Results' on page 20
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 15
All found references: 68
-> Warning: Malformed author string: 'Sand-AI'
-> Warning: Malformed author string: 'Decart'
-> Warning: Malformed author string: 'Etched'
-> Warning: Could not parse year in reference 'Google. Realestate10k.'!
-> Warning: Malformed author string: 'Google'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                               link  valid
0       1  Manuel Watter, Jost Springenberg, Joschka Boed...  ...                                                      None
1       2                    David Ha and Jürgen Schmidhuber  ...                                                      None
2       3  Danijar Hafner, Timothy Lillicrap, Mohammad No...  ...                                                      None
3       4  Jascha Sohl-Dickstein, Eric A  Weiss, Niru Mah...  ...                                                      None
4       5                        Yang Song and Stefano Ermon  ...                                                      None
..    ...                                                ...  ...                                                ...    ...
63     64  Richard Zhang, Phillip Isola, Alexei A Efros, ...  ...                                                      None
64     65  Ziqi Huang, Yinan He, Jiashuo Yu, Fan Zhang, C...  ...                                                      None
65     66  Kiwhan Song, Boyuan Chen, Max Simchowitz, Yilu...  ...                                                      None
66     67                                             Google  ...  https://google.github.io/realestate10k/index.h...   None
67     68  Jianwen Jiang, Chao Liang, Jiaqi Yang, Gaojie ...  ...                                                      None

[68 rows x 10 columns]
- Checking reference 1/68:
  -> INFO: Now checking 1 results for matching title: 'Embed to control: A locally linear latent dynamics model for control from raw images'
       -> INFO: All authors matched!
- Checking reference 2/68:
  -> INFO: Now checking 10 results for matching title: 'Recurrent world models facilitate policy evolution'
       -> INFO: All authors matched!
- Checking reference 3/68:
  -> INFO: Now checking 10 results for matching title: 'Mastering atari with discrete world models'
       -> INFO: All authors matched!
- Checking reference 4/68:
  -> INFO: Now checking 10 results for matching title: 'Deep unsupervised learning using nonequilibrium thermodynamics'
       -> INFO: All authors matched!
- Checking reference 5/68:
  -> INFO: Now checking 3 results for matching title: 'Generative modeling by estimating gradients of the data distribution'
       -> INFO: All authors matched!
- Checking reference 6/68:
  -> INFO: Now checking 10 results for matching title: 'Denoising diffusion probabilistic models'
       -> INFO: All authors matched!
- Checking reference 7/68:
  -> INFO: Now checking 10 results for matching title: 'Score-based generative modeling through stochastic differential equations'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 8/68:
  -> INFO: Now checking 10 results for matching title: 'Video generation models as world simulators'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Brooks', 'Peebles', 'Holmes', 'DePue', 'Guo', 'Jing', 'Schnurr', 'Taylor', 'Luhman', 'Luhman', 'Ng', 'Wang', 'Ramesh', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Video+generation+models+as+world+simulators manually and check the results.
        -> Author(s): Tim Brooks, Bill Peebles, Connor Holmes, Will DePue, Yufei Guo, Li Jing, David Schnurr, Joe Taylor, Troy Luhman, Eric Luhman, Clarence Ng, Ricky Wang, and Aditya Ramesh
        -> Title:     Video generation models as world simulators
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 9/68:
  -> INFO: Now checking 10 results for matching title: 'Genie: Generative interactive environments'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 10/68:
  -> INFO: Now checking 10 results for matching title: 'Diffusion models are real-time game engines'
       -> INFO: All authors matched!
- Checking reference 11/68:
  -> INFO: Now checking 10 results for matching title: 'Scaling autoregressive video models'
       -> INFO: All authors matched!
- Checking reference 12/68:
  -> INFO: Now checking 10 results for matching title: 'Flexible diffusion modeling of long videos'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Naderiparizi, Masrani, Weilbach, Wood'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/68:
  -> INFO: Now checking 2 results for matching title: 'Arlon: Boosting diffusion transformers with autoregressive models for long video generation'
       -> INFO: All authors matched!
- Checking reference 14/68:
  -> INFO: Now checking 10 results for matching title: 'Progressive autoregressive video diffusion models'
       -> INFO: All authors matched!
- Checking reference 15/68:
  -> INFO: Now checking 10 results for matching title: 'Gpt-4 technical report'
       -> WARNING: Not all 279 authors from the found ref. were matched (only 12)
                   Unmatched authors = 'Avila, Babuschkin, Balaji, Balcom, Baltescu, Bao, Bavarian, Belgum, Bello, Berdine, Bernadett-Shapiro, Berner, Bogdonoff, Boiko, Boyd, Brakman, Brockman, Brooks, Brundage, Button, Cai, Campbell, Cann, Carey, Carlson, Carmichael, Chan, Chang, Chantzis, Chen, Chen, Chen, Chen, Chen, Chess, Cho, Chu, Chung, Cummings, Currier, Dai, Decareaux, Degry, Deutsch, Deville, Dhar, Dohan, Dowling, Dunning, Ecoffet, Eleti, Eloundou, Farhi, Fedus, Felix, Fishman, Forte, Fulford, Gao, Georges, Gibson, Goel, Gogineni, Goh, Gontijo-Lopes, Gordon, Grafstein, Gray, Greene, Gross, Gu, Guo, Hallacy, Han, Harris, He, Heaton, Heidecke, Hesse, Hickey, Hickey, Hoeschele, Houghton, Hsu, Hu, Hu, Huizinga, Jain, Jain, Jang, Jiang, Jiang, Jin, Jin, Jomoto, Jonn, Jun, Kaftan, Kaiser, Kamali, Kanitscheider, Keskar, Khan, Kilpatrick, Kim, Kim, Kim, Kirchner, Kiros, Knight, Kokotajlo, Kondraciuk, Kondrich, Konstantinidis, Kosic, Krueger, Kuo, Lampe, Lan, Lee, Leike, Leung, Levy, Li, Lim, Lin, Lin, Litwin, Lopez, Lowe, Lue, Makanju, Malfacini, Manning, Markov, Markovski, Martin, Mayer, Mayne, McGrew, McKinney, McLeavey, McMillan, McNeil, Medina, Mehta, Menick, Metz, Mishchenko, Mishkin, Monaco, Morikawa, Mossing, Mu, Murati, Murk, M'ely, Nair, Nakano, Nayak, Neelakantan, Ngo, Noh, Long, O'Keefe, Pachocki, Paino, Palermo, Pantuliano, Parascandolo, Parish, Parparita, Passos, Pavlov, Peng, Perelman, Peres, Petrov, Pinto, Pokorny, Pokrass, Pong, Powell, Power, Power, Proehl, Puri, Radford, Rae, Ramesh, Raymond, Real, Rimbach, Ross, Rotsted, Roussez, Ryder, Saltarelli, Sanders, Santurkar, Sastry, Schnurr, Schulman, Selsam, Sheppard, Sherbakov, Shieh, Shoker, Sidor, Sigler, Simens, Sitkin, Slama, Sohl, Sokolowsky, Song, Staudacher, Such, Summers, Sutskever, Tang, Tezak, Thompson, Tillet, Tootoonchian, Tseng, Tuggle, Turley, Tworek, Uribe, Vallone, Vijayvergiya, Voss, Wainwright, Wang, Wang, Wang, Ward, Wei, Weinmann, Welihinda, Welinder, Weng, Weng, Wiethoff, Willner, Winter, Wolrich, Wong, Workman, Wu, Wu, Wu, Xiao, Xu, Yoo, Yu, Yuan, Zaremba, Zellers, Zhang, Zhang, Zhao, Zheng, Zhuang, Zhuk, Zoph'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/68:
  -> INFO: Now checking 10 results for matching title: 'Llama: Open and efficient foundation language models'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 17/68:
  -> INFO: Now checking 10 results for matching title: 'Retrieval-augmented generation for large language models: A survey'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 10)
                   Unmatched authors = 'Guo'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/68:
  -> INFO: Now checking 10 results for matching title: 'Retrieval-augmented generation for ai-generated content: A survey'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 9)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 19/68:
  -> INFO: Now checking 10 results for matching title: 'Align your latents: High-resolution video synthesis with latent diffusion models'
       -> INFO: All authors matched!
- Checking reference 20/68:
  -> INFO: Now checking 10 results for matching title: 'Structure-aware video generation with latent diffusion models'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Esser', 'Rombach', 'Ommer', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Structure-aware+video+generation+with+latent+diffusion+models manually and check the results.
        -> Author(s): Patrick Esser, Robin Rombach, and Björn Ommer
        -> Title:     Structure-aware video generation with latent diffusion models
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 21/68:
  -> INFO: Now checking 10 results for matching title: 'Stable video diffusion: Scaling latent video diffusion models to large datasets'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 6)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 22/68:
  -> INFO: Now checking 10 results for matching title: 'Videocrafter2: Overcoming data limitations for high-quality video diffusion models'
       -> INFO: All authors matched!
- Checking reference 23/68:
  -> INFO: Now checking 10 results for matching title: 'Video diffusion models'
       -> INFO: All authors matched!
- Checking reference 24/68:
  -> INFO: Now checking 10 results for matching title: 'Make-a-video: Text-to-video generation without text-video data'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Hayes, Yin, Zhang, Hu, Yang, Ashual, Gafni, Parikh, Gupta, Taigman'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 25/68:
  -> INFO: Now checking 1 results for matching title: 'Cogvideo: Large-scale pretraining for text-to-video generation with transformers'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Cogvideo: Large-scale pretraining for text-to-video generation with transformers'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Cogvideo:+Large-scale+pretraining+for+text-to-video+generation+with+transformers manually and check the results.
        -> Author(s): Yu Hong, Jing Wei, Xing Liu, Xiaodi Wang, Yutong Bai, Haitao Li, Ming Zhang, and Hao Xu
        -> Title:     Cogvideo: Large-scale pretraining for text-to-video generation with transformers
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 26/68:
  -> INFO: Now checking 1 results for matching title: 'Cogvideox: Text-to-video diffusion models with an expert transformer'
       -> WARNING: Not all 19 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Yin, Wang, Cheng, Liu, Dong, Tang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 27/68:
  -> INFO: Now checking 10 results for matching title: 'Modelscope text-to-video technical report'
       -> INFO: All authors matched!
- Checking reference 28/68:
  -> INFO: Now checking 6 results for matching title: 'Dollar: Few-step video generation via distillation and latent reward optimization'
       -> INFO: All authors matched!
- Checking reference 29/68:
  -> INFO: Now checking 1 results for matching title: 'Open-sora: Democratizing efficient video production for all'
       -> INFO: All authors matched!
- Checking reference 30/68:
  -> INFO: Now checking 10 results for matching title: 'Auto-encoding variational bayes.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Kingma', 'Welling', '2013']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Auto-encoding+variational+bayes. manually and check the results.
        -> Author(s): Diederik P Kingma, Max Welling, et al
        -> Title:     Auto-encoding variational bayes.
        -> Year:      2013
     -> Manual search was skipped by the user.
- Checking reference 31/68:
  -> INFO: Now checking 10 results for matching title: 'Highresolution image synthesis with latent diffusion models'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Highresolution image synthesis with latent diffusion models'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Highresolution+image+synthesis+with+latent+diffusion+models manually and check the results.
        -> Author(s): Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer
        -> Title:     Highresolution image synthesis with latent diffusion models
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 32/68:
  -> INFO: Now checking 10 results for matching title: 'Scalable diffusion models with transformers'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/68:
  -> INFO: Now checking 10 results for matching title: 'Attention is all you need'
       -> INFO: All authors matched!
- Checking reference 34/68:
  -> INFO: Now checking 3 results for matching title: 'Slowfast-vgen: Slow-fast learning for action-driven long video generation'
       -> WARNING: Not all 12 authors from the found ref. were matched (only 12)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 35/68:
  -> INFO: Now checking 3 results for matching title: 'ivideogpt: Interactive videogpts are scalable world models'
       -> INFO: All authors matched!
- Checking reference 36/68:
  -> INFO: Now checking 10 results for matching title: 'Fifo-diffusion: Generating infinite videos from text without training'
       -> INFO: All authors matched!
- Checking reference 37/68:
  -> INFO: Now checking 3 results for matching title: 'The matrix: Infinite-horizon world generation with real-time moving control'
       -> INFO: All authors matched!
- Checking reference 38/68:
  -> INFO: Now checking 10 results for matching title: 'Magi-1: Autoregressive video generation at scale.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 241 results for matching title: 'Magi-1: Autoregressive video generation at scale.'
  -> WARNING: None of the 241 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Magi-1:+Autoregressive+video+generation+at+scale. manually and check the results.
        -> Author(s): Sand-AI
        -> Title:     Magi-1: Autoregressive video generation at scale.
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 39/68:
  -> INFO: Now checking 4 results for matching title: 'Streamingt2v: Consistent, dynamic, and extendable long video generation from text'
       -> INFO: All authors matched!
- Checking reference 40/68:
  -> INFO: Now checking 3 results for matching title: 'Mcvd-masked conditional video diffusion for prediction, generation, and interpolation'
       -> INFO: All authors matched!
- Checking reference 41/68:
  -> INFO: Now checking 6 results for matching title: 'Diffusion forcing: Next-token prediction meets full-sequence diffusion'
       -> INFO: All authors matched!
- Checking reference 42/68:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Diffusion world model: Future modeling beyond step-by-step rollout for offline reinforcement learning
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 43 results for matching title: 'Diffusion world model: Future modeling beyond step-by-step rollout for offline reinforcement learning'
  -> WARNING: None of the 43 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Diffusion+world+model:+Future+modeling+beyond+step-by-step+rollout+for+offline+reinforcement+learning manually and check the results.
        -> Author(s): Zihan Ding, Amy Zhang, Yuandong Tian, and Qinqing Zheng
        -> Title:     Diffusion world model: Future modeling beyond step-by-step rollout for offline reinforcement learning
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 43/68:
  -> INFO: Now checking 1 results for matching title: 'Diffusion for world modeling: Visual details matter in atari'
       -> INFO: All authors matched!
- Checking reference 44/68:
  -> INFO: Now checking 10 results for matching title: 'Oasis: A universe in a transformer'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Decart', 'Etched', 'Quevedo', 'McIntyre', 'Campbell', 'Chen', 'Wachen', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Oasis:+A+universe+in+a+transformer manually and check the results.
        -> Author(s): Decart, Etched, Julian Quevedo, Quinn McIntyre, Spruce Campbell, Xinlei Chen, and Robert Wachen
        -> Title:     Oasis: A universe in a transformer
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 45/68:
  -> INFO: Now checking 10 results for matching title: 'Gamegen-x: Interactive open-world game video generation'
       -> INFO: All authors matched!
- Checking reference 46/68:
  -> INFO: Now checking 1 results for matching title: 'Mineworld: a real-time and open-source interactive world model on minecraft'
       -> INFO: All authors matched!
- Checking reference 47/68:
  -> INFO: Now checking 10 results for matching title: 'Gamefactory: Creating new games with generative interactive videos'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 469 results for matching title: 'Gamefactory: Creating new games with generative interactive videos'
  -> WARNING: None of the 469 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gamefactory:+Creating+new+games+with+generative+interactive+videos manually and check the results.
        -> Author(s): Jiwen Yu, Yiran Qin, Xintao Wang, Pengfei Wan, Di Zhang, and Xihui Liu
        -> Title:     Gamefactory: Creating new games with generative interactive videos
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 48/68:
  -> INFO: Now checking 1 results for matching title: 'Gaia-1: A generative world model for autonomous driving'
       -> INFO: All authors matched!
- Checking reference 49/68:
  -> INFO: Now checking 1 results for matching title: 'Cosmos-reason1: From physical common sense to embodied reasoning'
       -> WARNING: Not all 45 authors from the found ref. were matched (only 16)
                   Unmatched authors = 'Gu, Gururani, Hanafi, Hao, Huffman, Johnson, Khan, Kurian, Lantz, Lee, Liu, Mathau, Pavao, Ping, Romero, Smelyanskiy, Song, Tchapmi, Wang, Wang, Wang, Wei, Xu, Xu, Yang, Yang, Yang, Zeng, Zhang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 50/68:
  -> INFO: Now checking 10 results for matching title: 'Navigation world models'
       -> INFO: All authors matched!
- Checking reference 51/68:
  -> INFO: Now checking 10 results for matching title: 'Genie 2: A large-scale foundation world model'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Parker-Holder', 'Ball', 'Bruce', 'Dasagi', 'Holsheimer', 'Kaplanis', 'Moufarek', 'Scully', 'Shar', 'Shi', 'Spencer', 'Yung', 'Dennis', 'Kenjeyev', 'Long', 'Mnih', 'Chan', 'Gazeau', 'Li', 'Pardo', 'Wang', 'Zhang', 'Besse', 'Harley', 'Mitenkova', 'Wang', 'Clune', 'Hassabis', 'Hadsell', 'Bolton', 'Singh', 'Rocktäschel', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Genie+2:+A+large-scale+foundation+world+model manually and check the results.
        -> Author(s): Jack Parker-Holder, Philip Ball, Jake Bruce, Vibhavari Dasagi, Kristian Holsheimer, Christos Kaplanis, Alexandre Moufarek, Guy Scully, Jeremy Shar, Jimmy Shi, Stephen Spencer, Jessica Yung, Michael Dennis, Sultan Kenjeyev, Shangbang Long, Vlad Mnih, Harris Chan, Maxime Gazeau, Bonnie Li, Fabio Pardo, Luyu Wang, Lei Zhang, Frederic Besse, Tim Harley, Anna Mitenkova, Jane Wang, Jeff Clune, Demis Hassabis, Raia Hadsell, Adrian Bolton, Satinder Singh, and Tim Rocktäschel
        -> Title:     Genie 2: A large-scale foundation world model
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 52/68:
  -> INFO: Now checking 10 results for matching title: 'Aether: Geometric-aware unified world modeling'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 11)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 53/68:
  -> INFO: Now checking 1 results for matching title: 'Gen3c: 3d-informed worldconsistent video generation with precise camera control'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Gen3c: 3d-informed worldconsistent video generation with precise camera control'
  -> WARNING: None of the 2 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gen3c:+3d-informed+worldconsistent+video+generation+with+precise+camera+control manually and check the results.
        -> Author(s): Xuanchi Ren, Tianchang Shen, Jiahui Huang, Huan Ling, Yifan Lu, Merlin Nimier-David, Thomas Müller, Alexander Keller, Sanja Fidler, and Jun Gao
        -> Title:     Gen3c: 3d-informed worldconsistent video generation with precise camera control
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 54/68:
  -> INFO: Now checking 10 results for matching title: 'Reconx: Reconstruct any scene from sparse views with video diffusion model'
       -> INFO: All authors matched!
- Checking reference 55/68:
  -> INFO: Now checking 1 results for matching title: 'Cat3d: Create anything in 3d with multi-view diffusion models'
       -> INFO: All authors matched!
- Checking reference 56/68:
  -> INFO: Now checking 10 results for matching title: 'Tesseract: Learning 4d embodied world models'
       -> INFO: All authors matched!
- Checking reference 57/68:
  -> INFO: Now checking 10 results for matching title: 'Worldmem: Long-term consistent world simulation with memory'
       -> INFO: All authors matched!
- Checking reference 58/68:
  -> INFO: Now checking 10 results for matching title: 'Roformer: Enhanced transformer with rotary position embedding'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 5)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/68:
  -> INFO: Now checking 10 results for matching title: 'Yarn: Efficient context window extension of large language models'
       -> INFO: All authors matched!
- Checking reference 60/68:
  -> INFO: Now checking 1 results for matching title: 'Leave no context behind: Efficient infinite context transformers with infini-attention.'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Leave no context behind: Efficient infinite context transformers with infini-attention.'
       -> INFO: All authors matched!
- Checking reference 61/68:
  -> INFO: Now checking 4 results for matching title: 'Packing input frame context in next-frame prediction models for video generation.'
  -> WARNING: None of the 4 results matched the expected title!
  -> INFO: Now checking 15 results for matching title: 'Packing input frame context in next-frame prediction models for video generation.'
       -> INFO: All authors matched!
- Checking reference 62/68:
  -> INFO: Now checking 3 results for matching title: 'Minerl: A large-scale dataset of minecraft demonstrations'
       -> INFO: All authors matched!
- Checking reference 63/68:
  -> INFO: Now checking 10 results for matching title: 'Image quality assessment: from error visibility to structural similarity'
       -> INFO: All authors matched!
- Checking reference 64/68:
  -> INFO: Now checking 1 results for matching title: 'The unreasonable effectiveness of deep features as a perceptual metric'
       -> INFO: All authors matched!
- Checking reference 65/68:
  -> INFO: Now checking 10 results for matching title: 'Vbench: Comprehensive benchmark suite for video generative models'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 66/68:
  -> INFO: Now checking 10 results for matching title: 'History-guided video diffusion.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'History-guided video diffusion.'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 5)
                   Unmatched authors = '0003'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 5)
                   Unmatched authors = '0003'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 67/68:
  -> Checking if provided link is pingable: https://google.github.io/realestate10k/index.html,
  -> INFO: Now checking 10 results for matching title: 'Realestate10k'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 901 results for matching title: 'Realestate10k'
  -> WARNING: None of the 901 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Realestate10k manually and check the results.
        -> Author(s): Google
        -> Title:     Realestate10k
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 68/68:
  -> INFO: Now checking 1 results for matching title: 'Loopy: Taming audio-driven portrait avatar with long-term motion dependency'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: q(zt|zt−1) = N(zt;
-> Invalid unicode use found on p. 2: 1 −βtzt−1, βtI)
-> Invalid unicode use found on p. 2: L = Et,ϵ,z[∥ϵ −ϵθ(zt, t)∥2
-> Invalid unicode use found on p. 2: where zt = √¯αtz0 + √1 −¯αtϵ with ϵ ∼N(0, I).
-> Invalid unicode use found on p. 2: zt−1 =
-> Invalid unicode use found on p. 2: (zt −
-> Invalid unicode use found on p. 2: √1 −¯αt
-> Invalid unicode use found on p. 2: where αt = 1 −βt and ¯αt = Qt
-> Invalid unicode use found on p. 3: 0 +√1 −¯αtϵi, ϵi ∼N(0, I), where zi
-> Invalid unicode use found on p. 3: LDF = E[t],ϵ,z,a[∥ϵ −ϵθ(z[t], [t], a)∥2
-> Invalid unicode use found on p. 4: r(ˆs) = fsim(ˆs ⊙w, sL−1 ⊙w), ˆs ∈B
-> Invalid unicode use found on p. 4: to be predicted sL−1, and w ∈RS is a weight vector that modulates the importance of different state
-> Invalid unicode use found on p. 4: LVRAG = E[t],[t′],ϵ,˜z,a,s[∥ϵt −ϵθ(˜z˜t, ˜t, ˜a, ˜s)∥2
-> Invalid unicode use found on p. 5: where the inner product between query qm and key kn depends on relative distance (m −n). YaRN
-> Invalid unicode use found on p. 5: decreasing segments Gj, where Lj = L1 · αj−1. From each segment Gj, we sample k frames to
-> Invalid unicode use found on p. 5: and value vs matrices. The model retrieves hidden state Amem from compressive memory Ms−1:
-> Invalid unicode use found on p. 5: Amem = σ(qs)Ms−1
-> Invalid unicode use found on p. 5: σ(qs)ns−1 . Memory Ms−1 and normalization vector ns−1 are then updated. The final
-> Invalid unicode use found on p. 14: product between the m-th query qm and n-th key kn depends only on the relative distance (m −n):
-> Invalid unicode use found on p. 14: (Wqzm)(Wkzn)∗· ei(m−n)θ
-> Invalid unicode use found on p. 14: = g(zm, zn, m −n)
-> Invalid unicode use found on p. 14: frequencies per dimension: θd = b−2d/D, with b = 10000.
-> Invalid unicode use found on p. 14: h(θd) = (1 −γ(rd)) · θd
-> Invalid unicode use found on p. 14: Lj = L1 · αj−1 for a base α < 1 and L1 being the length of the oldest segment G1), ensuring that
-> Invalid unicode use found on p. 15: retrieves a hidden state Amem by querying the compressive memory Ms−1:
-> Invalid unicode use found on p. 15: Amem = σ(qs)Ms−1
-> Invalid unicode use found on p. 15: σ(qs)ns−1
-> Invalid unicode use found on p. 15: where σ(·) is an element-wise nonlinear activation function (e.g., ELU(·) + 1) and ns−1 is a
-> Invalid unicode use found on p. 15: normalization vector (accumulated up to segment s −1).
-> Invalid unicode use found on p. 15: Ms = Ms−1 + σ(ks)T
-> Invalid unicode use found on p. 15: vs −σ(ks)Ms−1
-> Invalid unicode use found on p. 15: σ(ks)ns−1
-> Invalid unicode use found on p. 15: ns = ns−1 + σ(ks)T 1N
-> Invalid unicode use found on p. 15: As = sigmoid(β) ⊙Amem + (1 −sigmoid(β)) ⊙Alocal
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Numeric reference range couldn't be parsed as Integers: ['∥ϵ −ϵθ(zt', ' t)∥2 2']
-> Warning: Numeric reference range couldn't be parsed as Integers: ['∥ϵ −ϵθ(z[t']
-> Warning: Numeric reference range couldn't be parsed as Integers: ['∥ϵt −ϵθ(˜z˜t', ' ˜t', ' ˜a', ' ˜s)∥2 2 ⊙m']
-> Warning: Bracket content ['0Lh', ' 1Lc'] on p. 5 could not be matched to a reference.
   -> Sentence:  Overall, the training objective of VRAG on diffusion models is defined as: LVRAG = E[t],[t′],ϵ,˜z,a,s[∥ϵt 
−ϵθ(˜z˜t, ˜t, ˜a, ˜s)∥2 2 ⊙m], (6) ˜z˜t = [zhist,[t′],z[t]], ˜a = [∅Lh, a], ˜s = [shist, s], m = [0Lh, 1Lc], (7) where ˜t is a 
concatenation of [t′] and [t], with t′ < t and t′, t ∈[T]
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 347 sentences on 11 pages -> Avg. of 35.7 sentences per page
-> Warning: Reference '68' never used in the document's text.
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
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
-> Missing an abstract for reference with index 30 (Ref. ID = 31); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
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
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
-> Missing an abstract for reference with index 61 (Ref. ID = 62); Skipping LLM check...
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 65 (Ref. ID = 66); Skipping LLM check...
-> Missing an abstract for reference with index 66 (Ref. ID = 67); Skipping LLM check...
-> Missing an abstract for reference with index 67 (Ref. ID = 68); Skipping LLM check...
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
  -> Found 4 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 3 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 15
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 16
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 17
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 18
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 19
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\25 Learning World Models\PAU_results.md
```