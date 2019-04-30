# coding: utf-8
# python 3.7.1 x86_64


class IterByBlockN:
    def __init__(self, obj, start:int=0, len_block:int=8):
        self.index = start
        self.len_block = len_block
        self.obj = obj
        self.len_obj = len(obj)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= self.len_obj:
            raise StopIteration
        ret = self.obj[self.index:self.index+self.len_block]
        self.index += self.len_block
        return ret
