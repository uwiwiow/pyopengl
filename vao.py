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

        # shadow cube vao
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cube']
        )

        # cat1 vao
        self.vaos['cat_1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat_1']
        )

        # shadow cat1 vao
        self.vaos['shadow_cat_1'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cat_1']
        )

        # cat2 vao
        self.vaos['cat_2'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat_2']
        )

        # shadow cat2 vao
        self.vaos['shadow_cat_2'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cat_2']
        )

        # cat3 vao
        self.vaos['cat_3'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat_3']
        )

        # shadow cat3 vao
        self.vaos['shadow_cat_3'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cat_3']
        )

        # steve vao
        self.vaos['steve'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['steve']
        )

        # shadow steve vao
        self.vaos['shadow_steve'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['steve']
        )

        # skybox vao
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox']
        )

        # advanced skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.programs['advanced_skybox'],
            vbo=self.vbo.vbos['advanced_skybox']
        )

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
