has_account=True
email_verified=False
can_login=has_account and email_verified 
print("Can_login:",can_login)
email="anu@gamil.com"
is_email_valid="@" in email
print("Email valid:",is_email_valid)
user_age=17
is_age_valid=user_age>=18
print("Age valid:",is_age_valid)
can_login_final=(has_account and email_verified and is_email_valid and is_age_valid)
print("Final_login:",can_login_final)
print("Hasa ccount is true:",has_account is True)

