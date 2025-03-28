from fastapi import FastAPI
from crawl4ai import AsyncWebCrawler
import asyncio

app = FastAPI(
    title="Web Crawler API",
    description="A simple API that crawls NBC News business section",
    version="1.0.0"
)

@app.get("/")
async def root(url: str):
    """
    Root endpoint that crawls NBC News business section and returns the markdown content
    """
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(
                url=url,
            )
            return {
                "status": "success",
                "markdown": result.markdown
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# This part is only needed if you want to run the script directly
# FastAPI is typically run with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)