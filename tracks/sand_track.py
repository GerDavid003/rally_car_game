from ursina import *

class SandTrack(Entity):
    def __init__(self, car):
        super().__init__(
            model = "sand_track.obj", 
            texture = "sand_track.png", 
            position = (-80, -50, -75), 
            scale = (18, 18, 18), 
            rotation = (0, 270, 0),
            collider = "mesh"
        )

        self.car = car

        self.finish_line = Entity(model = "cube", position = (-50, -50.2, -7), rotation = (0, 0, 0), scale = (3, 8, 30), visible = False)
        self.boundaries = Entity(model = "sand_track_bounds.obj", collider = "mesh", position = (-80, -50, -75), rotation = (0, 270, 0), scale = (18, 50, 18), visible = False)

        self.wall1 = Entity(model = "cube", position = (-75, -50, -48), rotation = (0, 90, 0), collider = "box", scale = (5, 30, 40), visible = False)
        self.wall2 = Entity(model = "cube", position = (-74, -50, -75), rotation = (0, 90, 0), collider = "box", scale = (5, 30, 40), visible = False)
        self.wall3 = Entity(model = "cube", position = (-61, -50, -60), rotation = (0, 0, 0), collider = "box", scale = (5, 30, 40), visible = False)
        self.wall4 = Entity(model = "cube", position = (-90, -50, -60), rotation = (0, 0, 0), collider = "box", scale = (5, 30, 40), visible = False)

        self.wall_trigger = Entity(model = "cube", position = (-100, -50, -114), rotation = (0, 0, 0), scale = (5, 20, 30), visible = False)

        self.cacti = Entity(model = "cacti-sand.obj", texture = "cactus-sand.png", position = (-80, -50, -75), scale = (18, 18, 18), rotation = (0, 270, 0))
        self.rocks = Entity(model = "rocks-sand.obj", texture = "rock-sand.png", position = (-80, -50, -75), scale = (18, 18, 18), rotation = (0, 270, 0))