from mydoc.core.facts import AtomicFact
from mydoc.core.rules import BasicRule
from mydoc.config.mapping import DEFAULT_MAPPING


class ConditionNotSupported(Exception):
    pass


def apply_conditon_from_rule(rule: BasicRule) -> bool:
    if rule.condition not in DEFAULT_MAPPING.keys():
        raise ConditionNotSupported(
            f"{rule.condition} not supported. Supported Condition are: {DEFAULT_MAPPING.keys()}"
        )

if __name__ == '__main__':
    f = AtomicFact('beni', 23)
    r = BasicRule()
    r.predicate = f
    r.condition = 'is_not'
    r.conclusion = 'bravo'

    apply_conditon_from_rule(r)