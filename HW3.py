is_logged=True
print("Is_logged:",is_logged)
is_subscribed=False
print("Is_subscribed:",is_subscribed)
user_credits=100
max_credits=200
min_credits=50
credits_valid=(user_credits <=min_credits and user_credits >= max_credits and user_credits != min_credits)
print("Credit_valid:",credits_valid)
bonus_eligible=is_subscribed or (user_credits <=min_credits and not is_subscribed)
print("Bonus_eligible:",bonus_eligible)
user_credits+=50
user_credits=-20
user_credits*=2
user_credits%=120
print(" Final user_credits:",user_credits)
power_result=user_credits**2
print("Power_result:",power_result)
full_access=is_logged and is_subscribed
print("Full_access:",full_access)
is_True_loggin=is_logged is True
print("Is_true_login:",is_True_loggin)
access_result = is_logged or is_subscribed is False
print("Access_result:",access_result)






