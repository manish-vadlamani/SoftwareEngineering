import matplotlib.pyplot as plt

fix_a = 0.1
fix_b = -2
fix_c = 25


def quadratic_weather_model(time, a, b, c):
  temperature = a * (time**2) + b * time + c
  return temperature

def main():
  try:
    user_a = float(input("Enter coefficient 'a': "))
    user_b = float(input("Enter coefficient 'b': "))
    user_c = float(input("Enter coefficient 'c': "))

    time_values = list(range(0, 11))

    temperature_fixed = [
        quadratic_weather_model(t, fix_a, fix_b, fix_c) for t in time_values
    ]
    temperature_user = [
        quadratic_weather_model(t, user_a, user_b, user_c) for t in time_values
    ]

    plt.figure(figsize=(8, 6))
    plt.plot(time_values,
             temperature_fixed,
             marker='o',
             linestyle='-',
             label="Fixed Coefficients")
    plt.plot(time_values,
             temperature_user,
             marker='o',
             linestyle='-',
             label="User Coefficients")
    plt.title('Temperature Variation Over Time with Hardcoded and User Input')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.grid(True)
    plt.xlim(0, 10)
    plt.legend()
    plt.show()

  except ValueError:
    print("Please enter valid numeric values for coefficients.")


if __name__ == "__main__":
  main()
