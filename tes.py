import matplotlib.pyplot as plt
import random
import numpy as np

# Tentukan kelas yang ingin ditampilkan
target_class = 0

# Ambil indeks dari sampel di `y_test` yang sesuai dengan kelas target
indices_for_target_class = [i for i, label in enumerate(y_test) if label == target_class]

# Tentukan jumlah gambar yang ingin ditampilkan (maksimal 10 gambar)
num_samples_to_show = 10
# Ambil sampel acak dari indeks yang sesuai
selected_indices = random.sample(indices_for_target_class, min(num_samples_to_show, len(indices_for_target_class)))

# Hitung akurasi untuk kelas yang ditargetkan
def calculate_accuracy(y_true, y_pred, target_class):
    # Ambil indeks dari prediksi yang sesuai dengan kelas target
    correct_predictions = sum((y_pred[i] == y_true[i]) for i in range(len(y_true)) if y_true[i] == target_class)
    total_predictions = sum(1 for label in y_true if label == target_class)
    
    accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0
    return accuracy

# Hitung akurasi untuk target_class
accuracy = calculate_accuracy(y_test, y_pred, target_class)

# Buat plot untuk menunjukkan gambar, prediksi, dan label aslinya
fig, axes = plt.subplots(1, num_samples_to_show, figsize=(15, 3))

for i, index in enumerate(selected_indices):
    ax = axes[i]
    image = X_test[index].reshape(28, 28)
    true_label = y_test[index]
    predicted_label = y_pred[index]

    # Tampilkan gambar
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    ax.set_title(f'True: {true_label}\nPred: {predicted_label}')

# Tampilkan akurasi di atas plot
plt.suptitle(f'Accuracy for Class {target_class}: {accuracy * 100:.2f}%', fontsize=16)
plt.show()
