from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, full_name, email, user_type, password=None, **extra_fields):
        if not full_name:
            raise ValueError("The full_name field must be set")
        if not email:
            raise ValueError("The email field must be set")
        if not user_type:
            raise ValueError("The user_type field must be set")

        email = self.normalize_email(email)
        user = self.model(
            full_name=full_name, email=email, user_type=user_type, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, full_name, email, user_type, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(full_name, email, user_type, password, **extra_fields)

    def create_superuser(self, mobile, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # Set default values for full_name, email, and user_type
        full_name = extra_fields.get("full_name", "Admin")
        email = extra_fields.get("email", "admin@example.com")
        user_type = extra_fields.get("user_type", "admin")

        return self._create_user(
            full_name, email, user_type, password, mobile=mobile, **extra_fields
        )
