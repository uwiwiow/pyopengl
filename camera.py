import glm

FOV = 45
NEAR = 0.1
FAR = 100


class Camera:
    def __init__(self, app):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(2, 3, 3)
        self.up = glm.vec3(0, 1, 0)
        self.m_view = self.get_view_matrix()
        """view matrix, se encarga de cambiar la posición y orientación de la cámara en relación con el objeto,
        lo que permite al usuario visualizar el objeto desde diferentes ángulos y posiciones."""
        self.m_proj = self.get_projection_matrix()
        """projection matrix, para ajustar la perspectiva y el campo de visión del objeto."""

    def get_view_matrix(self):
        return glm.lookAt(self.position, glm.vec3(0), self.up)

    def get_projection_matrix(self):
        return glm.perspective(FOV, self.aspect_ratio, NEAR, FAR)
