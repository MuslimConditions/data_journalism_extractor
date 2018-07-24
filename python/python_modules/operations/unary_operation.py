""" The abstract class for unary operation modules.
"""
from abc import ABC, abstractmethod
from graphviz import Digraph
from . import BaseModule


class UnaryOperation(BaseModule, ABC):
    """ An unary operation module must have a source.
    """
    def __init__(self, module, env, named_modules):
        super().__init__(module, env, named_modules)
        self.source = module.get('source')

        if self.source is None:
            raise ValueError(
                'The source was not provided in module {}'.format(module))

        self.template_path = 'operations'

    @abstractmethod
    def rendered_result(self) -> (str, str):
        pass

    def add_to_graph(self, graph: Digraph):
        super().add_to_graph(graph)

        graph.edge(self.source, self.__str__())
