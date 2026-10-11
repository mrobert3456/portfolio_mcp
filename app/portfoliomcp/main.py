import logging
from typing import List
from mcp.server.mcpserver import MCPServer, Context
from langchain_core.documents import Document as LangDocument
from tools.cv_search import RetrievalTool
from tools.github import GitHubClient, Repository
from typing import Any


mcp = MCPServer(name = "portfoliomcp")

logger = logging.getLogger("mcp_logger")

@mcp.tool()
async def cv_search(question: str, ctx: Context) -> List[LangDocument]:
    """A simple tool to search cv and return the relevant answer."""
    try:
        await ctx.info("Searching CV...")
        return RetrievalTool().run(question)
    except Exception as e:
        logger.error(str(e))
        raise e

@mcp.tool()
async def github_projects_tool(ctx: Context) -> list[Repository]:
    """A simple tool to fetch github projects."""
    try:
        await ctx.info("Fetching github repositories for mrobert3456... ")
        return GitHubClient().get_user_repositories("mrobert3456")
    except Exception as e:
        logger.error(str(e))
        raise e

@mcp.tool()
def email_preparation_tool(email: str, message: str, name: str) -> Any:
    """A simple tool to prepar email data to the user in a json format."""
    return {
        "name": name,
        "email": email,
        "message": message
    }


def main():
    mcp.run(transport="streamable-http", host="0.0.0.0", stateless_http=True)

if __name__ == "__main__":
    main()
