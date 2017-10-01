## Task 4:  Chi-Square test of Independence

Perform a chi-square test to test independence of variables `LandSlope` and `SalePrice` in the IOWA housing dataset. `SalePrice` isn't a categorical variable, but we can divide it into three categories - High, medium, low using pandas qcut [function](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html).

The function should return the result of the test at a 95% signifigance level.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df | DataFrame | compulsory |  | IOWA housing dataset |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| test_result | tuple | p-value and result of our chi2-test(true or false) |
