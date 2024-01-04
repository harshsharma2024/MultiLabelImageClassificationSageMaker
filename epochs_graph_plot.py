import re
import matplotlib.pyplot as plt

def parse_log(log_file):
    epochs = []
    training_accuracies = []
    validation_accuracies = []

    with open(log_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Extract epoch, training, and validation accuracy information
        match_train = re.search(r'Epoch\[(\d+)\] Train-accuracy=([\d.]+)', line)
        match_val = re.search(r'Epoch\[(\d+)\] Validation-accuracy=([\d.]+)', line)
        
        if match_train:
            epoch = int(match_train.group(1))
            training_accuracy = float(match_train.group(2))
            epochs.append(epoch)
            training_accuracies.append(training_accuracy)
        elif match_val:
            epoch = int(match_val.group(1))
            validation_accuracy = float(match_val.group(2))
            # Ensure that the epoch exists in the list; sometimes, validation logs might come before training logs
            if epoch not in epochs:
                epochs.append(epoch)
                training_accuracies.append(None)  # Placeholder for missing training accuracy
            validation_accuracies.append(validation_accuracy)

    return epochs, training_accuracies, validation_accuracies

def plot_accuracy(epochs, training_accuracies, validation_accuracies, epoch_gap=30):
    # Include every epoch_gap-th epoch
    selected_epochs = epochs[::epoch_gap]
    selected_training_accuracies = training_accuracies[::epoch_gap]
    selected_validation_accuracies = validation_accuracies[::epoch_gap]

    plt.plot(selected_epochs, selected_training_accuracies, marker='o', label='Training Accuracy')
    plt.plot(selected_epochs, selected_validation_accuracies, marker='o', label='Validation Accuracy')
    plt.title('Training and Validation Accuracy with Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    log_file = "log_file.txt"  # Update with the actual path to your log file
    epochs, training_accuracies, validation_accuracies = parse_log(log_file)
    plot_accuracy(epochs, training_accuracies, validation_accuracies)
