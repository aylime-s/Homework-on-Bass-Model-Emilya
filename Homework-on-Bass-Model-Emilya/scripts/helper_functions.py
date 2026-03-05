import numpy as np

def bass_model(t, p, q, M, N0=None):
    """
    Bass diffusion model using cumulative approach:
        N[t] = N[t-1] + (p + q * N[t-1]/M) * (M - N[t-1])
    Parameters:
        t  : array-like, time periods
        p  : float, innovation coefficient
        q  : float, imitation coefficient
        M  : float, market potential
        N0 : float, initial adopters (optional, defaults to first data point)
    Returns:
        N : predicted cumulative adopters per time period
    """
    N = np.zeros_like(t, dtype=float)
    if N0 is None:
        N[0] = 0
    else:
        N[0] = N0
    dt = 1
    for i in range(1, len(t)):
        N[i] = N[i-1] + (p + q * N[i-1]/M) * (M - N[i-1]) * dt
    return N