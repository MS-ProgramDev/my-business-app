from db import SessionLocal
from models import Requirement, RequirementCondition

# Create a new session
session = SessionLocal()

# Clear existing data
session.query(RequirementCondition).delete()
session.query(Requirement).delete()

# Define requirements
requirements = [
    Requirement(id=1, title="Gas System Approval", description="Approval needed for businesses using gas", action="Submit gas system plan to Ministry of Economy", priority="High"),
    Requirement(id=2, title="Meat Handling License", description="Required if business serves meat", action="Apply for meat license via Ministry of Health", priority="Medium"),
    Requirement(id=3, title="Alcohol Permit", description="Needed for selling alcohol", action="Apply for alcohol permit via Israel Police", priority="High"),
    Requirement(id=4, title="Delivery Registration", description="For delivery-based businesses", action="Register for sanitary oversight", priority="Low"),
    Requirement(id=5, title="Fire Department Approval", description="Fire safety approval required for large spaces", action="Get inspection by fire services", priority="High"),
    Requirement(id=6, title="Accessibility Compliance", description="Business must comply with accessibility regulations", action="Ensure proper ramps and signs", priority="Medium"),
    Requirement(id=7, title="Police Exemption Notice", description="Exempt from police requirements under certain conditions", action="No action required", priority="Low"),
    Requirement(id=8, title="General Sanitation Requirements", description="Every business must adhere to basic hygiene regulations", action="Provide no smoking signs, proper waste treatment, etc.", priority="High"),
]

# Define conditions
conditions = [
    RequirementCondition(requirement_id=1, field_name='uses_gas', operator='=', value='true'),
    RequirementCondition(requirement_id=2, field_name='serves_meat', operator='=', value='true'),
    RequirementCondition(requirement_id=3, field_name='serves_alcohol', operator='=', value='true'),
    RequirementCondition(requirement_id=4, field_name='offers_delivery', operator='=', value='true'),
    RequirementCondition(requirement_id=5, field_name='area', operator='>', value='100'),
    RequirementCondition(requirement_id=6, field_name='seating_capacity', operator='>', value='50'),
    RequirementCondition(requirement_id=7, field_name='seating_capacity', operator='<=', value='200'),
    RequirementCondition(requirement_id=7, field_name='serves_alcohol', operator='=', value='false'),
]

# Add to session
session.add_all(requirements)
session.add_all(conditions)

# Commit
session.commit()
session.close()

print("Requirements seeded successfully.")
