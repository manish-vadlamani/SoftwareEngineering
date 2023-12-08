import matplotlib.pyplot as plt

def quadratic_weather_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    try:
        with open('MultipleVariablesInput.txt', 'r') as file:
            lines = file.readlines()

        time_values = list(range(0, 11)) 
        plt.figure(figsize=(8, 6))

        for line in lines:
            coefficients = line.split()
            a, b, c = map(float, coefficients)

            temperature_values = [quadratic_weather_model(t, a, b, c) for t in time_values]

            plt.plot(time_values, temperature_values, marker='o', linestyle='-', label=f'a={a}, b={b}, c={c}')

        plt.title('Temperature Variation Over Time with Multiple Set of variables')
        plt.xlabel('Time')
        plt.ylabel('Temperature')
        plt.grid(True)
        plt.xlim(0, 10)
        plt.legend()
        plt.show()

    except FileNotFoundError:
        print("File not found. Please make sure 'MultipleSetVariables.txt' exists.")

if __name__ == "__main__":
    main()