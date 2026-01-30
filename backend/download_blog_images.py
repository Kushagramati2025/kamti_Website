import os
import urllib.request
import urllib.parse
import time

base_dir = r"d:\kmati_website\backend\media\blog"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

images = {
    "opencv.jpg": "futuristic computer vision scanning eye technology blue theme hd",
    "timeseries.jpg": "data analytics stock market chart time series graph growth prediction business",
    "socialmedia.jpg": "social media network connections global digital map cybersecurity lock",
    "graphdb.jpg": "abstract network nodes graph database connections 3d visualization purple blue",
    "aws_ec2.jpg": "cloud computing server room datacenter glowing lights amazon web services style"
}

print(f"Downloading images to {base_dir}...")

for filename, prompt in images.items():
    safe_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1024&height=600&nologo=true&seed={int(time.time())}"
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = response.read()
            file_path = os.path.join(base_dir, filename)
            with open(file_path, 'wb') as f:
                f.write(data)
            print(f"Saved {filename} ({len(data)} bytes)")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
    
    # Tiny sleep to ensure different seeds if time-based (optional but good practice)
    time.sleep(1)

print("All downloads complete.")
