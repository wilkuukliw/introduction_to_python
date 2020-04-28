# args.py

class MyRange:

    def __call__(self, *args):
        """  args: 10000000 skal tilføjes  """
        if len(args) == 1:
            self.start = 0
            self.end = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.end = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.end = args[1]
            self.step = args[2]
        return iter(self)
