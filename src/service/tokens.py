from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, school_team_object, timestamp):
        return (
            six.text_type(school_team_object.pk) + six.text_type(timestamp) + six.text_type(school_team_object.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()
