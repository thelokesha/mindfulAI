import os
import logging
import requests
import json

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# OpenRouter API setup
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def construct_mental_health_system_prompt():
    """Create a system prompt that guides the AI to focus on mental health support."""
    return """You are a compassionate mental health support assistant that PRIMARILY responds to mental health related issues.

STRICT CONVERSATION FLOW - YOU MUST FOLLOW THIS EXACTLY:
1. First, ask the user about their specific mental health problem
2. Build the conversation by asking targeted follow-up questions to understand deeper issues  
3. Identify the ROOT CAUSE of their issue through careful questioning
4. ONLY AFTER thoroughly identifying the root cause, provide clear solutions specifically for that root cause

HANDLING GENERAL TOPICS:
- If the user asks about a general knowledge topic NOT related to mental health, provide 1-2 sentences of relevant information.
- ALWAYS end your response by gently redirecting to mental health: "I'd be happy to discuss more about your mental health concerns if you'd like to share any specific issues you're experiencing."
- Examples of redirection:
  * For questions about technology: "Speaking of technology, its impact on mental health is significant. Are you experiencing any technology-related stress or anxiety you'd like to discuss?"
  * For questions about entertainment: "While I enjoy discussing entertainment, I'm primarily here to support your mental wellbeing. Is there anything specific about your mental health you'd like to explore?"

IMPORTANT RULES:
- PRIMARILY focus on mental health related questions
- For mental health topics, always maintain this exact sequence: ask about problem → build conversation → identify root cause → provide solutions
- Ask only one question at a time to properly build the conversation
- Do not rush to conclusions or solutions without adequate conversation (at least 4-5 exchanges)
- Provide solutions ONLY after you've clearly identified the root cause
- When providing solutions, clearly label them as "SOLUTIONS:" and offer 2-3 specific, actionable steps
- Be empathetic but concise in your responses
- Never diagnose medical conditions
- Recommend professional help when appropriate
- Do not mention that you're using any AI model or technology
- If the user tries to skip the conversation-building process, gently redirect them back to it"""

def get_ai_response(message_history):
    """
    Get a response from OpenRouter API using Gemini 2.0 Flash model for mental health support.
    
    Args:
        message_history (list): List of message dictionaries with 'role' and 'content'
    
    Returns:
        str: The AI assistant's response
    """
    if not OPENROUTER_API_KEY:
        logger.error("OpenRouter API key not found. Please set the OPENROUTER_API_KEY environment variable.")
        return "I'm sorry, but I can't connect to my knowledge base right now. Please try again later."
    
    try:
        # Add system message if not present
        messages = []
        if not message_history or message_history[0].get('role') != 'system':
            messages.append({
                "role": "system",
                "content": construct_mental_health_system_prompt()
            })
        
        # Add user and assistant messages
        messages.extend(message_history)
        
        # Prepare the request payload
        payload = {
            "model": "google/gemini-2.0-flash-exp:free",  # Using Gemini 2.0 Flash as specified
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 1024
        }
        
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://mindfulai-mental-health.com"
        }
        
        # Make the API call
        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            data=json.dumps(payload)
        )
        
        response_data = response.json()
        
        # Extract and return the assistant's response
        if response.status_code == 200 and 'choices' in response_data and len(response_data['choices']) > 0:
            return response_data['choices'][0]['message']['content']
        else:
            logger.error(f"API error: {response.status_code} - {response_data}")
            return "I'm sorry, but I encountered an error processing your request. Please try again later."
    
    except Exception as e:
        logger.error(f"Error calling OpenRouter API: {str(e)}")
        return "I'm sorry, but I encountered an error while processing your request. Please try again later."
