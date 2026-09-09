# Findings and interpretation decisions

- **Metadata mismatch:** downloaded CSV has 52,416 data rows; landing page lists 52,417. Use measured row count.
- **Incomplete year:** readings stop on December 30, 2017. The 364 complete days are preserved; December 31 is not invented.
- **Units absent on source table:** normalize aggregate demand to median 100. No unsupported physical-unit conversion.
- **No capacity measurements:** 110/125/140/155 are hypothetical normalized thresholds. 155 is the post-sweep illustrative scenario; all thresholds are retained.
- **Dependence changes the event:** independent reading resampling can inflate any-exceedance-per-day frequency relative to observed daily structure. It is not evidence that every independent-sampling model is universally wrong.
- **Weather association is not causation:** hottest-quarter days may also differ in season, calendar and behaviour. No causal heat sensitivity is inferred.
- **Simulation not forecast:** exact historical rates are available by direct counting. Monte Carlo matches those rates under the stated empirical pools; seeds are not future test periods.
- **Book provenance:** the p.63 resampling pattern inspired a fresh implementation. Day blocks, demand stress and weather pools are project extensions, not claims made by the book.
- **Scope of 50 lines:** the runnable scenario core has 50 physical lines. Supporting preparation, tests and documentation are additional files.
