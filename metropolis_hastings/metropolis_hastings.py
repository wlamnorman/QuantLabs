import random
from typing import Callable


class MetropolisHastings:
    def __init__(
        self,
        state: float,
        target_pdf: Callable[..., float],
        proposal_pdf: Callable[..., float],
        proposal_pdf_is_symmetric: bool = False,
    ):
        self.state = state
        self.target_pdf = target_pdf
        self.proposal_pdf = proposal_pdf
        self._symmetric_proposal_pdf = proposal_pdf_is_symmetric
        self._samples = [state]
        self._accepted = 0

    def sample_posterior(self, n: int):
        for _ in range(n):
            self.transition()

    def transition(self):
        candidate = self.proposal_pdf(self.state)
        if self._symmetric_proposal_pdf:
            acceptance_ratio = min(
                1, self.target_pdf(candidate) / self.target_pdf(self.state)
            )
        else:
            acceptance_ratio = min(
                1,
                (
                    self.target_pdf(candidate)
                    / (self.target_pdf(self.state))
                    * (
                        self.proposal_pdf(self.state, candidate)
                        / self.proposal_pdf(candidate, self.state)
                    )
                ),
            )

        if random.uniform(0, 1) < acceptance_ratio:
            self._accepted += 1
            self.state = candidate

        self._samples.append(self.state)

    def get_samples(self) -> list[float]:
        return self._samples

    def acceptance_rate(self) -> float:
        return self._accepted / len(self._samples)

    def thinning(self, k: int):
        """Take every `k`th sample to reduce autocorrelation."""
        self._samples = self._samples[::k]

    # TODO: Add visualisation as in https://exowanderer.medium.com/metropolis-hastings-mcmc-from-scratch-in-python-c21e53c485b7
    # with source code at https://github.com/exowanderer/medium_tutorials/blob/Bayesian/BayesianInference/MCMCFromScratch/MCMC_From_Scratch.ipynb
    # TODO: Add tests of convergence
    # TODO: Add test of autocorrelation
    # TODO: Add a nice way of handling burn-in
