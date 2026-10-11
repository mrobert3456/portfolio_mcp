from dataclasses import dataclass, field
import logging
from typing import Any
import requests


@dataclass
class Repository:
    id: str
    name: str
    full_name: str
    html_url: str
    description: str | None = None
    topics: list[str] = field(default_factory=list)
    created_at: str = ""
    updated_at: str = ""
    language: str = ""

    @classmethod
    def from_github(cls, data: dict[str, Any]) -> "Repository":
        return cls(
            id=str(data["id"]),
            name=data["name"],
            full_name=data["full_name"],
            html_url=data["html_url"],
            description=data.get("description"),
            topics=data.get("topics", []),
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            language=data.get("language") or "",
        )

    @classmethod
    def list_from_github(cls, repositories: list[dict[str, Any]]) -> list["Repository"]:
        return [cls.from_github(repo) for repo in repositories]
        

class GitHubClient:
    def __init__(self, token: str | None = None):
        self.logger = logging.getLogger("github_client")
        self.headers = {
            "Accept": "application/json",
        }
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def get_user_repositories(self, username: str) -> list[Repository]:
        self.logger.info(f"getting repositories for {username}...")
        response = requests.get(
            f"https://api.github.com/users/{username}/repos",
            headers=self.headers,
        )
        response.raise_for_status()
        repos = Repository.list_from_github(response.json())
        self.logger.info(f"repositories found: {len(repos)}")
        return repos
