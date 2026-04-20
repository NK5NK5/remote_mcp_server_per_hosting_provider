from __future__ import annotations

import json

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("remote_mcp_server_alpic")


@mcp.tool()
def get_mcp_client_ip() -> str:
    """Return the hosting provider name used by the benchmark server."""
    return json.dumps(
        {
            "mcp_client_ip": "unknown",
            "hosting_provider": "alpic",
        }
    )


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
