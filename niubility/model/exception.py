from ..exception import NiubilityError


class NoSuchStubTypeError(NiubilityError):
    pass


class NoSuchStubValueError(NiubilityError):
    pass


class StubAlreadyExistsError(NiubilityError):
    pass
