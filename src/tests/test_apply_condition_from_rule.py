from mydoc.helpers.condition_parser import apply_conditon_from_rule
from mydoc.core.rules import BasicRule
from mydoc.core.facts import AtomicFact

if __name__ == '__main__':
    f = AtomicFact('beni', 23)
    r = BasicRule()
    r.predicate = f
    r.condition = 'is_not'
    r.conclusion = 'bravo'

    apply_conditon_from_rule(r)

