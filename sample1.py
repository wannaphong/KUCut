# -*- coding: utf-8 -*-
from kucut import SimpleKucutWrapper as KUCut
myKUCut = KUCut()
result = myKUCut.tokenize(["ทดสอบทดสอบ"])
print("\n".join(
            ["\n".join(
                [" ".join(
                    [w for w in line])
                     for line in p])
                 for p in result]))
