from marshmallow import Schema, fields
from enum import Enum


class Skill(object):

    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __repr__(self):
        return f'<Skill(name="{self.name}", points="{self.points}")>'


class SkillSchema(Schema):
    name = fields.Str()
    points = fields.Int()


class Experience(object):
    def __init__(self, company_name, description, start_date, end_date):
        self.company_name = company_name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f'<Experience(company_name="{self.company_name}", company_name="{self.description}")>'


class ExperienceSchema(Schema):
    company_name = fields.Str()
    description = fields.Str()
    start_date = fields.DateTime(format="%Y-%m-%d")
    end_date = fields.DateTime(format="%Y-%m-%d")


class CV(object):
    def __init__(self, skill, experience):
        self.skills = skill
        self.experiences = experience

    def __repr__(self):
        return f'<CV(skill="{self.skills}", experience="{self.experiences}")>'


class CVSchema(Schema):
    skills = fields.List(fields.Nested(SkillSchema))
    experiences = fields.List(fields.Nested(ExperienceSchema))


class User(object):
    def __init__(self, name, password, email, account_type, cv):
        self.name = name
        self.password = password
        self.email = email
        self.account_type = account_type
        self.password = password
        self.cv = cv

    def __repr__(self):
        return f'<User(name="{self.name}")>'


class AccountType(Enum):
    EMPLOYEE = "EMPLOYEE"
    STAFF = "STAFF"
    ADMIN = "ADMIN"


class UserSchema(Schema):
    name = fields.Str()
    password = fields.Str()
    email = fields.Str()
    account_type = fields.Str()
    cv = fields.Nested(CVSchema)

