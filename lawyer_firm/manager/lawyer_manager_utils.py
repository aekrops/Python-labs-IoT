import doctest
from lawyer_firm.classes.lawyer import Lawyer
from lawyer_firm.classes.sort_type import SortType


class LawyerManagerUtils:

    def __init__(self, lawyers_list=None):
        if lawyers_list is None:
            self.lawyers_list = []
        else:
            self.lawyers_list = lawyers_list

    def __del__(self):
        return

    def sort_lawyers_by_name(self, type_of_sort: str):
        # python -m doctest -v D:\github\python-labs-IoT\lawyer_firm\manager\lawyer_manager_utils.py
        """
        >>> law1 = Lawyer('Sebastian', 12, 100, True, False, False)
        >>> law2 = Lawyer('Max', 13, 200, False, True, False)
        >>> law3 = Lawyer('Andrey', 15, 300, False, True, True)
        >>> law4 = Lawyer('Denys', 16, 100, False, True, False)
        >>> law5 = Lawyer('Nazar', 17, 123, False, False, True)
        >>> law6 = Lawyer('Roman', 19, 321, True, True, False)
        >>> lawyers = [law1, law2, law3, law4, law5, law6]
        >>> manager_utils = LawyerManagerUtils(lawyers)
        >>> sorted_lawyers = manager_utils.sort_lawyers_by_name(SortType.ASCENDING.value)
        >>> for lawyer in sorted_lawyers: print(lawyer.name)
        Andrey
        Denys
        Max
        Nazar
        Roman
        Sebastian
        >>> sorted_lawyers = manager_utils.sort_lawyers_by_name(SortType.DESCENDING.value)
        >>> for lawyer_1 in sorted_lawyers: print(lawyer_1.name)
        Sebastian
        Roman
        Nazar
        Max
        Denys
        Andrey
        """
        sorted_lawyers = sorted(self.lawyers_list, key=lambda lawyer: lawyer.name)
        if type_of_sort == 'ascending':
            return sorted_lawyers
        elif type_of_sort == 'descending':
            return sorted_lawyers[::-1]
        else:
            return sorted_lawyers

    def sort_lawyers_by_number_of_service(self, type_of_sort: str):
        """
        >>> law1 = Lawyer('Sebastian', 12, 100, True, False, False)
        >>> law2 = Lawyer('Max', 13, 200, False, True, True)
        >>> law3 = Lawyer('Andrey', 15, 300, False, True, True)
        >>> law4 = Lawyer('Denys', 16, 100, True, True, True)
        >>> law5 = Lawyer('Nazar', 17, 123, False, False, True)
        >>> law6 = Lawyer('Roman', 19, 321, True, True, False)
        >>> lawyers = [law1, law2, law3, law4, law5, law6]
        >>> manager_utils = LawyerManagerUtils(lawyers)
        >>> sorted_lawyer = manager_utils.sort_lawyers_by_number_of_service('ascending')
        >>> for lawyer in sorted_lawyer: print(lawyer.name)
        Sebastian
        Nazar
        Max
        Andrey
        Roman
        Denys
        >>> sorted_lawyers = manager_utils.sort_lawyers_by_number_of_service('descending')
        >>> for lawyer in sorted_lawyers: print(lawyer.name)
        Denys
        Roman
        Andrey
        Max
        Nazar
        Sebastian
        """
        sorted_lawyers = sorted(self.lawyers_list, key=lambda lawyer: (len(lawyer.services)))
        if type_of_sort == 'ascending':
            return sorted_lawyers
        elif type_of_sort == 'descending':
            return sorted_lawyers[::-1]


if __name__ == "__main__":
    doctest.testmod(verbose=True)


