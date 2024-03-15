def authenticate_team_member(school_team_object,  name, surname):
    team_member = None

    if school_team_object.first_member.member_name == name and school_team_object.first_member.member_surname == surname:
        team_member = school_team_object.first_member
    elif school_team_object.second_member.member_name == name and school_team_object.second_member.member_surname == surname:
        team_member = school_team_object.second_member
    return team_member
