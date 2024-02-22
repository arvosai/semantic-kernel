# Copyright (c) Microsoft. All rights reserved.
from typing import List, Optional

from openai.types.chat import ChatCompletion

from semantic_kernel.connectors.ai.open_ai.models.chat_completion.function_call import FunctionCall
from semantic_kernel.connectors.ai.open_ai.models.chat_completion.tool_calls import ToolCall
from semantic_kernel.contents import ChatMessageContent


class OpenAIChatMessageContent(ChatMessageContent):
    """This is the class for OpenAI chat message response content.

    Args:
        inner_content: ChatCompletion - The inner content of the response,
            this should hold all the information from the response so even
            when not creating a subclass a developer can leverage the full thing.
        ai_model_id: Optional[str] - The id of the AI model that generated this response.
        metadata: Dict[str, Any] - Any metadata that should be attached to the response.
        role: ChatRole - The role of the chat message.
        content: Optional[str] - The text of the response.
        encoding: Optional[str] - The encoding of the text.
        function_call: Optional[FunctionCall] - The function call that was generated by this response.
        tool_calls: Optional[List[ToolCall]] - The tool calls that were generated by this response.

    Methods:
        __str__: Returns the content of the response.
    """

    inner_content: ChatCompletion
    function_call: Optional[FunctionCall] = None
    tool_calls: Optional[List[ToolCall]] = None

    @staticmethod
    def ToolIdProperty():
        # Directly using the class name and the attribute name as strings
        return f"{ToolCall.__name__}.{ToolCall.id.__name__}"
