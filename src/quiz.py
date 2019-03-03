class Quiz:
    likes = 0
    dislikes = 0

    def results(self):
        if self.likes > self.dislikes:
            return "You like cats!"
        else:
            return "You dislike cats! How could you?!"