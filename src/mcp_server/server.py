from typing import Literal
from uuid import uuid4

from fastmcp import FastMCP

from mcp_server.database import (
        get_all_tasks,
        save_task,
        update_task_status_in_db,
)

mcp=FastMCP("MCP SERVER ACL")

@mcp.tool(name="create_task", description="Create a new to-do task")
def create_task(
    title: str,
    priority: Literal["low", "medium", "high"] = "medium",
    description: str = "",
) -> dict:
    task = {
        "task_id": str(uuid4()),
        "title": title,
        "description": description,
        "priority": priority,
        "status": "todo",
    }
    save_task(task)
    return task


@mcp.tool(name="list_tasks",description="this tool provide all the list of tasks in our database")
def list_tasks()->list[dict]:
    """ This function return all the tasks present in our database"""
    return get_all_tasks()

@mcp.tool(name="update_task_status",description="this tool will update a specific task status based on its ID")
def update_task_status(task_id:str,status:Literal["todo","in_progress","done"])->dict:
    """
    this function will update the status of a specific task based on its ID
    """
    return update_task_status_in_db(task_id,status)





if  __name__=="__main__":
    mcp.run(transport="http",port=8000)
    #create_task("this is second task",description="this is a test")