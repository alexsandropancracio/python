import fitz 
import pytesseract 
import cv2 
from PIL import Image 
import os 

pdf_path = r"C:\Users\Elisangela\Documents\OCR\nfse.pdf" 

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 

temp_dir = r"C:\Users\Elisangela\Documents\OCR\temp" 
os.makedirs(temp_dir, exist_ok=True) 
doc = fitz.open(pdf_path) 

for page_num in range(len(doc)): 
    page = doc.load_page(page_num) 
    pix = page.get_pixmap(dpi=300, alpha=False) 
    img_path = os.path.join(temp_dir, f"page_{page_num + 1}.png") 
    pix.save(img_path) 
    img = cv2.imread(img_path) 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray = cv2.medianBlur(gray, 3) 
    processed = cv2.adaptiveThreshold( gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10 ) 
    processed = cv2.convertScaleAbs(processed, alpha=1.5, beta=10) 
    treated_path = os.path.join(temp_dir, f"treated_{page_num + 1}.png") 
    cv2.imwrite(treated_path, processed) 
    config = r'--oem 3 --psm 4' 
    text = pytesseract.image_to_string(Image.open(treated_path), lang='por', config=config) 
    print(f"\n--- Página {page_num + 1} ---") 
    print(text.strip() or "(sem texto reconhecido)") 

doc.close() 
print("\n✅ OCR concluído com sucesso!")