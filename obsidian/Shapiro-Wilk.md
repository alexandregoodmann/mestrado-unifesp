To perform the Shapiro-Wilk test for normality, follow these steps:

1. **Collect Data**: Gather the dataset for which you want to test the normality assumption. Ensure that the data is quantitative and continuous.

2. **Arrange Data**: Organize your data in ascending order.

3. **Calculate Test Statistic (W)**: The Shapiro-Wilk test calculates a test statistic (W) that measures the degree of departure from normality. This statistic is based on the covariance between the observed data and the expected values under the assumption of normality.

4. **Calculate Critical Value**: Based on the sample size and significance level (typically 0.05), determine the critical value from the Shapiro-Wilk table or use statistical software to obtain it.

5. **Compare Test Statistic and Critical Value**: Compare the calculated test statistic (W) with the critical value. If the test statistic is less than the critical value, then there is no significant evidence to reject the null hypothesis of normality. However, if the test statistic is greater than the critical value, then you may reject the null hypothesis, indicating that the data significantly deviates from normality.

6. **Interpret Results**: Based on the comparison, make a conclusion regarding the normality assumption for your dataset. If the p-value associated with the test statistic is less than the chosen significance level (usually 0.05), you would reject the null hypothesis and conclude that the data is not normally distributed. Otherwise, you would fail to reject the null hypothesis, indicating that there is not enough evidence to suggest that the data significantly departs from a normal distribution.

7. **Report Findings**: Communicate the results of the Shapiro-Wilk test, including the test statistic, critical value, and the decision made regarding the normality assumption. This provides transparency and allows others to understand the validity of your data analysis.

Remember, the Shapiro-Wilk test is sensitive to sample size, so it might not be accurate for very large datasets. Additionally, while it's a useful tool, it's important to consider other diagnostic methods and the context of your data analysis when assessing normality.

-----------
## [[Python]] 
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html

--------------------

## Referências

http://www.de.ufpb.br/~ulisses/disciplinas/normality_tests_comparison.pdf
https://real-statistics.com/tests-normality-and-symmetry/statistical-tests-normality-symmetry/shapiro-wilk-test/

https://builtin.com/data-science/shapiro-wilk-test

https://www.sciencedirect.com/topics/mathematics/wilk-test

https://medium.com/@insufficient/is-it-normal-the-shapiro-wilk-normality-test-b11febde04c9

