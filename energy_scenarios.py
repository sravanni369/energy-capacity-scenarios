"""Day-block Monte Carlo; adapts Bruce/Bruce/Gedeck, 2nd ed., p.63 resampling."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
ROOT = Path(__file__).resolve().parent
CAPACITY, REPEATS = 155.0, 20000
def simulate(days, capacity, seed, repeats=REPEATS):
    days = np.asarray(days, dtype=float)
    if days.ndim != 2 or not days.size or not np.isfinite(days).all():
        raise ValueError('Finite nonempty matrix of complete days required')
    if capacity <= 0 or repeats < 1:
        raise ValueError('Positive capacity and simulation count required')
    rng = np.random.default_rng(seed)
    paths = days[rng.integers(len(days), size=repeats)]
    iid = rng.choice(days.ravel(), size=(repeats, days.shape[1]))
    block_p = float((paths > capacity).any(axis=1).mean())
    iid_p = float((iid > capacity).any(axis=1).mean())
    exact = float((days > capacity).any(axis=1).mean())
    iid_exact = float(1 - (days <= capacity).mean() ** days.shape[1])
    hours = float((paths > capacity).sum(axis=1).mean() / 6)
    return dict(block=block_p, iid=iid_p, exact=exact, iid_exact=iid_exact, hours=hours)
def main():
    df = pd.read_csv(ROOT / 'data/demand_weather.csv', parse_dates=['DateTime'])
    df['day'] = df.DateTime.dt.strftime('%Y-%m-%d')
    df['slot'] = df.DateTime.dt.hour * 6 + df.DateTime.dt.minute // 10
    load = df.pivot(index='day', columns='slot', values='load_index')
    assert load.shape[1] == 144 and load.notna().all().all()
    temp = df.groupby('day').Temperature.mean().reindex(load.index)
    threshold = float(temp.quantile(.75))
    groups = {'all_days': load.to_numpy(), 'warm_quartile': load[temp >= threshold].to_numpy()}
    result = dict(capacity_index=CAPACITY, repeats=REPEATS, warm_threshold=threshold, scenarios=[])
    print(f'CAPACITY SCENARIOS | index 100 = historical median | limit {CAPACITY:g}')
    print(f'{len(load)} complete days | 144 readings/day | {REPEATS:,} simulated days/method')
    print('group          growth seed   block%   iid%   empirical% hours/day')
    for group, days in groups.items():
        for growth in [0.0, 0.10]:
            for seed in [42, 137, 2026]:
                r = simulate(days * (1 + growth), CAPACITY, seed)
                result['scenarios'].append(dict(group=group, days=len(days), growth=growth, seed=seed, **r))
                print(f'{group:14} {growth:5.0%} {seed:4} {100*r["block"]:8.2f} {100*r["iid"]:6.2f} {100*r["exact"]:10.2f} {r["hours"]:9.2f}')
    result['capacity_sweep'] = []
    for cap in [110, 125, 140, 155]:
        for growth in [0.0, 0.10]:
            risk = float((groups['all_days'] * (1 + growth) > cap).any(axis=1).mean())
            result['capacity_sweep'].append(dict(capacity=cap, growth=growth, empirical_risk=risk))
    (ROOT / 'results/metrics.json').write_text(json.dumps(result, indent=2))
    print('Scenario assumptions, not actual grid capacity or outage probabilities.')
    print('Whole-day sampling preserves within-day demand/weather patterns; no forecast claim.')
if __name__ == '__main__': main()
