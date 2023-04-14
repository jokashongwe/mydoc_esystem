from mydoc.core.facts import AtomicFact

class BasicRule:
    predicate: AtomicFact
    condition: str
    conclusion: AtomicFact

    def apply(self) -> AtomicFact:
        """
            This function apply the condition to the predicate and 
            return  the result as AtomicFact
            :predicate AtomicFact
            :conclusion: str
            :condition: str (
                > greater_than
                >= greater_than_or_equal
                < less_than
                <= less_than_or_equal
                != different
                in in
                or or
                and and
                xor xor
                = is or equal
            )
        """
        