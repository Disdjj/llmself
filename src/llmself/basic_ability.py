# -*-coding:utf-8 -*-
class BasicAbility:
    def think(self, query: str, *args, **kwargs):
        return self

    def can_infer(self, query: str, *args, **kwargs):
        return self

    def infer(self, query: str, *args, **kwargs):
        return self

    def generate_text(self, query: str, *args, **kwargs):
        return self