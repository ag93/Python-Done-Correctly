# -*- coding: utf-8 -*-
import sys

try:
    a+b
except:
#    print(sys.exc_info()[0])
#    print(sys.exc_info()[1])
#    print(sys.exc_info()[2].tb_lineno)
    print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                         sys.exc_info()[1],
                                         sys.exc_info()[2].tb_lineno))