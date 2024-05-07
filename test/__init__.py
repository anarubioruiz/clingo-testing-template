from clorm import monkey
monkey.patch() # must call this before importing clingo
from clingo import Control


class ClingoTest:
    def clingo_setup(self, *files):
        self.ctrl = Control(['--models=0'], unifier=[
            Terms.Day,
            Terms.Select,
            Terms.NumDays
            # ...
        ])

        if not files:
            self.ctrl.load("src/engine.lp")
            self.ctrl.load("src/knowledge.lp")
            return

        for f in files:
            self.ctrl.load(f)

    def load_knowledge(self, facts):
        self.ctrl.add_facts(facts)
        self.ctrl.ground([("base", [])])

    def get_solutions(self):
        return self.ctrl.solve(yield_=True)


from clorm import ConstantField, Predicate, IntegerField

class Terms:
    class NumDays(Predicate):
        num_days = IntegerField

    class Day(Predicate):
        day = ConstantField

    class Select(Predicate):
        day = ConstantField
