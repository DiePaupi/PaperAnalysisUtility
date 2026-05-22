

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\49 JADE Joint Alignment and Deep Embedding\JADE Joint Alignment and Deep Embedding.pdf"
---
INFO:
 - 'springer' = Has two headerlines to skip (1st = Shortitle/Author; 2nd = page number)
 - 'acm'      = Has no headerlines to skip
Enter a supported formatting template (['springer', 'acm']): acm
---
INFO:
 - 'LFTOY' = Lastname, Firstname, Title, Outlet, Year
            -> This is, for example, used by Springer Nature
 - 'LFYTO' = Lastname, Firstname, Year, Title, Outlet
            -> This is, for example, used by the AAAI/ACM Conference
 - 'FLYTO' = Firstname, Lastname, Year, Title, Outlet
            -> This is, for example, used by ACM
 - 'FLTOY' = Firstname, Lastname, Title, Outlet, Year
            -> This is, for example, used by most papers of the NeurIPS Conference
Enter a supported bibliography layout (['LFTOY', 'LFYTO', 'FLYTO', 'FLTOY']): FLTOY
# PLEASE NOTE:
 -> The chosen bib layout uses ',' to separate multiple authors.
 => If that is correct, please press enter or type 'y', otherwise enter another author-separator to use: 
... Using default :)
---
INFO:
 - 'natbib'           = No numbering; reference in 'References' section starts with the authors' names
 - 'numbered_squares' = Reference in 'References' section starts with, e.g., '[1]'
 - 'number_with_dot'  = Reference in 'References' section starts with, e.g., '1.'
Enter a supported bibliography numbering (['natbib', 'numbered_squares', 'number_with_dot']): numbered_squares
---
INFO:
 - 'numeric'     = A number placed inside square brackets (e.g., [28])
                -> Multiple references are separated by a comma (e.g., [28,29])
 - 'authoryear'  = Authors' names and the year places insince brackets with or withou a comma in between (e.g., (Dignum et al., 2025))
                -> Multiple references are separated by a semicolon or comma (e.g., (Dignum et al. 2025; Caliskan et al. 2017))
Enter a supported referencing template (['numeric', 'authoryear']): numeric
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Methods' on page 2
- Found following heading '3 - Fast Computation for JADE' on page 5
- Found following heading '4 - Experiments' on page 6
- Found following heading '5 - Conclusions' on page 9
- Found following heading '6 - Acknowledgment' on page 10
=> Found references/literature section on page 10
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 10 -- 16
All found references: 84
Backend tkagg is interactive backend. Turning interactive mode on.
-> Warning: Malformed author string: '10'
-> Warning: Malformed author string: 'Liping'
-> Warning: Malformed author string: 'Others'
-> Warning: Malformed author string: ''
-> Warning: Malformed author string: 'Yang'
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ...                                               link  valid
0       1                                  Rohit Arora et al  ...                                                      None
1       2  Jun Aruga, Takashi Inoue, Jun Hoshino, and Kat...  ...                                                      None
2       3  Mykhailo Y Batiuk, Araks Martirosyan, Jérôme W...  ...                                                      None
3       4  Lina Vanessa Becerra-Hernández, Martha Isabel ...  ...                                                      None
4       5  Emelie Berglund, Jonas Maaskola, Niklas Schult...  ...                                                      None
..    ...                                                ...  ...                                                ...    ...
79     80  Ron Zeira, Max Land, Alexander Strzalkowski, a...  ...                                                      None
80     81   Yifan Zeng, Rong Yin, Meng Luo, Jian Chen, et al  ...                                                      None
81     82        Xiang Zhou, Kangning Dong, and Shihua Zhang  ...                                                      None
82     83  Yike Zong, Tian Yu, Xiaoqing Wang, Yufeng Wang...  ...                                                      None
83     84           Chunman Zuo, Junjie Xia, and Luonan Chen  ...  https://doi.org/10.1101/2025.11.21.689823doi:b...   None

[84 rows x 10 columns]
- Checking reference 1/84:
  -> INFO: Now checking 1 results for matching title: 'Spatial transcriptomics reveals distinct and conserved tumor core and edge architectures that predict survival and targeted therapy response'
       -> WARNING: Not all 16 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Cao, Kumar, Sinha, Chanda, McNeil, Samuel, Matthews, Chandarana, Hart, Dort, Biernaskie, Neri, Hyrcza, Bose'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 2/84:
  -> INFO: Now checking 1 results for matching title: 'Zic2 controls cerebellar development in cooperation with zic1'
       -> INFO: All authors matched!
- Checking reference 3/84:
  -> INFO: Now checking 1 results for matching title: 'Identification of region-specific astrocyte subtypes at single cell resolution'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Batiuk', 'Martirosyan', 'Wahis', 'Vin', 'Marneffe', 'Kusserow', 'Koeppen', 'Viana', 'Oliveira', 'Voet', 'Ponting', 'Belgard', 'Holt', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Identification+of+region-specific+astrocyte+subtypes+at+single+cell+resolution manually and check the results.
        -> Author(s): Mykhailo Y Batiuk, Araks Martirosyan, Jérôme Wahis, Filip de Vin, Catherine Marneffe, Carola Kusserow, Jordan Koeppen, João Filipe Viana, João Filipe Oliveira, Thierry Voet, Chris P Ponting, T Grant Belgard, and Matthew G Holt
        -> Title:     Identification of region-specific astrocyte subtypes at single cell resolution
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 4/84:
  -> INFO: Now checking 1 results for matching title: 'Crystallin alpha-b overexpression as a possible marker of reactive astrogliosis in human cerebral contusions'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Pimienta-Jiménez'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 5/84:
  -> INFO: Now checking 1 results for matching title: 'Spatial maps of prostate cancer transcriptomes reveal an unexplored landscape of heterogeneity'
       -> INFO: All authors matched!
- Checking reference 6/84:
  -> INFO: Now checking 6 results for matching title: 'Spatial transcriptomics coming of age'
       -> INFO: All authors matched!
- Checking reference 7/84:
  -> INFO: Now checking 1 results for matching title: 'West is an ensemble method for spatial transcriptomics analysis'
       -> INFO: All authors matched!
- Checking reference 8/84:
  -> Checking if provided link is pingable: https://doi.org/10.1101/2025.11.21.689823doi:bioRxiv
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: CC-BY 4.0 International license available under a (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity
  -> WARNING: No results were found through the dblp search!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Calvigioni', 'Máté', 'Fuzik', 'Girach', 'Zhang', 'Varró', 'Beiersdorf', 'Schwindling', 'Yanagawa', 'Dockray', '10', '2017']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=CC-BY+4.0+International+license+available+under+a+(which+was+not+certified+by+peer+review)+is+the+author/funder%2C+who+has+granted+bioRxiv+a+license+to+display+the+preprint+in+perpetuity manually and check the results.
        -> Author(s): Daniela Calvigioni, Zoltán Máté, János Fuzik, Fatima Girach, Ming-Dong Zhang, Andrea Varró, Johannes Beiersdorf, Christian Schwindling, Yuchio Yanagawa, Graham J Dockray, 10
        -> Title:     CC-BY 4.0 International license available under a (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity
        -> Year:      2017
     -> Manual search was skipped by the user.
- Checking reference 9/84:
  -> WARNING: Skipping search (due to not enough info) for reference titled ''
           -> Author(s): Ao Chen, Xuxun Ying, Yifei Zheng, Wentao Ma, Xiaopeng Zheng, Ping Zhou, Rui Lu, Yi Ding, Qian Ma, Jiping Zhao, Xia Feng, Wenxin Feng, Wei Hu, Jian Wang, Shu Yi, Wenying Yu, Chong Tao, Qianyi Du, Yi Huang, Zhiming Zhu, and Liping
           -> Year: 2022
- Checking reference 10/84:
  -> INFO: Now checking 10 results for matching title: 'Spatially resolved, highly multiplexed rna profiling in single cells'
       -> INFO: All authors matched!
- Checking reference 11/84:
  -> INFO: Now checking 3 results for matching title: 'Spatially resolved transcriptomics reveals genes associated with the vulnerability of middle temporal gyrus in alzheimer’s disease'
       -> INFO: All authors matched!
- Checking reference 12/84:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: Slat: a transformer-based method for simultaneous alignment and clustering of spatial transcriptomics data
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 1 results for matching title: 'Slat: a transformer-based method for simultaneous alignment and clustering of spatial transcriptomics data'
  -> WARNING: None of the 1 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Slat:+a+transformer-based+method+for+simultaneous+alignment+and+clustering+of+spatial+transcriptomics+data manually and check the results.
        -> Author(s): Zhihao Chen, Hantao Zhang, Yuhan Zhang, Zhanlin Hu, Quanquan Gu, Qing Zhang, and Shuo Suo
        -> Title:     Slat: a transformer-based method for simultaneous alignment and clustering of spatial transcriptomics data
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 13/84:
  -> INFO: Now checking 4 results for matching title: 'Stalign: Alignment of spatial transcriptomics data using diffeomorphic metric mapping'
       -> INFO: All authors matched!
- Checking reference 14/84:
  -> INFO: Now checking 10 results for matching title: 'Sinkhorn distances: Lightspeed computation of optimal transport'
       -> INFO: All authors matched!
- Checking reference 15/84:
  -> INFO: Now checking 10 results for matching title: 'Gromov–wasserstein optimal transport to align single-cell multi-omics data'
       -> INFO: All authors matched!
- Checking reference 16/84:
  -> INFO: Now checking 1 results for matching title: 'Deciphering spatial domains from spatially resolved transcriptomics with an adaptive graph attention auto-encoder'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 17/84:
  -> INFO: Now checking 1 results for matching title: 'Integration of pan-cancer single-cell and spatial transcriptomics reveals stromal cell features and therapeutic targets in tumor microenvironment'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Du', 'Kueckelhaus', 'Wang', '2024']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Integration+of+pan-cancer+single-cell+and+spatial+transcriptomics+reveals+stromal+cell+features+and+therapeutic+targets+in+tumor+microenvironment manually and check the results.
        -> Author(s): Yifei Du, Jessica Kueckelhaus, You Wang, et al
        -> Title:     Integration of pan-cancer single-cell and spatial transcriptomics reveals stromal cell features and therapeutic targets in tumor microenvironment
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 18/84:
  => ERROR: Semantic Scholar didn't find any results to parse!
     -> Semantic Scholar search was done for the title: ‘google maps’ project for cells reveals their role in spread of disease
  -> WARNING: No results were found through the dblp search!
  -> INFO: Now checking 703 results for matching title: '‘google maps’ project for cells reveals their role in spread of disease'
  -> WARNING: None of the 703 results matched the expected title!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=‘google+maps’+project+for+cells+reveals+their+role+in+spread+of+disease manually and check the results.
        -> Author(s): Financial Times
        -> Title:     ‘google maps’ project for cells reveals their role in spread of disease
        -> Year:      2024
     -> Manual search was skipped by the user.
- Checking reference 19/84:
  -> INFO: Now checking 1 results for matching title: 'Stereo-seq of the prefrontal cortex in aging and alzheimer’s disease'
       -> INFO: All authors matched!
- Checking reference 20/84:
  -> INFO: Now checking 1 results for matching title: 'Spiral: integrating and aligning spatially resolved transcriptomics data across different experiments, conditions, and technologies'
       -> INFO: All authors matched!
- Checking reference 21/84:
  -> Checking if provided link is pingable: https://doi.org/10.1101/2025.11.21.689823doi:bioRxiv
  -> INFO: Now checking 3 results for matching title: 'Batch effects in single-cell rna-sequencing data are corrected by matching mutual nearest neighbors'
  -> WARNING: None of the 3 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Haghverdi', 'Lun', 'Morgan', 'Marioni', '2025']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Batch+effects+in+single-cell+rna-sequencing+data+are+corrected+by+matching+mutual+nearest+neighbors manually and check the results.
        -> Author(s): Laleh Haghverdi, Aaron T L Lun, Mark D Morgan, and John C Marioni
        -> Title:     Batch effects in single-cell rna-sequencing data are corrected by matching mutual nearest neighbors
        -> Year:      2025
     -> Manual search was skipped by the user.
- Checking reference 22/84:
  -> INFO: Now checking 4 results for matching title: 'Dest-ot: Alignment of spatiotemporal transcriptomics data'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 23/84:
  -> INFO: Now checking 2 results for matching title: 'An anatomically comprehensive atlas of the adult human brain transcriptome'
       -> WARNING: Not all 67 authors from the found ref. were matched (only 61)
                   Unmatched authors = 'Dee, Geschwind, Hof, Koch, Grant, Jones'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 24/84:
  -> INFO: Now checking 2 results for matching title: 'Efficient integration of heterogeneous singlecell transcriptomes using scanorama'
  -> WARNING: None of the 2 results matched the expected title!
  -> Failed to query dblp API. Status code: 429
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Hie', 'Bryson', 'Berger', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Efficient+integration+of+heterogeneous+singlecell+transcriptomes+using+scanorama manually and check the results.
        -> Author(s): Brian Hie, Brendan Bryson, and Bonnie Berger
        -> Title:     Efficient integration of heterogeneous singlecell transcriptomes using scanorama
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 25/84:
  -> INFO: Now checking 2 results for matching title: 'Spagcn: Integrating gene expression, spatial location and histology to identify spatial domains and spatially variable genes by graph convolutional network'
       -> INFO: All authors matched!
- Checking reference 26/84:
  -> INFO: Now checking 1 results for matching title: 'Adept: Autoencoder with differentially expressed genes and imputation for robust spatial transcriptomics clustering'
       -> INFO: All authors matched!
- Checking reference 27/84:
  -> INFO: Now checking 2 results for matching title: 'Integrated single cell and unsupervised spatial transcriptomic analysis defines molecular anatomy of the human dorsolateral prefrontal cortex'
       -> WARNING: Not all 23 authors from the found ref. were matched (only 23)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 28/84:
  -> Checking if provided link is pingable: https://doi.org/10.1101/2022.10.06.510405
  -> INFO: Now checking 3 results for matching title: 'High resolution mapping of the breast cancer tumor microenvironment using integrated single cell, spatial and in situ analysis of ffpe tissue'
       -> WARNING: Not all 14 authors from the found ref. were matched (only 14)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 29/84:
  -> Semantic Scholar not reachable, trying again ... (TryCount = 1)
  -> INFO: Now checking 2 results for matching title: 'Multimodal analysis of composition and spatial architecture in human squamous cell carcinoma'
       -> WARNING: Not all 21 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Bai, Zhu, Bhaduri, Rovira-Clavé, Hollmig, Aasi, Nolan, Khavari'
       -> WARNING: Not all 21 authors from the found ref. were matched (only 13)
                   Unmatched authors = 'Bai, Zhu, Bhaduri, Rovira-Clavé, Hollmig, Aasi, Nolan, Khavari'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 30/84:
  -> INFO: Now checking 10 results for matching title: 'Alignment of spatial genomics data using deep gaussian processes'
       -> INFO: All authors matched!
- Checking reference 31/84:
  -> Checking if provided link is pingable: https://doi.org/10.1101/2025.11.21.689823doi:bioRxiv
  -> INFO: Now checking 10 results for matching title: 'Spatial transcriptomics in neuroscience'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 32/84:
  -> INFO: Now checking 1 results for matching title: 'Glutamatergic control of the expression of the proenkephalin gene in rat frontoparietal cortical slice cultures'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Just', 'Olenik', 'Heimrich', 'Meyer', '1998']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Glutamatergic+control+of+the+expression+of+the+proenkephalin+gene+in+rat+frontoparietal+cortical+slice+cultures manually and check the results.
        -> Author(s): L Just, C Olenik, B Heimrich, and D K Meyer
        -> Title:     Glutamatergic control of the expression of the proenkephalin gene in rat frontoparietal cortical slice cultures
        -> Year:      1998
     -> Manual search was skipped by the user.
- Checking reference 33/84:
  -> INFO: Now checking 1 results for matching title: 'Efficient and precise single-cell reference atlas mapping with symphony'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Nathan, Weinand, Zhang, Millard, Rumker, Moody'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 34/84:
  -> INFO: Now checking 10 results for matching title: 'Semi-supervised classification with graph convolutional networks'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 35/84:
  -> INFO: Now checking 10 results for matching title: 'Cell clustering for spatial transcriptomics data with graph neural networks'
       -> INFO: All authors matched!
- Checking reference 36/84:
  -> Checking if provided link is pingable: https://www.biorxiv.org/content/10.1101/2024.12.06.627127v1
  -> WARNING: Skipping search (due to not enough info) for reference titled ''
           -> Author(s): X Lin, Y Zhang, Z Chen, and
           -> Year: 2024
- Checking reference 37/84:
  -> INFO: Now checking 2 results for matching title: 'Probabilistic embedding, clustering, and alignment for integrating spatial transcriptomics data with precast'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Liao, Luo, Yang, Lau, Jiao, Shi, Zhai, Ji, Yeong'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 38/84:
  -> INFO: Now checking 3 results for matching title: 'Partial alignment of multislice spatially resolved transcriptomics data'
       -> INFO: All authors matched!
- Checking reference 39/84:
  -> INFO: Now checking 3 results for matching title: 'Spatially informed clustering, integration, and deconvolution of spatial transcriptomics with graphst'
       -> INFO: All authors matched!
- Checking reference 40/84:
  -> INFO: Now checking 2 results for matching title: 'Integrating singlecell and spatial transcriptomics to elucidate intercellular tissue dynamics'
  -> WARNING: None of the 2 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Longo', 'Guo', 'Ji', 'Khavari', '2021']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Integrating+singlecell+and+spatial+transcriptomics+to+elucidate+intercellular+tissue+dynamics manually and check the results.
        -> Author(s): Sarah K Longo, Michelle G Guo, Alexander L Ji, and Pamela A Khavari
        -> Title:     Integrating singlecell and spatial transcriptomics to elucidate intercellular tissue dynamics
        -> Year:      2021
     -> Manual search was skipped by the user.
- Checking reference 41/84:
  -> INFO: Now checking 10 results for matching title: 'Deep generative modeling for single-cell transcriptomics'
       -> INFO: All authors matched!
- Checking reference 42/84:
  -> INFO: Now checking 10 results for matching title: 'Mapping single-cell data to reference atlases by transfer learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 43/84:
  -> INFO: Now checking 10 results for matching title: 'Benchmarking atlas-level data integration in single-cell genomics'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Year (2020) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 44/84:
  -> INFO: Now checking 1 results for matching title: 'Batman: fast and accurate integration of single-cell rna-seq datasets via minimum-weight matching'
       -> INFO: All authors matched!
- Checking reference 45/84:
  -> INFO: Now checking 5 results for matching title: 'Spatiotemporal dynamics of molecular pathology in amyotrophic lateral sclerosis'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 46/84:
  -> Checking if provided link is pingable: https://doi.org/10.1101/2025.11.21.689823doi:bioRxiv
  -> INFO: Now checking 10 results for matching title: 'Method of the year: spatially resolved transcriptomics'
       -> INFO: All authors matched!
       -> WARNING: Year (2021) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 47/84:
  -> INFO: Now checking 10 results for matching title: 'Transcriptome-scale spatial gene expression in the human dorsolateral prefrontal cortex'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
       -> WARNING: Year (2020) does not match expected year (2021)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 48/84:
  -> INFO: Now checking 1 results for matching title: 'Gromov–wasserstein distances and the metric approach to object matching'
       -> INFO: All authors matched!
- Checking reference 49/84:
  -> INFO: Now checking 8 results for matching title: 'Integrating microarray-based spatial transcriptomics and single-cell rna-seq reveals tissue architecture in pancreatic ductal adenocarcinomas'
       -> INFO: All authors matched!
- Checking reference 50/84:
  -> INFO: Now checking 10 results for matching title: 'Museum of spatial transcriptomics'
       -> INFO: All authors matched!
       -> WARNING: Year (2020) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 51/84:
  -> INFO: Now checking 10 results for matching title: 'Isolation and characterization of myelin basic protein from rat brain'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Norton', 'Poduslo', '1973']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Isolation+and+characterization+of+myelin+basic+protein+from+rat+brain manually and check the results.
        -> Author(s): William T Norton and Selwyn E Poduslo
        -> Title:     Isolation and characterization of myelin basic protein from rat brain
        -> Year:      1973
     -> Manual search was skipped by the user.
- Checking reference 52/84:
  -> Checking if provided link is pingable: https://arxiv.org/abs/2506.15698
  -> INFO: Now checking 10 results for matching title: 'Global context-aware representation learning for spatially resolved transcriptomics'
       -> INFO: All authors matched!
- Checking reference 53/84:
  -> INFO: Now checking 1 results for matching title: 'Diverse signaling mechanisms and heterogeneity of astrocyte reactivity in alzheimer’s disease'
       -> INFO: All authors matched!
- Checking reference 54/84:
  -> INFO: Now checking 1 results for matching title: 'Secretagogin is expressed by developing neocortical gabaergic neurons in humans but not mice and increases neurite arbor size and complexity'
       -> INFO: All authors matched!
- Checking reference 55/84:
  -> INFO: Now checking 1 results for matching title: 'Identifying multicellular spatiotemporal organization of cells with spaceflow'
       -> INFO: All authors matched!
- Checking reference 56/84:
  -> INFO: Now checking 10 results for matching title: 'Measurement of diversity'
       -> INFO: All authors matched!
- Checking reference 57/84:
  -> INFO: Now checking 10 results for matching title: 'Concerning nonnegative matrices and doubly stochastic matrices'
       -> INFO: All authors matched!
- Checking reference 58/84:
  -> INFO: Now checking 4 results for matching title: 'Visualization and analysis of gene expression in tissue sections by spatial transcriptomics'
       -> WARNING: Not all 21 authors from the found ref. were matched (only 20)
                   Unmatched authors = 'Frisén'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 59/84:
  -> INFO: Now checking 10 results for matching title: 'Comprehensive integration of single-cell data'
       -> WARNING: Not all 9 authors from the found ref. were matched (only 9)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 60/84:
  -> Checking if provided link is pingable: https://doi.org/10.1101/2025.11.21.689823doi:bioRxiv
  -> INFO: Now checking 1 results for matching title: 'Cenp-v is required for centromere organization, chromosome alignment and cytokinesis'
       -> INFO: All authors matched!
       -> WARNING: Year (2008) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 61/84:
  -> INFO: Now checking 1 results for matching title: 'Secretagogin as a marker to distinguish between different neuron types in human frontal and temporal cortex'
       -> INFO: All authors matched!
- Checking reference 62/84:
  -> INFO: Now checking 2 results for matching title: 'A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain'
       -> WARNING: Not all 72 authors from the found ref. were matched (only 5)
                   Unmatched authors = 'Yao, Velthoven, Kunst, Zhang, McMillen, Lee, Jung, Goldy, Abdelhak, Baker, Barkan, Bertagnolli, Campos, Carey, Casper, Chakka, Chakrabarty, Chavan, Chen, Clark, Close, Crichton, Daniel, Dolbeare, Ellingwood, Gee, Glandon, Gloe, Gould, Gray, Guilford, Guzman, Hirschstein, Jin, Kroll, Lathia, Leon, Long, Maltzer, Martin, McCue, Meyerdierks, Nguyen, Pham, Rimorin, Ruiz, Shapovalova, Slaughterbeck, Sulc, Tieu, Torkelson, Tung, Cuevas, Wadhwani, Ward, Levi, Farrell, Thompson, Mufti, Pagan, Kruse, Dee, Sunkin, Esposito, Hawrylycz, Waters, Smith'
       -> WARNING: Not all 101 authors from the found ref. were matched (only 6)
                   Unmatched authors = 'Yao, Velthoven, Kunst, Zhang, McMillen, Lee, Jung, Goldy, Abdelhak, Aitken, Baker, Baker, Barkan, Bertagnolli, Bhandiwad, Bielstein, Bishwakarma, Campos, Carey, Casper, Chakka, Chakrabarty, Chavan, Chen, Clark, Close, Crichton, Daniel, DiValentin, Dolbeare, Ellingwood, Fiabane, Fliss, Gee, Gerstenberger, Glandon, Gloe, Gould, Gray, Guilford, Guzman, Hirschstein, Hooper, Hupp, Jin, Kroll, Lathia, Leon, Li, Long, Madigan, Malloy, Malone, Maltzer, Martin, McCue, McGinty, Mei, Melchor, Meyerdierks, Mollenkopf, Moonsman, Nguyen, Otto, Pham, Rimorin, Ruiz, Sanchez, Sawyer, Shapovalova, Shepard, Slaughterbeck, Sulc, Tieu, Torkelson, Tung, Cuevas, Vance, Wadhwani, Ward, Levi, Farrell, Young, Staats, Wang, Thompson, Mufti, Pagan, Kruse, Dee, Sunkin, Esposito, Hawrylycz, Waters, Smith'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 63/84:
  -> INFO: Now checking 1 results for matching title: 'Spatially resolved transcriptomics enables dissection of genetic heterogeneity in stage III cutaneous malignant melanoma'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Thrane', 'Eriksson', 'Maaskola', 'Hansson', 'Lundeberg', '2018']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Spatially+resolved+transcriptomics+enables+dissection+of+genetic+heterogeneity+in+stage+III+cutaneous+malignant+melanoma manually and check the results.
        -> Author(s): K Thrane, H Eriksson, J Maaskola, J Hansson, and J Lundeberg
        -> Title:     Spatially resolved transcriptomics enables dissection of genetic heterogeneity in stage III cutaneous malignant melanoma
        -> Year:      2018
     -> Manual search was skipped by the user.
- Checking reference 64/84:
  -> INFO: Now checking 10 results for matching title: 'The expanding vistas of spatial transcriptomics'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2023)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 65/84:
  -> INFO: Now checking 8 results for matching title: 'A molecular atlas of cell types and zonation in the brain vasculature'
       -> WARNING: Not all 18 authors from the found ref. were matched (only 8)
                   Unmatched authors = 'Mäe, Lavina, Gouveia, Sun, Raschperger, Räsänen, Zarb, Mochizuki, Keller, Lendahl'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 66/84:
  -> INFO: Now checking 10 results for matching title: 'Attention is all you need'
       -> INFO: All authors matched!
- Checking reference 67/84:
  -> INFO: Now checking 2 results for matching title: 'Optimal transport for structured data with application on graphs'
       -> INFO: All authors matched!
       -> WARNING: Year (2018) does not match expected year (2019)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 68/84:
  -> INFO: Now checking 10 results for matching title: 'Fused gromov–wasserstein distances for structured data'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Vayer', 'Chapel', 'Flamary', 'Tavenard', 'Courty', '2019']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Fused+gromov–wasserstein+distances+for+structured+data manually and check the results.
        -> Author(s): Tristan Vayer, Ludovic Chapel, Rémi Flamary, Rémi Tavenard, and Nicolas Courty
        -> Title:     Fused gromov–wasserstein distances for structured data
        -> Year:      2019
     -> Manual search was skipped by the user.
- Checking reference 69/84:
  -> INFO: Now checking 10 results for matching title: 'Deep graph infomax'
       -> INFO: All authors matched!
- Checking reference 70/84:
  -> INFO: Now checking 10 results for matching title: 'Identifying temporal and spatial patterns of variation from multimodal data using mefisto'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 3)
                   Unmatched authors = 'Argelaguet, Wirbel, Bredikhin, Zeller, Stegle'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 71/84:
  -> WARNING: Skipping search (due to not enough info) for reference titled ''
           -> Author(s): Zhen Wang, Qian Hu, Zhipeng Zheng, and Yang
           -> Year: 2023
- Checking reference 72/84:
  -> INFO: Now checking 6 results for matching title: 'Single-cell stereo-seq reveals induced progenitor cells involved in axolotl brain regeneration'
       -> WARNING: Not all 36 authors from the found ref. were matched (only 19)
                   Unmatched authors = 'Lai, Qiu, Wu, Zhang, Jiang, Xu, Peng, Lou, Yuan, Ma, Pan, Gao, Esteban, Fan, Xu, Fei, Gu'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 73/84:
  -> INFO: Now checking 1 results for matching title: 'The neocortical infrastructure for language involves region-specific patterns of laminar gene expression'
       -> WARNING: Not all 10 authors from the found ref. were matched (only 9)
                   Unmatched authors = 'Velthuijs'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 74/84:
  -> Checking if provided link is pingable: https://doi.org/10.1016/j.devcel.2022.04.011
  -> INFO: Now checking 1 results for matching title: 'The single-cell stereo-seq reveals region-specific cell subtypes and transcriptome profiling in arabidopsis leaves'
  -> WARNING: None of the 1 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Xia', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://doi.org/10.1016/j.devcel.2022.04.011 manually and check the results.
        -> Author(s): Keke Xia et al
        -> Title:     The single-cell stereo-seq reveals region-specific cell subtypes and transcriptome profiling in arabidopsis leaves
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 75/84:
  -> Checking if provided link is pingable: https://doi.org/10.1101/2025.11.21.689823doi:bioRxiv
  -> INFO: Now checking 2 results for matching title: 'Deepst: identifying spatial domains in spatial transcriptomics by deep learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2022) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 76/84:
  -> INFO: Now checking 10 results for matching title: 'Unsupervised spatially embedded deep representation of spatial transcriptomics'
       -> WARNING: Not all 11 authors from the found ref. were matched (only 11)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 77/84:
  -> INFO: Now checking 2 results for matching title: 'Spacel: deep learning-based characterization of spatial transcriptome architectures'
       -> INFO: All named authors matched; rest may fall under 'et al.'.
- Checking reference 78/84:
  -> INFO: Now checking 1 results for matching title: 'Graph embedding and gaussian mixture variational autoencoder network for end-to-end analysis of single-cell rna sequencing data'
       -> INFO: All authors matched!
       -> WARNING: Year (2023) does not match expected year (2022)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 79/84:
  -> INFO: Now checking 10 results for matching title: 'Benchmarking spatial clustering methods with spatially resolved transcriptomics data'
       -> WARNING: Not all 8 authors from the found ref. were matched (only 5)
                   Unmatched authors = 'Yao, Cui, Zhang'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 80/84:
  -> INFO: Now checking 10 results for matching title: 'Alignment and integration of spatial transcriptomics data'
       -> INFO: All authors matched!
- Checking reference 81/84:
  -> INFO: Now checking 4 results for matching title: 'Deciphering spatial domains by integrating histopathological image and transcriptomics via contrastive learning'
  -> WARNING: None of the 4 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zeng', 'Yin', 'Luo', 'Chen', '2022']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deciphering+spatial+domains+by+integrating+histopathological+image+and+transcriptomics+via+contrastive+learning manually and check the results.
        -> Author(s): Yifan Zeng, Rong Yin, Meng Luo, Jian Chen, et al
        -> Title:     Deciphering spatial domains by integrating histopathological image and transcriptomics via contrastive learning
        -> Year:      2022
     -> Manual search was skipped by the user.
- Checking reference 82/84:
  -> INFO: Now checking 10 results for matching title: 'Integrating spatial transcriptomics data across different conditions, technologies and developmental stages'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR: Reaching dblp failed: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
  => ERROR loading dblp result as JSON: Expecting value: line 1 column 1 (char 0)
     -> dblp search was done with these keywords: ['Zhou', 'Dong', 'Zhang', '2023']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Integrating+spatial+transcriptomics+data+across+different+conditions%2C+technologies+and+developmental+stages manually and check the results.
        -> Author(s): Xiang Zhou, Kangning Dong, and Shihua Zhang
        -> Title:     Integrating spatial transcriptomics data across different conditions, technologies and developmental stages
        -> Year:      2023
     -> Manual search was skipped by the user.
- Checking reference 83/84:
  -> INFO: Now checking 4 results for matching title: 'const: an interpretable multi-modal contrastive learning framework for spatial transcriptomics'
       -> INFO: All authors matched!
- Checking reference 84/84:
  -> Checking if provided link is pingable: https://doi.org/10.1101/2025.11.21.689823doi:bioRxiv
  -> INFO: Now checking 10 results for matching title: 'Dissecting tumor microenvironment from spatially resolved transcriptomics data by heterogeneous graph learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2024) does not match expected year (2025)!
  -> INFO: No perfect match found; taking the next best!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: −1
-> Invalid unicode use found on p. 2: −1
-> Invalid unicode use found on p. 3: n1 ||X1 −ˆX1||2
-> Invalid unicode use found on p. 3: n2 ||X2 −ˆX2||2
-> Invalid unicode use found on p. 3: −HT
-> Invalid unicode use found on p. 3: n1 ||D1 −n2
-> Invalid unicode use found on p. 3: n2 ||D2 −
-> Invalid unicode use found on p. 3: n1 ||H1 −n2ΠH2||F +
-> Invalid unicode use found on p. 3: n2 ||H2 −n1ΠT H1||F . Similarly, the scaling factors n2 and n1
-> Invalid unicode use found on p. 4: SCL = −1
-> Invalid unicode use found on p. 4: 1 −Φ(h′
-> Invalid unicode use found on p. 4: −Hhyper,T
-> Invalid unicode use found on p. 5: −HT
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 386 sentences on 10 pages -> Avg. of 43.888888888888886 sentences per page
---
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
-> Missing an abstract for reference with index 5 (Ref. ID = 6); Skipping LLM check...
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
-> Missing an abstract for reference with index 8 (Ref. ID = 9); Skipping LLM check...
-> Missing an abstract for reference with index 9 (Ref. ID = 10); Skipping LLM check...
-> Missing an abstract for reference with index 10 (Ref. ID = 11); Skipping LLM check...
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
-> Missing an abstract for reference with index 18 (Ref. ID = 19); Skipping LLM check...
-> Missing an abstract for reference with index 19 (Ref. ID = 20); Skipping LLM check...
-> Missing an abstract for reference with index 20 (Ref. ID = 21); Skipping LLM check...
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 23 (Ref. ID = 24); Skipping LLM check...
-> Missing an abstract for reference with index 24 (Ref. ID = 25); Skipping LLM check...
-> Missing an abstract for reference with index 25 (Ref. ID = 26); Skipping LLM check...
  // LLM calling counter = 6
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 7
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 8
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 29 (Ref. ID = 30); Skipping LLM check...
  // LLM calling counter = 9
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 31 (Ref. ID = 32); Skipping LLM check...
  // LLM calling counter = 10
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 11
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 34 (Ref. ID = 35); Skipping LLM check...
-> Missing an abstract for reference with index 35 (Ref. ID = 36); Skipping LLM check...
  // LLM calling counter = 12
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 37 (Ref. ID = 38); Skipping LLM check...
-> Missing an abstract for reference with index 38 (Ref. ID = 39); Skipping LLM check...
-> Missing an abstract for reference with index 39 (Ref. ID = 40); Skipping LLM check...
-> Missing an abstract for reference with index 40 (Ref. ID = 41); Skipping LLM check...
  // LLM calling counter = 13
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 14
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 43 (Ref. ID = 44); Skipping LLM check...
  // LLM calling counter = 15
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 45 (Ref. ID = 46); Skipping LLM check...
  // LLM calling counter = 16
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 47 (Ref. ID = 48); Skipping LLM check...
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
  // LLM calling counter = 17
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 18
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 60 (Ref. ID = 61); Skipping LLM check...
  // LLM calling counter = 19
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 62 (Ref. ID = 63); Skipping LLM check...
-> Missing an abstract for reference with index 63 (Ref. ID = 64); Skipping LLM check...
-> Missing an abstract for reference with index 64 (Ref. ID = 65); Skipping LLM check...
-> Missing an abstract for reference with index 65 (Ref. ID = 66); Skipping LLM check...
  // LLM calling counter = 20
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 67 (Ref. ID = 68); Skipping LLM check...
-> Missing an abstract for reference with index 68 (Ref. ID = 69); Skipping LLM check...
  // LLM calling counter = 21
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 70 (Ref. ID = 71); Skipping LLM check...
  // LLM calling counter = 22
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 23
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 73 (Ref. ID = 74); Skipping LLM check...
  // LLM calling counter = 24
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 25
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 76 (Ref. ID = 77); Skipping LLM check...
  // LLM calling counter = 26
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 78 (Ref. ID = 79); Skipping LLM check...
-> Missing an abstract for reference with index 79 (Ref. ID = 80); Skipping LLM check...
-> Missing an abstract for reference with index 80 (Ref. ID = 81); Skipping LLM check...
-> Missing an abstract for reference with index 81 (Ref. ID = 82); Skipping LLM check...
-> Missing an abstract for reference with index 82 (Ref. ID = 83); Skipping LLM check...
  // LLM calling counter = 27
  -> Automatic parsing of LLM list worked!
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
-> Now checking the JQ proceedings:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 4 matches in this ranking!
-> Now checking the JQ jounrals:
  -> Processing initial jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 16 matches in this ranking!
-> Now checking the CORE A+ - B rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 21 matches in this ranking!
-> Now checking the CORE C rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 12 matches in this ranking!
-> Now checking the remaining CORE rankings:
  -> Processing initial core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 10 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 2301 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 28
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━━━━━━━━━━  68% 0:00:01
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 29
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━━━━━━  71% 0:00:01
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 30
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━━━━━━━━  67% 0:00:01
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 31
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━━━━━━━━━  71% 0:00:01
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 32
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━━━  79% 0:00:01
###############################
# Starting Author Check
###############################
-> Saved chapter_fig on try 1
-> Saved lit_fig on try 1
-> Saved rank_fig on try 1
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\49 JADE Joint Alignment and Deep Embedding\PAU_results.md
```