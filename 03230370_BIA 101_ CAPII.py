class Employee: #Classes are used to create objects that share similar properties (attributes) and behaviors (methods).
  """Represents an employee with their details and tax calculation methods."""
# provides a brief description of the class's purpose

  def __init__(self, name, income, employee_type, organisation_type): # the init is responsible for initializing the object's attributes (variables).
    self.name = name # A string representing the employee's name
    self.income = income #A numerical value representing the employee's annual income.
    self.employee_type = employee_type # A string indicating the employee's type (e.g., "regular" and  "Contract")
    self.organisation_type = organisation_type #: A string representing the type of organization the employee works for (e.g., "Government ", "private")

  def calculate_deductions(self): # the caluculation_deduction functionis defined to calculate all the deduction
    """Calculates deductions based on employee type and organization type."""
    deductions = 0 # Initializes a variable named deductions to store the total amount of deductions (initially set to 0)

    # NPPF deduction
    if self.employee_type == "Regular" and self.organisation_type != "Government": #The employee must not work for a government organization.
      deductions += 0.10 * self.income # If both conditions are true, it adds a 10% deduction (10/100)

    # GIS deduction
    if self.employee_type == "Regular" and self.organisation_type != "Government":
      deductions += 0.05 * self.income # if the conditions are true, i adds a 5% to deduct

    # Education allowance deduction
    deductions += 350000 # for the eduaction purpose it deduct of 350000

    # Other deductions
    deductions += 0.30 * self.income

    return deductions # if the condtions are true all teh dedctions are being returned 

  def calculate_tax_rate(self, taxable_income):# define a new functions to calculate the tax deduction
    """Calculates the tax rate based on the taxable income."""
    if taxable_income <= 300000:
      return 0 # if the taxable_income is less or greater than the function retruns 0
    elif taxable_income <= 400000:
      return 0.10 * (taxable_income - 300000) # if the taxable_income is between 300000 and 400000  A tax rate of 10% is applied. 
    #The calculation is 0.10 * (taxable_income - 300000). For example, if the taxable income is $350,000, the tax would be $5,000 (0.10 * ($350,000 - $300,000)).
    elif taxable_income <= 650000:
      return 0.15 * (taxable_income - 400000) + 10000 # The tax rate is 15% applied on the income exceeding $400,000. Additionally, a fixed tax amount of $10,000 is added.
      #The calculation is 0.15 * (taxable_income - 400000) + 10000. For example, if the taxable income is $500,000, the tax would be $25,000 (0.15 * ($500,000 - $400,000) + $10,000).
    elif taxable_income <= 1000000: # the tax rate of 20% is applied on the income exceeding 650000, additionaly, a fixed tax amount of 350000 is added.
      return 0.20 * (taxable_income - 650000) + 35000 # the calculation would be 0.20 * (taxable_income - 650000) + 35000
    elif taxable_income <= 1500000:# the tax rate of 25% is applied  ont he incomne exceeding $1500000, addtionally a fixed tax amount of $ 75000 is addes.
      return 0.25 * (taxable_income - 1000000) + 75000 # the claculation would be .25 *( taxable_ income - 1000000)+ 75000
    else: # if all of the function is not fulfilled and the new tax calcualtion would be 30% and it is calculated 0.30 * ( taxable_income - 15000000)+ 125000
      return 0.30 * (taxable_income - 1500000) + 125000

  def calculate_tax(self): # the function is defined to access the employee attributes to the object
    """Calculates the total tax for the employee."""
    deductions = self.calculate_deductions() # fetching of the total deduction to the employee income
    taxable_income = self.income - deductions # finding of the total income after all the deduction 

    tax = self.calculate_tax_rate(taxable_income) #This function is responsible for calculating the tax rate based on the provided taxable income. 
    #The result (tax) is the tax amount before applying any surcharges.
    if tax >= 1000000:# checks whether the deduction is more than 1000000
      tax += tax * 0.10  # Apply surcharge

    return tax # this returns  the tax functionand surcharge


if __name__ == "__main__": # this functions checks the variable
  name = input("What's your name?\n>>> ")
  income = float(input("What's your annual income?\n>>> "))
  employee_type = input("Enter the employee's type (Regular or Contract):\n>>> ")
  organisation_type = input("Enter the organisation's type (Government or Private):\n>>> ")

  employee = Employee(name, income, employee_type, organisation_type)
  total_tax = employee.calculate_tax()
  # the print function is used to ask the details of the employee
  print(f"Total tax applicable at Nu.{income} is Nu.{total_tax}.")
  print(f"Tax for {name} is calculated.")
  print(f"Thank you for Using!")