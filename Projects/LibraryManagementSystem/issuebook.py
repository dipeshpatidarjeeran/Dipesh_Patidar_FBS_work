class IssueBook:
    def __init__(self, member_id, book_id, issue_date, return_date):
        self.member_id = member_id
        self.book_id = book_id
        self.issue_date = issue_date
        self.return_date = return_date

    def __str__(self):
        return f'{self.member_id}, {self.book_id}, {self.issue_date}, {self.return_date}'