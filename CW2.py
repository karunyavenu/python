book=''' Receipt header'''
book1="Python basics"
price1=450
book2="Data science intro"
price2=600
line1=("Book Title: {} {}".format(book1,price1))
line2=("Book Title: {} {}".format(book2,price2))
Total_price=price1+price2
line3=("Total_price:  {}".format(Total_price))
thankyou="Thank-you"
final=(line1+"\n"+line2+"\n"+line3+"\n"+"\t"+thankyou)
print(final.upper())
