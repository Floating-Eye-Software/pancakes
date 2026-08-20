# Plan 0014 — Pancakes Relationships Cleanup

## Document information

**Plan ID:** 0014  
**Status:** Proposed  
**Primary repository:** Pancakes  
**Related repositories:** Pitchfork, Sinead, Honk  
**Scope:** Conceptual documentation alignment  
**Depends upon:** Pancakes Relational Model draft

---

# 1. Purpose

The Pancakes Relational Model introduces a canonical vocabulary for:

* operative context,
* relevant and represented context,
* relation,
* interaction and transformation,
* historical carryover,
* relationship,
* agentic relationship,
* relational configuration,
* reality, recognition, and representation,
* and place as a materially situated relational configuration.

This vocabulary corrects several older formulations distributed across Pancakes, Pitchfork, and Sinead.

The cleanup must integrate the relational model, revise the two existing Pancakes place documents, reconcile Pitchfork's symbolic frequency and transformation language, and audit downstream documents for terminology that has become ambiguous or overly broad.

The cleanup should preserve the useful substance of the existing documents. It should not create a new relationship-tracking subsystem, relational database, universal graph, or symbolic-memory object.

---

# 2. Current state

The following work is complete in draft form:

* `pancakes-relational-model.md` has been written as a new foundational article.
* The article distinguishes operative context from context selected for an inquiry or representation.
* It defines a relation as a specified consequential connection.
* It defines historical carryover as prior interaction altering present conditions in a way that remains consequential.
* It defines a relationship as a path-dependent relation whose prior course helps govern its future course.
* It distinguishes bidirectional consequence from reciprocal agency.
* It defines place as a materially situated relational configuration rather than a relationship.
* It distinguishes reality, recognition, and representation.
* It maps the theory to Pitchfork without making acquired frequencies or provenance exhaustive accounts of history.

The draft still needs to be added to the Pancakes repository, linked from the documentation, and reconciled with the documents that currently use incompatible language.

---

# 3. Decisions carried by this plan

Unless review identifies a concrete problem, the cleanup should preserve the following decisions.

## 3.1 One foundational relational article

Pancakes should have one canonical relational article:

```text
docs/pancakes-relational-model.md
```

Do not split context, relation, historical carryover, relationship, and relational configuration into separate foundational documents during this cleanup.

## 3.2 Relationship is path-dependent relation

Use the following canonical distinction:

```text
relation
→ consequential connection

relationship
→ relation whose prior course helps govern its future course

agentic relationship
→ relationship in which multiple parties can independently
  interpret, initiate, answer, refuse, or contest
```

Duration and repetition may deepen a relationship but are not sufficient or necessary by themselves.

## 3.3 Historical carryover is changed present conditions

Historical carryover should not be defined as a stored trace-object.

Material traces, records, habits, expectations, legal states, skills, ecological states, precedents, and institutional procedures may carry historical consequences. The more general claim is that the present is organized differently because prior interaction occurred.

## 3.4 Place is a relational configuration

Use the following bridge definition:

> **A place is a materially situated configuration of overlapping relations that conditions participation within a locality.**

A person or institution may have a relationship with a place. That relationship is not the whole place.

Continuity and accumulated history are possible features of a place, not requirements for something to be a place.

## 3.5 Reality precedes representation

Nodes and information systems recognize, record, display, or interpret selected relations.

They do not decide which recognition-independent material, ecological, or infrastructural relations exist.

Recognition may reveal an existing relation, alter a relation, or help constitute a new social or institutional relation. These operations must remain distinguishable.

## 3.6 Symbolic systems represent selected historical meaning

Pitchfork frequencies, spectra, provenance, lineage, and terroir may represent symbolically consequential historical carryover.

They are not the complete ontology of a relation, entity, transformation, or place.

## 3.7 Do not create responsibility directly from relation

Relational involvement identifies where responsibility questions arise.

Responsibility still depends upon such grounds as contribution, control, capability, role, commitment, benefit, dependence, reciprocity, vulnerability, repair, and justice.

---

# 4. Terminology decisions to confirm early

Two decisions should be confirmed before broad edits begin.

## 4.1 Replacement for `relationship-bound institution`

The current Place and Institutions document contrasts `place-bound` with `relationship-bound` institutions.

This becomes ambiguous once relationship has a technical path-dependent meaning. Nearly every mature institution contains relationships.

Preferred replacement:

> **affiliation-bound institution**

An affiliation-bound institution exists because participants associate through a purpose, practice, identity, commitment, membership, or agreement rather than because they share unavoidable exposure to one locality or infrastructure.

Alternative if review finds `affiliation` inadequate:

> **association-bound institution**

Tasks:

* [ ] Confirm `affiliation-bound` or select a better term before editing Pancakes and Sinead.
* [ ] Define the selected term once in the revised Place and Institutions document.
* [ ] Use the same term in Sinead's place and institutional foundations.
* [ ] Avoid mechanical replacement where `relationship-bound` is being used in a different sense.

## 4.2 Canonical scope of terroir

Preferred definition:

> **Terroir is the characteristic way a place's present material, ecological, practical, and historically acquired conditions participate in and differentiate transformations.**

This distinguishes terroir from the complete place spectrum or everything that has happened in a place.

Tasks:

* [ ] Locate all existing terroir discussion, including current work notes such as `_work/notes/pitchfork-spectral-design-iteration.md`.
* [ ] Confirm whether terroir names the place's characteristic contribution to transformation, the place's acquired spectrum, or both.
* [ ] Prefer the narrower transformation-facing definition unless existing design work supplies a stronger reason otherwise.
* [ ] Establish one canonical home for the definition, preferably `pitchfork-symbolic-frequencies.md`.
* [ ] Make crafting and downstream RPG documents reference rather than redefine it.

---

# 5. Workstream A — Integrate the Pancakes Relational Model

## 5.1 Add the canonical document

* [ ] Add the completed draft as `docs/pancakes-relational-model.md`.
* [ ] Review the title, status, layer, companion-document list, and repository-relative links.
* [ ] Add Markdown navigation links to the Place Model and other companion documents where their final paths are known.
* [ ] Ensure the relational article remains the canonical source for `context`, `relation`, `historical carryover`, `relationship`, and `relational configuration`.
* [ ] Ensure the Place Model remains the canonical source for the detailed meaning of place.
* [ ] Ensure the Pitchfork frequency and crafting documents remain canonical for their own symbolic operations.

## 5.2 Register the document in public navigation

Audit and update as appropriate:

* [ ] `docs/README.md`
* [ ] `README.md`
* [ ] `docs/pancakes-primer.md`
* [ ] `docs/pancakes-ecosystem-overview.md`
* [ ] `docs/pancakes-ecosystem-layers.md`
* [ ] any conceptual-foundations or institutional-engineering navigation lists

Do not force the article into every overview. Add it where readers need the canonical vocabulary before encountering place, institutions, stewardship, meaning, or Pitchfork semantics.

## 5.3 Register this plan

Follow repository planning conventions.

* [ ] Add Plan 0014 to `_work/plans/plans.csv`.
* [ ] Update `_work/current-work-fronts.md` if this cleanup becomes an active work front.
* [ ] Update `_work/todo.csv` or `_work/todo.md` only where repository workflow requires a corresponding task entry.
* [ ] Do not duplicate plan status manually in files generated from another source.

## 5.4 Update context packaging

* [ ] Add `docs/pancakes-relational-model.md` to the appropriate Pancakes context composite configuration.
* [ ] Rebuild the composite using `scripts/assemble_context_composites.py` or the current documented workflow.
* [ ] Regenerate source inventory through its owning process rather than manually editing generated output.
* [ ] Confirm that future Pancakes, Pitchfork, Sinead, and Honk conversations receive the new canonical definitions where relevant.

---

# 6. Workstream B — Rewrite `pancakes-place-model.md`

The Place Model should become the place-specific application of the relational model.

## 6.1 Replace the canonical definition

Current language to remove:

> A place is a meaningful relationship rather than merely a coordinate.

> Places are relationships.

Replace with a definition grounded in materially situated relational configuration.

The revised definition should establish that:

* a coordinate locates;
* a place organizes overlapping material, ecological, infrastructural, social, institutional, and interpretive relations within a locality;
* a place can exist before any one participant understands it completely;
* participants may develop relationships with a place;
* no one participant's relationship or interpretation exhausts the place;
* and temporary places are possible.

Tasks:

* [ ] Rewrite the purpose and canonical-definition sections.
* [ ] Add a direct companion reference to the Pancakes Relational Model.
* [ ] Distinguish `place`, `location`, `place relation`, `relationship with place`, and `represented place context`.
* [ ] Preserve the principle that nodes and institutions do not own places.

## 6.2 Correct the reality-recognition boundary

Current language to remove or qualify:

> The node decides which relationships matter.

The revised text should say that a node decides which relations it recognizes, records, displays, or uses within its authority and permissions.

Tasks:

* [ ] Distinguish operative place relations from recorded node relationships.
* [ ] Explain that a relation may remain materially consequential when unrecorded or removed from the node.
* [ ] Preserve explicit, reviewable, locally governed, removable, and privacy-preserving requirements for node records.
* [ ] Clarify that removability applies to the representation where the underlying external relation cannot be removed.
* [ ] Preserve the boil-water example as an illustration of local interpretation without centralized household disclosure.

## 6.3 Separate history, carryover, memory, meaning, and responsibility

Current language to revise:

> Place therefore possesses symbolic memory.

The revised model should distinguish:

* events that occurred in a place;
* present material or ecological conditions altered by those events;
* historical carryover;
* records and community histories;
* personal and institutional memories;
* symbolic representations of history;
* attributed and contested meanings;
* and responsibilities grounded through a further normative analysis.

Tasks:

* [ ] Rename or rewrite the `Place Memory` section.
* [ ] Use `place history`, `historical carryover`, `recorded memory`, or `symbolic place history` where each is actually intended.
* [ ] State that not every event occurring at a location changes the place's later identity.
* [ ] State that repeated use does not automatically create shared meaning.
* [ ] State that causal involvement does not automatically create responsibility.
* [ ] Preserve the possibility that history remains consequential even when nobody remembers it.
* [ ] Preserve plural and contested interpretations of place.

## 6.4 Reconcile homelands

The homeland concept remains useful.

Tasks:

* [ ] Define homeland as a durable and recognized relationship between a node or community and one or more places.
* [ ] Explain what makes the relation path-dependent: belonging, familiarity, responsibility, recurring practice, or ongoing participation.
* [ ] Preserve optionality and support for mobile, travelling, privacy-sensitive, and virtual services.
* [ ] Preserve the rule that homeland does not imply live tracking, ownership, or exhaustive address disclosure.

## 6.5 Reconcile layers of place

The ecological, geological, civic, historical, cultural, and Indigenous-context sections remain valuable.

Tasks:

* [ ] Describe them as overlapping conditions, relations, interpretations, boundaries, and histories rather than automatically as identities possessed by a place.
* [ ] Preserve ecological and infrastructural relations that operate independently of node recognition.
* [ ] Preserve the Indigenous-context safeguards against appropriation, game conversion, ownership claims, and unauthorized interpretation.
* [ ] Do not imply that public reference services settle cultural authority or contested history.

## 6.6 Reconcile stewardship

* [ ] Preserve stewardship as care without ownership.
* [ ] Cross-reference the responsibility analysis in the Relational, Stewardship, and Power and Responsibility models.
* [ ] Avoid implying that any relation to a place automatically authorizes care, intervention, representation, or governance.
* [ ] Preserve restoration, maintenance, accessibility, mutual aid, and habitat-monitoring examples with appropriate authority and consent boundaries.

## 6.7 Reconcile place, transformation, spectrum, and terroir

The revised Place Model should explain the conceptual relationship but should not define Pitchfork crafting operations.

Tasks:

* [ ] Distinguish a place conditioning a transformation from a transformation altering a place.
* [ ] Explain that the same event may do both.
* [ ] Replace the current one-way `Place → Transformation → Symbolic spectrum → Place memory` diagram with a feedback model that distinguishes reality, recorded transformation, symbolic representation, and later place conditions.
* [ ] Refer to acquired place frequencies, place spectra, provenance, and terroir without making them exhaustive accounts of the place.
* [ ] Preserve the rule that no projection owns the meaning of a place.

## 6.8 Rewrite design principles and downstream references

* [ ] Replace `Places are relationships` with `Places are relational configurations` or equivalent language.
* [ ] Preserve `Stewardship matters more than ownership` with the appropriate authority qualification.
* [ ] Preserve privacy and separation of public knowledge from private interpretation.
* [ ] Update the `What Later Documents Should Reference` section to include the Relational Model.
* [ ] Ensure later documents reference the Place Model for detailed place semantics and the Relational Model for general relation semantics.

---

# 7. Workstream C — Revise `pancakes-place-and-institutions.md`

This document requires conceptual revision rather than a simple cross-reference patch.

## 7.1 Reframe place as situated rather than necessarily stable

Current subtitle:

> Place as the Stable Substrate of Institutional Life

Preferred direction:

> Place as the Situated Substrate of Institutional Life

Tasks:

* [ ] Rewrite the subtitle and abstract.
* [ ] Replace unconditional `Places provide continuity` claims with the more precise claim that durable places can provide continuity while place-bound coordination arises from shared situated conditions and exposure.
* [ ] Add temporary places and temporary place-bound coordination where useful.
* [ ] Preserve the important distinction between organizational continuity and the continuity of the people, capabilities, infrastructures, ecologies, commitments, and places an institution serves.

## 7.2 Replace the place-bound/relationship-bound contrast

After the terminology decision in Section 4:

* [ ] Rename the `Relationship-Bound Institutions` section.
* [ ] Replace the term consistently in the abstract, spectrum table, examples, case studies, participation discussion, and closing sections.
* [ ] Define the new term through affiliation, purpose, practice, identity, commitment, membership, or agreement.
* [ ] Preserve the observation that formal voluntariness does not eliminate dependency, power, or exit costs.
* [ ] Preserve hybrid and polycentric institutions.

## 7.3 Rework `Places Outlive Institutions`

The existing section contains a valuable continuity argument but overstates its universality.

Tasks:

* [ ] Retitle if necessary to indicate that places may outlast particular institutions.
* [ ] Remove the inherited claim that place is a meaningful relationship.
* [ ] Separate place history, historical carryover, public memory, obligations, and meaning.
* [ ] Explain that some places are transformed, dissolved, displaced, or created through institutional action.
* [ ] Preserve the principle that organizational survival is not the same as preserving the people, place, capabilities, or obligations an institution exists to serve.

## 7.4 Preserve the institutional-engineering substance

The following arguments remain strong and should be retained:

* [ ] coordination problems may follow territory, ecology, infrastructure, mobility, service use, or affiliation;
* [ ] participation may follow exposure even without consent;
* [ ] administrative boundaries imperfectly follow problems;
* [ ] several institutions may overlap one place;
* [ ] place does not grant unlimited authority;
* [ ] capability and stewardship bound legitimate scope;
* [ ] high exit costs increase the need for voice, accountability, due process, and appeal;
* [ ] federation should operate at the scale of the problem without absorbing unnecessary local authority.

## 7.5 Review the case studies

* [ ] Update terminology in the Brexit case without changing its neutral architectural purpose.
* [ ] Update terminology in the Toronto school-board case.
* [ ] Confirm that each case distinguishes place, territory, jurisdiction, institution, affiliation, and individual relationship correctly.
* [ ] Preserve existing source citations and verify that links remain live during final documentation review.

## 7.6 Revise the conclusion

Current language includes:

> Preserve places.

This should not become an unconditional requirement to freeze every current spatial or institutional arrangement.

Tasks:

* [ ] Reframe preservation around the people, capabilities, ecologies, histories, commitments, rights, and stewardship relations that require continuity.
* [ ] Preserve the principle that institutions may evolve without treating the places and participants they serve as disposable.
* [ ] Preserve bounded federation and authority proportional to stewardship and exit cost.
* [ ] Remove any closing statement that treats place as a single relationship.

---

# 8. Workstream D — Reconcile Pitchfork symbolic semantics

The relational model should clarify existing Pitchfork semantics rather than create a new subsystem.

## 8.1 Revise `pitchfork-symbolic-frequencies.md`

### Add relational grounding

* [ ] Add the Pancakes Relational Model as a conceptual dependency or companion.
* [ ] State that frequencies and spectra represent selected symbolic meaning.
* [ ] State that a spectrum does not establish every material, legal, ecological, institutional, or experiential fact about its subject.
* [ ] State that representation of a relation does not by itself prove that the relation exists as represented.

### Revise place-frequency language

Current language:

> Place frequencies arise from meaningful relationships with places.

Tasks:

* [ ] Allow place frequencies to arise when a place participates in the context, lineage, or interpretation of a transformation, including first encounters that are not yet relationships.
* [ ] Preserve place frequencies such as wetland, watershed, neighbourhood, trail, library, and market.

### Tighten intrinsic and acquired frequencies

Current language:

> Acquired frequencies describe what has happened.

Tasks:

* [ ] Clarify that acquired frequencies represent symbolically consequential aspects of prior transformations preserved in present symbolic state.
* [ ] Clarify that they do not record everything that happened.
* [ ] Review `intrinsic frequency` so that it describes current identity within Pitchfork semantics rather than a claim of timeless or observer-independent essence.
* [ ] Preserve the distinction between material identity and acquired symbolic history.

### Reconcile provenance

* [ ] Preserve provenance as the source and lineage of recorded results.
* [ ] Clarify that acquired frequencies are symbolic expressions of selected provenance, not provenance in its entirety.
* [ ] Preserve privacy-preserving omission, attenuation, and filtering.
* [ ] State that omission from a record or projection does not imply that no underlying history exists.

### Reconcile place spectra and memory language

Current language includes:

> A woodland trail accumulates memory.

Tasks:

* [ ] Replace literal or unqualified memory language with place history, historical carryover, recorded memory, acquired frequencies, or symbolic place history as appropriate.
* [ ] Say that Pitchfork may represent a place with a symbolic spectrum rather than implying that a spectrum exhausts what the place possesses.
* [ ] State that not every event at a location changes its place spectrum.

### Define terroir

* [ ] Add the confirmed canonical definition of terroir.
* [ ] Distinguish terroir from place reference, place spectrum, acquired place frequencies, and the complete history of a place.
* [ ] Include at least one example showing how two materially similar transformations differ because of place conditions and accumulated practice.

## 8.2 Revise `pitchfork-symbolic-crafting.md`

### Replace memory anthropomorphism

Current language:

> Symbolic crafting is transformation with memory.

> A crafted object remembers enough history to preserve meaningful continuity.

Tasks:

* [ ] Replace the canonical definition with language such as `Symbolic crafting preserves historical carryover through symbolic transformation`.
* [ ] Retain `transformation with memory` only as clearly identified shorthand if it remains useful.
* [ ] Replace object memory with lineage preserving historically relevant information.

### Clarify symbolic conservation

* [ ] Review `Symbolic meaning is conserved unless intentionally transformed`.
* [ ] Clarify that conservation is a Pitchfork accounting and lineage policy, not a metaphysical law that fixes meaning for every interpreter.
* [ ] Preserve refinement, amplification, attenuation, mixing, filtering, conversion, purification, and corruption as symbolic operations.
* [ ] Audit uses of `relationship` inside those operations so that symbolic association, intended configuration, and path-dependent relationship are not conflated.

### Clarify transformation boundaries

* [ ] Distinguish changes in reality from updates to recorded symbolic state.
* [ ] Clarify when a completed service or activity creates or updates a spectrum.
* [ ] Avoid claiming that every physical event automatically produces a canonical symbolic interpretation.
* [ ] Preserve canonical event and settlement boundaries defined elsewhere in Pitchfork.

### Clarify place feedback

* [ ] Distinguish place conditioning a transformation from transformation altering a place.
* [ ] Explain that the same transformation may do both.
* [ ] Require consequential carryover and appropriate representation before updating acquired place meaning.
* [ ] Replace `a commons accumulates ... memory` with precise language.
* [ ] Connect the place-conditioning direction to terroir.

### Preserve privacy and selective lineage

* [ ] Preserve community ancestry without unnecessary personal disclosure.
* [ ] Explain that filtering a public representation does not retroactively erase the underlying event or every private record of it.
* [ ] Preserve intentional forgetting as a governed transformation where deletion, attenuation, or privacy policy actually requires it.

## 8.3 Revise `pitchfork-symbolic-projections.md`

Current language includes:

> Transformations are canonical.

> The transformation is canonical.

Tasks:

* [ ] Clarify that the settled transformation record is canonical within Pitchfork's symbolic architecture.
* [ ] Do not equate the canonical record with reality in its entirety.
* [ ] Preserve the distinction among transformation record, symbolic spectrum, projection, and client experience.
* [ ] Clarify that projections do not rewrite the underlying settled record merely by interpreting it.
* [ ] Clarify that encountering a projection may influence people and thereby produce a new interaction or transformation.
* [ ] Review `Projections do not create symbolic meaning` so it does not deny the possibility that interpretation contributes to later meaning.
* [ ] Preserve `No projection owns meaning` and purpose-specific plurality.

## 8.4 Do not add a duplicate subsystem

* [ ] Do not create a universal `relationship_memory` object.
* [ ] Do not add a new relationship frequency family merely to mirror the relational theory.
* [ ] Do not retroactively tag every event, object, service, person, or place with relational metadata.
* [ ] Do not force contracts, capabilities, records, provenance, lineage, and symbolic spectra into one generalized history field.
* [ ] Use existing Pitchfork mechanisms according to their distinct responsibilities.

---

# 9. Workstream E — Align Sinead

Sinead currently repeats terminology that will conflict with the relational model.

## 9.1 `place-foundations.md`

Current language includes:

> A place accumulates relationships, memory, responsibility, use, and meaning.

> Place-bound and relationship-bound institutions

Tasks:

* [ ] Adopt place as a materially situated relational configuration.
* [ ] Separate physical and ecological history, historical carryover, recorded memory, meaning, and responsibility.
* [ ] Replace `relationship-bound` with the selected affiliation term.
* [ ] Preserve boundary plurality, infrastructure/ecology coupling, observation, uncertainty, and external-system context.
* [ ] Ensure diagrams can distinguish operative relation, recognized relation, recorded claim, and institutional jurisdiction where relevant.

## 9.2 `governance-foundations.md`

* [ ] Replace or qualify `relationship-bound` terminology.
* [ ] Preserve the claim that continued presence does not prove consent, satisfaction, or legitimacy.
* [ ] Align participation states with the distinction between relation, relationship, and agentic relationship.

## 9.3 `institutional-engineering-foundations.md`

* [ ] Replace the place-bound/relationship-bound contrast with place-bound/affiliation-bound or the confirmed terminology.
* [ ] Preserve the institution definition as a persistent system of expectations, roles, responsibilities, practices, and relations coordinating participation across time.
* [ ] Clarify that an institution is a governed relational configuration, not a single relationship.

## 9.4 Sinead notation audit

* [ ] Determine whether Sinead requires explicit notation for relation versus historically structured relationship.
* [ ] Do not add notation merely because the prose distinguishes the concepts.
* [ ] Add a notation requirement only if an institutional case cannot otherwise express path dependence, agency, recognition, or historical carryover.
* [ ] Keep implementation work outside this documentation cleanup unless separately planned.

---

# 10. Workstream F — Downstream Pancakes audit

The following documents should be audited after the foundational and place revisions are stable.

They should not be rewritten automatically. Change them only where they redefine a canonical term, rely on an obsolete claim, or would mislead a reader following the new model.

## 10.1 Required conceptual audits

* [ ] `docs/pancakes-institutional-participation.md`
  * Confirm that institutional relationships are path-dependent governed relations.
  * Preserve the distinction among adoption, consent, acceptance, endorsement, identification, compliance, dissent, and exit.
  * Ensure continued presence is not treated as recognition or legitimacy.

* [ ] `docs/pancakes-institutional-recognition.md`
  * Align recognition-independent, recognized, disputed, and recognition-constituted relations.
  * Ensure records and offices do not become self-validating.

* [ ] `docs/pancakes-stewardship-model.md`
  * Preserve relationship stewardship while distinguishing agentic and non-agentic relations.
  * Ensure relation alone does not create stewardship authority.
  * Remove literal relationship-memory language if present.

* [ ] `docs/pancakes-power-and-responsibility.md`
  * Align responsibility grounds with contribution, control, capability, commitment, role, benefit, dependence, vulnerability, repair, and justice.
  * Ensure causal involvement does not automatically allocate responsibility.

* [ ] `docs/pancakes-meaning.md`
  * Distinguish operative conditions, interpretation, attributed meaning, symbolic representation, and plural or contested meaning.
  * Ensure symbolic spectra do not become the exclusive source of meaning.

* [ ] `docs/pancakes-institutional-evolution.md`
  * Replace or qualify `place memory` language.
  * Preserve institutional history, commitments, capability, and succession without anthropomorphizing place.

## 10.2 Transformation and practice audits

* [ ] `docs/pancakes-recipes.md`
* [ ] `docs/pancakes-grimoires.md`
* [ ] `docs/pancakes-lifecraft.md`
* [ ] `docs/pancakes-household-lifecraft.md`
* [ ] `docs/pancakes-goods-and-services-model.md`

For each:

* confirm whether history changes present capability or only recorded meaning;
* distinguish practice from relationship with a practice;
* distinguish transformation state from symbolic interpretation;
* preserve provenance without claiming exhaustive history;
* and add cross-references only where the relational model materially clarifies the document.

## 10.3 Architecture and epistemic audits

* [ ] `docs/pancakes-epistemic-jurisdiction.md`
* [ ] `docs/pancakes-reference-services.md`
* [ ] `docs/pancakes-node-capabilities.md`
* [ ] `docs/pancakes-network-architecture.md`
* [ ] `docs/pancakes-value-discovery-model.md`
* [ ] `docs/pancakes-design-invariants.md`

Check that:

* reference services supply claims and public facts rather than ontological certainty;
* node records do not determine which external relations exist;
* permissions govern representation and action;
* private relations are not inferred or centralized unnecessarily;
* and network relationships remain scoped, reviewable, and governed.

---

# 11. Workstream G — Downstream Pitchfork and project audits

## 11.1 Pitchfork RPG and supporting documents

Audit canonical and explanatory documents for claims such as:

* a material literally carrying or remembering its whole history;
* provenance becoming part of material reality rather than a recorded and symbolically consequential history;
* every transformation necessarily producing one settled meaning;
* or relationship being used technically where connection or symbolic association is intended.

Priority files include:

* [ ] `docs/rpg/12-symbolic-materials.md`
* [ ] `docs/rpg/13-symbolic-crafting.md`
* [ ] `docs/rpg/pitchfork-frequencies.md`
* [ ] `docs/rpg/04-magic-system.md`
* [ ] `docs/pitchfork-recipes-and-grimoires.md`
* [ ] `docs/pitchfork-questing.md`
* [ ] `docs/pitchfork_overview.md`
* [ ] `docs/pitchfork_ecosystem.md`

Preserve poetic or lore-facing language when its metaphorical status is clear. Canonical technical documents must supply the precise meaning.

## 11.2 Honk terminology audit

Honk often uses `relationship` to mean ecological connection, including `Relationships Rather Than Things` and `Relationship Observations`.

Tasks:

* [ ] Decide whether these are intentionally ordinary-language uses or claims that should adopt the technical Pancakes distinction.
* [ ] In canonical design documents, prefer `relation`, `connection`, or `interaction` when no path-dependent prior course is involved.
* [ ] Preserve accessible player-facing language where technical replacement would make the game colder or less intelligible.
* [ ] Add a short terminology note rather than mechanically rewriting the entire project if that resolves the ambiguity.
* [ ] Preserve Honk's observation/recognition distinction: discovery may reveal a relation already operating.

Priority files include:

* [ ] `docs/lone-honk-design-proposal.md`
* [ ] `docs/lone-honk-processes.md`
* [ ] `docs/lone-honk-observation.md`
* [ ] `docs/lone-honk-ecology.md`

## 11.3 Redwitch and other applications

* [ ] Search Redwitch, client, mentor, household, and application documentation for definitions rather than ordinary uses of `context`, `relation`, `relationship`, `memory`, and `place`.
* [ ] Update only documents that contradict the new canonical vocabulary.
* [ ] Do not make the relational model a pretext for collecting or inferring additional sensitive information.

---

# 12. Search and terminology audit

Run repository-wide searches after the principal rewrites.

Search at minimum for:

```text
A place is a meaningful relationship
Places are relationships
relationship-bound
Place as the Stable Substrate
Places provide continuity
place memory
possesses symbolic memory
accumulates memory
object remembers
transformation with memory
Acquired frequencies describe what has happened
The transformation is canonical
Transformations are canonical
The node decides which relationships matter
```

For each match:

* [ ] determine whether it is a canonical claim, ordinary-language use, quotation, historical note, lore, or generated composite;
* [ ] update canonical conflicts;
* [ ] preserve deliberate metaphor where its status is clear;
* [ ] avoid editing generated composites directly;
* [ ] and record justified retained uses in the plan review or commit message so they are not repeatedly rediscovered.

Also search for broader combinations of:

```text
place + memory
relationship + memory
history + spectrum
provenance + material
context + node decides
relation + responsibility
relation + consent
place + owns
projection + canonical
```

These broader searches require human review and must not become global replacements.

---

# 13. Documentation and navigation consistency

After semantic edits:

* [ ] Add reciprocal navigation among the Relational Model, Place Model, and Place and Institutions.
* [ ] Add appropriate companion references from Institutional Participation, Recognition, Stewardship, Power and Responsibility, and Meaning.
* [ ] Add cross-repository references from Pitchfork frequencies and crafting to the Pancakes Relational Model.
* [ ] Ensure Pitchfork documents do not imply that Pancakes theory is owned or redefined by an implementation document.
* [ ] Ensure the Pancakes Relational Model does not redefine Pitchfork storage, settlement, crafting operations, or projection behaviour.
* [ ] Check headings, document status, companion lists, and link style for consistency.
* [ ] Check that public documentation does not link to private `_work` notes as canonical sources.

---

# 14. Validation

## 14.1 Conceptual validation

Review the final document set against the following questions.

* [ ] Can the model distinguish operative context from selected and represented context?
* [ ] Can it describe a relation without claiming everything is usefully related?
* [ ] Can it distinguish relation from path-dependent relationship?
* [ ] Can it represent a person-book relationship without granting the book reciprocal agency?
* [ ] Can it describe historical carryover without requiring literal memory or a surviving trace-object?
* [ ] Can it describe a temporary place?
* [ ] Can it distinguish place from a person's relationship with place?
* [ ] Can it distinguish material history from symbolic place history?
* [ ] Can it explain an unrecognized household-watershed relation?
* [ ] Can it explain a recognition-constituted contract or office?
* [ ] Can it prevent relation from automatically generating responsibility or authority?
* [ ] Can it map symbolic carryover to Pitchfork without treating frequencies as exhaustive reality?

## 14.2 Worked-scenario validation

Review at least these cases across the revised documents:

* [ ] person and person;
* [ ] person and book;
* [ ] person and home;
* [ ] person and landscape;
* [ ] household and watershed;
* [ ] person and institution;
* [ ] temporary emergency shelter;
* [ ] community wetland restoration;
* [ ] workshop whose accumulated practice affects later repair;
* [ ] contract whose recognition changes present standing;
* [ ] destroyed bridge whose history persists as changed route availability;
* [ ] projection that influences later action without rewriting the original event.

## 14.3 Repository validation

Use the documented workflow for each repository.

* [ ] Run Markdown formatting or lint checks if configured.
* [ ] Run link checks if configured.
* [ ] Build the Pancakes documentation site.
* [ ] Run Pancakes repository tests required for documentation changes.
* [ ] Run Pitchfork tests required by its repository workflow even if code is unchanged.
* [ ] Rebuild context composites.
* [ ] Confirm that generated composite diffs reflect source changes and no unrelated documents disappeared.
* [ ] Check `git diff --check` or the repository equivalent.
* [ ] Confirm that only intended source, navigation, plan, and generated-context files changed.

---

# 15. Acceptance criteria

This cleanup is complete when all of the following are true.

## 15.1 Canonical theory

* [ ] `docs/pancakes-relational-model.md` exists and is linked appropriately.
* [ ] It is the canonical source for context, relation, historical carryover, relationship, agentic relationship, and relational configuration.
* [ ] The Place Model is the canonical detailed specialization for place.

## 15.2 Place documents

* [ ] No canonical Pancakes document defines a place as a relationship.
* [ ] The Place Model distinguishes place from relationships with place.
* [ ] Temporary places are possible.
* [ ] Place history, historical carryover, memory, meaning, and responsibility are not bundled together.
* [ ] Node representation is distinguished from operative external relations.
* [ ] The Place and Institutions document uses the confirmed replacement for `relationship-bound`.
* [ ] Institutional continuity claims are qualified and retain their useful stewardship argument.

## 15.3 Pitchfork semantics

* [ ] Frequencies and spectra are clearly symbolic representations rather than exhaustive reality.
* [ ] Acquired frequencies represent selected symbolically consequential history.
* [ ] Provenance and lineage preserve selected history without pretending to contain all historical carryover.
* [ ] Crafting no longer requires objects or relationships to literally remember.
* [ ] Place-conditioning and place-changing transformations are distinguished.
* [ ] Terroir has one canonical definition.
* [ ] Projection canonicality is scoped to Pitchfork's recorded architecture.
* [ ] No duplicate relationship-memory subsystem has been introduced.

## 15.4 Downstream alignment

* [ ] Sinead uses compatible place and affiliation terminology.
* [ ] Downstream Pancakes documents do not redefine the canonical terms incompatibly.
* [ ] Honk and RPG metaphorical language is either compatible, intentionally informal, or explicitly qualified.
* [ ] Context composites contain the updated canonical sources.

## 15.5 Rights and privacy

* [ ] The cleanup does not authorize exhaustive relationship discovery or telemetry.
* [ ] Unrecorded relations are not treated as unreal.
* [ ] Private representations remain removable where appropriate.
* [ ] Recognition, consent, responsibility, authority, and legitimacy remain distinct.
* [ ] No symbolic or relational record is treated as unilateral ownership of another participant's meaning.

---

# 16. Risks and mitigations

## 16.1 Vocabulary migration becomes a global rewrite

**Risk:** Ordinary-language uses of `relationship`, `memory`, or `place` are mechanically replaced and project prose becomes awkward.

**Mitigation:** Restrict canonical precision to theoretical and technical claims. Review player-facing, narrative, and metaphorical uses individually.

## 16.2 Symbolic representation becomes ontology

**Risk:** Frequencies, provenance, lineage, or spectra are treated as everything a relation or place truly is.

**Mitigation:** Repeat the reality/recognition/representation boundary in the relational, frequency, crafting, and projection documents.

## 16.3 History becomes a universal data-retention mandate

**Risk:** Historical carryover is misread as a requirement to store complete histories.

**Mitigation:** Distinguish operative history from records. Preserve minimization, filtering, deletion, privacy, and local control. State explicitly that completeness is not the goal.

## 16.4 Relation automatically creates duty or authority

**Risk:** Any connection to a person, place, or ecosystem is treated as authorization to govern or intervene.

**Mitigation:** Require the separate Pancakes responsibility, stewardship, consent, jurisdiction, capability, and legitimacy analyses.

## 16.5 Technical `relationship` conflicts with existing institutional language

**Risk:** `Relationship-bound institution` becomes unintelligible or overinclusive.

**Mitigation:** Confirm and apply `affiliation-bound` or another dedicated term before downstream edits.

## 16.6 Terroir duplicates place spectrum

**Risk:** Terroir becomes a second name for every accumulated place meaning.

**Mitigation:** Define terroir through the characteristic way present place conditions participate in later transformation.

## 16.7 Cross-repository drift

**Risk:** Pancakes, Pitchfork, Sinead, and Honk adopt partially different meanings.

**Mitigation:** Establish Pancakes as the conceptual authority, make implementation documents reference it, rebuild context composites, and complete the cross-project terminology audit.

---

# 17. Suggested implementation order

Use small, reviewable changes.

## Phase 1 — Foundation

1. Confirm `affiliation-bound` terminology.
2. Confirm the narrow terroir definition.
3. Add and link `docs/pancakes-relational-model.md`.
4. Register Plan 0014 and the new source in context packaging.

## Phase 2 — Place

5. Rewrite `docs/pancakes-place-model.md`.
6. Review the Relational and Place models together for duplicated or conflicting definitions.
7. Revise `docs/pancakes-place-and-institutions.md`.

## Phase 3 — Pitchfork symbolic semantics

8. Revise `docs/pitchfork-symbolic-frequencies.md` and establish terroir.
9. Revise `docs/pitchfork-symbolic-crafting.md`.
10. Revise `docs/pitchfork-symbolic-projections.md`.
11. Review the three documents as one semantic stack.

## Phase 4 — Institutional language and downstream audit

12. Align Sinead place, governance, and institutional foundations.
13. Audit required Pancakes institutional, stewardship, responsibility, and meaning documents.
14. Audit Pancakes recipe, grimoire, Lifecraft, architecture, and epistemic documents.
15. Audit Pitchfork RPG documents.
16. Audit Honk terminology.
17. Audit Redwitch and other applications only for conflicting definitions.

## Phase 5 — Packaging and validation

18. Complete repository-wide terminology searches.
19. Update navigation and companion links.
20. Rebuild context composites and generated inventories.
21. Run documentation builds, link checks, and required repository tests.
22. Review acceptance criteria and close the plan.

---

# 18. Out of scope

This plan does not authorize:

* relational database redesign;
* new graph infrastructure;
* automated discovery of interpersonal relationships;
* location surveillance;
* retroactive event tagging;
* relationship scoring;
* new social metrics;
* a universal relationship-memory object;
* a new frequency family solely for relationality;
* migration of existing user data;
* implementation of new Sinead notation;
* changes to contract, settlement, permission, or identity code;
* wholesale replacement of ordinary-language `relationship` in narrative prose;
* or adoption of IER's technical vocabulary as Pancakes runtime terminology.

Any implementation requirement discovered during the cleanup should be recorded as a separate plan with its own authority, privacy analysis, and acceptance criteria.

---

# 19. Completion record

When the plan is complete, record:

* final terminology decisions;
* final terroir definition and canonical location;
* source documents changed;
* deliberate metaphorical uses retained;
* generated context artifacts rebuilt;
* validation commands run;
* unresolved implementation questions moved to later plans;
* and the commits or pull requests containing the work.
