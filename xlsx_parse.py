import argparse
import pandas as pd
from datetime import datetime

def transform_data(file_path):
    # Load the Excel file
    data = pd.read_excel(file_path).iloc[1:].reset_index(drop=True)
    
    # Define the template
    template = "【需求 {count}】\n源IP:\n{source_ip}\n目的IP：\n{destination_ip}\n目的端口：\n{destination_port}\n协议：\n{protocol}"

    # Apply the transformation
    formatted_rows = [
        template.format(
            count=i+1, 
            source_ip=row.iloc[0], 
            destination_ip=row.iloc[1], 
            destination_port=row.iloc[2], 
            protocol=row.iloc[3]
        )
        for i, row in data.iterrows()
    ]

    # Join all formatted rows into a single string
    formatted_text = "\n\n".join(formatted_rows)
    return formatted_text

def main():
    parser = argparse.ArgumentParser(description="Transform Excel network policy data.")
    parser.add_argument('--path', type=str, help="Path to the Excel file", required=True)
    parser.add_argument('--output', type=str, help="Output file path", required=False)
    
    args = parser.parse_args()
    transformed_data = transform_data(args.path)
    
    if args.output:
        output_file = args.output
    else:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_file = f"output_{timestamp}.txt"
        print(f'output> {output_file}')
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(transformed_data)

if __name__ == "__main__":
    main()
