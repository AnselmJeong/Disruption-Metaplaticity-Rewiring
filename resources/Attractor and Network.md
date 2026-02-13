# Research Report

## Executive Summary

The mathematical formalization of attractor dynamics provides a rigorous framework for understanding how neural populations encode, maintain, and transition between behaviorally relevant states through stable configurations determined by network connectivity patterns. Attractor neural networks, conceptualized as dynamical systems in which activity evolves toward stable configurations, offer a principled account of persistent neural activity, working memory, and the computational properties of recurrent circuits ([Dominguez et al. 2007](https://doi.org/10.1162/neco.2007.19.4.956)). The relationship between neural connectivity patterns and attractor landscape geometry constitutes a central problem in computational neuroscience, with theoretical work establishing fundamental principles whereby connection weights determine the location, depth, and basin geometry of stable attractor states ([Zemel and Mozer 2001](https://doi.org/10.1162/08997660151134325)). Recent empirical evidence has validated these theoretical predictions, demonstrating that line attractors in hypothalamic circuits encode persistent behavioral states such as aggression ([Nair et al. 2023](https://doi.org/10.1016/j.cell.2022.11.027)), with causal manipulations confirming that connectivity perturbations directly alter attractor dynamics and associated behavioral outputs ([Vinograd et al. 2024](https://doi.org/10.1038/s41586-024-07915-x)).

Methodological advances in energy landscape analysis have enabled the inference of attractor configurations from empirical neuroimaging data through maximum entropy models that characterize the probability distribution of observed brain states ([Watanabe et al. 2014](https://doi.org/10.3389/fninf.2014.00012)). These approaches have revealed that structural and functional connectivity patterns shape the global organization of brain energy landscapes ([Kang et al. 2017](https://doi.org/10.1016/j.neuroimage.2017.01.075)), with altered connectivity in clinical populations producing distinct signatures of attractor landscape disruption. Investigations of local neuronal networks have further demonstrated that diluted connectivity patterns produce characteristic modifications in attractor dynamics ([Rolls and Webb 2012](https://doi.org/10.1016/j.brainres.2011.08.002)), while intrinsic attractor manifolds persist across wakefulness and sleep states, suggesting that connectivity-imposed constraints maintain stable computational properties despite varying behavioral conditions ([Chaudhuri et al. 2019](https://doi.org/10.1038/s41593-019-0460-x)).

The conceptualization of psychiatric and neurological disorders through attractor dynamics and connectivity frameworks represents a paradigm shift from categorical diagnostic approaches toward mechanistic accounts of brain network pathophysiology ([Montague et al. 2012](https://doi.org/10.1016/j.tics.2011.11.018)). Within this framework, mental illness can be understood as arising from maladaptive configurations of neural attractor landscapes, wherein aberrant structural and functional connectivity patterns generate pathological stable states ([Durstewitz et al. 2021](https://doi.org/10.1016/j.bpsc.2020.01.001)). Energy landscape analyses have identified disorder-specific alterations in brain state transitions across conditions including depression ([Regonia et al. 2021](https://doi.org/10.3389/fpsyt.2021.780997)), schizophrenia ([Rolls et al. 2021](https://doi.org/10.1038/s41398-021-01197-x)), ADHD ([Iravani et al. 2021](https://doi.org/10.1016/j.neuroimage.2021.117844)), Alzheimer's disease ([Jing et al. 2025](https://doi.org/10.1016/j.biopsych.2025.07.022)), and disorders of consciousness ([Núñez et al. 2025](https://doi.org/10.1016/j.neuroimage.2025.121519)), suggesting that connectivity-mediated attractor landscape changes may serve as transdiagnostic biomarkers and potential targets for therapeutic intervention.

## Theoretical Foundations: Attractor Dynamics in Neural Systems

The mathematical formalization of attractor dynamics provides a rigorous framework for understanding how neural populations encode, maintain, and transition between behaviorally relevant states. Attractor neural networks, conceived as dynamical systems in which network activity evolves toward stable configurations, offer a principled account of persistent neural activity, working memory, and the computational properties of recurrent circuits ([Dominguez et al. 2007](https://doi.org/10.1162/neco.2007.19.4.956)). The attractor landscape metaphor—wherein neural activity trajectories are conceptualized as flowing through a high-dimensional state space toward local minima—has proven remarkably generative for interpreting experimental observations across diverse neural systems and behavioral paradigms ([Balaguer-Ballester et al. 2017](https://doi.org/10.3389/fnsys.2017.00099)).

Fixed-point attractors represent the canonical and most extensively characterized attractor class in theoretical neuroscience. These configurations correspond to stable equilibria where network activity converges to and persists at specific locations in state space, providing a neural substrate for working memory and the maintenance of behavioral states over extended temporal intervals. Recent experimental work has provided compelling causal evidence for fixed-point attractor dynamics in mammalian hypothalamic circuits, where approximately line attractors encode persistent internal states underlying aggressive behaviors ([Nair et al. 2023](https://doi.org/10.1016/j.cell.2022.11.027)). Complementary investigations have established that these line attractor architectures encode affective states with causal necessity, demonstrating that optogenetic perturbation of the underlying neural population systematically shifts the encoded state along the attractor manifold ([Vinograd et al. 2024](https://doi.org/10.1038/s41586-024-07915-x)). The mathematical structure of line attractors—continuous families of fixed points forming a one-dimensional manifold—enables graded encoding of behavioral state intensity, a computational feature that discrete point attractors cannot readily implement ([Vinograd et al. 2024](https://doi.org/10.1101/2024.05.21.595051)). Similar continuous attractor dynamics have been characterized in the encoding of female mating dynamics, suggesting that hypothalamic circuits may employ a conserved attractor architecture for diverse social and reproductive behaviors ([Liu et al. 2024](https://doi.org/10.1038/s41586-024-07916-w)).

The head-direction system exemplifies continuous attractor dynamics in the domain of spatial cognition, where neural populations encode angular orientation through ring attractor architectures ([Ajabi et al. 2023](https://doi.org/10.1038/s41586-023-05813-2)). The intrinsic manifold structure of this system persists across behavioral states including sleep, indicating that the attractor topology is embedded in the circuit's recurrent connectivity rather than arising solely from moment-to-moment sensory input ([Chaudhuri et al. 2019](https://doi.org/10.1038/s41593-019-0460-x)). These findings illuminate a fundamental principle: that attractor geometries can be intrinsically structured by synaptic connectivity, providing computational stability in the face of environmental variability and neural noise.

Limit cycle attractors, characterized by oscillatory activity patterns that return to stable periodic trajectories following perturbation, constitute a second fundamental attractor class with broad relevance to neural computation. Such dynamics have been implicated in central pattern generation, rhythmic motor output, and temporal coordination of behavioral sequences ([Piñero and Solé 2019](https://doi.org/10.1098/rstb.2018.0376)). The hypothalamic regulation of reproductive cycles exhibits periodic attractor-like dynamics that unfold over the extended timescale of the estrus cycle, demonstrating that limit cycle architectures can operate across multiple temporal scales from millisecond-range oscillations to multi-day endocrine rhythms ([Liu et al. 2023](https://doi.org/10.1101/2023.05.22.541741)). The mathematical formalism of shot-noise-induced switching between attractor states has been developed to characterize transitions in two-population neural networks, providing analytical tools for understanding how stochastic fluctuations can drive transitions between metastable states ([Kirillov et al. 2024](https://doi.org/10.1063/5.0193275)).

Metastable states—quasi-stable configurations that persist transiently before transitioning to alternative states—have emerged as a unifying concept for understanding the temporal organization of naturalistic behavior ([Mazzucato 2022](https://doi.org/10.7554/eLife.76577)). Unlike fixed-point attractors, metastable configurations do not represent asymptotically stable equilibria but rather local minima in a landscape shaped by both intrinsic dynamics and ongoing perturbations. The editorial synthesis by Balaguer-Ballester and colleagues articulates how metastability enables the sequential activation of neural ensembles while maintaining sensitivity to contextual and input-driven modulations ([Balaguer-Ballester et al. 2017](https://doi.org/10.3389/fnsys.2017.00099)). This framework accommodates the observation that cortical population dynamics often exhibit structured trajectories through state space that do not settle into fixed points, yet maintain computational specificity and behavioral relevance.

The relationship between network topology and attractor dynamics constitutes a critical theoretical frontier. Small-world architectures, characterized by high local clustering and short characteristic path lengths, are hypothesized to support efficient information propagation while maintaining the segregated processing necessary for multiple coexisting attractors ([Dominguez et al. 2007](https://doi.org/10.1162/neco.2007.19.4.956)). Scale-free topologies, with their heavy-tailed degree distributions, may confer robustness to random node failure while supporting rapid integration of activity across spatially distributed neural populations. The modular organization observed throughout the mammalian brain may reflect an optimal structure for implementing multiple semi-independent attractor networks that can be flexibly coupled or decoupled according to task demands ([Piñero and Solé 2019](https://doi.org/10.1098/rstb.2018.0376)). Information-theoretic analyses have demonstrated that the storage capacity and retrieval fidelity of attractor networks depend critically on the underlying connectivity structure, with implications for understanding both computational capabilities and pathological dynamics in neural systems ([Dominguez et al. 2007](https://doi.org/10.1162/neco.2007.19.4.956)).

Theoretical advances have enabled the constructive design of neural networks with pre-specified attractor dynamics, providing critical tests of the relationship between circuit structure and computational function ([Mininni and Zanutto 2024](https://doi.org/10.1038/s41598-024-69747-z)). Such inverse approaches complement traditional forward modeling by establishing whether hypothesized connectivity patterns are sufficient to generate observed dynamics. Expressive architectures for dynamics-based neural population models have enhanced the interpretability of learned dynamics, enabling researchers to extract explicit dynamical systems characterizations from high-dimensional neural recordings ([Sedler et al. 2023](https://doi.org/10.51628/001c.73987)). These methodological advances are essential for bridging the gap between phenomenological descriptions of neural population trajectories and mechanistic accounts of the underlying circuit dynamics.

Motor planning circuits in the premotor and supplementary motor areas have provided a productive model system for investigating attractor dynamics in the context of action preparation. The dynamics and geometry of choice in premotor cortex reveal that motor planning unfolds as a trajectory through a low-dimensional neural manifold, with decision variables encoded as the initial conditions from which trajectories evolve toward action-specific attractor basins ([Genkin et al. 2025](https://doi.org/10.1038/s41586-025-09199-1)). This geometry enables rapid action initiation while maintaining the capacity for ongoing modification of the planned response. Computational frameworks for motor planning emphasize that recurrent network dynamics can implement the integration of sensory evidence with internal goals, generating preparatory activity patterns that anticipate forthcoming movements ([Inagaki et al. 2022](https://doi.org/10.1146/annurev-neuro-092021-121730)).

The population dynamics of synaptic modulation and reward computation demonstrate that attractor frameworks extend beyond persistent activity patterns to encompass the dynamics of neuromodulatory systems themselves. Cell-type-specific analyses have revealed that distinct populations within reward circuits implement heterogeneous computational operations, with dopamine neuron subpopulations exhibiting differential encoding of reward prediction errors and state values ([Sylwestrak et al. 2022](https://doi.org/10.1016/j.cell.2022.08.019)). The neural population dynamics of computing with synaptic modulations indicates that neuromodulatory inputs can reshape attractor landscapes on multiple timescales, enabling context-dependent reconfiguration of circuit dynamics ([Aitken and Mihalas 2023](https://doi.org/10.7554/eLife.83035)). This perspective accommodates the observation that identical circuits can support distinct computational functions under different modulatory states, with attractor basins and barriers reconfigured by the balance of inhibitory and excitatory transmission.

Task-dependent recurrent dynamics in sensory cortex illustrate how attractor structures can be dynamically modulated by behavioral context and task demands. Visual cortical population dynamics exhibit structured trajectories that reflect both stimulus-driven responses and task-dependent recurrent interactions, with the latter enabling the integration of sensory input with behavioral state and prior expectations ([Tajima et al. 2017](https://doi.org/10.7554/eLife.26868)). These findings resonate with theoretical frameworks that conceptualize cortical circuits as implementing approximate inference through attractor dynamics, wherein neural activity settles into configurations that encode posterior beliefs over latent variables ([Kotler et al. 2025](https://doi.org/10.1038/s42003-025-08612-9)). The pathfinding framework for intuition extends these principles to propose that heuristically efficient decision-making emerges from attractor dynamics that encode learned statistical regularities of the environment, enabling rapid convergence to adaptive choices without exhaustive evaluation of alternatives.

The mathematical machinery of dynamical systems theory—comprising stability analysis, bifurcation theory, and phase space geometry—provides essential analytical tools for characterizing neural attractors. Linear stability analysis determines whether fixed points are stable (attracting) or unstable (repelling), while bifurcation analysis characterizes how attractor structure transforms with changes in parameters such as synaptic weights or external input ([Kirillov et al. 2024](https://doi.org/10.1063/5.0193275)). The concept of the attractor basin—the set of initial conditions that converge to a given attractor—provides a natural framework for understanding neural computation as classification or categorization, with basin boundaries implementing decision surfaces ([Inagaki et al. 2022](https://doi.org/10.1146/annurev-neuro-092021-121730)). Nullcline analysis and phase plane methods enable visualization of attractor structure in low-dimensional systems, while dimensionality reduction techniques permit analogous visualization of dynamics extracted from high-dimensional neural recordings ([Sedler et al. 2023](https://doi.org/10.51628/001c.73987)).

The synthesis of these theoretical and empirical advances establishes attractor dynamics as a central organizing principle for understanding neural computation across spatial and temporal scales. From the millisecond-scale oscillations of central pattern generators to the multi-day dynamics of endocrine cycles, from the rapid decisions of premotor cortex to the persistent states of hypothalamic behavioral control, attractor frameworks provide mathematical precision for characterizing how neural circuits implement the computational operations underlying behavior. The continued integration of dynamical systems theory with large-scale neural recording, optogenetic perturbation, and sophisticated modeling approaches promises to deepen our understanding of how attractor architectures are implemented in biological circuits and how their dysfunction may contribute to psychiatric and neurological disease.

## Connectivity-Attractor Mapping: Empirical and Computational Evidence

The relationship between neural connectivity patterns and attractor landscape geometry constitutes a central problem in computational neuroscience, with implications for understanding both normal cognitive function and pathological brain states. Theoretical work on localist attractor networks has established fundamental principles whereby connection weights determine the location, depth, and basin geometry of stable attractor states ([Zemel and Mozer 2001](https://doi.org/10.1162/08997660151134325)), providing a mathematical framework for predicting how structural connectivity alterations reshape dynamical landscapes. This connectivity-attractor mapping has been extensively characterized across multiple modeling scales, from abstract Hopfield-type networks to biophysically detailed spiking models.

In local neuronal circuits, attractor dynamics emerge from recurrent connectivity patterns that generate persistent activity states capable of maintaining information over behaviorally relevant timescales. Comprehensive analysis of local attractor networks has demonstrated that the number and stability of attractor states scale non-linearly with connectivity density and synaptic weight distributions ([Thivierge et al. 2014](https://doi.org/10.3389/fncir.2014.00022)). Crucially, diluted connectivity—wherein only a subset of possible connections are instantiated—fundamentally alters attractor basin geometry, producing shallower basins with broader attractor regions that may confer advantages for computational flexibility while compromising memory stability ([Rolls and Webb 2012](https://doi.org/10.1016/j.brainres.2011.08.002)). These computational predictions align with empirical observations that cortical networks operate with sparse connectivity yet maintain robust mnemonic representations, suggesting evolutionary optimization for a balance between stability and adaptability.

The hippocampal CA3 region has served as a model system for investigating connectivity-attractor relationships due to its highly recurrent circuit architecture. Detailed computational models incorporating realistic excitatory-inhibitory balance and synaptic dynamics have identified signatures of attractor dynamics in CA3, including pattern completion and competitive interactions between memory representations ([Rennó-Costa et al. 2014](https://doi.org/10.1371/journal.pcbi.1003641)). These models demonstrate that modifications to recurrent excitation strength or inhibitory feedback reshape attractor basins in predictable ways: strengthened excitation deepens basins and enhances stability but risks pathological attractor states, whereas enhanced inhibition flattens the landscape and promotes rapid transitions between states.

Task-dependent modulation of connectivity provides a mechanistic basis for dynamic attractor landscape reconfiguration. Investigation of recurrent dynamics in visual cortex has revealed that top-down inputs and task context alter effective connectivity in ways that reshape attractor basins to favor task-relevant states ([Tajima et al. 2017](https://doi.org/10.7554/eLife.26868)). This dynamic reconfiguration suggests that attractor landscapes are not static architectural features but rather continuously remodeled by neuromodulatory and activity-dependent processes. The free energy principle provides a unifying theoretical account whereby the brain dynamically adjusts its connectivity to minimize surprise, with attractor basins corresponding to prior expectations and connectivity changes implementing Bayesian belief updating ([Kim 2018](https://doi.org/10.1162/neco_a_01115)).

Whole-brain imaging studies have extended connectivity-attractor mapping beyond local circuits to examine how large-scale network architecture constrains global dynamical landscapes. Energy landscape analysis applied to resting-state fMRI data has demonstrated that brain networks occupy metastable states near critical points, enabling rapid transitions between functional configurations while maintaining overall dynamical stability ([Watanabe et al. 2014](https://doi.org/10.3389/fninf.2014.00012)). The structural connectome appears to establish boundary conditions on accessible attractor states, with hub regions particularly influential in determining landscape geometry. Sensory-motor cortices exert disproportionate influence over functional connectivity dynamics, effectively anchoring attractor basins that constrain the brain's dynamical repertoire ([Kong et al. 2021](https://doi.org/10.1038/s41467-021-26704-y)).

Clinical neuroimaging studies have begun translating connectivity-attractor mapping to understand pathological brain states. Whole-brain modeling of resting-state dynamics in attention-deficit/hyperactivity disorder has revealed subtype-specific alterations in attractor landscape geometry, with different clinical presentations characterized by distinct patterns of basin deepening and shallowing across distributed networks ([Iravani et al. 2021](https://doi.org/10.1016/j.neuroimage.2021.117844)). These findings suggest that psychiatric conditions may reflect not merely connectivity abnormalities but fundamental reshaping of neural attractor landscapes, potentially explaining the stability of pathological states and resistance to intervention.

Electrophysiological investigations provide complementary evidence with superior temporal resolution for examining attractor dynamics during state transitions. Analysis of highly nonstationary electroencephalographic recordings has identified characteristic fluctuations around stable attractor configurations, with transitions between attractors producing distinctive electrophysiological signatures ([Olguín-Rodríguez et al. 2018](https://doi.org/10.1089/brain.2018.0609)). Studies of awakening from anesthesia have proven particularly informative, demonstrating that the transition from unconsciousness to consciousness involves progressive emergence of competing attractor states that enrich cortical dynamics ([Tort-Colet et al. 2021](https://doi.org/10.1016/j.celrep.2021.109270)). The competition between nascent attractors during state transitions suggests that connectivity changes associated with arousal systems reshape the landscape geometry in real-time, enabling access to previously inaccessible dynamical configurations.

Place cell and grid cell systems in the hippocampal-entorhinal circuit provide compelling evidence for connectivity-dependent attractor dynamics in spatial navigation. Neural dynamics in these systems indicate parallel integration of environmental and self-motion information, with attractor networks in medial entorhinal cortex providing continuous attractor manifolds that support path integration ([Laptev and Burgess 2019](https://doi.org/10.3389/fncir.2019.00059)). The continuous attractor model predicts that connectivity patterns encoding spatial relationships generate two-dimensional attractor sheets, with bumps of activity representing position within the manifold. Alterations to inhibitory connectivity disrupt these continuous attractors, producing fragmented spatial representations and impaired navigation.

Computational neurostimulation studies have begun elucidating how therapeutic interventions might reshape attractor landscapes through targeted connectivity modulation. Transcranial direct current stimulation (tDCS) produces nonlinear physiological and behavioral effects that can be understood through the lens of attractor dynamics: weak perturbations may push the system between basins, whereas stronger stimulation may fundamentally alter landscape geometry ([Bonaiuto and Bestmann 2015](https://doi.org/10.1016/bs.pbr.2015.06.013)). These models suggest that therapeutic efficacy depends critically on initial attractor configuration and the relationship between stimulation parameters and basin geometry, potentially explaining variable treatment responses across individuals.

Recent theoretical work has critically examined limitations of attractor-based formalisms for understanding biological computation. Analysis of transient dynamics in neural systems has emphasized that much of cognition may operate through trajectories rather than equilibrium states, with connectivity patterns sculpting flow fields rather than simply carving attractor basins ([Koch et al. 2024](https://doi.org/10.1016/j.bbrc.2024.150069)). This perspective suggests that pure attractor models may incompletely capture neural computation, particularly for processes requiring rapid sequential processing rather than stable maintenance. The integration of transient and attractor dynamics within unified theoretical frameworks represents an active area of investigation, with implications for interpreting connectivity-landscape relationships.

Methodologically, attractor landscape analysis has benefited from computational tools enabling systematic characterization of network dynamics. While originally developed for cellular regulatory networks, landscape analysis approaches have been adapted for neural systems, permitting quantitative mapping between connectivity parameters and basin geometry ([Shah et al. 2018](https://doi.org/10.1038/s41598-018-22031-3)). Monte Carlo methods for simulating landscape topography with intermediate detail have proven valuable for visualizing how connectivity changes reshape attractor configurations ([Zhang et al. 2020](https://doi.org/10.1016/j.biosystems.2020.104275)), though challenges remain in scaling these approaches to whole-brain networks with realistic connectivity patterns.

The convergence of computational modeling, neuroimaging, and electrophysiological evidence supports a mechanistic framework wherein structural and functional connectivity alterations produce predictable changes in attractor landscape geometry. Strong recurrent excitation generates deep, stable basins resistant to perturbation but potentially trapping the system in pathological states. Diluted or weakened connectivity produces shallow basins enabling rapid state transitions but compromising memory stability. Inhibitory circuitry shapes basin boundaries and determines competition between co-active attractors. These principles, established through computational models and validated against empirical data, provide a foundation for understanding how connectivity abnormalities in psychiatric and neurological disorders produce characteristic dynamical signatures, and for designing interventions that therapeutically reshape attractor landscapes.

## Methodological Approaches for Quantifying Landscape-Connectivity Relationships

The quantification of relationships between neural connectivity patterns and attractor landscape dynamics requires the integration of multiple methodological frameworks spanning statistical physics, network neuroscience, and computational modeling. Central to these approaches is the inference of energy landscapes from empirical neuroimaging data, predominantly through maximum entropy models that characterize the probability distribution of observed brain states. The maximum entropy principle constrains the model to match empirically observed pairwise correlations while maximizing entropy, thereby yielding the most parsimonious statistical description consistent with available data ([Kang et al. 2017](https://doi.org/10.1016/j.neuroimage.2017.01.075)). This framework enables the construction of an energy function E(s) for each binary brain state configuration s, where lower energy states correspond to higher probability configurations and represent stable attractors in the neural state space.

The mathematical foundation for energy landscape construction derives from the relationship between the Boltzmann distribution P(s) ∝ exp(-E(s)/T) and the inverse problem of inferring parameters that reproduce observed statistics. Recent methodological advances have introduced Bayesian estimation frameworks for individualized energy landscape analysis, addressing limitations of group-level inference by incorporating prior distributions that regularize parameter estimation and improve generalizability to individual subjects ([Kang et al. 2021](https://doi.org/10.1002/hbm.25442)). These approaches prove particularly valuable for characterizing individual differences in brain dynamics and may enhance the translational utility of energy landscape metrics for clinical applications.

Langevin dynamics approximations provide a complementary theoretical framework for understanding transitions between metastable states on the energy landscape. The derivation of invariant free-energy landscapes from Langevin dynamics has established rigorous connections between stochastic differential equations governing neural dynamics and the topological features of attractor basins ([Nakamura 2024](https://doi.org/10.1103/PhysRevLett.132.137101)). This approach captures the interplay between deterministic drift forces arising from the gradient of the potential landscape and stochastic fluctuations that enable transitions between local minima. The non-Markovian characteristics of these transitions have been recognized as essential features, with memory effects substantially influencing transition pathways and kinetics between brain states ([Ayaz et al. 2021](https://doi.org/10.1073/pnas.2023856118)).

Energy landscape analysis has been extensively applied to characterize pathological alterations in neurological and psychiatric conditions. In Alzheimer's disease, multicenter cohort studies have demonstrated altered energy landscape configurations that distinguish patients from healthy controls, with specific basin structures correlating with cognitive decline severity ([Jing et al. 2025](https://doi.org/10.1016/j.biopsych.2025.07.022)). Independent investigations have corroborated these findings, identifying aberrant energy landscapes in prodromal stages of cognitive impairment and suggesting potential utility as early biomarkers ([Xing et al. 2024](https://doi.org/10.3389/fnagi.2024.1375091)). Similarly, depression and melancholia exhibit heterogeneous alterations in brain state dynamics that can be quantified through energy landscape topography, revealing distinct patterns associated with clinical subtypes ([Regonia et al. 2021](https://doi.org/10.3389/fpsyt.2021.780997)).

The extension of energy landscape methods to clinical biomarker development has progressed through machine learning integration. Functional connectivity biomarker extraction in schizophrenia has leveraged energy landscape features to identify reproducible signatures of dysconnectivity, achieving classification performance that suggests clinical utility ([Allen et al. 2024](https://doi.org/10.3390/s24237742)). Cross-diagnostic investigations comparing schizophrenia and mood disorders have revealed both shared and distinct alterations in large-scale network dynamics, with energy landscape metrics capturing transdiagnostic features of psychopathology ([Ishida et al. 2024](https://doi.org/10.1016/j.nicl.2024.103574)). In adolescent-onset schizophrenia specifically, the energy of functional brain states has demonstrated correlations with cognitive performance, linking landscape topology to behavioral phenotypes ([Theis et al. 2024](https://doi.org/10.1101/2023.11.06.565753)).

Subcortical network analyses have revealed fundamental system properties governing resting state dynamics, demonstrating that energy landscape configurations in basal ganglia and thalamic circuits exhibit characteristic attractor structures that constrain state transitions ([Kang et al. 2017](https://doi.org/10.1016/j.neuroimage.2017.01.075)). Critical appraisal of maximum entropy modeling approaches has identified methodological considerations including the choice of binarization thresholds, temporal autocorrelation handling, and generalization across scanning sessions, which require careful attention to ensure reproducibility ([Prasad et al. 2025](https://doi.org/10.21203/rs.3.rs-8428652/v1)).

Functional connectivity measurement approaches provide the empirical foundation for energy landscape inference, with resting-state functional MRI representing the predominant modality. Transcranial magnetic stimulation combined with electroencephalography offers an alternative approach for probing effective connectivity, enabling interrogation of causal interactions between brain regions and providing complementary information to correlation-based functional connectivity measures ([Gupta et al. 2023](https://doi.org/10.3390/s23084078)). The integration of pharmacological manipulation with connectivity analysis has revealed how GABAergic signaling modulates control network dynamics and influences landscape stability in conditions such as chronic insomnia ([Yu et al. 2025](https://doi.org/10.1038/s42003-025-08439-4)).

The relationship between network robustness and landscape stability has been examined in the context of pharmacological perturbation. Cocaine administration has been demonstrated to diminish functional network robustness and destabilize the energy landscape of neuronal activity in the medial prefrontal cortex, establishing causal links between neurochemical state and landscape topology ([Borzou et al. 2024](https://doi.org/10.1093/pnasnexus/pgae092)). Source localization methods combined with functional connectivity analysis have enabled examination of how network-level processes relate to behavioral phenomena, including the regulation of decision-making dynamics ([Xin et al. 2024](https://doi.org/10.1016/j.neuroscience.2024.01.016)).

Computational frameworks for mapping connectivity to dynamics increasingly integrate multiple analytical approaches within unified pipelines. The 25th Annual Computational Neuroscience Meeting highlighted numerous methodological advances in this domain, including dimensionality reduction techniques, network modeling approaches, and the integration of multi-scale data for constraining dynamical models ([Sharpee et al. 2016](https://doi.org/10.1186/s12868-016-0283-6)). The convergence of energy landscape analysis with other quantitative frameworks—including transcriptomic approaches for characterizing disease states ([Sneha et al. 2022](https://doi.org/10.3390/genes13122385)) and structural analyses of network assembly ([Lee and Arya 2022](https://doi.org/10.1039/d1nr07995f))—suggests opportunities for multi-modal integration in future investigations.

Mitochondrial respiratory capacity mapping has revealed regional heterogeneity in metabolic capacity across the human brain, establishing an anatomical substrate that may constrain the energetic requirements of state transitions on neural landscapes ([Mosharov et al. 2025](https://doi.org/10.1038/s41586-025-08740-6)). These findings suggest that metabolic constraints may fundamentally shape the accessibility of different regions of state space, with implications for understanding both normal brain dynamics and pathological alterations in conditions characterized by metabolic dysfunction.

## Clinical Implications: Psychiatric and Neurological Disorders

The conceptualization of psychiatric and neurological disorders through the lens of attractor dynamics and connectivity frameworks represents a paradigm shift from categorical diagnostic approaches toward a mechanistic understanding of brain network pathophysiology. Within this framework, mental illness can be understood as arising from maladaptive configurations of neural attractor landscapes, wherein aberrant structural and functional connectivity patterns generate pathological stable states, reduced basin depths, or inappropriate transitions between attractor states ([Durstewitz et al. 2021](https://doi.org/10.1016/j.bpsc.2020.01.001)). This perspective unifies diverse symptomatology under a common computational architecture, suggesting that phenomenologically distinct disorders may share fundamental dynamical mechanisms while differing in their anatomical loci and specific attractor configurations.

Schizophrenia provides a compelling exemplar of attractor dynamics gone awry, with multiple lines of evidence converging on disrupted connectivity patterns that fundamentally alter the landscape of accessible brain states. Temporal variability analyses have demonstrated that schizophrenia is characterized by altered dynamical connectivity patterns, with patients exhibiting reduced flexibility in transitioning between different network configurations compared to healthy controls ([Rolls et al. 2021](https://doi.org/10.1038/s41398-021-01197-x)). This rigidification of network dynamics can be understood within the attractor framework as an expansion of basin depths for certain pathological states, effectively trapping the system in maladaptive configurations. Working memory deficits, a cardinal feature of schizophrenia, have been modeled as arising from disturbed attractor dynamics in prefrontal circuits, where dopamine-mediated modulation of persistent activity states becomes dysregulated ([Durstewitz et al. 2000](https://doi.org/10.1038/81460)). The multi-timescale dynamics of midbrain dopamine neuronal firing exhibit characteristic alterations that may underlie these disturbances, with dopamine neurons displaying aberrant temporal patterns that disrupt the normal construction and maintenance of task-relevant attractors ([Zhao et al. 2023](https://doi.org/10.1016/j.jtbi.2022.111310)). Integrated network models of psychotic symptoms further suggest that hallucinations and delusions emerge from inappropriate stabilization of attractor states in sensory and belief-network circuits, respectively, with reduced competition between alternative interpretations leading to pathological certainty ([Looijestijn et al. 2015](https://doi.org/10.1016/j.neubiorev.2015.09.016)).

Major depressive disorder exemplifies how reward-processing circuitry can become trapped within maladaptive attractor configurations. Recent investigations have demonstrated that dopamine plays a crucial role in constructing and revealing reward-associated latent behavioral attractors, with dopamine release essentially sculpting the attractor landscape to bias future behavioral choices ([Naudé et al. 2024](https://doi.org/10.1038/s41467-024-53976-x)). In depression, this attractor-building capacity appears compromised, leading to impoverished repertoires of accessible motivational states. Cell-type-specific analyses of reward computations have revealed distinct population dynamics underlying different aspects of reward processing, suggesting that depression may involve selective disruption of specific computational channels rather than global reward circuit dysfunction ([Sylwestrak et al. 2022](https://doi.org/10.1016/j.cell.2022.08.019)). The "selfish network" hypothesis provides additional insight, proposing that the brain possesses intrinsic mechanisms to preserve behavioral function through shifts in neuronal network state, and that depression may represent a failure of these adaptive reconfiguration mechanisms ([Stroh et al. 2024](https://doi.org/10.1016/j.tins.2024.02.005)). The structural connections between the noradrenergic and cholinergic systems shape the dynamics of functional brain networks in ways that may be particularly relevant to depressive pathophysiology, as these neuromodulatory systems regulate the balance between network flexibility and stability ([Taylor et al. 2022](https://doi.org/10.1016/j.neuroimage.2022.119455)).

Disorders of consciousness represent perhaps the most extreme manifestation of attractor landscape pathology, wherein the system becomes trapped within configurations incompatible with aware wakefulness. Electrophysiological meta-state dynamics in patients with disorders of consciousness reveal profoundly altered attractor topologies, with reduced diversity of accessible states and impaired transitions between network configurations ([Núñez et al. 2025](https://doi.org/10.1016/j.neuroimage.2025.121519)). These findings suggest that consciousness requires not merely the integrity of specific anatomical structures but also the capacity for rich, flexible dynamics across a high-dimensional attractor landscape. The exploration of nonlinear dynamics through phase portraits and fuzzy recurrence plots has provided methodological advances for characterizing these pathological attractor configurations, offering quantitative metrics for assessing the complexity and stability of brain states ([Li et al. 2024](https://doi.org/10.1063/5.0203926)).

The therapeutic implications of the attractor-connectivity framework are profound, suggesting that interventions should aim not merely at modulating activity within specific circuits but at reshaping the entire attractor landscape. Non-invasive neuromodulation approaches, including transcranial magnetic stimulation and transcranial direct current stimulation, may exert their therapeutic effects by perturbing the system sufficiently to escape from pathological attractor basins and facilitating the establishment of more adaptive configurations. The construction of neural networks with pre-specified dynamics offers theoretical grounding for such interventions, demonstrating that appropriate stimulation patterns can indeed reshape attractor landscapes in desired ways ([Mininni and Zanutto 2024](https://doi.org/10.1038/s41598-024-69747-z)). Cholinergic neuromodulation of prefrontal attractor dynamics has been shown to control performance in spatial working memory tasks, suggesting that pharmacological interventions targeting specific neuromodulatory systems may achieve precise sculpting of attractor geometry ([Mahrach et al. 2024](https://doi.org/10.1101/2024.01.17.576071)).

Data-driven discovery of canonical large-scale brain dynamics has identified reproducible spatiotemporal patterns that constitute the normal repertoire of brain states, providing a reference against which pathological configurations can be assessed ([Piccinini et al. 2022](https://doi.org/10.1093/texcom/tgac045)). This approach enables personalized medicine applications, wherein individual patients' attractor landscapes can be characterized and targeted interventions designed to reshape specific pathological features. Continuous attractor models developed for understanding memory dynamics suggest that therapeutic approaches may need to consider not only discrete attractor states but also continuous manifolds along which neural activity flows ([Spalla et al. 2021](https://doi.org/10.7554/eLife.69499)). The spatial coding properties of grid cells and their attractor dynamics in the entorhinal cortex provide fundamental insights into how continuous attractors are implemented neurally, with implications for understanding cognitive dysfunction across multiple disorders ([Burak 2014](https://doi.org/10.1016/j.conb.2014.01.013)).

Computational approaches to robust working memory through unsupervised learning mechanisms offer theoretical frameworks for understanding how healthy attractor dynamics are established and maintained, and how these processes may fail in psychiatric illness ([Gu and Lim 2022](https://doi.org/10.1371/journal.pcbi.1009083)). These models suggest that therapeutic interventions might profitably target the learning rules that shape attractor landscapes over developmental and experiential timescales, rather than merely addressing acute network dynamics. The integration of these diverse perspectives under a unified attractor-connectivity framework promises to advance both our understanding of psychiatric and neurological pathophysiology and our capacity to develop more effective, mechanistically targeted interventions.

## Emerging Frameworks and Open Questions

The emergence of computational psychiatry as a discipline has catalyzed a paradigm shift from purely descriptive nosology toward mechanistic accounts of psychopathology grounded in formal neurocomputational principles ([Montague et al. 2012](https://doi.org/10.1016/j.tics.2011.11.018)). Central to this enterprise is the development of whole-brain computational models that bridge microscale neurophysiological processes with macroscale connectivity patterns and their associated attractor dynamics. The active inference framework represents one particularly promising avenue, positing that the brain maintains a generative model of its environment and continuously updates beliefs to minimize prediction errors through both perceptual inference and action selection ([Friston et al. 2016](https://doi.org/10.1016/j.neubiorev.2016.06.022)). This theoretical architecture naturally accommodates hierarchical predictive coding schemes and offers principled explanations for how disruptions in precision weighting—the neural encoding of uncertainty—might manifest as the positive symptoms of psychosis or the negative symptoms characterized by reduced motivational drive.

The integration of reinforcement learning frameworks with clinical neuroscience has yielded substantial insights into the computational substrates of psychiatric illness. Recent work has emphasized the importance of naturalistic paradigms that capture the complexity of real-world decision-making environments, moving beyond the simplified reward structures that have dominated experimental paradigms ([Wise et al. 2024](https://doi.org/10.1016/j.tics.2023.08.016)). Such approaches may prove essential for understanding how the brain navigates the hierarchical and temporally extended reward structures encountered in daily life, where the mapping between actions and outcomes is rarely deterministic or immediately observable. In schizophrenia, computational modeling has revealed specific alterations in reinforcement learning parameters, with patients demonstrating characteristic differences in learning rates and reward sensitivity that may inform patient stratification and treatment selection ([Geana et al. 2022](https://doi.org/10.1016/j.bpsc.2021.03.017)). Notably, the reward-complexity trade-off observed in schizophrenia suggests that patients may exhibit preserved or even enhanced performance on simpler reinforcement learning tasks while showing deficits when the computational demands of the task increase ([Gershman and Lai 2021](https://doi.org/10.5334/cpsy.71)).

The neural bases of emotion regulation have been increasingly characterized through computational lenses, with particular attention to how prefrontal control mechanisms modulate amygdala reactivity during threat processing ([Etkin et al. 2015](https://doi.org/10.1038/nrn4044)). Computational modeling of threat learning has revealed meaningful links between model-derived parameters, anxiety symptom dimensions, and neuroanatomical variation, suggesting that individual differences in threat prediction error signaling may constitute a transdiagnostic vulnerability marker ([Abend et al. 2022](https://doi.org/10.7554/eLife.66169)). The acquisition and extinction of conditioned fear responses rely on partially dissociable neural circuits, and computational frameworks have begun to formalize how the balance between these processes determines adaptive versus maladaptive threat responses ([Levy and Schiller 2021](https://doi.org/10.1016/j.tics.2020.11.007)). However, methodological considerations in measuring human trace fear conditioning remain substantial, with implications for the reliability and validity of model parameter estimates ([Wehrli et al. 2022](https://doi.org/10.1111/psyp.14119)).

A critical theoretical advancement has been the reconceptualization of mood states as representations of momentum in the reinforcement learning process, wherein mood tracks the rate of change in expected reward rather than absolute reward value ([Eldar et al. 2016](https://doi.org/10.1016/j.tics.2015.07.010)). This framework offers novel mechanistic accounts of mood disorders, suggesting that depressive episodes may arise from persistent negative prediction errors that generate downward momentum in affective state, while manic states might reflect inappropriately elevated momentum signals. The computational structure of consummatory anhedonia has similarly been dissected through formal modeling approaches, distinguishing between deficits in reward valuation, effort-cost computation, and the temporal integration of hedonic experience ([Hall et al. 2024](https://doi.org/10.1016/j.tics.2024.01.006)). Such computational fractionation of ostensibly unitary clinical constructs may prove invaluable for precision medicine approaches that target specific neurocomputational deficits.

The broader domain of reward processing and neuroeconomics has established fundamental relationships between dopaminergic signaling, reward prediction errors, and decision-making that inform psychiatric theory ([Zald and Treadway 2017](https://doi.org/10.1146/annurev-clinpsy-032816-044957)). These insights extend to pharmacological intervention, where reinforcement learning models have been deployed to understand how antidepressant medications modulate dopamine and serotonin signaling to alter reward sensitivity and learning rates ([Lan and Browning 2022](https://doi.org/10.5334/cpsy.83)). The interplay between reward and action selection represents another critical dimension, with implications for understanding apathy, avolition, and the role of effort-cost computations in motivated behavior ([Le Heron 2022](https://doi.org/10.1136/jnnp-2021-328302)). Experimental paradigms that dissociate cognitive effort from task difficulty have revealed that effort-cost computations may be separable from ability-related constraints, with implications for understanding the motivational deficits observed across multiple psychiatric conditions ([Fleming et al. 2023](https://doi.org/10.3758/s13415-023-01065-9)).

Social and interpersonal dimensions of reinforcement learning have garnered increasing attention, with investigations into how individuals discount the welfare of others when evaluating outcomes ([Story et al. 2020](https://doi.org/10.1002/jeab.631)). Such social discounting mechanisms may be relevant to understanding the interpersonal difficulties characteristic of multiple psychiatric disorders, though the translation of these findings to clinical populations remains in early stages. The developmental trajectory of model-based versus model-free decision-making has been traced through childhood and adolescence, revealing that the capacity for computationally demanding model-based control emerges gradually and may be particularly vulnerable to disruption during critical developmental windows ([Smid et al. 2023](https://doi.org/10.1111/desc.13295)). This developmental perspective has catalyzed the emergence of developmental computational psychiatry as a subdiscipline focused on understanding how computational parameters evolve across the lifespan and interact with risk factors for psychopathology ([Hauser et al. 2019](https://doi.org/10.1111/jcpp.12964)).

Despite considerable theoretical and empirical advances, the field confronts substantial methodological challenges that constrain translational impact. Perhaps most critically, the reliability of reinforcement learning parameters—both their test-retest stability and internal consistency—remains a significant concern, with recent investigations suggesting that commonly used parameters may exhibit inadequate psychometric properties for individual-level clinical applications ([Mkrtchian et al. 2023](https://doi.org/10.5334/cpsy.86)). Independent replication has confirmed that multiple reinforcement learning parameters show suboptimal reliability across sessions, raising questions about their suitability as biomarkers for diagnosis, treatment selection, or outcome prediction ([Schaaf et al. 2024](https://doi.org/10.3758/s13428-023-02203-4)). These psychometric limitations interact with the substantial heterogeneity observed within diagnostic categories, complicating efforts to establish robust computational signatures of specific disorders.

Several open questions merit priority consideration for future research. First, the development of computational models that bridge multiple temporal scales—from rapid neural dynamics to slowly evolving mood states and trait-like vulnerability factors—remains a formidable theoretical challenge. Second, the optimal level of computational abstraction for clinical translation requires clarification; while highly detailed models may capture neurobiological nuance, their parameter spaces may be unidentifiable from behavioral data alone. Third, the integration of computational psychiatry with neuroimaging and electrophysiological measures offers promise for constraining model parameters and improving reliability, though standardized protocols and analytical pipelines remain to be established. Fourth, the clinical utility of computational assessments must be rigorously evaluated against existing clinical measures, with attention to whether computational parameters provide incremental predictive value beyond simpler behavioral indices. The translation of computational frameworks from laboratory settings to routine clinical practice will require sustained attention to these methodological and conceptual challenges, yet the potential for mechanistically informed psychiatric nosology and personalized intervention strategies continues to justify this investigative investment.

## References

- Dominguez D, Koroutchev K, Serrano E, et al.. 2007. Information and topology in attractor neural networks.. *Neural computation*. [DOI: 10.1162/neco.2007.19.4.956](https://doi.org/10.1162/neco.2007.19.4.956)

- Zemel RS, Mozer MC. 2001. Localist attractor networks.. *Neural computation*. [DOI: 10.1162/08997660151134325](https://doi.org/10.1162/08997660151134325)

- Nair A, Karigo T, Yang B, et al.. 2023. An approximate line attractor in the hypothalamus encodes an aggressive state.. *Cell*. [DOI: 10.1016/j.cell.2022.11.027](https://doi.org/10.1016/j.cell.2022.11.027)

- Vinograd A, Nair A, Kim JH, et al.. 2024. Causal evidence of a line attractor encoding an affective state.. *Nature*. [DOI: 10.1038/s41586-024-07915-x](https://doi.org/10.1038/s41586-024-07915-x)

- Watanabe T, Hirose S, Wada H, et al.. 2014. Energy landscapes of resting-state brain networks.. *Frontiers in neuroinformatics*. [DOI: 10.3389/fninf.2014.00012](https://doi.org/10.3389/fninf.2014.00012)

- Kang J, Pae C, Park HJ. 2017. Energy landscape analysis of the subcortical brain network unravels system properties beneath resting state dynamics.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2017.01.075](https://doi.org/10.1016/j.neuroimage.2017.01.075)

- Rolls ET, Webb TJ. 2012. Cortical attractor network dynamics with diluted connectivity.. *Brain research*. [DOI: 10.1016/j.brainres.2011.08.002](https://doi.org/10.1016/j.brainres.2011.08.002)

- Chaudhuri R, Gerçek B, Pandey B, et al.. 2019. The intrinsic attractor manifold and population dynamics of a canonical cognitive circuit across waking and sleep.. *Nature neuroscience*. [DOI: 10.1038/s41593-019-0460-x](https://doi.org/10.1038/s41593-019-0460-x)

- Montague PR, Dolan RJ, Friston KJ, et al.. 2012. Computational psychiatry.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2011.11.018](https://doi.org/10.1016/j.tics.2011.11.018)

- Durstewitz D, Huys QJM, Koppe G. 2021. Psychiatric Illnesses as Disorders of Network Dynamics.. *Biological psychiatry. Cognitive neuroscience and neuroimaging*. [DOI: 10.1016/j.bpsc.2020.01.001](https://doi.org/10.1016/j.bpsc.2020.01.001)

- Regonia PR, Takamura M, Nakano T, et al.. 2021. Modeling Heterogeneous Brain Dynamics of Depression and Melancholia Using Energy Landscape Analysis.. *Frontiers in psychiatry*. [DOI: 10.3389/fpsyt.2021.780997](https://doi.org/10.3389/fpsyt.2021.780997)

- Rolls ET, Cheng W, Feng J. 2021. Brain dynamics: the temporal variability of connectivity, and differences in schizophrenia and ADHD.. *Translational psychiatry*. [DOI: 10.1038/s41398-021-01197-x](https://doi.org/10.1038/s41398-021-01197-x)

- Iravani B, Arshamian A, Fransson P, et al.. 2021. Whole-brain modelling of resting state fMRI differentiates ADHD subtypes and facilitates stratified neuro-stimulation therapy.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2021.117844](https://doi.org/10.1016/j.neuroimage.2021.117844)

- Jing R, Li P, Zhao K, et al.. 2025. Energy-Landscape Analysis of Brain Network Dynamics in a Multicenter Alzheimer's Disease and Mild Cognitive Impairment Cohort.. *Biological psychiatry*. [DOI: 10.1016/j.biopsych.2025.07.022](https://doi.org/10.1016/j.biopsych.2025.07.022)

- Núñez P, Tewarie P, Rodríguez-González V, et al.. 2025. Altered electrophysiological meta-state dynamics in disorders of consciousness.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2025.121519](https://doi.org/10.1016/j.neuroimage.2025.121519)

- Balaguer-Ballester E, Moreno-Bote R, Deco G, et al.. 2017. Editorial: Metastable Dynamics of Neural Ensembles.. *Frontiers in systems neuroscience*. [DOI: 10.3389/fnsys.2017.00099](https://doi.org/10.3389/fnsys.2017.00099)

- Vinograd A, Nair A, Linderman SW, et al.. 2024. Intrinsic Dynamics and Neural Implementation of a Hypothalamic Line Attractor Encoding an Internal Behavioral State.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2024.05.21.595051](https://doi.org/10.1101/2024.05.21.595051)

- Liu M, Nair A, Coria N, et al.. 2024. Encoding of female mating dynamics by a hypothalamic line attractor.. *Nature*. [DOI: 10.1038/s41586-024-07916-w](https://doi.org/10.1038/s41586-024-07916-w)

- Ajabi Z, Keinath AT, Wei XX, et al.. 2023. Population dynamics of head-direction neurons during drift and reorientation.. *Nature*. [DOI: 10.1038/s41586-023-05813-2](https://doi.org/10.1038/s41586-023-05813-2)

- Piñero J, Solé R. 2019. Statistical physics of liquid brains.. *Philosophical transactions of the Royal Society of London. Series B, Biological sciences*. [DOI: 10.1098/rstb.2018.0376](https://doi.org/10.1098/rstb.2018.0376)

- Liu M, Nair A, Linderman SW, et al.. 2023. Periodic hypothalamic attractor-like dynamics during the estrus cycle.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2023.05.22.541741](https://doi.org/10.1101/2023.05.22.541741)

- Kirillov SY, Smelov PS, Klinshov VV. 2024. Collective dynamics and shot-noise-induced switching in a two-population neural network.. *Chaos (Woodbury, N.Y.)*. [DOI: 10.1063/5.0193275](https://doi.org/10.1063/5.0193275)

- Mazzucato L. 2022. Neural mechanisms underlying the temporal organization of naturalistic animal behavior.. *eLife*. [DOI: 10.7554/eLife.76577](https://doi.org/10.7554/eLife.76577)

- Mininni CJ, Zanutto BS. 2024. Constructing neural networks with pre-specified dynamics.. *Scientific reports*. [DOI: 10.1038/s41598-024-69747-z](https://doi.org/10.1038/s41598-024-69747-z)

- Sedler AR, Versteeg C, Pandarinath C. 2023. Expressive architectures enhance interpretability of dynamics-based neural population models.. *Neurons, behavior, data analysis, and theory*. [DOI: 10.51628/001c.73987](https://doi.org/10.51628/001c.73987)

- Genkin M, Shenoy KV, Chandrasekaran C, et al.. 2025. The dynamics and geometry of choice in the premotor cortex.. *Nature*. [DOI: 10.1038/s41586-025-09199-1](https://doi.org/10.1038/s41586-025-09199-1)

- Inagaki HK, Chen S, Daie K, et al.. 2022. Neural Algorithms and Circuits for Motor Planning.. *Annual review of neuroscience*. [DOI: 10.1146/annurev-neuro-092021-121730](https://doi.org/10.1146/annurev-neuro-092021-121730)

- Sylwestrak EL, Jo Y, Vesuna S, et al.. 2022. Cell-type-specific population dynamics of diverse reward computations.. *Cell*. [DOI: 10.1016/j.cell.2022.08.019](https://doi.org/10.1016/j.cell.2022.08.019)

- Aitken K, Mihalas S. 2023. Neural population dynamics of computing with synaptic modulations.. *eLife*. [DOI: 10.7554/eLife.83035](https://doi.org/10.7554/eLife.83035)

- Tajima S, Koida K, Tajima CI, et al.. 2017. Task-dependent recurrent dynamics in visual cortex.. *eLife*. [DOI: 10.7554/eLife.26868](https://doi.org/10.7554/eLife.26868)

- Kotler S, Mannino M, Friston K, et al.. 2025. Pathfinding: a neurodynamical account of intuition.. *Communications biology*. [DOI: 10.1038/s42003-025-08612-9](https://doi.org/10.1038/s42003-025-08612-9)

- Thivierge JP, Comas R, Longtin A. 2014. Attractor dynamics in local neuronal networks.. *Frontiers in neural circuits*. [DOI: 10.3389/fncir.2014.00022](https://doi.org/10.3389/fncir.2014.00022)

- Rennó-Costa C, Lisman JE, Verschure PF. 2014. A signature of attractor dynamics in the CA3 region of the hippocampus.. *PLoS computational biology*. [DOI: 10.1371/journal.pcbi.1003641](https://doi.org/10.1371/journal.pcbi.1003641)

- Kim CS. 2018. Recognition Dynamics in the Brain under the Free Energy Principle.. *Neural computation*. [DOI: 10.1162/neco_a_01115](https://doi.org/10.1162/neco_a_01115)

- Kong X, Kong R, Orban C, et al.. 2021. Sensory-motor cortices shape functional connectivity dynamics in the human brain.. *Nature communications*. [DOI: 10.1038/s41467-021-26704-y](https://doi.org/10.1038/s41467-021-26704-y)

- Olguín-Rodríguez PV, Arzate-Mena JD, Corsi-Cabrera M, et al.. 2018. Characteristic Fluctuations Around Stable Attractor Dynamics Extracted from Highly Nonstationary Electroencephalographic Recordings.. *Brain connectivity*. [DOI: 10.1089/brain.2018.0609](https://doi.org/10.1089/brain.2018.0609)

- Tort-Colet N, Capone C, Sanchez-Vives MV, et al.. 2021. Attractor competition enriches cortical dynamics during awakening from anesthesia.. *Cell reports*. [DOI: 10.1016/j.celrep.2021.109270](https://doi.org/10.1016/j.celrep.2021.109270)

- Laptev D, Burgess N. 2019. Neural Dynamics Indicate Parallel Integration of Environmental and Self-Motion Information by Place and Grid Cells.. *Frontiers in neural circuits*. [DOI: 10.3389/fncir.2019.00059](https://doi.org/10.3389/fncir.2019.00059)

- Bonaiuto JJ, Bestmann S. 2015. Understanding the nonlinear physiological and behavioral effects of tDCS through computational neurostimulation.. *Progress in brain research*. [DOI: 10.1016/bs.pbr.2015.06.013](https://doi.org/10.1016/bs.pbr.2015.06.013)

- Koch D, Nandan A, Ramesan G, et al.. 2024. Biological computations: Limitations of attractor-based formalisms and the need for transients.. *Biochemical and biophysical research communications*. [DOI: 10.1016/j.bbrc.2024.150069](https://doi.org/10.1016/j.bbrc.2024.150069)

- Shah OS, Chaudhary MFA, Awan HA, et al.. 2018. ATLANTIS - Attractor Landscape Analysis Toolbox for Cell Fate Discovery and Reprogramming.. *Scientific reports*. [DOI: 10.1038/s41598-018-22031-3](https://doi.org/10.1038/s41598-018-22031-3)

- Zhang X, Chong KH, Zhu L, et al.. 2020. A Monte Carlo method for in silico modeling and visualization of Waddington's epigenetic landscape with intermediate details.. *Bio Systems*. [DOI: 10.1016/j.biosystems.2020.104275](https://doi.org/10.1016/j.biosystems.2020.104275)

- Kang J, Jeong SO, Pae C, et al.. 2021. Bayesian estimation of maximum entropy model for individualized energy landscape analysis of brain state dynamics.. *Human brain mapping*. [DOI: 10.1002/hbm.25442](https://doi.org/10.1002/hbm.25442)

- Nakamura T. 2024. Derivation of the Invariant Free-Energy Landscape Based on Langevin Dynamics.. *Physical review letters*. [DOI: 10.1103/PhysRevLett.132.137101](https://doi.org/10.1103/PhysRevLett.132.137101)

- Ayaz C, Tepper L, Brünig FN, et al.. 2021. Non-Markovian modeling of protein folding.. *Proceedings of the National Academy of Sciences of the United States of America*. [DOI: 10.1073/pnas.2023856118](https://doi.org/10.1073/pnas.2023856118)

- Xing L, Guo Z, Long Z. 2024. Energy landscape analysis of brain network dynamics in Alzheimer's disease.. *Frontiers in aging neuroscience*. [DOI: 10.3389/fnagi.2024.1375091](https://doi.org/10.3389/fnagi.2024.1375091)

- Allen JD, Varanasi S, Han F, et al.. 2024. Functional Connectivity Biomarker Extraction for Schizophrenia Based on Energy Landscape Machine Learning Techniques.. *Sensors (Basel, Switzerland)*. [DOI: 10.3390/s24237742](https://doi.org/10.3390/s24237742)

- Ishida T, Yamada S, Yasuda K, et al.. 2024. Aberrant brain dynamics of large-scale functional networks across schizophrenia and mood disorder.. *NeuroImage. Clinical*. [DOI: 10.1016/j.nicl.2024.103574](https://doi.org/10.1016/j.nicl.2024.103574)

- Theis N, Bahuguna J, Rubin JE, et al.. 2024. Energy of functional brain states correlates with cognition in adolescent-onset schizophrenia and healthy persons.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2023.11.06.565753](https://doi.org/10.1101/2023.11.06.565753)

- Prasad K, Bowei O, Theis N. 2025. From microstates to macroscales: A Critical Review of Maximum Entropy Modeling and Energy Landscape Analysis in functional MRI.. *Research square*. [DOI: 10.21203/rs.3.rs-8428652/v1](https://doi.org/10.21203/rs.3.rs-8428652/v1)

- Gupta D, Du X, Summerfelt A, et al.. 2023. Brain Connectivity Signature Extractions from TMS Invoked EEGs.. *Sensors (Basel, Switzerland)*. [DOI: 10.3390/s23084078](https://doi.org/10.3390/s23084078)

- Yu L, Gong L, Chen X, et al.. 2025. Exploratory GABAa-informed control network modulates hyperarousal brain dynamics in chronic insomnia.. *Communications biology*. [DOI: 10.1038/s42003-025-08439-4](https://doi.org/10.1038/s42003-025-08439-4)

- Borzou A, Miller SN, Hommel JD, et al.. 2024. Cocaine diminishes functional network robustness and destabilizes the energy landscape of neuronal activity in the medial prefrontal cortex.. *PNAS nexus*. [DOI: 10.1093/pnasnexus/pgae092](https://doi.org/10.1093/pnasnexus/pgae092)

- Xin Q, Hao S, Xiaoqin W, et al.. 2024. Brain Source Localization and Functional Connectivity in Group Identity Regulation of Overbidding in Contest.. *Neuroscience*. [DOI: 10.1016/j.neuroscience.2024.01.016](https://doi.org/10.1016/j.neuroscience.2024.01.016)

- Sharpee TO, Destexhe A, Kawato M, et al.. 2016. 25th Annual Computational Neuroscience Meeting: CNS-2016.. *BMC neuroscience*. [DOI: 10.1186/s12868-016-0283-6](https://doi.org/10.1186/s12868-016-0283-6)

- Sneha NP, Dharshini SAP, Taguchi YH, et al.. 2022. Integrative Meta-Analysis of Huntington's Disease Transcriptome Landscape.. *Genes*. [DOI: 10.3390/genes13122385](https://doi.org/10.3390/genes13122385)

- Lee BH, Arya G. 2022. Assembly mechanism of surface-functionalized nanocubes.. *Nanoscale*. [DOI: 10.1039/d1nr07995f](https://doi.org/10.1039/d1nr07995f)

- Mosharov EV, Rosenberg AM, Monzel AS, et al.. 2025. A human brain map of mitochondrial respiratory capacity and diversity.. *Nature*. [DOI: 10.1038/s41586-025-08740-6](https://doi.org/10.1038/s41586-025-08740-6)

- Durstewitz D, Seamans JK, Sejnowski TJ. 2000. Neurocomputational models of working memory.. *Nature neuroscience*. [DOI: 10.1038/81460](https://doi.org/10.1038/81460)

- Zhao N, Song J, Liu S. 2023. Multi-timescale analysis of midbrain dopamine neuronal firing activities.. *Journal of theoretical biology*. [DOI: 10.1016/j.jtbi.2022.111310](https://doi.org/10.1016/j.jtbi.2022.111310)

- Looijestijn J, Blom JD, Aleman A, et al.. 2015. An integrated network model of psychotic symptoms.. *Neuroscience and biobehavioral reviews*. [DOI: 10.1016/j.neubiorev.2015.09.016](https://doi.org/10.1016/j.neubiorev.2015.09.016)

- Naudé J, Sarazin MXB, Mondoloni S, et al.. 2024. Dopamine builds and reveals reward-associated latent behavioral attractors.. *Nature communications*. [DOI: 10.1038/s41467-024-53976-x](https://doi.org/10.1038/s41467-024-53976-x)

- Stroh A, Schweiger S, Ramirez JM, et al.. 2024. The selfish network: how the brain preserves behavioral function through shifts in neuronal network state.. *Trends in neurosciences*. [DOI: 10.1016/j.tins.2024.02.005](https://doi.org/10.1016/j.tins.2024.02.005)

- Taylor NL, D'Souza A, Munn BR, et al.. 2022. Structural connections between the noradrenergic and cholinergic system shape the dynamics of functional brain networks.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2022.119455](https://doi.org/10.1016/j.neuroimage.2022.119455)

- Li Q, Calhoun VD, Pham TD, et al.. 2024. Exploring nonlinear dynamics in brain functionality through phase portraits and fuzzy recurrence plots.. *Chaos (Woodbury, N.Y.)*. [DOI: 10.1063/5.0203926](https://doi.org/10.1063/5.0203926)

- Mahrach A, Bestue D, Qi XL, et al.. 2024. Cholinergic neuromodulation of prefrontal attractor dynamics controls performance in spatial working memory.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2024.01.17.576071](https://doi.org/10.1101/2024.01.17.576071)

- Piccinini J, Deco G, Kringelbach M, et al.. 2022. Data-driven discovery of canonical large-scale brain dynamics.. *Cerebral cortex communications*. [DOI: 10.1093/texcom/tgac045](https://doi.org/10.1093/texcom/tgac045)

- Spalla D, Cornacchia IM, Treves A. 2021. Continuous attractors for dynamic memories.. *eLife*. [DOI: 10.7554/eLife.69499](https://doi.org/10.7554/eLife.69499)

- Burak Y. 2014. Spatial coding and attractor dynamics of grid cells in the entorhinal cortex.. *Current opinion in neurobiology*. [DOI: 10.1016/j.conb.2014.01.013](https://doi.org/10.1016/j.conb.2014.01.013)

- Gu J, Lim S. 2022. Unsupervised learning for robust working memory.. *PLoS computational biology*. [DOI: 10.1371/journal.pcbi.1009083](https://doi.org/10.1371/journal.pcbi.1009083)

- Friston K, FitzGerald T, Rigoli F, et al.. 2016. Active inference and learning.. *Neuroscience and biobehavioral reviews*. [DOI: 10.1016/j.neubiorev.2016.06.022](https://doi.org/10.1016/j.neubiorev.2016.06.022)

- Wise T, Emery K, Radulescu A. 2024. Naturalistic reinforcement learning.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2023.08.016](https://doi.org/10.1016/j.tics.2023.08.016)

- Geana A, Barch DM, Gold JM, et al.. 2022. Using Computational Modeling to Capture Schizophrenia-Specific Reinforcement Learning Differences and Their Implications on Patient Classification.. *Biological psychiatry. Cognitive neuroscience and neuroimaging*. [DOI: 10.1016/j.bpsc.2021.03.017](https://doi.org/10.1016/j.bpsc.2021.03.017)

- Gershman SJ, Lai L. 2021. The Reward-Complexity Trade-off in Schizophrenia.. *Computational psychiatry (Cambridge, Mass.)*. [DOI: 10.5334/cpsy.71](https://doi.org/10.5334/cpsy.71)

- Etkin A, Büchel C, Gross JJ. 2015. The neural bases of emotion regulation.. *Nature reviews. Neuroscience*. [DOI: 10.1038/nrn4044](https://doi.org/10.1038/nrn4044)

- Abend R, Burk D, Ruiz SG, et al.. 2022. Computational modeling of threat learning reveals links with anxiety and neuroanatomy in humans.. *eLife*. [DOI: 10.7554/eLife.66169](https://doi.org/10.7554/eLife.66169)

- Levy I, Schiller D. 2021. Neural Computations of Threat.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2020.11.007](https://doi.org/10.1016/j.tics.2020.11.007)

- Wehrli JM, Xia Y, Gerster S, et al.. 2022. Measuring human trace fear conditioning.. *Psychophysiology*. [DOI: 10.1111/psyp.14119](https://doi.org/10.1111/psyp.14119)

- Eldar E, Rutledge RB, Dolan RJ, et al.. 2016. Mood as Representation of Momentum.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2015.07.010](https://doi.org/10.1016/j.tics.2015.07.010)

- Hall AF, Browning M, Huys QJM. 2024. The computational structure of consummatory anhedonia.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2024.01.006](https://doi.org/10.1016/j.tics.2024.01.006)

- Zald DH, Treadway MT. 2017. Reward Processing, Neuroeconomics, and Psychopathology.. *Annual review of clinical psychology*. [DOI: 10.1146/annurev-clinpsy-032816-044957](https://doi.org/10.1146/annurev-clinpsy-032816-044957)

- Lan DCL, Browning M. 2022. What Can Reinforcement Learning Models of Dopamine and Serotonin Tell Us about the Action of Antidepressants?. *Computational psychiatry (Cambridge, Mass.)*. [DOI: 10.5334/cpsy.83](https://doi.org/10.5334/cpsy.83)

- Le Heron CJ. 2022. Reward and actions and the game of life.. *Journal of neurology, neurosurgery, and psychiatry*. [DOI: 10.1136/jnnp-2021-328302](https://doi.org/10.1136/jnnp-2021-328302)

- Fleming H, Robinson OJ, Roiser JP. 2023. Measuring cognitive effort without difficulty.. *Cognitive, affective & behavioral neuroscience*. [DOI: 10.3758/s13415-023-01065-9](https://doi.org/10.3758/s13415-023-01065-9)

- Story GW, Kurth-Nelson Z, Crockett M, et al.. 2020. Social discounting of pain.. *Journal of the experimental analysis of behavior*. [DOI: 10.1002/jeab.631](https://doi.org/10.1002/jeab.631)

- Smid CR, Kool W, Hauser TU, et al.. 2023. Computational and behavioral markers of model-based decision making in childhood.. *Developmental science*. [DOI: 10.1111/desc.13295](https://doi.org/10.1111/desc.13295)

- Hauser TU, Will GJ, Dubois M, et al.. 2019. Annual Research Review: Developmental computational psychiatry.. *Journal of child psychology and psychiatry, and allied disciplines*. [DOI: 10.1111/jcpp.12964](https://doi.org/10.1111/jcpp.12964)

- Mkrtchian A, Valton V, Roiser JP. 2023. Reliability of Decision-Making and Reinforcement Learning Computational Parameters.. *Computational psychiatry (Cambridge, Mass.)*. [DOI: 10.5334/cpsy.86](https://doi.org/10.5334/cpsy.86)

- Schaaf JV, Weidinger L, Molleman L, et al.. 2024. Test-retest reliability of reinforcement learning parameters.. *Behavior research methods*. [DOI: 10.3758/s13428-023-02203-4](https://doi.org/10.3758/s13428-023-02203-4)
## References

- Dominguez D, Koroutchev K, Serrano E, et al.. 2007. Information and topology in attractor neural networks.. *Neural computation*. [DOI: 10.1162/neco.2007.19.4.956](https://doi.org/10.1162/neco.2007.19.4.956)

- Zemel RS, Mozer MC. 2001. Localist attractor networks.. *Neural computation*. [DOI: 10.1162/08997660151134325](https://doi.org/10.1162/08997660151134325)

- Nair A, Karigo T, Yang B, et al.. 2023. An approximate line attractor in the hypothalamus encodes an aggressive state.. *Cell*. [DOI: 10.1016/j.cell.2022.11.027](https://doi.org/10.1016/j.cell.2022.11.027)

- Vinograd A, Nair A, Kim JH, et al.. 2024. Causal evidence of a line attractor encoding an affective state.. *Nature*. [DOI: 10.1038/s41586-024-07915-x](https://doi.org/10.1038/s41586-024-07915-x)

- Watanabe T, Hirose S, Wada H, et al.. 2014. Energy landscapes of resting-state brain networks.. *Frontiers in neuroinformatics*. [DOI: 10.3389/fninf.2014.00012](https://doi.org/10.3389/fninf.2014.00012)

- Kang J, Pae C, Park HJ. 2017. Energy landscape analysis of the subcortical brain network unravels system properties beneath resting state dynamics.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2017.01.075](https://doi.org/10.1016/j.neuroimage.2017.01.075)

- Rolls ET, Webb TJ. 2012. Cortical attractor network dynamics with diluted connectivity.. *Brain research*. [DOI: 10.1016/j.brainres.2011.08.002](https://doi.org/10.1016/j.brainres.2011.08.002)

- Chaudhuri R, Gerçek B, Pandey B, et al.. 2019. The intrinsic attractor manifold and population dynamics of a canonical cognitive circuit across waking and sleep.. *Nature neuroscience*. [DOI: 10.1038/s41593-019-0460-x](https://doi.org/10.1038/s41593-019-0460-x)

- Montague PR, Dolan RJ, Friston KJ, et al.. 2012. Computational psychiatry.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2011.11.018](https://doi.org/10.1016/j.tics.2011.11.018)

- Durstewitz D, Huys QJM, Koppe G. 2021. Psychiatric Illnesses as Disorders of Network Dynamics.. *Biological psychiatry. Cognitive neuroscience and neuroimaging*. [DOI: 10.1016/j.bpsc.2020.01.001](https://doi.org/10.1016/j.bpsc.2020.01.001)

- Regonia PR, Takamura M, Nakano T, et al.. 2021. Modeling Heterogeneous Brain Dynamics of Depression and Melancholia Using Energy Landscape Analysis.. *Frontiers in psychiatry*. [DOI: 10.3389/fpsyt.2021.780997](https://doi.org/10.3389/fpsyt.2021.780997)

- Rolls ET, Cheng W, Feng J. 2021. Brain dynamics: the temporal variability of connectivity, and differences in schizophrenia and ADHD.. *Translational psychiatry*. [DOI: 10.1038/s41398-021-01197-x](https://doi.org/10.1038/s41398-021-01197-x)

- Iravani B, Arshamian A, Fransson P, et al.. 2021. Whole-brain modelling of resting state fMRI differentiates ADHD subtypes and facilitates stratified neuro-stimulation therapy.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2021.117844](https://doi.org/10.1016/j.neuroimage.2021.117844)

- Jing R, Li P, Zhao K, et al.. 2025. Energy-Landscape Analysis of Brain Network Dynamics in a Multicenter Alzheimer's Disease and Mild Cognitive Impairment Cohort.. *Biological psychiatry*. [DOI: 10.1016/j.biopsych.2025.07.022](https://doi.org/10.1016/j.biopsych.2025.07.022)

- Núñez P, Tewarie P, Rodríguez-González V, et al.. 2025. Altered electrophysiological meta-state dynamics in disorders of consciousness.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2025.121519](https://doi.org/10.1016/j.neuroimage.2025.121519)

- Balaguer-Ballester E, Moreno-Bote R, Deco G, et al.. 2017. Editorial: Metastable Dynamics of Neural Ensembles.. *Frontiers in systems neuroscience*. [DOI: 10.3389/fnsys.2017.00099](https://doi.org/10.3389/fnsys.2017.00099)

- Vinograd A, Nair A, Linderman SW, et al.. 2024. Intrinsic Dynamics and Neural Implementation of a Hypothalamic Line Attractor Encoding an Internal Behavioral State.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2024.05.21.595051](https://doi.org/10.1101/2024.05.21.595051)

- Liu M, Nair A, Coria N, et al.. 2024. Encoding of female mating dynamics by a hypothalamic line attractor.. *Nature*. [DOI: 10.1038/s41586-024-07916-w](https://doi.org/10.1038/s41586-024-07916-w)

- Ajabi Z, Keinath AT, Wei XX, et al.. 2023. Population dynamics of head-direction neurons during drift and reorientation.. *Nature*. [DOI: 10.1038/s41586-023-05813-2](https://doi.org/10.1038/s41586-023-05813-2)

- Piñero J, Solé R. 2019. Statistical physics of liquid brains.. *Philosophical transactions of the Royal Society of London. Series B, Biological sciences*. [DOI: 10.1098/rstb.2018.0376](https://doi.org/10.1098/rstb.2018.0376)

- Liu M, Nair A, Linderman SW, et al.. 2023. Periodic hypothalamic attractor-like dynamics during the estrus cycle.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2023.05.22.541741](https://doi.org/10.1101/2023.05.22.541741)

- Kirillov SY, Smelov PS, Klinshov VV. 2024. Collective dynamics and shot-noise-induced switching in a two-population neural network.. *Chaos (Woodbury, N.Y.)*. [DOI: 10.1063/5.0193275](https://doi.org/10.1063/5.0193275)

- Mazzucato L. 2022. Neural mechanisms underlying the temporal organization of naturalistic animal behavior.. *eLife*. [DOI: 10.7554/eLife.76577](https://doi.org/10.7554/eLife.76577)

- Mininni CJ, Zanutto BS. 2024. Constructing neural networks with pre-specified dynamics.. *Scientific reports*. [DOI: 10.1038/s41598-024-69747-z](https://doi.org/10.1038/s41598-024-69747-z)

- Sedler AR, Versteeg C, Pandarinath C. 2023. Expressive architectures enhance interpretability of dynamics-based neural population models.. *Neurons, behavior, data analysis, and theory*. [DOI: 10.51628/001c.73987](https://doi.org/10.51628/001c.73987)

- Genkin M, Shenoy KV, Chandrasekaran C, et al.. 2025. The dynamics and geometry of choice in the premotor cortex.. *Nature*. [DOI: 10.1038/s41586-025-09199-1](https://doi.org/10.1038/s41586-025-09199-1)

- Inagaki HK, Chen S, Daie K, et al.. 2022. Neural Algorithms and Circuits for Motor Planning.. *Annual review of neuroscience*. [DOI: 10.1146/annurev-neuro-092021-121730](https://doi.org/10.1146/annurev-neuro-092021-121730)

- Sylwestrak EL, Jo Y, Vesuna S, et al.. 2022. Cell-type-specific population dynamics of diverse reward computations.. *Cell*. [DOI: 10.1016/j.cell.2022.08.019](https://doi.org/10.1016/j.cell.2022.08.019)

- Aitken K, Mihalas S. 2023. Neural population dynamics of computing with synaptic modulations.. *eLife*. [DOI: 10.7554/eLife.83035](https://doi.org/10.7554/eLife.83035)

- Tajima S, Koida K, Tajima CI, et al.. 2017. Task-dependent recurrent dynamics in visual cortex.. *eLife*. [DOI: 10.7554/eLife.26868](https://doi.org/10.7554/eLife.26868)

- Kotler S, Mannino M, Friston K, et al.. 2025. Pathfinding: a neurodynamical account of intuition.. *Communications biology*. [DOI: 10.1038/s42003-025-08612-9](https://doi.org/10.1038/s42003-025-08612-9)

- Thivierge JP, Comas R, Longtin A. 2014. Attractor dynamics in local neuronal networks.. *Frontiers in neural circuits*. [DOI: 10.3389/fncir.2014.00022](https://doi.org/10.3389/fncir.2014.00022)

- Rennó-Costa C, Lisman JE, Verschure PF. 2014. A signature of attractor dynamics in the CA3 region of the hippocampus.. *PLoS computational biology*. [DOI: 10.1371/journal.pcbi.1003641](https://doi.org/10.1371/journal.pcbi.1003641)

- Kim CS. 2018. Recognition Dynamics in the Brain under the Free Energy Principle.. *Neural computation*. [DOI: 10.1162/neco_a_01115](https://doi.org/10.1162/neco_a_01115)

- Kong X, Kong R, Orban C, et al.. 2021. Sensory-motor cortices shape functional connectivity dynamics in the human brain.. *Nature communications*. [DOI: 10.1038/s41467-021-26704-y](https://doi.org/10.1038/s41467-021-26704-y)

- Olguín-Rodríguez PV, Arzate-Mena JD, Corsi-Cabrera M, et al.. 2018. Characteristic Fluctuations Around Stable Attractor Dynamics Extracted from Highly Nonstationary Electroencephalographic Recordings.. *Brain connectivity*. [DOI: 10.1089/brain.2018.0609](https://doi.org/10.1089/brain.2018.0609)

- Tort-Colet N, Capone C, Sanchez-Vives MV, et al.. 2021. Attractor competition enriches cortical dynamics during awakening from anesthesia.. *Cell reports*. [DOI: 10.1016/j.celrep.2021.109270](https://doi.org/10.1016/j.celrep.2021.109270)

- Laptev D, Burgess N. 2019. Neural Dynamics Indicate Parallel Integration of Environmental and Self-Motion Information by Place and Grid Cells.. *Frontiers in neural circuits*. [DOI: 10.3389/fncir.2019.00059](https://doi.org/10.3389/fncir.2019.00059)

- Bonaiuto JJ, Bestmann S. 2015. Understanding the nonlinear physiological and behavioral effects of tDCS through computational neurostimulation.. *Progress in brain research*. [DOI: 10.1016/bs.pbr.2015.06.013](https://doi.org/10.1016/bs.pbr.2015.06.013)

- Koch D, Nandan A, Ramesan G, et al.. 2024. Biological computations: Limitations of attractor-based formalisms and the need for transients.. *Biochemical and biophysical research communications*. [DOI: 10.1016/j.bbrc.2024.150069](https://doi.org/10.1016/j.bbrc.2024.150069)

- Shah OS, Chaudhary MFA, Awan HA, et al.. 2018. ATLANTIS - Attractor Landscape Analysis Toolbox for Cell Fate Discovery and Reprogramming.. *Scientific reports*. [DOI: 10.1038/s41598-018-22031-3](https://doi.org/10.1038/s41598-018-22031-3)

- Zhang X, Chong KH, Zhu L, et al.. 2020. A Monte Carlo method for in silico modeling and visualization of Waddington's epigenetic landscape with intermediate details.. *Bio Systems*. [DOI: 10.1016/j.biosystems.2020.104275](https://doi.org/10.1016/j.biosystems.2020.104275)

- Kang J, Jeong SO, Pae C, et al.. 2021. Bayesian estimation of maximum entropy model for individualized energy landscape analysis of brain state dynamics.. *Human brain mapping*. [DOI: 10.1002/hbm.25442](https://doi.org/10.1002/hbm.25442)

- Nakamura T. 2024. Derivation of the Invariant Free-Energy Landscape Based on Langevin Dynamics.. *Physical review letters*. [DOI: 10.1103/PhysRevLett.132.137101](https://doi.org/10.1103/PhysRevLett.132.137101)

- Ayaz C, Tepper L, Brünig FN, et al.. 2021. Non-Markovian modeling of protein folding.. *Proceedings of the National Academy of Sciences of the United States of America*. [DOI: 10.1073/pnas.2023856118](https://doi.org/10.1073/pnas.2023856118)

- Xing L, Guo Z, Long Z. 2024. Energy landscape analysis of brain network dynamics in Alzheimer's disease.. *Frontiers in aging neuroscience*. [DOI: 10.3389/fnagi.2024.1375091](https://doi.org/10.3389/fnagi.2024.1375091)

- Allen JD, Varanasi S, Han F, et al.. 2024. Functional Connectivity Biomarker Extraction for Schizophrenia Based on Energy Landscape Machine Learning Techniques.. *Sensors (Basel, Switzerland)*. [DOI: 10.3390/s24237742](https://doi.org/10.3390/s24237742)

- Ishida T, Yamada S, Yasuda K, et al.. 2024. Aberrant brain dynamics of large-scale functional networks across schizophrenia and mood disorder.. *NeuroImage. Clinical*. [DOI: 10.1016/j.nicl.2024.103574](https://doi.org/10.1016/j.nicl.2024.103574)

- Theis N, Bahuguna J, Rubin JE, et al.. 2024. Energy of functional brain states correlates with cognition in adolescent-onset schizophrenia and healthy persons.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2023.11.06.565753](https://doi.org/10.1101/2023.11.06.565753)

- Prasad K, Bowei O, Theis N. 2025. From microstates to macroscales: A Critical Review of Maximum Entropy Modeling and Energy Landscape Analysis in functional MRI.. *Research square*. [DOI: 10.21203/rs.3.rs-8428652/v1](https://doi.org/10.21203/rs.3.rs-8428652/v1)

- Gupta D, Du X, Summerfelt A, et al.. 2023. Brain Connectivity Signature Extractions from TMS Invoked EEGs.. *Sensors (Basel, Switzerland)*. [DOI: 10.3390/s23084078](https://doi.org/10.3390/s23084078)

- Yu L, Gong L, Chen X, et al.. 2025. Exploratory GABAa-informed control network modulates hyperarousal brain dynamics in chronic insomnia.. *Communications biology*. [DOI: 10.1038/s42003-025-08439-4](https://doi.org/10.1038/s42003-025-08439-4)

- Borzou A, Miller SN, Hommel JD, et al.. 2024. Cocaine diminishes functional network robustness and destabilizes the energy landscape of neuronal activity in the medial prefrontal cortex.. *PNAS nexus*. [DOI: 10.1093/pnasnexus/pgae092](https://doi.org/10.1093/pnasnexus/pgae092)

- Xin Q, Hao S, Xiaoqin W, et al.. 2024. Brain Source Localization and Functional Connectivity in Group Identity Regulation of Overbidding in Contest.. *Neuroscience*. [DOI: 10.1016/j.neuroscience.2024.01.016](https://doi.org/10.1016/j.neuroscience.2024.01.016)

- Sharpee TO, Destexhe A, Kawato M, et al.. 2016. 25th Annual Computational Neuroscience Meeting: CNS-2016.. *BMC neuroscience*. [DOI: 10.1186/s12868-016-0283-6](https://doi.org/10.1186/s12868-016-0283-6)

- Sneha NP, Dharshini SAP, Taguchi YH, et al.. 2022. Integrative Meta-Analysis of Huntington's Disease Transcriptome Landscape.. *Genes*. [DOI: 10.3390/genes13122385](https://doi.org/10.3390/genes13122385)

- Lee BH, Arya G. 2022. Assembly mechanism of surface-functionalized nanocubes.. *Nanoscale*. [DOI: 10.1039/d1nr07995f](https://doi.org/10.1039/d1nr07995f)

- Mosharov EV, Rosenberg AM, Monzel AS, et al.. 2025. A human brain map of mitochondrial respiratory capacity and diversity.. *Nature*. [DOI: 10.1038/s41586-025-08740-6](https://doi.org/10.1038/s41586-025-08740-6)

- Durstewitz D, Seamans JK, Sejnowski TJ. 2000. Neurocomputational models of working memory.. *Nature neuroscience*. [DOI: 10.1038/81460](https://doi.org/10.1038/81460)

- Zhao N, Song J, Liu S. 2023. Multi-timescale analysis of midbrain dopamine neuronal firing activities.. *Journal of theoretical biology*. [DOI: 10.1016/j.jtbi.2022.111310](https://doi.org/10.1016/j.jtbi.2022.111310)

- Looijestijn J, Blom JD, Aleman A, et al.. 2015. An integrated network model of psychotic symptoms.. *Neuroscience and biobehavioral reviews*. [DOI: 10.1016/j.neubiorev.2015.09.016](https://doi.org/10.1016/j.neubiorev.2015.09.016)

- Naudé J, Sarazin MXB, Mondoloni S, et al.. 2024. Dopamine builds and reveals reward-associated latent behavioral attractors.. *Nature communications*. [DOI: 10.1038/s41467-024-53976-x](https://doi.org/10.1038/s41467-024-53976-x)

- Stroh A, Schweiger S, Ramirez JM, et al.. 2024. The selfish network: how the brain preserves behavioral function through shifts in neuronal network state.. *Trends in neurosciences*. [DOI: 10.1016/j.tins.2024.02.005](https://doi.org/10.1016/j.tins.2024.02.005)

- Taylor NL, D'Souza A, Munn BR, et al.. 2022. Structural connections between the noradrenergic and cholinergic system shape the dynamics of functional brain networks.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2022.119455](https://doi.org/10.1016/j.neuroimage.2022.119455)

- Li Q, Calhoun VD, Pham TD, et al.. 2024. Exploring nonlinear dynamics in brain functionality through phase portraits and fuzzy recurrence plots.. *Chaos (Woodbury, N.Y.)*. [DOI: 10.1063/5.0203926](https://doi.org/10.1063/5.0203926)

- Mahrach A, Bestue D, Qi XL, et al.. 2024. Cholinergic neuromodulation of prefrontal attractor dynamics controls performance in spatial working memory.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2024.01.17.576071](https://doi.org/10.1101/2024.01.17.576071)

- Piccinini J, Deco G, Kringelbach M, et al.. 2022. Data-driven discovery of canonical large-scale brain dynamics.. *Cerebral cortex communications*. [DOI: 10.1093/texcom/tgac045](https://doi.org/10.1093/texcom/tgac045)

- Spalla D, Cornacchia IM, Treves A. 2021. Continuous attractors for dynamic memories.. *eLife*. [DOI: 10.7554/eLife.69499](https://doi.org/10.7554/eLife.69499)

- Burak Y. 2014. Spatial coding and attractor dynamics of grid cells in the entorhinal cortex.. *Current opinion in neurobiology*. [DOI: 10.1016/j.conb.2014.01.013](https://doi.org/10.1016/j.conb.2014.01.013)

- Gu J, Lim S. 2022. Unsupervised learning for robust working memory.. *PLoS computational biology*. [DOI: 10.1371/journal.pcbi.1009083](https://doi.org/10.1371/journal.pcbi.1009083)

- Friston K, FitzGerald T, Rigoli F, et al.. 2016. Active inference and learning.. *Neuroscience and biobehavioral reviews*. [DOI: 10.1016/j.neubiorev.2016.06.022](https://doi.org/10.1016/j.neubiorev.2016.06.022)

- Wise T, Emery K, Radulescu A. 2024. Naturalistic reinforcement learning.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2023.08.016](https://doi.org/10.1016/j.tics.2023.08.016)

- Geana A, Barch DM, Gold JM, et al.. 2022. Using Computational Modeling to Capture Schizophrenia-Specific Reinforcement Learning Differences and Their Implications on Patient Classification.. *Biological psychiatry. Cognitive neuroscience and neuroimaging*. [DOI: 10.1016/j.bpsc.2021.03.017](https://doi.org/10.1016/j.bpsc.2021.03.017)

- Gershman SJ, Lai L. 2021. The Reward-Complexity Trade-off in Schizophrenia.. *Computational psychiatry (Cambridge, Mass.)*. [DOI: 10.5334/cpsy.71](https://doi.org/10.5334/cpsy.71)

- Etkin A, Büchel C, Gross JJ. 2015. The neural bases of emotion regulation.. *Nature reviews. Neuroscience*. [DOI: 10.1038/nrn4044](https://doi.org/10.1038/nrn4044)

- Abend R, Burk D, Ruiz SG, et al.. 2022. Computational modeling of threat learning reveals links with anxiety and neuroanatomy in humans.. *eLife*. [DOI: 10.7554/eLife.66169](https://doi.org/10.7554/eLife.66169)

- Levy I, Schiller D. 2021. Neural Computations of Threat.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2020.11.007](https://doi.org/10.1016/j.tics.2020.11.007)

- Wehrli JM, Xia Y, Gerster S, et al.. 2022. Measuring human trace fear conditioning.. *Psychophysiology*. [DOI: 10.1111/psyp.14119](https://doi.org/10.1111/psyp.14119)

- Eldar E, Rutledge RB, Dolan RJ, et al.. 2016. Mood as Representation of Momentum.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2015.07.010](https://doi.org/10.1016/j.tics.2015.07.010)

- Hall AF, Browning M, Huys QJM. 2024. The computational structure of consummatory anhedonia.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2024.01.006](https://doi.org/10.1016/j.tics.2024.01.006)

- Zald DH, Treadway MT. 2017. Reward Processing, Neuroeconomics, and Psychopathology.. *Annual review of clinical psychology*. [DOI: 10.1146/annurev-clinpsy-032816-044957](https://doi.org/10.1146/annurev-clinpsy-032816-044957)

- Lan DCL, Browning M. 2022. What Can Reinforcement Learning Models of Dopamine and Serotonin Tell Us about the Action of Antidepressants?. *Computational psychiatry (Cambridge, Mass.)*. [DOI: 10.5334/cpsy.83](https://doi.org/10.5334/cpsy.83)

- Le Heron CJ. 2022. Reward and actions and the game of life.. *Journal of neurology, neurosurgery, and psychiatry*. [DOI: 10.1136/jnnp-2021-328302](https://doi.org/10.1136/jnnp-2021-328302)

- Fleming H, Robinson OJ, Roiser JP. 2023. Measuring cognitive effort without difficulty.. *Cognitive, affective & behavioral neuroscience*. [DOI: 10.3758/s13415-023-01065-9](https://doi.org/10.3758/s13415-023-01065-9)

- Story GW, Kurth-Nelson Z, Crockett M, et al.. 2020. Social discounting of pain.. *Journal of the experimental analysis of behavior*. [DOI: 10.1002/jeab.631](https://doi.org/10.1002/jeab.631)

- Smid CR, Kool W, Hauser TU, et al.. 2023. Computational and behavioral markers of model-based decision making in childhood.. *Developmental science*. [DOI: 10.1111/desc.13295](https://doi.org/10.1111/desc.13295)

- Hauser TU, Will GJ, Dubois M, et al.. 2019. Annual Research Review: Developmental computational psychiatry.. *Journal of child psychology and psychiatry, and allied disciplines*. [DOI: 10.1111/jcpp.12964](https://doi.org/10.1111/jcpp.12964)

- Mkrtchian A, Valton V, Roiser JP. 2023. Reliability of Decision-Making and Reinforcement Learning Computational Parameters.. *Computational psychiatry (Cambridge, Mass.)*. [DOI: 10.5334/cpsy.86](https://doi.org/10.5334/cpsy.86)

- Schaaf JV, Weidinger L, Molleman L, et al.. 2024. Test-retest reliability of reinforcement learning parameters.. *Behavior research methods*. [DOI: 10.3758/s13428-023-02203-4](https://doi.org/10.3758/s13428-023-02203-4)
## References

- Dominguez D, Koroutchev K, Serrano E, et al.. 2007. Information and topology in attractor neural networks.. *Neural computation*. [DOI: 10.1162/neco.2007.19.4.956](https://doi.org/10.1162/neco.2007.19.4.956)

- Zemel RS, Mozer MC. 2001. Localist attractor networks.. *Neural computation*. [DOI: 10.1162/08997660151134325](https://doi.org/10.1162/08997660151134325)

- Nair A, Karigo T, Yang B, et al.. 2023. An approximate line attractor in the hypothalamus encodes an aggressive state.. *Cell*. [DOI: 10.1016/j.cell.2022.11.027](https://doi.org/10.1016/j.cell.2022.11.027)

- Vinograd A, Nair A, Kim JH, et al.. 2024. Causal evidence of a line attractor encoding an affective state.. *Nature*. [DOI: 10.1038/s41586-024-07915-x](https://doi.org/10.1038/s41586-024-07915-x)

- Watanabe T, Hirose S, Wada H, et al.. 2014. Energy landscapes of resting-state brain networks.. *Frontiers in neuroinformatics*. [DOI: 10.3389/fninf.2014.00012](https://doi.org/10.3389/fninf.2014.00012)

- Kang J, Pae C, Park HJ. 2017. Energy landscape analysis of the subcortical brain network unravels system properties beneath resting state dynamics.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2017.01.075](https://doi.org/10.1016/j.neuroimage.2017.01.075)

- Rolls ET, Webb TJ. 2012. Cortical attractor network dynamics with diluted connectivity.. *Brain research*. [DOI: 10.1016/j.brainres.2011.08.002](https://doi.org/10.1016/j.brainres.2011.08.002)

- Chaudhuri R, Gerçek B, Pandey B, et al.. 2019. The intrinsic attractor manifold and population dynamics of a canonical cognitive circuit across waking and sleep.. *Nature neuroscience*. [DOI: 10.1038/s41593-019-0460-x](https://doi.org/10.1038/s41593-019-0460-x)

- Montague PR, Dolan RJ, Friston KJ, et al.. 2012. Computational psychiatry.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2011.11.018](https://doi.org/10.1016/j.tics.2011.11.018)

- Durstewitz D, Huys QJM, Koppe G. 2021. Psychiatric Illnesses as Disorders of Network Dynamics.. *Biological psychiatry. Cognitive neuroscience and neuroimaging*. [DOI: 10.1016/j.bpsc.2020.01.001](https://doi.org/10.1016/j.bpsc.2020.01.001)

- Regonia PR, Takamura M, Nakano T, et al.. 2021. Modeling Heterogeneous Brain Dynamics of Depression and Melancholia Using Energy Landscape Analysis.. *Frontiers in psychiatry*. [DOI: 10.3389/fpsyt.2021.780997](https://doi.org/10.3389/fpsyt.2021.780997)

- Rolls ET, Cheng W, Feng J. 2021. Brain dynamics: the temporal variability of connectivity, and differences in schizophrenia and ADHD.. *Translational psychiatry*. [DOI: 10.1038/s41398-021-01197-x](https://doi.org/10.1038/s41398-021-01197-x)

- Iravani B, Arshamian A, Fransson P, et al.. 2021. Whole-brain modelling of resting state fMRI differentiates ADHD subtypes and facilitates stratified neuro-stimulation therapy.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2021.117844](https://doi.org/10.1016/j.neuroimage.2021.117844)

- Jing R, Li P, Zhao K, et al.. 2025. Energy-Landscape Analysis of Brain Network Dynamics in a Multicenter Alzheimer's Disease and Mild Cognitive Impairment Cohort.. *Biological psychiatry*. [DOI: 10.1016/j.biopsych.2025.07.022](https://doi.org/10.1016/j.biopsych.2025.07.022)

- Núñez P, Tewarie P, Rodríguez-González V, et al.. 2025. Altered electrophysiological meta-state dynamics in disorders of consciousness.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2025.121519](https://doi.org/10.1016/j.neuroimage.2025.121519)

- Balaguer-Ballester E, Moreno-Bote R, Deco G, et al.. 2017. Editorial: Metastable Dynamics of Neural Ensembles.. *Frontiers in systems neuroscience*. [DOI: 10.3389/fnsys.2017.00099](https://doi.org/10.3389/fnsys.2017.00099)

- Vinograd A, Nair A, Linderman SW, et al.. 2024. Intrinsic Dynamics and Neural Implementation of a Hypothalamic Line Attractor Encoding an Internal Behavioral State.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2024.05.21.595051](https://doi.org/10.1101/2024.05.21.595051)

- Liu M, Nair A, Coria N, et al.. 2024. Encoding of female mating dynamics by a hypothalamic line attractor.. *Nature*. [DOI: 10.1038/s41586-024-07916-w](https://doi.org/10.1038/s41586-024-07916-w)

- Ajabi Z, Keinath AT, Wei XX, et al.. 2023. Population dynamics of head-direction neurons during drift and reorientation.. *Nature*. [DOI: 10.1038/s41586-023-05813-2](https://doi.org/10.1038/s41586-023-05813-2)

- Piñero J, Solé R. 2019. Statistical physics of liquid brains.. *Philosophical transactions of the Royal Society of London. Series B, Biological sciences*. [DOI: 10.1098/rstb.2018.0376](https://doi.org/10.1098/rstb.2018.0376)

- Liu M, Nair A, Linderman SW, et al.. 2023. Periodic hypothalamic attractor-like dynamics during the estrus cycle.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2023.05.22.541741](https://doi.org/10.1101/2023.05.22.541741)

- Kirillov SY, Smelov PS, Klinshov VV. 2024. Collective dynamics and shot-noise-induced switching in a two-population neural network.. *Chaos (Woodbury, N.Y.)*. [DOI: 10.1063/5.0193275](https://doi.org/10.1063/5.0193275)

- Mazzucato L. 2022. Neural mechanisms underlying the temporal organization of naturalistic animal behavior.. *eLife*. [DOI: 10.7554/eLife.76577](https://doi.org/10.7554/eLife.76577)

- Mininni CJ, Zanutto BS. 2024. Constructing neural networks with pre-specified dynamics.. *Scientific reports*. [DOI: 10.1038/s41598-024-69747-z](https://doi.org/10.1038/s41598-024-69747-z)

- Sedler AR, Versteeg C, Pandarinath C. 2023. Expressive architectures enhance interpretability of dynamics-based neural population models.. *Neurons, behavior, data analysis, and theory*. [DOI: 10.51628/001c.73987](https://doi.org/10.51628/001c.73987)

- Genkin M, Shenoy KV, Chandrasekaran C, et al.. 2025. The dynamics and geometry of choice in the premotor cortex.. *Nature*. [DOI: 10.1038/s41586-025-09199-1](https://doi.org/10.1038/s41586-025-09199-1)

- Inagaki HK, Chen S, Daie K, et al.. 2022. Neural Algorithms and Circuits for Motor Planning.. *Annual review of neuroscience*. [DOI: 10.1146/annurev-neuro-092021-121730](https://doi.org/10.1146/annurev-neuro-092021-121730)

- Sylwestrak EL, Jo Y, Vesuna S, et al.. 2022. Cell-type-specific population dynamics of diverse reward computations.. *Cell*. [DOI: 10.1016/j.cell.2022.08.019](https://doi.org/10.1016/j.cell.2022.08.019)

- Aitken K, Mihalas S. 2023. Neural population dynamics of computing with synaptic modulations.. *eLife*. [DOI: 10.7554/eLife.83035](https://doi.org/10.7554/eLife.83035)

- Tajima S, Koida K, Tajima CI, et al.. 2017. Task-dependent recurrent dynamics in visual cortex.. *eLife*. [DOI: 10.7554/eLife.26868](https://doi.org/10.7554/eLife.26868)

- Kotler S, Mannino M, Friston K, et al.. 2025. Pathfinding: a neurodynamical account of intuition.. *Communications biology*. [DOI: 10.1038/s42003-025-08612-9](https://doi.org/10.1038/s42003-025-08612-9)

- Thivierge JP, Comas R, Longtin A. 2014. Attractor dynamics in local neuronal networks.. *Frontiers in neural circuits*. [DOI: 10.3389/fncir.2014.00022](https://doi.org/10.3389/fncir.2014.00022)

- Rennó-Costa C, Lisman JE, Verschure PF. 2014. A signature of attractor dynamics in the CA3 region of the hippocampus.. *PLoS computational biology*. [DOI: 10.1371/journal.pcbi.1003641](https://doi.org/10.1371/journal.pcbi.1003641)

- Kim CS. 2018. Recognition Dynamics in the Brain under the Free Energy Principle.. *Neural computation*. [DOI: 10.1162/neco_a_01115](https://doi.org/10.1162/neco_a_01115)

- Kong X, Kong R, Orban C, et al.. 2021. Sensory-motor cortices shape functional connectivity dynamics in the human brain.. *Nature communications*. [DOI: 10.1038/s41467-021-26704-y](https://doi.org/10.1038/s41467-021-26704-y)

- Olguín-Rodríguez PV, Arzate-Mena JD, Corsi-Cabrera M, et al.. 2018. Characteristic Fluctuations Around Stable Attractor Dynamics Extracted from Highly Nonstationary Electroencephalographic Recordings.. *Brain connectivity*. [DOI: 10.1089/brain.2018.0609](https://doi.org/10.1089/brain.2018.0609)

- Tort-Colet N, Capone C, Sanchez-Vives MV, et al.. 2021. Attractor competition enriches cortical dynamics during awakening from anesthesia.. *Cell reports*. [DOI: 10.1016/j.celrep.2021.109270](https://doi.org/10.1016/j.celrep.2021.109270)

- Laptev D, Burgess N. 2019. Neural Dynamics Indicate Parallel Integration of Environmental and Self-Motion Information by Place and Grid Cells.. *Frontiers in neural circuits*. [DOI: 10.3389/fncir.2019.00059](https://doi.org/10.3389/fncir.2019.00059)

- Bonaiuto JJ, Bestmann S. 2015. Understanding the nonlinear physiological and behavioral effects of tDCS through computational neurostimulation.. *Progress in brain research*. [DOI: 10.1016/bs.pbr.2015.06.013](https://doi.org/10.1016/bs.pbr.2015.06.013)

- Koch D, Nandan A, Ramesan G, et al.. 2024. Biological computations: Limitations of attractor-based formalisms and the need for transients.. *Biochemical and biophysical research communications*. [DOI: 10.1016/j.bbrc.2024.150069](https://doi.org/10.1016/j.bbrc.2024.150069)

- Shah OS, Chaudhary MFA, Awan HA, et al.. 2018. ATLANTIS - Attractor Landscape Analysis Toolbox for Cell Fate Discovery and Reprogramming.. *Scientific reports*. [DOI: 10.1038/s41598-018-22031-3](https://doi.org/10.1038/s41598-018-22031-3)

- Zhang X, Chong KH, Zhu L, et al.. 2020. A Monte Carlo method for in silico modeling and visualization of Waddington's epigenetic landscape with intermediate details.. *Bio Systems*. [DOI: 10.1016/j.biosystems.2020.104275](https://doi.org/10.1016/j.biosystems.2020.104275)

- Kang J, Jeong SO, Pae C, et al.. 2021. Bayesian estimation of maximum entropy model for individualized energy landscape analysis of brain state dynamics.. *Human brain mapping*. [DOI: 10.1002/hbm.25442](https://doi.org/10.1002/hbm.25442)

- Nakamura T. 2024. Derivation of the Invariant Free-Energy Landscape Based on Langevin Dynamics.. *Physical review letters*. [DOI: 10.1103/PhysRevLett.132.137101](https://doi.org/10.1103/PhysRevLett.132.137101)

- Ayaz C, Tepper L, Brünig FN, et al.. 2021. Non-Markovian modeling of protein folding.. *Proceedings of the National Academy of Sciences of the United States of America*. [DOI: 10.1073/pnas.2023856118](https://doi.org/10.1073/pnas.2023856118)

- Xing L, Guo Z, Long Z. 2024. Energy landscape analysis of brain network dynamics in Alzheimer's disease.. *Frontiers in aging neuroscience*. [DOI: 10.3389/fnagi.2024.1375091](https://doi.org/10.3389/fnagi.2024.1375091)

- Allen JD, Varanasi S, Han F, et al.. 2024. Functional Connectivity Biomarker Extraction for Schizophrenia Based on Energy Landscape Machine Learning Techniques.. *Sensors (Basel, Switzerland)*. [DOI: 10.3390/s24237742](https://doi.org/10.3390/s24237742)

- Ishida T, Yamada S, Yasuda K, et al.. 2024. Aberrant brain dynamics of large-scale functional networks across schizophrenia and mood disorder.. *NeuroImage. Clinical*. [DOI: 10.1016/j.nicl.2024.103574](https://doi.org/10.1016/j.nicl.2024.103574)

- Theis N, Bahuguna J, Rubin JE, et al.. 2024. Energy of functional brain states correlates with cognition in adolescent-onset schizophrenia and healthy persons.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2023.11.06.565753](https://doi.org/10.1101/2023.11.06.565753)

- Prasad K, Bowei O, Theis N. 2025. From microstates to macroscales: A Critical Review of Maximum Entropy Modeling and Energy Landscape Analysis in functional MRI.. *Research square*. [DOI: 10.21203/rs.3.rs-8428652/v1](https://doi.org/10.21203/rs.3.rs-8428652/v1)

- Gupta D, Du X, Summerfelt A, et al.. 2023. Brain Connectivity Signature Extractions from TMS Invoked EEGs.. *Sensors (Basel, Switzerland)*. [DOI: 10.3390/s23084078](https://doi.org/10.3390/s23084078)

- Yu L, Gong L, Chen X, et al.. 2025. Exploratory GABAa-informed control network modulates hyperarousal brain dynamics in chronic insomnia.. *Communications biology*. [DOI: 10.1038/s42003-025-08439-4](https://doi.org/10.1038/s42003-025-08439-4)

- Borzou A, Miller SN, Hommel JD, et al.. 2024. Cocaine diminishes functional network robustness and destabilizes the energy landscape of neuronal activity in the medial prefrontal cortex.. *PNAS nexus*. [DOI: 10.1093/pnasnexus/pgae092](https://doi.org/10.1093/pnasnexus/pgae092)

- Xin Q, Hao S, Xiaoqin W, et al.. 2024. Brain Source Localization and Functional Connectivity in Group Identity Regulation of Overbidding in Contest.. *Neuroscience*. [DOI: 10.1016/j.neuroscience.2024.01.016](https://doi.org/10.1016/j.neuroscience.2024.01.016)

- Sharpee TO, Destexhe A, Kawato M, et al.. 2016. 25th Annual Computational Neuroscience Meeting: CNS-2016.. *BMC neuroscience*. [DOI: 10.1186/s12868-016-0283-6](https://doi.org/10.1186/s12868-016-0283-6)

- Sneha NP, Dharshini SAP, Taguchi YH, et al.. 2022. Integrative Meta-Analysis of Huntington's Disease Transcriptome Landscape.. *Genes*. [DOI: 10.3390/genes13122385](https://doi.org/10.3390/genes13122385)

- Lee BH, Arya G. 2022. Assembly mechanism of surface-functionalized nanocubes.. *Nanoscale*. [DOI: 10.1039/d1nr07995f](https://doi.org/10.1039/d1nr07995f)

- Mosharov EV, Rosenberg AM, Monzel AS, et al.. 2025. A human brain map of mitochondrial respiratory capacity and diversity.. *Nature*. [DOI: 10.1038/s41586-025-08740-6](https://doi.org/10.1038/s41586-025-08740-6)

- Durstewitz D, Seamans JK, Sejnowski TJ. 2000. Neurocomputational models of working memory.. *Nature neuroscience*. [DOI: 10.1038/81460](https://doi.org/10.1038/81460)

- Zhao N, Song J, Liu S. 2023. Multi-timescale analysis of midbrain dopamine neuronal firing activities.. *Journal of theoretical biology*. [DOI: 10.1016/j.jtbi.2022.111310](https://doi.org/10.1016/j.jtbi.2022.111310)

- Looijestijn J, Blom JD, Aleman A, et al.. 2015. An integrated network model of psychotic symptoms.. *Neuroscience and biobehavioral reviews*. [DOI: 10.1016/j.neubiorev.2015.09.016](https://doi.org/10.1016/j.neubiorev.2015.09.016)

- Naudé J, Sarazin MXB, Mondoloni S, et al.. 2024. Dopamine builds and reveals reward-associated latent behavioral attractors.. *Nature communications*. [DOI: 10.1038/s41467-024-53976-x](https://doi.org/10.1038/s41467-024-53976-x)

- Stroh A, Schweiger S, Ramirez JM, et al.. 2024. The selfish network: how the brain preserves behavioral function through shifts in neuronal network state.. *Trends in neurosciences*. [DOI: 10.1016/j.tins.2024.02.005](https://doi.org/10.1016/j.tins.2024.02.005)

- Taylor NL, D'Souza A, Munn BR, et al.. 2022. Structural connections between the noradrenergic and cholinergic system shape the dynamics of functional brain networks.. *NeuroImage*. [DOI: 10.1016/j.neuroimage.2022.119455](https://doi.org/10.1016/j.neuroimage.2022.119455)

- Li Q, Calhoun VD, Pham TD, et al.. 2024. Exploring nonlinear dynamics in brain functionality through phase portraits and fuzzy recurrence plots.. *Chaos (Woodbury, N.Y.)*. [DOI: 10.1063/5.0203926](https://doi.org/10.1063/5.0203926)

- Mahrach A, Bestue D, Qi XL, et al.. 2024. Cholinergic neuromodulation of prefrontal attractor dynamics controls performance in spatial working memory.. *bioRxiv : the preprint server for biology*. [DOI: 10.1101/2024.01.17.576071](https://doi.org/10.1101/2024.01.17.576071)

- Piccinini J, Deco G, Kringelbach M, et al.. 2022. Data-driven discovery of canonical large-scale brain dynamics.. *Cerebral cortex communications*. [DOI: 10.1093/texcom/tgac045](https://doi.org/10.1093/texcom/tgac045)

- Spalla D, Cornacchia IM, Treves A. 2021. Continuous attractors for dynamic memories.. *eLife*. [DOI: 10.7554/eLife.69499](https://doi.org/10.7554/eLife.69499)

- Burak Y. 2014. Spatial coding and attractor dynamics of grid cells in the entorhinal cortex.. *Current opinion in neurobiology*. [DOI: 10.1016/j.conb.2014.01.013](https://doi.org/10.1016/j.conb.2014.01.013)

- Gu J, Lim S. 2022. Unsupervised learning for robust working memory.. *PLoS computational biology*. [DOI: 10.1371/journal.pcbi.1009083](https://doi.org/10.1371/journal.pcbi.1009083)

- Friston K, FitzGerald T, Rigoli F, et al.. 2016. Active inference and learning.. *Neuroscience and biobehavioral reviews*. [DOI: 10.1016/j.neubiorev.2016.06.022](https://doi.org/10.1016/j.neubiorev.2016.06.022)

- Wise T, Emery K, Radulescu A. 2024. Naturalistic reinforcement learning.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2023.08.016](https://doi.org/10.1016/j.tics.2023.08.016)

- Geana A, Barch DM, Gold JM, et al.. 2022. Using Computational Modeling to Capture Schizophrenia-Specific Reinforcement Learning Differences and Their Implications on Patient Classification.. *Biological psychiatry. Cognitive neuroscience and neuroimaging*. [DOI: 10.1016/j.bpsc.2021.03.017](https://doi.org/10.1016/j.bpsc.2021.03.017)

- Gershman SJ, Lai L. 2021. The Reward-Complexity Trade-off in Schizophrenia.. *Computational psychiatry (Cambridge, Mass.)*. [DOI: 10.5334/cpsy.71](https://doi.org/10.5334/cpsy.71)

- Etkin A, Büchel C, Gross JJ. 2015. The neural bases of emotion regulation.. *Nature reviews. Neuroscience*. [DOI: 10.1038/nrn4044](https://doi.org/10.1038/nrn4044)

- Abend R, Burk D, Ruiz SG, et al.. 2022. Computational modeling of threat learning reveals links with anxiety and neuroanatomy in humans.. *eLife*. [DOI: 10.7554/eLife.66169](https://doi.org/10.7554/eLife.66169)

- Levy I, Schiller D. 2021. Neural Computations of Threat.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2020.11.007](https://doi.org/10.1016/j.tics.2020.11.007)

- Wehrli JM, Xia Y, Gerster S, et al.. 2022. Measuring human trace fear conditioning.. *Psychophysiology*. [DOI: 10.1111/psyp.14119](https://doi.org/10.1111/psyp.14119)

- Eldar E, Rutledge RB, Dolan RJ, et al.. 2016. Mood as Representation of Momentum.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2015.07.010](https://doi.org/10.1016/j.tics.2015.07.010)

- Hall AF, Browning M, Huys QJM. 2024. The computational structure of consummatory anhedonia.. *Trends in cognitive sciences*. [DOI: 10.1016/j.tics.2024.01.006](https://doi.org/10.1016/j.tics.2024.01.006)

- Zald DH, Treadway MT. 2017. Reward Processing, Neuroeconomics, and Psychopathology.. *Annual review of clinical psychology*. [DOI: 10.1146/annurev-clinpsy-032816-044957](https://doi.org/10.1146/annurev-clinpsy-032816-044957)

- Lan DCL, Browning M. 2022. What Can Reinforcement Learning Models of Dopamine and Serotonin Tell Us about the Action of Antidepressants?. *Computational psychiatry (Cambridge, Mass.)*. [DOI: 10.5334/cpsy.83](https://doi.org/10.5334/cpsy.83)

- Le Heron CJ. 2022. Reward and actions and the game of life.. *Journal of neurology, neurosurgery, and psychiatry*. [DOI: 10.1136/jnnp-2021-328302](https://doi.org/10.1136/jnnp-2021-328302)

- Fleming H, Robinson OJ, Roiser JP. 2023. Measuring cognitive effort without difficulty.. *Cognitive, affective & behavioral neuroscience*. [DOI: 10.3758/s13415-023-01065-9](https://doi.org/10.3758/s13415-023-01065-9)

- Story GW, Kurth-Nelson Z, Crockett M, et al.. 2020. Social discounting of pain.. *Journal of the experimental analysis of behavior*. [DOI: 10.1002/jeab.631](https://doi.org/10.1002/jeab.631)

- Smid CR, Kool W, Hauser TU, et al.. 2023. Computational and behavioral markers of model-based decision making in childhood.. *Developmental science*. [DOI: 10.1111/desc.13295](https://doi.org/10.1111/desc.13295)

- Hauser TU, Will GJ, Dubois M, et al.. 2019. Annual Research Review: Developmental computational psychiatry.. *Journal of child psychology and psychiatry, and allied disciplines*. [DOI: 10.1111/jcpp.12964](https://doi.org/10.1111/jcpp.12964)

- Mkrtchian A, Valton V, Roiser JP. 2023. Reliability of Decision-Making and Reinforcement Learning Computational Parameters.. *Computational psychiatry (Cambridge, Mass.)*. [DOI: 10.5334/cpsy.86](https://doi.org/10.5334/cpsy.86)

- Schaaf JV, Weidinger L, Molleman L, et al.. 2024. Test-retest reliability of reinforcement learning parameters.. *Behavior research methods*. [DOI: 10.3758/s13428-023-02203-4](https://doi.org/10.3758/s13428-023-02203-4)


