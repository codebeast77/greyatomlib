# Task 2: Find the confidence interval for the population mean given a sample distribution

In the class we calculated the confidence interval for `SalePrice`, lets try and make a similar one for `GrLivArea`, but this time we won't be using the population standard deviation (as it is not available in most cases).

*Note*: when not using the population standard deviation, find confidence interval as:

>$Estimate \pm (z-value) * (Standard Error)$

>$Standard Error = \sigma/\sqrt n$

where $\sigma$ is the sample standard deviation

## Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| sample | DataFrame | compulsory |  | sample data |


## Returns:

| Return | dtype | description |
| --- | --- | --- | 
| confidence_interval | tuple | lower(1st) and upper(2nd) limit of confidence interval returned as a tuple |
