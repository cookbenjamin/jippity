# Jippity

Jippity is a simple CLI wrapper around OpenAI's chat GPT, with added syntax highlighting functionality, because heading to the website is too slow.

## Setup and Installation

```bash
git clone https://github.com/cookbenjamin/jippity.git
cd jippity
python3 -m pip install .
```

You will need your own OpenAI API key and add it to your env.
e.g. in your ~/.bashrc
```bash
export OPENAI_API_KEY=<key goes here>
```

## How to Run

```bash
jip <your prompt goes here>
```

## Features

- Syntax highlighting: The application supports syntax highlighting of code segments for enhanced readability. This feature can be toggled off by setting the environment variable `JIP_NOCOLOR`.

- Conversation history: A history of the conversation with the GPT model is maintained in 'conversation_history.json', allowing for continuation of the conversation across different sessions.

