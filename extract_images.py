import PyPDF2
from PIL import Image
import io

pdf_path = r'c:\Users\TKards\Documents\GitHub\portfolio\assets\Article_Teacher Travis Kim Shows How Math Can Be Solved with a Little Bit of Magic.pdf'

try:
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        print(f"Total pages: {len(reader.pages)}")
        
        for page_num, page in enumerate(reader.pages):
            print(f"\n--- Page {page_num + 1} ---")
            
            # Try to extract images
            if '/XObject' in page['/Resources']:
                xObject = page['/Resources']['/XObject'].get_object()
                
                for obj_name in xObject:
                    obj = xObject[obj_name]
                    
                    if obj['/Subtype'] == '/Image':
                        print(f"Found image: {obj_name}")
                        
                        # Get image info
                        if '/Width' in obj and '/Height' in obj:
                            print(f"  Size: {obj['/Width']} x {obj['/Height']}")
                        
                        try:
                            # Try to save the image
                            size = (obj['/Width'], obj['/Height'])
                            data = obj.get_data()
                            
                            if obj['/ColorSpace'] == '/DeviceRGB':
                                mode = "RGB"
                            else:
                                mode = "P"
                            
                            img = Image.frombytes(mode, size, data)
                            img.save(f'c:\\Users\\TKards\\Documents\\GitHub\\portfolio\\assets\\article_image_{page_num}_{obj_name[1:]}.png')
                            print(f"  Saved as: article_image_{page_num}_{obj_name[1:]}.png")
                        except Exception as e:
                            print(f"  Could not extract: {e}")
            else:
                print("No images found on this page")
                
except Exception as e:
    print(f"Error: {e}")
