I shuffled the electricity readings. The estimated daily risk jumped from 16% to 96%.

I adapted the resampling example from Practical Statistics for Data Scientists by Peter Bruce, Andrew Bruce and Peter Gedeck (O'Reilly, 2nd edition, chapter 2, pp. 62–64; Python example p. 63) into a 50-line energy scenario simulator.

The question: how often would demand exceed a hypothetical capacity limit?

I downloaded UCI's Tetouan demand-and-weather data and audited it: 52,416 readings, 364 complete days, no missing cells and no duplicate timestamps.

Then I compared two ways to simulate a day:

• Draw 144 independent ten-minute readings.
• Draw one complete historical day, keeping its demand pattern together.

At an illustrative capacity index of 155, with median demand set to 100, seed 42 produced:

Independent readings: 96.07% of simulated days crossed the limit.
Whole days: 16.07%.
Exact historical day rate: 15.93%.

The independent sampler scattered clustered peaks across many more artificial days. Same source data. Different time structure. Different answer.

I also tested a stated 10% demand-growth scenario. The exact all-day rate rose from 15.93% to 34.34%. For the warmest quarter of historical days, it went from 62.64% to 80.22%.

These are scenario results, not real grid capacity, blackout probabilities, a forecast, or a causal claim about temperature. The repo keeps the full capacity sweep, including the initial 125-point scenario that was exceeded almost every day.

Seven tests passed. Two complete runs matched. Three seeds were checked against exact probabilities. The core has exactly 50 physical lines; data preparation and tests are separate.

The textbook supplied the resampling pattern. My extension was preserving complete days, adding weather context and demand stress, and checking the simulation against a result I could calculate exactly.

https://github.com/sravanni369/energy-capacity-scenarios

#DataScience #EnergyAnalytics #Python #MonteCarlo #DataQuality
