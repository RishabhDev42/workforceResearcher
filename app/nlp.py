import os
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Precompute reference embedding
REFERENCE_TOPICS = [
    "AI in the workforce",
    "artificial intelligence and jobs",
    "impact of AI at work",
    "AI replacing jobs",
    "AI improving productivity",
    "automation and employment",
    "machine learning in business",
    "future of work with AI",
    "AI tools for professionals",
    "ethical implications of AI in workplace",
    "AI-driven decision making",
    "AI and job market trends",
    "AI augmenting human tasks",
    "Workforce adaptation to AI technologies",
    "Reskilling for AI and automation",
    "Impact of AI on job market trends",
    "Digital transformation and AI",
    "Robotics in the workplace",
    "AI in job recruitment",
    "Fear of losing job to technology",
    "Technology replacing workers",
    "Concerns about automation",
    "Using AI to enhance work efficiency",
    "Using AI in business processes",
    "Using AI in workplace productivity",
    "Sentiment around AI in the workplace",
    "Sentiment around AI replacing jobs",
    "Sentiment around AI improving work",
    "Sentiment around AI tools",
]

AI_KEYWORDS = [
    "artificial intelligence", "ai", "machine learning", "deep learning",
    "automation", "neural network", "chatgpt", "large language model", "copilot",
    "robotics", "intelligent systems", "data science", "predictive analytics",
    "natural language processing", "computer vision", "algorithm", "smart technology",
    "cursor", "digital assistant", "intelligent automation", "AI tools"
]

def get_embedding(text: str) -> list:
    """Generate embedding using OpenAI API."""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Precompute topic embeddings
TOPIC_EMBEDDINGS = [get_embedding(t) for t in REFERENCE_TOPICS]

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def is_ai_related(message: str, threshold: float = 0.5) -> bool:
    """Check if message is semantically related to AI in workforce."""
    msg_embedding = get_embedding(message)
    similarities = [cosine_similarity(msg_embedding, ref) for ref in TOPIC_EMBEDDINGS]
    return (max(similarities) >= threshold) or (any(keyword in message.lower() for keyword in AI_KEYWORDS))
