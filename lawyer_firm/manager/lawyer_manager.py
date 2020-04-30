import doctest
from lawyer_firm.classes.lawyer import Lawyer
from lawyer_firm.classes.services_type import ServiceType


class LawyerManager:

    def __init__(self, lawyer_list=None):
        if lawyer_list is None:
            self.lawyer_list = []
        else:
            self.lawyer_list = lawyer_list

    def __del__(self):
        return

    def find_lawyers_by_service(self, service_to_find: ServiceType):
        # python -m doctest -v D:\github\python-labs-IoT\lawyer_firm\manager\lawyer_manager.py
        """
        >>> law1 = Lawyer('Sebastian', 12, 100, True, False, False)
        >>> law2 = Lawyer('Petro', 13, 200, False, True, False)
        >>> law3 = Lawyer('Max', 15, 300, False, True, True)
        >>> lawyers = [law1, law2, law3]
        >>> manager = LawyerManager(lawyers)
        >>> print(manager.find_lawyers_by_service(ServiceType.ADVICE.value))
        ['Petro', 'Max']
        >>> print(manager.find_lawyers_by_service(ServiceType.COLLECTING_EVIDENCE.value))
        ['Max']
        >>> print(manager.find_lawyers_by_service(ServiceType.REPRESENTATION_IN_COURT.value))
        ['Sebastian']
        """
        result_lawyers = []
        for lawyer in self.lawyer_list:
            for service in lawyer.services:
                if service == service_to_find:
                    result_lawyers.append(lawyer.name)
                else:
                    pass
        return result_lawyers


if __name__ == "__main__":
    doctest.testmod(verbose=True)
