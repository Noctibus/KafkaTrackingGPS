from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import folium
import geopy.distance
import random

app = FastAPI()

def generate_pau_coordinates(num_points, start_point):
    center_lat, center_lon = 43.2951, -0.3708
    coordinates = [start_point]

    for _ in range(1, num_points):
        displacement = random.uniform(0, 10)
        bearing = random.uniform(0, 360)
        new_point = geopy.distance.distance(meters=displacement).destination(point=start_point, bearing=bearing)
        coordinates.append((new_point.latitude, new_point.longitude))
        start_point = (new_point.latitude, new_point.longitude)

    return coordinates

def display_trajectory(coordinates):
    center_lat = sum(coord[0] for coord in coordinates) / len(coordinates)
    center_lon = sum(coord[1] for coord in coordinates) / len(coordinates)

    map_center = folium.Map(location=[center_lat, center_lon], zoom_start=15)

    #for coord in coordinates:
        #folium.Marker(location=coord, popup=str(coord)).add_to(map_center)

    folium.PolyLine(locations=coordinates, color='blue').add_to(map_center)

    return map_center._repr_html_()

@app.get("/generate_trajectory/{num_points}", response_class=HTMLResponse)
async def generate_and_display_trajectory(num_points: int):
    if num_points <= 0:
        raise HTTPException(status_code=400, detail="NUM_POINTS should be greater than 0")

    initial_point = (43.2951, -0.3708)
    pau_coordinates = generate_pau_coordinates(num_points=num_points, start_point=initial_point)
    map_html = display_trajectory(pau_coordinates)

    return HTMLResponse(content=map_html)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
