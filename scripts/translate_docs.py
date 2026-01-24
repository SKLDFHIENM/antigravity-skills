import os
import sys
import google.generativeai as genai

def translate_file(input_path, output_path):
    print(f"Translating {input_path} to {output_path}...")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    You are a professional technical translator. Translate the following Markdown content from Chinese to English.
    Maintain the original Markdown formatting precisely. 
    Ensure technical terms are translated accurately (e.g., '符号链接' to 'Symbolic Link' or 'Symlink').
    Do not add any preamble or postamble, just provide the translated Markdown content.

    Content to translate:
    {content}
    """
    
    response = model.generate_content(prompt)
    translated_content = response.text
    
    # Simple check to remove potential Triple Backticks wrapper from LLM
    if translated_content.startswith("```markdown"):
        translated_content = translated_content[len("```markdown"):].strip()
    if translated_content.endswith("```"):
        translated_content = translated_content[:-3].strip()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated_content)
    
    print(f"Successfully saved to {output_path}")

if __name__ == "__main__":
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        sys.exit(1)
        
    genai.configure(api_key=api_key)
    
    files_to_translate = [
        ("README.md", "README.EN.md"),
        ("docs/Antigravity_Skills_Manual_CN.md", "docs/Antigravity_Skills_Manual_EN.md")
    ]
    
    for cn_file, en_file in files_to_translate:
        if os.path.exists(cn_file):
            translate_file(cn_file, en_file)
        else:
             print(f"Warning: {cn_file} does not exist. Skipping.")
