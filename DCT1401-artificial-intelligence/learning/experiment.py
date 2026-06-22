import sys
import pandas as pd
from neuron import Perceptron

target = sys.argv[1]
if target not in ["iris_setosa", "iris_versicolor", "iris_virginica"]:
    print("Invalid target")
    sys.exit(1)

df = pd.read_csv("./irisflowers.csv")
# Shuffle the data
df = df.sample(frac=1).reset_index(drop=True)
# Drop class column
class_column = df.pop("class")

# Apply StandardScaler to normalize the data
for column in df.columns:
    df[column] = (df[column] - df[column].mean()) / df[column].std()

# Add class column back
df["class"] = class_column
df["class_num"] = df["class"].apply(lambda x: 1 if x == target else 0)

attrs = ["sepal_length", "sepal_width", "petal_length", "petal_width"]


neuron = Perceptron(
    X=df[attrs].values, Y=df["class_num"].values, learning_rate=0.001, bias=1.0
)

correct_count = [0]
error_count = [0]
iterations = 0

neuron.rand_weights()

# Plot and update the correct and error counts every 10 iterations

import matplotlib.pyplot as plt

plt.ion()

fig, ax = plt.subplots()
ax.plot(correct_count, label="Correct")
ax.plot(error_count, label="Error")
ax.set_xlabel("Iterations")
ax.set_ylabel("Count")
ax.legend()

ax.title.set_text(f"Target: {target}")

while neuron.changed:

    for i in range(len(df)):
        pred = neuron.compute_output(df[attrs].values[i])

        if pred == df["class_num"].values[i]:
            correct_count[iterations] += 1
        else:
            error_count[iterations] += 1
            neuron.learn()

    if correct_count[iterations] == len(df) or error_count[iterations] == 0:
        break
    else:
        if iterations % 5 == 0:
            line1 = ax.lines[0]
            line2 = ax.lines[1]

            line1.set_xdata(range(iterations + 1))
            line1.set_ydata(correct_count)
            line2.set_xdata(range(iterations + 1))
            line2.set_ydata(error_count)
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw()
            fig.canvas.flush_events()

            hit_std = pd.Series(correct_count[-5:]).std()
            miss_std = pd.Series(error_count[-5:]).std()

            print(
                f"Hit std: {hit_std} - Miss std: {miss_std}, LR: {neuron.learning_rate}\n",
                f"Correct: {correct_count[iterations]} - Error: {error_count[iterations]}\n",
            )

            # Update legend
            ax.title.set_text(
                f"Target: {target} - Correct: {correct_count[iterations]} - Error: {error_count[iterations]}"
            )

        neuron.learn()

    iterations += 1
    correct_count.append(0)
    error_count.append(0)

print(f"\t RESULT: Correct: {correct_count} - Error: {error_count}")

plt.ioff()
plt.show()
