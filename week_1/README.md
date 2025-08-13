# Prompt Testing Framework with promptfoo (Experimental)

This project demonstrates how to test LLM prompts using promptfoo, focusing on different types of prompts and testing scenarios.

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/Jaimeman84/promptfoo-framework-sample.git
cd promptfoo-framework-sample
```

2. Install promptfoo globally:
```bash
npm install -g promptfoo
```

3. Set up your API keys in environment variables:
```bash
export OPENAI_API_KEY=your_key_here
export ANTHROPIC_API_KEY=your_key_here
```

Or create a `.env` file in the project root:
```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

4. Run your first test:
```bash
# Test sentiment analysis
promptfoo eval -c config/promptfooconfig.yaml -p prompts/single/sentiment.txt -t tests/single/sentiment_tests.yaml

# View results in browser
promptfoo view
```

## Project Structure

```
promptfoo-examples/
├── config/
│   └── promptfooconfig.yaml    # Provider settings (OpenAI, Claude, etc.)
├── prompts/
│   ├── single/
│   │   └── sentiment.txt      # Analyzes text sentiment
│   ├── multi/
│   │   └── chat_thread.txt   # Customer service conversation
│   └── file_based/
│       └── code_review.txt   # Reviews code files
└── tests/
    ├── single/
    │   └── sentiment_tests.yaml
    ├── multi/
    │   └── conversation_tests.yaml
    └── file_based/
        └── code_review_tests.yaml
```

## Running Tests

### Test Individual Scenarios

1. Sentiment Analysis:
```bash
promptfoo eval -c config/promptfooconfig.yaml -p prompts/single/sentiment.txt -t tests/single/sentiment_tests.yaml
```

2. Customer Service Chat:
```bash
promptfoo eval -c config/promptfooconfig.yaml -p prompts/multi/chat_thread.txt -t tests/multi/conversation_tests.yaml
```

3. Code Review:
```bash
promptfoo eval -c config/promptfooconfig.yaml -p prompts/file_based/code_review.txt -t tests/file_based/code_review_tests.yaml
```

### View Results in Browser
```bash
promptfoo view
```

## Prompt Types Examples

1. **Sentiment Analysis** (`prompts/single/sentiment.txt`)
   - Takes: Text input
   - Returns: JSON with sentiment, confidence, and explanation

2. **Customer Service** (`prompts/multi/chat_thread.txt`)
   - Takes: Customer name, history, and current issue
   - Returns: Professional customer service response

3. **Code Review** (`prompts/file_based/code_review.txt`)
   - Takes: Code file content
   - Returns: Detailed code review with issues and suggestions

## Test File Structure

Each test file contains:
```yaml
- vars:           # Input variables
    text: "I love this product!"
  assert:         # What to check in the response
    - type: contains
      value: "positive"
    - type: is-json
      value: {...}
```

Common assertion types:
- `contains`: Check for specific text
- `is-json`: Validate JSON structure
- `contains-all`: Check for multiple strings
- `llm-rubric`: Use AI to grade response quality

## Troubleshooting

1. **Path Issues**: Make sure you're in the project root directory when running commands
2. **API Keys**: Double-check your environment variables or .env file
3. **Model Names**: Verify provider names in config/promptfooconfig.yaml match your API access

## Support

If you encounter any issues or have questions:
1. Check the [promptfoo documentation](https://promptfoo.dev/docs)
2. Open an issue in this repository
3. Join the [promptfoo Discord community](https://discord.gg/promptfoo)

---
Created by Jaime Mantilla, MSIT + AI  
Last Updated: 08/2025
