import json

# Step 1: Read the text file
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Step 2: Process the text data to extract information
def process_text_data(text):
    paragraphs = {}
    current_paragraph = None

    lines = text.split('\n')
    current_index = 0
    for line in lines:
        if line.startswith("Paragraph"):
            if current_paragraph:
                paragraphs[current_paragraph[0]] = {
                    "content": current_paragraph[1].strip(),
                    "start_index": current_paragraph[2],
                    "end_index": current_index
                }
            paragraph_num, paragraph_text = line.split(": ", 1)
            current_paragraph = [paragraph_num.strip(), paragraph_text.strip(), current_index]
        else:
            current_index += len(line) + 1

    # Add the last paragraph
    if current_paragraph:
        paragraphs[current_paragraph[0]] = {
            "content": current_paragraph[1].strip(),
            "start_index": current_paragraph[2],
            "end_index": current_index
        }

    return paragraphs

# Step 3: Write the dictionary to a JSON file
def write_to_json(data, json_file_path):
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage:
text_file_path = "/home/ahmed/text.txt"
json_file_path = "output_data.json"

text_data = read_text_file(text_file_path)
extracted_data = process_text_data(text_data)

write_to_json(extracted_data, json_file_path)
