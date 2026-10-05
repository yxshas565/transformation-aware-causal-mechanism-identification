# TACMI Toy Mechanism: Two Bit XOR

## 1. Purpose

The first TACMI benchmark uses a deterministic binary computation whose causal mechanism is completely known.

The benchmark is intentionally small.

The purpose is not to demonstrate performance on a realistic neural network.

The purpose is to establish whether the proposed causal mechanism equivalence framework can distinguish:

1. behavioral equivalence,
2. representational equivalence,
3. causal mechanism equivalence.

---

## 2. Input Space

The input consists of two binary variables:

\[
x_1, x_2 \in \{0,1\}
\]

Therefore:

\[
\mathcal{X} =
\{(0,0),(0,1),(1,0),(1,1)\}
\]

---

## 3. Target Function

The target output is:

\[
y = x_1 \oplus x_2
\]

The complete truth table is:

| \(x_1\) | \(x_2\) | \(y\) |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

---

## 4. Ground Truth Mechanism A

The first mechanism computes XOR through the two intermediate conjunctions:

\[
z_1 = x_1(1-x_2)
\]

\[
z_2 = (1-x_1)x_2
\]

The output is:

\[
y = z_1 + z_2
\]

Therefore:

\[
y =
x_1(1-x_2)
+
(1-x_1)x_2
\]

which is equivalent to:

\[
x_1 \oplus x_2
\]

### Causal structure

```text
x1 ─────┬──────────────► z1 ─────┐
        │                         │
x2 ─────┴──────────────► z1       │
                                  ├──► y
x1 ─────┬──────────────► z2       │
        │                         │
x2 ─────┴──────────────► z2 ──────┘

The important causal variables are:

$$ z_1,\ z_2 $$

because each captures one of the two mutually exclusive cases in which XOR is true.

5. Mechanism B: Alternative Internal Representation

Mechanism B should compute the same XOR function while using a different internal representation.

For example, define:

$$ u_1 = z_1 + z_2 $$

and:

$$ u_2 = z_1 - z_2 $$

The pair:

$$ (u_1,u_2) $$

is an invertible linear transformation of:

$$ (z_1,z_2) $$

because:

$$ z_1 = \frac{u_1+u_2}{2} $$ $$ z_2 = \frac{u_1-u_2}{2} $$

The output remains:

$$ y = u_1 $$

Thus Mechanism B is intended to represent the same underlying computation under a changed internal coordinate system.

This case will test whether TACMI can distinguish:

different representation

from:

different causal mechanism.

6. Mechanism C: Behaviorally Equivalent Alternative

Mechanism C should produce the same observable XOR outputs while using a structurally different internal computation.

One candidate formulation is:

$$ s = x_1 + x_2 $$ $$ p = x_1x_2 $$

followed by:

$$ y = s - 2p $$

For binary inputs:

$$ s - 2p = x_1 \oplus x_2 $$

Therefore:

$$ y_C(x)=y_A(x) $$

for every input in the domain.

However, the intermediate variables and causal pathways differ from Mechanism A.

This creates the central adversarial pair:

$$ M_A \approx_B M_C $$

while the benchmark should investigate whether:

$$ M_A \not\approx_C M_C $$

under an appropriate intervention family.

7. Mechanism D: Behavior and Mechanism Change

Mechanism D represents a case where both the internal computation and observable behavior differ.

For example:

$$ y_D = x_1 $$

This is intentionally simple.

For some inputs:

$$ y_D(x) \neq x_1 \oplus x_2 $$

Therefore:

$$ M_A \not\approx_B M_D $$

and the causal mechanism is also different.

This provides an easy negative control.

8. Ground Truth Labels

The initial benchmark therefore contains:

Pair	Behavior	Representation	Mechanism
A vs A	Same	Same	Same
A vs B	Same	Different	Intended same
A vs C	Same	Different	Intended different
A vs D	Different	Different	Different

These labels are benchmark ground truth hypotheses derived from the explicit computational construction.

The A vs C distinction is the critical adversarial test.

9. Intervention Space

Initial interventions will target internal variables.

For a model \(M\), define an intervention:

$$ do(v \leftarrow c) $$

where:

\(v\) is an internal variable,
\(c\) is an allowed replacement value.

The first intervention family will use:

$$ c \in \{0,1\} $$

for binary internal variables.

The experiment will record:

$$ K_M(do(v\leftarrow c),x) $$

as the resulting observable output.

10. Causal Response

For each input:

$$ x \in \mathcal{X} $$

and intervention:

$$ I = do(v\leftarrow c) $$

the benchmark records:

$$ K_M(I,x) $$

The complete collection of responses forms the causal response matrix:

$$ R_M = \left[ K_M(I_i,x_j) \right]_{i,j} $$

Two mechanisms can then be compared through their intervention response matrices.

11. Important Limitation

The A vs C construction is not yet sufficient to establish that the two computations are fundamentally causally different under every possible intervention definition.

The benchmark must therefore treat this as a research construction requiring validation.

In particular, we must determine:

which variables count as corresponding causal variables,
which interventions are admissible,
whether intervention correspondence exists,
whether a transformation can map one mechanism into the other,
whether the distinction survives a richer intervention family.

The benchmark must not assume its own conclusion.

12. Experimental Objective

The first executable experiment should determine whether a causal intervention system can correctly recover the known distinctions:

Positive control
$$ A \rightarrow A $$

should be classified as mechanism preserved.

Representation transformation
$$ A \rightarrow B $$

should be classified as mechanism preserved despite representation change.

Adversarial behaviorally equivalent pair
$$ A \rightarrow C $$

should be investigated as a potential mechanism change despite identical observable behavior.

Negative control
$$ A \rightarrow D $$

should be classified as mechanism changed.

13. Research Principle

The benchmark must not be designed so that the mechanism label can be recovered simply by reading the implementation.

The eventual causal identification procedure should receive only the permitted model access and intervention responses.

Ground truth is used for evaluation, not supplied to the identification algorithm.


### Important correction before we code

I deliberately wrote **"intended same"** and **"intended different"** rather than pretending we've already proved those labels.

That distinction is crucial.

In fact, **A vs C is exactly where we need to be careful**. If there exists a valid intervention correspondence that makes their causal response structures equivalent, then C isn't actually a different mechanism under our formal definition. That's not a failure of the experiment. That's a scientific result that tells us our mechanism definition needs refinement.