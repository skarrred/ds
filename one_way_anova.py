import scipy.stats as stats

# Class exam scores
class_a = [85, 90, 88, 82, 87]
class_b = [76, 78, 80, 81, 75]
class_c = [92, 88, 94, 89, 90]

# Combine data into a single list
all_scores = class_a + class_b + class_c

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(class_a, class_b, class_c)

# Set significance level (alpha)
alpha = 0.05

# Interpret results
if p_value < alpha:
    print("Reject null hypothesis (H0). There is a statistically significant difference (p-value =", p_value, ") in average exam scores between the classes.")
else:
    print("Fail to reject null hypothesis (H0). There is not enough evidence (p-value =", p_value, ") to conclude a significant difference in average scores between the classes.")

