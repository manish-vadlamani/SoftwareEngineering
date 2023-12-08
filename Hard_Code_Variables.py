import matplotlib.pyplot as plt

def quadratic_weather_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    a = 0.2
    b = -2
    c = 25
    time_values = list(range(0, 11))
    temperature_values = [quadratic_weather_model(t, a, b, c) for t in time_values]

    plt.figure(figsize=(8, 6))
    plt.plot(time_values, temperature_values, marker='o', linestyle='-')
    plt.title('Temperature Variation Over Time using Hard Coding Variables')

    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.grid(True)
    plt.xlim(0, 10)
    plt.ylim(min(temperature_values) - 5, max(temperature_values) + 5)
    plt.show()

if __name__ == "__main__":
    main()