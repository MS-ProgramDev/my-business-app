from models import Requirement, RequirementCondition
import operator

ops = {
    "=": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le
}

def get_matching_requirements(business, session):
    matched = []
    requirements = session.query(Requirement).all()

    for req in requirements:
        conditions = session.query(RequirementCondition).filter_by(requirement_id=req.id).all()
        satisfied = True

        for cond in conditions:
            field_value = getattr(business, cond.field_name)
            if cond.value.lower() in ["true", "false"]:
                target_value = cond.value.lower() == "true"
            else:
                try:
                    target_value = type(field_value)(cond.value)
                except:
                    satisfied = False
                    break

            if not ops[cond.operator](field_value, target_value):
                satisfied = False
                break

        if satisfied:
            matched.append({
                "id": req.id,
                "title": req.title,
                "description": req.description,
                "action": req.action,
                "priority": req.priority
            })

    return matched
