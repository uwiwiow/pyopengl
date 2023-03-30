from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cube']
        )

        # cat1 vao
        self.vaos['cat_1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat_1']
        )

        # cat2 vao
        self.vaos['cat_2'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat_2']
        )

        # cat2 vao
        self.vaos['cat_3'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat_3']
        )

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
