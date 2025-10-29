# ASCII Art

Transform any image into **[ASCII art](https://en.wikipedia.org/wiki/ASCII_art)** and export it as a **dark-mode PDF** — all in pure Python.  
ASCII art is a graphic design technique that uses the 95 printable characters from the American Standard Code for Information Interchange (ASCII) to create images
This project uses pixel brightness values to generate detailed ASCII visualizations that resemble the original image.

---

## Features
- **Dark Mode Output** — black background with white ASCII text  
- **Pixel-accurate brightness mapping** using NumPy  
- **Fully customizable** resolution, font size, and color theme  
- **Direct PDF generation** using ReportLab  
- **Lightweight and dependency-minimal**  

---

## Tech Stack
- **Python 3.9+**
- [Pillow](https://pillow.readthedocs.io/) – for image processing  
- [NumPy](https://numpy.org/) – for pixel array manipulation  
- [ReportLab](https://www.reportlab.com/) – for PDF creation  

## Instructions

Follow these steps to use and customize the ASCII Art to PDF Generator:

### 1. Prepare the Image
- Choose a **clear image** (preferably with good contrast).  
- Rename it (optional) and place it inside the `ASCII_art/` folder.  
- Recommended formats: `.jpg`, `.png`, `.jpeg`.

### 2. Run the Script
- Open a terminal inside the project folder.  
- Run:
  ```bash
  python ascii_to_pdf.py

**Recommended:** Open the PDF in Google Chrome for the best dark-mode rendering and text clarity.
