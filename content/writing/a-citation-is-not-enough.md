A transcript contains the sentence “I have been waking up with the baby every night.” An assistant includes a citation and writes a personal update about the recipient's experience as a new parent.

The sentence exists. The citation resolves. The update can still be wrong.

Perhaps a colleague was speaking. Perhaps the recipient was quoting a customer. Perhaps a product team was role-playing a fictional user. A retrieval system can return exactly the right passage while the writing system assigns it the wrong status.

The example is synthetic. It illustrates why I treat source support, ownership, and autobiographical eligibility as separate questions.

## Four checks hidden inside “grounded”

First ask whether the words or proposition are supported by the source. Then ask who spoke. Then ask whose experience the statement describes. Finally ask what kind of statement it was: report, quotation, role-play, hypothesis, or something unresolved.

These questions can disagree without any component being broken. A speaker can accurately quote somebody else's experience. A correctly attributed utterance can describe an imaginary person.

| Source | What is supported | What is not yet supported |
| --- | --- | --- |
| “My customer said, ‘I wake up with the baby.’” | A report about a customer's statement | The speaker has a baby |
| “Imagine I am a new parent…” | A role-play setup | A fact about the speaker's family |
| “I woke up with my baby last night.” | A direct self-report, subject to context | A permanent pattern of sleep deprivation |

The final row also shows a scope problem. Correct ownership does not justify widening one night's report into a durable characterization.

## Keep the proposed claim next to the evidence

Instead of checking whether a paragraph has any citation, inspect the specific claim the output makes. “You are a new parent” is a different claim from “you discussed the experience of new parents.”

A minimal review worksheet can include the proposed statement, its supporting passage, the person it concerns, and unresolved qualifications. This is an explanatory aid, not a proposed mandatory schema or a claim that structured fields solve interpretation.

The critical question is whether the source supports this statement about this person at this level of certainty.

A reviewer should see enough surrounding context to notice a role-play introduction. Cropping to the apparently supportive sentence may make the wrong claim seem inevitable. Conversely, adding an entire archive may bury the decisive sentence. Context selection itself needs inspection.

## Test meaning changes, not only names

A useful small evaluation keeps most of the wording identical while changing the context:

- Direct self-report becomes quotation.
- Quotation becomes role-play.
- A hypothetical sentence becomes an explicit correction.
- The speaker remains the same while the subject changes.

Then examine whether the output changes accordingly. A system that only verifies the speaker label may pass identity checks and still fail all the role-play cases.

Include positive examples too. A system that refuses to write any personal fact avoids some mistakes by becoming useless. The test should reveal both false attribution and unnecessary omission.

## The source can also be wrong

Sometimes a structured transcript labels the wrong speaker. A downstream validator can preserve that label perfectly and still contradict reality.

That is a different failure from ignoring a correct label. It calls for a source-correction process or a visible unresolved state, not more confident inference from the same mistaken input.

A debugging report should distinguish these cases. Otherwise, improvements in source alignment can be mistaken for improvements in language understanding, or vice versa.

This is one reason I would not collapse all “grounding” failures into one score. Unsupported wording, wrong ownership, mistaken speech context, and bad source data imply different repairs.

## An accurate citation is the beginning

[Provenance standards such as PROV](https://www.w3.org/TR/prov-overview/) help describe derivation and attribution. They do not, by themselves, decide whether a role-play utterance is an autobiographical fact. That remains a semantic judgment requiring appropriate evidence and evaluation.

For personal AI, the cost of getting this wrong extends beyond one awkward paragraph. If the generated claim becomes a memory, a temporary attribution error can influence later recommendations and messages.

The practical standard is simple to state, even when hard to meet: a claim should be supported, belong to the right person, and preserve the kind of statement the person actually made.
