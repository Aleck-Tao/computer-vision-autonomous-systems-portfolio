# Comparing mission parsers

The current front end is a rule-based adapter for constrained mission text. It provides a fixed contract against which a learned parser could be compared.

A useful comparison would keep the downstream policy unchanged and vary only the parser. Requests should include explicit constraints, omitted constraints, negation and conflicts. For each request, a separately specified expected contract would distinguish a parsing error from a policy rejection.

Three outcomes should be counted separately:

- a correct contract that passes the configured policy;
- a correct interpretation of an unsafe request that is blocked;
- an incorrect interpretation, including one that happens to pass the policy.

The third case matters because policy acceptance can otherwise be mistaken for language understanding. For example, keyword detection of “low LiDAR confidence” does not by itself establish whether the instruction asks to stop or asks not to stop.

Adding visual observations introduces another question: did the parser ground the target in the current scene? That requires paired observations and target annotations. The current mission examples exercise text-to-contract handling; the field-video audit measures image quality. Combining them into a grounding experiment would require an explicit correspondence between instruction, observation and expected target.
