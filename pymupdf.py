import fitz

pdf_file = "./Contract.pdf"
doc = fitz.open(pdf_file)

target_x = 100
target_y = 200

for page in doc.pages():
    words = page.get_text("words")
    for word in words:
        x, y = word[7], word[7]
        if x == target_x and y == target_y:
            print(f"Word: {word['text']}, Position: ({x}, {y})")

doc.close()