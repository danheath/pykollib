# Stubs for tortoise.exceptions (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

class BaseORMException(Exception): ...
class FieldError(BaseORMException): ...
class ParamsError(BaseORMException): ...
class ConfigurationError(BaseORMException): ...
class TransactionManagementError(BaseORMException): ...
class OperationalError(BaseORMException): ...
class IntegrityError(OperationalError): ...
class NoValuesFetched(OperationalError): ...
class MultipleObjectsReturned(OperationalError): ...
class DoesNotExist(OperationalError): ...
class DBConnectionError(BaseORMException): ...
