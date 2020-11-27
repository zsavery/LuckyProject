class Application:
    def __init__(self, skill, luck, weight_luck):
        self.skill = skill
        self.luck = luck
        self.score = (skill * (1 - weight_luck)) + (luck * weight_luck)

applicant_1 = Application(75, 50, .25)

assert applicant_1.score == 68.75