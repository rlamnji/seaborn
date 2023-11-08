"""
Joint kernel density estimate
=============================

_thumb: .6, .4
"""
# %%
import seaborn as sns
sns.set_theme(style="ticks")

# Load the penguins dataset
penguins = sns.load_dataset("penguins")

# 추가된 함수 적용해보기
# a = sns.print_a()

# Show the joint distribution using kernel density estimation
g = sns.jointplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="species",
    kind="kde",
)
