import matplotlib.pyplot as plt
from load_csv import load


def plot_life_expectancy(country: str) -> None:
    """
    Plot the life expectancy over time for a given country.

    Loads life_expectancy_years.csv and displays a line chart
    with title and axis labels.
    """
    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        return

    row = dataset[dataset["country"] == country]
    if row.empty:
        print(f"Error: country '{country}' not found in dataset.")
        return

    years = row.columns[1:].astype(int)
    values = row.iloc[0, 1:].values.astype(float)

    plt.figure(figsize=(10, 6))
    plt.plot(years, values)
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.tight_layout()
    plt.show()


def main():
    """Entry point: display life expectancy chart for France."""
    plot_life_expectancy("France")

if __name__ == "__main__":
    main()