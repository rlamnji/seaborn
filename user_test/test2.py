# %%
import seaborn as sns
import test1


def user_test1():
    g = sns.jointplot(
        data=test1.penguins,
        x="bill_length_mm", y="bill_depth_mm", hue="species",
        kind="kde",
    )


def user_test2():
    return "hi"
