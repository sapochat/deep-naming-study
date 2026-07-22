# Deep Naming Study

A research-led naming workflow for the point where ordinary brainstorming reaches “I like it, but I don’t love it.”

More names do not help when the generative theory is wrong. Recover the source mechanism, generate from genuinely different theories, criticize blindly, check collisions late, and test finalists in real editorial use.

## Protocol

1. Detect the exhausted synonym loop.
2. Write one shared brief and explicit rubric.
3. Research the source language or institutional history.
4. Diverge by theory—not model count.
5. Preserve independent artifacts.
6. Merge candidates without voting.
7. Run blind hostile criticism.
8. Use disagreement diagnostically.
9. Check collisions and domains only for taste-qualified survivors.
10. Simulate finalists over issue titles, descriptors, a masthead, and spoken use.

## Run

```bash
PYTHONPATH=src python3 -m deep_naming_study.cli init examples/publication-brief.json /tmp/naming-study
PYTHONPATH=src python3 -m deep_naming_study.cli check /tmp/naming-study
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

MIT licensed.
