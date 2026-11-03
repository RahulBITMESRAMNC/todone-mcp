# todone-mcp

A Model Context Protocol (MCP) server for task management, powered by FastMCP,
LangChain, and Groq. Provides tools to create, list, and update to-do tasks
backed by SQLite.

## Tools exposed

- `create_task` — create a new task (title, priority, description)
- `list_tasks` — list all tasks
- `update_task_status` — update status of a task by ID

## Run the server

uv run server.py
# serves MCP on http://127.0.0.1:8000/mcp

## Test the client

uv run client.py

## Stack

Python 3.12+ · FastMCP · LangChain (MCP adapter) · LangChain-Groq · SQLite · uv