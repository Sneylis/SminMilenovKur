class DataMixin:
    def get_user_context(self,**kwargs):
        context = kwargs

        user_ok =self.request.user.is_authenticated

