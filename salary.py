
salary = float(input("Enter Salary: ₹"))


bonus_salary = salary + (salary * 0.10)


final_salary = bonus_salary - (bonus_salary * 0.05)


print(f"Original Salary: ₹{int(salary)}")
print(f"Bonus Added: ₹{int(bonus_salary)}")
print(f"After Tax Deduction: ₹{int(final_salary)}")
