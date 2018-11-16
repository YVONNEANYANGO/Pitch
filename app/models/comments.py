class Comment:

    all_comments = []

    def __init__(self,pitch_id):
        self.pitch_id = pitch_id


    def save_comment(self):
        Comment.all_comments.append(self)


    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()
        