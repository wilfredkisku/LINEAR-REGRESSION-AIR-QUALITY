
# Air Quality Prediction (Linear Regression)
## 
The model chosen is a simple linear regression model with training being carried out using gradient descent,
the number of samples are quite large as it has been sampled from the year 2008 to 2018.
In regression we would model a hypothesis that would be used to predict the output of the next days
concentration of SO2, PM2.5 and O3. A linear hypothesis is selected as the prediction is to made over a
range of real values R. The hypothesis is h<sub>w</sub>(x). A cost function is to be calculated to penalize the hypothesis
as to obtain the correct set of parameters w.
$$
J(w) = \frac{1}{2m} \Sum P(h_w(x) − y)^2
$$
The linear model hw(x) = w
T x = w0 + w1x1 + ... + wdxd, the parameters are to be adjusted to minimize the
cost J(w). One way of doing it is by gradient descent, where each iteration performs an update:
wi
:= wi − η
1
m
P(hw(x) − y)x
With each step of the gradient descent the parameters w comes closer to the optimal values that will achieve
the lost cost J(w).

\prod \bigcup \frac{\partial^2 {_{}}^{}}{\partial x^2}

$\text{S}_1(N) = \sum_{p=1}^N \text{E}(p)$

<a href="https://www.codecogs.com/eqnedit.php?latex=\prod&space;\bigcup&space;\frac{\partial^2&space;{_{}}^{}}{\partial&space;x^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\prod&space;\bigcup&space;\frac{\partial^2&space;{_{}}^{}}{\partial&space;x^2}" title="\prod \bigcup \frac{\partial^2 {_{}}^{}}{\partial x^2}" /></a>
