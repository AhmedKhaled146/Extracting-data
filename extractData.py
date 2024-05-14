import json

def extract_data(text):
    paragraphs = text.split('\n\n')  # Split text into paragraphs based on double newline
    data = []

    for i, paragraph in enumerate(paragraphs):
        if paragraph.strip():  # Check if paragraph is not empty
            header, content = paragraph.split(': ', 1)  # Split header and content
            data.append({
                "header": header.strip(),
                "content": content.strip(),
                "start_index": text.find(paragraph),
                "end_index": text.find(paragraph) + len(paragraph)
            })
    return data

def main():
    try:
        # Read the text file
        with open('/home/ahmed/text.txt', 'r') as file:
            text_data = file.read()

        # Extract data and determine start/end indices
        extracted_data = extract_data(text_data)

        if extracted_data:
            # Convert to JSON
            json_data = json.dumps(extracted_data, indent=4)

            # Write to JSON file
            with open('output.json', 'w') as json_file:
                json_file.write(json_data)
            print("JSON file created successfully!")
        else:
            print("No data found in the text file.")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
