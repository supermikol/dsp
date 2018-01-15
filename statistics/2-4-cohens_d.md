[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Cohen's D is an example of effect size. Other examples of effect size are: correlation between two variables, mean difference, regression coefficients and standardized test statistics such as: t, Z, F, etc. In this example, you will compute Cohen's D to quantify (or measure) the difference between two groups of data.

You will see effect size again and again in results of algorithms that are run in data science. For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

>> The Cohen's D comparing totalwgt_lb is `-0.088672927072602`. This means first babies are 0.089 standard deviations lighter than non-first babies. This value is very small, showing no significant meaning in weight difference. This insignificance is the same as with the case of pregnancy length, where the difference is negligible.
