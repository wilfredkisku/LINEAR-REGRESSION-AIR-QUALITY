
# Air Quality Prediction (Linear Regression)
## Problem Statement
We need to model a predictive learning model to estimate the future dated values of the pollutants such as O<sub>3</sub>, PM<sub>2.5</sub> and SO<sub>2</sub>. The most important aspect is to get an idea of the dataset and extract useful information that can be processed by the system for its training. This makes it imperative to pre-process and remove redundant information from the dataset. Also, the dataset should be free from inconsistencies such as missing data points, multiple data points, incoherent data points between the AQS dataset and the MesoWest dataset.

## Preprocessing
<ul>
  <li>There were two datasets that has to be accessed and consolidated, the MesoWest dataset for the features and the AQS dataset to obtain the particulate matter concentration in the air.</li>
  <li>The Datasets had a missing and uncomputable values such as <tt>’NA’</tt>, <tt>’N/A’</tt>, <tt>’na’</tt>, <tt>’n/a’</tt>, <tt>’--’</tt>, <tt>’-’</tt>, <tt>Null</tt> being some of the most common missing values in the dataset.</li>
  <li>The complete matrix contain the X matrix (D features + 1 bias) concatinated with the output vector Y. So the matrix would be of the dimension m × D+2, where m is the total number of samples (or) rows in the matrix (data points).</li>
</ul>

## Model Description
A linear hypothesis is selected as the prediction is to made over a range of real values R. The hypothesis is h<sub>w</sub>(x). A cost function is to be calculated to penalize the hypothesis as to obtain the correct set of parameters w.

<a href="https://www.codecogs.com/eqnedit.php?latex=J(w)&space;=&space;\frac{1}{2m}&space;\sum{(h_w(x)&space;-&space;y)^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(w)&space;=&space;\frac{1}{2m}&space;\sum{(h_w(x)&space;-&space;y)^2}" title="J(w) = \frac{1}{2m} \sum{(h_w(x) - y)^2}" /></a>

Weight update can be effected using the gradient descent expression:

<a href="https://www.codecogs.com/eqnedit.php?latex=w&space;:=&space;w_i&space;-&space;\eta&space;\frac{1}{m}\sum{(h_w(x)-y)&space;\times&space;x}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?w&space;:=&space;w_i&space;-&space;\eta&space;\frac{1}{m}\sum{(h_w(x)-y)&space;\times&space;x}" title="w := w_i - \eta \frac{1}{m}\sum{(h_w(x)-y) \times x}" /></a>

## Result
The plots are individual column value plots(altimeter, air temperature etc.) in relation with the concentrations of the pollutants. Since the models includes multiple features, it is multi-dimensional is nature making it hard to get a visual representation of the features in relation to the output concentration
of the pollutants.

It can be seen that the it would be very difficult to get a linear relation between the concentration of the pollutants, here below is the concentration of O<sub>3</sub>, with just a single meteorological data such as pressure, temperature or humidity. So including multiple features would make it easier to draw a relation between the output concentrations and the features.
