import json

system_prompt = """You are ChatGPT, specialized in translating complex English sentences into accurate and fluent Italian translations. 
Provide only the Italian translation for each given English sentence.
"""

def create_new_jsonl(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Read each line from the input file
            data = json.loads(line)
            
            # Create a new message structure
            new_message = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": data['input']},
                    {"role": "assistant", "content": data['output_4o']}
                ]
            }
            
            # Write the new message structure to the output file
            json.dump(new_message, outfile)
            outfile.write('\n')

# Example usage
create_new_jsonl(r"Days\009\openai_distillation\output.jsonl", r"Days\009\openai_distillation\training.jsonl")
