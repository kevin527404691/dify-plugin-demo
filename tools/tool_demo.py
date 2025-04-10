from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.entities.model.llm import LLMModelConfig
from dify_plugin.entities.model.message import UserPromptMessage

class ToolDemoTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        print(tool_parameters)
        model_info = tool_parameters.get("model")
        query = tool_parameters.get("query")
        
        print("uu", self.session.dify_plugin_daemon_url)
        
        res = self.session.model.llm.invoke(
            model_config=LLMModelConfig(
                provider=model_info.get("provider"),
                model=model_info.get("model"),
                mode=model_info.get("mode"),
                completion_params=model_info.get("completion_params"),
            ),
            prompt_messages=[UserPromptMessage(content=query)],
            stream=False,
        )
        
        yield self.create_json_message({
            "result": res
        })
