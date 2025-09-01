# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model was created on 9/1/2025 by Matthew Zuniga-Mitchell. It is the first version of the model. The model is
a logistic regression model to predict whether or not a an individual has a salary of more than 50 thousand (value of 1)
or less then 50 thousand(value of 0).


## Intended Use
The primary intended use of this model is to identify individuals who make exactly 50 thousand or more.
The primary intended users of this model are students intrested in learning machine learning. This model is not
intended to provide the best possible preditions, just demenstrate the models capabiliies. 

## Training Data
The training data set utilized for this model is titled "Census Income" can can be found at 
https://archive.ics.uci.edu/dataset/20/census+income. This dataset was chosen because it 
includes several features that can be investigated and already has the income requirments seperated. 
The dataset was spilt into test and training sets and used for training and
evaluation of the model.
The preprocessing of the training dataset included seperating the categorical and numerical features,
encoding the categorical values, and scaling the numerical features.

## Evaluation Data
The evaluation dataset is the test set from the training data split. This dataset
followed the same preprocessing steps as the training data. This includes eperating the categorical and numerical features,
encoding the categorical values, and scaling the numerical features.


## Metrics
The metrics used for this model are Precision, Recall, and F1 score. 
The models metric performance values are:
    Precision: 74.14%
    Reacal: 60.20%
    F1 score: 66.45%

## Ethical Considerations
The "Census Income" data set does include some potentially sensitive information such as the "Age" and "Sex" columns.
This model is not intended to make decisions for human life and should not be used in such manner.
At this time, I have not identified any risks or harms from this model, but a final conclusion is unknown. 

## Caveats and Recommendations
One caveat in this modelf is that the training data included varying quanities of each sliced value.
For instance the "native-country" column value "Haiti" has only records. This leads the model to have very low metric scores for this data slice.
One recommendation for this model would be to collect more data for slices such as "Haiti"'s that have low record counts.