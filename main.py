from flask import Flask, request, Blueprint
from datetime import datetime

from models import Skill, SkillSchema
from models import Experience, ExperienceSchema
from models import CV, CVSchema
from models import User, UserSchema, AccountType

app = Flask(__name__)

SKILLS = [
    Skill("Python", 3),
    Skill("HTML", 5),
    Skill("CSS", 6),
    Skill("AWS", 8),
    Skill("AWS", 1),
]

EXPERIENCES = [
    Experience("Xebia", "admin", datetime(2019, 1, 1), datetime(2022, 1, 1)),
    Experience("PGS", "devops", datetime(2010, 10, 1), datetime(2022, 1, 12)),
]

CVS = [
    CV(SKILLS[0:2], [EXPERIENCES[0]]),
    CV(SKILLS[1:3], [EXPERIENCES[1]]),
]

USERS = [
    User(
        "Jacek Placek",
        "jacek123",
        "kochamplacki@email.com",
        AccountType.EMPLOYEE,
        CVS[0]
    ),
    User(
        "Piotrus Pan",
        "hak",
        "pp@email.com",
        AccountType.STAFF,
        CVS[1]
    ),
    User(
        "Masta Disasta",
        "admin123",
        "admin@email.com",
        AccountType.ADMIN,
        None
    ),
]


@app.route('/user/', methods=['GET'])
def get_users():
    schema = UserSchema(many=True)
    users = schema.dump(USERS)
    return users


@app.route('/user/<int:user_id>/cv', methods=['GET'])
def user_get_cv(user_id):
    schema = CVSchema(many=False)
    cv = schema.dump(USERS[user_id].cv)
    return cv


@app.route('/user/<int:user_id>/skill', methods=['POST'])
def user_add_skill(user_id):
    obj = SkillSchema().load(request.get_json())
    USERS[user_id].cv.skills.append(obj)
    return "", 204


@app.route('/user/<int:user_id>/skill/<int:skill_id>', methods=['PUT'])
def user_update_skill(user_id, skill_id):
    obj = SkillSchema().load(request.get_json())
    USERS[user_id].cv.skills[skill_id] = obj


@app.route('/user/<int:user_id>/skill/<int:skill_id>', methods=['DELETE'])
def user_delete_skill(user_id, skill_id):
    USERS[user_id].cv.skills.pop(skill_id)
    return "", 204


@app.route('/user/<int:user_id>/experience', methods=['POST'])
def user_add_experience(user_id):
    obj = ExperienceSchema().load(request.get_json())
    USERS[user_id].cv.experiences.append(obj)
    return "", 204


@app.route('/user/<int:user_id>/experience/<int:experience_id>', methods=['PUT'])
def user_update_experience(user_id, experience_id):
    obj = ExperienceSchema().load(request.get_json())
    USERS[user_id].cv.experiences[experience_id] = obj
    return "", 204


@app.route('/user/<int:user_id>/experience/<int:experience_id>', methods=['DELETE'])
def user_delete_experience(user_id, experience_id):
    USERS[user_id].cv.experiences.pop(experience_id)
    return "", 204


@app.route('/skill/skill-average', methods=['GET'])
def statistics_skill_average():
    skill_points = {}
    skill_count = {}
    for skill in SKILLS:
        if skill.name in skill_points:
            skill_points[skill.name] += skill.points
            skill_count[skill.name] += 1
        else:
            skill_points[skill.name] = skill.points
            skill_count[skill.name] = 1
    skill_average = {}
    for (name, points), (_, count) in \
            zip(skill_points.items(), skill_count.items()):
        skill_average[name] = points/count

    return skill_average


@app.route('/skill/skill-summary', methods=['GET'])
def statistics_skill_summary():

    skill_count = {}
    for user in USERS:
        if not user.cv:
            continue
        for skill in user.cv.skills:

            if str(skill) in skill_count:
                skill_count[str(skill)] += 1
            else:
                skill_count[str(skill)] = 1

    return skill_count


if __name__ == "__main__":
    app.run(debug=True)
