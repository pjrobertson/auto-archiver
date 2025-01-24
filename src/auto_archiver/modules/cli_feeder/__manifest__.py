{
    "name": "CLI Feeder",
    "type": ["feeder"],
    "requires_setup": False,
    "external_dependencies": {
        "python": ["loguru"],
    },
    "configs": {
        "urls": {
            "default": None,
            "help": "URL(s) to archive, either a single URL or a list of urls, should not come from config.yaml",
        },
    },
    "description": """
    Processes URLs to archive passed via the command line and feeds them into the archiving pipeline.

    ### Features
    - Takes a single URL or a list of URLs provided via the command line.
    - Converts each URL into a `Metadata` object and yields it for processing.
    - Ensures URLs are processed only if they are explicitly provided.

    """
}
