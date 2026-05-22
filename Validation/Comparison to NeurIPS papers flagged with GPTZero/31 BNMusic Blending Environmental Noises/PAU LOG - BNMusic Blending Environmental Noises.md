
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\31 BNMusic Blending Environmental Noises\BNMusic Blending Environmental Noises into.pdf"
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
- Found following heading '2 - Related work' on page 3
- Found following heading '3 - BNMusic framework: Blending Noises into personalized Music' on page 4
- Found following heading '4 - Experiment' on page 6
- Found following heading '5 - Conclusion and discussion' on page 9
=> Found references/literature section on page 10
- Found first appendix 'A - Loudness-FAD relationship' on page 13
- Found following appendix 'B - More details in Stage 1' on page 13
- Found following appendix 'C - More details about subjective evaluation' on page 15
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 13
All found references: 42
-> Warning: Malformed author string: 'OpenAI'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ... link  valid
0       1  Zalán Borsos, Matt Sharifi, and Marco Tagliasa...  ...        None
1       2  Marco Comunità, Zhi Zhong, Akira Takahashi, Sh...  ...        None
2       3  Jade Copet, Felix Kreuk, Itai Gat, Tal Remez, ...  ...        None
3       4  Zach Evans, Julian D Parker, CJ Carr, Zack Zuk...  ...        None
4       5                  Seth* Forsgren and Hayk* Martiros  ...        None
5       6                                 Donald D Greenwood  ...        None
6       7  Bing Han, Junyu Dai, Weituo Hao, Xinyan He, Do...  ...        None
7       8          Jonathan Ho, Ajay Jain, and Pieter Abbeel  ...        None
8       9  Jaesung Huh, Jacob Chalk, Evangelos Kazakos, D...  ...        None
9      10  Kevin Kilgour, Mauricio Zuluaga, Dominik Roble...  ...        None
10     11                      Sen M Kuo and Dennis R Morgan  ...        None
11     12  Haohe Liu, Zehua Chen, Yi Yuan, Xinhao Mei, Xu...  ...        None
12     13  Haohe Liu, Yi Yuan, Xubo Liu, Xinhao Mei, Qiuq...  ...        None
13     14  Shansong Liu, Atin Sakkeer Hussain, Chenshuo S...  ...        None
14     15  Andreas Lugmayr, Martin Danelljan, Andres Rome...  ...        None
15     16                      Hila Manor and Tomer Michaeli  ...        None
16     17  Andrés Marafioti, Piotr Majdak, Nicki Holighau...  ...        None
17     18  Jan Melechovsky, Zixun Guo, Deepanway Ghosal, ...  ...        None
18     19                      Ondrej Mokry and Pavel Rajmic  ...        None
19     20                                     Brian CJ Moore  ...        None
20     21  Masato Nakayama, Takuya Hayashi, Toru Takahash...  ...        None
21     22  Thibaud Necciari, Peter Balazs, Richard Kronla...  ...        None
22     23  Zachary Novack, Julian McAuley, Taylor Berg-Ki...  ...        None
23     24  Zachary Novack, Ge Zhu, Jonah Casebeer, Julian...  ...        None
24     25                                             OpenAI  ...        None
25     26                          T  Painter and A  Spanias  ...        None
26     27  Jeongseung Park, Minseon Yang, Minz Won Park, ...  ...        None
27     28  Julian D Parker, Janne Spijkervet, Katerina Ko...  ...        None
28     29  Nathanaël Perraudin, Peter Balazs, and Peter L...  ...        None
29     30                                    Karol J  Piczak  ...        None
30     31  Robin Rombach, Andreas Blattmann, Dominik Lore...  ...        None
31     32  Koichi Saito, Dongjun Kim, Takashi Shibuya, Ch...  ...        None
32     33                                           B Scharf  ...        None
33     34  Flavio Schneider, Ojasv Kamal, Zhijing Jin, an...  ...        None
34     35                  Ying Song, Yu Gong, and Sen M Kuo  ...        None
35     36         Christian J  Steinmetz and Joshua D  Reiss  ...        None
36     37  Mitchell D Swanson, Bin Zhu, Ahmed H Tewfik, a...  ...        None
37     38  Yuancheng Wang, Zeqian Ju, Xu Tan, Lei He, Zhi...  ...        None
38     39  Shih-Lun Wu, Chris Donahue, Shinji Watanabe, a...  ...        None
39     40         Shiyuan Yang, Xiaodong Chen, and Jing Liao  ...        None
40     41                          Shilun Zhang and Lin Chen  ...        None
41     42  Yixiao Zhang, Yukara Ikemiya, Gus Xia, Naoki M...  ...        None

[42 rows x 10 columns]
- Checking reference 1/42:
  -> INFO: Now checking 2 results for matching title: 'Speechpainter: Text-conditioned speech inpainting'
       -> INFO: All authors matched!
- Checking reference 2/42:
  -> INFO: Now checking 1 results for matching title: 'Specmaskgit: Masked generative modeling of audio spectrograms for efficient audio synthesis and beyond'
       -> INFO: All authors matched!
- Checking reference 3/42:
  -> INFO: Now checking 10 results for matching title: 'Simple and controllable music generation.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Copet', 'Kreuk', 'Gat', 'Remez', 'Kant', 'Synnaeve', 'Adi', 'Défossez', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Simple+and+controllable+music+generation. manually and check the results.
        -> Author(s): Jade Copet, Felix Kreuk, Itai Gat, Tal Remez, David Kant, Gabriel Synnaeve, Yossi Adi, and Alexandre Défossez
        -> Title:     Simple and controllable music generation.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 4/42:
  -> INFO: Now checking 10 results for matching title: 'Long-form music generation with latent diffusion'
       -> INFO: All authors matched!
- Checking reference 5/42:
  -> INFO: Now checking 3 results for matching title: 'Riffusion - Stable diffusion for real-time music generation'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Forsgren', 'Martiros', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Riffusion+-+Stable+diffusion+for+real-time+music+generation manually and check the results.
        -> Author(s): Seth* Forsgren and Hayk* Martiros
        -> Title:     Riffusion - Stable diffusion for real-time music generation
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 6/42:
  -> INFO: Now checking 10 results for matching title: 'Auditory masking and the critical band'
       -> INFO: All authors matched!
- Checking reference 7/42:
  -> INFO: Now checking 2 results for matching title: 'Instructme: An instruction guided music edit and remix framework with latent diffusion models'
       -> INFO: All authors matched!
- Checking reference 8/42:
  -> INFO: Now checking 10 results for matching title: 'Denoising diffusion probabilistic models'
       -> INFO: All authors matched!
- Checking reference 9/42:
  -> INFO: Now checking 2 results for matching title: 'EPIC-SOUNDS: A Large-Scale Dataset of Actions that Sound'
       -> INFO: All authors matched!
- Checking reference 10/42:
  -> INFO: Now checking 2 results for matching title: 'Fréchet audio distance: A metric for evaluating music enhancement algorithms.'
  -> WARNING: None of the 2 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Fréchet audio distance: A metric for evaluating music enhancement algorithms.'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Fréchet+audio+distance:+A+metric+for+evaluating+music+enhancement+algorithms. manually and check the results.
        -> Author(s): Kevin Kilgour, Mauricio Zuluaga, Dominik Roblek, and Matthew Sharifi
        -> Title:     Fréchet audio distance: A metric for evaluating music enhancement algorithms.
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 11/42:
  -> INFO: Now checking 10 results for matching title: 'Active noise control: A tutorial review'
       -> INFO: All authors matched!
- Checking reference 12/42:
  -> INFO: Now checking 10 results for matching title: 'Audioldm: Text-to-audio generation with latent diffusion models'
       -> INFO: All authors matched!
- Checking reference 13/42:
  -> INFO: Now checking 1 results for matching title: 'Audioldm 2: Learning holistic audio generation with self-supervised pretraining'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 14/42:
  -> INFO: Now checking 2 results for matching title: 'M2ugen: Multi-modal music understanding and generation with the power of large language models'
       -> INFO: All authors matched!
- Checking reference 15/42:
  -> INFO: Now checking 10 results for matching title: 'Repaint: Inpainting using denoising diffusion probabilistic models'
       -> INFO: All authors matched!
- Checking reference 16/42:
  -> INFO: Now checking 1 results for matching title: 'Zero-shot unsupervised and text-based audio editing using DDPM inversion'
       -> INFO: All authors matched!
- Checking reference 17/42:
  -> INFO: Now checking 1 results for matching title: 'GACELA: A generative adversarial context encoder for long audio inpainting of music'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/42:
  -> INFO: Now checking 10 results for matching title: 'Mustango: Toward controllable text-to-music generation.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Melechovsky', 'Guo', 'Ghosal', 'Majumder', 'Herremans', 'Poria', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Mustango:+Toward+controllable+text-to-music+generation. manually and check the results.
        -> Author(s): Jan Melechovsky, Zixun Guo, Deepanway Ghosal, Navonil Majumder, Dorien Herremans, and Soujanya Poria
        -> Title:     Mustango: Toward controllable text-to-music generation.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 19/42:
  -> INFO: Now checking 1 results for matching title: 'Audio inpainting: Revisited and reweighted'
       -> WARNING: Not all 2 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Mokrý'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 20/42:
  -> INFO: Now checking 10 results for matching title: 'Psychoacoustics'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 306 results for matching title: 'Psychoacoustics'
  -> WARNING: None of the 306 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Psychoacoustics manually and check the results.
        -> Author(s): Brian CJ Moore
        -> Title:     Psychoacoustics
        -> Year:      2014
     -> Manual search was skipped by the user.
- Checking reference 21/42:
  -> INFO: Now checking 1 results for matching title: 'Comfortable sound design based on auditory masking with chord progression and melody generation corresponding to the peak frequencies of dental treatment noises'
       -> INFO: All authors matched!
- Checking reference 22/42:
  -> INFO: Now checking 10 results for matching title: 'Auditory time-frequency masking: Psychoacoustical data and application to audio representations'
       -> INFO: All authors matched!
       -> WARNING: Year (2011) does not match expected year (2012)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 23/42:
  -> INFO: Now checking 2 results for matching title: 'DITTO: Diffusion inference-time t-optimization for music generation'
       -> INFO: All authors matched!
- Checking reference 24/42:
  -> INFO: Now checking 1 results for matching title: 'Presto! distilling steps and layers for accelerating music generation'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 25/42:
  -> INFO: Now checking 10 results for matching title: 'Chatgpt: Language model for dialogue, 2024'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 83 results for matching title: 'Chatgpt: Language model for dialogue, 2024'
  -> WARNING: None of the 83 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Chatgpt:+Language+model+for+dialogue%2C+2024 manually and check the results.
        -> Author(s): OpenAI
        -> Title:     Chatgpt: Language model for dialogue, 2024
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 26/42:
  -> INFO: Now checking 10 results for matching title: 'Perceptual coding of digital audio'
       -> INFO: All authors matched!
- Checking reference 27/42:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Diffsound: Differential sound manipulation with a few-shot supervision
  -> WARNING: No results were found through the dblp search!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Park', 'Yang', 'Park', 'Lee', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Diffsound:+Differential+sound+manipulation+with+a+few-shot+supervision manually and check the results.
        -> Author(s): Jeongseung Park, Minseon Yang, Minz Won Park, and Geonseok Lee
        -> Title:     Diffsound: Differential sound manipulation with a few-shot supervision
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 28/42:
  -> INFO: Now checking 10 results for matching title: 'Stemgen: A music generation model that listens'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/42:
  -> INFO: Now checking 10 results for matching title: 'A fast griffin-lim algorithm'
       -> INFO: All authors matched!
- Checking reference 30/42:
  -> INFO: Now checking 10 results for matching title: 'ESC: Dataset for Environmental Sound Classification'
       -> INFO: All authors matched!
- Checking reference 31/42:
  -> INFO: Now checking 10 results for matching title: 'High-resolution image synthesis with latent diffusion models'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 32/42:
  -> INFO: Now checking 1 results for matching title: 'SoundCTM: Unifying score-based and consistency models for full-band text-to-sound generation'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/42:
  -> INFO: Now checking 10 results for matching title: 'Fundamentals of auditory masking'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Scharf', '1971']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Fundamentals+of+auditory+masking manually and check the results.
        -> Author(s): B Scharf
        -> Title:     Fundamentals of auditory masking
        -> Year:      1971
     -> Manual search was skipped by the user.
- Checking reference 34/42:
  -> INFO: Now checking 2 results for matching title: 'Moûsai: Text-to-music generation with long-context latent diffusion.'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Schneider', 'Kamal', 'Jin', 'Schölkopf', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Moûsai:+Text-to-music+generation+with+long-context+latent+diffusion. manually and check the results.
        -> Author(s): Flavio Schneider, Ojasv Kamal, Zhijing Jin, and Bernhard Schölkopf
        -> Title:     Moûsai: Text-to-music generation with long-context latent diffusion.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 35/42:
  -> INFO: Now checking 10 results for matching title: 'A robust hybrid feedback active noise cancellation headset'
       -> INFO: All authors matched!
       -> WARNING: Year (2003) does not match expected year (2005)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 36/42:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: pyloudnorm: A simple yet flexible loudness meter in python
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Steinmetz', 'Reiss', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=pyloudnorm:+A+simple+yet+flexible+loudness+meter+in+python manually and check the results.
        -> Author(s): Christian J  Steinmetz and Joshua D  Reiss
        -> Title:     pyloudnorm: A simple yet flexible loudness meter in python
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 37/42:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Robust audio watermarking using perceptual masking11this work was supported by afosr under grant af/f49620-94-1-0461
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Swanson', 'Zhu', 'Tewfik', 'Boney', '1998']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Robust+audio+watermarking+using+perceptual+masking11this+work+was+supported+by+afosr+under+grant+af/f49620-94-1-0461 manually and check the results.
        -> Author(s): Mitchell D Swanson, Bin Zhu, Ahmed H Tewfik, and Laurence Boney
        -> Title:     Robust audio watermarking using perceptual masking11this work was supported by afosr under grant af/f49620-94-1-0461
        -> Year:      1998
     -> Manual search was skipped by the user.
- Checking reference 38/42:
  -> INFO: Now checking 1 results for matching title: 'Audit: Audio editing by following instructions with latent diffusion models.'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wang', 'Ju', 'Tan', 'He', 'Wu', 'Bian', 'Zhao', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Audit:+Audio+editing+by+following+instructions+with+latent+diffusion+models. manually and check the results.
        -> Author(s): Yuancheng Wang, Zeqian Ju, Xu Tan, Lei He, Zhizheng Wu, Jiang Bian, and Sheng Zhao
        -> Title:     Audit: Audio editing by following instructions with latent diffusion models.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 39/42:
  -> INFO: Now checking 10 results for matching title: 'Music controlnet: Multiple time-varying controls for music generation'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 40/42:
  -> INFO: Now checking 1 results for matching title: 'Uni-paint: A unified framework for multimodal image inpainting with pretrained diffusion model'
       -> INFO: All authors matched!
- Checking reference 41/42:
  -> INFO: Now checking 1 results for matching title: 'Acoustic information masking effects of natural sounds on traffic noise based on psychological health in open urban spaces'
       -> INFO: All authors matched!
- Checking reference 42/42:
  -> INFO: Now checking 5 results for matching title: 'Musicmagus: Zero-shot text-to-music editing via diffusion models.'
  -> WARNING: None of the 5 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Ikemiya', 'Xia', 'Murata', 'Martínez-Ramírez', 'Liao', 'Mitsufuji', 'Dixon', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Musicmagus:+Zero-shot+text-to-music+editing+via+diffusion+models. manually and check the results.
        -> Author(s): Yixiao Zhang, Yukara Ikemiya, Gus Xia, Naoki Murata, Marco A  Martínez-Ramírez, Wei-Hsiang Liao, Yuki Mitsufuji, and Simon Dixon
        -> Title:     Musicmagus: Zero-shot text-to-music editing via diffusion models.
        -> Year:      2024
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 4: latent state zt−1 is computed as:
-> Invalid unicode use found on p. 4: p(zt−1 | zt, exNoise, Ctext) = N
-> Invalid unicode use found on p. 4: zt−1; µ(zt, ϵθ(zt, t, exNoise, Ctext)), σ2
-> Invalid unicode use found on p. 4: exMid = xMid ⊙(1 −M) ∈[0, 255]W ×H×1.
-> Invalid unicode use found on p. 5: Music)+ SUM(max[(TMask −S′
-> Invalid unicode use found on p. 5: of the music signal in the optimization. SUM(max[(TMask −S′
-> Invalid unicode use found on p. 5: AMusic = ISTFT(Griffin-Lim(Mel−1(S′
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Bracket content ['0', ' 255'] on p. 4 could not be matched to a reference.
   -> Sentence:  Once the mel-spectrogram is obtained, its amplitude values are mapped to grayscale pixel intensities in the range
[0, 255]
-> Warning: Bracket content ['0', ' 255'] on p. 4 could not be matched to a reference.
   -> Sentence:  This process yields a detailed grayscale melspectrogram plot, denoted as xNoise ∈[0, 255]W ×H×1, where the last 
dimension represents a single grayscale channel
-> Warning: Bracket content ['0', ' 255'] on p. 5 could not be matched to a reference.
   -> Sentence:  The masked image can be calculated as exNoise = xNoise ⊙M ∈[0, 255]W ×H×1, where ⊙represents element-wise 
multiplication
-> Warning: Bracket content ['0', ' 255'] on p. 5 could not be matched to a reference.
   -> Sentence:  The outpainted region of the xMid aligns the rhythmic patterns with the remaining noise content, leading us to 
invert the mask M to let the model inpaint on the area that represents the higher energy components of the noise: exMid = xMid ⊙(1
−M) ∈[0, 255]W ×H×1
-> Warning: Numeric reference range couldn't be parsed as Integers: ['(TMask −S′ Music) ⊙M', ' 0']
-> Warning: Numeric reference range couldn't be parsed as Integers: ['(TMask −S′ Music) ⊙M', ' 0']
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 344 sentences on 10 pages -> Avg. of 39.22222222222222 sentences per page
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
  // LLM calling counter = 1
  => WARNING: A Syntax Error occured during parsing: invalid syntax. Perhaps you forgot a comma? (<string>, line 1)
     Structurally parsing response as string: [(" However, while recent advances in music generation-particularly those based on mel-spectrogram representations in the frequency domain [5, 34, 18, 13, 38, 39, 42, 16]-have demonstrated remarkable progress, most existing models are trained to generate music from clean, structured inputs such as text prompts or orderly music excerpts", True, "not enough information"), (" AudioLDM2 [13] proposes a unified "language of audio" (LOA) representation, using GPT-2 to bridge multiple modalities and guiding generation with a latent diffusion model", True, "supports"), (" Many approaches adopt a vision-inspired paradigm by converting audio into 2D representations such as mel-spectrograms, enabling the application of powerful image editing techniques to audio [5, 34, 18, 13, 38, 39, 42, 16]", False, "not enough information")]
  -> Warning: The LLM response has not 3 values per sentence;                 len(response_splitted) % 3 = 1
  -> LLM list extracted as follows:
[['not enough information")', '16', 'False'], ['not enough information")', '16', 'False'], ['not enough information")', '16', 'False'], ['not enough information")', '16', 'False'], ['not enough information")', '16', 'False'], ['not enough information")', '16', 'False'], ['not enough information")', '16', 'False'], ['not enough information")', '16', 'False'], ['not enough information")', '16', 'False']]
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
-> Missing an abstract for reference with index 40 (Ref. ID = 41); Skipping LLM check...
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
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
  -> Found 2 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 28 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 11
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 12
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 13
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 14
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 15
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\31 BNMusic Blending Environmental Noises\PAU_results.md
```