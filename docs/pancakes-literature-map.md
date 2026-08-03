# Pancakes Literature Map

**Status:** Working public map  
**Scope:** Pancakes ecosystem  
**Purpose:** Connect Pancakes, Pitchfork, Sinead, and related applications to established scholarly conversations  
**Last reviewed:** 2026-08-03

## Purpose and limits

Pancakes combines ideas that are normally studied in separate fields: institutional economics, commons governance, political philosophy, social ontology, accounting, software architecture, human-computer interaction, and institutional design. This map shows where the ecosystem enters those conversations and provides defensible starting points for further research.

It is not:

- a claim that the cited authors anticipated or endorse Pancakes;
- a complete bibliography for every ecosystem project;
- a list of authorities whose conclusions Pancakes simply adopts; or
- evidence that a software implementation is legitimate merely because it resembles an academic model.

The map distinguishes three relationships:

- **Inheritance** — a project directly uses a concept or method already developed in a field.
- **Synthesis** — a project connects concepts that the literature usually treats separately.
- **Proposal** — a project introduces a design that must be argued and tested on its own merits.

The private Book 02 bibliography should carry claim-level citations, competing interpretations, reading notes, and evidentiary judgments. This public map remains broader and more stable.

## Ecosystem orientation

| Project or layer | Primary concern | Closest scholarly conversations |
|---|---|---|
| **IER** | A physicalist identity theory of experience: Unified Experiential Fields, intrinsic constraint, experiential subjecthood, and the ethical consequences of experiential identity | philosophy of mind; consciousness studies; physicalism and identity theory; phenomenology; moral philosophy |
| **Pancakes** | The meaning, design, legitimacy, stewardship, and evolution of institutions | institutional analysis; commons governance; social ontology; political philosophy; institutional design |
| **Sinead** | A language for expressing and interrogating institutional arrangements | institutional grammar; deontic and legal concepts; conceptual modeling; policy languages; provenance |
| **Pitchfork** | Bounded execution, accounting, contracts, settlement, and projections | accounting theory; transaction systems; event sourcing; mechanism design; computational institutions |
| **Red Witch** | A humane participant interface and personal institutional environment | HCI; value-sensitive design; privacy; personal informatics; explainable systems |
| **Pitchfork QMS** | Evidence, findings, deviations, corrective action, and institutional learning | quality management; safety science; organizational learning; audit and assurance |
| **Pitchfork RPG** | Learning institutional design through simulated situations and repair | serious games; constructionism; simulation; systems thinking; problem-based learning |
| **Honk** | A bounded creative and exploratory application in the ecosystem | creativity support; participatory media; playful systems; end-user development |

The rows overlap deliberately. Pancakes is a socio-technical project: no single discipline supplies its theory, ethics, implementation, or evaluation.

## Map at a glance

| Literature cluster | Questions contributed to Pancakes | Strongest ecosystem connection |
|---|---|---|
| Institutions and governance | What are institutions, and how do rules-in-use organize recurring situations? | Pancakes, Sinead |
| Commons and polycentricity | How can people govern shared resources through nested, locally adapted arrangements? | Pancakes, Pitchfork |
| Institutional economics | How do transaction costs, property relations, governance structures, and institutional change shape coordination? | Pancakes, Pitchfork |
| Social ontology | What are roles, groups, offices, collective agents, institutional facts, and practices? | Pancakes, Sinead |
| Authority, legitimacy, and rights | When may an institution direct, constrain, or bind people, and what limits its authority? | Pancakes, Sinead, Pitchfork |
| Democracy and collective choice | How are proposals, reasons, preferences, judgments, and dissent turned into decisions? | Pancakes, Pitchfork |
| Justice, capabilities, and care | What should institutional success mean beyond output, price, or preference satisfaction? | Pancakes, Red Witch |
| Value, exchange, and accounting | What can ledgers make visible, what do prices omit, and how should contribution and settlement be represented? | Pitchfork, Pancakes |
| Participatory and value-sensitive design | Who participates in design, whose values count, and how are indirect stakeholders represented? | Red Witch, Pancakes |
| Infrastructure and socio-technical systems | How do standards, classifications, installed bases, maintenance, and invisible work shape institutions? | Pancakes, Pitchfork |
| Formal rules and computational institutions | How can rules, permissions, obligations, events, and institutional state be represented without confusing code with legitimacy? | Sinead, Pitchfork |
| Learning, resilience, and repair | How do institutions detect failure, learn, adapt, and retain memory without normalizing harm? | Pitchfork QMS, Pancakes |
| Privacy, contextual integrity, and autonomy | When is information flow appropriate, and how do consent, exit, and delegation remain meaningful? | Red Witch, Pancakes |
| Simulation and institutional pedagogy | What can models and games teach, and where do their abstractions stop? | Pitchfork RPG, Sinead |

## 1. Institutions, rules, and action situations

### Connection

Pancakes treats the institution—not the market, firm, state, or software system—as the main unit of design. Institutional Analysis and Development (IAD) offers the closest established framework for examining participants, positions, actions, information, control, costs and benefits, outcomes, and rules-in-use within recurring action situations.

The connection is strongest where Pancakes asks:

- who participates and in what role;
- which rules are written, practiced, ignored, or contested;
- what information and capabilities participants possess;
- how local outcomes connect to larger institutional settings;
- how rules change; and
- how an institution can be compared without assuming one universal form.

### Representative entry points

- Elinor Ostrom, *Understanding Institutional Diversity* (2005) — the IAD framework, rule configurations, and institutional diversity.
- Sue E. S. Crawford and Elinor Ostrom, [“A Grammar of Institutions”](https://doi.org/10.2307/2082975) (1995) — a syntax for strategies, norms, and rules.
- Elinor Ostrom, [“Background on the Institutional Analysis and Development Framework”](https://doi.org/10.1007/s11115-011-0157-x) (2011) — a compact retrospective introduction.
- Michael D. McGinnis, *Polycentric Governance and Development* (1999) — applications and development of the Bloomington school.

### Pancakes research obligations

- Compare Pancakes' primitives explicitly with IAD rather than casually relabeling them.
- Preserve the distinction between rules-in-form and rules-in-use.
- Treat Sinead as one possible descriptive and design language, not as the institution itself.
- Test whether the framework represents informal practices and contested rules, not only registered procedures.

## 2. Commons, collective action, and polycentric governance

### Connection

The Pancakes commons, node, household, village, farm, and federation models are closest to the commons-governance and polycentricity literature. This literature rejects the assumption that every shared-resource problem reduces to privatization or centralized command. It studies how communities build boundaries, monitoring, sanctions, conflict-resolution processes, and nested governance suited to particular resources and places.

Pancakes extends the design problem from natural-resource commons to physical, social, informational, and digital commons. That extension is a proposal, not an automatic consequence of Ostrom's findings.

### Representative entry points

- Elinor Ostrom, *Governing the Commons* (1990) — empirical analysis of durable common-pool resource institutions.
- Elinor Ostrom, [“Beyond Markets and States: Polycentric Governance of Complex Economic Systems”](https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/lecture/) (2009) — overview of institutional diversity and polycentric governance.
- Vincent Ostrom, Charles M. Tiebout, and Robert Warren, [“The Organization of Government in Metropolitan Areas”](https://doi.org/10.2307/1952530) (1961) — foundational polycentricity argument.
- Charlotte Hess and Elinor Ostrom, eds., *Understanding Knowledge as a Commons* (2007) — application of commons analysis to knowledge.
- Yochai Benkler, *The Wealth of Networks* (2006) — commons-based peer production and networked information.

### Pancakes research obligations

- Specify the resource, community, boundaries, and threats in every claimed commons.
- Do not turn Ostrom's design principles into a universal checklist or constitution.
- Study power, exclusion, colonial property histories, gendered work, and unequal exit alongside cooperation.
- Distinguish abundance, subtractability, congestion, stewardship, and access across physical and digital resources.

## 3. Institutional economics and economic governance

### Connection

Institutional economics supplies tools for analyzing how rules, organizations, property relations, transaction costs, path dependence, and governance structures shape economic activity. Pancakes shares its rejection of an economy understood only as isolated exchange among frictionless actors. Pitchfork's contracts and settlements also invite comparison with work on firms, relational contracting, and alternative governance structures.

Pancakes differs by centering human flourishing, participation, legitimacy, and institutional repair rather than treating economizing as the sole objective.

### Representative entry points

- Ronald H. Coase, [“The Nature of the Firm”](https://doi.org/10.1111/j.1468-0335.1937.tb00002.x) (1937) — why coordination occurs through firms as well as markets.
- Ronald H. Coase, [“The Problem of Social Cost”](https://www.jstor.org/stable/724810) (1960) — reciprocal harms, transaction costs, and institutional comparison.
- Douglass C. North, *Institutions, Institutional Change and Economic Performance* (1990) — formal and informal constraints, organizations, and path-dependent change.
- Oliver E. Williamson, [“The New Institutional Economics: Taking Stock, Looking Ahead”](https://doi.org/10.1257/jel.38.3.595) (2000) — governance, transaction costs, and levels of institutional analysis.
- Karl Polanyi, *The Great Transformation* (1944) — economies embedded in social and political institutions.
- Geoffrey M. Hodgson, [“What Are Institutions?”](https://doi.org/10.1111/j.1467-6435.2006.00288.x) (2006) — definitional clarification within institutional economics.

### Pancakes research obligations

- Compare feasible institutional alternatives, including their administrative and political costs.
- Represent informal norms and historical lock-in, not only explicit contracts.
- Avoid assuming that lower transaction cost means greater justice or legitimacy.
- Explain when coordination belongs in households, commons, firms, markets, public institutions, or hybrids.

## 4. Social ontology and collective agency

### Connection

Sinead needs a defensible vocabulary for persons, groups, institutions, organizations, roles, offices, practices, rules, status, collective action, and responsibility. Social ontology studies what these entities are and how they come to exist, persist, and act.

This literature is crucial to the Pancakes distinction between an institution, its participants, its governing architecture, its operational organization, its implementation, and its history.

### Representative entry points

- [Stanford Encyclopedia of Philosophy, “Social Ontology”](https://plato.stanford.edu/entries/social-ontology/) — field overview and bibliography.
- John R. Searle, *The Construction of Social Reality* (1995) and *Making the Social World* (2010) — institutional facts, status functions, and constitutive rules.
- Margaret Gilbert, *On Social Facts* (1989) — plural subjects and joint commitment.
- Raimo Tuomela, *The Philosophy of Sociality* (2007) — we-mode collective intentionality.
- Christian List and Philip Pettit, *Group Agency* (2011) — conditions under which groups can count as agents.
- Brian Epstein, *The Ant Trap* (2015) — critique and reconstruction of social ontology's grounding assumptions.

### Pancakes research obligations

- Keep ontological claims separate from convenient database entities.
- State when collective agency is literal, attributed, delegated, or merely shorthand.
- Represent institutional continuity and succession without erasing participant change.
- Permit several theories of groups and institutions rather than embedding one disputed ontology invisibly.

## 5. Authority, legitimacy, rights, and normative relations

### Connection

Pancakes distinguishes capability, power, permission, responsibility, authority, stewardship, recognition, and legitimacy. Political philosophy and jurisprudence provide the necessary arguments and counterexamples. They show why legality, effectiveness, consent, popularity, and moral legitimacy cannot be collapsed into one property.

Hohfeld's analysis is especially relevant to Sinead: a single `right` primitive is unlikely to represent claim-rights, liberties, powers, liabilities, immunities, and disabilities accurately.

### Representative entry points

- [Stanford Encyclopedia of Philosophy, “Authority”](https://plato.stanford.edu/entries/authority/) and [“Political Legitimacy”](https://plato.stanford.edu/entries/legitimacy/) — major theories and distinctions.
- Max Weber, *Economy and Society* (1922/1978) — authority and legitimate domination as sociological categories.
- David Beetham, *The Legitimation of Power* (1991/2013) — legality, shared beliefs, and expressed consent.
- Allen Buchanan, [“Political Legitimacy and Democracy”](https://doi.org/10.1086/233791) (2002) — legitimacy, justice, and democratic authorization.
- Wesley Newcomb Hohfeld, *Fundamental Legal Conceptions as Applied in Judicial Reasoning* (1919) — the claim/liberty/power/immunity framework.
- Joseph Raz, *The Morality of Freedom* (1986) — authority and the service conception.

### Pancakes research obligations

- Model legitimacy as an argued and revisable assessment, not a boolean system fact.
- Identify the constituency, domain, grounds, and time of a legitimacy claim.
- Distinguish voluntary contracts from philosophical social contracts and imposed political obligations.
- Treat consent, voice, contestation, appeal, remedy, and feasible exit as separate mechanisms.
- Make rights capable of constraining otherwise valid execution and settlement.

## 6. Democracy, deliberation, and collective choice

### Connection

Governance is more than voting. Pancakes needs an account of agenda formation, standing, proposal, deliberation, information, aggregation, authorization, execution, review, dissent, and reversal. Social-choice theory demonstrates that aggregation rules embody tradeoffs and cannot simply reveal a pre-existing “will of the community.” Deliberative and participatory democracy add reason-giving, inclusion, and communicative conditions.

### Representative entry points

- [Stanford Encyclopedia of Philosophy, “Social Choice Theory”](https://plato.stanford.edu/entries/social-choice/) — accessible overview and bibliography.
- Kenneth J. Arrow, *Social Choice and Individual Values* (1951/1963) — limits of preference aggregation.
- Amartya Sen, *Collective Choice and Social Welfare* (1970/2017) — information, welfare, liberty, and social choice.
- James S. Fishkin, *Democracy and Deliberation* (1991) — deliberation and informed public judgment.
- Jürgen Habermas, *Between Facts and Norms* (1992/1996) — law, public discourse, and democratic legitimacy.
- Jane Mansbridge et al., [“A Systemic Approach to Deliberative Democracy”](https://doi.org/10.1017/CBO9781139178914.002) (2012) — deliberation distributed across a political system.
- Hélène Landemore, *Open Democracy* (2020) — openness, deliberation, and citizen participation beyond electoral representation.

### Pancakes research obligations

- Record the electorate, agenda, procedure, rule version, quorum, outcome, and dissent.
- Evaluate agenda power and exclusion as well as the final tally.
- Support multiple decision mechanisms without presenting them as politically neutral.
- Separate epistemic quality, procedural fairness, legitimacy, and participant acceptance.

## 7. Justice, capabilities, care, and human flourishing

### Connection

Pancakes does not treat price, income, preference satisfaction, engagement, or aggregate output as a complete measure of institutional success. The capability approach asks what people are actually able to be and do. Theories of justice examine rights, fair distribution, social structure, recognition, and the treatment of the least advantaged. Care ethics makes dependency, relationship, maintenance, and asymmetrical need visible.

### Representative entry points

- John Rawls, *A Theory of Justice* (1971/1999) — basic liberties, fair equality of opportunity, and distributive principles.
- Amartya Sen, *The Idea of Justice* (2009) — comparative justice, public reasoning, and realized lives.
- Martha C. Nussbaum, *Creating Capabilities* (2011) — a capabilities account grounded in dignity.
- Ingrid Robeyns, *Wellbeing, Freedom and Social Justice* (2017) — a systematic account of the capability approach.
- Iris Marion Young, *Justice and the Politics of Difference* (1990) — structural domination and oppression beyond distribution alone.
- Joan C. Tronto, *Moral Boundaries* (1993) and *Caring Democracy* (2013) — care as moral and political practice.
- Nancy Fraser, *Scales of Justice* (2008) — redistribution, recognition, representation, and framing.

### Pancakes research obligations

- State whose flourishing is being assessed and who participates in defining it.
- Keep individual capabilities distinct from institutional or software “capabilities.”
- Include disability, dependency, unpaid care, structural oppression, and unequal bargaining power in apparently general models.
- Do not infer welfare from activity, compliance, retention, or willingness to transact.

## 8. Value, exchange, contribution, and accounting

### Connection

Pitchfork treats accounting as a bounded institutional memory and settlement substrate. Pancakes asks how price, need, contribution, stewardship, reciprocity, externality, and human value relate without forcing them into a single scalar. Accounting research helps distinguish transaction records, valuation conventions, accountability relationships, organizational control, and social or environmental accounts.

Economic sociology and plural theories of value warn that markets and prices are instituted arrangements, not neutral discovery devices that exhaust what people value.

### Representative entry points

- Yuji Ijiri, *Theory of Accounting Measurement* (1975) — foundations and limits of accounting measurement.
- Anthony G. Hopwood and Peter Miller, eds., *Accounting as Social and Institutional Practice* (1994) — accounting as constitutive organizational practice.
- Michael Power, *The Audit Society* (1997) — institutional effects and limits of auditability.
- Viviana A. Zelizer, *The Social Meaning of Money* (1994) — differentiated social meanings and uses of money.
- David Graeber, *Debt: The First 5,000 Years* (2011) — anthropological history of debt, obligation, and money.
- Elinor Ostrom, [“Crossing the Great Divide: Coproduction, Synergy, and Development”](https://doi.org/10.1016/0305-750X(96)00023-X) (1996) — citizens and public providers jointly producing services.
- Mariana Mazzucato, *The Value of Everything* (2018) — debate over value creation and value extraction.

### Pancakes research obligations

- Say what each ledger measures, for whom, under which valuation convention, and for what decision.
- Preserve non-fungible and qualitative judgments rather than manufacturing false commensurability.
- Distinguish correct settlement from fair settlement.
- Make externalities, unpaid burdens, dependency, and extraction visible to review without claiming an automatic moral verdict.
- Study how metrics change behavior and redistribute authority.

## 9. Participatory design, value-sensitive design, and responsible innovation

### Connection

Pancakes institutions are meant to be designed with participants, not merely delivered to users. Participatory design brings workplace democracy, mutual learning, and the politics of design into technical practice. Value Sensitive Design provides methods for investigating values and direct and indirect stakeholders throughout design. Responsible innovation adds anticipation, reflexivity, inclusion, and responsiveness.

### Representative entry points

- Douglas Schuler and Aki Namioka, eds., *Participatory Design: Principles and Practices* (1993).
- Pelle Ehn, *Work-Oriented Design of Computer Artifacts* (1988) — Scandinavian participatory-design foundations.
- Batya Friedman and David G. Hendry, *Value Sensitive Design* (2019) — theory and practical methods; see the [VSD Lab reading guide](https://vsdesign.org/publications/).
- Batya Friedman, [“Value-Sensitive Design”](https://doi.org/10.1145/242485.242493) (1996) — concise foundational statement.
- Jack Stilgoe, Richard Owen, and Phil Macnaghten, [“Developing a Framework for Responsible Innovation”](https://doi.org/10.1016/j.respol.2013.05.008) (2013).
- Sasha Costanza-Chock, *Design Justice* (2020) — design led by marginalized communities and analysis of structural inequality.

### Pancakes research obligations

- Involve affected people before formalization, not only after a prototype exists.
- Distinguish participation in design from consent to deployment or governance.
- Identify indirect stakeholders, non-users, future participants, and people who cannot safely exit.
- Treat values as contested and situated rather than as labels selected by designers.

## 10. Infrastructure, classification, and invisible work

### Connection

Pancakes nodes, reference services, capabilities, standards, and institutional memory form infrastructure. Infrastructure studies shows that infrastructure is relational, embedded in practice, built on installed bases, learned through membership, and often most visible when it fails. Classification systems and standards allocate attention, burden, legitimacy, and access. CSCW studies the articulation and invisible work required to make formal systems function.

### Representative entry points

- Susan Leigh Star and Karen Ruhleder, [“Steps Toward an Ecology of Infrastructure”](https://doi.org/10.1287/isre.7.1.111) (1996).
- Geoffrey C. Bowker and Susan Leigh Star, *Sorting Things Out* (1999) — classifications, standards, and their consequences.
- Susan Leigh Star, [“The Ethnography of Infrastructure”](https://doi.org/10.1177/00027649921955326) (1999).
- Lucy Suchman, *Plans and Situated Actions* (1987/2007) — situated practice and the limits of plans.
- Anselm Strauss, *Continual Permutations of Action* (1993) — articulation work and negotiated order.
- Geoffrey Bowker et al., eds., *Boundary Objects and Beyond* (2015) — coordination across social worlds without complete consensus.

### Pancakes research obligations

- Document maintenance, migration, training, exception handling, and repair as first-class work.
- Test classifications with people who bear their edge cases.
- Expect actual practice to exceed workflows and schemas.
- Preserve local meaning while enabling interoperability; do not confuse standardization with consensus.

## 11. Formal rules, deontic relations, and computational institutions

### Connection

Sinead and Pitchfork sit near research on deontic logic, legal and policy representation, normative multi-agent systems, smart contracts, and electronic institutions. These fields ask how obligations, permissions, prohibitions, powers, roles, sanctions, and institutional events can be represented or executed.

The most important Pancakes boundary is negative: executable rules do not prove that an institution is legitimate, complete, fair, or faithful to practice.

### Representative entry points

- Georg Henrik von Wright, [“Deontic Logic”](https://doi.org/10.1093/mind/LX.237.1) (1951) — foundational formal treatment of obligation and permission.
- Andrew J. I. Jones and Marek Sergot, [“A Formal Characterisation of Institutionalised Power”](https://doi.org/10.1007/3-540-60085-9_53) (1996) — institutional power and normative systems.
- Guido Governatori et al., [“Rule-Based Modelling of Contracts”](https://doi.org/10.1007/11575771_3) (2005) — formal rules, violations, and reparations in contracts.
- Alexander Boer, Tom van Engers, and Radboud Winkels, [“Using Ontologies for Comparing and Harmonizing Legislation”](https://doi.org/10.1145/1165485.1165500) (2006) — legal knowledge representation and comparison.
- Virginia Dignum, *A Model for Organizational Interaction* (2004) — agent organizations, roles, norms, and interaction.
- Primavera De Filippi and Aaron Wright, *Blockchain and the Law* (2018) — code, governance, and legal institutions.

### Pancakes research obligations

- Compare Sinead directly with Institutional Grammar, Hohfeldian relations, deontic systems, policy languages, and legal ontologies.
- Represent violation, justified exception, contestation, waiver, remedy, and rule change—not only compliance.
- Separate descriptive claims, normative claims, executable constraints, and evaluative findings.
- Keep human-readable reasons and jurisdiction visible alongside machine execution.
- State the limits of what a formal model and simulator can infer.

## 12. Organizational learning, safety, quality, and institutional repair

### Connection

Pancakes treats evolution and repair as core institutional capabilities. Pitchfork QMS makes claims, evidence, findings, deviations, corrective actions, responsibility, and learning traceable. Organizational learning, safety science, resilience engineering, and quality improvement offer mature accounts of feedback and failure—but also warn that formal compliance and performance indicators can conceal systemic risk.

### Representative entry points

- Chris Argyris and Donald A. Schön, *Organizational Learning II* (1996) — single-loop and double-loop learning, inquiry, and defensive routines.
- Donald A. Schön, *The Reflective Practitioner* (1983) — reflection-in-action and professional learning.
- Charles Perrow, *Normal Accidents* (1984/1999) — interactive complexity and tightly coupled systems.
- James Reason, *Managing the Risks of Organizational Accidents* (1997) — organizational defenses and latent conditions.
- Sidney Dekker, *Just Culture* (2007/2012) — accountability and learning after failure.
- Erik Hollnagel, David D. Woods, and Nancy Leveson, eds., *Resilience Engineering* (2006) — adaptation and system resilience.
- Nancy Leveson, *Engineering a Safer World* (2011) — systems-theoretic safety and control.
- Donald T. Campbell, [“Assessing the Impact of Planned Social Change”](https://doi.org/10.1016/0149-7189(79)90048-X) (1979) — corruption pressures created by quantitative indicators.

### Pancakes research obligations

- Design findings to support learning and remedy, not merely blame or closure.
- Distinguish local error from systemic conditions and distributed responsibility.
- Preserve negative evidence, uncertainty, dissent, and the remit of each inquiry.
- Audit whether the measurement and review system creates metric gaming or ritual compliance.
- Make repair reversible where possible and evaluate its downstream effects.

## 13. Privacy, information flow, autonomy, and explanation

### Connection

Pancakes and Red Witch organize information across personal, household, community, and institutional contexts. Privacy is therefore not just secrecy or access control. Contextual-integrity research asks whether information flows are appropriate to social roles, purposes, subjects, senders, recipients, and transmission principles. Work on autonomy and informed consent tests whether delegation, recommendation, personalization, and exit remain meaningful.

### Representative entry points

- Helen Nissenbaum, *Privacy in Context* (2010) — contextual integrity and appropriate information flows.
- Julie E. Cohen, *Configuring the Networked Self* (2012) — privacy, subject formation, and networked information power.
- Solon Barocas and Helen Nissenbaum, [“Big Data's End Run around Anonymity and Consent”](https://nissenbaum.tech.cornell.edu/papers/BigDatasEndRun.pdf) (2014).
- Batya Friedman, Peter H. Kahn Jr., and Alan Borning, [“Value Sensitive Design and Information Systems”](https://doi.org/10.1007/978-94-007-7844-3_4) (2013).
- Finale Doshi-Velez and Been Kim, [“Towards a Rigorous Science of Interpretable Machine Learning”](https://arxiv.org/abs/1702.08608) (2017) — evaluation questions for interpretability.
- Harry Collins and Robert Evans, *Rethinking Expertise* (2007) — contributory and interactional expertise.

### Pancakes research obligations

- Evaluate flows by context and purpose, not only by whether a user once consented.
- Make delegation granular, revocable, inspectable, and time-bounded where appropriate.
- Keep explanation connected to standing, evidence, authority, and remedy.
- Do not infer that legibility to software or administrators equals understanding by participants.
- Use interactional expertise to make institutional interfaces intelligible without claiming to replace practitioners.

## 14. Simulation, games, and learning institutional design

### Connection

Pitchfork RPG and Book 02's puzzle architecture use formal situations to teach institutional diagnosis and repair. Constructionism, experiential learning, microworlds, serious games, and participatory simulation provide relevant methods. The game can test consequences only within its world model; accepting arbitrary prose or Sinead syntax does not supply missing causal semantics.

### Representative entry points

- Seymour Papert, *Mindstorms* (1980) — constructionism and learning by building public artifacts.
- Donald A. Schön, *The Reflective Practitioner* (1983) — problem framing and reflective experimentation.
- John D. Sterman, *Business Dynamics* (2000) — system-dynamics modeling and learning about feedback.
- Clark C. Abt, *Serious Games* (1970) — games for education and policy problems.
- Kurt Squire, *Video Games and Learning* (2011) — designed experiences and situated learning.
- Etienne Wenger, *Communities of Practice* (1998) — learning through participation and changing identity.

### Pancakes research obligations

- Publish the model boundary, assumptions, causal rules, and acceptance criteria of each scenario.
- Permit multiple successful architectures and preserve their different consequences.
- Distinguish “works in this simulation” from feasibility, justice, legitimacy, and real-world evidence.
- Pair simulation with participatory design, domain expertise, adversarial review, and reversible pilots before real use.

## Cross-cutting critical literatures

The following are not optional application areas. They test whether apparently general institutional concepts hide assumptions about independence, rationality, competence, household form, property, identity, safety, or exit.

| Critical literature | What it tests in Pancakes |
|---|---|
| Feminist economics and social reproduction | Whether unpaid care, dependency, household power, and reproductive labor disappear from economic models |
| Disability studies and disability justice | Whether participation assumes standardized bodies, cognition, communication, time, or independence |
| Critical race theory and racial capitalism | Whether rules and property arrangements reproduce historically structured power while appearing neutral |
| Indigenous governance and knowledge | Whether commons and stewardship language appropriates traditions or ignores sovereignty and legal plurality |
| Postcolonial and decolonial theory | Whether institutional “development” universalizes one history or administrative model |
| Science and technology studies | How facts, classifications, expertise, and technical artifacts acquire authority |
| Platform studies and surveillance studies | How interfaces, data extraction, ranking, lock-in, and private governance reshape participation |
| Labor process and workplace democracy | Who controls work, tools, information, surplus, and institutional change |

Representative starting points include Marilyn Waring's *If Women Counted* (1988), Nancy Folbre's *The Invisible Heart* (2001), Rosemarie Garland-Thomson's *Extraordinary Bodies* (1997), Leah Lakshmi Piepzna-Samarasinha's *Care Work* (2018), Kimberlé Crenshaw's work on intersectionality, Cedric J. Robinson's *Black Marxism* (1983/2000), Glen Sean Coulthard's *Red Skin, White Masks* (2014), Linda Tuhiwai Smith's *Decolonizing Methodologies* (1999/2021), and Ruha Benjamin's *Race After Technology* (2019).

These literatures should change core definitions and test cases, not be added after a supposedly neutral architecture is complete.

## Where the ecosystem appears to contribute

The following are candidate Pancakes syntheses or proposals. Each requires comparison, evidence, and critical testing before it can be presented as a contribution.

1. **Institutional engineering as a compositional practice.** Institutions are described through people, purposes, places, roles, capabilities, resources, transformations, rules, authority, records, and repair mechanisms, then evaluated as working arrangements.
2. **A semantic layer separated from execution.** Pancakes supplies institutional meaning, Sinead formalizes an interrogable arrangement, and Pitchfork executes only bounded registered semantics.
3. **Legitimacy as a continuing, domain-specific assessment.** Legitimacy is neither stored as a permanent system property nor inferred from compliance, persistence, or successful settlement.
4. **Accounting without totalization.** Pitchfork records events and supports projections while allowing important human values and qualitative judgments to remain outside a single ledger or score.
5. **Institutional interrogation.** Reference practice, institutional traces, claims, evidence, findings, deviations, exceptions, responsibility, remedies, and learning form a reusable method across domains.
6. **Capability-preserving stewardship.** Institutional health includes whether people and communities gain the real ability to understand, maintain, contest, repair, and replace their arrangements.
7. **Executable institutional puzzles.** Learners propose institutional architectures, and a bounded simulator evaluates consequences rather than checking for one anticipated answer.
8. **Polycentric personal and community computing.** Household, community, and federated nodes can share capabilities and settle commitments without making one platform the universal governor.

## Common category errors to avoid

- **Institution ≠ software.** Software may record or enforce parts of an institution; people, practices, interpretation, authority, and material conditions remain constitutive.
- **Rule-in-form ≠ rule-in-use.** Registered policy does not establish actual practice.
- **Capability ≠ permission.** Being technically able to act does not authorize the action.
- **Power ≠ authority.** Control or leverage does not establish a right to rule.
- **Legality ≠ legitimacy.** Legal recognition is one institutional fact, not a complete moral judgment.
- **Consent ≠ justice.** Formally voluntary exchange may still involve exploitation, dependency, or constrained exit.
- **Correct settlement ≠ fair settlement.** Computational validity does not decide distributive or procedural fairness.
- **Metric ≠ value.** A measure is produced for a purpose under a convention and can change the activity measured.
- **Formal expressibility ≠ causal knowledge.** Sinead syntax alone cannot tell a simulator how an invented practice changes the world.
- **Simulation success ≠ real-world feasibility.** Administrative capacity, power, history, adoption, noncompliance, and maintenance remain empirical questions.
- **Participation ≠ legitimacy.** Participation can be symbolic, unsafe, unrepresentative, or structurally constrained.
- **Exit ≠ freedom.** Exit may be costly, unavailable, or require abandoning essential relationships and resources.

## Suggested reading paths

### For Pancakes institutional foundations

1. Ostrom, *Understanding Institutional Diversity*.
2. Hodgson, “What Are Institutions?”
3. Stanford Encyclopedia, “Social Ontology.”
4. Beetham, *The Legitimation of Power*.
5. Sen, *The Idea of Justice*.
6. Star and Ruhleder, “Steps Toward an Ecology of Infrastructure.”

### For Sinead language design

1. Crawford and Ostrom, “A Grammar of Institutions.”
2. Hohfeld, *Fundamental Legal Conceptions*.
3. von Wright, “Deontic Logic.”
4. Jones and Sergot, “A Formal Characterisation of Institutionalised Power.”
5. Bowker and Star, *Sorting Things Out*.
6. Suchman, *Plans and Situated Actions*.

### For Pitchfork economic and execution semantics

1. Williamson, “The New Institutional Economics.”
2. Hopwood and Miller, *Accounting as Social and Institutional Practice*.
3. Sen, *Collective Choice and Social Welfare*.
4. Ostrom, “Crossing the Great Divide.”
5. Governatori et al., “Rule-Based Modelling of Contracts.”
6. Power, *The Audit Society*.

### For Red Witch and participant-facing applications

1. Nissenbaum, *Privacy in Context*.
2. Friedman and Hendry, *Value Sensitive Design*.
3. Costanza-Chock, *Design Justice*.
4. Cohen, *Configuring the Networked Self*.
5. Collins and Evans, *Rethinking Expertise*.
6. Tronto, *Caring Democracy*.

### For Pitchfork QMS and institutional repair

1. Argyris and Schön, *Organizational Learning II*.
2. Reason, *Managing the Risks of Organizational Accidents*.
3. Dekker, *Just Culture*.
4. Leveson, *Engineering a Safer World*.
5. Power, *The Audit Society*.
6. Campbell, “Assessing the Impact of Planned Social Change.”

### For Pitchfork RPG and the Book 02 puzzles

1. Papert, *Mindstorms*.
2. Schön, *The Reflective Practitioner*.
3. Sterman, *Business Dynamics*.
4. Squire, *Video Games and Learning*.
5. Ostrom, *Understanding Institutional Diversity*.
6. Wenger, *Communities of Practice*.

## Research gaps and next reviews

The next focused literature reviews should address:

1. **Sinead's normative relations:** compare its proposed primitives with Hohfeld, Institutional Grammar, deontic logic, legal ontologies, and policy languages.
2. **Pancakes legitimacy:** compare its multidimensional model with political legitimacy, organizational legitimacy, procedural justice, recognition, and trust research.
3. **Plural accounting:** examine social accounting, ecological economics, multi-capital accounting, care accounting, and critiques of commensuration.
4. **Institutional feasibility:** develop a ladder from conceptual coherence through simulation, implementation, adoption, operation, resilience, and repair.
5. **Digital commons:** distinguish knowledge commons, data commons, platform cooperatives, open-source communities, and common-pool resources.
6. **Institutional memory and evidence:** connect provenance, archival theory, audit, oral history, testimony, and epistemic injustice.
7. **Federation and legal pluralism:** study overlapping jurisdiction, subsidiarity, conflict of laws, Indigenous sovereignty, and polycentric coordination.
8. **Economic power and exploitation:** connect bargaining power, monopsony, dependency, principal-agent problems, labor process, and theories of exploitation.
9. **Care and household institutions:** test whether Pancakes models care, childhood, disability, intimacy, and dependency without importing market or contract assumptions.
10. **Evaluation:** define how prototypes and pilots will be studied with participants, including failure, withdrawal, unintended use, and long-term maintenance.

## Maintenance policy

This map should remain navigational rather than exhaustive.

- Add a field when it changes how an ecosystem concept should be understood, designed, or evaluated.
- Prefer a small number of representative and contrasting sources over a long undifferentiated bibliography.
- Link to stable publisher, DOI, author, or open-access pages where possible.
- Identify whether a source is empirical, normative, formal, historical, interpretive, or design-oriented.
- Do not cite a field as support for a Pancakes proposal unless the cited work actually establishes the relevant claim.
- Preserve disagreements. A literature map should expose live alternatives rather than manufacture consensus.
- Move claim-level notes, quotations, page references, and comprehensive bibliographies into project-specific research files or the private Book 02 bibliography.

## Acknowledgment of intellectual position

Pancakes is best understood as a constructive synthesis situated among these fields. The ecosystem inherits many established distinctions, connects them across disciplinary boundaries, and proposes computational and institutional arrangements that remain open to critique and empirical testing. Its public documentation should make those relationships visible without borrowing academic authority that the work has not earned.
