
# Air Quality Prediction (Linear Regression)
## Problem Statement
We need to model a predictive learning model to estimate the future dated values of the pollutants such as O<sub>3</sub>, PM<sub>2.5</sub> and SO<sub>2</sub>. The most important aspect is to get an idea of the dataset and extract useful information that can be processed by the system for its training. This makes it imperative to pre-process and remove redundant information from the dataset. Also, the dataset should be free from inconsistencies such as missing data points, multiple data points, incoherent data points between the AQS dataset and the MesoWest dataset.

## Preprocessing
<ul>
  <li>There were two datasets that has to be accessed and consolidated, the MesoWest dataset for the features and the AQS dataset to obtain the particulate matter concentration in the air.</li>
  <li>The Datasets had a missing and uncomputable values such as <tt>’NA’</tt>, <tt>’N/A’</tt>, <tt>’na’</tt>, <tt>’n/a’</tt>, <tt>’--’</tt>, <tt>’-’</tt>, <tt>Null</tt> being some of the most common missing values in the dataset.</li>
  <li>The complete matrix contain the X matrix (D features + 1 bias) concatinated with the output vector Y. So the matrix would be of the dimension m × D+2, where m is the total number of samples (or) rows in the matrix (data points).</li>
  <li></li>
</ul>
