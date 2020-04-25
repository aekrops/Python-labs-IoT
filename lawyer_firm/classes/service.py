class Service:

    def __init__(self, representation_in_court=None, advice=None, collecting_evidence=None):
        self.drafting_a_claim = True
        self.signing_a_contract = True
        self.representation_in_court = representation_in_court
        self.advice = advice
        self.collecting_evidence = collecting_evidence

    @staticmethod
    def create_list_of_services(representation_in_court: bool, advice: bool, collecting_evidence: bool):
        services = [representation_in_court, advice, collecting_evidence]
        services_name = ['representation_in_court', 'advice', 'collecting_evidence']
        result_service = []
        for enum in range(3):
            if services[enum]:
                result_service.append(services_name[enum])
        return result_service

    def __del__(self):
        return

    def __str__(self):
        drafting_a_claim = 'Drafting a claim: {}\n'.format(self.drafting_a_claim)
        signing_a_contract = 'Signing a contract: {}\n'.format(self.signing_a_contract)
        representation_in_court = 'Representation in court: {}\n'.format(self.representation_in_court)
        advice = 'Advice: {}\n'.format(self.advice)
        collecting_evidence = 'Collecting evidence: {}\n'.format(self.collecting_evidence)
        return drafting_a_claim + signing_a_contract + representation_in_court + advice + collecting_evidence


class Litigation(Service):

    def __init__(self, classification_of_the_court=None):
        self.classification_of_the_court = classification_of_the_court

    def __del__(self):
        return

    def __str__(self):
        classification_of_the_court = f'Classification of the court: {self.classification_of_the_court}'
        return classification_of_the_court


class ProtectionOfIntellectualProperty(Service):

    def __init__(self, kind_of_intellectual_property=None):
        self.kind_of_intellectual_property = kind_of_intellectual_property

    def __del__(self):
        return

    def __str__(self):
        kind_of_intellectual_property = f'Kind of intellectual property: {self.kind_of_intellectual_property}'
        return kind_of_intellectual_property


class LegalAssistance(Service):

    def __init__(self, kind_of_legal_assistance=None):
        self.kind_of_legal_assistance = kind_of_legal_assistance

    def __del__(self):
        return

    def __str__(self):
        kind_of_legal_assistance = f'Kind of legal assistance: {self.kind_of_legal_assistance}'
        return kind_of_legal_assistance
