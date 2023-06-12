from textwrap import dedent
from typing import List
from ..core.main import Step
from ..core.sdk import ContinueSDK
from .core.core import MessageStep


class SimpleChatStep(Step):
    user_input: str
    name: str = "Chat"

    async def run(self, sdk: ContinueSDK):
<<<<<<< Updated upstream
        self.description = sdk.models.gpt35.complete(self.user_input, with_history=await sdk.get_chat_context())
=======
        # TODO: With history
        self.description = ""
        for chunk in sdk.models.gpt35.stream_chat([{"role": "user", "content": self.user_input}]):
            self.description += chunk
            await sdk.update_ui()

        self.name = sdk.models.gpt35.complete(
            f"Write a short title for the following chat message: {self.description}").strip()
>>>>>>> Stashed changes
