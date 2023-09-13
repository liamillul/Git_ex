monthly_hours = float(input("enter how many hours you worked: "))
hourly_payment = float(input("enter your payment per hour: "))
monthly_salary_without_taxes = monthly_hours*hourly_payment
income_tax = 0.1*monthly_salary_without_taxes
social_security = 0.05*monthly_salary_without_taxes
health_tax = 0.1*social_security
all_the_taxes = income_tax+social_security+health_tax
monthly_salary_after_taxes = monthly_salary_without_taxes-all_the_taxes
print(monthly_salary_after_taxes)
