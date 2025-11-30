from load_csv import load
import matplotlib.pyplot as plt


def convert_population(value):
    """Convert population string (like '3.28M' or '400k') to number."""
    if isinstance(value, str):
        value = value.strip()
        if value.endswith('M'):
            return float(value[:-1]) * 1e6
        elif value.endswith('k'):
            return float(value[:-1]) * 1e3
        else:
            return float(value)
    return float(value)


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
    
    # Get population values and convert to numbers
    uae_pop = [convert_population(x) for x in uae_data.iloc[0, 1:].values[year_mask]]
    france_pop = [convert_population(x) for x in france_data.iloc[0, 1:].values[year_mask]]

    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(years, uae_pop, label=country1)
    plt.plot(years, france_pop, label=country2)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    
    # Format y-axis to show values with M suffix (millions)
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))
    
    plt.show()


if __name__ == "__main__":
    main()
