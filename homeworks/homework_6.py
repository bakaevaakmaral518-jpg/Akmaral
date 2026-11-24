class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


# Порядок родителей: (Mutant, Streamer)
# Обоснование: Для GlowStreamer важнее мутация (он стримит именно как мутант).
# Если поменять местами на (Streamer, Mutant), то первым в MRO окажется Streamer,
# и метод live() будет возвращать стримерское приветствие вместо фразы про свечение.
class GlowStreamer(Mutant, Streamer):

    def ultimate_content(self):
        # Используем методы родителей через self
        return f"Эпичный стрим-мутация: {self.superpower()} и прямо во время трансляции {self.earn().lower()}!"


# Порядок родителей: (TikToker, Mutant)
# Обоснование: ViralCyborg позиционирует себя прежде всего как TikTok-блогер,
# а мутация лишь дополняет его вирусные ролики.
# Если поменять местами на (Mutant, TikToker), то live() начнет выдавать фразу мутанта, а не тиктокера.
class ViralCyborg(TikToker, Mutant):

    def ultimate_content(self):
        # Используем методы родителей через self
        return f"Вирусный киборг в деле: {self.viral()} благодаря тому, что я {self.superpower().lower()}!"


# Порядок родителей: (Streamer, TikToker)
# Обоснование: DonateMage изначально классический стример, который успешно освоил формат коротких роликов.
# Если поменять местами на (TikToker, Streamer), то метод live() сменится с запуска стрима на трендовый тиктокерский.
class DonateMage(Streamer, TikToker):

    def ultimate_content(self):
        return f"Магический донат: {self.earn()}, после чего {self.viral().lower()}!"

if __name__ == "__main__":
    print("=== GlowStreamer ===")
    glow = GlowStreamer()
    print("MRO:", GlowStreamer.mro())
    print("live():", glow.live())
    print("ultimate_content():", glow.ultimate_content())
    print()

    print("=== ViralCyborg ===")
    cyborg = ViralCyborg()
    print("MRO:", ViralCyborg.mro())
    print("live():", cyborg.live())
    print("ultimate_content():", cyborg.ultimate_content())
    print()

    print("=== DonateMage ===")
    mage = DonateMage()
    print("MRO:", DonateMage.mro())
    print("live():", mage.live())
    print("ultimate_content():", mage.ultimate_content())