from enum import Enum


class ServiceType(Enum):
    DRAFTING_A_CLAIM = 'drafting_a_claim'
    SIGNING_A_CONTRACT = 'signing_a_contract'
    REPRESENTATION_IN_COURT = 'representation_in_court'
    ADVICE = 'advice'
    COLLECTING_EVIDENCE = 'collecting_evidence'
