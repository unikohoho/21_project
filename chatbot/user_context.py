import pandas as pd

def load_user_profile(user_id: str):
    df = pd.read_csv("../data/user_profiles.csv")
    user_info = df[df['user_id'] == user_id].iloc[0]

    return {
        "child_age": user_info["child_age"],
        "parenting_style": user_info["parenting_style"],
        "parenting_goal": user_info["parenting_goal"],
        "child_traits": user_info["child_traits"],
        "preferred_tone": user_info["preferred_tone"],
        "language": user_info["language"],
        "health_issues": user_info["allergies_or_health_issues"]
    }
