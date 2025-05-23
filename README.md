# SAR Image Colorization Web App

This project provides a client-side web application for colorizing grayscale Synthetic Aperture Radar (SAR) images using a K-Nearest Neighbors (KNN) approach. It leverages a reference color image to learn a mapping from grayscale intensities to color values, which is then applied to the input SAR images.

---

## Features

* **Client-Side Operation:** Runs entirely in your web browser using HTML, CSS (Tailwind CSS), and JavaScript. No server-side setup or Python environment is required.

* **Batch Grayscale Image Upload:** Upload multiple grayscale SAR images for colorization.

* **Reference Color Image Upload:** Provide one or more reference color images from which the color information will be extracted.

* **Automatic Image Resizing:** All uploaded images are automatically resized to 256x256 pixels for consistent processing.

* **KNN-based Colorization:** Employs a simplified 1-Nearest Neighbor (1-NN) approach, effectively creating a direct mapping from grayscale pixel intensities to corresponding colors observed in the reference image.

* **Interactive Display:** View the uploaded grayscale images, the reference color image(s), and the resulting colorized SAR images directly in the browser.

* **Clear Status Messages:** Provides feedback on the upload and processing status.

---

## How It Works

The core idea behind this colorization method is to "learn" a color for each possible grayscale intensity value (0-255) from a given reference image.

1.  **Image Upload and Preprocessing:**

    * You upload grayscale images (to be colorized) and at least one reference color image.

    * All images are loaded and resized to a consistent 256x256 resolution. Grayscale images are ensured to be truly grayscale.

2.  **KNN "Training" (Color Mapping):**

    * The **first** uploaded reference color image is used for training.

    * For every pixel in this reference image, its grayscale intensity value is calculated (luminance).

    * A lookup table (or "color map") is created where each unique grayscale intensity (0-255) is associated with the corresponding BGR (Blue, Green, Red) color of that pixel in the reference image. Since `n_neighbors=1`, if multiple pixels in the reference image have the same grayscale intensity but different colors, the first encountered mapping is used.

3.  **Colorization:**

    * For each grayscale SAR image you uploaded, the application iterates through every pixel.

    * For each pixel, its grayscale intensity value is obtained.

    * This grayscale value is then used to look up the corresponding color in the previously generated color map.

    * The colorized image is constructed pixel by pixel using the predicted colors.

4.  **Display Results:**

    * The original uploaded grayscale images, the reference color images, and the newly generated colorized images are displayed side-by-side for comparison.

---

## Getting Started

To use the application, follow these simple steps:

1.  **Save the Code:** Copy the entire HTML code provided below and save it as an `.html` file (e.g., `index.html`) on your computer.

2.  **Open in Browser:** Open the saved `index.html` file with your preferred web browser (Chrome, Firefox, Edge, Safari, etc.).

3.  **Upload Images:**

    * Click on "Upload Grayscale Images" to select one or more grayscale SAR images.

    * Click on "Upload Reference Color Images" to select one or more reference color images. (Note: Only the first reference image will be used for color mapping).

4.  **View Results:** Once both types of images are uploaded, the application will automatically process them and display the uploaded images and the colorized results below.

---

## Technical Stack

* **HTML5:** For the basic structure of the web page.

* **CSS3 (Tailwind CSS):** For styling and layout, providing a clean and responsive user interface.

* **JavaScript:** For all the core logic, including:

    * File handling and reading.

    * Image loading, resizing, and pixel manipulation (using Canvas API).

    * Implementation of the simplified KNN (grayscale-to-color mapping).

---

## Considerations for SAR Images

SAR images often represent intensity information and do not inherently contain color. This colorization method applies colors based on intensity values learned from a *natural* or *optical* reference image. The effectiveness of the colorization heavily depends on:

* **The content of the reference image:** A reference image that visually correlates well with the features or terrains expected in the SAR image will yield more meaningful results.

* **The nature of SAR data:** Direct intensity mapping might not always capture complex textural or structural information inherent in SAR data, but it provides a basic and often effective colorization for visualization purposes.

---

## Author

* **Udaya Venkata Pavan Gudala

---

## License

This project is licensed under the MIT License - see the [LICENSE](#license) section below for details.

### MIT License
