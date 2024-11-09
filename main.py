
opencv-python-headless
numpy
pillow
# プロジェクトディレクトリに移動
cd dental-xray-enhancer

# Gitの初期化
git init

# GitHubリポジトリをリモートに追加
git remote add origin https://github.com/username/dental-xray-enhancer.git

# ファイルを追加してコミット
git add .
git commit -m "Initial commit with dental X-ray enhancer code"

# GitHubにプッシュ
git push -u origin main
README.md
# Dental X-Ray Enhancer

This is a Python application that enhances the clarity of dental X-ray images. 

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Pillow

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/username/dental-xray-enhancer.git
cd dental-xray-enhancer
pip install -r requirements.txt
python main.py
