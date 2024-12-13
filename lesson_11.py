#3
def chickenpox_by_sex(df):
    df = df.query("num_of_vaccinations > 0")
    grouped = df.groupby(["sex", "had_chickenpox"])
    counts = grouped.size().unstack(level="had_chickenpox").fillna(0)
    ratios = (counts[True] / (counts[True] + counts[False])).to_dict()
    return ratios
results = chickenpox_by_sex(df)
print(results)

#4
import pandas as pd
import scipy.stats as stats
def corr_chickenpox(df):
    corr, pval = stats.pearsonr(df["had_chickenpox_column"], df["num_chickenpox_vaccine_column"])
    return corr, pval
corr, pval = corr_chickenpox(df)
print("Correlation:", corr)
print("P-value:", pval)