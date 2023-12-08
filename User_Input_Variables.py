import matplotlib.pyplot as plt

def quadratic_weather_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    a = float(input("Enter the coefficient x^2:"))
    b = float(input("Enter the coefficient x:"))
    c = float(input("Enter the constant value:"))
    time_values = list(range(10, 21))
    temperature_values = [quadratic_weather_model(t, a, b, c) for t in time_values]

    plt.figure(figsize=(8, 6))
    plt.plot(time_values, temperature_values, marker='o', linestyle='-')
    plt.title('Temperature Variation Over Time using User Input')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.grid(True)
    plt.xlim(10, 20)
    plt.ylim(min(temperature_values) - 5, max(temperature_values) + 5)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()