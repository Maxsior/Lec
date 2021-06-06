class ValueValidationError(Exception):
    def __init__(self, alias, values):
        self.alias = alias
        self.values = values

    def __str__(self):
        return f"Can't find appropriate value for call object '{self.alias}' in set [ {self.values} ]"
