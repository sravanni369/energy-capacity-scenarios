import unittest
import numpy as np
from energy_scenarios import simulate

class ScenarioTests(unittest.TestCase):
    def test_always_safe_and_always_above(self):
        self.assertEqual(simulate(np.ones((3,144)),2,42)['block'],0)
        self.assertEqual(simulate(np.ones((3,144))*3,2,42)['block'],1)
    def test_strict_exceedance(self):
        self.assertEqual(simulate(np.ones((3,144))*2,2,42)['block'],0)
    def test_known_dependence_case(self):
        r=simulate([[0,0],[2,2]],1,42,repeats=50000)
        self.assertEqual(r['exact'],.5)
        self.assertEqual(r['iid_exact'],.75)
        self.assertAlmostEqual(r['block'],.5,delta=.01)
        self.assertAlmostEqual(r['iid'],.75,delta=.01)
    def test_duration_conversion(self):
        self.assertEqual(simulate(np.ones((2,144))*2,1,42)['hours'],24)
    def test_monotone_capacity_with_common_scenarios(self):
        days=np.arange(144*3).reshape(3,144)
        self.assertGreaterEqual(simulate(days,100,42)['block'],simulate(days,200,42)['block'])
    def test_reproducibility(self):
        self.assertEqual(simulate([[0,2],[2,0]],1,42),simulate([[0,2],[2,0]],1,42))
    def test_invalid_input(self):
        for days in [[],[1,2],[[np.nan]],np.empty((2,0))]:
            with self.assertRaises(ValueError): simulate(days,1,42)

if __name__=='__main__': unittest.main(verbosity=2)
