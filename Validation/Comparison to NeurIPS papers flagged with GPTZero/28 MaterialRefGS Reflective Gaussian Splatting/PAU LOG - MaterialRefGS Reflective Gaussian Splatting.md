
```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\28 MaterialRefGS Reflective Gaussian Splatting\MaterialRefGS Reflective Gaussian Splatting with.pdf"
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
- Found following heading '3 - Method' on page 3
- Found following heading '4 - Experiments' on page 7
- Found following heading '5 - Conclusion' on page 10
- Found following heading '6 - Acknowledgement' on page 10
=> Found references/literature section on page 10
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 15
All found references: 72
-> Warning: Could not parse year in reference 'Daniel Gatis. Rembg: A tool to remove images background.'!
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ... link  valid
0       1  Jonathan T Barron, Ben Mildenhall, Dor Verbin,...  ...        None
1       2  Marcelo Bertalmio, Guillermo Sapiro, Vincent C...  ...        None
2       3  Sai Bi, Zexiang Xu, Kalyan Sunkavalli, Miloš H...  ...        None
3       4     Brent Burley and Walt Disney Animation Studios  ...        None
4       5           Chao Chen, Yu-Shen Liu, and Zhizhong Han  ...        None
..    ...                                                ...  ...  ...    ...
67     68  Junsheng Zhou, Baorui Ma, Wenyuan Zhang, Yi Fa...  ...        None
68     69  Junsheng Zhou, Xingyu Shi, Haichuan Song, Yi F...  ...        None
69     70  Junsheng Zhou, Jinsheng Wang, Baorui Ma, Yu-Sh...  ...        None
70     71        Junsheng Zhou, Weiqi Zhang, and Yu-Shen Liu  ...        None
71     72  Matthias Zwicker, Hanspeter Pfister, Jeroen Va...  ...        None

[72 rows x 10 columns]
- Checking reference 1/72:
  -> INFO: Now checking 8 results for matching title: 'MipNeRF 360: Unbounded anti-aliased neural radiance fields'
  -> WARNING: None of the 8 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'MipNeRF 360: Unbounded anti-aliased neural radiance fields'
  -> WARNING: None of the 2 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=MipNeRF+360:+Unbounded+anti-aliased+neural+radiance+fields manually and check the results.
        -> Author(s): Jonathan T Barron, Ben Mildenhall, Dor Verbin, Pratul P Srinivasan, and Peter Hedman
        -> Title:     MipNeRF 360: Unbounded anti-aliased neural radiance fields
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 2/72:
  -> INFO: Now checking 10 results for matching title: 'Image inpainting'
       -> INFO: All authors matched!
- Checking reference 3/72:
  -> INFO: Now checking 1 results for matching title: 'Deep Reflectance Volumes: Relightable reconstructions from multiview photometric images'
  -> WARNING: None of the 1 results matched the expected title!
  -> INFO: Now checking 3 results for matching title: 'Deep Reflectance Volumes: Relightable reconstructions from multiview photometric images'
  -> WARNING: None of the 3 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+Reflectance+Volumes:+Relightable+reconstructions+from+multiview+photometric+images manually and check the results.
        -> Author(s): Sai Bi, Zexiang Xu, Kalyan Sunkavalli, Miloš Hašan, Yannick Hold-Geoffroy, David Kriegman, and Ravi Ramamoorthi
        -> Title:     Deep Reflectance Volumes: Relightable reconstructions from multiview photometric images
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 4/72:
  -> INFO: Now checking 7 results for matching title: 'Physically-based shading at disney'
       -> WARNING: Not all 1 authors from the found ref. were matched (only 1)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 5/72:
  -> INFO: Now checking 10 results for matching title: 'NeuralTPS: Learning signed distance functions without priors from single sparse point clouds'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 6/72:
  -> INFO: Now checking 4 results for matching title: 'PGSR: Planar-based gaussian splatting for efficient and high-fidelity surface reconstruction'
       -> INFO: All authors matched!
- Checking reference 7/72:
  -> INFO: Now checking 10 results for matching title: 'MVSplat: Efficient 3D gaussian splatting from sparse multi-view images'
       -> INFO: All authors matched!
- Checking reference 8/72:
  -> INFO: Now checking 5 results for matching title: 'Improving neural implicit surfaces geometry with patch warping'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/72:
  -> INFO: Now checking 1 results for matching title: 'Kling-avatar: Grounding multimodal instructions for cascaded long-duration avatar animation synthesis'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Chen'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/72:
  -> INFO: Now checking 2 results for matching title: 'GS-ID: Illumination Decomposition on Gaussian Splatting via Diffusion Prior and Parametric Light Source Optimization'
       -> INFO: All authors matched!
- Checking reference 11/72:
  -> INFO: Now checking 2 results for matching title: 'Relightable 3d gaussians: Realistic point cloud relighting with brdf decomposition and ray tracing'
       -> WARNING: Not all 7 authors from the found ref. were matched (only 7)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/72:
  -> Checking if provided link is pingable: https://github.com/danielgatis/rembg,
  -> INFO: Now checking 10 results for matching title: 'Rembg: A tool to remove images background'
  -> WARNING: None of the 10 results matched the expected title!
  -> INFO: Now checking 2 results for matching title: 'Rembg: A tool to remove images background'
  -> WARNING: None of the 2 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Rembg:+A+tool+to+remove+images+background manually and check the results.
        -> Author(s): Daniel Gatis
        -> Title:     Rembg: A tool to remove images background
        -> Year:      0
     -> Manual search was skipped by the user.
- Checking reference 13/72:
  -> INFO: Now checking 1 results for matching title: 'Ref-NeuS: Ambiguityreduced neural implicit surface learning for multi-view reconstruction with reflection'
  -> WARNING: None of the 1 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ge', 'Hu', 'Zhao', 'Liu', 'Chen', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Ref-NeuS:+Ambiguityreduced+neural+implicit+surface+learning+for+multi-view+reconstruction+with+reflection manually and check the results.
        -> Author(s): Wenhang Ge, Tao Hu, Haoyu Zhao, Shu Liu, and Ying-Cong Chen
        -> Title:     Ref-NeuS: Ambiguityreduced neural implicit surface learning for multi-view reconstruction with reflection
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 14/72:
  -> INFO: Now checking 3 results for matching title: 'IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
       -> INFO: All authors matched!
- Checking reference 15/72:
  -> INFO: Now checking 8 results for matching title: 'SuGaR: Surface-aligned gaussian splatting for efficient 3d mesh reconstruction and high-quality mesh rendering'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/72:
  -> INFO: Now checking 2 results for matching title: 'SparseRecon: Neural implicit surface reconstruction from sparse views with feature and depth consistencies'
       -> INFO: All authors matched!
- Checking reference 17/72:
  -> INFO: Now checking 10 results for matching title: 'Binocular-Guided 3D Gaussian Splatting with View Consistency for Sparse View Synthesis'
       -> INFO: All authors matched!
- Checking reference 18/72:
  -> INFO: Now checking 10 results for matching title: '2D Gaussian Splatting for Geometrically Accurate Radiance Fields'
       -> INFO: All authors matched!
- Checking reference 19/72:
  -> INFO: Now checking 1 results for matching title: 'FatesGS: Fast and accurate sparse-view surface reconstruction using gaussian splatting with depth-feature consistency'
       -> INFO: All authors matched!
- Checking reference 20/72:
  -> INFO: Now checking 2 results for matching title: 'GaussianShader: 3D Gaussian Splatting with Shading Functions for Reflective Surfaces'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
       -> INFO: All authors matched!
- Checking reference 21/72:
  -> INFO: Now checking 4 results for matching title: 'TensoIR: Tensorial inverse rendering'
       -> INFO: All authors matched!
- Checking reference 22/72:
  -> INFO: Now checking 10 results for matching title: '3D gaussian splatting for real-time radiance field rendering'
       -> INFO: All authors matched!
- Checking reference 23/72:
  -> INFO: Now checking 1 results for matching title: 'A hierarchical 3d gaussian representation for real-time rendering of very large datasets'
       -> INFO: All authors matched!
- Checking reference 24/72:
  -> INFO: Now checking 10 results for matching title: '3D Gaussian Splatting with Deferred Reflection'
       -> INFO: All authors matched!
- Checking reference 25/72:
  -> INFO: Now checking 1 results for matching title: 'TensoSDF: Roughness-aware tensorial representation for robust geometry and material reconstruction'
       -> INFO: All authors matched!
- Checking reference 26/72:
  -> INFO: Now checking 10 results for matching title: 'Spec-NeRF: Multi-spectral neural radiance fields'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 27/72:
  -> INFO: Now checking 1 results for matching title: 'VA-GS: Enhancing the geometric representation of gaussian splatting via view alignment'
       -> INFO: All authors matched!
- Checking reference 28/72:
  -> INFO: Now checking 10 results for matching title: 'I-filtering: Implicit filtering for learning neural distance functions from 3d point clouds'
       -> INFO: All authors matched!
- Checking reference 29/72:
  -> INFO: Now checking 2 results for matching title: 'GaussianUDF: Inferring Unsigned Distance Functions through 3D Gaussian Splatting'
       -> INFO: All authors matched!
- Checking reference 30/72:
  -> INFO: Now checking 5 results for matching title: 'ENVIDR: Implicit differentiable renderer with neural environment lighting'
       -> INFO: All authors matched!
- Checking reference 31/72:
  -> INFO: Now checking 10 results for matching title: 'GS-IR: 3D Gaussian Splatting for Inverse Rendering'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 32/72:
  -> INFO: Now checking 1 results for matching title: 'Point2Sequence: Learning the Shape Representation of 3D Point Clouds with an Attention-based Sequence to Sequence Network'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 33/72:
  -> INFO: Now checking 1 results for matching title: 'NeRO: Neural geometry and brdf reconstruction of reflective objects from multiview images'
       -> INFO: All authors matched!
- Checking reference 34/72:
  -> INFO: Now checking 10 results for matching title: 'ScaffoldGS: Structured 3D gaussians for view-adaptive rendering'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Lu', 'Yu', 'Xu', 'Xiangli', 'Wang', 'Lin', 'Dai', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=ScaffoldGS:+Structured+3D+gaussians+for+view-adaptive+rendering manually and check the results.
        -> Author(s): Tao Lu, Mulin Yu, Linning Xu, Yuanbo Xiangli, Limin Wang, Dahua Lin, and Bo Dai
        -> Title:     ScaffoldGS: Structured 3D gaussians for view-adaptive rendering
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 35/72:
  -> INFO: Now checking 4 results for matching title: 'Neural-Pull: Learning signed distance function from point clouds by learning to pull space onto surface'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ma', 'Han', 'Liu', 'Zwicker', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Neural-Pull:+Learning+signed+distance+function+from+point+clouds+by+learning+to+pull+space+onto+surface manually and check the results.
        -> Author(s): Baorui Ma, Zhizhong Han, Yu-Shen Liu, and Matthias Zwicker
        -> Title:     Neural-Pull: Learning signed distance function from point clouds by learning to pull space onto surface
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 36/72:
  -> INFO: Now checking 10 results for matching title: 'NeRF: Representing scenes as neural radiance fields for view synthesis'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Mildenhall', 'Srinivasan', 'Tancik', 'Barron', 'Ramamoorthi', 'Ng', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=NeRF:+Representing+scenes+as+neural+radiance+fields+for+view+synthesis manually and check the results.
        -> Author(s): Ben Mildenhall, Pratul P Srinivasan, Matthew Tancik, Jonathan T Barron, Ravi Ramamoorthi, and Ren Ng
        -> Title:     NeRF: Representing scenes as neural radiance fields for view synthesis
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 37/72:
  -> INFO: Now checking 10 results for matching title: '3D Gaussian Ray Tracing: Fast tracing of particle scenes'
       -> INFO: All authors matched!
- Checking reference 38/72:
  -> INFO: Now checking 10 results for matching title: 'Extracting triangular 3d models, materials, and lighting from images'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 39/72:
  -> INFO: Now checking 1 results for matching title: 'Learning bijective surface parameterization for inferring signed distance functions from sparse point clouds with grid deformation'
       -> INFO: All authors matched!
- Checking reference 40/72:
  -> INFO: Now checking 3 results for matching title: 'Pointnet++: Deep hierarchical feature learning on point sets in a metric space'
       -> INFO: All authors matched!
- Checking reference 41/72:
  -> INFO: Now checking 10 results for matching title: 'LangSplat: 3d language gaussian splatting'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 42/72:
  -> INFO: Now checking 10 results for matching title: 'Sam 2: Segment anything in images and videos'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 43/72:
  -> INFO: Now checking 4 results for matching title: 'OctreeGS: Towards consistent real-time rendering with lod-structured 3d gaussians'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Ren', 'Jiang', 'Lu', 'Yu', 'Xu', 'Ni', 'Dai', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=OctreeGS:+Towards+consistent+real-time+rendering+with+lod-structured+3d+gaussians manually and check the results.
        -> Author(s): Kerui Ren, Lihan Jiang, Tao Lu, Mulin Yu, Linning Xu, Zhangkai Ni, and Bo Dai
        -> Title:     OctreeGS: Towards consistent real-time rendering with lod-structured 3d gaussians
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 44/72:
  -> INFO: Now checking 10 results for matching title: 'Physically-based rendering'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Rendering', '2015']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Physically-based+rendering manually and check the results.
        -> Author(s): Why Physically-Based Rendering
        -> Title:     Physically-based rendering
        -> Year:      2015
     -> Manual search was skipped by the user.
- Checking reference 45/72:
  -> INFO: Now checking 1 results for matching title: 'Map projections for global and continental data sets and an analysis of pixel distortion caused by reprojection'
       -> INFO: All authors matched!
- Checking reference 46/72:
  -> INFO: Now checking 1 results for matching title: '3iGS: Factorised tensorial illumination for 3d gaussian splatting'
       -> INFO: All authors matched!
- Checking reference 47/72:
  -> INFO: Now checking 10 results for matching title: 'Ref-NeRF: Structured view-dependent appearance for neural radiance fields'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/72:
  -> INFO: Now checking 1 results for matching title: 'UniSDF: Unifying neural representations for high-fidelity 3d reconstruction of complex scenes with reflections'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 49/72:
  -> INFO: Now checking 10 results for matching title: 'Image quality assessment: from error visibility to structural similarity'
       -> INFO: All authors matched!
- Checking reference 50/72:
  -> INFO: Now checking 10 results for matching title: '4d gaussian splatting for real-time dynamic scene rendering'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 51/72:
  -> INFO: Now checking 10 results for matching title: 'Sparis: Neural implicit surface reconstruction of indoor scenes from sparse views'
       -> INFO: All authors matched!
- Checking reference 52/72:
  -> INFO: Now checking 3 results for matching title: 'Snowflake point deconvolution for point cloud completion and generation with skip-transformer'
       -> INFO: All authors matched!
- Checking reference 53/72:
  -> INFO: Now checking 9 results for matching title: 'EnvGS: Modeling view-dependent appearance with environment gaussian'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 54/72:
  -> INFO: Now checking 10 results for matching title: 'HVI: A new color space for low-light image enhancement'
       -> INFO: All authors matched!
- Checking reference 55/72:
  -> INFO: Now checking 2 results for matching title: 'PSNeRF: Neural inverse rendering for multi-view photometric stereo'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Yang', 'Chen', 'Chen', 'Chen', 'Wong', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=PSNeRF:+Neural+inverse+rendering+for+multi-view+photometric+stereo manually and check the results.
        -> Author(s): Wenqi Yang, Guanying Chen, Chaofeng Chen, Zhenfang Chen, and Kwan-Yee K Wong
        -> Title:     PSNeRF: Neural inverse rendering for multi-view photometric stereo
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 56/72:
  -> INFO: Now checking 10 results for matching title: 'Reflective gaussian splatting'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
       -> INFO: All authors matched!
- Checking reference 57/72:
  -> INFO: Now checking 1 results for matching title: 'StableNormal: Reducing diffusion variance for stable and sharp normal'
       -> INFO: All authors matched!
- Checking reference 58/72:
  -> INFO: Now checking 1 results for matching title: 'GeoSplatting: Towards geometry guided gaussian splatting for physically-based inverse rendering'
       -> INFO: All authors matched!
- Checking reference 59/72:
  -> INFO: Now checking 1 results for matching title: 'The unreasonable effectiveness of deep features as a perceptual metric'
       -> INFO: All authors matched!
- Checking reference 60/72:
  -> INFO: Now checking 2 results for matching title: 'GAP: Gaussianize any point clouds with text guidance'
       -> INFO: All authors matched!
- Checking reference 61/72:
  -> INFO: Now checking 2 results for matching title: 'Neural Signed Distance Function Inference through Splatting 3D Gaussians Pulled on Zero-Level Set'
       -> INFO: All authors matched!
- Checking reference 62/72:
  -> INFO: Now checking 10 results for matching title: 'Learning unsigned distance functions from multi-view images with volume rendering priors'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhang', 'Shi', 'Liu', 'Han', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Learning+unsigned+distance+functions+from+multi-view+images+with+volume+rendering+priors manually and check the results.
        -> Author(s): Wenyuan Zhang, Kanle Shi, Yu-Shen Liu, and Zhizhong Han
        -> Title:     Learning unsigned distance functions from multi-view images with volume rendering priors
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 63/72:
  -> INFO: Now checking 2 results for matching title: 'NeRFPrior: Learning neural radiance field as a prior for indoor scene reconstruction'
       -> WARNING: Not all 6 authors from the found ref. were matched (only 6)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 64/72:
  -> INFO: Now checking 2 results for matching title: 'Fast Learning Radiance Fields by Shooting Much Fewer Rays'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 65/72:
  -> INFO: Now checking 2 results for matching title: 'MonoInstance: Enhancing monocular priors via multi-view instance alignment for neural rendering and reconstruction'
       -> INFO: All authors matched!
- Checking reference 66/72:
  -> INFO: Now checking 1 results for matching title: 'Ref-GS: Directional factorization for 2d gaussian splatting'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 67/72:
  -> INFO: Now checking 1 results for matching title: 'CAP-UDF: Learning unsigned distance functions progressively from raw point clouds with consistencyaware field optimization'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhou', 'Ma', 'Li', 'Liu', 'Fang', 'Han', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=CAP-UDF:+Learning+unsigned+distance+functions+progressively+from+raw+point+clouds+with+consistencyaware+field+optimization manually and check the results.
        -> Author(s): Junsheng Zhou, Baorui Ma, Shujuan Li, Yu-Shen Liu, Yi Fang, and Zhizhong Han
        -> Title:     CAP-UDF: Learning unsigned distance functions progressively from raw point clouds with consistencyaware field optimization
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 68/72:
  -> INFO: Now checking 2 results for matching title: 'Differentiable registration of images and lidar point clouds with voxelpoint-to-pixel matching'
       -> INFO: All authors matched!
- Checking reference 69/72:
  -> INFO: Now checking 1 results for matching title: 'U-CAN: Unsupervised point cloud denoising with consistency-aware noise2noise matching'
       -> INFO: All authors matched!
- Checking reference 70/72:
  -> INFO: Now checking 10 results for matching title: 'Uni3D: Exploring Unified 3D Representation at Scale'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2024)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 71/72:
  -> INFO: Now checking 2 results for matching title: 'DiffGS: Functional gaussian splatting diffusion'
       -> INFO: All authors matched!
- Checking reference 72/72:
  -> INFO: Now checking 10 results for matching title: 'Surface splatting'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zwicker', 'Pfister', 'Baar', 'Gross', '2001']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Surface+splatting manually and check the results.
        -> Author(s): Matthias Zwicker, Hanspeter Pfister, Jeroen Van Baar, and Markus Gross
        -> Title:     Surface splatting
        -> Year:      2001
     -> Manual search was skipped by the user.
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 3: i−1
-> Invalid unicode use found on p. 3: (1 −oj),
-> Invalid unicode use found on p. 3: c(ωo) = (1 −m)cd + Ls(ωo, a, m, r, n),
-> Invalid unicode use found on p. 4: P ′(πj(p)) = HijP(πi(p)), Hij = Kj(Rij −TijnT
-> Invalid unicode use found on p. 4: )K−1
-> Invalid unicode use found on p. 4: Lmv = ∥Ψi[P(πi(p))] −Ψj[P ′(πj(p))]∥2.
-> Invalid unicode use found on p. 5: wref · Γ(u, v) · |M0(u, v) −ΨM(u, v)|
-> Invalid unicode use found on p. 5: Li(ωi) = Lindirect(ωi) + (1 −O(ωi)) · Ldirect(ωi).
-> Invalid unicode use found on p. 6: i−1
-> Invalid unicode use found on p. 6: (1 −oj) + cr, O(ωi) =
-> Invalid unicode use found on p. 6: i−1
-> Invalid unicode use found on p. 6: (1 −oj),
-> Invalid unicode use found on p. 6: L = Lc + λn−dLn−d + λnLn + λmvLmv + λrefLref,
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Warning: Bracket content ['P ′ n1(u', ' v)'] on p. 5 could not be matched to a reference.
   -> Sentence:  We then compute the averaged per-pixel variance among these patches as a reflection score for vr, using standard 
deviation, refscore = 1 9 X (x,y)∈Pr(u,v) std(Ψr[Pr(u, v)], Ψn1[P ′ n1(u, v)], 
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 421 sentences on 10 pages -> Avg. of 47.77777777777778 sentences per page
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
-> Missing an abstract for reference with index 21 (Ref. ID = 22); Skipping LLM check...
-> Missing an abstract for reference with index 22 (Ref. ID = 23); Skipping LLM check...
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 26 (Ref. ID = 27); Skipping LLM check...
-> Missing an abstract for reference with index 27 (Ref. ID = 28); Skipping LLM check...
-> Missing an abstract for reference with index 28 (Ref. ID = 29); Skipping LLM check...
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 32 (Ref. ID = 33); Skipping LLM check...
-> Missing an abstract for reference with index 33 (Ref. ID = 34); Skipping LLM check...
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
-> Missing an abstract for reference with index 36 (Ref. ID = 37); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 41 (Ref. ID = 42); Skipping LLM check...
-> Missing an abstract for reference with index 42 (Ref. ID = 43); Skipping LLM check...
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
-> Missing an abstract for reference with index 44 (Ref. ID = 45); Skipping LLM check...
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 48 (Ref. ID = 49); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 50 (Ref. ID = 51); Skipping LLM check...
-> Missing an abstract for reference with index 51 (Ref. ID = 52); Skipping LLM check...
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 53 (Ref. ID = 54); Skipping LLM check...
-> Missing an abstract for reference with index 54 (Ref. ID = 55); Skipping LLM check...
-> Missing an abstract for reference with index 55 (Ref. ID = 56); Skipping LLM check...
-> Missing an abstract for reference with index 56 (Ref. ID = 57); Skipping LLM check...
-> Missing an abstract for reference with index 57 (Ref. ID = 58); Skipping LLM check...
-> Missing an abstract for reference with index 58 (Ref. ID = 59); Skipping LLM check...
-> Missing an abstract for reference with index 59 (Ref. ID = 60); Skipping LLM check...
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
-> Missing an abstract for reference with index 61 (Ref. ID = 62); Skipping LLM check...
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
  // LLM calling counter = 17
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 66 (Ref. ID = 67); Skipping LLM check...
-> Missing an abstract for reference with index 67 (Ref. ID = 68); Skipping LLM check...
-> Missing an abstract for reference with index 68 (Ref. ID = 69); Skipping LLM check...
  // LLM calling counter = 18
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 70 (Ref. ID = 71); Skipping LLM check...
-> Missing an abstract for reference with index 71 (Ref. ID = 72); Skipping LLM check...
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
  -> Found 5 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 8 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 19
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 20
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 21
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 22
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 23
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
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\28 MaterialRefGS Reflective Gaussian Splatting\PAU_results.md
```