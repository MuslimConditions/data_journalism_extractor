""" The union operation module
"""
import os
from jinja2 import Environment
from extractor_exceptions import IntegrityError
from .binary_operation import BinaryOperation


class Union(BinaryOperation):
    """ A module that does a union of two incoming data flows.
    """
    def __init__(self, module, env: Environment, named_modules):
        super().__init__(module, env, named_modules)

        self.template_path = os.path.join(self.template_path,
                                          'scala_union.template')

        self.template = self.env.get_template(self.template_path)

    def rendered_result(self) -> (str, str):
        return self.template.render(
            name=self.name,
            source1=self.source1,
            source2=self.source2,
        ), ''

    def get_out_type(self):
        # Equality is checked during integrity test
        return self.named_modules.get(self.source1).get_out_type()

    def check_integrity(self):
        type1 = self.named_modules.get(self.source1).get_out_type()
        type2 = self.named_modules.get(self.source2).get_out_type()

        if type1 != type2:
            raise IntegrityError(
                "Trying to make a union on two flows with" +
                " different types in module {}:\n\t{}\n\t{}".format(
                    self.name, type1, type2))