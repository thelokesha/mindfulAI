import os
import logging
import google.generativeai as genai

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Gemini API setup
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Model setup
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 800,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings
)

def construct_mental_health_system_prompt():
    """Create a system prompt that guides the AI to focus on mental health support."""
    return """You are a compassionate mental health support assistant that ONLY responds to mental health related issues.

STRICT CONVERSATION FLOW:
1. First, ask the user about their specific mental health problem
2. Build the conversation by asking targeted follow-up questions  
3. Identify the ROOT CAUSE of their issue through careful questioning
4. ONLY AFTER identifying the root cause, provide clear solutions specifically for that root cause

IMPORTANT RULES:
- ONLY answer mental health related questions - decline to answer anything else
- Always maintain this exact sequence: ask about problem → build conversation → identify root cause → provide solutions
- Ask one question at a time to properly build the conversation
- Do not rush to conclusions or solutions without adequate conversation
- Provide solutions ONLY after you've clearly identified the root cause
- Frame solutions in a practical, actionable way with 2-3 specific steps
- Be empathetic but concise in your responses
- Never diagnose medical conditions
- Recommend professional help when appropriate
- Do not mention that you're using any AI model or technology
- If the user tries to skip the conversation-building process, gently redirect them back to it"""

def get_ai_response(message_history):
    """
    Get a response from Gemini API for mental health support.
    
    Args:
        message_history (list): List of message dictionaries with 'role' and 'content'
    
    Returns:
        str: The AI assistant's response
    """
    if not GEMINI_API_KEY:
        logger.error("Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")
        return "I'm sorry, but I can't connect to my knowledge base right now. Please try again later."
    
    try:
        # Convert message history to Gemini's expected format
        chat = model.start_chat(history=[])
        
        # Add system message first if not present
        system_prompt = construct_mental_health_system_prompt()
        if not message_history or message_history[0].get('role') != 'system':
            chat.send_message(system_prompt)
        
        # Add user and assistant messages
        for msg in message_history:
            if msg['role'] == 'user':
                chat.send_message(msg['content'])
            elif msg['role'] == 'assistant':
                pass
        
        # Get response
        response = chat.send_message("Please continue the conversation as the mental health assistant.")
        return response.text
    
    except Exception as e:
        logger.error(f"Error calling Gemini API: {str(e)}")
        return "I'm sorry, but I encountered an error while processing your request. Please try again later."
