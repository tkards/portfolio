import sys
try:
    import PyPDF2
    pdf_path = r'c:\Users\TKards\Documents\GitHub\portfolio\assets\Article_Teacher Travis Kim Shows How Math Can Be Solved with a Little Bit of Magic.pdf'
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        print(text)
except ImportError:
    print("PyPDF2 not installed. Please provide the article content manually.")
except Exception as e:
    print(f"Error: {e}")
