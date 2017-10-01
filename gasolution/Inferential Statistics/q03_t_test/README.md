# Task 3:  Hypothesis testing using t-test

In the class we tested if house prices in OldTown is different than the mean price. Lets now check if the Living Area (`GrLivArea`) is significantly different than the mean area.
>Null Hypothesis: The mean of Living area of houses in OldTown is the same as the population mean.

> Alternate Hypothesis: The mean of Living area of houses in OldTown is different than the population mean.

Test the above hypothesis at 95% significance level and return True if we reject the null hypothesis.

## Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df | DataFrame | compulsory |  | IOWA housing dataset |


## Returns:

| Return | dtype | description |
| --- | --- | --- |
| test_result | tuple | p-value and result of our t-test(true or false) |
