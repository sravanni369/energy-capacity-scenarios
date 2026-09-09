I got two very different answers from the same electricity dataset: 16% and 96%.

The difference came from how I sampled a day.

For this project, I adapted the bootstrap example in Practical Statistics for Data Scientists by Peter Bruce, Andrew Bruce and Peter Gedeck into a 50-line Python energy scenario simulator.

The business question was simple: how often could demand cross a chosen capacity limit?

I used UCI's Tetouan electricity and weather records: 52,416 readings across 364 complete days. After checking timestamps, missing values and duplicates, I tried two approaches:

• Pick 144 ten-minute readings independently to build an artificial day.
• Pick a whole historical day and keep its demand pattern together.

At the same hypothetical capacity limit, one run gave:

Independent readings: 96.07% of simulated days crossed the limit.
Whole historical days: 16.07%.
Exact historical day rate: 15.93%.

Picking readings independently spread clustered peaks across many more days. That changed the answer dramatically, even though the source data stayed the same.

I also added a 10% demand-growth scenario. The exact all-day exceedance rate rose from 15.93% to 34.34%. The repository includes the warm-weather comparison and the full capacity sweep, so the headline result has context.

The limit is illustrative: an index of 155, with median demand set to 100. These results do not predict blackouts or measure the city's actual capacity.

Seven tests passed, two full runs matched, and I checked three random seeds against exact probabilities. The simulation core is 50 lines; preparation and tests are separate.

My main takeaway: before trusting a simulation, check what its sampling method does to the structure of the data.

Book credit: Practical Statistics for Data Scientists, 2nd edition, O'Reilly (2020), chapter 2, pp. 62–64; Python example on p. 63. I extended its resampling pattern to complete electricity-demand days, weather groups and demand-growth scenarios.

Data credit: Salam and El Hibaoui, Power Consumption of Tetouan City, UCI, CC BY 4.0.

Code, data, tests and results:
https://github.com/sravanni369/energy-capacity-scenarios

#DataScience #EnergyAnalytics #Python #MonteCarlo
