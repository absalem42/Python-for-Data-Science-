from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Main function to display population data for two countries."""
    data = load("population_total.csv")
    if data is None:
        return

    # Select countries to compare
    country1 = "United Arab Emirates"
    country2 = "France"
    
    # Filter data for both countries
    uae_data = data[data["country"] == country1]
    france_data = data[data["country"] == country2]
    
    if france_data.empty or uae_data.empty:
        print("Error: Country not found in dataset")
        return

    # Get years from 1800 to 2050
    years = data.columns[1:].astype(int)
    year_mask = (years >= 1800) & (years <= 2050)
    years = years[year_mask]
    
    # Get population values
    uae_pop = uae_data.iloc[0, 1:].values[year_mask]
    france_pop = france_data.iloc[0, 1:].values[year_mask]

    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(years, uae_pop, label=country1)
    plt.plot(years, france_pop, label=country2)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
