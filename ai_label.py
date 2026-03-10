import os
import csv
import shutil
import time
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

# Gemini setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemma-3-27b-it")

PROMPT = """
Bayangkan anda adalah seorang pengawas konten media sosial. Anda ditugaskan untuk mencari tahu apakah suatu gambar aman atau tidak dikonsumsi untuk anak-anak.
Hindari penggunaan tanda koma (,) untuk penginputan lebih mudah ke CSV

Suatu gambar dikatakan UNSAFE bila mengandung:
- Konten seksual atau pornografi
- Grafik kekerasan atau gore
- Alcohol, narkoba, atau penggunaan substansi sejenis
- Ujaran kebencian dan ekstrimis
- Konten dewasa eksplisit atau tipis 
- Kata-kata kasar
- Konten LGBTQ
- Konten yang mengandung humor dewasa atau mengarah ke humor dewasa
- Lainnya yang menurut anda bersifat negatif bagi anak

Respon hanya menggunakan format yang sama persis seperti berikut: 
LABEL: <SAFE or UNSAFE>
REASON: <deskripsikan gambar tersebut, lalu jelaskan mengapa gambar tersebut aman/tidak aman dikonsumsi anak-anak. jelaskan dengan jelas dalam 1-3 kalimat.>
"""

def ai_label(path, unsafe_path, safe_path, csv_output="label_results.csv"):
    """
    Uses Gemini API to automatically classify images as SAFE or UNSAFE,
    moves them to the appropriate folder, and saves results to a CSV.

    Args:
        path        (str): Source folder containing images to label.
        unsafe_path (str): Destination folder for unsafe images.
        safe_path   (str): Destination folder for safe images.
        csv_output  (str): Path to the output CSV file (default: 'label_results.csv')
    """
    os.makedirs(unsafe_path, exist_ok=True)
    os.makedirs(safe_path, exist_ok=True)

    img_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    image_files = sorted([f for f in os.listdir(path) if f.endswith(img_extensions)])

    if not image_files:
        print(f"No images found in '{path}'")
        return

    results = []
    total = len(image_files)

    for i, filename in enumerate(image_files, start=1):
        img_path = os.path.join(path, filename)
        print(f"Processing: {filename}")

        try:
            # load and send image to gemini
            # Use a with-block so the file handle is closed before shutil.move()
            with Image.open(img_path) as pil_img:
                pil_img.load()  # force full load into memory
                response = model.generate_content([PROMPT, pil_img])
            raw_text = response.text.strip()

            # response parsing
            label  = "UNKNOWN"
            reason = raw_text

            for line in raw_text.splitlines():
                if line.startswith("LABEL:"):
                    label = line.replace("LABEL:", "").strip().upper()
                elif line.startswith("REASON:"):
                    reason = line.replace("REASON:", "").strip()

            # move file
            if label == "UNSAFE":
                dest = os.path.join(unsafe_path, filename)
                shutil.move(img_path, dest)
                print(f"UNSAFE = {reason}")
            else:
                dest = os.path.join(safe_path, filename)
                shutil.move(img_path, dest)
                print(f"SAFE = {reason}")

            results.append({
                "image_name" : filename,
                "label"      : label,
                "description": reason
            })

        except Exception as e:
            print(f"Error processing {filename}: {e}")
            results.append({
                "image_name" : filename,
                "label"      : "ERROR",
                "description": str(e)
            })

        # Small delay to respect Gemini rate limits
        time.sleep(0.5)

    # Save CSV
    with open(csv_output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["image_name", "label", "description"])
        writer.writeheader()
        writer.writerows(results)

    # Summary
    safe_count   = sum(1 for r in results if r["label"] == "SAFE")
    unsafe_count = sum(1 for r in results if r["label"] == "UNSAFE")
    error_count  = sum(1 for r in results if r["label"] == "ERROR")

    print(f"Done! Results saved to: {csv_output}")
    print(f"SAFE   : {safe_count}")
    print(f"UNSAFE : {unsafe_count}")
    print(f"ERROR  : {error_count}")


# ── Entry Point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    ai_label(
        path        = 'gallery-dl/instagram/tag/jomok',
        unsafe_path = 'jomok/unsafe',
        safe_path   = 'jomok/safe',
        csv_output  = 'jomok/label_results.csv'
    )
