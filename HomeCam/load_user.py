import pandas as pd


def load_user_profile(csv_path: str, user_id: str):
    user_df = pd.read_csv(csv_path)
    user_info = user_df[user_df['user_id'] == user_id].iloc[0]
    return {
        "child_age": user_info['child_age'],
        "parenting_style": user_info['parenting_style'],
        "parenting_goal": user_info['parenting_goal'],
        "child_traits": user_info['child_traits'],
        "preferred_tone": user_info['preferred_tone'],
        "language": user_info['language'],
        "health_issues": user_info['allergies_or_health_issues']
    }
