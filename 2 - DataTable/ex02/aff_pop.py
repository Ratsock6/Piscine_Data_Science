import matplotlib.pyplot as plt
from load_csv import load


def parse_population(value: str) -> float:
    """
    Convert population string with suffix (M, B, k) to a float.

    For example: '65M' -> 65000000, '500k' -> 500000.
    """
    if isinstance(value, (int, float)):
        return float(value)
    value = str(value).strip()
    multipliers = {"B": 1e9, "M": 1e6, "k": 1e3}
    if value[-1] in multipliers:
        return float(value[:-1]) * multipliers[value[-1]]
    return float(value)


def plot_population(country1: str, country2: str) -> None:
    """
    Plot population projections for two countries from 1800 to 2050.

    Loads population_total.csv and displays a line chart
    with title, axis labels and a legend per country.
    """
    dataset = load("population_total.csv")
    if dataset is None:
        return

    all_years = dataset.columns[1:].astype(int)
    mask = (all_years >= 1800) & (all_years <= 2050)
    years = all_years[mask]

    for country in [country1, country2]:
        row = dataset[dataset["country"] == country]
        if row.empty:
            print(f"Error: country '{country}' not found.")
            return
        values = row.iloc[0, 1:].values[mask]
        values = [parse_population(v) for v in values]
        plt.plot(years, values, label=country)

    def format_population(x, _):
        """Format y-axis tick labels with M suffix."""
        return f"{int(x / 1e6)}M"

    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(format_population)
    )

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    """Entry point: compare population of France and Belgium."""
    plot_population("France", "Belgium")


if __name__ == "__main__":
    main()