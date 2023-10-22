# Metropolis-Hastings
Given a target density $f$ on a state space $\mathcal{X}$ computable up to a normalising constant such that $\tilde{f}(x) \propto f(x)$ where the proposed target density $\tilde{f}$ is known, an ergodic Markov chain $X_t$ is constructed on $\mathcal{X}$ that is stationary, meaning that $X_t \sim f \implies X_{t+1} \sim f$, that is $X_t$ converges in distribution to $f$. The Markov chain is then a sequence of _dependent_ samples of the target distribution.

## The algorithm
Description and derivation to be added.


## How to use the class
```python
# example use of class
```


## Practical use
https://arxiv.org/pdf/1504.01896.pdf#page=15&zoom=100,116,272
### Burn-in
### Test for convergence:
1. Trace Plots
Visual inspection of trace plots can provide a quick idea. If the trace plot shows a good "mixing" of states and doesn't exhibit trends, that's a good sign.

2. Autocorrelation Plots
If the autocorrelation drops off quickly, that's another sign that the chain is mixing well.

3. Gelman-Rubin Diagnostic
This involves running multiple chains and comparing the variance within each chain to the variance between chains. Values close to 1 suggest convergence.

4. Effective Sample Size (ESS)
A high ESS relative to the total number of samples suggests that you have a lot of "effective" independent samples, another sign of good mixing and convergence.

5. Running Mean
Plotting the running mean of the samples can show whether the mean is stabilizing, which suggests convergence.

6. Geweke Test
Compares the mean of the first 10% and the last 50% of the samples. If the chain has converged, the two means should be similar.
### Autocorrelation: thinning and randomisation


