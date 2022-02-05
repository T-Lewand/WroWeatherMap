

class Area():
    def __init__(self, center_lat, center_lon, grid_shape=(3, 3), cell_size=0.5):
        self.center = (center_lat, center_lon)
        self.size = (grid_shape[0]*cell_size, grid_shape[1]*cell_size)
        self.border = (center_lon - self.size[1]/2, center_lat + self.size[0]/2,
                       center_lon + self.size[1]/2, center_lat + self.size[0]/2)
