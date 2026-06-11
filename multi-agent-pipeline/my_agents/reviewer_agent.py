from groq_config import client


def reviewer_agent(article):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
                Review the article.
                Give:
                - Score out of 10
                - Feedback
                - Improved version
                """
            },
            {
                "role": "user",
                "content": article
            }
        ]
    )

    return response.choices[0].message.content