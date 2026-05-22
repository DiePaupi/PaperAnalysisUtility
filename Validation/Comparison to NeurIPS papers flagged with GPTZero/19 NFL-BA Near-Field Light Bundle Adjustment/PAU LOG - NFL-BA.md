
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\19 NFL-BA Near-Field Light Bundle Adjustment\NFL-BA Near-Field Light Bundle Adjustment for SLAM in Dynamic Lighting.pdf"
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
- Found following heading '3 - Background' on page 3
- Found following heading '4 - Near-Field Light Bundle Adjustment' on page 4
- Found following heading '5 - Evaluation' on page 6
- Found following heading '6 - Conclusions' on page 9
=> Found references/literature section on page 10
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 13
All found references: 62
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ... link  valid
0       1    Hatem Alismail, Brett Browning, and Simon Lucey  ...        None
1       2  Víctor M Batlle, José MM Montiel, Pascal Fua, ...  ...        None
2       3  Taylor L Bobrow, Mayank Golhar, Rohan Vijayan,...  ...        None
3       4  Mark Boss, Raphael Braun, Varun Jampani, Jonat...  ...        None
4       5  C  Campos, R  Elvira, J  J  G  Rodríguez, J  M...  ...        None
..    ...                                                ...  ...  ...    ...
57     58                 L  Zhou, R  Klette, and K  Scheibe  ...        None
58     59  A  Zhu, Z  Zhang, H  Su, L  Li, G  Wang, and X...  ...        None
59     60  Lingting Zhu, Zhao Wang, Jiahao Cui, Zhenchao ...  ...        None
60     61  Z  Zhu, T  Yu, X  Zhang, J  Li, Y  Zhang, and ...  ...        None
61     62  Zihan Zhu, Songyou Peng, Viktor Larsson, Zhaop...  ...        None

[62 rows x 10 columns]
- Checking reference 1/62:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 10 results for matching title: 'Photometric bundle adjustment for vision-based slam.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 6 results for matching title: 'Photometric bundle adjustment for vision-based slam.'
       -> INFO: All authors matched!
- Checking reference 2/62:
  -> INFO: Now checking 1 results for matching title: 'LightNeuS: Neural surface reconstruction in endoscopy using illumination decline'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Tard'os'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/62:
  -> INFO: Now checking 10 results for matching title: 'Colonoscopy 3d video dataset with paired depth from 2d-3d registration'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/62:
  -> INFO: Now checking 10 results for matching title: 'Nerd: Neural reflectance decomposition from image collections'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 5/62:
  -> INFO: Now checking 1 results for matching title: 'Orb-slam3: An accurate open-source library for visual, visual-inertial, and multi-map slam'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Orb-slam3: An accurate open-source library for visual, visual-inertial, and multi-map slam'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Orb-slam3:+An+accurate+open-source+library+for+visual%2C+visual-inertial%2C+and+multi-map+slam manually and check the results.
        -> Author(s): C  Campos, R  Elvira, J  J  G  Rodríguez, J  M  M  Montiel, and J  D  Tardós
        -> Title:     Orb-slam3: An accurate open-source library for visual, visual-inertial, and multi-map slam
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 6/62:
  -> INFO: Now checking 10 results for matching title: 'Neural topological slam for visual navigation'
       -> INFO: All authors matched!
- Checking reference 7/62:
  -> INFO: Now checking 5 results for matching title: 'Vcr-gaus: View consistent depth-normal regularizer for gaussian surface reconstruction'
       -> INFO: All authors matched!
- Checking reference 8/62:
  -> INFO: Now checking 2 results for matching title: 'Endodac: Efficient adapting foundation model for self-supervised depth estimation from any endoscopic camera'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Hoque, Bai, Wang, Ren'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/62:
  -> INFO: Now checking 10 results for matching title: 'Compact 3d gaussian splatting for dense visual slam.'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 20 results for matching title: 'Compact 3d gaussian splatting for dense visual slam.'
  -> WARNING: None of the 20 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Compact+3d+gaussian+splatting+for+dense+visual+slam. manually and check the results.
        -> Author(s): Tianchen Deng, Yaohui Chen, Leyan Zhang, Jianfei Yang, Shenghai Yuan, Jiuming Liu, Danwei Wang, Hesheng Wang, and Weidong Chen
        -> Title:     Compact 3d gaussian splatting for dense visual slam.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 10/62:
  -> INFO: Now checking 10 results for matching title: 'Direct sparse odometry'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/62:
  -> INFO: Now checking 1 results for matching title: 'Ekf monocular slam with relocalization for laparoscopic sequences'
       -> INFO: All authors matched!
- Checking reference 12/62:
  -> INFO: Now checking 10 results for matching title: 'Free-SurGS: SfM-Free 3D Gaussian Splatting for Surgical Scene Reconstruction'
       -> INFO: All authors matched!
- Checking reference 13/62:
  -> INFO: Now checking 10 results for matching title: 'Multiple View Geometry in Computer Vision'
       -> INFO: All authors matched!
       -> WARNING: Year (2001) does not match expected year (2003)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 14/62:
  -> INFO: Now checking 2 results for matching title: 'Online 3D reconstruction and dense tracking in endoscopic videos'
       -> INFO: All authors matched!
- Checking reference 15/62:
  -> INFO: Now checking 1 results for matching title: 'Photo-slam: Real-time simultaneous localization and photorealistic mapping for monocular, stereo, and rgb-d cameras'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/62:
  -> INFO: Now checking 2 results for matching title: 'Endo-4DGS: Endoscopic Monocular Scene Reconstruction with 4D Gaussian Splatting'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 6)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/62:
  -> INFO: Now checking 10 results for matching title: 'Endometric: Near-light metric scale monocular slam'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Tard'os'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/62:
  -> INFO: Now checking 10 results for matching title: 'Reconstructing shape from shading images under point light source illumination'
       -> INFO: All authors matched!
- Checking reference 19/62:
  -> INFO: Now checking 10 results for matching title: '3d gaussian splatting for real-time radiance field rendering'
       -> INFO: All authors matched!
- Checking reference 20/62:
  -> INFO: Now checking 10 results for matching title: 'Photometric stereo with near-field lighting using neural networks'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Lichy', 'authors', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Photometric+stereo+with+near-field+lighting+using+neural+networks manually and check the results.
        -> Author(s): C  Lichy and Other authors
        -> Title:     Photometric stereo with near-field lighting using neural networks
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 21/62:
  -> INFO: Now checking 10 results for matching title: 'Fast light-weight near-field photometric stereo'
       -> INFO: All authors matched!
- Checking reference 22/62:
  -> INFO: Now checking 10 results for matching title: 'Endogaussian: Gaussian splatting for deformable surgical scene reconstruction'
       -> INFO: All authors matched!
- Checking reference 23/62:
  -> INFO: Now checking 10 results for matching title: 'Monogs: Monocular gaussian splatting for robust slam'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1000 results for matching title: 'Monogs: Monocular gaussian splatting for robust slam'
  -> WARNING: None of the 1000 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Monogs:+Monocular+gaussian+splatting+for+robust+slam manually and check the results.
        -> Author(s): J  Lu, Y  Zhang, and X  Chen
        -> Title:     Monogs: Monocular gaussian splatting for robust slam
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 24/62:
  -> INFO: Now checking 1 results for matching title: 'Colon10k: A benchmark for place recognition in colonoscopy'
       -> INFO: All authors matched!
- Checking reference 25/62:
  -> INFO: Now checking 1 results for matching title: 'Realtime 3d reconstruction of colonoscopic surfaces for determining missing regions'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Realtime 3d reconstruction of colonoscopic surfaces for determining missing regions'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Realtime+3d+reconstruction+of+colonoscopic+surfaces+for+determining+missing+regions manually and check the results.
        -> Author(s): Ruibin Ma, Rui Wang, Stephen Pizer, Julian Rosenman, Sarah K McGill, and Jan-Michael Frahm
        -> Title:     Realtime 3d reconstruction of colonoscopic surfaces for determining missing regions
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 26/62:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Unscented kalman filter for visual slam with photometric calibration
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Martínez-Cantín', 'Tardós', '2016']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Unscented+kalman+filter+for+visual+slam+with+photometric+calibration manually and check the results.
        -> Author(s): R  Martínez-Cantín and J  D  Tardós
        -> Title:     Unscented kalman filter for visual slam with photometric calibration
        -> Year:      2016
     -> Manual search was skipped by the user.
- Checking reference 27/62:
  -> INFO: Now checking 10 results for matching title: 'Gaussian splatting slam'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 28/62:
  -> INFO: Now checking 10 results for matching title: 'Nerf: representing scenes as neural radiance fields for view synthesis'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Mildenhall', 'Srinivasan', 'Tancik', 'Barron', 'Ramamoorthi', 'Ng', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Nerf:+representing+scenes+as+neural+radiance+fields+for+view+synthesis manually and check the results.
        -> Author(s): Ben Mildenhall, Pratul P  Srinivasan, Matthew Tancik, Jonathan T  Barron, Ravi Ramamoorthi, and Ren Ng
        -> Title:     Nerf: representing scenes as neural radiance fields for view synthesis
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 29/62:
  -> INFO: Now checking 1 results for matching title: 'Topological slam in colonoscopies leveraging deep features and topological priors'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Tard'os'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/62:
  -> INFO: Now checking 7 results for matching title: 'Orb-slam: A versatile and accurate monocular slam system'
       -> INFO: All authors matched!
- Checking reference 31/62:
  -> INFO: Now checking 10 results for matching title: 'DINOv2: Learning robust visual features without supervision'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 32/62:
  -> INFO: Now checking 2 results for matching title: 'Endoslam dataset and an unsupervised monocular visual odometry and depth estimation approach for endoscopic videos'
       -> WARNING: Not all 15 authors from the found ref. were matched (only 14)
                   Unmatched authors = 'Araújo'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/62:
  -> INFO: Now checking 1 results for matching title: 'Inspection of an underwater structure using point-cloud slam with an auv and a laser scanner'
       -> INFO: All authors matched!
- Checking reference 34/62:
  -> INFO: Now checking 5 results for matching title: 'Leveraging near-field lighting for monocular depth estimation from endoscopy videos'
       -> INFO: All authors matched!
- Checking reference 35/62:
  -> INFO: Now checking 10 results for matching title: 'Nr-slam: Non-rigid monocular slam'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Rodríguez', 'Montiel', 'Tardós', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Nr-slam:+Non-rigid+monocular+slam manually and check the results.
        -> Author(s): Juan J Gómez Rodríguez, José MM Montiel, and Juan D Tardós
        -> Title:     Nr-slam: Non-rigid monocular slam
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 36/62:
  -> INFO: Now checking 9 results for matching title: 'LightDepth: single-view depth self-supervision from illumination decline'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 5)
                   Unmatched authors = 'Rodr'iguez-Puigvert, Tard'os'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 37/62:
  -> INFO: Now checking 10 results for matching title: 'Point-slam: Dense neural point cloud-based slam'
       -> INFO: All authors matched!
- Checking reference 38/62:
  -> INFO: Now checking 5 results for matching title: 'Colonnerf: Neural radiance fields for high-fidelity long-sequence colonoscopy reconstruction'
       -> INFO: All authors matched!
- Checking reference 39/62:
  -> INFO: Now checking 10 results for matching title: 'Yang'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Stoyanov', 'Mylonas', 'Deligianni', 'Darzi', '-Z', '2005']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Yang manually and check the results.
        -> Author(s): D  Stoyanov, G  Mylonas, F  Deligianni, A  Darzi, and G -Z
        -> Title:     Yang
        -> Year:      2005
     -> Manual search was skipped by the user.
- Checking reference 40/62:
  -> INFO: Now checking 1 results for matching title: 'imap: Implicit mapping and positioning in real-time'
       -> INFO: All authors matched!
- Checking reference 41/62:
  -> INFO: Now checking 10 results for matching title: 'Lightglue: Feature matching under adverse conditions'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sun', 'Kähler', 'Sattler', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Lightglue:+Feature+matching+under+adverse+conditions manually and check the results.
        -> Author(s): X  Sun, O  Kähler, and K  Sattler
        -> Title:     Lightglue: Feature matching under adverse conditions
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 42/62:
  -> INFO: Now checking 8 results for matching title: 'Droid-slam: Deep visual slam for monocular, stereo, and rgb-d cameras'
       -> INFO: All authors matched!
- Checking reference 43/62:
  -> INFO: Now checking 1 results for matching title: 'How nerfs and 3d gaussian splatting are reshaping slam: a survey'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Tosi', 'Zhang', 'Gong', 'Sandström', 'Mattoccia', 'Oswald', 'Poggi', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=How+nerfs+and+3d+gaussian+splatting+are+reshaping+slam:+a+survey manually and check the results.
        -> Author(s): Fabio Tosi, Youmin Zhang, Ziren Gong, Erik Sandström, Stefano Mattoccia, Martin R Oswald, and Matteo Poggi
        -> Title:     How nerfs and 3d gaussian splatting are reshaping slam: a survey
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 44/62:
  -> INFO: Now checking 1 results for matching title: 'Co-slam: Joint coordinate and sparse parametric encodings for neural real-time slam'
       -> INFO: All authors matched!
- Checking reference 45/62:
  -> INFO: Now checking 1 results for matching title: 'EndoGSLAM: Real-Time Dense Reconstruction and Tracking in Endoscopic Surgeries using Gaussian Splatting'
       -> INFO: All authors matched!
- Checking reference 46/62:
  -> INFO: Now checking 1 results for matching title: 'A surface-normal based neural framework for colonoscopy reconstruction'
       -> INFO: All authors matched!
- Checking reference 47/62:
  -> INFO: Now checking 10 results for matching title: 'Surface reconstruction from 3d gaussian splatting via local structural hints'
       -> INFO: All authors matched!
- Checking reference 48/62:
  -> INFO: Now checking 10 results for matching title: 'Gs-slam: Dense visual slam with 3d gaussian splatting'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 49/62:
  -> INFO: Now checking 1 results for matching title: 'Depth anything: Unleashing the power of large-scale unlabeled data'
       -> INFO: All authors matched!
- Checking reference 50/62:
  -> INFO: Now checking 2 results for matching title: 'Deform3DGS: Flexible Deformation for Fast Surgical Scene Reconstruction with Gaussian Splatting'
       -> INFO: All authors matched!
- Checking reference 51/62:
  -> INFO: Now checking 10 results for matching title: '3d gaussian splatting with deferred reflection'
       -> INFO: All authors matched!
- Checking reference 52/62:
  -> INFO: Now checking 10 results for matching title: 'Gaussian-slam: Photo-realistic dense slam with gaussian splatting.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yugay', 'Li', 'Gevers', 'Oswald', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Gaussian-slam:+Photo-realistic+dense+slam+with+gaussian+splatting. manually and check the results.
        -> Author(s): Vladimir Yugay, Yue Li, Theo Gevers, and Martin R  Oswald
        -> Title:     Gaussian-slam: Photo-realistic dense slam with gaussian splatting.
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 53/62:
  -> INFO: Now checking 1 results for matching title: 'Quantitative assessment of the upper airway in infants and children with subglottic stenosis'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2015)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/62:
  -> INFO: Now checking 1 results for matching title: 'The unreasonable effectiveness of deep features as a perceptual metric'
       -> INFO: All authors matched!
- Checking reference 55/62:
  -> INFO: Now checking 4 results for matching title: 'Airslam: Illumination-invariant hybrid slam'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Oswald', 'Cremers', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Airslam:+Illumination-invariant+hybrid+slam manually and check the results.
        -> Author(s): Y  Zhang, M  Oswald, and D  Cremers
        -> Title:     Airslam: Illumination-invariant hybrid slam
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 56/62:
  -> INFO: Now checking 1 results for matching title: 'Colde: a depth estimation framework for colonoscopy reconstruction'
       -> INFO: All authors matched!
- Checking reference 57/62:
  -> INFO: Now checking 10 results for matching title: 'Nerf-slam: Real-time dense monocular slam with neural radiance fields'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhi', 'Lai', 'Kundu', 'Bloesch', 'Davison', 'Zisserman', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Nerf-slam:+Real-time+dense+monocular+slam+with+neural+radiance+fields manually and check the results.
        -> Author(s): S  Zhi, J  Lai, A  Kundu, M  Bloesch, A  Davison, and A  Zisserman
        -> Title:     Nerf-slam: Real-time dense monocular slam with neural radiance fields
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 58/62:
  -> INFO: Now checking 3 results for matching title: 'A multi-image shape-from-shading framework for near-lighting perspective endoscopes'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhou', 'Klette', 'Scheibe', '2009']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+multi-image+shape-from-shading+framework+for+near-lighting+perspective+endoscopes manually and check the results.
        -> Author(s): L  Zhou, R  Klette, and K  Scheibe
        -> Title:     A multi-image shape-from-shading framework for near-lighting perspective endoscopes
        -> Year:      2009
     -> Manual search was skipped by the user.
- Checking reference 59/62:
  -> INFO: Now checking 10 results for matching title: 'Nice-slam: Neural implicit scalable encoding for slam'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Peng, Larsson, Xu, Bao, Cui, Oswald, Pollefeys'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 60/62:
  -> INFO: Now checking 10 results for matching title: 'Endogs: Deformable endoscopic tissues reconstruction with gaussian splatting'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhu', 'Wang', 'Cui', 'Jin', 'Lin', 'Yu', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Endogs:+Deformable+endoscopic+tissues+reconstruction+with+gaussian+splatting manually and check the results.
        -> Author(s): Lingting Zhu, Zhao Wang, Jiahao Cui, Zhenchao Jin, Guying Lin, and Lequan Yu
        -> Title:     Endogs: Deformable endoscopic tissues reconstruction with gaussian splatting
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 61/62:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Neuralrgb-d: Neural representations for depth estimation and scene mapping
  -> WARNING: No results were found through the dblp search!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhu', 'Yu', 'Zhang', 'Li', 'Zhang', 'Fu', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Neuralrgb-d:+Neural+representations+for+depth+estimation+and+scene+mapping manually and check the results.
        -> Author(s): Z  Zhu, T  Yu, X  Zhang, J  Li, Y  Zhang, and Y  Fu
        -> Title:     Neuralrgb-d: Neural representations for depth estimation and scene mapping
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 62/62:
  -> INFO: Now checking 10 results for matching title: 'Nicer-slam: Neural implicit scene encoding for rgb slam'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: ciαiΠi−1
-> Invalid unicode use found on p. 2: j=1(1 −αj) ,
-> Invalid unicode use found on p. 2: ziαiΠi−1
-> Invalid unicode use found on p. 2: j=1(1 −αj)
-> Invalid unicode use found on p. 3: Lren = ∥Mt ⊙( ˆC −C)∥p,
-> Invalid unicode use found on p. 3: Lgeo = ∥Mt ⊙( ˆD −D)∥p
-> Invalid unicode use found on p. 3: the volume density σi and the distance between adjacent samples δi as αi = 1 −exp(−σiδi).
-> Invalid unicode use found on p. 3: αi = αi exp(−1
-> Invalid unicode use found on p. 3: 2(p −¯µi
-> Invalid unicode use found on p. 3: −1(p −¯µi
-> Invalid unicode use found on p. 4: xp −xL
-> Invalid unicode use found on p. 4: ∥xp −xL∥,
-> Invalid unicode use found on p. 4: ∥xp −xL∥2 ,
-> Invalid unicode use found on p. 4: ρ(xi)PPS(xi)αiΠi−1
-> Invalid unicode use found on p. 4: j=1(1 −αj)
-> Invalid unicode use found on p. 4: La(xp) = 1/∥xp −xL∥2. This simplification is justified because the angular attenuation in settings
-> Invalid unicode use found on p. 5: follows [4]: n(xi) = −∇σ(xi)/∥∇σ(xi)∥. For Gaussian Splatting, we use the shortest axis of each
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 366 sentences on 10 pages -> Avg. of 41.666666666666664 sentences per page
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
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
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
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
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
-> Missing an abstract for reference with index 49 (Ref. ID = 50); Skipping LLM check...
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
-> Missing an abstract for reference with index 52 (Ref. ID = 53); Skipping LLM check...
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
-> Missing an abstract for reference with index 57 (Ref. ID = 58); Skipping LLM check...
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
  -> Warning: A parsed outlet title is empty. Skipping this one.
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
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
  -> Found 9 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 16
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 17
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 18
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 19
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━  95% 0:00:01
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 20
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\19 NFL-BA Near-Field Light Bundle Adjustment\PAU_results.md
```