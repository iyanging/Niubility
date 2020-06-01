from typing import TypeVar, Type, Dict

from .exception import NoSuchStubTypeError, NoSuchStubValueError, StubAlreadyExistsError
from .field_meta import FieldMeta

T = TypeVar('T')


class MetaCan:
    """保存field元信息的容器

    type -> { typed value -> meta info },
    """

    def __init__(self):
        self.can: Dict[Type[T], Dict[T, FieldMeta]] = {}

    def new_stub(self, t: Type[T]) -> T:
        """创建一个stub用于占位，并返回相应的占位值

        :param t: 用于占位的类型
        :return: 占位值
        """
        pass  # TODO:

    def put(self, stub: T, meta: FieldMeta) -> None:
        """将field元信息放入容器

        :param stub: 占位值
        :param meta: field元信息
        :raises NoSuchStubTypeError: stub的类型未被注册
        """
        typed_can = self.can.get(type(stub))  # 不知道为什么写成"if typed_can := ..."在PyCharm里会丢失类型信息
        if typed_can is None:
            raise NoSuchStubTypeError()  # TODO: 增加错误位置，哪一个model的哪一个field
        elif stub in typed_can:  # stub已经注册过了
            raise StubAlreadyExistsError()
        else:
            typed_can.setdefault(stub, meta)

    def get(self, stub: T) -> FieldMeta:
        """通过占位值取得field元信息

        :param stub: 占位值
        :return: field元信息
        :raises NoSuchStubTypeError: stub的类型未被注册
        :raises NoSuchStubValueError: stub占位值未被注册
        """
        typed_can = self.can.get(type(stub))

        if typed_can is None:
            raise NoSuchStubTypeError()  # TODO: 增加错误位置，哪一个model的哪一个field
        if meta := typed_can.get(stub) is None:
            raise NoSuchStubValueError()  # TODO: 增加错误位置，哪一个model的哪一个field
        else:
            return meta


metaCan = MetaCan()
