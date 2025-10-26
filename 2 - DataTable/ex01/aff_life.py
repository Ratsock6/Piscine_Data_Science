from load_csv import load
import matplotlib.pyplot as plt
import numpy as np

def aff_life(dataset):
    """
    Create a scatter plot showing the relationship between GDP per capita
    and life expectancy.

    Parameters:
    dataset (pd.DataFrame): The dataset containing 'GDP per capita' and
    'Life expectancy' columns.

    This function generates a scatter plot with GDP per capita on the x-axis
    and life expectancy on the y-axis.
    It displays the plot using matplotlib.
    """
    try:
        if dataset is None:
            raise AssertionError("The dataset is None")
        df = load("life_expectancy_years.csv")
        if df is None:
            raise AssertionError("Failed to load dataset")
        
        df.set_index('country', inplace=True)
        country = "United States"
        if country not in df.index:
            raise AssertionError(f"{country} not found in dataset")
        
        years = np.array(df.columns, dtype=int)
        values = np.array(df.loc[country], dtype=float)

        plt.plot(years, values, label=country)
        plt.title("Life Expectancy Over Years")
        plt.xlabel("Year")
        plt.xticks(years[::40])
        plt.ylabel("Life Expectancy (years)")
        plt.yticks(range(30, 91, 10))
        plt.legend()
        plt.tight_layout()
        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return

 
if __name__ == "__main__":
    data = load("life_expectancy_years.csv")
    aff_life(data)