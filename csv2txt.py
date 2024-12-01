import pandas as pd
import os

def convert_csv_to_txt(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        
        with open(output_file, 'w', encoding='utf-8') as txt_file:
            for index, row in df.iterrows():
                txt_file.write("________\n")
                txt_file.write(f"{row['Content']}\n")  # content
                txt_file.write(f"Link: {row['URL']}\n\n")  # link
                
        print(f"Done!: {output_file}")
        
    except FileNotFoundError:
        print(f"שגיאה: הקובץ '{input_file}'not found.")
    except Exception as e:
        print(f"שגיאה: {str(e)}")

if __name__ == "__main__":
    input_csv = "scraped_data.csv"
    output_txt = "output.txt"
    
    convert_csv_to_txt(input_csv, output_txt)
