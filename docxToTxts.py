import os
from docx import Document

def docx_to_txt(input_dir, output_dir):
    """
    Converts all .docx files in the input directory to .txt files in the output directory.

    Args:
        input_dir (str): Path to the directory containing .docx files.
        output_dir (str): Path to save the converted .txt files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".docx"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")

            print(f"Converting: {input_path} -> {output_path}")
            
            try:
                # Load the DOCX file
                doc = Document(input_path)
                with open(output_path, "w", encoding="utf-8") as txt_file:
                    # Write paragraphs to the text file
                    for para in doc.paragraphs:
                        txt_file.write(para.text + "\n")
                print(f"Successfully converted: {output_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    input_directory = input("Enter the directory containing .docx files: ").strip()
    output_directory = input("Enter the directory to save .txt files: ").strip()
    docx_to_txt(input_directory, output_directory)
