import re
import matplotlib.pyplot as plt

def parse_log(log_file):
    epochs = []
    validation_accuracies = []

    with open(log_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Extract epoch and validation accuracy information
        match = re.search(r'Epoch\[(\d+)\] Validation-accuracy=([\d.]+)', line)
        if match:
            epoch = int(match.group(1))
            accuracy = float(match.group(2))
            epochs.append(epoch)
            validation_accuracies.append(accuracy)

    return epochs, validation_accuracies

def plot_validation_accuracy(epochs, accuracies, epoch_gap=30):
    # Include every epoch_gap-th epoch
    selected_epochs = epochs[::epoch_gap]
    selected_accuracies = accuracies[::epoch_gap]

    plt.plot(selected_epochs, selected_accuracies, marker='o')
    plt.title('Validation Accuracy with Epochs (Gap of 10)')
    plt.xlabel('Epochs')
    plt.ylabel('Validation Accuracy')
    plt.show()

if __name__ == "__main__":
    log_file = "log_file.txt"  # Update with the actual path to your log file
    epochs, validation_accuracies = parse_log(log_file)
    plot_validation_accuracy(epochs, validation_accuracies)
