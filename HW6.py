blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

total = 0
trending = 0

for views in blog_views:

    if views > 1000:
        print("Trending")
        trending = trending + 1

    elif views >= 500:
        print("Average")

    else:
        print("Low Traffic")

    total = total + views

print("Total views:", total)
print("Trending posts:", trending)
