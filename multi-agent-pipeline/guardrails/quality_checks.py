from agents import (
    output_guardrail,
    GuardrailFunctionOutput
)


@output_guardrail
async def check_minimum_length(
    ctx,
    agent,
    output
):
    text = output.draft

    words = len(text.split())

    return GuardrailFunctionOutput(
        output_info={
            "words": words
        },
        tripwire_triggered=words < 100,
    )