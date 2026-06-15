try:
    import cv2
except ModuleNotFoundError:
    cv2 = None

import numpy as np
from tkinter import Tk, Button, Label, filedialog, Canvas, messagebox
from PIL import Image, ImageTk

def segment_banana(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([15, 40, 40])
    upper = np.array([75, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)

    mask_white = cv2.inRange(hsv, (0, 0, 200), (180, 60, 255))
    mask = cv2.bitwise_and(mask, cv2.bitwise_not(mask_white))

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    return mask

def rgb_to_hsi(image):
    image = image.astype(np.float32) / 255.0
    B, G, R = cv2.split(image)

    I = (R + G + B) / 3.0
    min_rgb = np.minimum(np.minimum(R, G), B)
    S = 1 - (3 / (R + G + B + 1e-6)) * min_rgb

    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G) ** 2 + (R - B) * (G - B)) + 1e-6
    theta = np.arccos(np.clip(num / den, -1, 1))

    H = np.where(B <= G, theta, 2 * np.pi - theta)
    H = H * (180 / np.pi) 

    return H, S, I

def get_dominant_hue_saturation(image):
    mask = segment_banana(image)
    H, S, _ = rgb_to_hsi(image)

    hue_values = H[mask > 0]
    sat_values = S[mask > 0]

    if len(hue_values) == 0 or len(sat_values) == 0:
        return None, None

    return np.mean(hue_values), np.mean(sat_values)

def classify_ripeness(hue, sat):
    if hue is None or sat is None:
        return "Tidak Diketahui"

    if 66 <= hue <= 90 and 0.20 <= sat <= 0.75:
        return "Mentah"
    elif 31 <= hue <= 53 and 0.40 <= sat <= 0.81:
        return "Matang"
    else:
        return "Tidak Diketahui"


class BananaRipenessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deteksi Kematangan Pisang (HSI)")
        self.root.geometry("600x600")
        self.root.configure(bg="#fdf6e3")

        Label(root, text="Deteksi Kematangan Pisang", font=("Helvetica", 20, "bold"), bg="#fdf6e3").pack(pady=20)
        Button(root, text="Masukkan Gambar", command=self.load_image, font=("Helvetica", 14), bg="#b2dfdb").pack(pady=10)

        self.canvas = Canvas(root, width=400, height=300, bg="#eeeeee")
        self.canvas.pack(pady=10)

        self.result_label = Label(root, text="", font=("Helvetica", 14), bg="#fdf6e3", fg="#333")
        self.result_label.pack(pady=10)

        self.img_tk = None

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if not file_path:
            return

        image_cv = cv2.imread(file_path)
        if image_cv is None:
            self.result_label.config(text="❌ Gagal memuat gambar.")
            return

        hue, sat = get_dominant_hue_saturation(image_cv)
        ripeness = classify_ripeness(hue, sat)

        image_rgb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb).resize((400, 300))
        self.img_tk = ImageTk.PhotoImage(image_pil)
        self.canvas.create_image(0, 0, anchor="nw", image=self.img_tk)

        hue_text = f"{hue:.2f}" if hue is not None else "Tidak Diketahui"
        sat_text = f"{sat:.2f}" if sat is not None else "Tidak Diketahui"
        result_text = f"Hasil: {ripeness}\nHue: {hue_text} | Saturasi: {sat_text}"
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    if cv2 is None:
        import sys
        try:
            root = Tk()
            root.withdraw()
            messagebox.showerror("Missing dependency",
                                 "Module 'cv2' not found. Install dependencies:\n\npip install -r requirements.txt")
            root.destroy()
        except Exception:
            print("Missing module 'cv2'. Install dependencies: pip install -r requirements.txt")
        sys.exit(1)

    root = Tk()
    app = BananaRipenessApp(root)
    root.mainloop()
