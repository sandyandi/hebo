from typing import Optional


def get_system_prompt(
    context: str, behaviour: str, conversation_summaries: Optional[str] = None
) -> str:
    """
    Constructs the system prompt with behaviour, context, and optional conversation history.

    Args:
        behaviour: String describing how the assistant should behave
        context: String containing scenarios and examples for the assistant
        conversation_summaries: Optional string containing summaries of past conversations

    Returns:
        Formatted system prompt string
    """
    # Start with behaviour
    prompt = f"{behaviour}\n\n"

    # Add context section with instructions
    prompt += """Below you will find context information in the form of scenarios and examples.
Scenarios are sets of instructions on how to handle specific real-world conversation situations.
Examples are conversation samples that should guide you in understanding how to better interact with users.
Please analyze this context carefully and use it to inform your responses:

Context:
{context}

"""

    # Add conversation summaries section if provided
    if conversation_summaries:
        prompt += """Previous conversations have taken place that may be relevant to this interaction.
Below are dense summaries of these past conversations - use this information to maintain continuity
and provide more contextual responses:

{conversation_summaries}

"""

    return prompt.format(
        context=context,
        conversation_summaries=conversation_summaries if conversation_summaries else "",
    )
