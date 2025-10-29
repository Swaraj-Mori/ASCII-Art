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
