# Multi-Agent Blog Writer

## Overview
The **Multi-Agent Blog Writer** is an AI-powered tool designed to streamline the content creation process for LinkedIn posts. By utilizing multiple agents with distinct roles and goals, it ensures the generation of high-quality, engaging, and insightful posts tailored to specific topics.

This project is built using the `crewai` framework and integrates large language models (LLMs) to perform tasks such as planning, writing, and editing content collaboratively.

## Features
1. **Content Planner**: Plans engaging and factually correct content based on the specified topic.
2. **Content Writer**: Writes an accurate and insightful LinkedIn post following the planner's outline.
3. **Content Editor**: Reviews the content, aligns it with best practices of copywriting, and adds hooks and calls to action (CTAs).

## Workflow
1. **Initialization**: The system is initialized with the topic for the LinkedIn post.
2. **Sequential Processing**: The agents perform their roles in the following sequence:
   - Planner → Writer → Editor.
3. **Output**: The final result is a polished, engaging LinkedIn post ready for publishing.

## Prerequisites
1. Python 3.9 or later.
2. Install required dependencies:
   ```bash
   pip install crewai python-dotenv
   ```
3. Create a `.env` file in the project directory to store your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage
1. Define your agents in the script.
2. Provide a topic for the content in the `crew.kickoff` method:
   ```python
   result = crew.kickoff(inputs={"topic": "How to learn GenAI"})
   print(result)
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## Example Output
```plaintext
Planning content for the topic: "How to learn GenAI."
Content Writer is drafting the post...
Editor is refining the post...
Final post: "Are you looking to dive into Generative AI? Here's how to start... [Detailed post]"
```

## Customization
- **Agents**: Modify roles, goals, or backstories to suit your content creation requirements.
- **LLM Model**: Replace `groq/llama3-8b-8192` with another model if needed.
- **Verbose Output**: Adjust verbosity for debugging or detailed logs.

## Limitations
- Requires a valid API key for LLM integration.
- Performance and accuracy depend on the underlying language model.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
