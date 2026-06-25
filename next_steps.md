# Next Steps — Protocol Phase 0

The current plan. Single source of truth for "what now". Newest plan on top; rewrite as priorities change.

## Now

**Job 2 — onboard the 5 kept candidates (run in your terminal, not Cowork).**
Scope = BROAD. Dave kept 5, dropped NCT04805983 (SAD-like). Run from `protocol_corpus` where the venv + network work:

```bash
cd protocol_corpus && source .venv/bin/activate
for n in NCT04128683 NCT05725005 NCT03019289 NCT03861000 NCT03511105; do
  python scripts/fetch_ctgov_protocols.py download-pdf $n
done
python scripts/sync_registry.py --mode scan
python scripts/sync_registry.py --mode enrich
# then, per protocol, AI-backed ground truth (needs ANTHROPIC_API_KEY):
for n in NCT04128683 NCT05725005 NCT03019289 NCT03861000 NCT03511105; do
  python scripts/build_ground_truth.py $n --apply
done
```
Then select the 5 into this project's Phase-0 subset and move to Job 3.

Kept (ranked): NCT04128683 (dopamine challenge fMRI, UCSD, n=31) · NCT05725005 (ASN51 PET occupancy, n=12) · NCT03019289 (pridopidine sigma1/D2 occupancy, n=23) · NCT03861000 (PDE4D PET radioligand, NIMH, n=3) · NCT03511105 (GSK LPS alveolar challenge, n=47). Dropped: NCT04805983.

Search method that worked: drop the `phase:0` filter (junk — Early Phase 1 is a grab-bag); use `query.term` for PET "receptor occupancy" / radioligand / "pharmacological challenge" + `aggFilters=docs:prot,healthy:y`; verify PDF per study via single-study endpoint `…/studies/NCT?fields=…,DocumentSection`. Real PDFs are common, not rare.

**Job 3 — characterise the SoAs + USDM delta.**
For the protocols found, characterise the SoA and test the one open question: do single-day / no-conventional-visit studies add or stress any pattern **beyond** the 12-pattern atlas — especially the collapse of the visit/Encounter axis (everything timed relative to dosing). Do **not** rebuild the general atlas; only the Phase-0 delta.

**Fill the report.** Populate Parts 2 (protocol set) and 3 (SoA characterisation + USDM impact) of `docs/report/phase0_soa.md`, rebuild the HTML.

## Open decisions to resolve

- **Scope when the set is in hand:** narrow (classic AMS/PK microdosing) vs broad (any sub-therapeutic exploratory, keeps the two imaging protocols). Dave leans toward the single-day experimental-medicine archetype regardless of readout. Settle against the real candidates.
- **"EMP" meaning** — unconfirmed (best guess Experimental Medicine Protocol). Watch for it appearing verbatim in protocol PDFs.
