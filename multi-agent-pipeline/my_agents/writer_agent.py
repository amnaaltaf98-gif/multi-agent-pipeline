from groq_config import client


def writer_agent(research):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a technical writer."
            },
            {
                "role": "user",
                "content": research
            }
        ]
    )

    return response.choices[0].message.content