# 🎨 Image Inpainting Comparison Project

This repository explores two different methods for the image inpainting problem (removing and seamlessly filling objects):

## 1. Deep Learning Approach (Kandinsky 2.2)

* **File:** `kandinsky_inpainting.ipynb`
* **Methodology:** Uses the Hugging Face `diffusers` library and the Kandinsky 2.2 model. This is **Generative AI**—it creates entirely new, realistic content based on a text prompt to fill the hole.
* **Best for:** Creative object replacement and highly complex fills.
* **Execution Note:** Best run in Google Colab because it requires a powerful GPU.

## 2. Classic Computer Vision Approach (OpenCV)

* **File:** `opencv_inpainting.py`
* **Methodology:** Uses the classic **OpenCV Telea Algorithm** (`cv2.INPAINT_TELEA`). This method fills the hole by copying texture and color from the pixels right around the edge of the mask.
* **Best for:** Fast, seamless removal of wires, small blemishes, or simple backgrounds.

---

## 🛠️ How to Run the Project

### Installation (The Requirements)

Anyone can set up the environment using the `requirements.txt` file.
