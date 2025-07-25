import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from skimage.io import imread
from skimage.transform import resize
import matplotlib.pyplot as plt
import seaborn as sns


data_dir = 'flowers'
image_size = (64, 64)
X, y = [], []

print("Loading and processing images...")
for label in os.listdir(data_dir):
    label_path = os.path.join(data_dir, label)
    if not os.path.isdir(label_path):
        continue

    image_files = os.listdir(label_path)
    for i, image_file in enumerate(image_files):
        img_path = os.path.join(label_path, image_file)
        try:
            img = imread(img_path)
            img_resized = resize(img, image_size, anti_aliasing=True).flatten()
            X.append(img_resized)
            y.append(label)

            if i % 50 == 0:
                print(f"Processed {i} images in class '{label}'...")
        except Exception as e:
            print(f"Skipping {img_path} due to error: {e}")

X = np.array(X)
y = np.array(y)
print(f"Total images loaded: {len(X)}")

le = LabelEncoder()
y_encoded = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.5, random_state=42)

print("Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=le.classes_))

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='YlGnBu', xticklabels=le.classes_, yticklabels=le.classes_)
plt.title('Confusion Matrix Heatmap')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.tight_layout()
plt.show()
