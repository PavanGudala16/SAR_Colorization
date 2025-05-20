import streamlit as st
import numpy as np
import cv2
import os
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import tempfile

st.title("SAR Image Colorization using KNN")

st.markdown("Upload grayscale SAR images and reference color images to perform colorization.")

# Upload folders for grayscale and reference images
gray_files = st.file_uploader("Upload Grayscale Images", accept_multiple_files=True, type=["jpg", "png", "jpeg"])
color_files = st.file_uploader("Upload Reference Color Images", accept_multiple_files=True, type=["jpg", "png", "jpeg"])

def load_uploaded_images(uploaded_files, grayscale=False):
    images = []
    for file in uploaded_files:
        file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        flag = cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_COLOR
        img = cv2.imdecode(file_bytes, flag)
        if img is not None:
            img = cv2.resize(img, (256, 256))
            images.append(img)
    return images

if gray_files and color_files:
    st.success("Images uploaded. Processing...")
    gray_images = load_uploaded_images(gray_files, grayscale=True)
    color_images = load_uploaded_images(color_files, grayscale=False)

    st.write("## Grayscale Images")
    for img in gray_images:
        st.image(img, clamp=True, channels="GRAY")

    st.write("## Reference Color Images")
    for img in color_images:
        st.image(img, clamp=True, channels="BGR")

    # ----- Begin KNN Colorization -----
    def extract_features(img):
        features = []
        labels = []
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                gray_val = int(0.299 * img[i, j, 2] + 0.587 * img[i, j, 1] + 0.114 * img[i, j, 0])
                features.append([gray_val])
                labels.append(img[i, j])
        return np.array(features), np.array(labels)

    st.write("## Colorizing...")

    # Use the first reference image for training
    ref_img = color_images[0]
    features, labels = extract_features(ref_img)

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(features, labels)

    for idx, gray_img in enumerate(gray_images):
        test_features = gray_img.flatten().reshape(-1, 1)
        pred_colors = knn.predict(test_features)
        colorized_img = pred_colors.reshape(256, 256, 3).astype(np.uint8)

        st.write(f"### Colorized Image {idx+1}")
        st.image(colorized_img, channels="BGR")
else:
    st.info("Please upload both grayscale and reference color images.")
