#/usr/bin/env python

from operator import itemgetter
from itertools import groupby
import ast

class FilterModule(object):
    def filters(self):
        return {
            'consecutive_groups': self.consecutive_groups
        }

    def consecutive_groups(self,data):
        if type(data) == str:
            iterable = ast.literal_eval(data)
        groups=[]
        for k,g in groupby(enumerate(data),lambda x:x[0]-x[1]):
            groups.append(list(map(itemgetter(1),g)))
        return groups
