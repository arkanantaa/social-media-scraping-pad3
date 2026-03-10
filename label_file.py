import os
import cv2
import shutil

def label_files(path, unsafe_path, safe_path):
    """
    Label file berdasarkan safe/unsafe lalu simpan ke dalam 
    sebuah folder yang berbeda.

    Args:
        path (str): File path asli.
    
    Controls:
        [u] = Unsafe
        [s] = Safe
        [q] = Quit
    """

    # Buat kedua folder jika tidak ada
    os.makedirs(unsafe_path, exist_ok=True)  
    os.makedirs(safe_path, exist_ok=True)  

    for filename in os.listdir(path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.webp')):
            img_path = os.path.join(path, filename)
            img = cv2.imread(img_path)

            display_img = cv2.resize(img, (500, 500))
            cv2.imshow('Labeling - [u] Unsafe  [s] Safe  [q] Quit', display_img)

            key = cv2.waitKey(0)

            if key == ord('u'):
                shutil.move(img_path, os.path.join(unsafe_path, filename))
                print(f"[UNSAFE] {filename}")
            elif key == ord('s'):
                shutil.move(img_path, os.path.join(safe_path, filename))  # ✅ Bug 3 fix
                print(f"[SAFE]   {filename}")
            elif key == ord('q'):
                print("Quit labeling.")
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    label_files('gallery-dl/instagram/tag/anakdugem', 'anakdugem/unsafe', 'anakdugem/safe')