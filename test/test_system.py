import pytest
import numpy as np
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))
from system import System  # noqa: 401


def test_system_wavefunction_2d():
    num_particles = 1
    num_dimensions = 2
    alpha = 1.0
    beta = 1.0
    a = 0.0
    s = System(num_particles, num_dimensions, alpha, beta, a)
    positions = np.zeros(shape=(num_particles, num_dimensions))
    x = 2.92858925782756
    y = 0.00925285752985
    positions[0, 0] = x
    positions[0, 1] = y

    wf = s.single_particle_function(positions)
    assert wf == pytest.approx(np.exp(-x**2 - y**2), abs=1e-14)

    for _ in range(50):
        alpha = np.random.uniform(1e-3, 10)
        s.alpha = alpha

        x = np.random.uniform(-20, 20)
        y = np.random.uniform(-20, 20)
        positions[0, 0] = x
        positions[0, 1] = y
        wf = s.single_particle_function(positions)
        assert wf == pytest.approx(np.exp(-alpha*(x**2 + y**2)), abs=1e-14)


def test_system_wavefunction_3d():
    num_particles = 1
    num_dimensions = 3
    alpha = 1.0
    beta = 1.0
    a = 0.0
    s = System(num_particles, num_dimensions, alpha, beta, a)
    positions = np.zeros(shape=(num_particles, num_dimensions))

    for _ in range(50):
        alpha = np.random.uniform(1e-3, 10)
        beta = np.random.uniform(1e-3, 10)
        s.alpha = alpha
        s.beta = beta

        x = np.random.uniform(-20, 20)
        y = np.random.uniform(-20, 20)
        z = np.random.uniform(-20, 20)

        positions[0, 0] = x
        positions[0, 1] = y
        positions[0, 2] = z
        wf = s.single_particle_function(positions)
        assert wf == pytest.approx(np.exp(-alpha*(x**2 + y**2 + beta*z**2)),
                                   abs=1e-14)


def test_system_derivative_psi_term_2d():
    num_particles = 1
    num_dimensions = 3
    alpha = 1.0
    beta = 1.0
    a = 0.0
    s = System(num_particles, num_dimensions, alpha, beta, a)
    positions = np.zeros(shape=(num_particles, num_dimensions))

    for _ in range(50):
        alpha = np.random.uniform(1e-3, 10)
        s.alpha = alpha

        x = np.random.uniform(-20, 20)
        y = np.random.uniform(-20, 20)

        positions[0, 0] = x
        positions[0, 1] = y
        wf = s.derivative_psi_term(positions)

        assert wf == pytest.approx((-x**2 - y**2), abs=1e-14)


def test_system_derivative_psi_term_3d():
    num_particles = 1
    num_dimensions = 3
    alpha = 1.0
    beta = 1.0
    a = 0.0
    s = System(num_particles, num_dimensions, alpha, beta, a)
    positions = np.zeros(shape=(num_particles, num_dimensions))

    for _ in range(50):
        alpha = np.random.uniform(1e-3, 10)
        beta = np.random.uniform(1e-3, 10)
        s.alpha = alpha
        s.beta = beta

        x = np.random.uniform(-20, 20)
        y = np.random.uniform(-20, 20)
        z = np.random.uniform(-20, 20)

        positions[0, 0] = x
        positions[0, 1] = y
        positions[0, 2] = z
        wf = s.derivative_psi_term(positions)

        assert wf == pytest.approx((-x**2 - y**2 - beta*z**2), abs=1e-12)
