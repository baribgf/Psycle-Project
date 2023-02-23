
"""
# Psycle v1.0
A module to work with the psycle object, which is a data structure like Circular Linked List.
"""

from __future__ import annotations

from collections.abc import Iterator
from collections.abc import Iterable

from typing import NewType as _new_type
from typing import Type as _type
from typing import Callable
from typing import Any

from .res.pyshs import styled

Item = _new_type('_item', _type)
SupportsIterating = _new_type("_SupportsIterating", _type)

def _override_exception_msg(exception: Exception, *messages):
    exception.args = messages
    return exception

class Node:
    def __init__(self, value, next = None) -> None:
        self.__value: Any = value
        self.__next: self = next

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_next(self) -> Node:
        return self.__next

    def set_next(self, node: Node):
        self.__next = node

    def __str__(self) -> str:
        return str(self.__value)

class Psycle(tuple):
    """Main Psycle object"""

    def __init__(self, *args, **kwargs) -> None:
        """
        Main Psycle object

        Args:
            * `init_arr`: the initialization arrary, leave 'None' for later initialization
        """

        self.__last_node: Node     = None
        self.__buffer: tuple[Node] = ()

        try:
            if args[0] is not None:
                self.from_of(args[0])

            elif kwargs.get('init_arr') is not None:
                self.from_of(kwargs.get('init_arr'))
        except IndexError:
            pass

    def attach_at(self, index: int, value) -> None:
        """Attach / Add a new node at index to object"""

        if not self.is_empty():
            try:
                if index < 0 and self.size() + index + 1 >= 0:
                    index = self.size() + index + 1

                pre  = self.__buffer[index - 1]
                post = pre.get_next()
                new  = Node(value, post)

                pre.set_next(new)
                new.set_next(post)

                self.__buffer = (*self.__buffer[:index], new, *self.__buffer[index:])

            except TypeError as e:
                raise _override_exception_msg(e, f'index must be an integer, got: \'{index}\'')

            except IndexError as e:
                raise _override_exception_msg(e, f'Index must be in range [0 .. size], got index: {index}, size: {self.size()}')

        else:
            self.head = Node(value, None)
            self.head.set_next(self.head)
            self.__last_node = self.head
            self.__buffer = (*self.__buffer, self.head)

    def attach(self, value):
        """Attach / Add a new node at the end of object"""
        self.attach_at(self.size(), value)

    def detach_at(self, index: int) -> None:
        """Detach / Remove a node at index from object and return it's value"""

        try:
            if index < 0 and self.size() + index >= 0:
                index = self.size() + index

            detached = self.__buffer[index]
            pre      = self.__buffer[index - 1]
            post     = detached.get_next()

            pre.set_next(post)
            self.__buffer = (*self.__buffer[:index], *self.__buffer[index + 1:])

            return detached

        except TypeError as e:
            raise _override_exception_msg(e, f'index must be an integer, got: \'{index}\'')

        except IndexError as e:
            raise _override_exception_msg(e, f'Index must be in range [0 .. size[, got index: {index}, size: {self.size()}')

    def detach(self):
        """Detach / Remove a node from the end of object and return it's value"""
        return self.detach_at(self.size() - 1)

    def next(self) -> Node:
        """Get next node"""

        last_node = self.__last_node
        self.__last_node = last_node.get_next()
        return last_node

    def get_at(self, index):
        """Get a specific node at index"""
        return self.__buffer[index].get_value()

    def size(self):
        """Get size of object"""
        return len(self.__buffer)

    def is_empty(self) -> bool:
        """Check whether object is empty"""
        return self.size() == 0

    def from_of(self, init_arr: SupportsIterating):
        """Create a Psycle object from an iterable"""
        if isinstance(init_arr, Iterable):
            for i in init_arr:
                self.attach(i)

        else:
            raise TypeError(f"'init_arr' must be an iterable, got: {init_arr}")

    def foreach(self, handler: Callable[[Item], Any]):
        """Foreach method to iterate over all object items"""
        for i in self.__buffer:
            handler(i)

    def __iter__(self) -> Iterator:
        return [i.get_value() for i in self.__buffer].__iter__()

    def __str__(self) -> str:
        rep = ""
        rep += "[ "

        for i in self.__buffer:
            item = i.get_value()

            if isinstance(item, str):
                rep += f"'{item}'"
            else:
                rep += str(item)

            if i != self.__buffer[-1]:
                rep += styled(' > ', fg='blue')
            else:
                rep += styled(' @', fg='red')

        rep += " ]"
        return rep
