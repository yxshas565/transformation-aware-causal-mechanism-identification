# Transformation Aware Causal Mechanism Equivalence

## 1. Purpose

This document defines the formal object that TACMI attempts to identify:

> whether a transformed model preserves the same underlying causal mechanism as an original model.

The target is stronger than behavioral equivalence and different from representational similarity.

TACMI studies models related by a known transformation:

\[
M' = T(M)
\]

where \(M\) is the original model, \(T\) is a known transformation, and \(M'\) is the transformed model.

Examples of transformations include:

1. LoRA adaptation
2. Fine tuning
3. Weight merging
4. Quantization
5. Model editing
6. Distillation

The central question is whether the causal computation responsible for a target capability survives the transformation.

---

## 2. Three Levels of Equivalence

TACMI distinguishes three different notions of equivalence.

### 2.1 Behavioral equivalence

Two models are behaviorally equivalent over an evaluation distribution if they produce sufficiently similar observable outputs.

For models \(M\) and \(M'\):

\[
M \approx_B M'
\]

means that their externally observable behavior is sufficiently similar under the chosen evaluation.

Behavioral equivalence alone does not establish that the same internal mechanism produces the behavior.

---

### 2.2 Representational equivalence

Two models are representationally equivalent if their internal representations satisfy a specified similarity relation.

For example:

\[
M \approx_R M'
\]

could be evaluated using representation similarity measures such as:

1. CKA
2. CCA
3. cosine similarity
4. Procrustes alignment

These measures can establish similarity between representations under their respective assumptions.

They do not, by themselves, establish preservation of causal mechanism.

---

### 2.3 Causal mechanism equivalence

The primary TACMI target is causal mechanism equivalence.

Informally:

> Two models are causally mechanism equivalent when corresponding interventions on the models produce equivalent causal responses, under an explicitly defined intervention correspondence and tolerance.

We denote this as:

\[
M \approx_C^{(\omega,\epsilon)} M'
\]

where:

* \(\omega\) maps interventions on the original model to corresponding interventions on the transformed model.
* \(\epsilon\) specifies the permitted causal-response divergence.

This definition is intentionally conditional on the intervention family and intervention correspondence.

---

## 3. Intervention Response

Let:

\[
I \in \mathcal{I}
\]

denote an intervention available to the evaluation procedure.

For an input \(x\), define the causal response of model \(M\) to intervention \(I\) as:

\[
K_M(I,x)
\]

Similarly, for the transformed model:

\[
K_{M'}(I',x)
\]

where \(I'\) is the corresponding intervention in the transformed model.

The intervention response may contain any explicitly defined observable consequence of the intervention, including:

1. output changes
2. internal activation changes
3. downstream state changes
4. task-specific causal effects

The exact response representation must be specified by the experiment.

---

## 4. Intervention Correspondence

Because a transformation can change coordinates or internal parameterization, the same literal intervention need not remain meaningful after transformation.

Therefore TACMI introduces an intervention correspondence:

\[
\omega : \mathcal{I}_M \rightarrow \mathcal{I}_{M'}
\]

where:

* \(\mathcal{I}_M\) is the intervention family available on \(M\)
* \(\mathcal{I}_{M'}\) is the intervention family available on \(M'\)
* \(\omega(I)\) is the transformed-model intervention corresponding to \(I\)

The construction of \(\omega\) is part of the scientific problem.

It must not be assumed that identical coordinates imply identical causal meaning.

---

## 5. Causal Mechanism Equivalence

Given an intervention family \(\mathcal{I}\), intervention correspondence \(\omega\), input domain \(\mathcal{X}\), and divergence measure \(D\), define causal mechanism equivalence under tolerance \(\epsilon\) as:

\[
\sup_{x \in \mathcal{X}, I \in \mathcal{I}}
D
\left(
K_M(I,x),
K_{M'}(\omega(I),x)
\right)
\leq \epsilon
\]

If this condition holds, we say that \(M'\) preserves the tested causal mechanism of \(M\) under:

1. the selected intervention family
2. the selected intervention correspondence
3. the selected response representation
4. the selected divergence measure
5. the selected tolerance

This is a restricted equivalence claim.

It is not a claim of unrestricted mechanistic equivalence across every possible intervention.

---

## 6. Finite Identification Problem

The definition above may require evaluating a potentially large or infinite intervention and input space.

TACMI therefore studies a finite identification problem.

Given:

\[
\mathcal{I}_{test}
\subseteq
\mathcal{I}
\]

and:

\[
\mathcal{X}_{test}
\subseteq
\mathcal{X}
\]

the practical objective is to determine whether the tested evidence is sufficient to support a mechanism-preservation claim.

The central research question is:

> Under what realistic restrictions can a finite set of interventions provide sufficient evidence that a transformed model preserves a causal mechanism?

This is distinct from simply measuring whether the models behave similarly.

---

## 7. Transformation Condition

The transformation:

\[
M' = T(M)
\]

provides structural information that may constrain the space of possible transformed mechanisms.

Examples:

### LoRA

\[
W' = W + BA
\]

where the update is constrained by the low rank of \(BA\).

### Quantization

The transformation constrains parameter values through a discretization procedure.

### Weight merging

The transformed model is constrained by a known composition of source parameter sets.

### Model editing

The transformation may impose locality or targeted modification assumptions.

TACMI investigates whether this transformation information can be used to construct more informative causal interventions.

---

## 8. Transformation Conditioned Identification

The proposed TACMI workflow is:

\[
M
\rightarrow
T
\rightarrow
M'
\]

followed by:

\[
\text{transformation constraints}
\rightarrow
\text{mechanism hypothesis space}
\rightarrow
\text{intervention selection}
\rightarrow
\text{causal response matrix}
\rightarrow
\text{mechanism identity test}
\]

The key hypothesis is that intervention selection conditioned on the known transformation may provide information that is unavailable from generic similarity measures or transformation agnostic intervention selection.

This is a research hypothesis, not an established result.

---

## 9. What This Definition Does Not Claim

This specification does not currently claim:

1. that TACMI can identify arbitrary mechanisms from finite observations
2. that causal mechanism equivalence is universally identifiable
3. that transformation conditioned intervention selection is novel relative to all existing active experiment design methods
4. that the proposed method is already superior to causal tracing, activation patching, interchange interventions, causal abstraction, or optimal experiment design
5. that LoRA preservation implies mechanism preservation
6. that behavioral equivalence implies causal mechanism equivalence
7. that representation similarity implies causal mechanism equivalence

These remain empirical or theoretical questions.

---

## 10. Core Scientific Hypothesis

The central hypothesis under investigation is:

> Given a known transformation and appropriate structural restrictions induced by that transformation, a finite and efficiently selected set of causal interventions may be sufficient to distinguish preservation of an underlying mechanism from behaviorally equivalent replacement mechanisms.

The hypothesis is considered successful only if it survives comparison against strong existing baselines and deliberately constructed adversarial cases.

---

## 11. Identification Failure Cases

The evaluation must explicitly include cases where commonly used measurements are misleading.

At minimum:

1. Same mechanism with a coordinate transformation.
2. Different mechanisms with nearly identical outputs.
3. Same evaluation outputs but different counterfactual behavior.
4. Different representations with equivalent intervention responses.
5. Strong representation similarity despite mechanism change.
6. Large parameter update with mechanism preservation.
7. Small parameter update with mechanism change.

A method that fails to distinguish these cases cannot be treated as evidence of causal mechanism identification.

---

## 12. Current Epistemic Status

The following claims are treated as hypotheses or research targets rather than established facts:

1. A useful restricted form of causal mechanism identification may be possible.
2. Transformation structure may reduce the relevant hypothesis space.
3. Transformation conditioned intervention selection may outperform generic intervention selection.
4. A finite mechanism-preservation certificate may be possible under explicit assumptions.
5. A nontrivial identifiability result or lower bound may exist for restricted transformation classes.

The research program must attempt to falsify these claims.

---

## 13. Next Formalization Tasks

The next stages of formalization are:

1. Define the mechanism representation.
2. Define the intervention space.
3. Define the causal response space.
4. Define admissible intervention correspondences.
5. Define the divergence measure.
6. Define what constitutes a mechanism-preservation certificate.
7. Define the assumptions under which finite identification may be possible.
8. Construct mechanisms for which behavioral equivalence and causal mechanism equivalence disagree.

These definitions must be resolved before the main synthetic benchmark is implemented.