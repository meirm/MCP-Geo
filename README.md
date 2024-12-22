# MCP-Geo
Geocoding MCP server with GeoPY!


## 📋 System Requirements


- Python 3.6+

## 📦 Dependencies

Install all required dependencies:

```bash
# Using pip
uv pip install -r requirements.txt
```

### Required Packages
- **fastmcp**: Framework for building Model Context Protocol servers
- **geoPy**: Python library for accessing and geocoding/reverse geocoding locations.


All dependencies are specified in `requirements.txt` for easy installation.

## 📑 Table of Contents
- [System Requirements](#-system-requirements)
- [Dependencies](#-dependencies)
- [MCP Tools](#%EF%B8%8F-mcp-tools)
- [Getting Started](#-getting-started)
- [Installation Options](#-installation-options)
  - [Claude Desktop](#option-1-install-for-claude-desktop)
  - [Elsewhere](#option-2-install-elsewhere)
- [Safety Features](#-safety-features)
- [Development Documentation](#-development-documentation)
- [Environment Variables](#%EF%B8%8F-environment-variables)

## 🛠️ MCP Tools

This MCP server provides the following geocoding tools to Large Language Models (LLMs):

### geocode_location

	•	Takes a user-provided address or place name and returns the best match’s latitude, longitude, and formatted address.

	•	Handles errors gracefully and returns None if the location is not found or if an error occurs.

### reverse_geocode

	•	Takes a latitude and longitude and returns the nearest address.
	•	Useful for finding descriptive information about a point on the map.

### geocode_with_details

	•	Similar to geocode_location but returns additional data such as bounding boxes and more detailed address info, if supported by the geocoder.

### geocode_multiple_locations

	•	Accepts a list of address strings and returns a list of geocoding results (lat/lon/address) for each address.

	•	Rate-limited to avoid hitting geocoding service quotas.

### reverse_geocode_multiple_locations

	•	Accepts a list of [lat, lon] pairs to perform reverse geocoding for each.
	•	Returns a list of dictionaries containing lat, lon, and address or None for unsuccessful lookups, also rate-limited.

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/webcoderz/MCP-Geo.git
cd MCP-Geo
```


## 📦 Installation Options

You can install this MCP server in either Claude Desktop or the Cline VSCode plugin. Choose the option that best suits your needs.

### Option 1: Install for Claude Desktop

Install using FastMCP:

```bash
fastmcp install geo.py --name "MCP Geo"
```

### Option 2: Install elsewhere

To use this server with the [Cline VSCode plugin](http://cline.bot):

1. In VSCode, click the server icon (☰) in the Cline plugin sidebar
2. Click the "Edit MCP Settings" button (✎)
3. Add the following configuration to the settings file:

```json
{
    "mcp-geo": {
        "command": "uv",
        "args": [
        "run",
        "--with",
        "fastmcp",
        "fastmcp",
        "run",
        "MCP-Geo/geo.py"
        ],
        "env": {
        "NOMINATIM_URL": "nominatim.openstreetmap.org"
        }
    }
}
```

Replace `/path/to/repo` with the full path to where you cloned this repository (e.g., `/Users/username/Projects/imessage-query-fastmcp-mcp-server`)

🔒 Safety Features
	•	Rate Limiting: Each geocoding call is rate-limited (e.g., 1-second delay) to avoid excessive requests that violate usage limits.
	•	Error Handling: Catches geopy exceptions (timeouts, service errors) and returns safe None results instead of crashing.

📚 Development Documentation

If you’d like to extend or modify this server:
	•	Check geo.py for how each tool is implemented and how geopy is integrated.
	•	Adjust environment variables to switch providers (Nominatim, ArcGIS, Bing, etc.).
	•	Look at geopy’s official docs for advanced usage like bounding boxes, language settings, or advanced data extraction.

⚙️ Environment Variables

Configure the server using environment variables:

| Variable             | Description                              | Default            |
 |----------------------|------------------------------------------|--------------------|
| `GEOCODER_PROVIDER` (optional)   | "nominatim", "arcgis", or "bing"     | nominatim          |
| `NOMINATIM_URL` (optional)       | Domain for Nominatim | nominatim.openstreetmap.org       |
| `SCHEME` (optional)              | http/https    | http               |
| `ARC_USERNAME` (optional for ArcGIS)        | ArcGIS username            | None               |
| `ARC_PASSWORD` (optional for ArcGIS)        | ArcGIS password      | None               |
| `BING_API_KEY` (required for Bing)        | Your Bing Maps key.      | None               |

These can be set in your shell or in the MCP settings file for your environment. If more are needed just edit geo.py and add them in to whichever geocoder you are using.