from unittest import TestCase
from clorm import FactBase

from . import ClingoTest
from . import Terms

class TestDay(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()
        self.facts = FactBase([])

    def test_only_one_day_is_selected(self):
        self.facts.add(Terms.NumDays(num_days=1))
        self.load_knowledge(self.facts)

        possibilities = [
            Terms.Select(day="saturday"),
            Terms.Select(day="sunday"),
        ]

        solutions = self.get_solutions()

        for solution in solutions:
            query = list(solution.facts(atoms=True)
                .query(Terms.Select)
                .all()
            )

            self.assertTrue(len(query) == 1)
            self.assertIn(query[0], possibilities)
