from fastapi import FastAPI
import pandas as pd
import asyncio

app = FastAPI(title="Discover Karabakh - Demo API")

async def parse_csv_data(file_path: str):
    def read_data():
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    
    return await asyncio.to_thread(read_data)

@app.get("/api/regions", summary="Regionların siyahısını gətirir")
async def get_regions():
    try:
        regions_data = await parse_csv_data("regions.csv")
        return {
            "status": "success",
            "count": len(regions_data),
            "data": regions_data
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }