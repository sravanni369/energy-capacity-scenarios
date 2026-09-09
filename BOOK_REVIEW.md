# Book collection review

The supplied collection contained 63 PDF files, including six duplicates: 57 unique PDFs and 11,730 pages were mechanically text-scanned for algorithm terms. This was a collection search, not a claim that every page was closely read. Selected source passages were then reviewed directly. No CSV, Excel or Parquet dataset was found in the books collection, so the project uses public UCI demand and weather records.

## Selected source

Peter Bruce, Andrew Bruce and Peter Gedeck, *Practical Statistics for Data Scientists*, second edition (O'Reilly, 2020), chapter 2, The Bootstrap, printed pages 62–64. The Python example on printed page 63 (PDF page 81 in the supplied copy) repeatedly resamples loan-income observations and computes a median.

This project independently adapts sampling with replacement to whole historical electricity-demand days. It changes the statistic to daily capacity exceedance and compares complete days with independent readings. The source is credited as a conceptual and algorithmic starting point; no book PDF or scanned page is redistributed.

## Related Monte Carlo source

Phil Winder's *Reinforcement Learning* (O'Reilly), pages 50–58, was the source for the earlier inventory project. Its Monte Carlo reinforcement-learning method estimates returns for policies. The current energy project is scenario simulation through empirical resampling, not a reproduction of that reinforcement-learning algorithm. This distinction prevents attributing a new energy implementation to unrelated textbook code.

## Selection rationale

Complete-day resampling makes a practical business modelling issue testable in a compact implementation: daily peak events depend on the relationship between readings within a day. Exact empirical probabilities provide a transparent baseline for checking the simulation. Weather-conditioned pools and explicit growth assumptions extend the example without claiming a forecast or a measured grid reliability assessment.
