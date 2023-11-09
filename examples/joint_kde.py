"""
Joint kernel density estimate
=============================

_thumb: .6, .4
"""
# %%
import seaborn as sns
import test0
import test2

sns.set_theme(style="ticks")

# Load the penguins dataset
penguins = sns.load_dataset("penguins")

# 추가된 함수 적용해보기
print(test0.testing_case_1())
# test2.user_test1()

# print(test1.test2())
# print(test1.test3())

# Show the joint distribution using kernel density estimation
g = sns.jointplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="species",
    kind="kde",
)


# %%
