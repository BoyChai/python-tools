import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def process_images(img_path1, img_path2):
    img1 = cv2.imread(img_path1)
    img2 = cv2.imread(img_path2)

    if img1 is None or img2 is None:
        print("无法读取图片.")
        return None

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    lsd = cv2.createLineSegmentDetector(0)
    lines1, _, _, _ = lsd.detect(gray1)
    lines2, _, _, _ = lsd.detect(gray2)

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(gray1, None)
    kp2, des2 = orb.detectAndCompute(gray2, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    result_img = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None,
                                    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    return result_img, img1, img2


class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图像处理器")
        self.root.geometry("1000x680")  # 设置窗口大小

        self.img_path1 = ""
        self.img_path2 = ""
        self.result_img = None

        self.create_widgets()

    def create_widgets(self):
        # 左侧布局
        left_frame = tk.Frame(self.root)
        left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Label(left_frame, text="选择图像 1:").pack()
        tk.Button(left_frame, text="浏览", command=self.browse_image1).pack()

        self.image_frame1 = tk.Frame(left_frame, width=400, height=300)
        self.image_frame1.pack()

        tk.Label(left_frame, text="选择图像 2:").pack()
        tk.Button(left_frame, text="浏览", command=self.browse_image2).pack()

        self.image_frame2 = tk.Frame(left_frame, width=400, height=300)
        self.image_frame2.pack()

        # 右侧布局
        right_frame = tk.Frame(self.root)
        right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.process_button = tk.Button(right_frame, text="处理图像", command=self.process_images)
        self.process_button.pack()

        self.save_button = tk.Button(right_frame, text="保存结果", command=self.save_result, state=tk.DISABLED)
        self.save_button.pack()

        self.result_label = tk.Label(right_frame, width=800, height=600)
        self.result_label.pack()

    def browse_image1(self):
        self.img_path1 = filedialog.askopenfilename(filetypes=[("图像文件", "*.png;*.jpg;*.jpeg")])
        img = self.load_image(self.img_path1)
        self.display_image(img, self.image_frame1)

    def browse_image2(self):
        self.img_path2 = filedialog.askopenfilename(filetypes=[("图像文件", "*.png;*.jpg;*.jpeg")])
        img = self.load_image(self.img_path2)
        self.display_image(img, self.image_frame2)

    def process_images(self):
        self.result_img, img1, img2 = process_images(self.img_path1, self.img_path2)
        if self.result_img is not None:
            self.display_image(img1, self.image_frame1)
            self.display_image(img2, self.image_frame2)
            self.display_image(self.result_img, self.result_label)
            self.save_button.config(state=tk.NORMAL)  # 启用保存按钮
        else:
            self.save_button.config(state=tk.DISABLED)  # 禁用保存按钮

    def display_image(self, img, frame):
        img = cv2.resize(img, (400, 300))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)

        # 清空frame
        for widget in frame.winfo_children():
            widget.destroy()

        label = tk.Label(frame, image=img)
        label.image = img
        label.pack()

    def save_result(self):
        if self.result_img is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG 文件", "*.jpg")])
            if save_path:
                cv2.imwrite(save_path, self.result_img)

    def load_image(self, img_path):
        img = cv2.imread(img_path)
        return img


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
