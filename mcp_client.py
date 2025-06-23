#!/usr/bin/env python3

# mcp_client.py
from fastmcp import Client
import click
import asyncio

async def interact_with_server(transport: str, host: str, port: int, use_ssl: bool):
    print("--- Creating Client ---")
    if transport == "stdio":
        client = Client("geo.py")
    elif transport == "sse":
        if use_ssl:
            client = Client(f"https://{host}:{port}")
        else:
            client = Client(f"http://{host}:{port}")
    else:
        raise ValueError(f"Invalid transport: {transport}")

    # print(f"Client configured to connect to: {client.target}")

    try:
        async with client:
            print("--- Client Connected ---")
            tools = await client.list_tools()
            print(f"Available tools: {tools}")
            # Call the 'geocode_location' tool
            result = await client.call_tool("geocode_location", {"location_str": "1600 Amphitheatre Parkway, Mountain View, CA"})
            print(f"geocode_location result: {result}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("--- Client Interaction Finished ---")

@click.command()
@click.option("--transport", type=click.Choice(["stdio", "sse"]), default="sse")
@click.option("--host", type=str, default="localhost")
@click.option("--port", type=int, default=8000)
@click.option("--use-ssl", is_flag=True, default=False)
def main(transport: str, host: str, port: int, use_ssl: bool):
    asyncio.run(interact_with_server(transport=transport, host=host, port=port, use_ssl=use_ssl))

if __name__ == "__main__":
    main()