# stdlib
import uuid

# third party
import numpy as np

# syft relative
from ...passthrough import is_acceptable_simple_type
from ..tensor import AutogradTensor
from .op import Op


class ClipOp(Op):
    def forward(
        self, x: AutogradTensor, y: AutogradTensor, z: AutogradTensor
    ) -> AutogradTensor:
        self.x = x
        self.y = y
        self.z = z

    def _backward(self, grad: AutogradTensor, backprop_id: uuid.uuid4):
        if self.x.requires_grad:
            pass

        if self.y.requires_grad:
            pass

        if self.z.requires_grad:
            pass