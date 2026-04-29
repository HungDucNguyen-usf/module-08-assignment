# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {"Web Development": 200, "Backend Developer": 250, "Marketing": 80, "Banking": 300, "Accounting": 150}
# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {"company_name": "Limbus Company", "contact_person": "Dante", "email": "ClickClack@gmail.com", "phone": "828-4567"}
customer2 = {"company_name": "Rhodes Pharma", "contact_person": "Amiya", "email": "GOBDoctor@gmail.com", "phone": "132-4589"}
customer3 = {"company_name": "Tracen Academy", "contact_person": "Tazuna", "email": "TrainerA@gmail.com", "phone": "132-2132"}
customer4 = {"company_name": "Hogwarts", "contact_person": "Dumbledore", "email": "IhateHarryPotter@gmail.com", "phone": "019-5678"}
# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {"C001": customer1, "C002": customer2, "C003": customer3, "C004": customer4}
# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
print(customers)
# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
c002_info = customers["C002"] 
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")
print(c002_info)
print(c003_contact)
print(c999_info)
# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
#update phone and create another field
customers["C001"]["phone"] = "243-1932"
customers["C002"]["industry"] = "Web Development"
print(customers["C001"])
print(customers["C002"])
# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here
projects = {
    "C001": [
        {"name": "Backend hotfix", "service": "Backend Developer", "hours": 12, "budget": 4900, "status": "pending"},
        {"name": "Website upscaler", "service": "Web Development", "hours": 13, "budget": 3600, "status": "active"}
    ],
    "C002": [
        {"name": "Fixing code", "service": "Backend Developer", "hours": 12, "budget": 3150, "status": "completed"},
        {"name": "Schedule meetings", "service": "Accounting", "hours": 5, "budget": 3500, "status": "pending"}
    ],
    "C003": [
        {"name": "Spreadsheets filling", "service": "Accounting", "hours": 8, "budget": 3333, "status": "completed"},
        {"name": "Selling", "service": "Marketing", "hours": 8, "budget": 3250, "status": "active"}
        ],
    "C004": [
        {"name": "Total funds", "service": "Banking", "hours": 10, "budget": 5110, "status": "pending"},
        {"name": "Clean text", "service": "Web Development", "hours": 12, "budget": 4990, "status": "completed"}
        ]
    }
# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for plist in projects.values(): #project list
    for p in plist: #projects in project list
        hourly_rate = services[p["service"]] 
        p["cost"] = hourly_rate * p["hours"]
print(projects)
# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
print(list(customers.keys()))
for company in customers.values():
    print(company["company_name"])
print(len(customers))
# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
service_counts = {}
for plist in projects.values():
    for p in plist:
        service = p["service"]
        service_counts[service] = service_counts.get(service,0) + 1
print(f"Project used for each services: {service_counts}")
# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
min_budget = min([p["budget"] for plist in projects.values() for p in plist])
print("-" * 60)
# Add your code here
total_hours = sum(p["hours"] for plist in projects.values() for p in plist) #sum of hours
total_budget = sum([p["budget"] for plist in projects.values() for p in plist]) 
min_budget = min([p["budget"] for plist in projects.values() for p in plist])
avg_budget = total_budget/len([p for plist in projects.values() for p in plist])
max_budget = max([p["budget"] for plist in projects.values() for p in plist])
min_budget = min([p["budget"] for plist in projects.values() for p in plist])
print(f"Total hours: {total_hours}")
print(f"Total budget: ${total_budget}")
print(f"Average budget: ${avg_budget}")
print(f"Max budget: ${max_budget}")
print(f"Min budget: ${min_budget}")
# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
for cid, plist in projects.items():
    total_budget = sum(p["budget"] for p in plist)
    total_hours = sum(p["hours"] for p in plist)
    projects_count = len([p for p in plist]) #total projects
    print(f"{cid} - total budget: ${total_budget}, total hours: {total_hours}, number of projects: {projects_count}") 
# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
adjusted_rates = {service: rate*1.1 for service, rate in services.items()} #increase rate
# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
active_customers = {cid: customers[cid] for cid in projects if cid in customers} #if customer has projects
print(f"Active customers: {active_customers}")
# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()} #dict comprehension each id get a sum
print(f"customers budgets are: {customer_budgets}")
# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
service_tiers = {service: "Premium" if hourly_rates >= 200 #dict comprehension: if >= 200 premium,...
                 else "Standard" if 100 <= hourly_rates <=199
                 else "Basic"
                 for service, hourly_rates in services.items()
                 }
print(service_tiers)
# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
def validate_customer(customers):
    required = {"company_name", "contact_person", "email", "phone"}
    return required.issubset(customers.keys()) #check if it's a subset
for cid, cinfo in customers.items():
    print(cid, validate_customer(cinfo))
# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here
status_counts = {}
for plist in projects.values():
    for p in plist:
        status = p["status"]
        status_counts[status] = status_counts.get(status, 0) + 1 #get status
print(f"statuses of projects: {status_counts}")
# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
def analyze_customer_budgets(projects):
    analysis = {}
    for cid, plist in projects.items():
        total_budget = sum(p["budget"] for p in plist) #total budget
        pcount = len(plist) #projects counts
        average_budget = total_budget/pcount
        analysis[cid] = {"total": total_budget, "average": average_budget, "count": pcount} #put into a dict
    return analysis
print(analyze_customer_budgets(projects))
# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
def recommend_services(customer_id, customers, projects, services):
    past_services = [] #services used
    recommendation = [] 
    max_budget = int(max(p["budget"] for p in projects[customer_id])) #max budget for a customer
    for p in projects[customer_id]:
        if p["service"] not in past_services:
            past_services.append(p["service"]) #if have used -> append
    recommendation = []
    for service, rate in services.items():
        if service not in past_services:
            if 15 * rate <= max_budget: #an approximate budget range
                recommendation.append(service)
    return recommendation
print(recommend_services("C001", customers, projects, services))
    
    
    
    
    
    
    
    