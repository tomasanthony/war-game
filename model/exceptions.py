class CheatingError(Exception):
    """Someone is trying to cheat!"""


class InvalidDeckError(Exception):
    """This deck size is incompatible with the
    number of suits and card rankings."""
