#!/usr/bin/env python
#
# Pandas-based Data Frame Handlers DNA-sequencing
# https://github.com/dceoy/pandna

from abc import ABCMeta, abstractmethod
import os
import pandas as pd


class BaseBioDataFrame(object, metaclass=ABCMeta):
    def __init__(self, path, supported_exts=[]):
        if os.path.isfile(path):
            self.path = path
        else:
            raise BioDataFrameError('file not found: {}'.format(path))
        exts = [x for x in supported_exts if path.endswith(x)]
        if not supported_exts:
            self.ext = None
        elif exts:
            self.ext = exts[0]
        else:
            raise BioDataFrameError('invalid file extension: {}'.format(path))
        self.df = pd.DataFrame()

    @abstractmethod
    def load(self):
        pass

    def load_and_output_df(self):
        self.load()
        return self.df

    def write_df(self, path, mode='w', **kwargs):
        if self.header:
            with open(path, mode=mode) as f:
                for h in self.header:
                    f.write(h + os.linesep)
        self.df.to_csv(path, mode=('a' if self.header else 'w'), **kwargs)


class BioDataFrameError(RuntimeError):
    pass
