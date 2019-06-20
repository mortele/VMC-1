"""Optimizer class."""


class Optimizer:
    """Docstring."""

    """The optimizer method runs through a whole Monte Carlo loop
    for each gradient descent iteration. Update of the variational
    parameter is done within the run_vmc file."""

    def __init__(self, learning_rate):
        """Docstring."""
        self.learning_rate = learning_rate

    def gradient_descent(self, alpha, derivative_energy):
        """Docstring."""
        new_alpha = alpha - self.learning_rate*derivative_energy

        return new_alpha
