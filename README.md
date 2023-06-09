# PHSX815_Week12

This assignment uses Gaussian Kernel density estimation to 
model a Gaussian mixture model. The mixture model is made
of two Gaussian distributions with `mean_1 = 1` and `mean_2 = 5`.
The standard deviation of both of these distributions is 1. 
<br/>
To run, type `python3 generate_and_analyze_data.py` <br/>
The probability of first distribution being chosen is `0.4`, and naturally, 
the probability of second distribution being chosen is `0.6`. These parameters
are defined conveniently in `generate_and_analyze_data.py` as `mean_list = [1, 5]`
, `weight_list = [0.4, 0.6]`. 
<br/>
In `main()` of `generate_and_analyze_data.py`, first the multimodal data is generated. Next, `mixed_gaussian_prob()` gets the true values of the multimodal distribution for
a given range (taking min and max of the generated data) using analytic expression. `get_gaussian_estimate()` gets the
Gaussian kernel density estimate of each point - summing up Gaussian 
contributions at a point with respect to every other point.
<br/>
Finally, these three distributions are plotted.
<br/>
`H = 2.0` is the standard deviation chosen for the Gaussian kernel. As `H` increases, it is expected
that the `get_gaussian_estimate()` smoothens out and all values become likely since contribution of any point
on any other point will be "faded".  
<br/>
The plots containing the simulated values (as histogram), true values (using analytic method) and predicted values (
using Gaussian kernel estimation) are shown in `histogram_generated_h_{H}.png`
where H is varied. 
<br/>
It can be seen that as H decreases, the predicted values distribution become more "localized". 
As H increases, the predicted values distribution becomes more smoothened. 
<br/>
Value of H = 0.25 and H = 0.5 seems to give the best results as they are not too localized and not too uniform.
