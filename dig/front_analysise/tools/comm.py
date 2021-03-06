
class JSFile():
    def __init__(self, fpath, be_depend=None):
        if be_depend is None:
            be_depend = set()
        self.be_depend = be_depend
        self.fpath = fpath
        self.name = self.fpath.split("/")[-1]
    @property
    def be_depend_count(self):
        return len(self.be_depend)
    def add_depend(self, html_file):
        self.be_depend.add(html_file)
    def get_bedepend(self):
        return self.be_depend
    def __add__(self, other):
        return JSFile(self.fpath, self.be_depend | other.be_depend)