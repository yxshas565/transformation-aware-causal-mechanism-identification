# TACMI Adversarial Mechanism Cases

## Purpose

This document defines deliberately constructed model pairs that test whether causal mechanism equivalence can be distinguished from behavioral and representational similarity.

The cases are intended to falsify weak identification strategies.

---

# Case 1: Same Behavior, Different Mechanism

## Construction

Construct two models:

\[
M_A
\]

and

\[
M_B
\]

such that:

\[
M_A(x) = M_B(x)
\]

for all inputs in the evaluation distribution, while their internal causal computations differ.

### Example

Let the target function be:

\[
y = x_1 \oplus x_2
\]

Model A computes XOR directly through an internal feature:

\[
z_A = x_1 \oplus x_2
\]

and outputs:

\[
y_A = z_A
\]

Model B computes the same output through a different decomposition, for example by representing the Boolean function through an alternative internal basis.

The two models therefore have identical observable behavior while implementing different internal causal pathways.

## Required property

\[
M_A \approx_B M_B
\]

but:

\[
M_A \not\approx_C M_B
\]

under an intervention family capable of distinguishing their causal pathways.

## Purpose

This case tests whether behavioral evaluation alone incorrectly concludes mechanism preservation.

---

# Case 2: Same Mechanism, Different Representation

## Construction

Construct two models that implement the same causal computation but use different internal coordinates.

Let:

\[
z_B = Pz_A
\]

where \(P\) is an invertible transformation.

The downstream computation is adjusted consistently so that the same causal computation is preserved.

The representations therefore differ while the underlying causal relationships remain equivalent.

## Required property

Representation similarity may be low:

\[
M_A \not\approx_R M_B
\]

while causal mechanism equivalence holds:

\[
M_A \approx_C M_B
\]

under the correctly translated intervention correspondence.

## Purpose

This case tests whether representation comparison incorrectly rejects a preserved mechanism.

---

# Case 3: Small Parameter Change, Mechanism Change

Construct models where:

\[
\|W_A-W_B\|
\]

is small, but a causally important computation changes.

The transformation should produce a small parameter difference while changing the relevant counterfactual response.

## Required property

Parameter similarity is high, but causal mechanism equivalence fails.

## Purpose

This tests whether parameter distance can be used as a proxy for mechanism preservation.

Expected result:

\[
\text{small weight change}
\not\Rightarrow
\text{mechanism preservation}
\]

---

# Case 4: Large Parameter Change, Mechanism Preservation

Construct models where:

\[
\|W_A-W_B\|
\]

is large while the same causal computation is preserved under a coordinate transformation or equivalent reparameterization.

## Required property

Parameter similarity is low, but causal mechanism equivalence holds.

## Purpose

This tests whether large parameter changes are incorrectly interpreted as mechanism destruction.

Expected result:

\[
\text{large weight change}
\not\Rightarrow
\text{mechanism change}
\]

---

# Case 5: Same Benchmark Outputs, Different Counterfactuals

Construct models that agree on the evaluation dataset:

\[
M_A(x)=M_B(x)
\]

for all tested \(x\), but differ under interventions.

For an intervention \(I\):

\[
K_{M_A}(I,x)
\neq
K_{M_B}(I,x)
\]

## Purpose

This demonstrates that ordinary evaluation behavior does not identify counterfactual causal structure.

---

# Case 6: Representation Similarity Despite Mechanism Change

Construct models whose internal representations remain highly similar according to a chosen representation metric while a causally important computation has changed.

## Required property

\[
M_A \approx_R M_B
\]

but:

\[
M_A \not\approx_C M_B
\]

## Purpose

This tests whether high representation similarity is sufficient evidence for mechanism preservation.

Expected result:

\[
\text{representation similarity}
\not\Rightarrow
\text{causal mechanism equivalence}
\]

---

# Case 7: Intervention Coordinate Mismatch

Construct two models implementing the same mechanism under different internal coordinates.

A literal intervention:

\[
I
\]

on model \(M_A\) should not necessarily correspond to the identical literal intervention on \(M_B\).

Instead:

\[
\omega(I) \neq I
\]

may be required.

## Purpose

This case tests the necessity of an explicit intervention correspondence.

A method that assumes:

\[
\omega(I)=I
\]

without justification may falsely conclude that an equivalent mechanism has changed.

---

# Case 8: Intervention Basis Failure

Construct a mechanism for which one intervention basis produces little or no information about the mechanism difference, while another basis reveals the difference.

## Purpose

This tests whether fixed intervention bases are sufficient.

It motivates the investigation of intervention selection as a research problem.

---

# Required Benchmark Matrix

Every future method should eventually be evaluated against the following conceptual matrix:

| Case | Behavior | Representation | Causal Mechanism | Expected Detection |
|------|-----------|-----------------|------------------|--------------------|
| 1 | Same | Possibly similar | Different | Detect difference |
| 2 | Same | Different | Same | Detect preservation |
| 3 | Same/close | Similar | Different | Detect difference |
| 4 | Same | Different | Same | Detect preservation |
| 5 | Same | Similar | Different | Detect difference |
| 6 | Same | Similar | Different | Detect difference |
| 7 | Same | Different | Same | Handle intervention translation |
| 8 | Same | Variable | Variable | Select informative intervention |

---

# Scientific Requirement

A method must not be considered successful merely because it performs well on ordinary transformed models.

It must survive deliberately constructed cases where:

1. behavior is misleading,
2. representation is misleading,
3. parameter distance is misleading,
4. fixed interventions are uninformative,
5. intervention coordinates change.

The benchmark must therefore contain known ground truth about the causal mechanism.

---

# Open Questions

The following questions remain unresolved:

1. What mathematical object constitutes the "mechanism" in the benchmark?
2. What transformations count as equivalent reparameterizations?
3. What intervention family is sufficient to distinguish the constructed mechanisms?
4. How should intervention correspondence \(\omega\) be defined?
5. What response space should \(K_M(I,x)\) inhabit?
6. What tolerance \(\epsilon\) is scientifically meaningful?
7. When can finite interventions identify mechanism preservation?
8. What assumptions are necessary for identification?
9. Can the intervention selector provide information beyond generic active experiment design?
10. What are the exact failure boundaries of the proposed equivalence notion?