# Scope of this research companion

## Intended use

This repository communicates a research direction and demonstrates a small piece of result bookkeeping. The code was written specifically for this public companion. It is not extracted from the research system.

The environment loop asks whether a candidate capability is supported well enough to retain. The learning loop asks whether a particular training use has separate supporting evidence. These decisions need not agree.

## What the example means

`capability_checks_passed` and `learning_evidence_supports_use` are fictional, externally supplied decisions. The example does not define or implement the checks that produce them. Missing evidence stays pending. A claim of training use without capability admission is rejected as an inconsistent record.

The example intentionally omits the verifier, candidate proposal process, diagnostic rules, training policy, scoring machinery and deployment integration. It cannot establish correctness, generalization or improved grading.

## Experimental reporting principles

- Preserve negative results and unresolved cases.
- Keep synthetic development results distinct from real-world evaluation.
- Distinguish model-generated labels from independently reviewed ground truth.
- Repeated evaluation of the same items does not create independent new test items.
- Separate a proposed method from measured outcomes.

These principles describe the reporting boundary, not a claim that all planned research gates have been completed. Detailed protocols and experimental records are outside this release.
