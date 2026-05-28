from .models import User

class UserRepository:
    def create_user(self, name, email):
        return User.objects.create(name=name, email=email)

    def get_user(self, user_id):
        return User.objects.filter(id=user_id).first()

    def update_user(self, user_id, name, email):
        user = self.get_user(user_id)
        if user:
            user.name = name
            user.email = email
            user.save()
        return user

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            user.delete()
            return True
        return False
    def allUser(self):
        user = User.objects.filter()
        return user
