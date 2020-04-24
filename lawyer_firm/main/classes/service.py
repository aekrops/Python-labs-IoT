class Service:

    def __init__(self, representation_in_court, advice, collecting_evidence):
        self.drafting_a_claim = True
        self.signing_a_contract = True
        self.representation_in_court = representation_in_court
        self.advice = advice
        self.collecting_evidence = collecting_evidence

    def __del__(self):
        return

    def __str__(self):
        drafting_a_claim = 'Drafting a claim: {}\n'.format(
            self.drafting_a_claim)
        signing_a_contract = 'Signing a contract: {}\n'.format(
            self.signing_a_contract)
        representation_in_court = 'Representation in court: {}\n'.format(
            self.representation_in_court)
        advice = 'Advice: {}\n'.format(self.advice)
        collecting_evidence = 'Collecting evidence: {}\n'.format(
            self.collecting_evidence)
        return drafting_a_claim + signing_a_contract + representation_in_court + advice + collecting_evidence
