from groq_config import client


def research_agent(topic):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a research expert."
            },
            {
                "role": "user",
                "content": f"Research: {topic}"
            }
        ]
    )

    return response.choices[0].message.content