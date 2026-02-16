The metastability framework captures the spatiotemporal dynamics given as the vari-
ability of states of phase configurations as a function of time (Cabral et al., 2014;
Deco et al., 2017a), i.e., how the synchronisation between the different nodes fluctu-
ates across time (Wildie and Shanahan, 2012). Thus, the metastability can be meas-
ured as the standard deviation of the Kuramoto order parameter across time, defined
by following equation:
(2.4)
where is the instantaneous phase of each narrowband BOLD signal at node k.
The Kuramoto order parameter measures the global level of synchronisation of the n
oscillating signals. Under complete independence, the n phases are uniformly distrib-
uted and thus R is nearly zero, whereas R =1 if all phases are equal (full synchronisa-
tion) (see Figure 2.4)

Please note that here we define the global metastability as the variability across time of
the global Kuramoto parameter, that is the global level of synchronisation. It is of
course possible—and necessary—to define a measure of local metastability, that is the
variability of the local level of spacetime synchronisation. We will return to this impor-
tant topic in Chapter 9 and show that this measure is essential to measuring turbu-
lence in the brain

The PMS framework (with LEiDA) is a precise description of the spatiotemporal
dynamics of whole-brain activity (Deco et al., 2019). For a given brain state, this esti-
mates the underlying constituent networks and the transitions over time between
these. The first step is to pre-process time series in a given parcellation and Hilbert-
transformed these to yield the phase evolution of the regional signals. The dynamic
functional connectivity (dFC) is given by the phase coherence for each pair of regions
at any given time, which is defined as the cosine of the phase differences:
(2.6)
where n and p are pairs of brain regions at time t. This definition means that pairwise
signals changing in exactly the same or opposite direction, will have values varying
from 1 to –1, respectively.
This process yields a 3D matrix, where N is number of brain regions in a
given parcellation and T is the number of timepoints. The metastable states are then
determined through clustering of the large number of dFC matrices over time.
Reducing the very large dimensionality of the dFC matrices can significantly improve
the signal-to-noise ratio. One popular way to estimate the metastable states is to use
the Leading Eigenvector Dynamics Analysis (LEiDA) method (Cabral et al., 2017) (see
Figure 2.5).
LEiDA relies on the extraction of the first N-dimensional eigenvector, V1, of each
dFC matrix, from which one can reliably detect a discrete number of reduced dFC pat-
terns by applying clustering across time points and subjects. With the symmetry of the
dFC matrices, each leading eigenvector may be used in turn to estimate the instantane-
ous corresponding dFC matrix by computing V1.V1T. LEiDA uses k-clustering to
obtain the centroids that define the ‘metastable substates’, for which one can compute
the probability of the centroid, as well as transition probabilities. This quantifies the
probability of occurrence of each FC state in each condition. The probability of occur-
rence (or fractional occupancy) is simply the ratio of the number of epochs assigned to
a given cluster centroid Vc divided by the total number of epochs (TRs) in each exper-
imental condition (which is the same in all experimental conditions). The probabilities
were calculated for each subject, in each experimental condition and for the whole
range of the explored clustering conditions. This allows for the estimation of the
switching matrix, which captures the trajectories of PMS dynamics in a directional
manner. In more detail, it indicates the probability of being in a given substate (rows)
and transitioning to any of the other substates (columns). Differences in probabilities
of occurrence and probabilities of transition can be statistically assessed between con-
ditions using a permutation-based paired t-test.



제공된 자료를 바탕으로 **'Metastability(메타안정성)'**가 무엇인지 이해하기 쉽게 설명해 드리겠습니다.

간단히 말해, Metastability는 뇌가 **특정한 하나의 상태에 고정되지 않고, 다양한 상태로 끊임없이 변화할 수 있는 능력(유연성)**을 의미합니다.

자료에 근거한 구체적인 정의와 측정 방식은 다음과 같습니다.

### 1. Metastability의 핵심 개념

Metastability는 뇌의 시공간적 역학(spatiotemporal dynamics)을 설명하는 지표로, **시간에 따라 뇌 영역 간의 동기화(synchronization) 수준이 얼마나 변동하는지**를 나타냅니다.

- 뇌가 완전히 무질서한 상태(동기화 0)도 아니고, 완전히 굳어버린 상태(완전 동기화)도 아닌, 그 사이에서 끊임없이 동기화 수준이 출렁이며 변화하는 상태를 말합니다.

### 2. 어떻게 측정하나? (쿠라모토 질서 변수)

이 개념을 수학적으로 측정하기 위해 **'쿠라모토 질서 변수(Kuramoto order parameter)'**라는 것을 사용합니다.

- **쿠라모토 질서 변수 ($R$):** 뇌의 신호들이 얼마나 전역적으로 동기화되었는지를 0과 1 사이의 값으로 보여줍니다. $R=1$이면 모든 신호의 위상(phase)이 일치하여 완전히 동기화된 것이고, $R=0$에 가까우면 서로 독립적으로 제각각 움직이는 상태입니다.
- **Metastability의 계산:** 시간의 흐름에 따른 **쿠라모토 질서 변수($R$)의 표준편차(Standard Deviation)**로 계산합니다,.

### 3. 쉽게 이해하기 (직관적 해석)

- **낮은 Metastability:** 뇌가 항상 완전히 동기화되어 있거나($R$이 계속 1), 혹은 항상 따로따로 놀고 있다면($R$이 계속 0), $R$ 값에 변화가 없으므로 표준편차가 작아져 Metastability는 낮습니다. 이는 뇌가 경직되어 있거나 통합되지 못함을 의미합니다.
- **높은 Metastability:** 뇌의 동기화 수준($R$)이 시간에 따라 높았다가 낮았다가 하며 크게 변동한다면 표준편차가 커지고 Metastability가 높게 나옵니다. 이는 뇌가 필요에 따라 정보를 통합(동기화)하거나 분리(비동기화)하면서 유연하게 작동하고 있다는 뜻입니다.

요약하자면, Metastability는 뇌 전체의 동기화 수준이 시간에 따라 얼마나 역동적으로 흔들리는지를 보여주는 지표이며, 이는 뇌가 고정된 상태에 머물지 않고 다양한 인지 활동을 수행할 수 있는 잠재력을 가지고 있음을 시사합니다.


