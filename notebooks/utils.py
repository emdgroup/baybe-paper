import seaborn as sns
import pandas as pd
from pathlib import Path

sns.set_context("paper", font_scale=1.2)


def backtest_plot(
    df: pd.DataFrame,
    figure_name: str,
    y: str,
    hue: str,
    path: str = "../figures",
    x: str = "Num_Experiments",
    indicator_y: float | None = None,
    indicator_labels: list[str] | None = None,
):
    """Plot utility."""
    ax = sns.lineplot(
        data=df,
        marker="o",
        markersize=7,
        x=x,
        y=y,
        hue=hue,
    )
    ax.figure.set_size_inches(10, 6)

    if indicator_y is not None:
        indicator_labels = indicator_labels or df[hue].unique().tolist()

        xmax = 0.0
        for label in indicator_labels:
            label_data = df[df[hue] == label]
            grouped = label_data.groupby(x)[y].mean().reset_index()

            closest_point = grouped.iloc[(grouped[y] - indicator_y).abs().argmin()]
            closest_x = closest_point[x]  # .values[0]
            xmax = max(xmax, closest_x)

            ax.axvline(
                closest_x,
                color="grey",
                linestyle="--",
                ymax=(indicator_y - ax.get_ylim()[0])
                / (ax.get_ylim()[1] - ax.get_ylim()[0]),
            )

        ax.axhline(
            indicator_y, color="grey", linestyle="--", xmax=xmax / ax.get_xlim()[1]
        )

    output_path = Path(path, f"{figure_name}.svg")
    ax.figure.savefig(output_path, format="svg", transparent=True)
