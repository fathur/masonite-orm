class RegisterRelations:

    _morph_map = {}

    def __init__(self):
        pass

    def morph_map(self):
        return self._morph_map

    @classmethod
    def set_morph_map(cls, morph_map):
        cls._morph_map = morph_map
        return cls
