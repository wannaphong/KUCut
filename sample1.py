# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from kucut import SimpleKucutWrapper as KUCut
myKUCut = KUCut()
result = myKUCut.tokenize([u"ทดสอบทดสอบ"])
print(u"\n".join(
            [u"\n".join(
                [u" ".join(
                    [w for w in line])
                     for line in p])
                 for p in result]))
