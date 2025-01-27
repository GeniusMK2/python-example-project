from .process import Process


class Project:

    def __init__(self, options):
        self.options = options
        self.process = Process()

    """
     Features can be presented here.
    """

    def date(self):
        return self._get_date()

    def _get_date(self):
        # prints stdout of subprocess with command "date"
        # strips tailing end-of-lines because print adds one
        return self.process.execute("date").rstrip('\n')

    def print_example_arg(self):
        return self.options.known.example
