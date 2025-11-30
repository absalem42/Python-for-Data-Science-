from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Main function to display life expectancy data for France."""
    data = load("life_expectancy_years.csv")
    if data is None:
        return

    # Filter data for France
    uae_data = data[data["country"] == "United Arab Emirates"]
    if uae_data.empty:
        print("Error: Country 'United Arab Emirates' not found in the dataset")
        return

    # Get years and life expectancy values
    years = data.columns[1:].astype(int)
    life_expectancy = uae_data.iloc[0, 1:].values

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(years, life_expectancy)
    plt.title("France Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.xticks(range(1800, 2101, 40))
    plt.show()


if __name__ == "__main__":
    main()
