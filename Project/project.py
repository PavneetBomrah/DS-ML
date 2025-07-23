import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from skimage.io import imread
from skimage.transform import resize

# ==== SETTINGS ====
data_dir = 'flowers'
image_size = (64, 64)
max_images_per_class = 600  # for quick testing

# ==== LOAD DATA ====
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

# ==== ENCODE LABELS ====
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# ==== SPLIT DATA ====
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# ==== TRAIN CLASSIFIER ====
print("Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ==== EVALUATE ====
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=le.classes_))
