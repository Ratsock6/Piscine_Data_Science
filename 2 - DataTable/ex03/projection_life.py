import matplotlib.pyplot as plt
from load_csv import load


def plot_projection(year: str) -> None:
    """
    Plot life expectancy vs GDP per capita for all countries in a given year.

    Loads income_per_person_gdppercapita_ppp_inflation_adjusted.csv and
    life_expectancy_years.csv, merges them on country, and displays a
    scatter plot with a logarithmic x-axis.
    """
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")

    if gdp is None or life is None:
        return

    if year not in gdp.columns or year not in life.columns:
        print(f"Error: year '{year}' not found in one of the datasets.")
        return

    gdp_year = gdp[["country", year]].rename(columns={year: "gdp"})
    life_year = life[["country", year]].rename(columns={year: "life"})

    merged = gdp_year.merge(life_year, on="country").dropna()

    plt.figure(figsize=(10, 6))
    plt.scatter(merged["gdp"], merged["life"], s=20)
    plt.xscale("log")
    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    ticks = [300, 1000, 10000]
    labels = ["300", "1k", "10k"]
    plt.xticks(ticks, labels)

    plt.tight_layout()
    plt.show()


def main():
    """Entry point: display life expectancy vs GDP scatter plot for 1900."""
    plot_projection("1900")


if __name__ == "__main__":
    main()