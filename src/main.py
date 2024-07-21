from openai import OpenAI
import sys
import os
import json
import re
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
conversation_history = []

def highlight_code(code):
    if os.getenv('JIP_NOCOLOR'):
        return code

    pattern = re.compile(r"```(\w+)\n(.*?)```", re.DOTALL)
    matches = re.findall(pattern, code)

    highlighted_code = code
    for match in matches:
        language, code_segment = match
        try:
            lexer = get_lexer_by_name(language)
            highlighted_segment = highlight(code_segment, lexer, TerminalFormatter())
            highlighted_code = highlighted_code.replace(f'```{language}\n{code_segment}```', highlighted_segment)
        except:
            print('Invalid language:', language)
    
    return highlighted_code

def chat_with_gpt(prompt):
    global conversation_history
    if os.path.exists('conversation_history.json'):
        with open('conversation_history.json', 'r') as file:
            conversation_history = json.load(file)
            
    messages = conversation_history + [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt}],
        },
        {
            "role": "system",
            "content": [
                {"type": "text",
                 "text": "You are an assistant that writes simple and straightforward code. If the user requests 'code only' then only respond with the code portion of the response."
                 }
            ]
        }
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    
    conversation_history.append(
        {
            'role': 'assistant',
            'content': [{'type': 'text', 'text': response.choices[0].message.content}]
        }
    )
    with open('conversation_history.json', 'w') as file:
        json.dump(conversation_history, file)
    
    return response

if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Please provide a prompt: ")
    response = chat_with_gpt(user_input)
    # add syntax highlighting before printing out the response
    print(highlight_code(response.choices[0].message.content))
