

```
Enter the path to the PDF file: "C:...\PAU - All  GPTZero NeurIPS Paper with H\6 Memory-Augmented Potential Field Theory\Memory-Augmented Potential Field Theory.pdf"
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
 - 'authoryear_round'  = Authors' names and the year places insince round brackets (e.g., (Speckmann et al., 2025))
                      -> Multiple references are separated by a semicolon (e.g., (Speckmann et al. 2025; Janiesch et al. 2021))
                      -> Please note that the author and year are *not* separated
 - 'authoryear_square' = Authors' names and the year places insince square brackets (e.g., [Speckmann et al., 2025])
                      -> Multiple references are separated by a comma (e.g., [Speckmann et al., 2025, Janiesch et al., 2021])
                      -> Please note that the author and year are also separated by a comma
Enter a supported referencing template (['numeric', 'authoryear_round', 'authoryear_square']): numeric
##########################################################
# Starting Structure Check
##########################################################
- Found Introduction on page 1
- Found following heading '2 - Related Work' on page 2
- Found following heading '3 - Memory-Augmented Potential Field Theory' on page 3
- Found following heading '4 - An Extension: Memory-Augmented Predictive Path Integral Method' on page 5
- Found following heading '5 - Experimental Evaluation in Robotic Control Environments' on page 7
- Found following heading '6 - Further Experiments on Complex Engineering Systems' on page 8
- Found following heading '7 - Discussion and Limitations' on page 10
=> Found references/literature section on page 11
- Found first appendix 'A - Broader Impacts' on page 12
- Found following appendix 'B - Detailed Memory Framework' on page 12
- Found following appendix 'C - Theoretical Proofs' on page 14
- Found following appendix 'D - Connections to Related Mathematical Frameworks' on page 16
- Found following appendix 'E - MA-MPPI Algorithm Details' on page 16
- Found following appendix 'F - Topological Feature Detection Details' on page 17
- Found following appendix 'G - Adaptive Potential Field Synthesis Details' on page 19
- Found following appendix 'H - Additional Details of Robotic Control Experiments' on page 21
- Found following appendix 'I - Additional Details of Complex Engineering Systems Experiments' on page 26
- Found following appendix 'J - Hyperparameter Sensitivity Analysis' on page 29
- Found following appendix 'K - Analysis of Generalization Limitations' on page 31
##########################################################
# Starting Literature Check
##########################################################
Checking references on pages: 11 -- 12
All found references: 19
-----------
 -> Parsed references DataFrame:
   ref_id                                            authors  ... link  valid
0       1  Greg Brockman, Vicki Cheung, Ludwig Pettersson...  ...        None
1       2  Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, ...  ...        None
2       3  Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, a...  ...        None
3       4  Mingliang Han, Bingni W Wei, Phelan Senatus, J...  ...        None
4       5  Nicolas Heess, Jonathan J Hunt, Timothy P Lill...  ...        None
5       6  Shaoshuai Jiang, Rongzhi Zhang, Weiyu Li, Jian...  ...        None
6       7  Chi Jin, Rong Ge, Praneeth Netrapalli, Sham M ...  ...        None
7       8                 Daniel E Koditschek and Elon Rimon  ...        None
8       9  Timothy P Lillicrap, Jonathan J Hunt, Alexande...  ...        None
9      10  Bethany Lusch, J Nathan Kutz, and Steven L Bru...  ...        None
10     11  Anusha Nagabandi, Gregory Kahn, Ronald S Feari...  ...        None
11     12  Mario Paolone, Trevor Gaunt, Xavier Guillaud, ...  ...        None
12     13  Alexander Pritzel, Benigno Uria, Sriram Sriniv...  ...        None
13     14  John Schulman, Filip Wolski, Prafulla Dhariwal...  ...        None
14     15         Yuval Tassa, Tom Erez, and Emanuel Todorov  ...        None
15     16  Evangelos Theodorou, Jonas Buchli, and Stefan ...  ...        None
16     17         Emanuel Todorov, Tom Erez, and Yuval Tassa  ...        None
17     18  Grady Williams, Andrew Aldrich, and Evangelos ...  ...        None
18     19  Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benj...  ...        None

[19 rows x 10 columns]
- Checking reference 1/19:
  -> INFO: Now checking 10 results for matching title: 'Openai gym'
       -> INFO: All authors matched!
- Checking reference 2/19:
  -> INFO: Now checking 10 results for matching title: 'Diffusion policy: Visuomotor policy learning via action diffusion'
       -> INFO: All authors matched!
- Checking reference 3/19:
  -> INFO: Now checking 10 results for matching title: 'Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor'
       -> INFO: All authors matched!
- Checking reference 4/19:
  -> INFO: Now checking 10 results for matching title: 'Deep koopman operator: A model-free approach to nonlinear dynamical systems'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Han', 'Wei', 'Senatus', 'Winkel', 'Youngblood', 'Lee', 'Mandell', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=Deep+koopman+operator:+A+model-free+approach+to+nonlinear+dynamical+systems manually and check the results.
        -> Author(s): Mingliang Han, Bingni W Wei, Phelan Senatus, Jörg D Winkel, Mason Youngblood, I-Han Lee, and David J Mandell
        -> Title:     Deep koopman operator: A model-free approach to nonlinear dynamical systems
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 5/19:
  -> INFO: Now checking 10 results for matching title: 'Memory-based control with recurrent neural networks'
       -> INFO: All authors matched!
- Checking reference 6/19:
  -> INFO: Now checking 2 results for matching title: 'Motion transformer with global intention localization and local movement refinement'
       -> WARNING: Not all 4 authors from the found ref. were matched (only 1)
                   Unmatched authors = 'Shi, Dai, Schiele'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 7/19:
  -> INFO: Now checking 10 results for matching title: 'How to escape saddle points efficiently'
       -> INFO: All authors matched!
- Checking reference 8/19:
  -> INFO: Now checking 5 results for matching title: 'Robot navigation functions on manifolds with boundary'
       -> WARNING: Not all 1 authors from the found ref. were matched (only 1)
                   Unmatched authors = ''
  -> INFO: No perfect match found; taking the next best!
- Checking reference 9/19:
  -> INFO: Now checking 10 results for matching title: 'Continuous control with deep reinforcement learning'
       -> INFO: All authors matched!
       -> WARNING: Year (2015) does not match expected year (2016)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 10/19:
  -> INFO: Now checking 6 results for matching title: 'Deep learning for universal linear embeddings of nonlinear dynamics'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 11/19:
  -> INFO: Now checking 10 results for matching title: 'Neural network dynamics for model-based deep reinforcement learning with model-free fine-tuning'
       -> INFO: All authors matched!
       -> WARNING: Year (2017) does not match expected year (2018)!
  -> INFO: No perfect match found; taking the next best!
- Checking reference 12/19:
  -> INFO: Now checking 10 results for matching title: 'A benchmark model for power system stability controls'
  -> WARNING: None of the 10 results matched the expected title!
  => ERROR loading dblp result as JSON: 'hit'
     -> dblp search was done with these keywords: ['Paolone', 'Gaunt', 'Guillaud', 'Liserre', 'Meliopoulos', 'Monti', 'Cutsem', 'Vittal', 'Vournas', '2020']
  -> WARNING: No results were found through the dblp search!
     -> You could also open https://scholar.google.com/scholar?hl=en&q=A+benchmark+model+for+power+system+stability+controls manually and check the results.
        -> Author(s): Mario Paolone, Trevor Gaunt, Xavier Guillaud, Marco Liserre, Sakis Meliopoulos, Antonello Monti, Thierry Van Cutsem, Vijay Vittal, and Costas Vournas
        -> Title:     A benchmark model for power system stability controls
        -> Year:      2020
     -> Manual search was skipped by the user.
- Checking reference 13/19:
  -> INFO: Now checking 10 results for matching title: 'Neural episodic control'
       -> INFO: All authors matched!
- Checking reference 14/19:
  -> INFO: Now checking 10 results for matching title: 'Proximal policy optimization algorithms'
       -> INFO: All authors matched!
- Checking reference 15/19:
  -> INFO: Now checking 10 results for matching title: 'Control-limited differential dynamic programming'
       -> WARNING: Not all 3 authors from the found ref. were matched (only 2)
                   Unmatched authors = 'Mansard'
  -> INFO: No perfect match found; taking the next best!
- Checking reference 16/19:
  -> INFO: Now checking 10 results for matching title: 'A generalized path integral control approach to reinforcement learning'
       -> INFO: All authors matched!
- Checking reference 17/19:
  -> INFO: Now checking 10 results for matching title: 'Mujoco: A physics engine for model-based control'
       -> INFO: All authors matched!
- Checking reference 18/19:
  -> INFO: Now checking 10 results for matching title: 'Model predictive path integral control: From theory to parallel computation'
       -> INFO: All authors matched!
- Checking reference 19/19:
  -> INFO: Now checking 10 results for matching title: 'Understanding deep learning requires rethinking generalization'
       -> INFO: All authors matched!
       -> WARNING: Year (2016) does not match expected year (2017)!
  -> INFO: No perfect match found; taking the next best!
-> Starting the sorting of mismatching entries!
##########################################################
# Starting Unicode Check
##########################################################
-> Invalid unicode use found on p. 2: covariance matrix. The objective is to find a control sequence u = {u0, u1, . . . , uT −1} that minimizes
-> Invalid unicode use found on p. 2: "T −1
-> Invalid unicode use found on p. 2: −1
-> Invalid unicode use found on p. 2: −1
-> Invalid unicode use found on p. 2: V (x, M) = α(x, M) · Vbase(x) + (1 −α(x, M)) · Vmem(x, M)
-> Invalid unicode use found on p. 3: Theorem 3.1 (Non-convex Escape Property). Let B(mi, ri) = {x ∈Rn : ∥x −mi∥≤ri} be
-> Invalid unicode use found on p. 3: P (∃t ≤Tescape(δ) : xt /∈B(mi, ri) | x0 ∈B(mi, ri)) ≥1 −δ
-> Invalid unicode use found on p. 3: t≥Tconv(ϵ,δ) ∥xt −x∗∥≤ϵ
-> Invalid unicode use found on p. 3: ≥1 −δ
-> Invalid unicode use found on p. 4: ˜V (x, Mt) = α(x, Mt)Vbase(x) + (1 −α(x, Mt))Vmem(x, Mt)
-> Invalid unicode use found on p. 4: λ(xt, Mt) = λ0(1 + η(1 −α(xt, Mt)))
-> Invalid unicode use found on p. 4: exp(−1
-> Invalid unicode use found on p. 4: i=1 exp(−1
-> Invalid unicode use found on p. 6: ˜V (x, Mt) = α(x, Mt)Vbase(x) + (1 −α(x, Mt))Vmem(x, Mt)
-> Invalid unicode use found on p. 6: λ(x, Mt) = λ0 · (1 + η · (1 −α(x, Mt)))
-> Invalid unicode use found on p. 7: represents measured outputs. The control objective is minu0:T −1
-> Invalid unicode use found on p. 7: PT −1
-> Invalid unicode use found on p. 8: mR · f −kd∥v∥v
-> Invalid unicode use found on p. 8: ˙ω = J−1(τ −ω × Jω)
-> Invalid unicode use found on p. 11: if ∥xt −mi∥≤ri and stagnating
-> Invalid unicode use found on p. 11: if ∥xt −mi∥> ri for t > tthreshold
-> Invalid unicode use found on p. 12: Var({xt−w, xt−w+1, ..., xt}) < θvar
-> Invalid unicode use found on p. 12: i∈{1,2,...,|M|} ∥xt −mi∥> θdist
-> Invalid unicode use found on p. 12: 1 −∥x −mi∥2
-> Invalid unicode use found on p. 12: 1 −∥x −mi∥2
-> Invalid unicode use found on p. 12: · (di · (x −mi))
-> Invalid unicode use found on p. 13: 1 −∥x −mi∥2
-> Invalid unicode use found on p. 13: · ((di · (x −mi))2 −∥(I −didT
-> Invalid unicode use found on p. 13: i )(x −mi)∥2)
-> Invalid unicode use found on p. 13: ∥x −mi∥
-> Invalid unicode use found on p. 13: 1+e−z is the sigmoid function and β > 0 controls the sharpness of the transition
-> Invalid unicode use found on p. 13: ∇V (x, M) = α(x, M) · ∇Vbase(x) + (1 −α(x, M)) · ∇Vmem(x, M)
-> Invalid unicode use found on p. 13: + ∇α(x, M) · (Vbase(x) −Vmem(x, M))
-> Invalid unicode use found on p. 13: Since x ∈B(mi, ri), we have ∥x −mi∥≤ri, and the dominant memory feature is precisely the
-> Invalid unicode use found on p. 13: ∇ϕ1(x, mi, ri) = −4
-> Invalid unicode use found on p. 13: 1 −∥x −mi∥2
-> Invalid unicode use found on p. 13: · (x −mi)
-> Invalid unicode use found on p. 13: region within finite time with probability at least 1 −δ.
-> Invalid unicode use found on p. 14: P(∃t ≤T1(δ/2) : xt ∈B) ≥1 −δ/2
-> Invalid unicode use found on p. 14: t≥T2(ϵ,δ/2) ∥xt −x∗∥≤ϵ | xT1(δ/2) ∈B
-> Invalid unicode use found on p. 14: ≥1 −δ/2
-> Invalid unicode use found on p. 14: t≥T1(δ/2)+T2(ϵ,δ/2) ∥xt −x∗∥≤ϵ
-> Invalid unicode use found on p. 14: t≥T2(ϵ,δ/2) ∥xt −x∗∥≤ϵ | xT1(δ/2) ∈B
-> Invalid unicode use found on p. 14: ≥(1 −δ/2) · (1 −δ/2)
-> Invalid unicode use found on p. 14: = 1 −δ + δ2
-> Invalid unicode use found on p. 14: ≥1 −δ
-> Invalid unicode use found on p. 14: t≥Tconv(ϵ,δ) ∥xt −x∗∥≤ϵ
-> Invalid unicode use found on p. 14: ≥1 −δ
-> Invalid unicode use found on p. 15: times, and we can model Ni as a geometric random variable with parameter (1 −qi), where qi is the
-> Invalid unicode use found on p. 15: 1−qi .
-> Invalid unicode use found on p. 15: gradient of the value function. The base value function generates a gradient flow ˙x = −∇Vbase(x)
-> Invalid unicode use found on p. 15: −∇V (x, M) where previously stable equilibria become unstable or are eliminated entirely, creating
-> Invalid unicode use found on p. 16: if ∥xt −mi∥≤ri and stagnating
-> Invalid unicode use found on p. 16: if ∥xt −mi∥> ri for t > tthreshold
-> Invalid unicode use found on p. 16: ∇˜V (x, Mt) = α(x, Mt)∇Vbase(x) + (1 −α(x, Mt))∇Vmem(x, Mt)
-> Invalid unicode use found on p. 16: + ∇α(x, Mt) · (Vbase(x) −Vmem(x, Mt))
-> Invalid unicode use found on p. 16: Σu(xt, Mt) = Σu,0 · (1 + µ · (1 −α(xt, Mt)))
-> Invalid unicode use found on p. 16: with weights wk = exp(−1
-> Invalid unicode use found on p. 16: i=t−K+1
-> Invalid unicode use found on p. 16: ||xi −¯xt||2
-> Invalid unicode use found on p. 17: ∇Vbase(xt) · ∇Vbase(xt−1)
-> Invalid unicode use found on p. 17: ||∇Vbase(xt)|| · ||∇Vbase(xt−1)||
-> Invalid unicode use found on p. 17: −1
-> Invalid unicode use found on p. 17: Merge if: ||mnew −mi||
-> Invalid unicode use found on p. 18: ri, rnew, ||mi −mnew||
-> Invalid unicode use found on p. 18: if ||xt −mi|| ≤ri and Var(Xt) < θvar
-> Invalid unicode use found on p. 18: if ||xt −mi|| > ri for t > tthreshold
-> Invalid unicode use found on p. 19: 1 −||x −mi||2
-> Invalid unicode use found on p. 19: 1 −||x −mi||2
-> Invalid unicode use found on p. 19: · (di · (x −mi))
-> Invalid unicode use found on p. 19: 1 −||x −mi||2
-> Invalid unicode use found on p. 19: (di · (x −mi))2
-> Invalid unicode use found on p. 19: ||x −mi||2
-> Invalid unicode use found on p. 19: −β
-> Invalid unicode use found on p. 19: 0, 1 −||x −mi||
-> Invalid unicode use found on p. 19: λ(x, Mt) = λ0 · (1 + η · (1 −α(x, Mt)))
-> Invalid unicode use found on p. 20: ϕκi(x, mi, ri, di) = 0 if ||x −mi|| > ri
-> Invalid unicode use found on p. 26: constrained to f ∈[0, 30] N and τ ∈[−0.5, 0.5] Nm.
##########################################################
# Starting Reference-Bibliography-Comparision
##########################################################
-> Processing set references in the doc's text... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Processed 410 sentences on 11 pages -> Avg. of 42.0 sentences per page
---
-> Missing an abstract for reference with index 0 (Ref. ID = 1); Skipping LLM check...
-> Missing an abstract for reference with index 1 (Ref. ID = 2); Skipping LLM check...
-> Missing an abstract for reference with index 2 (Ref. ID = 3); Skipping LLM check...
-> Missing an abstract for reference with index 3 (Ref. ID = 4); Skipping LLM check...
-> Missing an abstract for reference with index 4 (Ref. ID = 5); Skipping LLM check...
  // LLM calling counter = 1
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 6 (Ref. ID = 7); Skipping LLM check...
-> Missing an abstract for reference with index 7 (Ref. ID = 8); Skipping LLM check...
  // LLM calling counter = 2
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 3
  -> Automatic parsing of LLM list worked!
  // LLM calling counter = 4
  -> Automatic parsing of LLM list worked!
-> Missing an abstract for reference with index 11 (Ref. ID = 12); Skipping LLM check...
-> Missing an abstract for reference with index 12 (Ref. ID = 13); Skipping LLM check...
-> Missing an abstract for reference with index 13 (Ref. ID = 14); Skipping LLM check...
-> Missing an abstract for reference with index 14 (Ref. ID = 15); Skipping LLM check...
-> Missing an abstract for reference with index 15 (Ref. ID = 16); Skipping LLM check...
-> Missing an abstract for reference with index 16 (Ref. ID = 17); Skipping LLM check...
-> Missing an abstract for reference with index 17 (Ref. ID = 18); Skipping LLM check...
  // LLM calling counter = 5
  -> Automatic parsing of LLM list worked!
###############################
# Starting Ranking Check
###############################
-> Loading rankings and iterating them; please wait, this might take a minute!
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
  -> Found 1 matches in this ranking!
-> Now checking the journal impact factors:
  -> Processing initial impact_factor check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
  -> Found 7 matches in this ranking!
-> Fallback activated. Now matching the JQ proceedings and the parsed outlets using an LLM:
  // LLM calling counter = 6
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the JQ jounrals and the parsed outlets using an LLM:
  // LLM calling counter = 7
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM jq_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE A+ - B rankings and the parsed outlets using an LLM:
  // LLM calling counter = 8
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the CORE C rankings and the parsed outlets using an LLM:
  // LLM calling counter = 9
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
-> Now matching the remaining CORE rankings and the parsed outlets using an LLM:
  // LLM calling counter = 10
  -> Automatic parsing of LLM DF worked!
  -> Processing LLM core_ranking check... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
###############################
# Starting Author Check
###############################
---
FINISHED!
 -> Results saved to C:...\PAU - All  GPTZero NeurIPS Paper with H\6 Memory-Augmented Potential Field Theory\PAU_results.md
```