from app import create_app

#
# class SMS(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     phoneNumber = db.Column(db.Integer, index=True)
#     shortCode = db.Column(db.Integer, index=True)
#     keyword = db.Column(db.String(64), index=True)
#     updateType = db.Column(db.String(64), index=True)
#
#     def __repr__(self):
#         return "SMS {}".format(self.phoneNumber, self.shortCode, self.keyword, self.updateType)
