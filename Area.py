import numpy as np

class Area():
    def __init__(self, center_lat, center_lon, grid_shape=(3, 3), cell_size=0.5):
        """
        Creates Area instance with given parameters
        :param center_lat: Latitude coordinate of central point
        :param center_lon: Longitude coordinate of central point
        :param grid_shape: shape of grid, only odd numbers
        :param cell_size: length between two closest points in grid given in degrees

        Attributes
        center: coordinates of center point, tuple with two elements (lat, lon)
        grid_shape: shape of grid, tuple with two elements
        cell_size: length between two closest points in grid given in degrees
        size: size of area in degrees
        border: values of top, bottom latitudes, and left, right longitudes, tuple with four elements (left_lon,
            top_lat, right_lon, bottom_lat)
        """
        self.center = (center_lat, center_lon)
        self.grid_shape = grid_shape
        self.cell_size = cell_size
        self.size = ((grid_shape[0]-1)*cell_size, (grid_shape[1]-1)*cell_size)
        self.border = (center_lon - self.size[1]/2, center_lat + self.size[0]/2,
                       center_lon + self.size[1]/2, center_lat - self.size[0]/2)
        self.left_border = self.border[0]
        self.top_border = self.border[1]
        self.right_border = self.border[2]
        self.bottom_border = self.border[3]

    def grid_coordinates(self):
        """
        Calculates coordinates of every point in grid
        :return: Numpy array of coordinates, 3 dimension, (row, column, (lat,lon))
        """
        vector_lat = np.zeros((self.grid_shape[0], 1))
        vector_lon = np.zeros((self.grid_shape[1], 1))
        k = 0
        for lat, lon in zip(vector_lat, vector_lon):
            lat = self.top_border - self.cell_size * k
            lon = self.left_border + self.cell_size * k

            vector_lat[k], vector_lon[k] = lat, lon
            k += 1

        vector_lat = vector_lat.T
        vector_lon = vector_lon.T
        matrix_lat = vector_lat
        matrix_lon = vector_lon
        for i in range(self.grid_shape[0]-1):
            matrix_lat = np.vstack([matrix_lat, vector_lat])
            matrix_lon = np.vstack([matrix_lon, vector_lon])


        self.grid_coord_ = np.dstack((matrix_lat.T, matrix_lon))
        return self.grid_coord_