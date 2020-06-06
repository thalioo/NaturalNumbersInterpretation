import re
import itertools
pattern_with_spaces = "^(0\s*0\s*3\s*0\s*)"

class PhoneNumber():

    #lambda function for validating a number
    __y = lambda self, a: True if ((a.startswith(("00302", "003069"))
                                   and len(a) == 14)
                                   or (a.startswith(("2", "69"))
                                   and len(a) == 10)) else False

    def __init__(self, num):
        self.full_number_str = num
        self.full_number_tokens = num.split(" ")
        self.set_prefix
        self.set_sufix
        self.number_suffix_tokens = self.number_suffix_str.strip().split(" ")

    @property
    def set_prefix(self):
        match = re.match(pattern_with_spaces, self.full_number_str)
        if match:
            self.number_prefix_str = match.group().replace(" ", "")
        else:
            self.number_prefix_str = ''

    @property
    def set_sufix(self):
        self.number_suffix_str = re.sub(pattern_with_spaces, "",
                                        self.full_number_str)

    def basic(self):
        ''' Basic Level. Idintifies if a number is valid Greek number
        Returns
        -------
        tuple (str,str)
            A tuple of the concated number and VALID or INVALID.

        '''
        concated_number = self.number_prefix_str + ''.join(self.number_suffix_tokens)
        return self.__validation(concated_number)

    def __validation(self, concated_number):
        if self.__y(concated_number):
            valid = "VALID"
        else:
            valid = "INVALID"
        return concated_number, valid

    def advanced(self):
        """ Advanced Level. Identifies possible number ambiguities and their
        basic validation.
        Each possible interpretation is then passed to basic level to identify
        if it is valid number.

        Returns
        -------
        validations : list of tuples (str,str).
            Tuple is obtained from basic level.
        """

        solutions = self.__advanced_concat()
        validations = []
        for solution in solutions:
            validations.append(self.__validation
                               (self.number_prefix_str + solution))
        return validations

    def __first_level_merge(self):
        """ Performs the first level merge.
        Parameters
        ----------
        subs : list of str
            The suffix sequences list.

        Returns
        -------
        version : list
            DESCRIPTION.

        """
        subs = self.number_suffix_tokens
        version = [subs[0]]
        j = 0
        for i in range(1, len(subs)):
            x = self.__merge(version[j], subs[i])[0]
            if (len(x) > 3 or (len(version[j]) == 1)
                or int(version[j]) == 0
                    or not version[j].endswith('0' * len(subs[i]))):
                version.append(subs[i])
                j += 1
            else:
                # version.remove(version[j])
                del version[j]
                version.append(x)
        return version

    def __merge(self, s1, s2):
        """ Performs the mergings of s1 and s2
        Parameters
        ----------
        s1 : str
            sequence of numbers.
        s2 : str
            sequence of numbers.

        Returns
        -------
        list
            list of merged sequences.

        """
        zero_padding = len(s1) - len(s1.lstrip('0'))
        y = int(s1+s2)
        x = ''
        if s1.endswith('0' * len(s2)):
            x = int(s1) + int(s2)
            if y <= x:
                x = ''
            elif zero_padding > 0:
                x = zero_padding*'0'+str(x)

        return [str(x), s1+s2] if str(x) else [s1+s2]

    def __expand(self, s):
        """ Expands a single sequence of numbers

        Parameters
        ----------
        s : str
            sequence of numbers.

        Returns
        -------
        list
            List of all possible exapnds of s.

        """

        if len(s) == 1:
            return [s]
        elif len(s) == 2:
            return [s] if '0' in s or s == '11' or s == '12' else [s, s[0]+'0'+s[1]]
        # elif s.endswith('00'):
        #     return [s]
        else:
            if s.endswith('00'):
                return [s]
            partial_solution = self.__expand(s[1:])
            solution = []
            for item in partial_solution:
                solution += [s[0]+item]
                if s[0] != '0':
                    prefix = '0' if item.startswith('0') else '00'
                    solution += [s[0]+prefix+item]
            return solution

    def __advanced_concat(self):
        """ Performs the concatanation of valid merges and expands.
        Returns
        -------
        solutions : list
            A list of all the phone number ambiguities.

        """
        self.number_suffix_tokens = self.__first_level_merge()
        expanded_nums = {idx: self.__expand(seq)
                         for idx, seq in enumerate(self.number_suffix_tokens)}

        solutions = set(''.join(x) for x in itertools.product(
                                                *list(expanded_nums.values())))
        return solutions
