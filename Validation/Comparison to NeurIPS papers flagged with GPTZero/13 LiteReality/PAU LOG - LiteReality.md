
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\13 LiteReality\LiteReality Graphics-Ready 3D Scene Reconstruction from RGB-D Scans.pdf"
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
- Found following heading '3 - Methodology' on page 4
- Found following heading '4 - Experiments and Results' on page 7
- Found following heading '5 - Conclusion' on page 9
=> Found references/literature section on page 10
- Found first appendix 'A - Outline' on page 15
- Found following appendix 'B - LiteReality Database' on page 15
- Found following appendix 'C - Benchmarking Details' on page 16
- Found following appendix 'D - More on Methodologies' on page 19
- Found following appendix 'E - More Results' on page 21
- Found following appendix 'F - Application of LiteReality' on page 25
- Found following appendix 'G - Limitations and Future Work' on page 25
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 15
All found references: 66
-> Warning: Malformed author string: 'OpenAI'
-> Warning: Could not parse year in reference 'Jeremy Schwartz and Esther Alter. Threedworld simulation environment.'!
-> Warning: Could not parse year in reference 'Sketchfab. 3d models and assets.'!
-> Warning: Malformed author string: 'Sketchfab'
-> Warning: Could not parse year in reference 'ManyCore Research Team. Spatiallm: Large language model for spatial understanding.'!
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ... link  valid
0       1  Stefan Ainetter, Sinisa Stekovic, Friedrich Fr...  ...        None
1       2  Stefan Ainetter, Sinisa Stekovic, Friedrich Fr...  ...        None
2       3  Armen Avetisyan, Manuel Dahnert, Angela Dai, M...  ...        None
3       4  Armen Avetisyan, Angela Dai, and Matthias Nießner  ...        None
4       5  Armen Avetisyan, Tatiana Khanova, Christopher ...  ...        None
..    ...                                                ...  ...  ...    ...
61     62  Yue Yang, Fan-Yun Sun, Luca Weihs, Eli VanderB...  ...        None
62     63  Kaixin Yao, Longwen Zhang, Xinhao Yan, Yan Zen...  ...        None
63     64  Yu-Ying Yeh, Zhengqin Li, Yannick Hold-Geoffro...  ...        None
64     65  Huangyue Yu, Baoxiong Jia, Yixin Chen, Yandan ...  ...        None
65     66  Shangzhan Zhang, Sida Peng, Tao Xu, Yuanbo Yan...  ...        None

[66 rows x 10 columns]
- Checking reference 1/66:
  -> INFO: Now checking 4 results for matching title: 'Automatically annotating indoor images with cad models via rgb-d scans'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/66:
  -> INFO: Now checking 1 results for matching title: 'HOC-Search: Efficient CAD model and pose retrieval from RGB-D scans'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 3/66:
  -> INFO: Now checking 3 results for matching title: 'Scan2CAD: Learning CAD model alignment in RGB-D scans'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 4/66:
  -> INFO: Now checking 1 results for matching title: 'End-to-end cad model retrieval and 9dof alignment in 3d scans'
       -> INFO: All authors matched!
- Checking reference 5/66:
  -> INFO: Now checking 1 results for matching title: 'Scenecad: Predicting object alignments and layouts in rgb-d scans'
       -> INFO: All authors matched!
- Checking reference 6/66:
  -> INFO: Now checking 1 results for matching title: 'Scenescript: Reconstructing scenes with an autoregressive structured language model'
       -> INFO: All authors matched!
- Checking reference 7/66:
  -> INFO: Now checking 6 results for matching title: 'Mip-nerf: A multiscale representation for anti-aliasing neural radiance fields'
       -> INFO: All authors matched!
- Checking reference 8/66:
  -> INFO: Now checking 10 results for matching title: 'Shapenet: An information-rich 3d model repository'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 9/66:
  -> INFO: Now checking 6 results for matching title: 'Scannet: Richly-annotated 3d reconstructions of indoor scenes'
       -> INFO: All authors matched!
- Checking reference 10/66:
  -> INFO: Now checking 1 results for matching title: 'Automated creation of digital cousins for robust policy learning'
       -> INFO: All authors matched!
- Checking reference 11/66:
  -> INFO: Now checking 1 results for matching title: 'RoboTHOR: An Open Simulation-to-Real Embodied AI Platform'
       -> INFO: All authors matched!
- Checking reference 12/66:
  -> INFO: Now checking 1 results for matching title: 'Phone2proc: Bringing robust robots into our chaotic world'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 5)
                   Unmatched authors = 'Weihs'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 13/66:
  -> INFO: Now checking 10 results for matching title: 'ProcTHOR: Large-Scale Embodied AI Using Procedural Generation'
       -> INFO: All authors matched!
- Checking reference 14/66:
  -> INFO: Now checking 3 results for matching title: 'Make-it-real: Unleashing large multimodal model for painting 3d objects with realistic materials'
       -> INFO: All authors matched!
- Checking reference 15/66:
  -> INFO: Now checking 10 results for matching title: '3d-future: 3d furniture shape with texture'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/66:
  -> INFO: Now checking 1 results for matching title: 'Diffcad: Weakly-supervised probabilistic cad model retrieval and alignment from an rgb image'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/66:
  -> INFO: Now checking 10 results for matching title: 'Roca: Robust cad model retrieval and alignment from a single image'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 18/66:
  -> INFO: Now checking 10 results for matching title: 'Monte carlo scene search for 3d scene understanding'
       -> INFO: All authors matched!
- Checking reference 19/66:
  -> INFO: Now checking 6 results for matching title: 'Cooperative holistic scene understanding: Unifying 3d object, layout, and camera pose estimation'
       -> INFO: All authors matched!
- Checking reference 20/66:
  -> INFO: Now checking 10 results for matching title: 'Holistic 3d scene parsing and reconstruction from a single rgb image'
       -> INFO: All authors matched!
- Checking reference 21/66:
  -> INFO: Now checking 10 results for matching title: 'Roomplan: 3d parametric room representation'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 994 results for matching title: 'Roomplan: 3d parametric room representation'
  -> WARNING: None of the 994 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Roomplan:+3d+parametric+room+representation manually and check the results.
        -> Author(s): Apple Inc
        -> Title:     Roomplan: 3d parametric room representation
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 22/66:
  -> INFO: Now checking 4 results for matching title: 'Im2cad'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
       -> INFO: All authors matched!
- Checking reference 23/66:
  -> INFO: Now checking 10 results for matching title: 'Efficient 3d gaussian splatting for real-time neural rendering'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Kerbl', 'Müller', 'Favaro', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Efficient+3d+gaussian+splatting+for+real-time+neural+rendering manually and check the results.
        -> Author(s): Bernd Kerbl, Thomas Müller, and Paolo Favaro
        -> Title:     Efficient 3d gaussian splatting for real-time neural rendering
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 24/66:
  -> INFO: Now checking 10 results for matching title: 'Matching real-world material appearance'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Khungurn', 'Adelson', 'Dorsey', 'Rushmeier', '2015']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Matching+real-world+material+appearance manually and check the results.
        -> Author(s): Punchana Khungurn, Edward H  Adelson, Julie Dorsey, and Holly Rushmeier
        -> Title:     Matching real-world material appearance
        -> Year:      2015
     -> Manual search was skipped by the user.
- Checking reference 25/66:
  -> INFO: Now checking 10 results for matching title: 'Segment anything'
       -> INFO: All authors matched!
- Checking reference 26/66:
  -> INFO: Now checking 2 results for matching title: 'AI2-THOR: An Interactive 3D Environment for Visual AI'
       -> WARNING: Not all 13 authors from the found ref. were matched (only 10)
                   Unmatched authors = 'Deitke, Ehsani, Kembhavi'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 27/66:
  -> INFO: Now checking 1 results for matching title: 'Mask2cad: 3d shape prediction by learning to segment and retrieve'
       -> INFO: All authors matched!
- Checking reference 28/66:
  -> INFO: Now checking 1 results for matching title: 'Sparc: Sparse render-and-compare for cad model alignment in a single rgb image'
       -> INFO: All authors matched!
- Checking reference 29/66:
  -> INFO: Now checking 1 results for matching title: 'Fastcad: Real-time cad retrieval and alignment from scans and videos'
       -> INFO: All authors matched!
- Checking reference 30/66:
  -> INFO: Now checking 1 results for matching title: 'FastCAD: Real-time CAD retrieval and alignment from scans and videos'
       -> INFO: All authors matched!
- Checking reference 31/66:
  -> INFO: Now checking 10 results for matching title: 'Cubify anything: Scaling indoor 3d object detection'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 32/66:
  -> INFO: Now checking 1 results for matching title: 'End-to-end procedural material capture with proxy-free mixed-integer optimization'
       -> INFO: All authors matched!
- Checking reference 33/66:
  -> INFO: Now checking 1 results for matching title: 'BEHAVIOR-1k: A benchmark for embodied AI with 1,000 everyday activities and realistic simulation'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/66:
  -> INFO: Now checking 2 results for matching title: 'Odam: Object detection, association, and mapping using posed rgb video'
       -> INFO: All authors matched!
- Checking reference 35/66:
  -> INFO: Now checking 10 results for matching title: 'Deeproom: 3d room layout and pose estimation from a single image'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Deeproom: 3d room layout and pose estimation from a single image'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deeproom:+3d+room+layout+and+pose+estimation+from+a+single+image manually and check the results.
        -> Author(s): Qiang Li, Jian Xiao, Myungjin Kim, Yineng Chen, and Liang Xie
        -> Title:     Deeproom: 3d room layout and pose estimation from a single image
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 36/66:
  -> INFO: Now checking 2 results for matching title: 'Openrooms: An open framework for photorealistic indoor scene datasets'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 10)
                   Unmatched authors = 'Havsan'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 37/66:
  -> INFO: Now checking 10 results for matching title: 'Material palette: Extraction of materials from a single image'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 38/66:
  -> INFO: Now checking 1 results for matching title: 'Total-decom: Decomposed 3d scene reconstruction with minimal interaction'
       -> INFO: All authors matched!
- Checking reference 39/66:
  -> INFO: Now checking 10 results for matching title: 'Vid2cad: Cad model alignment using multi-view constraints from videos'
       -> INFO: All authors matched!
- Checking reference 40/66:
  -> INFO: Now checking 10 results for matching title: 'Vid2CAD: CAD model alignment using multi-view constraints from videos'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 41/66:
  -> INFO: Now checking 3 results for matching title: 'Cad-estate: Large-scale cad model annotation in rgb videos'
       -> INFO: All authors matched!
- Checking reference 42/66:
  -> INFO: Now checking 10 results for matching title: 'Nerf: Representing scenes as neural radiance fields for view synthesis'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 4 results for matching title: 'Nerf: Representing scenes as neural radiance fields for view synthesis'
  -> WARNING: None of the 4 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Nerf:+Representing+scenes+as+neural+radiance+fields+for+view+synthesis manually and check the results.
        -> Author(s): Ben Mildenhall, Pratul P Srinivasan, Matthew Tancik, Jonathan T Barron, Ravi Ramamoorthi, and Ren Ng
        -> Title:     Nerf: Representing scenes as neural radiance fields for view synthesis
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 43/66:
  -> INFO: Now checking 10 results for matching title: 'Indoor scan2bim: Building information models of house interiors'
       -> INFO: All authors matched!
- Checking reference 44/66:
  -> INFO: Now checking 1 results for matching title: 'Total3dunderstanding: Joint layout, object pose and mesh reconstruction for indoor scenes from a single image'
       -> INFO: All authors matched!
- Checking reference 45/66:
  -> INFO: Now checking 10 results for matching title: 'Gpt-4 technical report'
       -> INFO: All authors matched!
- Checking reference 46/66:
  -> INFO: Now checking 10 results for matching title: 'Dinov2: Learning robust visual features without supervision'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 47/66:
  -> INFO: Now checking 2 results for matching title: 'Photoshape: Photorealistic materials for large-scale shape collections'
  -> WARNING: None of the 2 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Photoshape: Photorealistic materials for large-scale shape collections'
  -> WARNING: None of the 2 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Photoshape:+Photorealistic+materials+for+large-scale+shape+collections manually and check the results.
        -> Author(s): Keunhong Park, Konstantinos Rematas, Ali Farhadi, and Steven M  Seitz
        -> Title:     Photoshape: Photorealistic materials for large-scale shape collections
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 48/66:
  -> INFO: Now checking 10 results for matching title: 'Virtualhome: Simulating household activities via programs'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Boben, Wang, Fidler'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 49/66:
  -> INFO: Now checking 10 results for matching title: 'Habitat 3'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 1 results for matching title: 'Habitat 3'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Habitat+3 manually and check the results.
        -> Author(s): Xavier Puig, Eric Undersander, Andrew Szot, Mikael Dallaire Cote, Tsung-Yen Yang, Ruslan Partsey, Ruta Desai, Alexander William Clegg, Michal Hlavac, So Yeon Min, Vladimír Vondruš, Theophile Gervet, Vincent-Pierre Berges, John M  Turner, Oleksandr Maksymets, Zsolt Kira, Mrinal Kalakrishnan, Jitendra Malik, Devendra Singh Chaplot, Unnat Jain, Dhruv Batra, Akshara Rai, and Roozbeh Mottaghi
        -> Title:     Habitat 3
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 50/66:
  -> Checking if provided link is pingable: https://github.com/threedworld-mit/tdw,
  -> INFO: Now checking 10 results for matching title: 'Threedworld simulation environment'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 11 results for matching title: 'Threedworld simulation environment'
  -> WARNING: None of the 11 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Threedworld+simulation+environment manually and check the results.
        -> Author(s): Jeremy Schwartz and Esther Alter
        -> Title:     Threedworld simulation environment
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 51/66:
  -> INFO: Now checking 10 results for matching title: 'Structure-from-motion revisited'
       -> INFO: All authors matched!
- Checking reference 52/66:
  -> INFO: Now checking 10 results for matching title: 'Match: Differentiable material graphs for procedural material capture'
  -> WARNING: None of the 10 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Shi', 'Li', 'Hašan', 'Sunkavalli', 'Boubekeur', 'Mech', 'Matusik', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Match:+Differentiable+material+graphs+for+procedural+material+capture manually and check the results.
        -> Author(s): Liang Shi, Beichen Li, Miloš Hašan, Kalyan Sunkavalli, Tamy Boubekeur, Radomir Mech, and Wojciech Matusik
        -> Title:     Match: Differentiable material graphs for procedural material capture
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 53/66:
  -> Checking if provided link is pingable: https://sketchfab.com/.
  -> INFO: Now checking 10 results for matching title: '3d models and assets'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Sketchfab', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://sketchfab.com/. manually and check the results.
        -> Author(s): Sketchfab
        -> Title:     3d models and assets
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 54/66:
  -> INFO: Now checking 1 results for matching title: 'Efm3d: A benchmark for measuring progress towards 3d egocentric foundation models'
       -> INFO: All authors matched!
- Checking reference 55/66:
  -> Checking if provided link is pingable: https://github.com/manycore-research/SpatialLM,
  -> INFO: Now checking 10 results for matching title: 'Spatiallm: Large language model for spatial understanding'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Team', '0']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Spatiallm:+Large+language+model+for+spatial+understanding manually and check the results.
        -> Author(s): ManyCore Research Team
        -> Title:     Spatiallm: Large language model for spatial understanding
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 56/66:
  -> INFO: Now checking 1 results for matching title: 'Raytran: 3d pose estimation and shape reconstruction of multiple objects from videos with ray-traced transformers'
       -> INFO: All authors matched!
- Checking reference 57/66:
  -> INFO: Now checking 10 results for matching title: 'DISN: Deep implicit surface network for high-quality single-view 3d reconstruction'
       -> WARNING: Not all 5 authors from the found ref. were matched (only 4)
                   Unmatched authors = 'Měch'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 58/66:
  -> INFO: Now checking 10 results for matching title: 'Accurate instance-level CAD model retrieval in a large-scale database'
       -> INFO: All authors matched!
- Checking reference 59/66:
  -> INFO: Now checking 10 results for matching title: 'Visualsfm: A visual structure-from-motion system.'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Wu', '2011']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Visualsfm:+A+visual+structure-from-motion+system. manually and check the results.
        -> Author(s): Changchang Wu
        -> Title:     Visualsfm: A visual structure-from-motion system.
        -> Year:      2011
     -> Manual search was skipped by the user.
- Checking reference 60/66:
  -> INFO: Now checking 1 results for matching title: 'Psdr-room: Single photo to scene using differentiable rendering'
       -> INFO: All authors matched!
- Checking reference 61/66:
  -> INFO: Now checking 4 results for matching title: 'Set-of-mark prompting unleashes extraordinary visual grounding in gpt-4v.'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yang', 'Zhang', 'Li', 'Zou', 'Li', 'Gao', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Set-of-mark+prompting+unleashes+extraordinary+visual+grounding+in+gpt-4v. manually and check the results.
        -> Author(s): Jianwei Yang, Hao Zhang, Feng Li, Xueyan Zou, Chunyuan Li, and Jianfeng Gao
        -> Title:     Set-of-mark prompting unleashes extraordinary visual grounding in gpt-4v.
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 62/66:
  -> INFO: Now checking 9 results for matching title: 'Holodeck: Language guided generation of 3d embodied ai environments'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 63/66:
  -> INFO: Now checking 5 results for matching title: 'Cast: Component-aligned 3d scene reconstruction from an rgb image'
       -> INFO: All authors matched!
- Checking reference 64/66:
  -> INFO: Now checking 1 results for matching title: 'Photoscene: Photorealistic material and lighting transfer for indoor scenes'
       -> INFO: All authors matched!
- Checking reference 65/66:
  -> INFO: Now checking 1 results for matching title: 'Metascenes: Towards automated replica creation for real-world 3d scans'
       -> INFO: All authors matched!
- Checking reference 66/66:
  -> INFO: Now checking 1 results for matching title: 'Mapa: Text-driven photorealistic material painting for 3d shapes'
       -> INFO: All authors matched!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 5: T −
-> Invalid unicode use found on p. 16: b∈B ∥a −b∥1 + 1
-> Invalid unicode use found on p. 16: a∈A ∥b −a∥1
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 347 sentences on 10 pages -> Avg. of 39.55555555555556 sentences per page
-> Warning: Reference '30' never used in the document's text.
-> Warning: Reference '40' never used in the document's text.
-> Warning: Reference '57' never used in the document's text.
-> Warning: Reference '61' never used in the document's text.
---
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
-> WARNING: Reference with index 39 (Ref. ID = 40) has no associated sentence!
-> Missing an abstract for reference with index 40 (Ref. ID = 41); Skipping LLM check...
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
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
-> WARNING: Reference with index 56 (Ref. ID = 57) has no associated sentence!
-> Missing an abstract for reference with index 57 (Ref. ID = 58); Skipping LLM check...
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
-> Missing an abstract for reference with index 65 (Ref. ID = 66); Skipping LLM check...
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
  -> Found 3 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 0 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 8 matches in this ranking!
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\13 LiteReality\PAU_results.md
```